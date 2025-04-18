import { Raleway } from "next/font/google";
import "./globals.css";

const raleway = Raleway({
  subsets: ["latin"],
  weight: ["100","200","300", "400","500","600", "700"],
  variable: "--font-raleway",
});

export const metadata = {
  title: "The GoodAds",
  description: "A Title Description To Go Here!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={raleway.variable}
      >
        {children}
      </body>
    </html>
  );
}