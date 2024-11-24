import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlay } from '@fortawesome/free-solid-svg-icons';
import classes from './Run.module.css';

const Run = ({ onRun, isDarkMode }) => {
  return (
    <button
      onClick={onRun}
      className={`${classes.runButton} ${isDarkMode ? classes.dark : classes.light}`}
    >
      <FontAwesomeIcon
        icon={faPlay}
        className={`${classes.icon} ${isDarkMode ? classes.dark : classes.light}`}
      />
      <span className={`${classes.tooltip} ${isDarkMode ? classes.dark : ''}`}>Run</span>
    </button>
  );
};

export default Run;
