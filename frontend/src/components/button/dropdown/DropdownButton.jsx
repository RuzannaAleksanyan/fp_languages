import { useState, useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { ChevronDown, Globe } from 'lucide-react';
import './DropdownButton.css';

function DropdownButton({ onSelect, isDarkMode }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const [selectedOption, setSelectedOption] = useState(() => {
    return localStorage.getItem("selectedDropdownOption") || "";
  });

  const dropdownRef = useRef(null);

  useEffect(() => {
    onSelect(selectedOption);
  }, [selectedOption, onSelect]);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsMenuOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
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
      <button
        className={`dropdown-button ${isDarkMode ? 'dark' : 'light'}`}
        onClick={toggleMenu}
      >
        <Globe className="dropdown-icon" color={isDarkMode ? 'white' : 'black'} />
        {selectedOption ? selectedOption : 'Ընտրել'}
        <ChevronDown className="dropdown-chevron" color={isDarkMode ? 'white' : 'black'} />
      </button>
      {isMenuOpen && (
        <div className={`dropdown-menu ${isDarkMode ? 'dark' : 'light'}`}>
          <div onClick={() => handleOptionSelect(' Bekus fp language')}> Bekus fp language </div>
          <div onClick={() => handleOptionSelect(' Herbrand Godel Klini fp language')}> Herbrand Godel Klini fp language </div>
        </div>
      )}
    </div>
  );
}

export default DropdownButton;