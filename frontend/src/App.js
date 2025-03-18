import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage.js';
import TeamsPage from './pages/TeamsPage.js';
import BracketPage from './pages/BracketPage.js';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/teams" element={<TeamsPage />} />
          <Route path="/bracket" element={<BracketPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;