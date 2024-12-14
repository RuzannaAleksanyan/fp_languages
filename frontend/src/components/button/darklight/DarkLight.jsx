import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSun, faMoon } from '@fortawesome/free-solid-svg-icons';
import classes from './DarkLight.module.css';

const DarkLight = ({ toggleDarkMode, isDarkMode }) => {
  return (
    <button
      onClick={toggleDarkMode}
      className={`${classes.darkLightButton} ${isDarkMode ? classes.dark : classes.light}`}
    >
      <FontAwesomeIcon
        icon={isDarkMode ? faSun : faMoon}
        className={`${classes.icon} ${isDarkMode ? classes.dark : classes.light}`}
      />
      {/* <span className={classes.tooltip}>{isDarkMode ? 'Light Mode' : 'Dark Mode'}</span> */}
    </button>
  );
};

export default DarkLight;
