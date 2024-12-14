import React from 'react';
import classes from './Input.module.css';

const InputField = ({ value, setValue, isDarkMode }) => {
  return (
    <div className={`${classes.inputContainer} ${isDarkMode ? classes.dark : ''}`}>
      <label className={classes.inputLabel}>Input</label> {/* Ուղղված է styles -> classes */}
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className={`${classes.inputField} ${isDarkMode ? classes.darkField : ''}`}
        // placeholder="Enter your text here"
        aria-label="User input"
      />
    </div>
  );
};

export default InputField;
