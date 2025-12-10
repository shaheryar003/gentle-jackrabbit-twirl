import asyncio
import os
import random
import time
import requests
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    print("Error: MONGODB_URI not found in environment variables.")
    exit(1)

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def get_pexels_image(query):
    if not PEXELS_API_KEY:
        print("Warning: PEXELS_API_KEY not set. Using placeholder images.")
        return f"https://placehold.co/800x600/gray/white?text={query.replace(' ', '+')}"
    
    headers = {"Authorization": PEXELS_API_KEY}
    try:
        # Search for the query
        response = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=1",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("photos"):
                return data["photos"][0]["src"]["large"]
    except Exception as e:
        print(f"Error fetching image for '{query}': {e}")
    
    # Fallback
    return f"https://placehold.co/800x600/gray/white?text={query.replace(' ', '+')}"

# Themes Data
themes_data = [
    {
        "id": "warfare",
        "name": "Warfare",
        "description": "Explore the history of conflict, weaponry, and the martial arts across different civilizations.",
        "image": get_pexels_image("Warfare"),
    },
    {
        "id": "women",
        "name": "Women",
        "description": "Celebrating the roles, contributions, and representations of women throughout history.",
        "image": get_pexels_image("Women in history"),
    },
    {
        "id": "art",
        "name": "Art",
        "description": "A journey through human creativity, from ancient sculptures to renaissance masterpieces.",
        "image": get_pexels_image("Classical Art"),
    },
    {
        "id": "religion",
        "name": "Religion",
        "description": "Discover the sacred artifacts, rituals, and beliefs that have shaped human spirituality.",
        "image": get_pexels_image("Religion"),
    },
    {
        "id": "mesopotamia",
        "name": "Mesopotamia",
        "description": "Artifacts from the 'Cradle of Civilization', the land between the Tigris and Euphrates rivers.",
        "image": get_pexels_image("Mesopotamia"),
    },
    {
        "id": "roman-empire",
        "name": "The Roman Empire",
        "description": "The glory of Rome: law, engineering, conquest, and daily life in the ancient empire.",
        "image": get_pexels_image("Roman Empire"),
    },
    {
        "id": "motherhood",
        "name": "Motherhood",
        "description": "A cross-cultural look at maternity, fertility, and the mother-child bond through the ages.",
        "image": get_pexels_image("Mother and Child Art"),
    },
]

# Helper to generate objects
def generate_objects():
    objects = []
    
    # --- Warfare Objects (20) ---
    warfare_items = [
        ("Bronze Age Sword", "A leaf-shaped blade used in early close-quarters combat.", "Warfare in the Bronze Age was characterized by the development of metal weaponry. This sword, cast from bronze, represents a leap in military technology, allowing for slashing attacks that were impossible with stone tools."),
        ("Roman Gladius", "The primary sword of Ancient Roman foot soldiers.", "The Gladius Hispaniensis was known for its devastating efficiency in the tight formations of the Roman Legion. Its short, stabbing point was ideal for the disciplined shield-wall tactics of the time."),
        ("Samurai Katana", "A traditional Japanese sword worn by the samurai class.", "The Katana is renowned for its sharpness and strength, folded repeatedly during forging. It was not just a weapon but the soul of the samurai, representing honor and social standing in feudal Japan."),
        ("Medieval Crossbow", "A ranged weapon capable of piercing heavy armor.", "The crossbow changed the face of medieval warfare by allowing minimally trained soldiers to penetrate the armor of elite knights. It was considered so deadly that the Pope attempted to ban its use against Christians."),
        ("Viking Shield", "A round wooden shield with a central iron boss.", "Viking shields were crucial for the 'shield wall' formation. Painted with clan symbols, they offered protection and could be used offensively to bash opponents."),
        ("Greek Hoplite Helmet", "A bronze Corinthian helmet offering full face protection.", "This helmet is iconic of the Greek hoplite. While it offered excellent protection, it restricted hearing and vision, encouraging the phalanx formation where soldiers relied on their neighbors."),
        ("Assyrian Chariot Panel", "A relief depicting a war chariot in battle.", "Chariots were the tanks of the ancient world. This panel shows the might of the Assyrian army, with archers firing from a moving platform, terrifying their enemies."),
        ("Zulu Assegai", "A short stabbing spear introduced by Shaka Zulu.", "Shaka Zulu revolutionized local warfare by shortening the traditional throwing spear into a stabbing weapon, forcing his warriors to close with the enemy."),
        ("English Longbow", "A powerful bow made of yew.", "The English Longbow was famous for its range and power, decimating French cavalry at battles like Agincourt. It required immense strength and years of training to master."),
        ("Persian Immortals Spear", "A silver-tipped spear carried by the elite guard.", "The Immortals were the elite force of the Persian Empire, always maintained at 10,000 strong. Their spears were symbols of their status and their duty to protect the King of Kings."),
        ("Knight's Plate Armor", "Full steel suit of armor from the 15th century.", "This suit of Maximilian armor represents the pinnacle of protection before firearms made plate obsolete. It is fluted to deflect blows and increase structural strength."),
        ("Maori Mere", "A short, broad-bladed club made of greenstone.", "The Mere was a prestigious weapon of the Maori chiefs. Made of jade (pounamu), it was used for thrusting strikes and was passed down through generations as a taonga (treasure)."),
        ("Mongol Recurve Bow", "A composite bow made of horn, wood, and sinew.", "The Mongol bow was the most advanced ranged weapon of its time, allowing horse archers to shoot with power and accuracy while riding, enabling the vast conquests of Genghis Khan."),
        ("Aztec Macuahuitl", "A wooden club embedded with obsidian blades.", "This weapon was capable of inflicting horrific injuries, with obsidian blades sharper than surgical steel. It was designed to maim enemies for capture and sacrifice."),
        ("Ottoman Janissary Musket", "An early firearm used by the Sultan's elite troops.", "The Janissaries were among the first standing armies to adopt firearms widely. This musket represents the transition from medieval to gunpowder warfare."),
        ("Spartan Xiphos", "A secondary short sword used by Spartans.", "When the spear was broken, the Spartan drew his Xiphos. Its leaf shape added weight to the cut, making it a deadly weapon in the press of the phalanx."),
        ("Crusader Heater Shield", "A shield shaped like a flat iron.", "Developed from the kite shield, the heater shield was smaller and more manageable for a knight on horseback, displaying his coat of arms for identification."),
        ("Japanese Yumi", "A tall, asymmetrical bow.", "The Yumi has been used by samurai for centuries. Its unique asymmetrical shape allows it to be shot easily from horseback while maintaining great power."),
        ("Indian Katar", "A punch dagger with a horizontal grip.", "The Katar allowed a warrior to put their whole body weight into a thrust. It was capable of piercing mail armor and was a symbol of martial prowess."),
        ("Civil War Cannonball", "A heavy iron projectile.", "Artillery dominated the battlefields of the 19th century. This solid shot was designed to smash through formations and fortifications alike.")
    ]
    
    # --- Women Objects (20) ---
    women_items = [
        ("Bust of Nefertiti", "A painted stucco-coated limestone bust.", "Nefertiti was the Great Royal Wife of Akhenaten. Her name means 'The Beautiful One Has Come'. This bust is an icon of feminine beauty and power in the ancient world."),
        ("Suffragette Sash", "A 'Votes for Women' sash.", "Worn by women fighting for the right to vote in the early 20th century. It symbolizes the long and difficult struggle for political equality."),
        ("Empress Dowager Cixi's Robe", "A silk robe embroidered with phoenixes.", "Cixi effectively controlled the Chinese government for 47 years. The phoenix motif was reserved for the Empress, symbolizing her supreme status."),
        ("Medieval Spindle Whorl", "A weighted disc used for spinning wool.", "Textile production was a primary economic activity for women in the medieval period. This tool represents the 'distaff side' of the household and women's contribution to the economy."),
        ("Portrait of Elizabeth I", "The 'Armada Portrait' of the Queen.", "This portrait depicts Elizabeth I at the height of her power, after the defeat of the Spanish Armada. It is a carefully constructed image of female sovereignty and strength."),
        ("Ancient Greek Pyxis", "A cylindrical box for cosmetics.", "Used by women in ancient Greece to hold jewelry or cosmetics. Scenes painted on these boxes often depicted the private lives of women in the women's quarters (gynaeceum)."),
        ("Frida Kahlo's Palette", "An artist's palette used by the Mexican painter.", "Frida Kahlo's art explored identity, postcolonialism, gender, class, and race. Her palette represents her tool for expressing the female experience."),
        ("Victorian Chatelaine", "A decorative belt hook with chains for keys and tools.", "The chatelaine was worn by the mistress of a household. It held the keys to the pantry and other important rooms, symbolizing her authority over the domestic sphere."),
        ("Scold's Bridle", "A metal muzzle used to punish 'gossiping' women.", "A dark reminder of the patriarchal control over women's speech. This instrument of torture was used to silence women deemed troublesome or outspoken."),
        ("Marie Curie's Notebook", "A lab notebook containing notes on radiation.", "Marie Curie was the first woman to win a Nobel Prize. This notebook records the groundbreaking research that would eventually cost her her life but save millions."),
        ("Geisha's Kimono", "A heavily embroidered silk garment.", "The kimono of a geisha is a work of art, but also a uniform of a complex profession. It represents the highly stylized and disciplined world of Japanese female entertainers."),
        ("Hatshepsut's Statue", "A statue of the female Pharaoh with a beard.", "Hatshepsut ruled as a Pharaoh, not just a queen regent. She is often depicted with the false beard of kingship, blending male symbols of power with her female identity."),
        ("Flapper Dress", "A beaded dress from the 1920s.", "The flapper dress symbolizes the 'New Woman' of the Jazz Age—women who voted, drove cars, and rejected the restrictive corsets and morals of the Victorian era."),
        ("Amelia Earhart's Goggles", "Flight goggles worn by the aviation pioneer.", "Earhart broke barriers for women in aviation. These goggles represent her courage and the spirit of adventure that inspired a generation of women."),
        ("Mayan Weaving Loom", "A backstrap loom for cotton textiles.", "Weaving was a sacred duty for Mayan women, associated with the moon goddess. The intricate patterns carried cultural stories and lineage information."),
        ("Catherine the Great's Fan", "A hand fan painted with court scenes.", "Fans were not just accessories but tools of communication in the European courts. Catherine used every tool at her disposal to navigate and dominate the political landscape."),
        ("Native American Cradleboard", "A carrier for an infant.", "Made by women to carry their children while working. The intricate beadwork often told stories of the child's family and was a labor of love and protection."),
        ("Renaissance Mirror", "A polished metal mirror.", "In art, the mirror often symbolized vanity, a vice attributed to women. However, it was also a tool for self-reflection and the subject of many paintings of women."),
        ("Sappho's Fragment", "A papyrus fragment of poetry.", "Sappho was one of the few female poets of antiquity whose work survives. Her poetry speaks of love and desire between women, giving us the term 'Lesbian'."),
        ("Rosie the Riveter Poster", "A propaganda poster from WWII.", "Representing the millions of women who entered the workforce during World War II, this image became a lasting symbol of female empowerment and capability.")
    ]

    # --- Art Objects (20) ---
    art_items = [
        ("Mona Lisa Replica", "A high-quality study of Da Vinci's masterpiece.", "The Mona Lisa is the archetype of the Renaissance portrait. Its sfumato technique and the enigmatic expression have captivated viewers for centuries."),
        ("Impressionist Landscape", "Oil on canvas depicting a garden.", "Impressionism broke from the rigid rules of the Academy, focusing on light and momentary scenes. This painting captures the fleeting atmosphere of a summer afternoon."),
        ("Ming Dynasty Vase", "Blue and white porcelain vase.", "Ming porcelain is famous for its technical perfection and artistic refinement. The cobalt blue pigment was imported from Persia, showing early global trade links."),
        ("Benin Bronze Head", "A brass head of an Oba (King).", "Created by the Edo people of Nigeria, these sculptures challenge colonial assumptions about African art. They are technically sophisticated and spiritually significant."),
        ("Abstract Expressionist Canvas", "Large scale painting with splatter technique.", "Reacting against representation, this work focuses on the act of painting itself. It expresses raw emotion and the subconscious through chaotic application of paint."),
        ("Greek Amphora", "Black-figure pottery jar.", "Amphoras were used for storage but also served as canvases for Greek myth. This piece depicts the labors of Hercules in striking black silhouettes."),
        ("Islamic Geometric Tile", "A star-patterned ceramic tile.", "Islamic art often avoids figural representation, focusing instead on the infinite nature of God through complex, repeating geometric patterns (arabesque)."),
        ("Fabergé Egg", "Jeweled egg with a hidden surprise.", "Created for the Russian Tsars, these eggs are the ultimate symbol of luxury and craftsmanship, made with gold, diamonds, and enamel."),
        ("Hokusai Woodblock Print", "The Great Wave off Kanagawa.", "This ukiyo-e print is one of the most recognized works of Japanese art. It captures the power of nature and the fragility of man."),
        ("Tiffany Stained Glass", "A lamp shade with floral motifs.", "Louis Comfort Tiffany revolutionized glass art. This piece shows the Art Nouveau style, inspired by natural forms and organic lines."),
        ("Rodin's The Thinker Study", "A small bronze cast.", "Rodin brought sculpture into the modern era by emphasizing emotion and the physical reality of the body rather than idealized forms."),
        ("Medieval Tapestry", "Woven depiction of a hunt.", "Tapestries were both art and insulation for drafty castles. They were incredibly expensive status symbols, often taking years to weave."),
        ("Calligraphy Scroll", "Chinese brush calligraphy.", "In China, calligraphy is considered the highest art form. The flow of the ink and the strength of the brushstrokes reveal the character of the artist."),
        ("Pre-Raphaelite Painting", "Oil painting of a medieval legend.", "The Pre-Raphaelites sought to return to the intense colors and complex compositions of Quattrocento Italian art, rejecting the mechanistic approach of Mannerism."),
        ("Surrealist Clock", "A melting clock sculpture.", "Inspired by Dali, this object challenges our perception of reality and time, exploring the dream world and the unconscious mind."),
        ("Art Deco Statue", "Bronze and ivory figure.", "Art Deco combined modern styles with fine craftsmanship and rich materials. This figure represents the glamour and optimism of the Roaring Twenties."),
        ("Byzantine Icon", "Gold-leaf religious painting on wood.", "Icons are 'windows to heaven' in Orthodox Christianity. The stylized figures and gold background are meant to transport the viewer to a spiritual realm."),
        ("Rococo Fan", "Silk and ivory fan.", "Rococo art is characterized by lightness, elegance, and curving natural forms. This fan was a fashion accessory for the French aristocracy."),
        ("Pop Art Soup Can", "Screenprint on canvas.", "Pop Art blurred the boundaries between 'high' art and low culture. This piece comments on consumerism and mass production."),
        ("Bauhaus Chair", "Tubular steel and leather chair.", "Form follows function. The Bauhaus school sought to unify art, craft, and technology, creating designs that were simple, functional, and mass-producible.")
    ]

    # --- Religion Objects (20) ---
    religion_items = [
        ("Dead Sea Scroll Fragment", "Parchment containing biblical text.", "These ancient manuscripts provide the oldest known copies of the Hebrew Bible. They offer unparalleled insight into the history of Judaism and the background of Christianity."),
        ("Statue of Ganesh", "Stone sculpture of the elephant-headed god.", "Ganesh is the remover of obstacles and the god of beginnings in Hinduism. He is worshipped before any major enterprise and is the patron of intellectuals."),
        ("Tibetan Prayer Wheel", "Metal cylinder containing mantras.", "Spinning the wheel is considered equivalent to reciting the mantras inside. It is a physical manifestation of prayer and the desire to spread compassion."),
        ("Medieval Reliquary", "Gilded box containing a saint's bone.", "Relics were central to medieval Christianity. Faithful pilgrims traveled hundreds of miles to venerate them, hoping for miracles or intercession."),
        ("Aztec Sun Stone Replica", "A calendar stone depicting the sun god.", "Often called the Aztec Calendar, it depicts the five eras of the sun. It represents the Aztec view of time and the necessity of sacrifice to keep the sun moving."),
        ("Shinto Mirror", "Bronze mirror from a shrine.", "In Shinto, the mirror is a symbol of truth and the kami (spirit). It reflects the soul of the viewer and is one of the Imperial Regalia of Japan."),
        ("Islamic Prayer Rug", "Wool rug with a mihrab design.", "The prayer rug creates a clean space for the Muslim to pray five times a day. The design points towards Mecca, the spiritual center of Islam."),
        ("Torah Scroll", "Handwritten parchment scroll.", "The Torah contains the first five books of Moses. It is treated with the utmost reverence in the synagogue, read publicly on the Sabbath."),
        ("Buddha Head", "Sandstone head from the Gupta period.", "This head depicts the Buddha in a state of deep meditation. The half-closed eyes and serene smile symbolize inner peace and enlightenment."),
        ("Viking Thor's Hammer", "Silver pendant amulet.", "Mjölnir pendants were worn by Norse pagans as a sign of their faith in Thor, the protector of mankind, especially as Christianity began to spread."),
        ("Coptic Cross", " intricate metal cross from Ethiopia.", "The Ethiopian Orthodox Church has a unique artistic tradition. This cross processional cross features complex lattice patterns symbolizing the eternal nature of God."),
        ("Zoroastrian Fire Vase", "Vessel used in fire rituals.", "Fire is a symbol of purity in Zoroastrianism. It represents the light of God (Ahura Mazda) and is kept burning continuously in fire temples."),
        ("Incan Golden Llama", "Votive figurine.", "Gold was the 'sweat of the sun' to the Incas. Small figures like this were buried as offerings to the mountain gods (Apus) to ensure the fertility of the herds."),
        ("Daoist Immortal Statue", "Porcelain figure.", "The Eight Immortals are legendary figures in Daoism who attained immortality. They represent different aspects of society and are signs of prosperity and longevity."),
        ("Catholic Rosary", "Beads made of rosewood.", "The Rosary is a tool for meditation on the life of Christ and the Virgin Mary. It represents a rhythmic, repetitive prayer tradition."),
        ("Sikh Kirpan", "Ceremonial dagger.", "The Kirpan is one of the five articles of faith worn by initiated Sikhs. It symbolizes the duty to protect the innocent and fight against injustice."),
        ("Ancient Egyptian Ankh", "Faience amulet.", "The Ankh is the hieroglyph for 'life'. It was carried by gods and pharaohs as a symbol of their power to give and sustain life, both here and in the afterlife."),
        ("Yoruba Ifa Tray", "Wooden divination tray.", "Used by Babalawo priests to interpret the will of the Orisha. Dust is sprinkled on the tray to mark the signs of the Ifa corpus."),
        ("Masonic Apron", "Lambskin apron with symbols.", "Freemasonry uses the tools of stonemasons as moral allegories. The apron is the badge of a Mason, symbolizing purity of life and conduct."),
        ("Shaman's Drum", "Reindeer hide drum.", "For Siberian shamans, the drum is the steed that carries them to the spirit world. The beat drives the trance state necessary for healing and prophecy.")
    ]

    # --- Mesopotamia Objects (15) ---
    mesopotamia_items = [
        ("Cuneiform Tablet", "Clay tablet recording a grain sale.", "Mesopotamia gave the world its first writing system: Cuneiform. This daily record provides a glimpse into the sophisticated bureaucracy and economy of ancient Sumer."),
        ("Standard of Ur Box", "Inlaid box with scenes of war and peace.", "This artifact from the Royal Tombs of Ur is a mosaic of shell, limestone, and lapis lazuli. It depicts the two sides of royal rule: leading the army and holding banquets."),
        ("Gudea Statue", "Diorite statue of a ruler.", "Gudea of Lagash was a pious ruler who built many temples. His statues portray him in a humble posture of prayer, emphasizing his duty to the gods rather than military might."),
        ("Cylinder Seal", "Stone seal with mythological scene.", "Rolled onto wet clay, these seals acted as signatures. The intricate carving on this tiny stone shows the incredible skill of Mesopotamian lapidaries."),
        ("Lamassu Fragment", "Piece of a winged bull guardian.", "Lamassu were colossal guardian figures placed at the gates of Assyrian palaces. They combined the wisdom of a man, the strength of a bull, and the speed of an eagle."),
        ("Law Code of Hammurabi", "Stele fragment with laws.", "Hammurabi's code is one of the earliest written legal codes. It established the principle of 'an eye for an eye' and presumed innocence until proven guilty."),
        ("Ishtar Gate Brick", "Glazed blue brick with a dragon.", "The Ishtar Gate of Babylon was a wonder of the ancient world. The blue glazed bricks and relief animals proclaimed the power of the city and its gods."),
        ("Sumerian Votive Figure", "Wide-eyed worshipper statue.", "These figures were placed in temples to pray eternally on behalf of the donor. Their wide eyes symbolize eternal wakefulness and awe before the divine."),
        ("Flood Tablet", "Tablet XI of the Epic of Gilgamesh.", "This tablet tells the story of a great flood sent by the gods, a narrative that predates the biblical account of Noah, highlighting shared cultural memories in the region."),
        ("Royal Game of Ur", "Board game with playing pieces.", "One of the oldest board games in the world. It was a race game similar to backgammon, enjoyed by the royalty of Ur over 4,500 years ago."),
        ("Assyrian Lion Hunt Relief", "Stone panel.", "Assyrian kings proved their right to rule by killing lions. This relief shows the raw power and violence of the hunt, serving as royal propaganda."),
        ("Ziggurat Foundation Peg", "Copper peg in the shape of a god.", "Buried in the foundations of temples to sanctify the ground and anchor the structure spiritually. It depicts a god driving the peg into the earth."),
        ("Babylonian Map of the World", "Clay tablet with a map.", "The earliest known map of the world. It shows Babylon at the center, surrounded by the 'Bitter River', reflecting the Babylonians' view of their place in the cosmos."),
        ("Gold Lyre of Ur", "Reconstruction of a musical instrument.", "Found in the Royal Cemetery, this lyre had a golden bull's head. Music was an integral part of courtly life and religious rituals."),
        ("Agade Period Seal", "Seal showing a contest scene.", "The Akkadian period introduced a new level of realism and dynamism to art. This seal shows heroes wrestling with wild beasts, a metaphor for order vs. chaos.")
    ]

    # --- Roman Empire Objects (15) ---
    roman_items = [
        ("Bust of Augustus", "Marble portrait of the first Emperor.", "Augustus transformed Rome from a republic to an empire. This idealized portrait served as political propaganda, showing him as eternally young and capable."),
        ("Legionary Helmet", "Iron helmet with cheek guards.", "The Galea protected the Roman soldier's head while allowing for visibility and hearing. It is the symbol of the military machine that conquered the Mediterranean."),
        ("Denarius of Julius Caesar", "Silver coin.", "This coin was the first to feature a living Roman leader, a bold move that contributed to the accusations of kingship that led to Caesar's assassination."),
        ("Pompeii Fresco Fragment", "Plaster painted with garden scene.", "Preserved by the eruption of Vesuvius, this fresco shows the Roman love for nature and the vibrant colors used to decorate their homes."),
        ("Roman Glass Flask", "Blown glass perfume bottle.", "The Romans invented glassblowing, making glass affordable for the first time. This delicate vessel held precious oils or perfumes."),
        ("Gladiator's Greave", "Bronze shin guard.", "Gladiators were the superstars of the Roman world. This decorated armor protected the leg but was also designed to look impressive in the arena."),
        ("Wolf and Twins Statue", "Bronze She-Wolf suckling Romulus and Remus.", "The foundation myth of Rome. The twins, abandoned to die, were saved by a wolf. It symbolizes Rome's fierce and divinely ordained origins."),
        ("Roman Surgical Tools", "Bronze scalpels and probes.", "Roman medicine was advanced for its time, especially in battlefield surgery. These tools are surprisingly similar to modern medical instruments."),
        ("Mosaic Floor Section", "Tesserae depicting a fish.", "Mosaics were the carpets of the Roman world. This piece, likely from a dining room, shows the abundance of the sea."),
        ("Oil Lamp", "Terracotta lamp with a gladiator scene.", "Mass-produced oil lamps were the lightbulbs of antiquity. They were often decorated with scenes from daily life, including popular entertainments."),
        ("Trajan's Column Cast", "Plaster cast of a relief section.", "The column chronicles Trajan's wars in Dacia. It is a continuous narrative in stone, providing detailed information on the Roman army."),
        ("Cameo Glass Vase", "The Portland Vase replica.", "Cameo glass involved carving through layers of different colored glass. It was a luxury art form, and this vase is its most famous example."),
        ("Roman Key", "Bronze ring key.", "Romans were concerned with security. Keys were often worn as rings for convenience and to show that the wearer had possessions worth locking up."),
        ("Strigil", "Curved metal tool.", "Used in the Roman baths to scrape oil and dirt from the skin. Bathing was a central social activity in Roman culture."),
        ("Toga Fibula", "Bronze brooch.", "The fibula was used to pin the heavy woolen toga. Styles changed over time, making them useful for dating archaeological sites.")
    ]

    # --- Motherhood Objects (15) ---
    motherhood_items = [
        ("Isis Nursing Horus", "Bronze statuette.", "The image of the goddess Isis nursing her son Horus is a powerful symbol of maternal protection and divine kingship. It influenced later Christian iconography of Mary and Jesus."),
        ("Medieval Madonna and Child", "Wooden polychrome statue.", "This tender depiction emphasizes the humanity of Christ and the motherly love of Mary, a popular theme in medieval devotion."),
        ("Prehistoric Venus Figurine", "Limestone carving.", "These ancient figures with exaggerated fertility features are believed to be some of the earliest representations of motherhood and the generative power of women."),
        ("Victorian Nursing Chair", "Low upholstered chair.", "Designed without arms to accommodate a mother's wide skirts and provide a comfortable position for breastfeeding. It speaks to the domestic focus of the era."),
        ("African Maternity Figure", "Wood carving of mother and twins.", "In many African cultures, twins are considered special or sacred. This figure honors the mother and seeks protection for her children."),
        ("Baby Carrier (Amauti)", "Inuit parka with baby pouch.", "The Amauti allows the mother to carry the baby against her back, sharing body heat in the harsh Arctic climate. It represents the close bond and survival."),
        ("Roman Votive Uterus", "Terracotta offering.", "offered at temples by women seeking to conceive or thanking the gods for a safe childbirth. It highlights the medical and spiritual anxieties around reproduction."),
        ("Mary Cassatt Print", "The Maternal Caress.", "Cassatt was an Impressionist who specialized in the intimate social lives of women, particularly the bond between mother and child, depicted here with unsentimental tenderness."),
        ("Klimt's Mother and Child", "Detail from 'The Three Ages of Woman'.", "Klimt's work envelops the mother and child in a decorative cocoon, symbolizing the sleep-like peace and organic unity of the maternal bond."),
        ("Native American Umbilical Amulet", "Beaded turtle pouch.", "Used to store the child's umbilical cord. The turtle symbolizes longevity and protection. It was kept as a charm for the child's life."),
        ("Chinese '100 Boys' Vase", "Porcelain vase.", "Depicting many sons playing, this motif represents the wish for abundant male offspring to carry on the family line, reflecting traditional Confucian values."),
        ("Victorian Mourning Locket", "Gold locket with hair.", "High infant mortality meant motherhood often involved loss. This locket contains a lock of a child's hair, worn as a keepsake of a life cut short."),
        ("Depression Era Photo", "Migrant Mother.", "Dorothea Lange's iconic photo captures the anxiety and strength of a mother trying to survive and protect her children during the Great Depression."),
        ("Fertility Doll (Akuaba)", "Ashanti wooden doll.", "Carved with a high forehead and round face (ideals of beauty), these dolls are carried by women who wish to conceive, treated like real babies."),
        ("Modern Breast Pump", "Early 20th century glass pump.", "The industrialization of motherhood. This object represents the intersection of technology and the biological function of nursing.")
    ]

    # Combine and tag items
    all_theme_items = [
        (warfare_items, "warfare"),
        (women_items, "women"),
        (art_items, "art"),
        (religion_items, "religion"),
        (mesopotamia_items, "mesopotamia"),
        (roman_items, "roman-empire"),
        (motherhood_items, "motherhood"),
    ]

    obj_counter = 1
    
    # Locations
    floors = ["Floor 1", "Floor 2", "Floor 3"]
    rooms = range(100, 310)

    for items, theme_id in all_theme_items:
        for title, short_desc, context in items:
            
            # 20% chance to add a secondary theme if applicable
            themes = [theme_id]
            if theme_id == "roman-empire" and random.random() < 0.3:
                themes.append("warfare")
            if theme_id == "motherhood" and random.random() < 0.3:
                themes.append("women")
            if theme_id == "art" and "Statue" in title:
                themes.append("women") # Just a random overlap for variety
            
            # Map position (randomized)
            top = f"{random.randint(10, 80)}%"
            left = f"{random.randint(10, 80)}%"

            # Location
            location = f"{random.choice(floors)}, Room {random.choice(rooms)}"

            obj_data = {
                "id": f"obj-{obj_counter:03d}",
                "title": title,
                "shortDescription": short_desc,
                "contextualBackground": context,
                "galleryLocation": location,
                "image": get_pexels_image(title),
                "themeIds": themes,
                "mapPosition": {"top": top, "left": left}
            }
            objects.append(obj_data)
            obj_counter += 1
            print(f"Generated object {obj_counter-1}: {title}")
            time.sleep(0.5) # Rate limiting to be safe

    return objects

objects_data = generate_objects()

# Simple tour generation based on new themes
tours_data = []
for theme in themes_data:
    theme_id = theme["id"]
    # Find objects for this theme
    theme_objs = [o["id"] for o in objects_data if theme_id in o["themeIds"]]
    
    # Create Small, Medium, Large tours
    if len(theme_objs) >= 2:
        tours_data.append({
            "themeId": theme_id,
            "size": "Small",
            "objectIds": theme_objs[:3]
        })
    if len(theme_objs) >= 5:
        tours_data.append({
            "themeId": theme_id,
            "size": "Medium",
            "objectIds": theme_objs[:5]
        })
    if len(theme_objs) >= 8:
        tours_data.append({
            "themeId": theme_id,
            "size": "Large",
            "objectIds": theme_objs[:8]
        })


async def seed():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client["museum_tour"]

    try:
        # Seed Themes
        await db.themes.delete_many({})
        # Set _id to be the same as id
        themes_to_insert = [{**item, "_id": item["id"]} for item in themes_data]
        await db.themes.insert_many(themes_to_insert)
        print(f"Seeded {len(themes_to_insert)} themes")

        # Seed Objects
        await db.objects.delete_many({})
        objects_to_insert = [{**item, "_id": item["id"]} for item in objects_data]
        await db.objects.insert_many(objects_to_insert)
        print(f"Seeded {len(objects_to_insert)} objects")

        # Seed Tours
        await db.tours.delete_many({})
        await db.tours.insert_many(tours_data)
        print(f"Seeded {len(tours_data)} tours")

        print("Database seeding completed successfully!")

    except Exception as e:
        print(f"An error occurred during seeding: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed())