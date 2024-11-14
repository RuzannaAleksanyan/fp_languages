// // import React from 'react';
// // import classes from './Run.module.css';

// // const RunField = ({ inputValue }) => {
// //   const handleClick = async () => {
// //     console.log('Button clicked!');
// //     console.log('Input value:', inputValue);

// //     try {
// //       const response = await fetch('http://localhost:3001/api/input', {
// //         method: 'POST',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify({ userInput: inputValue }),
// //       });

// //       const data = await response.json();
// //       console.log('Response from server:', data);
// //     } catch (error) {
// //       console.error('Error sending input:', error);
// //     }
// //   };

// //   return (
// //     <div className={classes.runContainer}>
// //       <button onClick={handleClick} className={classes.runField}>
// //         run
// //       </button>
// //     </div>
// //   );
// // };

// // export default RunField;



// // Run.jsx
// import React from 'react';
// import classes from './Run.module.css';

// const RunField = ({ onRun }) => {
//   return (
//     <div className={classes.runContainer}>
//       <button onClick={onRun} className={classes.runField}>
//         Run
//       </button>
//     </div>
//   );
// };

// export default RunField;


import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlay } from '@fortawesome/free-solid-svg-icons';
import classes from './Run.module.css';

const Run = ({ onRun }) => {
  return (
    <button onClick={onRun} className={classes.runButton}>
      <FontAwesomeIcon icon={faPlay} style={{ marginRight: '5px' }} />
      Run
    </button>
  );
};

export default Run;
