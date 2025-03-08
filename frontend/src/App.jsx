// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import { useState, useEffect } from 'react';
// import './App.css';
// import Input from './components/input/Input';
// import Output from './components/output/Output';
// import Run from './components/button/run/Run';
// import DarkLight from './components/button/darklight/DarkLight';
// import Clear from './components/button/clear/Clear';
// import DropdownButton from './components/button/dropdown/DropdownButton';
// import InfoButton from './components/button/info/InfoButton';
// import InfoPage from './page/bekus/InfoPageBekus';
// import Home from './components/button/home/Home';

// function App() {
//   const [value, setValue] = useState('');
//   const [result, setResult] = useState('');
//   const [isDarkMode, setIsDarkMode] = useState(false);
//   const [selectedOption, setSelectedOption] = useState('');

//   useEffect(() => {
//     const storedMode = localStorage.getItem('isDarkMode');
//     if (storedMode) {
//       setIsDarkMode(JSON.parse(storedMode));
//     }
//   }, []);

//   useEffect(() => {
//     if (isDarkMode) {
//       document.body.classList.add('dark-mode');
//     } else {
//       document.body.classList.remove('dark-mode');
//     }
//   }, [isDarkMode]);

//   const toggleDarkMode = () => {
//     setIsDarkMode((prevMode) => {
//       const newMode = !prevMode;
//       localStorage.setItem('isDarkMode', JSON.stringify(newMode));
//       return newMode;
//     });
//   };

//   const handleRun = async () => {
//     try {
//       const response = await fetch('http://localhost:5000/api/input', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ userInput: value, selectedOption }),
//       });

//       const data = await response.json();
//       setResult(data.output);
//     } catch (error) {
//       console.error('Error:', error);
//       setResult('Error processing request');
//     }
//   };

//   return (
//     <Router>
//       <div className="App">
//         <div className={`buttons ${isDarkMode ? 'dark' : 'light'}`}>
//           <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
//           <Run onRun={handleRun} isDarkMode={isDarkMode} />
//           <Clear value={value} setValue={setValue} isDarkMode={isDarkMode} />
//           <DropdownButton onSelect={setSelectedOption} />
//           <InfoButton onSelect={setSelectedOption} />
//           <Home />
//         </div>

//         <Routes>
//           <Route path="/" element={
//             <div className={`stream ${isDarkMode ? 'dark' : 'light'}`}>
//               <Input value={value} setValue={setValue} />
//               <Output result={result} />
//             </div>
//           } />
//           <Route path="/info-bekus" element={<InfoPageBekus />} />
//           <Route path="/info-herbrand" element={<InfoPageHerbranGyodelKlini />} />
//         </Routes>
//       </div>
//     </Router>
//   );
// }

// export default App;

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';
import DropdownButton from './components/button/dropdown/DropdownButton';
import InfoButton from './components/button/info/InfoButton';
import InfoPageBekus from './page/bekus/InfoPageBekus';  // ✅ Անվանման ուղղում
import InfoPageHerbran from './page/herbran_gyodel_klini/InfoPageHerbranGyodelKlini'
import Home from './components/button/home/Home';

function App() {
  const [value, setValue] = useState('');
  const [result, setResult] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedOption, setSelectedOption] = useState('');

  useEffect(() => {
    const storedMode = localStorage.getItem('isDarkMode');
    if (storedMode) {
      setIsDarkMode(JSON.parse(storedMode));
    }
  }, []);

  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }, [isDarkMode]);

  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => {
      const newMode = !prevMode;
      localStorage.setItem('isDarkMode', JSON.stringify(newMode));
      return newMode;
    });
  };

  const handleRun = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/input', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userInput: value, selectedOption }),
      });

      if (!response.ok) {
        throw new Error('Server error');
      }

      const data = await response.json();
      setResult(data.output);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error processing request');
    }
  };

  return (
    <Router>
      <div className="App">
        <div className={`buttons ${isDarkMode ? 'dark' : 'light'}`}>
          <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
          <Run onRun={handleRun} isDarkMode={isDarkMode} />
          <Clear setValue={setValue} setResult={setResult} isDarkMode={isDarkMode} />  {/* ✅ setResult էլ փոխանցել */}
          <DropdownButton onSelect={setSelectedOption} />
          <InfoButton onSelect={selectedOption} />
          <Home />
        </div>

        <Routes>
          <Route
            path="/"
            element={
              <div className={`stream ${isDarkMode ? 'dark' : 'light'}`}>
                <Input value={value} setValue={setValue} />
                <Output result={result} />
              </div>
            }
          />
          <Route path="/info-bekus" element={<InfoPageBekus />} />
          <Route path="/info-herbrand" element={<InfoPageHerbran />} />  {/* ✅ Անվանման ուղղում */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
