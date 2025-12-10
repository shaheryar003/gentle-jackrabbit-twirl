export type TourSize = "Small" | "Medium" | "Large";

export interface MuseumTheme {
  id: string;
  name: string;
  description: string;
  image: string;
}

export interface MuseumObject {
  id: string;
  title: string;
  shortDescription: string;
  contextualBackground: string;
  galleryLocation: string;
  image: string;
  themeIds: string[];
  mapPosition: { top: string; left: string };
}

export interface Tour {
  themeId: string;
  size: TourSize;
  objectIds: string[];
}