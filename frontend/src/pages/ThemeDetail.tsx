import { useState, useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { fetchTheme } from "@/lib/api";
import { MuseumTheme } from "@/types";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ArrowLeft } from "lucide-react";
import Layout from "@/components/Layout";
import { Skeleton } from "@/components/ui/skeleton";

const TourSizes = ["Small", "Medium", "Large"];

const ThemeDetail = () => {
  const { themeId } = useParams<{ themeId: string }>();
  const navigate = useNavigate();
  const [theme, setTheme] = useState<MuseumTheme | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadTheme = async () => {
      if (!themeId) return;
      try {
        const data = await fetchTheme(themeId);
        setTheme(data);
      } catch (err) {
        setError("Failed to load theme details.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    loadTheme();
  }, [themeId]);

  if (loading) {
    return (
      <Layout>
        <div className="space-y-8">
          <div>
            <Skeleton className="h-10 w-32 mb-4" />
            <Skeleton className="h-12 w-3/4 mb-4" />
            <Skeleton className="h-6 w-full" />
          </div>
          <Card>
            <CardHeader>
               <Skeleton className="h-8 w-48 mb-2" />
               <Skeleton className="h-4 w-64" />
            </CardHeader>
            <CardContent className="grid gap-4 md:grid-cols-3">
              {[1, 2, 3].map((i) => (
                <Skeleton key={i} className="h-24 w-full" />
              ))}
            </CardContent>
          </Card>
        </div>
      </Layout>
    );
  }

  if (error || !theme) {
    return (
      <Layout>
        <div className="text-center">
          <h2 className="text-2xl font-bold">{error || "Theme not found"}</h2>
          <Button onClick={() => navigate("/")} className="mt-4">
            Back to Themes
          </Button>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-8">
        <div>
          <Button variant="ghost" onClick={() => navigate("/")} className="mb-4">
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Themes
          </Button>
          <h1 className="text-4xl font-bold tracking-tight">{theme.name}</h1>
          <p className="mt-2 text-lg text-gray-600">{theme.description}</p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Choose Your Tour Size</CardTitle>
            <CardDescription>Select how many objects you'd like to see.</CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4 md:grid-cols-3">
            {TourSizes.map((size) => (
              <Link key={size} to={`/tour/${theme.id}/${size}`}>
                <Button className="w-full h-24 text-xl">{size}</Button>
              </Link>
            ))}
          </CardContent>
        </Card>
      </div>
    </Layout>
  );
};

export default ThemeDetail;