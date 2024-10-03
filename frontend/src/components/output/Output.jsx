import React from 'react';
import classes from './Output.module.css'

const OutputField = ({ value, setValue }) => {
    return (
        <div className={classes.outputContainer}>
            <input
                type="text"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                className={classes.outputField}
                placeholder="Output"
                aria-label="Back output"
            />
        </div>
    );
};

export default OutputField;
