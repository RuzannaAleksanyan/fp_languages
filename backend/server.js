const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3001; // You can change the port if needed

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Endpoint to receive input data
app.post('/api/input', (req, res) => {
  const { userInput } = req.body;
  console.log(`Received input: ${userInput}`);

  // Here you can process the input (e.g., save it, transform it, etc.)
  
  res.status(200).json({ message: 'Input received successfully', receivedInput: userInput });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
