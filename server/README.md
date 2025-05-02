```plaintext
good_ads_backend/
├── app/
│   ├── api/                 # API route handlers (CRUD endpoints)
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   └── societies.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/                # Configuration, environment variables
│   │   └── config.py
│   ├── models/              # SQLAlchemy ORM models
│   │   └── society.py
│   ├── schemas/             # Pydantic schemas (request and response models)
│   │   └── society.py
│   ├── crud/                # Database operations (CRUD functions)
│   │   └── society.py
│   ├── db/                  # Database session, connection, migrations
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   ├── main.py              # FastAPI app instance
│   └── __init__.py
├── alembic/                 # For database migrations
├── tests/                   # Test cases
│   └── test_societies.py
├── .env                     # Environment variables (DB URL, SECRET_KEY, etc.)
├── requirements.txt         # Python dependencies
├── Dockerfile               # (for production dockerizing)
├── docker-compose.yml       # ( using Docker Compose)
└── README.md                # Project documentation
```



| Folder/File      | Purpose                                                         |
| ---------------- | --------------------------------------------------------------- |
| `app/api/`     | All your API routes (endpoints for societies, maybe later auth) |
| `app/core/`    | Configuration: database settings, secret keys, etc.             |
| `app/models/`  | Database ORM models using SQLAlchemy                            |
| `app/schemas/` | Pydantic models for request and response bodies                 |
| `app/crud/`    | Functions that directly interact with the DB                    |
| `app/db/`      | Database session setup and base classes                         |
| `alembic/`     | Auto-manage database migrations                                 |
| `tests/`       | Test cases for APIs                                             |
| `.env`         | Secrets (like DB URL, secret keys, etc.)                        |
| `main.py`      | Launches the FastAPI app                                        |



DB Session management
client -> FastAPI -> Depends(get_db) -> creates session -> uses -> closes after

change that will allow you to create graphs inline using Mermaid syntax, for example:

```mermaid
flowchart TB
 subgraph Frontend["Frontend"]
    direction TB
        NXApp["Next.js App"]
        components["Various Components"]
        configs["Configurations"]
  end
 subgraph Backend["Backend"]
    direction TB
        APIService["FastAPI Service"]
        elements["Essential Elements"]
  end
 subgraph Database["Database"]
    direction TB
        DB["PostgreSQL Database"]
        Alembic["Alembic Migrations"]
  end
 subgraph Infrastructure["Infrastructure"]
    direction TB
        Docker["Docker Configuration"]
  end
    NXApp --> components & configs
    Browser["Browser (End User)"] -- HTTPS --> NXApp
    APIService --> elements
    NXApp -- REST API calls --> APIService
    APIService -- SQLAlchemy --> DB
    Alembic --> DB
    Infrastructure --> Docker
    Docker --> APIService & DB
    Browser --> n1["Untitled Node"]

     Browser:::frontend
     NXApp:::frontend
     components:::frontend
     configs:::frontend
     APIService:::backend
     elements:::backend
     DB:::db
     Alembic:::backend
     Docker:::infra
    classDef frontend fill:#cce5ff,stroke:#333,stroke-width:1px
    classDef backend fill:#d4edda,stroke:#333,stroke-width:1px
    classDef db fill:#fff3cd,stroke:#333,stroke-width:1px
    classDef infra fill:#f8d7da,stroke:#333,stroke-width:1px
    click components "https://github.com/shopnobanerjee/the-good-ads/blob/main/client"
    click configs "https://github.com/shopnobanerjee/the-good-ads/blob/main/client"
    click elements "https://github.com/shopnobanerjee/the-good-ads/blob/main/server"
    click DB "https://github.com/shopnobanerjee/the-good-ads/tree/main/server"
    click Alembic "https://github.com/shopnobanerjee/the-good-ads/tree/main/server/alembic"
    click Docker "https://github.com/shopnobanerjee/the-good-ads/tree/main/server"
```
