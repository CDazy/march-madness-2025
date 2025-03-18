// Simulate a single matchup between two teams
const simulateMatchup = (team1, team2) => {
    // Calculate a performance score
    const calculateTeamScore = (team) => {
      return (
        team.k_off * 0.4 +  // Offensive rating
        (100 - team.k_def) * 0.4 +  // Defensive rating (inverted)
        team.efg_pct * 0.1 +  // Effective Field Goal %
        team.ft_pct * 0.1     // Free Throw %
      );
    };
  
    const team1Score = calculateTeamScore(team1);
    const team2Score = calculateTeamScore(team2);
  
    return {
      team1,
      team2,
      winner: team1Score > team2Score ? team1 : team2,
      loser: team1Score > team2Score ? team2 : team1
    };
  };
  
  // Simulate first round matchups
  const simulateFirstRound = (teams, regionTeams) => {
    const matchups = [];
    
    // Identify and simulate play-in games
    const playInMatchups = [
      { 
        team1: teams.find(t => t.name === 'Texas'), 
        team2: teams.find(t => t.name === 'Xavier'),
        region: 'Midwest'
      },
      { 
        team1: teams.find(t => t.name === 'North Carolina'), 
        team2: teams.find(t => t.name === 'San Diego St.'),
        region: 'South'
      },
      { 
        team1: teams.find(t => t.name === 'Alabama St.'), 
        team2: teams.find(t => t.name === 'Saint Francis'),
        region: 'South'
      },
      { 
        team1: teams.find(t => t.name === 'American'), 
        team2: teams.find(t => t.id === 67),
        region: 'East'
      }
    ];
  
    // Simulate play-in games
    const playInWinners = playInMatchups.map(matchup => ({
      winner: simulateMatchup(matchup.team1, matchup.team2).winner,
      region: matchup.region
    }));
  
    // Remove losing play-in teams from region teams
    const adjustedRegionTeams = regionTeams.filter(team => 
      !playInMatchups.some(matchup => 
        matchup.team1 === team || matchup.team2 === team
      )
    );
  
    // Add play-in winners only to their specific region
    const finalRegionTeams = adjustedRegionTeams.concat(
      playInWinners
        .filter(pw => pw.winner.region === regionTeams[0].region)
        .map(pw => pw.winner)
    );
  
    // Sort teams by seed to ensure correct matchups
    finalRegionTeams.sort((a, b) => a.seed - b.seed);
  
    // Create matchups based on seed order
    for (let i = 0; i < 8; i++) {
      const team1 = finalRegionTeams[i];
      const team2 = finalRegionTeams[15 - i];
      matchups.push(simulateMatchup(team1, team2));
    }
  
    return matchups;
  };
  
  // Simulate second round (Round of 32)
  const simulateSecondRound = (firstRoundMatchups) => {
    const nextRoundMatchups = [];
    
    // Matchup order: 1/16 vs 8/9, 5/12 vs 4/13, 6/11 vs 3/14, 7/10 vs 2/15
    const matchupOrder = [
      { index1: 0, index2: 7 },   // 1/16 vs 8/9
      { index1: 4, index2: 3 },   // 5/12 vs 4/13
      { index1: 5, index2: 2 },   // 6/11 vs 3/14
      { index1: 6, index2: 1 }    // 7/10 vs 2/15
    ];
  
    matchupOrder.forEach(({ index1, index2 }) => {
      const team1 = firstRoundMatchups[index1].winner;
      const team2 = firstRoundMatchups[index2].winner;
      nextRoundMatchups.push(simulateMatchup(team1, team2));
    });
  
    return nextRoundMatchups;
  };
  
  // Simulate Sweet Sixteen
  const simulateSweetSixteen = (secondRoundMatchups) => {
    const nextRoundMatchups = [];
    
    // Sweet Sixteen matchup order
    const matchupOrder = [
      { index1: 0, index2: 1 },   // Winner of 1/16 vs 8/9 plays winner of 5/12 vs 4/13
      { index1: 2, index2: 3 }    // Winner of 6/11 vs 3/14 plays winner of 7/10 vs 2/15
    ];
  
    matchupOrder.forEach(({ index1, index2 }) => {
      const team1 = secondRoundMatchups[index1].winner;
      const team2 = secondRoundMatchups[index2].winner;
      nextRoundMatchups.push(simulateMatchup(team1, team2));
    });
  
    return nextRoundMatchups;
  };
  
  // Simulate Elite Eight
  const simulateEliteEight = (sweetSixteenMatchups) => {
    return [
      simulateMatchup(sweetSixteenMatchups[0].winner, sweetSixteenMatchups[1].winner)
    ];
  };
  
  // Simulate Final Four
const simulateFinalFour = (eliteEightMatchups) => {
    // Assuming eliteEightMatchups contains the champions of each region
    return [
      simulateMatchup(eliteEightMatchups[0].winner, eliteEightMatchups[2].winner),  // South vs West
      simulateMatchup(eliteEightMatchups[1].winner, eliteEightMatchups[3].winner)   // East vs Midwest
    ];
  };
  
  // Simulate Championship
  const simulateChampionship = (finalFourMatchups) => {
    return simulateMatchup(finalFourMatchups[0].winner, finalFourMatchups[1].winner);
  };
  
  // Simulate entire tournament
  export const simulateTournament = (teams) => {
    const regions = ['South', 'East', 'West', 'Midwest'];
    const tournamentBracket = {
      regions: {},
      finalFour: null,
      championship: null,
      champion: null
    };
  
    const regionChampions = [];
  
    regions.forEach(region => {
      // Filter and sort teams in this region
      const regionTeams = teams
        .filter(team => team.region === region)
        .sort((a, b) => a.seed - b.seed);
  
      // First Round
      const firstRoundMatchups = simulateFirstRound(teams, regionTeams);
      
      // Second Round (Round of 32)
      const secondRoundMatchups = simulateSecondRound(firstRoundMatchups);
      
      // Sweet Sixteen
      const sweetSixteenMatchups = simulateSweetSixteen(secondRoundMatchups);
      
      // Elite Eight
      const eliteEightMatchups = simulateEliteEight(sweetSixteenMatchups);
      
      // Store region champion
      regionChampions.push(eliteEightMatchups[0]);
  
      // Store region details
      tournamentBracket.regions[region] = {
        firstRound: firstRoundMatchups,
        secondRound: secondRoundMatchups,
        sweetSixteen: sweetSixteenMatchups,
        eliteEight: eliteEightMatchups,
        regionChampion: eliteEightMatchups[0].winner
      };
    });
  
    // Final Four
    const finalFourMatchups = simulateFinalFour(regionChampions);
    tournamentBracket.finalFour = finalFourMatchups;
  
    // Championship
    const championshipGame = simulateChampionship(finalFourMatchups);
    tournamentBracket.championship = championshipGame;
    tournamentBracket.champion = championshipGame.winner;
  
    return tournamentBracket;
  };