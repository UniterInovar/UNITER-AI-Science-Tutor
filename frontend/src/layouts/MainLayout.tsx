import { Outlet } from "react-router-dom";

import Navbar from "../components/Navbar/Navbar";
import Sidebar from "../components/Sidebar/Sidebar";
import Footer from "../components/Footer/Footer";

export default function MainLayout() {
  return (
    <>
      <Navbar />

      <div
        style={{
          display: "flex",
          minHeight: "calc(100vh - 70px)",
        }}
      >
        <Sidebar />

        <main
          style={{
            flex: 1,
            padding: "40px",
            background: "#f5f7fb",
          }}
        >
          <Outlet />
        </main>
      </div>

      <Footer />
    </>
  );
}