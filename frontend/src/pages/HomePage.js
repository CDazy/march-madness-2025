import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/HomePage.css';

function HomePage() {
  return (
    <div className="home-page">
      <div className="hero-section">
        <h1>March Madness 2025 Simulator</h1>
        <p>Predict, analyze, and simulate the tournament!</p>
        <div className="home-actions">
          <Link to="/teams" className="btn">View Teams</Link>
          <Link to="/bracket" className="btn">Start Simulation</Link>
        </div>
      </div>
      <div className="features-section">
        <div className="feature">
          <h3>Team Analysis</h3>
          <p>Dive deep into team statistics and performance</p>
        </div>
        <div className="feature">
          <h3>Bracket Simulation</h3>
          <p>Run multiple tournament scenarios</p>
        </div>
        <div className="feature">
          <h3>Detailed Insights</h3>
          <p>Comprehensive team and matchup data</p>
        </div>
      </div>
    </div>
  );
}

export default HomePage;