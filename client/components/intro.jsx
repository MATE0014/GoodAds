"use client";

import Image from "next/image";

export default function Intro() {
  return (
    <section className="w-full py-16 bg-[#a8e0f0]">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          <div className="space-y-6">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-[#1a5173]">
              Welcome to
              <br />
              The GoodAds
            </h1>
            <p className="text-[#1a5173] text-lg max-w-xl">
              We're building the future of brand collaborations! a vibrant marketplace where college societies meet
              forward-thinking businesses to create innovative, niche-driven content.
            </p>

            <div className="flex items-center space-x-2 mt-8">
              <div className="relative">
                <div className="w-12 h-12 relative -top-4 left-0">
                  <Image
                    src="/earth illus.png"
                    alt="Globe icon"
                    width={50}
                    height={50}
                    className="object-contain"
                  />
                </div>
              </div>
              <div className="absolute">
                <p className="text-[#1a5173] text-2xl md:text-3xl font-medium ml-4">
                  For the <span className="text-white font-semibold drop-shadow-md">Creators</span>, By the{" "}
                  <span className="text-white font-semibold drop-shadow-md">Creators</span>
                </p>
              </div>
            </div>
          </div>

          <div className="flex justify-center lg:justify-end">
            <div className="relative w-full max-w-md">
              <Image
                src="/intro graphic.png"
                alt="Person pointing at screen with lightbulb"
                width={400}
                height={400}
                className="object-contain"
              />
            </div>
          </div>
        </div>
        <div className="pt-8">
              <p className="text-[#1a5173] font-extrabold mb-4">Trusted By:</p>
              <div className="bg-[#8fd4e8] p-4 rounded-lg flex flex-wrap justify-between items-center gap-4">
                <Image
                  src="/iitk-logo.png"
                  alt="IIT KANPUR"
                  width={120}
                  height={50}
                  className="object-contain"
                />
                <Image
                  src="/fc-logo.png"
                  alt="FAST COMPANY"
                  width={120}
                  height={50}
                  className="object-contain"
                />
                <Image
                  src="/mit-logo.png"
                  alt="MIT"
                  width={80}
                  height={50}
                  className="object-contain"
                />
                <Image
                  src="/forbes-logo.png"
                  alt="Forbes"
                  width={120}
                  height={50}
                  className="object-contain"
                />
              </div>
            </div>
      </div>
    </section>
  )
}
