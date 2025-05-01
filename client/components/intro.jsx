"use client";

const Intro = () => {
  return (
    <div className="relative w-full h-[65vh] bg-[url('/intro-bg.jpg')] bg-cover bg-[center_5%] grid grid-cols-2 px-10">
      {/* Color Overlay */}
      <div className="absolute inset-0 bg-[rgba(99,195,221,0.61)] z-0" />

      {/* Content Layer */}
      <div className="grid grid-rows-2 relative z-10 pt-0">
        {/* Title */}
        <h1 className="text-secondary text-6xl font-bold font-outfit leading-tight drop-shadow-[0_2px_2px_rgba(0,0,0,0.25)] pl-8 pt-8 m-0">
          Welcome to <br /> The GoodAds
        </h1>

        {/* Description */}
        <p className="text-[#197099] font-semibold text-2xl pl-8 pt-0 m-0">
          We're building the future of brand collaborations — a vibrant marketplace where college societies meet forward-thinking businesses to create innovative, niche-driven content.
        </p>
      </div>

      {/* Image Section (spanning 2 rows) */}
      <div className="relative z-10 flex items-start justify-end row-span-2 m-0 p-0">
        <img
          src="/intro graphic.png"
          alt="Intro Graphic"
          className="w-[452px] h-[432px]"
        />
      </div>

      {/* Third Row Section - Absolutely Positioned Tagline */}
      <div className="absolute top-[327px] left-[236px] flex items-center z-20">
        {/* Earth Icon */}
        <img
          src="/earth illus.png"
          alt="Small Icon"
          className="w-[95px] h-[95px] mr-4"
        />

        {/* Tagline */}
        <div className="flex items-center space-x-2">
          <span className="text-base text-secondary font-bold font-outfit">For The</span>
          <span className="text-3xl font-extrabold text-white font-outfit">Creators</span>
          <span className="text-base text-secondary font-bold font-outfit">, By The</span>
          <span className="text-3xl font-extrabold text-white font-outfit">Creators</span>
        </div>
      </div>
    </div>
  );
};

export default Intro;
