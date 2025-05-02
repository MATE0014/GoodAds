"use client";

const wwd = () => {
  return (
    <section className="relative">
      {/* Bg img */}
      <div
        className="absolute inset-0 bg-[url('/backgrounds/wwd-bg.jpg')] bg-cover bg-center opacity-80 pointer-events-none"
        style={{ minHeight: '100%', height: '100%', width: '100%' }}
        aria-hidden="true"
      />

      {/* Component content */}
      <div className="relative z-10 bg-text bg-opacity-90 text-white py-16 px-4 md:px-12">
        <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-center mb-8 font-outfit">
          What We Do?
        </h2>

        {/* WWD- Row 1 */}
        <div className="max-w-4xl mx-auto text-center mb-0">
          <p className="text-lg md:text-xl font-semibold">
            Whether you're a brand looking to tap into fresh, creative energy or a student group eager to showcase your talent to real-world clients, The GoodAds is your launchpad.
          </p>
        </div>

        {/* WWD- Row 2 */}
        <div className="grid grid-cols-1 md:grid-cols-2 items-center gap-8 mt-4">
          <div className="relative z-0">
            <div className="absolute inset-0 bg-[#1986A4] opacity-30 blur-2xl rounded-full z-0" />
            <div className="p-6 relative z-10">
              <p className="text-white text-4xl font-medium ml-6 font-outfit">
                We<span className="text-white text-5xl font-semibold drop-shadow-md"> Connect </span>businesses<br />with student creators
              </p>
              <p className="pt-8 pl-6 font-normal text-2xl">
                We bridge the gap between innovative companies and the brightest college talent. We match you with the right student teams to drive real, actionable results tailored to your industry needs.
              </p>
            </div>
          </div>

          <div className="flex justify-center overflow-hidden">
            <img
              src="/illustrations/illus2whatwedo.png"
              alt="Illustration 1"
              className="w-[800px] h-[500px] object-contain rounded-lg"
            />
          </div>
        </div>

        {/* WWD- Row 3 */}
        <div className="grid grid-cols-1 md:grid-cols-2 items-center gap-8 mt-4">
          <div className="flex justify-center overflow-hidden">
            <img
              src="/illustrations/illus whatwedo.png"
              alt="Illustration 2"
              className="w-[600px] h-[500px] object-contain rounded-lg"
            />
          </div>

          <div className="relative z-0">
            <div className="absolute inset-0 bg-[#1986A4] opacity-30 blur-2xl rounded-full z-0" />
            <div className="p-6 relative z-10">
              <p className="text-white text-4xl font-medium ml-6 font-outfit">
                We<span className="text-white text-5xl font-semibold drop-shadow-md"> Support </span>businesses<br />across industries
              </p>
              <p className="pt-8 pl-6 font-normal text-2xl">
                From finance and consulting to marketing, tech, and multimedia production, we provide companies with agile, cost-effective solutions through the creativity of student societies. 
              </p>
            </div>
          </div>
        </div>

        {/* Our Services */}
        <div className="mt-20">
          <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-center mb-8 font-outfit">
            Our Services To
          </h2>
        </div>
      </div>
    </section>
  );
};

export default wwd;
