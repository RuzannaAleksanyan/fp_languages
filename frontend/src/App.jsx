import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';

function App() {
  const [value, setValue] = useState(''); // State for input value
  const [isDarkMode, setIsDarkMode] = useState(false); // Define isDarkMode state

  // Load the dark mode preference from localStorage
  useEffect(() => {
    const storedMode = localStorage.getItem('isDarkMode');
    if (storedMode) {
      setIsDarkMode(JSON.parse(storedMode)); // Parse and set the dark mode state
    }
  }, []);

  // Function to toggle dark mode
  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => {
      const newMode = !prevMode;
      localStorage.setItem('isDarkMode', JSON.stringify(newMode)); // Save the new preference
      return newMode;
    });
  };
  
  return (
    <div
      className="App"
      style={{
        backgroundColor: isDarkMode ? 'black' : 'white',
        color: isDarkMode ? 'white' : 'black',
        height: '100vh', // Make sure it covers the full height of the screen
        transition: 'background-color 0.3s ease', // Smooth transition
      }}
    >
      <Input value={value} setValue={setValue} /> 
      <Output/>
      {/* Pass the `value` as `inputValue` to Run */}
      <Run inputValue={value} />
      <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
      <Clear/>
    </div>
  );
}

export default App;
