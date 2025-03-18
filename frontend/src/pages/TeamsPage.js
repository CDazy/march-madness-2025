import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';

function TeamsPage() {
  const [teams, setTeams] = useState([]);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    async function loadTeams() {
      const teamData = await fetchTeams();
      setTeams(teamData);
    }
    loadTeams();
  }, []);

  const filteredTeams = teams.filter(team => 
    team.name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div className="teams-page">
      <h1>Tournament Teams</h1>
      <input 
        type="text" 
        placeholder="Search teams..." 
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      <div className="teams-grid">
        {filteredTeams.map(team => (
          <div key={team.id} className="team-card">
            <h3>{team.name}</h3>
            <p>Seed: {team.seed}</p>
            <p>Region: {team.region}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TeamsPage;