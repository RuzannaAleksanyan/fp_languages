import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import classes from './Clear.module.css';

const ClearField = ({ value, setValue, isDarkMode }) => {
  const handleClick = () => {
    if (value !== '') {
      console.log('Clearing input!');
      setValue('');
    } else {
      console.log('Nothing to clear!');
    }
  };

  return (
    <button
      onClick={handleClick}
      className={`${classes.clearButton} ${isDarkMode ? classes.dark : classes.light}`}
    >
      <FontAwesomeIcon
        icon={faTrash}
        className={`${classes.icon} ${isDarkMode ? classes.dark : classes.light}`}
      /> 
      
      {/* <span className={`${classes.tooltip} ${isDarkMode ? classes.dark : ''}`}></span> */}
    </button>
  );
};

export default ClearField;
