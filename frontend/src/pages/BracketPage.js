import React, { useState, useEffect } from 'react';
import { fetchTeams } from '../services/api';
import { simulateTournament } from '../services/simulationService';
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

  const renderRegionBracket = (regionName, regionData) => {
    if (!regionData) return null;

    return (
      <div key={regionName} className="region-bracket">
        <h3>{regionName} Region</h3>
        <div className="round">
          <h4>First Round</h4>
          {regionData.firstRound.map((matchup, index) => (
            <div key={index} className="matchup">
              <div>{matchup.team1.name} vs {matchup.team2.name}</div>
              <div>Winner: {matchup.winner.name}</div>
            </div>
          ))}
        </div>
        <div className="round">
          <h4>Second Round</h4>
          {regionData.secondRound.map((matchup, index) => (
            <div key={index} className="matchup">
              <div>{matchup.team1.name} vs {matchup.team2.name}</div>
              <div>Winner: {matchup.winner.name}</div>
            </div>
          ))}
        </div>
        <div className="round">
          <h4>Sweet Sixteen</h4>
          {regionData.sweetSixteen.map((matchup, index) => (
            <div key={index} className="matchup">
              <div>{matchup.team1.name} vs {matchup.team2.name}</div>
              <div>Winner: {matchup.winner.name}</div>
            </div>
          ))}
        </div>
        <div className="round">
          <h4>Elite Eight</h4>
          {regionData.eliteEight.map((matchup, index) => (
            <div key={index} className="matchup">
              <div>{matchup.team1.name} vs {matchup.team2.name}</div>
              <div>Winner: {matchup.winner.name}</div>
            </div>
          ))}
        </div>
        <div className="round">
          <h4>Region Champion</h4>
          <div>{regionData.regionChampion.name}</div>
        </div>
      </div>
    );
  };

  return (
    <div className="bracket-page">
      <h1>Tournament Bracket Simulator</h1>
      <button onClick={handleSimulateTournament}>
        Simulate Tournament
      </button>
      
      {tournamentBracket && (
        <div>
          <div className="tournament-bracket">
            {Object.entries(tournamentBracket.regions).map(([regionName, regionData]) => 
              renderRegionBracket(regionName, regionData)
            )}
          </div>
          <div className="final-stages">
            <h2>Final Four</h2>
            {tournamentBracket.finalFour.map((matchup, index) => (
              <div key={index} className="matchup">
                <div>{matchup.team1.name} vs {matchup.team2.name}</div>
                <div>Winner: {matchup.winner.name}</div>
              </div>
            ))}
            <h2>Championship</h2>
            <div className="matchup">
              <div>{tournamentBracket.championship.team1.name} vs {tournamentBracket.championship.team2.name}</div>
              <div>Champion: {tournamentBracket.champion.name}</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default BracketPage;