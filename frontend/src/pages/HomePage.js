import React from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';
import trophyImage from '../images/trophy.png'; // <-- import depuis src/images

const HomePage = () => {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate('/vote/0'); // Redirige vers la première catégorie
  };

  return (
    <div className="home-container">
      <h1 className="home-title">Bienvenue sur P/N AWARDS</h1>

      <div className="trophy-placeholder">
        <div className="image-box">
          <img 
            src={trophyImage}
            alt="Trophée Awards"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              borderRadius: '15px'
            }}
          />
        </div>
      </div>

      <p className="rules-text">
        Une fois que vous avez voté pour une catégorie, vous ne pouvez pas revenir en arrière.<br />
        Vous passerez automatiquement à la catégorie suivante après chaque vote.<br />
        Merci de voter sérieusement, chaque vote compte !
      </p>

      <button className="start-button" onClick={handleStart}>
        Commencer
      </button>
    </div>
  );
};

export default HomePage;
