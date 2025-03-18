import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';

function BracketPage() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    async function loadTeams() {
      const teamData = await fetchTeams();
      setTeams(teamData);
    }
    loadTeams();
  }, []);

  return (
    <div className="bracket-page">
      <h1>Tournament Bracket</h1>
      <div className="bracket-controls">
        <button>Simulate Tournament</button>
        <button>Reset Bracket</button>
      </div>
      <div className="bracket-visualization">
        {/* Placeholder for bracket visualization */}
        <p>Bracket visualization coming soon</p>
      </div>
    </div>
  );
}

export default BracketPage;