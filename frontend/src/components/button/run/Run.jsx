import React from 'react';
import classes from './Run.module.css';

const ButtonField = () => {
  const handleClick = () => {
    console.log('Button clicked!');
  };

  return (
    <div className={classes.inputContainer}>
      <button onClick={handleClick} className={classes.inputField}>
        {/* {value} */}
        run
      </button>
    </div>
  );
};

export default ButtonField;
