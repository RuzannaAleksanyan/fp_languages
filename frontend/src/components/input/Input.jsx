import React from 'react';
import classes from './Input.module.css';

const InputField = ({ value, setValue, isDarkMode }) => {
  return (
    <div className={`${classes.inputContainer} ${isDarkMode ? classes.dark : ''}`}>
      <label className={classes.inputLabel}>Input</label> {}
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className={`${classes.inputField} ${isDarkMode ? classes.darkField : ''}`}
        aria-label="User input"
      />
    </div>
  );
};

export default InputField;
