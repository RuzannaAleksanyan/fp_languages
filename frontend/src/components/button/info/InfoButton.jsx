import { Settings } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import './InfoButton.module.css';

function InfoButton({ language }) {
  const location = useLocation();
  const storedLanguage = localStorage.getItem("selectedDropdownOption") || language;
  
  const infoPagePath = storedLanguage === 'Bekus fp language' ? '/info-bekus' : '/info-herbrand';

  return (
    <Link to={infoPagePath} className="infoButton">
      <Settings size={80} className="icon" />
      <span className="tooltip"></span>
    </Link>
  );
}

export default InfoButton;
