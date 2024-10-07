import React from 'react';
import classes from './Run.module.css';

const RunField = () => {
  const handleClick = () => {
    console.log('Button clicked!');
  };

  return (
    <div className={classes.runContainer}>
      <button onClick={handleClick} className={classes.runField}>
        {/* {value} */}
        run
      </button>
    </div>
  );
};

export default RunField;
