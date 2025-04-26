"use client";

import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Button, buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import MobileNav from "./mobileNav";

const navLinks = [
  { name: "Home", path: "/" },
  { name: "Our Services", path: "/services" },
  { name: "About Us", path: "/about" },
  { name: "Blog", path: "/blog" },
];

const Header = () => {
  const pathname = usePathname();

  return (

    /* Column based design for the header */
    <header className="w-full mt-4 px-2 sm:px-4 lg:px-8">
      <div className="bg-white shadow-md rounded-2xl max-w-7xl mx-auto h-20 grid grid-cols-12 items-center px-4">

        {/* Logo - takes 4 columns on mobile, 3 on desktop */}
        <div className="col-span-4 lg:col-span-3 flex items-center h-full overflow-hidden">
          <Link href="/">
            <Image
              src="/logo-nobg.png"
              alt="The GoodAds"
              width={100}
              height={100}
              className="object-contain"
              priority
            />
          </Link>
        </div>

        {/* Center Nav Links (only on lg+) - takes 6 columns */}
        <nav className="hidden lg:flex justify-center gap-3 col-span-6 mb-[0.6rem]">
          {navLinks.map((link) => {
            const isActive = pathname === link.path;
            return (
              <Link key={link.path} href={link.path}>
                <div
                  className={cn(
                    buttonVariants({
                      variant: isActive ? "default" : "outline",
                      size: "default",
                    }),
                    "rounded-full text-sm"
                  )}
                >
                  {link.name}
                </div>
              </Link>
            );
          })}
        </nav>

        {/* Right side - takes 8 columns on mobile (pushes content right), 3 on desktop */}
        <div className="col-span-8 lg:col-span-3 flex justify-end items-center mb-[0.6rem]">

          {/* Show on large screens */}
          <div className="hidden lg:flex items-center gap-2">
            <Link href="/login">
              <Button variant="outline" size="default">
                Dashboard
              </Button>
            </Link>
          </div>

          {/* Show only on mobile */}
          <div className="flex lg:hidden w-full justify-end">
            <MobileNav />
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;