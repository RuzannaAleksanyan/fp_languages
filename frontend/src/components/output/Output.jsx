import React from 'react';
import classes from './Output.module.css';

const OutputField = () => {
  return (
    <div className={classes.outputContainer}>
      <textarea
        className={classes.outputField}
        placeholder="Output"
        aria-label="Back output"
      />
    </div>
  );
};

export default OutputField;
