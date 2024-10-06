import { useState } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';

import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';

function App() {
  const [value, setValue] = useState('')
  return (
    <div className="App">
      <Input value={value} setValue={setValue} /> 
      <Output/>

      <Run/>
      <DarkLight/>
      <Clear/>
    </div>
  );
}

export default App;