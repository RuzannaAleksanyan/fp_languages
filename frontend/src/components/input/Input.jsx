import React from 'react';
import classes from './Input.module.css';

const InputField = ({ value, setValue }) => {
  const handleKeyPress = async (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      try {
        const response = await fetch('http://localhost:3001/api/input', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ userInput: value }),
        });

        const data = await response.json();
        console.log('Response from server:', data);
      } catch (error) {
        console.error('Error sending input:', error);
      }
    }
  };

  return (
    <div className={classes.inputContainer}>
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyPress={handleKeyPress}
        className={classes.inputField}
        placeholder="Enter your text here"
        aria-label="User input"
      />
    </div>
  );
};

export default InputField;
