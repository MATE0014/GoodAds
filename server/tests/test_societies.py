# ...tests for societies endpoints...
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

from app.db.base import Base
from app.db.session import get_db
from app.core.security import hash_password, create_access_token
from app import models

# --- 1) Create an in-memory SQLite engine + session factory for testing ---
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- 2) Override the get_db dependency to use our testing session ---
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# --- 3) Create all tables in SQLite before running tests ---
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    # create tables
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# --- 4) Helper to register & login a test society user and return Bearer token ---
@pytest.fixture
def auth_token():
    db = TestingSessionLocal()
    # create a test society user
    test_user = models.User(
        username="test_society",
        email="society@example.com",
        hashed_password=hash_password("secret123"),
        user_type="society",
    )
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    db.close()

    # create JWT token
    token = create_access_token({"sub": str(test_user.id)})
    return f"Bearer {token}"

# --- 5) Instantiate TestClient once per module ---
@pytest.fixture
def client():
    return TestClient(app)

# --- 6) Tests start here ---

def test_list_empty_societies(client):
    """When no societies exist, GET /societies/ should return []"""
    r = client.get("/api/v1/societies/")
    assert r.status_code == 200
    assert r.json() == []

def test_create_society_unauthenticated(client):
    """POST /societies/ without token is 401"""
    payload = {"name": "Chess Club", "description": "We love chess!", "logo_url": None}
    r = client.post("/api/v1/societies/", json=payload)
    assert r.status_code == 401  # not authenticated

def test_create_society_forbidden_for_business(client, auth_token):
    """Only user_type='society' can create — if we simulate a 'business' token it 403s"""
    # create a business user token
    db = TestingSessionLocal()
    biz = models.User(
        username="biz_user",
        email="biz@example.com",
        hashed_password=hash_password("abc123"),
        user_type="business",
    )
    db.add(biz)
    db.commit()
    db.refresh(biz)
    db.close()
    biz_token = create_access_token({"sub": str(biz.id)})
    headers = {"Authorization": f"Bearer {biz_token}"}

    payload = {"name": "Biz Society", "description": "N/A"}
    r = client.post("/api/v1/societies/", json=payload, headers=headers)
    assert r.status_code == 403
    assert r.json()["detail"] == "Only society users can create societies"

def test_create_and_read_society(client, auth_token):
    """Create a society, then GET it back by ID and in list"""
    headers = {"Authorization": auth_token}
    payload = {
        "name": "Drama Club",
        "description": "All about acting.",
        "logo_url": "http://example.com/logo.png"
    }
    # Create
    r = client.post("/api/v1/societies/", json=payload, headers=headers)
    assert r.status_code == 200
    created = r.json()
    assert created["name"] == payload["name"]
    assert created["id"] > 0
    society_id = created["id"]

    # Read single
    r2 = client.get(f"/api/v1/societies/{society_id}")
    assert r2.status_code == 200
    assert r2.json() == created

    # Read list
    r3 = client.get("/api/v1/societies/")
    assert r3.status_code == 200
    lst = r3.json()
    assert isinstance(lst, list)
    assert any(s["id"] == society_id for s in lst)

def test_update_and_delete_society(client, auth_token):
    """Update the society you own, then delete it"""
    headers = {"Authorization": auth_token}
    # First, create one
    payload = {"name": "Music Club", "description": "We play tunes."}
    r = client.post("/api/v1/societies/", json=payload, headers=headers)
    society = r.json()
    sid = society["id"]

    # Update only works if you own it
    update_payload = {"name": "Music Ensemble", "description": "Classical tunes."}
    r2 = client.put(f"/api/v1/societies/{sid}", json=update_payload, headers=headers)
    assert r2.status_code == 200
    assert r2.json()["name"] == "Music Ensemble"

    # Attempt update as another user (should 403)
    # create a second society user
    db = TestingSessionLocal()
    other = models.User(
        username="other_soc",
        email="other@example.com",
        hashed_password=hash_password("pw123"),
        user_type="society",
    )
    db.add(other); db.commit(); db.refresh(other); db.close()
    other_token = create_access_token({"sub": str(other.id)})
    r3 = client.put(f"/api/v1/societies/{sid}", json=update_payload, headers={"Authorization": f"Bearer {other_token}"})
    assert r3.status_code == 403

    # Delete as owner
    r4 = client.delete(f"/api/v1/societies/{sid}", headers=headers)
    assert r4.status_code == 200
    assert r4.json() == {"ok": True}

    # Ensure it’s gone
    r5 = client.get(f"/api/v1/societies/{sid}")
    assert r5.status_code == 404
