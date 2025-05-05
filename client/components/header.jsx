"use client";

import Image from "next/image";
import Link from "next/link";
import { FiArrowRight } from "react-icons/fi";
import { FaCaretDown } from "react-icons/fa";
import { useState } from "react";

// Reusable Dropdown Component
const Dropdown = ({ title, menuItems }) => {
const [isOpen, setIsOpen] = useState(false);
let closeTimeout = null;

const handleMouseEnter = () => {
  if (closeTimeout) clearTimeout(closeTimeout);
  setIsOpen(true);
};

const handleMouseLeave = () => {
  closeTimeout = setTimeout(() => {
    setIsOpen(false);
  }, 80); //80ms delay so that the menu doesn't close immediately when hovering over it
};

  return (
    <div
      className="relative group"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <button className="flex items-center gap-1 text-gray-700">
        {title} <FaCaretDown size={14} />
      </button>
      <div
        className={`absolute top-full left-0 mt-2 w-44 bg-white shadow-md rounded-md py-2 z-10 ${
          isOpen ? "block" : "hidden"
        } group-hover:block`}
      >
        {menuItems.map((item, index) => (
          <Link
            key={index}
            href={item.href}
            className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
          >
            {item.label}
          </Link>
        ))}
      </div>
    </div>
  );
};

const Header = () => {
  return (
    <header className="bg-white shadow-md px-6 py-4 flex items-center justify-between h-20">
      {/* Logo here */}
      <div className="flex items-center h-full pl-12">
        <Link href="/">
          <Image
            src="/logo/our-logo.png"
            alt="The GoodAds"
            width={100}
            height={100}
            className="object-contain"
          />
        </Link>
      </div>

      {/* Navbar here */}
      <nav className="hidden md:flex gap-6 text-[#15325a] text-lg font-medium font-outfit">
        <Link href="/">Home</Link>

        <Dropdown
          title="About Us"
          menuItems={[
            { label: "Our Story", href: "/about#story" },
            { label: "Team", href: "/about#team" },
          ]}
        />

        <Dropdown
          title="Our Services"
          menuItems={[
            { label: "College Societies", href: "/collegesocieties" },
            { label: "Companies / Startups", href: "/businesses" },
          ]}
        />

        <Dropdown
          title="Contact Us"
          menuItems={[
            { label: "Support", href: "/contact#support" },
            { label: "Sales", href: "/contact#sales" },
          ]}
        />
      </nav>

      {/* Login/Signup buttons */}
      <div className="font-inter pr-12">
        <Link
          href="/login"
          className="flex font-outfit items-center gap-2 px-4 py-2 bg-accent text-white rounded-[4px] text-lg transition-colors"
        >
          Login / Signup
          <FiArrowRight size={16} />
        </Link>
      </div>
    </header>
  );
};

export default Header;
