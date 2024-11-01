// import React from 'react';
// import classes from './Output.module.css';

// const OutputField = ({ result }) => {
//   return (
//     <div className={classes.outputContainer}>
//       <textarea
//         className={classes.outputField}
//         placeholder="Output"
//         value={result} // Display the result here
//         readOnly // Make it read-only to prevent user edits
//         aria-label="Back output"
//       />
//     </div>
//   );
// };

// export default OutputField;


// Output.jsx
import React from 'react';
import classes from './Output.module.css';

const OutputField = ({ result }) => {
  return (
    <div className={classes.outputContainer}>
      <textarea
        className={classes.outputField}
        placeholder="Output"
        value={result} // Display the result here
        readOnly // Make it read-only to prevent user edits
        aria-label="Back output"
      />
    </div>
  );
};

export default OutputField;
