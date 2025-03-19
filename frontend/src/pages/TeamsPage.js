import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';
import '../styles/TeamsPage.css';

function TeamsPage() {
  const [teams, setTeams] = useState([]);
  const [filter, setFilter] = useState('');
  const [sortConfig, setSortConfig] = useState({ key: 'seed', direction: 'ascending' });

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

  // Define all columns to display, with seed and name swapped
  const columns = [
    'seed', 'name', 'region', 
    'k_off', 'k_def', 
    'efg_pct', 'efg_pct_def',
    'oreb_pct', 'dreb_pct',
    'op_oreb_pct', 'op_dreb_pct',
    'two_pt_pct', 'two_pt_pct_def',
    'three_pt_pct', 'three_pt_pct_def',
    'ft_pct', 'elite_sos'
  ];

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
      <div className="table-container">
        <table className="teams-table">
          <thead>
            <tr>
              {columns.map(column => (
                <th 
                  key={column} 
                  onClick={() => requestSort(column)}
                >
                  {column.replace(/_/g, ' ').toUpperCase()}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
          {filteredTeams.map((team, index) => (
            <tr key={index}>
              {columns.map(column => (
                <td key={column}>
                  {typeof team[column] === 'number' 
                    ? (column === 'seed' 
                      ? team[column] 
                      : team[column].toFixed(2)) 
                    : team[column]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
        </table>
      </div>
    </div>
  );
}

export default TeamsPage;