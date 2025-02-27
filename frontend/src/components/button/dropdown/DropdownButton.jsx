// import { useState } from 'react';
// import { ChevronDown, Globe } from 'lucide-react';
// import './DropdownButton.css';

// function DropdownButton({ onSelect }) {
//   const [isMenuOpen, setIsMenuOpen] = useState(false);
//   const [selectedOption, setSelectedOption] = useState("");

//   const toggleMenu = () => {
//     setIsMenuOpen(!isMenuOpen);
//   };

//   const handleOptionSelect = (option) => {
//     console.log("Dropdown selected:", option);  // Debug log
//     setSelectedOption(option);
//     onSelect(option); // Pass selected option to parent component (App.jsx)
//     setIsMenuOpen(false);
//   };

//   return (
//     <div className="dropdown">
//       <button className="dropdown-button" onClick={toggleMenu}>
//         <Globe className="dropdown-icon" />
//         {selectedOption ? selectedOption : 'Ընտրել'}
//         <ChevronDown className="dropdown-chevron" />
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

import { useState, useEffect } from 'react';
import { ChevronDown, Globe } from 'lucide-react';
import './DropdownButton.css';

function DropdownButton({ onSelect }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState(() => {
    return localStorage.getItem("selectedDropdownOption") || "";
  });

  useEffect(() => {
    onSelect(selectedOption); // Վերականգնված արժեքը փոխանցում ենք `App.jsx`-ին
  }, [selectedOption, onSelect]);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleOptionSelect = (option) => {
    console.log("Dropdown selected:", option);
    setSelectedOption(option);
    localStorage.setItem("selectedDropdownOption", option); // Պահպանում ենք `localStorage`-ում
    onSelect(option);
    setIsMenuOpen(false);
  };

  return (
    <div className="dropdown">
      <button className="dropdown-button" onClick={toggleMenu}>
        <Globe className="dropdown-icon" />
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
