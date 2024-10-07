import React from 'react';
import classes from './Clear.module.css';

const ClearField = () => {
  const handleClick = () => {
    console.log('Clear clicked!');
  };

  return (
    <div className={classes.clearContainer}>
      <button onClick={handleClick} className={classes.clearField}>
        Clear
      </button>
    </div>
  );
};

export default ClearField;
