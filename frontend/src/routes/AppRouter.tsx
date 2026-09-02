import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Home from "../pages/Home";
import Chat from "../pages/Chat/Chat";
import Subjects from "../pages/Subjects/Subjects";
import Practice from "../pages/Practice/Practice";
import Progress from "../pages/Progress/Progress";
import Settings from "../pages/Settings/Settings";
import Profile from "../pages/Profile/Profile";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          {/* Temporary: Chat is the home page while we build it */}
          <Route path="/" element={<Chat />} />

          <Route path="/home" element={<Home />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/subjects" element={<Subjects />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="/progress" element={<Progress />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/profile" element={<Profile />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}