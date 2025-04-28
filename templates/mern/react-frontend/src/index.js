import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Optional, if you want to add styles
import App from './App'; // Import your root component

// Render the App component inside the div with id 'root'
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);