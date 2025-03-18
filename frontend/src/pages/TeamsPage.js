import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';
import '../styles/TeamsPage.css';  // Add this import

function TeamsPage() {
  const [teams, setTeams] = useState([]);
  const [filter, setFilter] = useState('');
  const [sortConfig, setSortConfig] = useState({ key: 'name', direction: 'ascending' });

  useEffect(() => {
    async function loadTeams() {
      const teamData = await fetchTeams();
      setTeams(teamData);
    }
    loadTeams();
  }, []);

  const sortedTeams = React.useMemo(() => {
    let sortableTeams = [...teams];
    sortableTeams.sort((a, b) => {
      if (a[sortConfig.key] < b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? -1 : 1;
      }
      if (a[sortConfig.key] > b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? 1 : -1;
      }
      return 0;
    });
    return sortableTeams;
  }, [teams, sortConfig]);

  const filteredTeams = sortedTeams.filter(team => 
    team.name.toLowerCase().includes(filter.toLowerCase())
  );

  const requestSort = (key) => {
    let direction = 'ascending';
    if (sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    setSortConfig({ key, direction });
  };

  return (
    <div className="teams-page">
      <h1>Tournament Teams</h1>
      <div className="teams-controls">
        <input 
          type="text" 
          placeholder="Search teams..." 
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        />
      </div>
      <table className="teams-table">
        <thead>
          <tr>
            <th onClick={() => requestSort('name')}>Name</th>
            <th onClick={() => requestSort('seed')}>Seed</th>
            <th onClick={() => requestSort('region')}>Region</th>
            <th onClick={() => requestSort('k_off')}>Offensive Rating</th>
            <th onClick={() => requestSort('k_def')}>Defensive Rating</th>
          </tr>
        </thead>
        <tbody>
          {filteredTeams.map(team => (
            <tr key={team.id}>
              <td>{team.name}</td>
              <td>{team.seed}</td>
              <td>{team.region}</td>
              <td>{team.k_off.toFixed(2)}</td>
              <td>{team.k_def.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TeamsPage;