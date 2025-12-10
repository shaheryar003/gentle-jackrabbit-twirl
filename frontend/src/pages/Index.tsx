import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { fetchThemes } from "@/lib/api";
import { MuseumTheme } from "@/types";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import Layout from "@/components/Layout";
import { WelcomeModal } from "@/components/WelcomeModal";
import { Skeleton } from "@/components/ui/skeleton";

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
};

const cardVariants = {
  hidden: { y: 20, opacity: 0 },
  visible: {
    y: 0,
    opacity: 1,
    transition: {
      type: "spring" as const,
      stiffness: 100,
    },
  },
};

const Index = () => {
  const [themes, setThemes] = useState<MuseumTheme[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isWelcomeModalOpen, setIsWelcomeModalOpen] = useState(false);

  useEffect(() => {
    const loadThemes = async () => {
      try {
        const data = await fetchThemes();
        setThemes(data);
      } catch (err) {
        setError("Failed to load themes. Please try again later.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    loadThemes();
  }, []);

  useEffect(() => {
    const hasVisited = localStorage.getItem("hasVisitedMuseumApp");
    if (!hasVisited) {
      setIsWelcomeModalOpen(true);
    }
  }, []);

  const handleCloseModal = () => {
    localStorage.setItem("hasVisitedMuseumApp", "true");
    setIsWelcomeModalOpen(false);
  };

  return (
    <Layout>
      <WelcomeModal isOpen={isWelcomeModalOpen} onClose={handleCloseModal} />
      <div className="text-center mb-12">
        <h1 className="text-4xl font-extrabold tracking-tight lg:text-5xl">
          Discover the Collection
        </h1>
        <p className="mt-4 text-xl text-gray-600">
          Select a theme to begin your personalized tour.
        </p>
      </div>
      
      {loading ? (
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
           {[1, 2, 3, 4, 5, 6].map((i) => (
             <Card key={i} className="h-full">
               <CardHeader>
                 <Skeleton className="w-full h-40 rounded-t-lg" />
                 <Skeleton className="h-6 w-3/4 pt-4" />
               </CardHeader>
               <CardContent>
                 <Skeleton className="h-4 w-full mb-2" />
                 <Skeleton className="h-4 w-5/6" />
               </CardContent>
             </Card>
           ))}
        </div>
      ) : error ? (
        <div className="text-center text-red-500">
          <p>{error}</p>
        </div>
      ) : (
        <motion.div
          className="grid gap-8 md:grid-cols-2 lg:grid-cols-3"
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          {themes.map((theme) => (
            <motion.div key={theme.id} variants={cardVariants}>
              <Link to={`/theme/${theme.id}`} className="group">
                <Card className="h-full transition-all duration-200 group-hover:shadow-xl group-hover:-translate-y-1">
                  <CardHeader>
                    <img src={theme.image} alt={theme.name} className="w-full h-40 object-cover rounded-t-lg bg-gray-200" />
                    <CardTitle className="pt-4">{theme.name}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <CardDescription>{theme.description}</CardDescription>
                  </CardContent>
                </Card>
              </Link>
            </motion.div>
          ))}
        </motion.div>
      )}
    </Layout>
  );
};

export default Index;