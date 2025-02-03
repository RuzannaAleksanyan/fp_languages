// import { useState } from 'react';
// import './DropdownButton.css';

// function DropdownButton({ onSelect }) {
//   const [isMenuOpen, setIsMenuOpen] = useState(false);
//   const [selectedOption, setSelectedOption] = useState(null);

//   const toggleMenu = () => {
//     setIsMenuOpen(!isMenuOpen);
//   };

//   const handleOptionSelect = (option) => {
//     setSelectedOption(option);
//     setIsMenuOpen(false);
//     onSelect(option);
//   };

//   return (
//     <div className="dropdown">
//       <button className="dropdown-button" onClick={toggleMenu}>
//         {selectedOption ? selectedOption : 'Ընտրել'}
//       </button>
//       {isMenuOpen && (
//         <div className="dropdown-menu">
//           <div onClick={() => handleOptionSelect('Bekus fp language')}>Bekus fp language</div>
//           <div onClick={() => handleOptionSelect('Herbrand Godel Klini fp language')}>Herbrand Godel Klini fp language</div>
//         </div>
//       )}
//     </div>
//   );
// }

// export default DropdownButton;


import { useState } from 'react';
import { ChevronDown, Globe } from 'lucide-react'; // Icon-ները ներմուծում ենք
import './DropdownButton.css';

function DropdownButton({ onSelect }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleOptionSelect = (option) => {
    setSelectedOption(option);
    setIsMenuOpen(false);
    onSelect(option);
  };

  return (
    <div className="dropdown">
      <button className="dropdown-button" onClick={toggleMenu}>
        <Globe className="dropdown-icon" /> {/* Այստեղ ավելացրու icon */}
        {selectedOption ? selectedOption : 'Ընտրել'}
        <ChevronDown className="dropdown-chevron" />
      </button>
      {isMenuOpen && (
        <div className="dropdown-menu">
          <div onClick={() => handleOptionSelect('Bekus fp language')}>Bekus fp language</div>
          <div onClick={() => handleOptionSelect('Herbrand Godel Klini fp language')}>Herbrand Godel Klini fp language</div>
        </div>
      )}
    </div>
  );
}

export default DropdownButton;
