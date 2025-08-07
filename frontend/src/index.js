import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; // The main component for your entire application
import './index.css';   // Global styles

// 1. Find the "stage" (the div with id="root" from index.html).
const rootElement = document.getElementById('root');

// 2. Create a React root to manage rendering inside that element.
const root = ReactDOM.createRoot(rootElement);

// 3. Tell React to "start the play" by rendering the main <App /> component.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);