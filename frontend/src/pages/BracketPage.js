import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';
import { simulateTournament, SimulationStrategies } from '../services/simulationService';
import GraphicalBracket from '../components/GraphicalBracket';
import '../styles/BracketPage.css';

function BracketPage() {
  const [teams, setTeams] = useState([]);
  const [tournamentBracket, setTournamentBracket] = useState(null);
  const [selectedStrategy, setSelectedStrategy] = useState(SimulationStrategies.CHALK);
  const [customStats, setCustomStats] = useState([]);

  useEffect(() => {
    async function loadTeams() {
      const teamData = await fetchTeams();
      setTeams(teamData);
    }
    loadTeams();
  }, []);

  const handleSimulateTournament = () => {
    const simulatedBracket = simulateTournament(
      teams, 
      selectedStrategy, 
      selectedStrategy === SimulationStrategies.CUSTOM ? customStats : []
    );
    setTournamentBracket(simulatedBracket);
  };

  const handleClearAllStats = () => {
    setCustomStats([]);
  };

  const availableStats = [
    'k_off', 'k_def', 'efg_pct', 'efg_pct_def', 
    'oreb_pct', 'dreb_pct', 'two_pt_pct', 
    'three_pt_pct', 'ft_pct', 'elite_sos'
  ];

  return (
    <div className="bracket-page">
      <div className="simulation-controls">
        <select 
          value={selectedStrategy}
          onChange={(e) => setSelectedStrategy(e.target.value)}
        >
          {Object.values(SimulationStrategies).map(strategy => (
            <option key={strategy} value={strategy}>
              {strategy.replace(/_/g, ' ')}
            </option>
          ))}
        </select>

        {selectedStrategy === SimulationStrategies.CUSTOM && (
          <div className="custom-stats-selector">
            <div className="stats-header">
              <h4>Select Custom Stats</h4>
              <label className="clear-all-checkbox">
                <input
                  type="checkbox"
                  checked={customStats.length === availableStats.length}
                  onChange={customStats.length === availableStats.length 
                    ? handleClearAllStats 
                    : () => setCustomStats([...availableStats])
                  }
                />
                {customStats.length === availableStats.length ? 'Clear All' : 'Select All'}
              </label>
            </div>
            <div className="stats-grid">
              {availableStats.map(stat => (
                <label key={stat} className="stat-checkbox">
                  <input
                    type="checkbox"
                    checked={customStats.includes(stat)}
                    onChange={() => {
                      setCustomStats(prev => 
                        prev.includes(stat) 
                          ? prev.filter(s => s !== stat)
                          : [...prev, stat]
                      );
                    }}
                  />
                  {stat}
                </label>
              ))}
            </div>
          </div>
        )}

        <button 
          onClick={handleSimulateTournament}
          disabled={teams.length === 0}
        >
          Simulate Tournament
        </button>
      </div>

      {tournamentBracket && (
        <GraphicalBracket tournamentBracket={tournamentBracket} />
      )}
    </div>
  );
}

export default BracketPage;