import React from 'react';
import classes from './Output.module.css';

const OutputField = ({ result, isDarkMode }) => {
  return (
    <div className={`${classes.outputContainer} ${isDarkMode ? classes.dark : ''}`}>
       <label className={classes.outputLabel}>Output</label> {}

      <textarea
        className={`${classes.outputField} ${isDarkMode ? classes.darkField : ''}`}
        // placeholder="Output"
        value={result}
        readOnly
        aria-label="Back output"
      />
    </div>
  );
};

export default OutputField;
