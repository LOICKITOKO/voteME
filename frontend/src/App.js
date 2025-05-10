// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import VotePage from './pages/VotePage';
import ThankYouPage from './pages/ThankYouPage';

const App = () => {
  const categories = [
    "Meilleur artiste", "Rappeur", "Chanteur", "DJ", "Révélation",
    "Groupe de danse", "Web media", "Humoriste", "Influenceur",
    "Ambassadeur", "Collaboration", "Performance live", "Réalisateur"
  ];

  const VoteWrapper = ({ index }) => (
    <VotePage categoryIndex={parseInt(index)} />
  );

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/vote/:index" element={<VotePage />} />
        <Route path="/merci" element={<ThankYouPage />} />
      </Routes>
    </Router>
  );
};

export default App;
