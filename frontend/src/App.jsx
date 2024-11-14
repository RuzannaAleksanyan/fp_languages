import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';

function App() {
  const [value, setValue] = useState('');
  const [result, setResult] = useState(''); // State for the output
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Load the dark mode preference from localStorage
  useEffect(() => {
    const storedMode = localStorage.getItem('isDarkMode');
    if (storedMode) {
      setIsDarkMode(JSON.parse(storedMode));
    }
  }, []);

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
      setResult(data.output); // Set the output result
    } catch (error) {
      console.error('Error:', error);
      setResult('Error processing request');
    }
  };

  return (
    <div
      className="App"
      style={{
        backgroundColor: isDarkMode ? 'black' : 'white',
        color: isDarkMode ? 'white' : 'black',
        height: '90vh',
        display: 'flex',
        flexDirection: 'column',
        transition: 'background-color 0.3s ease',
      }}
    >
      {/* Top Controls */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          padding: '10px',
          height: '80px',
        }}
      >
        <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
        <Run onRun={handleRun} /> {/* Pass handleRun to Run */}
        <Clear value={value} setValue={setValue} />
      </div>

      {/* Main container with two columns */}
      <div
        style={{
          display: 'flex',
          flex: 1,
          flexDirection: 'row',
          height: 'calc(100vh - 80px)', 
        }}
      >
        <div
          style={{
            flex: 1,
            padding: '10px',
            height: '100%',
          }}
        >
          <Input value={value} setValue={setValue} />
        </div>
        <div
          style={{
            flex: 1,
            padding: '10px',
            height: '100%',
          }}
        >
          <Output result={result} /> {/* Pass result to Output */}
        </div>
      </div>
    </div>
  );
}

export default App;
