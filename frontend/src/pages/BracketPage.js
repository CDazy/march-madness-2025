import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';
import { simulateTournament } from '../services/simulationService';
import GraphicalBracket from '../components/GraphicalBracket';
import '../styles/BracketPage.css';

function BracketPage() {
  const [teams, setTeams] = useState([]);
  const [tournamentBracket, setTournamentBracket] = useState(null);

  useEffect(() => {
    async function loadTeams() {
      const teamData = await fetchTeams();
      setTeams(teamData);
    }
    loadTeams();
  }, []);

  const handleSimulateTournament = () => {
    const simulatedBracket = simulateTournament(teams);
    setTournamentBracket(simulatedBracket);
  };

  const handleManualWinnerSelect = (matchup, selectedWinner) => {
    // Logic to manually override simulation
    console.log('Manual winner selected:', selectedWinner.name);
    // You'll need to implement logic to update the bracket
  };

  return (
    <div className="bracket-page">
      <h1>Tournament Bracket Simulator</h1>
      <button onClick={handleSimulateTournament}>
        Simulate Tournament
      </button>
      
      {tournamentBracket && (
        <GraphicalBracket
          tournamentBracket={tournamentBracket}
          onManualWinnerSelect={handleManualWinnerSelect}
        />
      )}
    </div>
  );
}

export default BracketPage;