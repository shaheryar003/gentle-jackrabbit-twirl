import { Link } from "react-router-dom";
import { MuseumObject } from "@/types";

interface MuseumMapProps {
  objects: MuseumObject[];
}

const MuseumMap = ({ objects }: MuseumMapProps) => {
  return (
    <div className="relative w-full max-w-3xl mx-auto">
      <svg
        viewBox="0 0 800 600"
        className="w-full h-auto bg-gray-100 rounded-lg border-2 border-gray-200"
      >
        {/* Floor outline */}
        <rect
          x="1"
          y="1"
          width="798"
          height="598"
          fill="#f7fafc"
          stroke="#e2e8f0"
          strokeWidth="2"
        />

        {/* Gallery dividers */}
        <line x1="200" y1="0" x2="200" y2="400" stroke="#cbd5e0" strokeWidth="2" />
        <line x1="500" y1="0" x2="500" y2="400" stroke="#cbd5e0" strokeWidth="2" />
        <line x1="0" y1="400" x2="800" y2="400" stroke="#cbd5e0" strokeWidth="2" />
        <line x1="400" y1="400" x2="400" y2="600" stroke="#cbd5e0" strokeWidth="2" />

        {/* Room Labels */}
        <text x="100" y="200" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 3</text>
        <text x="350" y="200" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 4</text>
        <text x="650" y="200" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 8</text>
        <text x="650" y="300" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 9</text>
        <text x="200" y="500" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 10</text>
        <text x="600" y="500" fontFamily="sans-serif" fontSize="16" fill="#a0aec0" textAnchor="middle">Room 12</text>
      </svg>

      {/* Object Pins */}
      {objects.map((obj, index) => (
        <Link to={`/object/${obj.id}`} key={obj.id}>
          <div
            className="absolute w-8 h-8 bg-red-600 text-white rounded-full flex items-center justify-center font-bold text-lg border-2 border-white shadow-lg transition-transform hover:scale-110"
            style={{
              top: obj.mapPosition.top,
              left: obj.mapPosition.left,
              transform: "translate(-50%, -50%)",
            }}
            title={`${obj.title} - ${obj.galleryLocation}`}
          >
            {index + 1}
          </div>
        </Link>
      ))}
    </div>
  );
};

export default MuseumMap;