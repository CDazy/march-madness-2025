import React from 'react';
import '../styles/Help.css';

function Help() {
  return (
    <div className="help-page">
      <h1>March Madness Simulator - Help Guide</h1>
      <section className="help-section">
        <p>Disclaimer: If you're not seeing any teams or the simulation button on the bracket page is disabled, you need to wait a minute for the server to start. 
        The backend server that stores all the team data goes idle for every 15 minutes of inactivity, so when you first access the site it might take a minute for anything to work.</p> 
      </section>
      <section className="help-section">
        <h2>Pages Overview</h2>
        <div className="page-descriptions">
          <div className="page-description">
            <h3>Home Page</h3>
            <p>
              The landing page provides a quick overview of the March Madness Simulator. 
              From here, you can navigate to view teams or start a tournament simulation.
            </p>
          </div>
          
          <div className="page-description">
            <h3>Teams Page</h3>
            <p>
              Explore detailed statistics for all tournament teams. 
              Features include:
              - Searchable team list
              - Sortable columns
              - Comprehensive team statistics
            </p>
          </div>
          
          <div className="page-description">
            <h3>Bracket Page</h3>
            <p>
              Simulate the entire tournament using various strategies:
            </p>
            <ul>
              <li><strong>Chalk:</strong> Winners determined by seed</li>
              <li><strong>Random:</strong> Completely random outcomes</li>\
              <li><strong>Custom:</strong> Choose your own statistical factors</li>
              <li><strong>3PT Focus:</strong> Emphasizes 3-point shooting</li>
              <li><strong>AI Strategy:</strong> KenPom-like rating simulation</li>
              <li><strong>Enhanced AI Strategy:</strong> Includes strength of schedule</li>
              <li><strong>All Stats:</strong> Comprehensive stat-based simulation</li>  
            </ul>
          </div>
          <p>Contact Support: caldoese@gmail.com</p>
        </div>
      </section>
    </div>
  );
}

export default Help;