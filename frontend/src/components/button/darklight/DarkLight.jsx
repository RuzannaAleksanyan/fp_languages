import React, { useState } from 'react';
import classes from './DarkLight.module.css';

const ButtonField = () => {
  // State to store the current background color
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Toggle the background color
  const handleToggleBackground = () => {
    setIsDarkMode((prevMode) => !prevMode);
  };

  return (
    <div
      className={classes.inputContainer}
      style={{
        backgroundColor: isDarkMode ? 'black' : 'white', // Change background color
        color: isDarkMode ? 'white' : 'black', // Change text color for better visibility
        height: '100vh', // Set height to fill the viewport for visual effect
      }}
    >
      <button onClick={handleToggleBackground} className={classes.inputField}>
        {isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
      </button>
    </div>
  );
};

export default ButtonField;
