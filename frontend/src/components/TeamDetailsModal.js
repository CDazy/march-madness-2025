import React from 'react';
import '../styles/TeamDetailsModal.css';

function TeamDetailsModal({ team, onClose }) {
  if (!team) return null;

  return (
    <div className="modal-backdrop">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>×</button>
        <h2>{team.name}</h2>
        <div className="team-details">
          <div className="team-basic-info">
            <p>Seed: {team.seed}</p>
            <p>Region: {team.region}</p>
          </div>
          <div className="team-stats">
            <h3>Team Statistics</h3>
            <table>
              <tbody>
                <tr>
                  <td>Offensive Rating:</td>
                  <td>{team.k_off.toFixed(2)}</td>
                </tr>
                <tr>
                  <td>Defensive Rating:</td>
                  <td>{team.k_def.toFixed(2)}</td>
                </tr>
                <tr>
                  <td>Effective Field Goal %:</td>
                  <td>{team.efg_pct.toFixed(2)}%</td>
                </tr>
                <tr>
                  <td>Offensive Rebound %:</td>
                  <td>{team.oreb_pct.toFixed(2)}%</td>
                </tr>
                <tr>
                  <td>Free Throw %:</td>
                  <td>{team.ft_pct.toFixed(2)}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TeamDetailsModal;