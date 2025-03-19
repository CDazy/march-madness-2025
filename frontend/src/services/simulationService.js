export const SimulationStrategies = {
  CHALK: 'Chalk',
  RANDOM: 'Random',
  CUSTOM: 'Custom',
  THREE_PT_FOCUS: 'Three_pt_Strategy',
  CURRENT: 'AI_Strategy',
  ENHANCED_CURRENT: 'Enhanced_AI_Strategy',
  STATISTICAL_SCORING: 'All_Stats',
};

export const simulateMatchup = (team1, team2, strategy, customStats = []) => {
  switch(strategy) {
    case SimulationStrategies.CHALK:
      return chalkSimulation(team1, team2);
    case SimulationStrategies.STATISTICAL_SCORING:
      return statisticalScoringSimulation(team1, team2);
    case SimulationStrategies.CURRENT:
      return currentSimulation(team1, team2);
    case SimulationStrategies.ENHANCED_CURRENT:
      return enhancedCurrentSimulation(team1, team2);
    case SimulationStrategies.THREE_PT_FOCUS:
      return threePtFocusSimulation(team1, team2);
    case SimulationStrategies.RANDOM:
      return randomSimulation(team1, team2);
    case SimulationStrategies.CUSTOM:
      return customStatSimulation(team1, team2, customStats);
    default:
      return currentSimulation(team1, team2);
  }
};


const chalkSimulation = (team1, team2) => {
  if (team1.seed < team2.seed) {
    return { 
      team1, 
      team2, 
      winner: team1, 
      loser: team2 
    };
  }
  if (team2.seed < team1.seed) {
    return { 
      team1, 
      team2, 
      winner: team2, 
      loser: team1 
    };
  }
  
  // Tie-breaker: random
  const winner = Math.random() < 0.5 ? team1 : team2;
  const loser = winner === team1 ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const statisticalScoringSimulation = (team1, team2) => {
  let team1Score = 0;
  let team2Score = 0;

  // Seed advantage
  if (team1.seed < team2.seed) team1Score += 2;
  if (team2.seed < team1.seed) team2Score += 2;

  // Offensive Rating
  if (team1.k_off > team2.k_off) team1Score += 2;
  if (team2.k_off > team1.k_off) team2Score += 2;

  // Defensive Rating
  if (team1.k_def < team2.k_def) team1Score += 2;
  if (team2.k_def < team1.k_def) team2Score += 2;

  // EFG%
  if (team1.efg_pct > team2.efg_pct) team1Score += 1;
  if (team2.efg_pct > team1.efg_pct) team2Score += 1;

  // EFG%D
  if (team1.efg_pct_def < team2.efg_pct_def) team1Score += 1;
  if (team2.efg_pct_def < team1.efg_pct_def) team2Score += 1;

  // Continue with other stats...
  // (Full implementation as in previous version)

  const winner = team1Score > team2Score ? team1 : team2;
  const loser = team1Score > team2Score ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const currentSimulation = (team1, team2) => {
  const calculateTeamScore = (team) => (
    team.k_off * 0.4 +
    (100 - team.k_def) * 0.4 +
    team.efg_pct * 0.1 +
    team.ft_pct * 0.1
  );

  const team1Score = calculateTeamScore(team1);
  const team2Score = calculateTeamScore(team2);

  const winner = team1Score > team2Score ? team1 : team2;
  const loser = team1Score > team2Score ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const enhancedCurrentSimulation = (team1, team2) => {
  const calculateTeamScore = (team) => (
    team.k_off * 0.35 +
    (100 - team.k_def) * 0.35 +
    team.efg_pct * 0.1 +
    team.ft_pct * 0.1 +
    team.elite_sos * 0.1
  );

  const team1Score = calculateTeamScore(team1);
  const team2Score = calculateTeamScore(team2);

  const winner = team1Score > team2Score ? team1 : team2;
  const loser = team1Score > team2Score ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const threePtFocusSimulation = (team1, team2) => {
  const calculateTeamScore = (team) => (
    team.three_pt_pct * 0.7 +
    team.elite_sos * 0.3
  );

  const team1Score = calculateTeamScore(team1);
  const team2Score = calculateTeamScore(team2);

  const winner = team1Score > team2Score ? team1 : team2;
  const loser = team1Score > team2Score ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const randomSimulation = (team1, team2) => {
  const winner = Math.random() < 0.5 ? team1 : team2;
  const loser = winner === team1 ? team2 : team1;
  
  return { team1, team2, winner, loser };
};

const customStatSimulation = (team1, team2, customStats) => {
  let team1Score = 0;
  let team2Score = 0;

  customStats.forEach(stat => {
    if (team1[stat] > team2[stat]) team1Score++;
    if (team2[stat] > team1[stat]) team2Score++;
  });

  const winner = team1Score > team2Score ? team1 : team2;
  const loser = team1Score > team2Score ? team2 : team1;
  
  return { team1, team2, winner, loser };
};




  
  // Simulate first round matchups
  const simulateFirstRound = (teams, regionTeams, strategy, customStats = []) => {
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
      winner: simulateMatchup(matchup.team1, matchup.team2, strategy, customStats).winner,
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
      matchups.push(simulateMatchup(team1, team2, strategy, customStats));
    }
  
    return matchups;
  };
  
  // Simulate second round (Round of 32)
  const simulateSecondRound = (firstRoundMatchups, strategy, customStats = []) => {
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
      nextRoundMatchups.push(simulateMatchup(team1, team2, strategy, customStats));
    });
  
    return nextRoundMatchups;
  };
  
  // Simulate Sweet Sixteen
  const simulateSweetSixteen = (secondRoundMatchups, strategy, customStats = []) => {
    const nextRoundMatchups = [];
    
    // Sweet Sixteen matchup order
    const matchupOrder = [
      { index1: 0, index2: 1 },   // Winner of 1/16 vs 8/9 plays winner of 5/12 vs 4/13
      { index1: 2, index2: 3 }    // Winner of 6/11 vs 3/14 plays winner of 7/10 vs 2/15
    ];
  
    matchupOrder.forEach(({ index1, index2 }) => {
      const team1 = secondRoundMatchups[index1].winner;
      const team2 = secondRoundMatchups[index2].winner;
      nextRoundMatchups.push(simulateMatchup(team1, team2, strategy, customStats));
    });
  
    return nextRoundMatchups;
  };
  
  // Simulate Elite Eight
  const simulateEliteEight = (sweetSixteenMatchups, strategy, customStats = []) => {
    return [
      simulateMatchup(
        sweetSixteenMatchups[0].winner, 
        sweetSixteenMatchups[1].winner, 
        strategy, 
        customStats
      )
    ];
  };
  
  // Simulate Final Four
  const simulateFinalFour = (eliteEightMatchups, strategy, customStats = []) => {
    return [
      simulateMatchup(
        eliteEightMatchups[0].winner, 
        eliteEightMatchups[2].winner, 
        strategy, 
        customStats
      ),
      simulateMatchup(
        eliteEightMatchups[1].winner, 
        eliteEightMatchups[3].winner, 
        strategy, 
        customStats
      )
    ];
  };
  
  // Simulate Championship
  const simulateChampionship = (finalFourMatchups, strategy, customStats = []) => {
    return simulateMatchup(
      finalFourMatchups[0].winner, 
      finalFourMatchups[1].winner, 
      strategy, 
      customStats
    );
  };
  
  // Simulate entire tournament
  export const simulateTournament = (teams, strategy = 'current', customStats = []) => {
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
      const firstRoundMatchups = simulateFirstRound(teams, regionTeams, strategy, customStats);
      
      // Second Round (Round of 32)
      const secondRoundMatchups = simulateSecondRound(firstRoundMatchups, strategy, customStats);
      
      // Sweet Sixteen
      const sweetSixteenMatchups = simulateSweetSixteen(secondRoundMatchups, strategy, customStats);
      
      // Elite Eight
      const eliteEightMatchups = simulateEliteEight(sweetSixteenMatchups, strategy, customStats);
      
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
    const finalFourMatchups = simulateFinalFour(
      regionChampions, 
      strategy, 
      customStats
    );
    tournamentBracket.finalFour = finalFourMatchups;
  
    // Championship
    const championshipGame = simulateChampionship(
      finalFourMatchups, 
      strategy, 
      customStats
    );
    tournamentBracket.championship = championshipGame;
    tournamentBracket.champion = championshipGame.winner;
  
    return tournamentBracket;
  };