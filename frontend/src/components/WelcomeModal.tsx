import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Landmark, ListChecks, Map } from "lucide-react";

interface WelcomeModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const WelcomeModal = ({ isOpen, onClose }: WelcomeModalProps) => {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle className="text-2xl text-center">Welcome to the Museum!</DialogTitle>
          <DialogDescription className="text-center pt-2">
            Discover the collection with your own personalized tour in three simple steps.
          </DialogDescription>
        </DialogHeader>
        <div className="space-y-4 py-4">
          <div className="flex items-center space-x-4">
            <div className="p-2 bg-gray-100 rounded-full"><Landmark className="h-6 w-6 text-gray-700" /></div>
            <div>
              <h3 className="font-semibold">1. Choose a Theme</h3>
              <p className="text-sm text-gray-600">Select a topic that interests you.</p>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <div className="p-2 bg-gray-100 rounded-full"><ListChecks className="h-6 w-6 text-gray-700" /></div>
            <div>
              <h3 className="font-semibold">2. Pick a Tour Size</h3>
              <p className="text-sm text-gray-600">Decide how many objects you want to see.</p>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <div className="p-2 bg-gray-100 rounded-full"><Map className="h-6 w-6 text-gray-700" /></div>
            <div>
              <h3 className="font-semibold">3. Follow the Map</h3>
              <p className="text-sm text-gray-600">Enjoy your custom-made itinerary!</p>
            </div>
          </div>
        </div>
        <DialogFooter>
          <Button onClick={onClose} className="w-full">Get Started</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};