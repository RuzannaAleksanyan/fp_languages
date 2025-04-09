// import { Settings } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import './InfoButton.module.css';

import { ReactComponent as MyIcon } from './myIcon.svg';


function InfoButton({ language }) {
  const location = useLocation();
  const storedLanguage = localStorage.getItem("selectedDropdownOption") || language;

  const infoPagePath = storedLanguage === 'Bekus fp language' ? '/info-bekus' : '/info-herbrand';

  return (
    <Link to={infoPagePath} className="infoButton">
      <MyIcon className="icon" width={80} height={80} />
      <span className="tooltip"></span>
    </Link>
  );
}

export default InfoButton;
