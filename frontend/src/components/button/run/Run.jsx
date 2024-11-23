import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlay } from '@fortawesome/free-solid-svg-icons';
import classes from './Run.module.css';

const Run = ({ onRun }) => {
  return (
    <button onClick={onRun} className={classes.runButton}>
      <FontAwesomeIcon icon={faPlay} style={{ marginRight: '5px' }} />
      <span className={classes.tooltip}>{"Run"}</span>
      {/* Run */}
    </button>
  );
};

export default Run;
