import { Raleway, Inter } from "next/font/google";
import "./globals.css";

const raleway = Raleway({
  subsets: ["latin"],
  weight: ["100","200","300", "400","500","600", "700"],
  variable: "--font-raleway",
});

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-inter",
});

export const metadata = {
  title: "The GoodAds",
  description: "A Title Description To Go Here!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${raleway.variable} ${inter.variable}`}>
      <body>
        {children}
      </body>
    </html>
  );
}