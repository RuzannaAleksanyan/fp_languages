import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';

function App() {
  const [value, setValue] = useState('');
  const [result, setResult] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Load the dark mode preference from localStorage
  useEffect(() => {
    const storedMode = localStorage.getItem('isDarkMode');
    if (storedMode) {
      setIsDarkMode(JSON.parse(storedMode));
    }
  }, []);

  // Apply dark mode class to the body
  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }, [isDarkMode]);

  // Function to toggle dark mode
  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => {
      const newMode = !prevMode;
      localStorage.setItem('isDarkMode', JSON.stringify(newMode));
      return newMode;
    });
  };

  // Function to send the input to the server and receive the output
  const handleRun = async () => {
    try {
      const response = await fetch('http://localhost:3001/api/input', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userInput: value }),
      });
      const data = await response.json();
      setResult(data.output);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error processing request');
    }
  };

  return (
    <div className="App" >
      <div className={`buttons ${isDarkMode ? 'dark' : 'light'}`}>
        <div class="logo-container">
          <img src={require('./logo.png')} alt="Logo" />
        </div>

        <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
        <Run onRun={handleRun} isDarkMode={isDarkMode} />
        <Clear value={value} setValue={setValue} isDarkMode={isDarkMode} />
      </div>      

      <div className={`stream ${isDarkMode ? 'dark' : 'light'}`} >
        <div>
          <Input value={value} setValue={setValue} />
        </div>
        <div>
          <Output result={result} />
        </div>
      </div>
    </div>
  );
}

export default App;
