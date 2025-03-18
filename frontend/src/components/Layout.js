import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Layout.css';

function Layout({ children }) {
  return (
    <div className="app-layout">
      <nav className="main-nav">
        <div className="nav-logo">
          March Madness Simulator
        </div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/teams">Teams</Link>
          <Link to="/bracket">Bracket</Link>
        </div>
      </nav>
      <main className="main-content">
        {children}
      </main>
      <footer className="main-footer">
        <p>© 2025 March Madness Simulator</p>
      </footer>
    </div>
  );
}

export default Layout;