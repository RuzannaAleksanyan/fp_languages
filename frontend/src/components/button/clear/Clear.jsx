// import React from 'react';
// import classes from './Clear.module.css';

// const ClearField = ({ value, setValue }) => {
//   const handleClick = () => {
//     if (value !== '') {
//       console.log('Clearing input!');
//       setValue('');
//     } else {
//       console.log('Nothing to clear!');
//     }
//   };

//   return (
//     <div className={classes.clearContainer}>
//       <button onClick={handleClick} className={classes.clearField}>
//         Clear
//       </button>
//     </div>
//   );
// };

// export default ClearField;



import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEraser } from '@fortawesome/free-solid-svg-icons';
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
      <FontAwesomeIcon icon={faEraser} style={{ marginRight: '5px' }} />
      Clear
    </button>
  );
};

export default ClearField;
