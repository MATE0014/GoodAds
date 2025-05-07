"use client";

import Image from "next/image";
import Link from "next/link";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-regular-svg-icons";
import { z } from "zod";

// Zod schema for login form
const loginSchema = z.object({
  email: z.string().email("Please enter a valid email address."),
  password: z.string().min(8, "Password must be at least 8 characters."),
});

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    const result = loginSchema.safeParse({ email, password });

    if (!result.success) {
      const errors = result.error.flatten().fieldErrors;
      setEmailError(errors.email?.[0] || "");
      setPasswordError(errors.password?.[0] || "");
      return;
    }

    setEmailError("");
    setPasswordError("");
    console.log({ email, password });

    setEmail("");
    setPassword("");
  };

  return (
    <div className="relative min-h-screen grid grid-cols-12 overflow-hidden">
      {/* Left Illus */}
      <div className="col-span-2 lg:col-span-3 -ml-3 hidden md:flex items-center justify-center bg-white">
        <Image
          src="/illustrations/login illus1.png"
          alt="img1"
          width={466}
          height={600}
        />
      </div>

      {/* Login Form */}
      <div className="col-span-12 md:col-span-8 lg:col-span-6 flex flex-col items-center justify-center px-6 py-10 bg-white">

        <div className="overflow-hidden mb-2">
          <Image
            src="/logo/our-logo.png"
            alt="Logo"
            width={140}
            height={85}
            className="object-contain"
          />
        </div>

        <h1 className="text-2xl font-semibold font-outfit text-black mb-2">Log In</h1>

        <p className="mb-6 text-base font-outfit text-[#00000066]">
          Don't have an account yet?{" "}
          <Link href="/signup" className="text-[#009dc9] font-outfit hover:underline">
            Sign up
          </Link>
        </p>

        {/* Google Apple SignIn */}
        <div className="w-full max-w-md space-y-4 mb-6">
          <button className="font-outfit font-normal flex items-center justify-center w-full border border-[#999999] bg-[#f8f8f8] rounded-[100px] py-2 hover:bg-gray-100 text-black shadow-[0_4px_12px_rgba(0,0,0,0.3)]">
            <Image
              src="/logo/google-logo.png"
              alt="Google"
              width={30}
              height={20}
              className="mr-2"
            />
            Continue with Google
          </button>
          <button className="font-outfit font-normal text-black flex items-center justify-center w-full border border-[#999999] bg-[#f8f8f8] rounded-[100px] py-2 hover:bg-gray-100 shadow-[0_4px_12px_rgba(0,0,0,0.3)]">
            <Image
              src="/logo/apple-logo.png"
              alt="Apple"
              width={20}
              height={20}
              className="mr-2"
            />
            Continue with Apple
          </button>
        </div>

        {/* Divider */}
        <div className="flex items-center w-full max-w-md mb-6">
          <hr className="flex-grow border-[#dcdcdc]" />
          <span className="px-2 text-base font-outfit font-medium text-[#00000066]">OR</span>
          <hr className="flex-grow border-[#dcdcdc]" />
        </div>

        {/* login Form */}
        <form className="w-full max-w-md space-y-4" onSubmit={handleSubmit}>
          {/* Email */}
          <div className="flex flex-col space-y-1">
            <label className="text-black font-outfit text-sm">Email</label>
            <input
              type="text"
              placeholder="user@goodads.in"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full border border-[#dcdcdc] rounded-xl px-4 py-2 text-black"
            />
            {emailError && (
              <span className="text-red-500 text-xs font-outfit">{emailError}</span>
            )}
          </div>
          {/* Password */}
          <div className="flex flex-col space-y-1">
            <label className="text-black font-outfit text-sm">Password</label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full border border-[#dcdcdc] rounded-xl px-4 py-2 text-black pr-10"
              />
              <button
                type="button"
                onClick={() => setShowPassword((prev) => !prev)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"
              >
                <FontAwesomeIcon icon={showPassword ? faEyeSlash : faEye} />
              </button>
            </div>
            {passwordError && (
              <span className="text-red-500 text-xs font-outfit font-normal">{passwordError}</span>
            )}
          </div>
          {/* Forgot Password */}
          <div className="text-right">
            <Link
              href="/forgot-password"
              className="text-base font-outfit font-normal text-[#D74848] hover:underline"
            >
              Forgot password?
            </Link>
          </div>

          {/* Submit & Home Buttons */}
          <button
            type="submit"
            className="w-full bg-[#11aad4] border border-[#11aad4] text-white py-2 rounded-[40px] hover:text-[#11aad4] hover:bg-white hover:border hover:border-[#11aad4] font-outfit font-semibold transition duration-300"
          >
            Sign In
          </button>
          <Link
            href="/"
            className="block mt-2 w-full text-center text-base font-outfit text-[#11aad4] bg-white border border-[#11aad4] py-2 rounded-[40px] hover:bg-[#11aad4] hover:text-white transition duration-300"
          >
            Back to Home
          </Link>
        </form>
      </div>

      {/* Right Illus */}
      <div className="col-span-2 lg:col-span-3 hidden md:flex items-center justify-center bg-white">
        <Image
          src="/illustrations/login illus2.png"
          alt="img2"
          width={1250}
          height={100}
          className="absolute top-0 right-0 z-50 pointer-events-none"
          priority
        />
      </div>
    </div>
  );
}
