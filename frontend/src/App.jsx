import { useState } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';

function App() {
  const [value, setValue] = useState('')
  return (
    <div className="App">
      <Input value={value} setValue={setValue} /> 
      {/* {value} */}
      <Output/>
    </div>
  );
}

export default App;