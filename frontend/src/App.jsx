import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';
import DropdownButton from './components/button/dropdown/DropdownButton';

function App() {
  const [value, setValue] = useState('');
  const [result, setResult] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedOption, setSelectedOption] = useState(""); // Default `""` instead of `null`

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

  // Function to send the input and dropdown value to the server
  const handleRun = async () => {
    console.log("Selected option before sending:", selectedOption);

    try {
      const response = await fetch('http://localhost:5000/api/input', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          userInput: value, 
          selectedOption: selectedOption // Ensuring it is sent
        }),
      });

      const data = await response.json();
      setResult(data.output);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error processing request');
    }
  };

  return (
    <div className="App">
      <div className={`buttons ${isDarkMode ? 'dark' : 'light'}`}>
        <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
        <Run onRun={handleRun} isDarkMode={isDarkMode} />
        <Clear value={value} setValue={setValue} isDarkMode={isDarkMode} />
        
        <DropdownButton onSelect={setSelectedOption} />
      </div>      

      <div className={`stream ${isDarkMode ? 'dark' : 'light'}`}>
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
