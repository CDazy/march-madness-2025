import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="home-page">
      <h1>March Madness Simulator 2025</h1>
      <div className="home-actions">
        <Link to="/teams" className="btn">View Teams</Link>
        <Link to="/bracket" className="btn">Start Simulation</Link>
      </div>
      <div className="tournament-overview">
        {/* Could add tournament stats or preview */}
        <h2>Tournament Preview</h2>
        {/* Add some initial content */}
      </div>
    </div>
  );
}

export default HomePage;