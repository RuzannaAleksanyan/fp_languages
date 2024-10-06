import React from 'react';
import classes from './Clear.module.css';

const ClearField = () => {
  const handleClick = () => {
    console.log('Clear clicked!');
  };

  return (
    <div className={classes.inputContainer}>
      <button onClick={handleClick} className={classes.inputField}>
        Clear
      </button>
    </div>
  );
};

export default ClearField;
