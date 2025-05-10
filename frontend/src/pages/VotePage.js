import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './VotePage.css';

const VotePage = () => {
  const [categories, setCategories] = useState([]);
  const [currentCategoryIndex, setCurrentCategoryIndex] = useState(0);
  const [hasVoted, setHasVoted] = useState(false);
  const [votingFinished, setVotingFinished] = useState(false); // pour la fin du vote
  const navigate = useNavigate();

  useEffect(() => {
    // Récupérer les catégories depuis l'API
    fetch('http://127.0.0.1:8000/api/categories/')
      .then(response => response.json())
      .then(data => setCategories(data));
  }, []);

  const handleVote = (nomineeId) => {
    // Envoi du vote à l'API
    fetch('http://127.0.0.1:8000/api/vote/', {
      method: 'POST',
      body: JSON.stringify({ nominee_id: nomineeId }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(() => {
        setHasVoted(true);
        // Après le vote, on passe à la catégorie suivante
        setTimeout(() => {
          if (currentCategoryIndex < categories.length - 1) {
            setCurrentCategoryIndex(currentCategoryIndex + 1);
            setHasVoted(false);
          } else {
            setVotingFinished(true); // Le vote est terminé
          }
        }, 2000); // Attente de 2 secondes avant de passer à la catégorie suivante
      });
  };

  const currentCategory = categories[currentCategoryIndex];

  return (
    <div className="vote-page">
      {!votingFinished ? (
        <div>
          <div className="intro-text">
            <h1>Bienvenue à la Cérémonie des Vœux !</h1>
            <p>
              C'est le moment de faire entendre votre voix ! Choisissez les meilleurs artistes, 
              rappeurs, chanteurs, et bien plus encore. Chaque vote compte pour l'événement 
              le plus attendu de l'année.
            </p>
            <div className="trophy-box">
              {/* Cette case contiendra l'image du trophée */}
              <img src="https://via.placeholder.com/150" alt="Trophée" className="trophy-image" />
            </div>
            <p>
              Vous êtes à un pas de faire une différence, alors faites vos choix avec soin !
            </p>
          </div>

          {currentCategory ? (
            <div>
              <h2>{currentCategory.name}</h2>
              <div className="artists-grid">
                {currentCategory.nominees.map((nominee) => (
                  <div key={nominee.id} className="artist-box" onClick={() => handleVote(nominee.id)}>
                    <div className="image-placeholder">
                      {/* Image vide pour l'artiste */}
                    </div>
                    <div className="artist-name">{nominee.name}</div>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            <p className="loading">Chargement des catégories...</p>
          )}

          {hasVoted && <p className="success">Votre vote a été pris en compte !</p>}
        </div>
      ) : (
        <div className="thank-you-message">
          <h1>Merci pour vos votes !</h1>
          <p>
            Félicitations, vous avez complété votre participation aux votes. 
            L'événement sera célébré le <strong>15 juillet 2025</strong>.
          </p>
          <p>
            La remise des trophées aura lieu lors de la grande cérémonie en direct. 
            Restez connecté et suivez l'événement !
          </p>
          <button onClick={() => navigate('/')}>Retour à la page d'accueil</button>
        </div>
      )}
    </div>
  );
};

export default VotePage;
