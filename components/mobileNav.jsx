"use client";

import { useState } from "react";
import {
  Sheet,
  SheetContent,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { usePathname } from "next/navigation";
import Link from "next/link";
import { CiMenuFries } from "react-icons/ci";

const navLinks = [
  { name: "Home", path: "/" },
  { name: "Our Services", path: "/services" },
  { name: "About Us", path: "/about" },
  { name: "Blog", path: "/blog" },
];

const MobileNav = () => {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();

  const handleCloseWithDelay = () => {
    setTimeout(() => setIsOpen(false), 300); // subtle delay to allow smooth transition
  };

  return (
    <Sheet open={isOpen} onOpenChange={setIsOpen}>
      <SheetTrigger
        onClick={() => setIsOpen(true)}
        className="flex justify-center items-center"
      >
        <CiMenuFries className="text-[32px] text-primary" />
      </SheetTrigger>

      <SheetContent className="flex flex-col">
        {/* Hidden for accessibility only */}
        <SheetTitle className="sr-only">Navigation</SheetTitle>

        {/* Mobile Logo */}
        <div className="mt-16 mb-12 text-center text-3xl font-semibold">
          <Link href="/" onClick={handleCloseWithDelay}>
            TheGoodAds
          </Link>
        </div>

        {/* Nav Links */}
        <nav className="flex flex-col items-center gap-6">
          {navLinks.map((link, index) => {
            const isActive = pathname === link.path;
            return (
              <Link
                key={index}
                href={link.path}
                onClick={handleCloseWithDelay}
                className={`text-lg font-medium capitalize transition-colors ${
                  isActive
                    ? "text-primary border-b-2 border-primary"
                    : "hover:text-primary"
                }`}
              >
                {link.name}
              </Link>
            );
          })}
        </nav>

        {/* Auth Buttons */}
        <div className="mt-10 flex flex-col items-center gap-3">
          <Link href="/login" onClick={handleCloseWithDelay}>
            <button className="w-40 py-2 border border-gray-300 rounded-full hover:bg-gray-100 transition">
              Log In
            </button>
          </Link>
          <Link href="/signup" onClick={handleCloseWithDelay}>
            <button className="w-40 py-2 bg-primary text-white rounded-full hover:bg-primary/90 transition">
              Sign Up
            </button>
          </Link>
        </div>
      </SheetContent>
    </Sheet>
  );
};

export default MobileNav;
