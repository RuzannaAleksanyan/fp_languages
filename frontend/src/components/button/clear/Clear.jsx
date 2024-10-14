import React from 'react';
import classes from './Clear.module.css';

const ClearField = ({ value, setValue }) => {
  const handleClick = () => {
    if (value !== '') {
      console.log('Clearing input!');
      setValue('');
    } else {
      console.log('Nothing to clear!');
    }
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
