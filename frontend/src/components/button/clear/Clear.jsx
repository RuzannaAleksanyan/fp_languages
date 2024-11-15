import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
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
    <button onClick={handleClick} className={classes.clearButton}>
      <FontAwesomeIcon icon={faTrash} style={{ marginRight: '5px' }} />
      <span className={classes.tooltip}>{"Clear"}</span>
      {/* Clear */}
    </button>
  );
};

export default ClearField;
