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
            'region': team.region
        } for team in teams
    ])

if __name__ == '__main__':
    app.run(debug=True, port=5000)