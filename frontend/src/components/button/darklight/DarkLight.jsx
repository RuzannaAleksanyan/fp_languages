// import React, { useState } from 'react';
// import classes from './DarkLight.module.css';

// const ButtonField = () => {
//   // State to store the current background color
//   const [isDarkMode, setIsDarkMode] = useState(false);

//   // Toggle the background color
//   const handleToggleBackground = () => {
//     setIsDarkMode((prevMode) => !prevMode);
//   };

//   return (
//     <div
//       className={classes.darkLightContainer}
//       style={{
//         backgroundColor: isDarkMode ? 'black' : 'white', // Change background color
//         color: isDarkMode ? 'white' : 'black', // Change text color for better visibility
//       }}
//     >
//       <button onClick={handleToggleBackground} className={classes.darkLightField}>
//         {isDarkMode ? 'Light' : 'Dark'}
//       </button>
//     </div>
//   );
// };

// export default ButtonField;



import React from 'react';
import classes from './DarkLight.module.css';

const DarkLight = ({ toggleDarkMode, isDarkMode }) => {
  return (
    <div
      className={classes.darkLightContainer}
      style={{
        color: isDarkMode ? 'white' : 'black', // Change text color for better visibility
      }}
    >
      <button onClick={toggleDarkMode} className={classes.darkLightField}>
        {isDarkMode ? 'Light' : 'Dark'}
      </button>
    </div>
  );
};

export default DarkLight;
