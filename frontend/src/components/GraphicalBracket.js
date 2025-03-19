import React from 'react';
import { Bracket } from 'react-brackets';
import '../styles/GraphicalBracket.css';

function GraphicalBracket({ tournamentBracket }) {
    const formatTeamName = (team, isRtl) => {
        // Basic team name with dot handling
        let formattedName = team.name;
        
        // For RTL regions, move the dot to the end if it exists
        if (isRtl && formattedName.includes('.')) {
            const parts = formattedName.split('.');
            formattedName = `${parts.slice(0, -1).join('.')} .${parts[parts.length - 1]}`;
        }
        
        // Add seed after the name for RTL regions, before the name for others
        return isRtl 
            ? `${formattedName} ${team.seed}` 
            : `${team.seed} ${formattedName}`;
    };

    const convertRegionToRounds = (regionData, isRtl = false) => {
        // Define the correct matchup order for first round
        const firstRoundOrder = [
          { index1: 0, index2: 7 },   // 1 vs 16
          { index1: 7, index2: 0 },   // 8 vs 9
          { index1: 4, index2: 3 },   // 5 vs 12
          { index1: 3, index2: 4 },   // 3 vs 14
          { index1: 5, index2: 2 },   // 6 vs 11
          { index1: 2, index2: 5 },   // 3 vs 14
          { index1: 6, index2: 1 },   // 7 vs 10
          { index1: 1, index2: 6 },   // 2 vs 15
        ];
      
        return [
          {
            title: 'First Round',
            seeds: firstRoundOrder.map(({ index1, index2 }) => ({
              id: index1 + 1,
              teams: [
                { name: formatTeamName(regionData.firstRound[index1].team1, isRtl) },
                { name: formatTeamName(regionData.firstRound[index1].team2, isRtl) }
              ]
            }))
          },
          {
            title: 'Second Round',
            seeds: regionData.secondRound.map((matchup, index) => ({
              id: index + 1,
              teams: [
                { name: formatTeamName(matchup.team1, isRtl) },
                { name: formatTeamName(matchup.team2, isRtl) }
              ]
            }))
          },
          {
            title: 'Sweet Sixteen',
            seeds: regionData.sweetSixteen.map((matchup, index) => ({
              id: index + 1,
              teams: [
                { name: formatTeamName(matchup.team1, isRtl) },
                { name: formatTeamName(matchup.team2, isRtl) }
              ]
            }))
          },
          {
            title: 'Elite Eight',
            seeds: regionData.eliteEight.map((matchup, index) => ({
              id: index + 1,
              teams: [
                { name: formatTeamName(matchup.team1, isRtl) },
                { name: formatTeamName(matchup.team2, isRtl) }
              ]
            }))
          }
        ];
      };

  const convertFinalFourToRounds = (finalFour, championship) => {
    return [
      {
        title: 'Final Four',
        seeds: finalFour.map((matchup, index) => ({
          id: index + 1,
          date: 'April 5, 2025',
          teams: [
            { name: `${matchup.team1.seed} ${matchup.team1.name}` },
            { name: `${matchup.team2.seed} ${matchup.team2.name}` }
          ]
        }))
      },
      {
        title: 'Championship',
        seeds: [
          {
            id: 1,
            date: 'April 7, 2025',
            teams: [
              { name: `${championship.team1.seed} ${championship.team1.name}` },
              { name: `${championship.team2.seed} ${championship.team2.name}` }
            ]
          }
        ]
      }
    ];
  };

  return (
    <div className="graphical-tournament-bracket">
      <div className="top-regions">
        <div className="region-bracket west-region">
          <h3>West Region</h3>
          <Bracket 
            rounds={convertRegionToRounds(tournamentBracket.regions.West)}
            mobileBreakpoint={300}
          />
        </div>
        
        <div className="region-bracket east-region">
          <h3>East Region</h3>
          <Bracket 
            rounds={convertRegionToRounds(tournamentBracket.regions.East, true)}
            rtl
            mobileBreakpoint={300}
          />
        </div>
      </div>

      <div className="final-stages">
        <h2>Final Four</h2>
        <Bracket 
          rounds={convertFinalFourToRounds(
            tournamentBracket.finalFour, 
            tournamentBracket.championship
          )}
          mobileBreakpoint={300}
        />
        <div className="champion">
          <h1>Champion: {tournamentBracket.champion.name}</h1>
        </div>
      </div>

      <div className="bottom-regions">
        <div className="region-bracket midwest-region">
          <h3>Midwest Region</h3>
          <Bracket 
            rounds={convertRegionToRounds(tournamentBracket.regions.Midwest)}
            mobileBreakpoint={300}
          />
        </div>
        <div className="region-bracket south-region">
          <h3>South Region</h3>
          <Bracket 
            rounds={convertRegionToRounds(tournamentBracket.regions.South, true)}
            rtl
            mobileBreakpoint={300}
          />
        </div>
      </div>
    </div>
  );
}

export default GraphicalBracket;