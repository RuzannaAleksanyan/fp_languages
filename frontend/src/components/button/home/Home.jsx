
import { Link } from 'react-router-dom';
import homeIcon from '../../../image/logo.png';
import classes from './Home.module.css';

function Home() {
  return (
    <Link to="/">
      <img src={homeIcon} alt="Home" className={classes.icone}/>
      {/* <HomeIcon className={classes.icone} style={{ fill: 'black' }} /> */}

    </Link>
  );
}

export default Home;
