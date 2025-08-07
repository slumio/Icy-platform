import React from 'react';
import './InfluencerCard.css'; // We'll create this CSS file

// A helper to format large numbers
const formatFollowers = (num) => {
  if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
  if (num >= 1000) return (num / 1000).toFixed(0) + 'K';
  return num;
};

// A helper to determine the color of the score badge
const getScoreColor = (score) => {
  if (score >= 90) return 'score-high';
  if (score >= 75) return 'score-medium';
  return 'score-low';
};

function InfluencerCard({ influencer }) {
  // Graceful handling if data is missing
  if (!influencer || !influencer.scores) {
    return <div className="card-skeleton">Loading...</div>;
  }

  return (
    <div className="influencer-card">
      <div className={`score-badge ${getScoreColor(influencer.scores.brand_fit_score)}`}>
        {influencer.scores.brand_fit_score}%
        <span>Brand Fit</span>
      </div>
      <img
        className="profile-pic"
        src={influencer.profile_pic_url}
        alt={influencer.handle}
        onError={(e) => { e.target.onerror = null; e.target.src="https://placehold.co/100x100/EFEFEF/333?text=404"; }}
      />
      <h3 className="handle">@{influencer.handle}</h3>
      <p className="niche">{influencer.niche.join(' • ')}</p>
      <div className="stats">
        <div className="stat-item">
          <strong>{formatFollowers(influencer.followers)}</strong>
          <span>Followers</span>
        </div>
        <div className="stat-item">
          <strong>{influencer.engagement_rate}%</strong>
          <span>Engagement</span>
        </div>
        <div className="stat-item">
          <strong>{influencer.scores.authenticity_score}%</strong>
          <span>Authenticity</span>
        </div>
      </div>
      <button className="outreach-btn">View & Outreach</button>
    </div>
  );
}

export default InfluencerCard;