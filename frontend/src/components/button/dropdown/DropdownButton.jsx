// import { useState, useEffect } from 'react';
// import { useLocation, useNavigate } from 'react-router-dom';
// import { ChevronDown, Globe } from 'lucide-react';
// import './DropdownButton.css';

// function DropdownButton({ onSelect }) {
//   const [isMenuOpen, setIsMenuOpen] = useState(false);
//   const location = useLocation();
//   const navigate = useNavigate();
  
//   const [selectedOption, setSelectedOption] = useState(() => {
//     return localStorage.getItem("selectedDropdownOption") || "";
//   });

//   useEffect(() => {
//     onSelect(selectedOption); 
//   }, [selectedOption, onSelect]);

//   const toggleMenu = () => {
//     setIsMenuOpen(!isMenuOpen);
//   };

//   const handleOptionSelect = (option) => {
//     setSelectedOption(option);
//     localStorage.setItem("selectedDropdownOption", option); 
//     onSelect(option);
//     setIsMenuOpen(false);

//     const isInfoPage = location.pathname === "/info-bekus" || location.pathname === "/info-herbrand";

//     if (isInfoPage) {
//       if (option === 'Bekus fp language' && location.pathname !== "/info-bekus") {
//         navigate("/info-bekus");
//       } else if (option === 'Herbrand Godel Klini fp language' && location.pathname !== "/info-herbrand") {
//         navigate("/info-herbrand");
//       }
//     }
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


import { useState, useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { ChevronDown, Globe } from 'lucide-react';
import './DropdownButton.css';

function DropdownButton({ onSelect }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();
  
  const [selectedOption, setSelectedOption] = useState(() => {
    return localStorage.getItem("selectedDropdownOption") || "";
  });

  const dropdownRef = useRef(null);  // Dropdown-ի ref

  useEffect(() => {
    onSelect(selectedOption); 
  }, [selectedOption, onSelect]);

  // Ավելացնում ենք օնկլիք իրադարձություն ամբողջ էջում, որ փակենք dropdown-ը եթե սեղմվում է դուրս
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsMenuOpen(false);  // Փակել մենյուն
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);  // Խուսափել հիշողության leaks-ից
    };
  }, []);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleOptionSelect = (option) => {
    setSelectedOption(option);
    localStorage.setItem("selectedDropdownOption", option); 
    onSelect(option);
    setIsMenuOpen(false);

    const isInfoPage = location.pathname === "/info-bekus" || location.pathname === "/info-herbrand";

    if (isInfoPage) {
      if (option === 'Bekus fp language' && location.pathname !== "/info-bekus") {
        navigate("/info-bekus");
      } else if (option === 'Herbrand Godel Klini fp language' && location.pathname !== "/info-herbrand") {
        navigate("/info-herbrand");
      }
    }
  };

  return (
    <div className="dropdown" ref={dropdownRef}>
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
