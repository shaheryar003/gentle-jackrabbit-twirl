import { MuseumTheme, MuseumObject, Tour, TourSize } from "@/types";

const themes: MuseumTheme[] = [
  {
    id: "roman-empire",
    name: "The Roman Empire",
    description: "Explore the might and majesty of ancient Rome, from its military conquests to its intricate society.",
    image: "https://placehold.co/600x400/A3BFFA/000000?text=Roman+Empire",
  },
  {
    id: "ancient-egypt",
    name: "Ancient Egypt",
    description: "Uncover the mysteries of the pharaohs, their gods, and the enduring legacy of a civilization along the Nile.",
    image: "https://placehold.co/600x400/FFD700/000000?text=Ancient+Egypt",
  },
  {
    id: "renaissance-art",
    name: "Renaissance Art",
    description: "Witness the rebirth of art and culture in Europe, featuring masterpieces of unparalleled beauty and skill.",
    image: "https://placehold.co/600x400/D1B48C/000000?text=Renaissance+Art",
  },
  {
    id: "ancient-greece",
    name: "Ancient Greece",
    description: "Journey back to the cradle of Western civilization and discover the art, philosophy, and politics of the ancient Greeks.",
    image: "https://placehold.co/600x400/B0E0E6/000000?text=Ancient+Greece",
  },
];

const objects: MuseumObject[] = [
  // Roman Empire
  {
    id: "obj-01",
    title: "Legionary Helmet",
    shortDescription: "A standard issue helmet for a Roman legionary.",
    contextualBackground: "The Galea, or Roman helmet, was a critical piece of equipment for the Roman soldier. Its design evolved over centuries, providing protection from swords, arrows, and other battlefield threats. This particular piece dates back to the 1st century AD and shows signs of use in campaign.",
    galleryLocation: "Floor 1, Room 3",
    image: "https://placehold.co/800x600/94a3b8/ffffff?text=Legionary+Helmet",
    themeIds: ["roman-empire"],
    mapPosition: { top: "25%", left: "15%" },
  },
  {
    id: "obj-02",
    title: "Bust of Augustus",
    shortDescription: "A marble bust of the first Roman Emperor, Augustus.",
    contextualBackground: "This portrait of Augustus, the founder of the Roman Empire, captures the idealized and calm expression typical of Augustan art. It was used as a powerful tool of political propaganda, distributed throughout the empire to promote his image as a strong and benevolent ruler.",
    galleryLocation: "Floor 1, Room 3",
    image: "https://placehold.co/800x600/a1a1aa/ffffff?text=Bust+of+Augustus",
    themeIds: ["roman-empire"],
    mapPosition: { top: "28%", left: "20%" },
  },
  {
    id: "obj-03",
    title: "Roman Coin Hoard",
    shortDescription: "A collection of silver denarii.",
    contextualBackground: "Coin hoards like this one provide invaluable information about the Roman economy, trade routes, and the movement of armies. This collection was found buried in a ceramic pot, likely hidden for safekeeping during a period of unrest.",
    galleryLocation: "Floor 1, Room 4",
    image: "https://placehold.co/800x600/a3a3a3/ffffff?text=Roman+Coins",
    themeIds: ["roman-empire"],
    mapPosition: { top: "35%", left: "30%" },
  },
  // Ancient Egypt
  {
    id: "obj-04",
    title: "Rosetta Stone",
    shortDescription: "The key to deciphering Egyptian hieroglyphs.",
    contextualBackground: "Discovered in 1799, the Rosetta Stone is inscribed with a decree issued at Memphis, Egypt, in 196 BC on behalf of King Ptolemy V. The decree appears in three scripts: Ancient Egyptian hieroglyphs, Demotic script, and Ancient Greek, which made it possible to finally understand hieroglyphs.",
    galleryLocation: "Floor 2, Room 10",
    image: "https://placehold.co/800x600/737373/ffffff?text=Rosetta+Stone",
    themeIds: ["ancient-egypt"],
    mapPosition: { top: "50%", left: "55%" },
  },
  {
    id: "obj-05",
    title: "Sarcophagus of Seti I",
    shortDescription: "An intricately carved alabaster sarcophagus.",
    contextualBackground: "This magnificent sarcophagus was made for Pharaoh Seti I. It is adorned with texts from the Book of Gates, a sacred text describing the journey of the soul through the underworld. Although the pharaoh's mummy was not found inside, it remains a masterpiece of Egyptian funerary art.",
    galleryLocation: "Floor 2, Room 12",
    image: "https://placehold.co/800x600/ca8a04/ffffff?text=Sarcophagus",
    themeIds: ["ancient-egypt"],
    mapPosition: { top: "55%", left: "65%" },
  },
  {
    id: "obj-06",
    title: "Canopic Jars",
    shortDescription: "Vessels used in the mummification process.",
    contextualBackground: "Canopic jars were used by the ancient Egyptians during the mummification process to store and preserve the viscera of their owner for the afterlife. They were commonly carved from limestone or made of pottery.",
    galleryLocation: "Floor 2, Room 12",
    image: "https://placehold.co/800x600/eab308/ffffff?text=Canopic+Jars",
    themeIds: ["ancient-egypt"],
    mapPosition: { top: "58%", left: "70%" },
  },
  // Renaissance Art
  {
    id: "obj-07",
    title: "The Vitruvian Man Drawing",
    shortDescription: "A study of proportions by Leonardo da Vinci.",
    contextualBackground: "Leonardo da Vinci's drawing is a cornerstone of Renaissance art, blending artistic skill with scientific inquiry. It depicts a man in two superimposed positions with his arms and legs apart and inscribed in a circle and square, representing the ideal human body proportions as described by the ancient Roman architect Vitruvius.",
    galleryLocation: "Floor 3, Room 21",
    image: "https://placehold.co/800x600/7c2d12/ffffff?text=Vitruvian+Man",
    themeIds: ["renaissance-art"],
    mapPosition: { top: "70%", left: "40%" },
  },
  {
    id: "obj-08",
    title: "Bronze statue of David",
    shortDescription: "A bronze statue by Donatello.",
    contextualBackground: "Donatello's David is one of the most significant works of the early Renaissance. It was the first unsupported standing work of bronze cast during the Renaissance and the first freestanding nude male sculpture made since antiquity. It symbolizes the victory of civic virtue and freedom.",
    galleryLocation: "Floor 3, Room 22",
    image: "https://placehold.co/800x600/92400e/ffffff?text=Statue+of+David",
    themeIds: ["renaissance-art"],
    mapPosition: { top: "75%", left: "50%" },
  },
  // Ancient Greece
  {
    id: "obj-09",
    title: "Parthenon Marbles",
    shortDescription: "Sculptures from the pediments of the Parthenon.",
    contextualBackground: "Also known as the Elgin Marbles, these sculptures are masterpieces of classical Greek art. They originally adorned the Parthenon temple on the Athenian Acropolis and depict scenes from Greek mythology, representing the pinnacle of artistic achievement in 5th-century BC Athens.",
    galleryLocation: "Floor 1, Room 8",
    image: "https://placehold.co/800x600/d4d4d8/000000?text=Parthenon+Marbles",
    themeIds: ["ancient-greece"],
    mapPosition: { top: "40%", left: "45%" },
  },
  {
    id: "obj-10",
    title: "Bust of Pericles",
    shortDescription: "A Roman copy of a Greek original.",
    contextualBackground: "This bust depicts Pericles, the influential Athenian statesman and general during the city's Golden Age. The helmet symbolizes his role as a military leader. The idealized features reflect the classical Greek ideal of a calm, rational, and dignified leader.",
    galleryLocation: "Floor 1, Room 8",
    image: "https://placehold.co/800x600/e4e4e7/000000?text=Bust+of+Pericles",
    themeIds: ["ancient-greece"],
    mapPosition: { top: "42%", left: "50%" },
  },
  {
    id: "obj-11",
    title: "Athenian Owl Tetradrachm",
    shortDescription: "An ancient silver coin of Athens.",
    contextualBackground: "The 'Owl' was one of the most influential coins of the ancient world. On the obverse is the head of the goddess Athena, and on the reverse is her symbol, the owl. These coins were widely used in trade and are a symbol of Athens' economic power and cultural influence.",
    galleryLocation: "Floor 1, Room 9",
    image: "https://placehold.co/800x600/e5e5e5/000000?text=Athenian+Coin",
    themeIds: ["ancient-greece"],
    mapPosition: { top: "45%", left: "58%" },
  },
];

const tours: Tour[] = [
  {
    themeId: "roman-empire",
    size: "Small",
    objectIds: ["obj-01", "obj-02"],
  },
  {
    themeId: "roman-empire",
    size: "Medium",
    objectIds: ["obj-01", "obj-02", "obj-03"],
  },
  {
    themeId: "roman-empire",
    size: "Large",
    objectIds: ["obj-01", "obj-02", "obj-03"],
  },
  {
    themeId: "ancient-egypt",
    size: "Small",
    objectIds: ["obj-04", "obj-05"],
  },
  {
    themeId: "ancient-egypt",
    size: "Medium",
    objectIds: ["obj-04", "obj-05", "obj-06"],
  },
  {
    themeId: "ancient-egypt",
    size: "Large",
    objectIds: ["obj-04", "obj-05", "obj-06"],
  },
  {
    themeId: "renaissance-art",
    size: "Small",
    objectIds: ["obj-07", "obj-08"],
  },
  {
    themeId: "renaissance-art",
    size: "Medium",
    objectIds: ["obj-07", "obj-08"],
  },
  {
    themeId: "renaissance-art",
    size: "Large",
    objectIds: ["obj-07", "obj-08"],
  },
  {
    themeId: "ancient-greece",
    size: "Small",
    objectIds: ["obj-09", "obj-10"],
  },
  {
    themeId: "ancient-greece",
    size: "Medium",
    objectIds: ["obj-09", "obj-10", "obj-11"],
  },
  {
    themeId: "ancient-greece",
    size: "Large",
    objectIds: ["obj-09", "obj-10", "obj-11"],
  },
];

export const getThemes = (): MuseumTheme[] => themes;

export const getTheme = (id: string): MuseumTheme | undefined => themes.find((t) => t.id === id);

export const getObjects = (): MuseumObject[] => objects;

export const getObject = (id:string): MuseumObject | undefined => objects.find((o) => o.id === id);

export const getTourObjects = (themeId: string, size: TourSize): MuseumObject[] => {
  const tour = tours.find((t) => t.themeId === themeId && t.size === size);
  if (!tour) return [];
  return tour.objectIds.map((id) => getObject(id)).filter((o) => o !== undefined) as MuseumObject[];
};