import { Settings } from 'lucide-react';
import { Link } from 'react-router-dom';
import './InfoButton.module.css';

function InfoButton() {
  return (
    <Link to="/info" className="infoButton">
      <Settings size={80} className="icon" />
      <span className="tooltip"></span>
    </Link>
  );
}

export default InfoButton;
