import { useState, useEffect } from "react";
import { useParams, useNavigate, useLocation } from "react-router-dom";
import { fetchObject } from "@/lib/api";
import { MuseumObject } from "@/types";
import { Button } from "@/components/ui/button";
import { ArrowLeft, Loader2 } from "lucide-react";
import Layout from "@/components/Layout";
import { useToast } from "@/components/ui/use-toast";

const ObjectDetail = () => {
  const { objectId } = useParams<{ objectId: string }>();
  const navigate = useNavigate();
  const location = useLocation();
  const { toast } = useToast();

  const [museumObject, setMuseumObject] = useState<MuseumObject | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadObject = async () => {
      if (!objectId) return;

      try {
        setLoading(true);
        const data = await fetchObject(objectId);
        setMuseumObject(data);
      } catch (err) {
        console.error("Failed to fetch object:", err);
        setError("Failed to load object details.");
        toast({
          variant: "destructive",
          title: "Error",
          description: "Could not load object details.",
        });
      } finally {
        setLoading(false);
      }
    };

    loadObject();
  }, [objectId, toast]);

  if (loading) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-64">
          <Loader2 className="h-8 w-8 animate-spin" />
        </div>
      </Layout>
    );
  }

  if (error || !museumObject) {
    return (
      <Layout>
        <div className="text-center">
          <h2 className="text-2xl font-bold">{error || "Object not found"}</h2>
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
        <Button
          variant="ghost"
          onClick={() => {
            if (location.state?.backLink) {
              navigate(location.state.backLink);
            } else {
              navigate(-1);
            }
          }}
          className="mb-4"
        >
          <ArrowLeft className="mr-2 h-4 w-4" />
          Back
        </Button>
        <div className="grid md:grid-cols-2 gap-8">
          <div>
            <img src={museumObject.image} alt={museumObject.title} className="w-full h-auto rounded-lg shadow-lg bg-gray-200" />
          </div>
          <div className="space-y-4">
            <h1 className="text-4xl font-bold tracking-tight">{museumObject.title}</h1>
            <p className="text-lg font-medium text-gray-700">{museumObject.galleryLocation}</p>
            <p className="text-gray-600">{museumObject.contextualBackground}</p>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ObjectDetail;