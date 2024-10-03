import React from 'react';
import classes from './Input.module.css'
// import './Input.css'; // Fixed import path

const InputField = ({ value, setValue }) => {
  return (
    <div className={classes.inputContainer}>
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className={classes.inputField}
        placeholder="Input"
        aria-label="User input"
      />
    </div>
  );
};

export default InputField;
