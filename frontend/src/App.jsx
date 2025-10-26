// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProtectedRoute from "./components/protectedRoutes";
import Navbar from "./components/Navbar";
import Quiz from "./pages/Quiz";
import Result from "./pages/Result";
import SavedCareers from "./pages/SavedCareers";
import CareerDetails from "./pages/CareerDetails";
import ProfilePage from "./pages/ProfilePage";
import AuthPage from "./pages/Auth";


// Pages
import Home from "./pages/Home";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Router>
        <Navbar />

        <main>
         
          <Routes>
  {/* Public page */}
  <Route path="/auth" element={<AuthPage />} />

  <Route path="/" element={<Home />} />

  {/* Protected pages */}
  <Route path="/quiz" element={<ProtectedRoute> <Quiz /> </ProtectedRoute>}/>
  <Route path="/results" element={ <ProtectedRoute> <Result /> </ProtectedRoute>}/>
  <Route path="/saved-careers" element={ <ProtectedRoute> <SavedCareers /> </ProtectedRoute>}/>
  <Route path="/career-details" element={ <ProtectedRoute> <CareerDetails /> </ProtectedRoute>}/>
  <Route path="/profile" element={<ProtectedRoute> <ProfilePage /> </ProtectedRoute> }/>
  </Routes>

        </main>
      </Router>
    </div>
  );
}

