import React from 'react';
import classes from './DarkLight.module.css';

const DarkLight = ({ toggleDarkMode, isDarkMode }) => {
  return (
    <div
      className={classes.darkLightContainer}
      style={{
        color: isDarkMode ? 'white' : 'black',
      }}
    >
      <button onClick={toggleDarkMode} className={classes.darkLightField}>
        {isDarkMode ? 'Light' : 'Dark'}
      </button>
    </div>
  );
};

export default DarkLight;
