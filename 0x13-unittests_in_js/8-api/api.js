const express = require('express');

const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
