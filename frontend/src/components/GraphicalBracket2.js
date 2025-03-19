import React from 'react';
import { Bracket } from 'react-tournament-bracket';
import '../styles/GraphicalBracket.css';

function GraphicalBracket2({ tournamentBracket }) {
    const convertMatchupToGame = (matchup, roundIndex, matchupIndex) => {
        const gameId = `game-${roundIndex}-${matchupIndex}`;
        
        return {
          '@id': gameId,
          'id': gameId,
          'version': 1,
          'created': Date.now(),
          'updated': Date.now(),
          'name': `${matchup.team1.name} vs ${matchup.team2.name}`,
          'sides': {
            'home': {
              'team': {
                '@id': matchup.team1.name,
                'id': matchup.team1.name,
                'name': matchup.team1.name
              },
              'seed': {
                'rank': matchup.team1.seed || 0,
                'displayName': `${matchup.team1.seed} seed`
              },
              'score': null
            },
            'visitor': {
              'team': {
                '@id': matchup.team2.name,
                'id': matchup.team2.name,
                'name': matchup.team2.name
              },
              'seed': {
                'rank': matchup.team2.seed || 0,
                'displayName': `${matchup.team2.seed} seed`
              },
              'score': null
            }
          },
          'homeTeam': {
            '@id': matchup.team1.name,
            'id': matchup.team1.name,
            'name': matchup.team1.name
          },
          'visitorTeam': {
            '@id': matchup.team2.name,
            'id': matchup.team2.name,
            'name': matchup.team2.name
          },
          'homeScore': null,
          'visitorScore': null,
          'winner': {
            'team': {
              'name': matchup.winner ? matchup.winner.name : null
            }
          }
        };
      };

  return (
    <div className="graphical-tournament-bracket">
      <div className="regions-container">
        {tournamentBracket && Object.entries(tournamentBracket.regions).map(
          ([regionName, regionData], index) => (
            <div key={index} className="region-bracket">
              <h3>{regionName} Region</h3>
              <Bracket 
  game={{
    '@id': `${regionName}-root`,
    'id': `${regionName}-root`,
    'name': `${regionName} Region Tournament`,
    'sides': {
      'home': {},
      'visitor': {}
    },
    'rounds': [
      regionData.firstRound.map((matchup, matchupIndex) => {
        const game = convertMatchupToGame(matchup, 0, matchupIndex);
        console.log(`First Round Game ${matchupIndex}:`, game);
        return game;
      }),
      regionData.secondRound.map((matchup, matchupIndex) => {
        const game = convertMatchupToGame(matchup, 1, matchupIndex);
        console.log(`Second Round Game ${matchupIndex}:`, game);
        return game;
      }),
      regionData.sweetSixteen.map((matchup, matchupIndex) => {
        const game = convertMatchupToGame(matchup, 2, matchupIndex);
        console.log(`Sweet Sixteen Game ${matchupIndex}:`, game);
        return game;
      }),
      regionData.eliteEight.map((matchup, matchupIndex) => {
        const game = convertMatchupToGame(matchup, 3, matchupIndex);
        console.log(`Elite Eight Game ${matchupIndex}:`, game);
        return game;
      })
    ]
  }}
/>
            </div>
          )
        )}
      </div>

      {tournamentBracket && tournamentBracket.finalFour && (
        <div className="final-stages">
          <h2>Final Four & Championship</h2>
          <Bracket 
            game={{
              '@id': 'final-four-root',
              'id': 'final-four-root',
              'name': 'Final Four Tournament',
              'sides': {
                'home': {},
                'visitor': {}
              },
              'rounds': [
                tournamentBracket.finalFour.map((matchup, matchupIndex) => 
                  convertMatchupToGame(matchup, 0, matchupIndex)
                ),
                [convertMatchupToGame(tournamentBracket.championship, 1, 0)]
              ]
            }}
          />
          <div className="champion">
            <h3>Champion: {tournamentBracket.champion.name}</h3>
          </div>
        </div>
      )}
    </div>
  );
}

export default GraphicalBracket2;