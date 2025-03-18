from flask import Flask, jsonify
from flask_cors import CORS
from database import init_db, get_db
from models import Team

app = Flask(__name__)
CORS(app)

# Initialize database
init_db()

@app.route('/teams')
def get_teams():
    db = next(get_db())
    teams = db.query(Team).all()
    return jsonify([
        {
            'id': team.id,
            'name': team.name,
            'seed': team.seed,
            'region': team.region,
            'k_off': team.k_off,
            'k_def': team.k_def,
            'efg_pct': team.efg_pct,
            'efg_pct_def': team.efg_pct_def,
            'oreb_pct': team.oreb_pct,
            'dreb_pct': team.dreb_pct,
            'op_oreb_pct': team.op_oreb_pct,
            'op_dreb_pct': team.op_dreb_pct,
            'two_pt_pct': team.two_pt_pct,
            'two_pt_pct_def': team.two_pt_pct_def,
            'three_pt_pct': team.three_pt_pct,
            'three_pt_pct_def': team.three_pt_pct_def,
            'ft_pct': team.ft_pct,
            'elite_sos': team.elite_sos
        } for team in teams
    ])

if __name__ == '__main__':
    app.run(debug=True, port=5000)