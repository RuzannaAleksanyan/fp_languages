import React from 'react';
import classes from './Input.module.css';

const InputField = ({ value, setValue }) => {
  return (
    <div className={classes.inputContainer}>
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className={classes.inputField}
        placeholder="Enter your text here"
        aria-label="User input"
      />
    </div>
  );
};

export default InputField;
