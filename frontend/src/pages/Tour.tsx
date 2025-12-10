import { useState, useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { fetchTour, fetchTheme } from "@/lib/api";
import { TourSize, MuseumTheme, MuseumObject } from "@/types";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { ArrowLeft, MapIcon, ListIcon, Loader2 } from "lucide-react";
import Layout from "@/components/Layout";
import MuseumMap from "@/components/MuseumMap";
import { useToast } from "@/components/ui/use-toast";

const Tour = () => {
  const { themeId, size } = useParams<{ themeId: string; size: TourSize }>();
  const navigate = useNavigate();
  const { toast } = useToast();
  
  const [theme, setTheme] = useState<MuseumTheme | null>(null);
  const [objects, setObjects] = useState<MuseumObject[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadData = async () => {
      if (!themeId || !size) return;
      
      try {
        setLoading(true);
        // Load theme and tour objects in parallel
        const [themeData, tourObjects] = await Promise.all([
          fetchTheme(themeId),
          fetchTour(themeId, size)
        ]);
        
        setTheme(themeData);
        setObjects(tourObjects);
      } catch (err) {
        console.error("Failed to load tour:", err);
        setError("Failed to load tour data. Please try again.");
        toast({
          variant: "destructive",
          title: "Error",
          description: "Could not load tour details.",
        });
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [themeId, size, toast]);

  if (loading) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-64">
          <Loader2 className="h-8 w-8 animate-spin" />
        </div>
      </Layout>
    );
  }

  if (error || !theme || objects.length === 0) {
    return (
      <Layout>
        <div className="text-center">
          <h2 className="text-2xl font-bold">{error || "Tour not found"}</h2>
          <Button onClick={() => navigate("/")} className="mt-4">
            Back to Themes
          </Button>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div>
        <Button variant="ghost" onClick={() => navigate(`/theme/${themeId}`)} className="mb-4">
          <ArrowLeft className="mr-2 h-4 w-4" />
          Back to Size Selection
        </Button>
        <h1 className="text-3xl font-bold">{theme.name} Tour</h1>
        <p className="text-xl text-gray-600">{size} Itinerary</p>
      </div>

      <Tabs defaultValue="list" className="mt-6">
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="list"><ListIcon className="mr-2 h-4 w-4" />Itinerary</TabsTrigger>
          <TabsTrigger value="map"><MapIcon className="mr-2 h-4 w-4" />Map</TabsTrigger>
        </TabsList>
        <TabsContent value="list">
          <Card>
            <CardHeader>
              <CardTitle>Suggested Route</CardTitle>
            </CardHeader>
            <CardContent>
              <ol className="space-y-4">
                {objects.map((obj, index) => (
                  <li key={obj.id} className="flex items-start space-x-4">
                    <div className="flex-shrink-0 w-8 h-8 bg-gray-800 text-white rounded-full flex items-center justify-center font-bold text-lg">
                      {index + 1}
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">{obj.title}</h3>
                      <p className="text-gray-600">{obj.galleryLocation}</p>
                      <p className="mt-1 text-sm">{obj.shortDescription}</p>
                       <Link
                        to={`/object/${obj.id}`}
                        state={{ backLink: `/tour/${themeId}/${size}` }}
                        className="text-blue-600 hover:underline text-sm mt-1 inline-block"
                      >
                        View Details
                      </Link>
                    </div>
                  </li>
                ))}
              </ol>
            </CardContent>
          </Card>
        </TabsContent>
        <TabsContent value="map">
          <Card>
            <CardHeader>
              <CardTitle>Museum Map</CardTitle>
            </CardHeader>
            <CardContent>
              <MuseumMap objects={objects} />
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </Layout>
  );
};

export default Tour;