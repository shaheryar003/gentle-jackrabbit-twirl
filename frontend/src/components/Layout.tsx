import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Landmark, LogOut, User, WifiOff } from "lucide-react";
import { Button } from "@/components/ui/button";

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [userEmail, setUserEmail] = useState<string | null>(null);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const navigate = useNavigate();

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem("access_token");
      if (token) {
        try {
          const response = await fetch("http://localhost:8000/api/v1/users/me", {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          if (response.ok) {
            const data = await response.json();
            setUserEmail(data.email);
          } else {
            // Token invalid or expired
            localStorage.removeItem("access_token");
            setUserEmail(null);
          }
        } catch (error) {
          console.error("Auth check failed:", error);
          setUserEmail(null);
        }
      }
    };

    checkAuth();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setUserEmail(null);
    navigate("/");
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {!isOnline && (
        <div className="bg-yellow-600 text-white px-4 py-2 text-center text-sm font-medium flex items-center justify-center space-x-2">
          <WifiOff className="h-4 w-4" />
          <span>You are offline. Showing cached content.</span>
        </div>
      )}
      <header className="bg-white shadow-sm">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <Link to="/" className="flex items-center space-x-2">
              <Landmark className="h-8 w-8 text-gray-800" />
              <span className="text-xl font-semibold text-gray-800">
                Museum Thematic Tours
              </span>
            </Link>
            <div className="flex items-center space-x-4">
              {userEmail ? (
                <div className="flex items-center space-x-4">
                  <div className="flex items-center space-x-2 text-sm text-gray-600">
                    <User className="h-4 w-4" />
                    <span>{userEmail}</span>
                  </div>
                  <Button variant="ghost" size="sm" onClick={handleLogout}>
                    <LogOut className="h-4 w-4 mr-2" />
                    Logout
                  </Button>
                </div>
              ) : (
                <Link to="/login">
                  <Button variant="default" size="sm">
                    Login
                  </Button>
                </Link>
              )}
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  );
};

export default Layout;