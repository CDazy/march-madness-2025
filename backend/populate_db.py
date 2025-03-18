from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Team

# Create engine and session
engine = create_engine('sqlite:///march_madness.db')
Base.metadata.create_all(engine)  # Ensure tables are created
SessionLocal = sessionmaker(bind=engine)

def add_initial_teams():
    # Create a new session
    db = SessionLocal()
    
    try:
        # Example teams
        teams = [
    {
        "name": "Duke", 
        "seed": 1, 
        "region": "East", 
        "k_off": 124.282,
        "k_def": 93.0646,
        "efg_pct": 57.4,
        "efg_pct_def": 44.5,
        "oreb_pct": 35.2,
        "dreb_pct": 73.5,
        "op_oreb_pct": 26.5,
        "op_dreb_pct": 64.8,
        "two_pt_pct": 58.0,
        "two_pt_pct_def": 43.4,
        "three_pt_pct": 37.7,
        "three_pt_pct_def": 30.9,
        "ft_pct": 78.4,
        "elite_sos": 30.63
    },
    {
        "name": "Auburn", 
        "seed": 1, 
        "region": "South", 
        "k_off": 121.014,
        "k_def": 100.799,
        "efg_pct": 55.7,
        "efg_pct_def": 46.0,
        "oreb_pct": 34.3,
        "dreb_pct": 69.7,
        "op_oreb_pct": 30.3,
        "op_dreb_pct": 65.7,
        "two_pt_pct": 56.1,
        "two_pt_pct_def": 47.2,
        "three_pt_pct": 36.8,
        "three_pt_pct_def": 29.2,
        "ft_pct": 74.0,
        "elite_sos": 45.564
    },
    {
        "name": "Florida", 
        "seed": 1, 
        "region": "West", 
        "k_off": 120.249,
        "k_def": 97.1962,
        "efg_pct": 55.0,
        "efg_pct_def": 45.3,
        "oreb_pct": 38.1,
        "dreb_pct": 71.2,
        "op_oreb_pct": 28.8,
        "op_dreb_pct": 61.9,
        "two_pt_pct": 56.4,
        "two_pt_pct_def": 45.9,
        "three_pt_pct": 35.5,
        "three_pt_pct_def": 29.6,
        "ft_pct": 71.8,
        "elite_sos": 37.75
    },
    {
        "name": "Houston", 
        "seed": 1, 
        "region": "Midwest", 
        "k_off": 116.89,
        "k_def": 91.9137,
        "efg_pct": 52.7,
        "efg_pct_def": 44.9,
        "oreb_pct": 36.1,
        "dreb_pct": 70.7,
        "op_oreb_pct": 29.3,
        "op_dreb_pct": 63.9,
        "two_pt_pct": 49.0,
        "two_pt_pct_def": 43.9,
        "three_pt_pct": 39.8,
        "three_pt_pct_def": 30.9,
        "ft_pct": 74.1,
        "elite_sos": 38.577
    },
    {
        "name": "Alabama", 
        "seed": 2, 
        "region": "East", 
        "k_off": 118.725,
        "k_def": 106.121,
        "efg_pct": 56.3,
        "efg_pct_def": 47.9,
        "oreb_pct": 34.7,
        "dreb_pct": 70.8,
        "op_oreb_pct": 29.2,
        "op_dreb_pct": 65.3,
        "two_pt_pct": 59.7,
        "two_pt_pct_def": 48.8,
        "three_pt_pct": 35.0,
        "three_pt_pct_def": 30.8,
        "ft_pct": 71.6,
        "elite_sos": 46.471
    },
    {
        "name": "Tennessee", 
        "seed": 2, 
        "region": "Midwest", 
        "k_off": 114.091,
        "k_def": 95.4042,
        "efg_pct": 52.8,
        "efg_pct_def": 44.4,
        "oreb_pct": 35.4,
        "dreb_pct": 69.9,
        "op_oreb_pct": 30.1,
        "op_dreb_pct": 64.6,
        "two_pt_pct": 54.1,
        "two_pt_pct_def": 46.7,
        "three_pt_pct": 34.0,
        "three_pt_pct_def": 27.8,
        "ft_pct": 74.3,
        "elite_sos": 41.282
    },
    {
        "name": "Michigan St.", 
        "seed": 2, 
        "region": "South", 
        "k_off": 112.538,
        "k_def": 96.7934,
        "efg_pct": 51.2,
        "efg_pct_def": 46.1,
        "oreb_pct": 35.3,
        "dreb_pct": 75.4,
        "op_oreb_pct": 24.6,
        "op_dreb_pct": 64.7,
        "two_pt_pct": 53.6,
        "two_pt_pct_def": 49.1,
        "three_pt_pct": 30.8,
        "three_pt_pct_def": 27.9,
        "ft_pct": 78.1,
        "elite_sos": 34.707
    },
    {
        "name": "St. John's", 
        "seed": 2, 
        "region": "West", 
        "k_off": 110.13,
        "k_def": 92.0927,
        "efg_pct": 49.7,
        "efg_pct_def": 46.6,
        "oreb_pct": 37.3,
        "dreb_pct": 71.1,
        "op_oreb_pct": 28.9,
        "op_dreb_pct": 62.7,
        "two_pt_pct": 51.5,
        "two_pt_pct_def": 45.8,
        "three_pt_pct": 30.4,
        "three_pt_pct_def": 31.8,
        "ft_pct": 68.9,
        "elite_sos": 27.94
    },
    {
        "name": "Texas Tech", 
        "seed": 3, 
        "region": "West", 
        "k_off": 119.883,
        "k_def": 100.015,
        "efg_pct": 55.5,
        "efg_pct_def": 48.0,
        "oreb_pct": 34.3,
        "dreb_pct": 71.5,
        "op_oreb_pct": 28.5,
        "op_dreb_pct": 65.7,
        "two_pt_pct": 54.3,
        "two_pt_pct_def": 48.2,
        "three_pt_pct": 37.9,
        "three_pt_pct_def": 31.7,
        "ft_pct": 76.4,
        "elite_sos": 35.224
    },
    {
        "name": "Kentucky", 
        "seed": 3, 
        "region": "Midwest", 
        "k_off": 116.923,
        "k_def": 106.759,
        "efg_pct": 56.0,
        "efg_pct_def": 50.4,
        "oreb_pct": 28.7,
        "dreb_pct": 74.1,
        "op_oreb_pct": 25.9,
        "op_dreb_pct": 71.3,
        "two_pt_pct": 55.9,
        "two_pt_pct_def": 53.7,
        "three_pt_pct": 37.4,
        "three_pt_pct_def": 30.8,
        "ft_pct": 73.8,
        "elite_sos": 43.526
    },
    {
        "name": "Wisconsin", 
        "seed": 3, 
        "region": "East", 
        "k_off": 116.921,
        "k_def": 102.695,
        "efg_pct": 53.6,
        "efg_pct_def": 47.9,
        "oreb_pct": 28.0,
        "dreb_pct": 73.4,
        "op_oreb_pct": 26.6,
        "op_dreb_pct": 72.0,
        "two_pt_pct": 54.7,
        "two_pt_pct_def": 46.8,
        "three_pt_pct": 34.9,
        "three_pt_pct_def": 33.0,
        "ft_pct": 82.8,
        "elite_sos": 35.559
    },
    {
        "name": "Iowa St.", 
        "seed": 3, 
        "region": "South", 
        "k_off": 113.82,
        "k_def": 96.4765,
        "efg_pct": 54.6,
        "efg_pct_def": 48.4,
        "oreb_pct": 32.2,
        "dreb_pct": 71.6,
        "op_oreb_pct": 28.4,
        "op_dreb_pct": 67.8,
        "two_pt_pct": 55.1,
        "two_pt_pct_def": 47.5,
        "three_pt_pct": 35.8,
        "three_pt_pct_def": 33.2,
        "ft_pct": 75.7,
        "elite_sos": 36.738
    },
    {
        "name": "Purdue", 
        "seed": 4, 
        "region": "Midwest", 
        "k_off": 117.029,
        "k_def": 106.819,
        "efg_pct": 56.3,
        "efg_pct_def": 52.0,
        "oreb_pct": 31.0,
        "dreb_pct": 70.1,
        "op_oreb_pct": 29.9,
        "op_dreb_pct": 69.0,
        "two_pt_pct": 55.5,
        "two_pt_pct_def": 56.4,
        "three_pt_pct": 38.5,
        "three_pt_pct_def": 30.7,
        "ft_pct": 73.0,
        "elite_sos": 38.46
    },
    {
        "name": "Arizona", 
        "seed": 4, 
        "region": "East", 
        "k_off": 115.408,
        "k_def": 102.537,
        "efg_pct": 52.9,
        "efg_pct_def": 48.6,
        "oreb_pct": 35.9,
        "dreb_pct": 71.5,
        "op_oreb_pct": 28.5,
        "op_dreb_pct": 64.1,
        "two_pt_pct": 55.1,
        "two_pt_pct_def": 47.2,
        "three_pt_pct": 32.4,
        "three_pt_pct_def": 33.6,
        "ft_pct": 78.4,
        "elite_sos": 44.259
    },
    {
        "name": "Maryland", 
        "seed": 4, 
        "region": "West", 
        "k_off": 114.918,
        "k_def": 94.8324,
        "efg_pct": 53.8,
        "efg_pct_def": 47.0,
        "oreb_pct": 31.0,
        "dreb_pct": 72.8,
        "op_oreb_pct": 27.2,
        "op_dreb_pct": 69.0,
        "two_pt_pct": 52.7,
        "two_pt_pct_def": 47.6,
        "three_pt_pct": 37.2,
        "three_pt_pct_def": 30.7,
        "ft_pct": 75.5,
        "elite_sos": 31.337
    },
    {
        "name": "Texas A&M", 
        "seed": 4, 
        "region": "South", 
        "k_off": 109.403,
        "k_def": 99.5409,
        "efg_pct": 47.5,
        "efg_pct_def": 48.2,
        "oreb_pct": 42.0,
        "dreb_pct": 72.2,
        "op_oreb_pct": 27.8,
        "op_dreb_pct": 58.0,
        "two_pt_pct": 48.0,
        "two_pt_pct_def": 46.5,
        "three_pt_pct": 31.1,
        "three_pt_pct_def": 33.4,
        "ft_pct": 69.5,
        "elite_sos": 39.956
    },
    {
        "name": "Clemson", 
        "seed": 5, 
        "region": "Midwest", 
        "k_off": 115.072,
        "k_def": 98.5179,
        "efg_pct": 53.6,
        "efg_pct_def": 48.9,
        "oreb_pct": 33.7,
        "dreb_pct": 70.1,
        "op_oreb_pct": 29.9,
        "op_dreb_pct": 66.3,
        "two_pt_pct": 52.3,
        "two_pt_pct_def": 49.3,
        "three_pt_pct": 37.2,
        "three_pt_pct_def": 32.2,
        "ft_pct": 76.6,
        "elite_sos": 26.367
    },
    {
        "name": "Memphis", 
        "seed": 5, 
        "region": "West", 
        "k_off": 111.124,
        "k_def": 101.709,
        "efg_pct": 53.6,
        "efg_pct_def": 48.5,
        "oreb_pct": 35.1,
        "dreb_pct": 67.7,
        "op_oreb_pct": 32.3,
        "op_dreb_pct": 64.9,
        "two_pt_pct": 52.0,
        "two_pt_pct_def": 48.6,
        "three_pt_pct": 38.0,
        "three_pt_pct_def": 32.2,
        "ft_pct": 70.2,
        "elite_sos": 23.012
    },
    {
        "name": "Michigan", 
        "seed": 5, 
        "region": "South", 
        "k_off": 110.475,
        "k_def": 100.897,
        "efg_pct": 54.5,
        "efg_pct_def": 46.3,
        "oreb_pct": 33.2,
        "dreb_pct": 70.2,
        "op_oreb_pct": 29.8,
        "op_dreb_pct": 66.8,
        "two_pt_pct": 57.7,
        "two_pt_pct_def": 45.9,
        "three_pt_pct": 33.4,
        "three_pt_pct_def": 31.3,
        "ft_pct": 72.8,
        "elite_sos": 37.294
    },
    {
        "name": "Oregon", 
        "seed": 5, 
        "region": "East", 
        "k_off": 110.017,
        "k_def": 102.377,
        "efg_pct": 52.2,
        "efg_pct_def": 49.1,
        "oreb_pct": 30.6,
        "dreb_pct": 70.8,
        "op_oreb_pct": 29.2,
        "op_dreb_pct": 69.4,
        "two_pt_pct": 53.0,
        "two_pt_pct_def": 50.0,
        "three_pt_pct": 34.0,
        "three_pt_pct_def": 31.7,
        "ft_pct": 76.3,
        "elite_sos": 35.999
    },
    {
        "name": "Missouri", 
        "seed": 6, 
        "region": "West", 
        "k_off": 120.367,
        "k_def": 105.067,
        "efg_pct": 56.2,
        "efg_pct_def": 50.7,
        "oreb_pct": 33.7,
        "dreb_pct": 67.8,
        "op_oreb_pct": 32.2,
        "op_dreb_pct": 66.3,
        "two_pt_pct": 56.7,
        "two_pt_pct_def": 51.1,
        "three_pt_pct": 37.0,
        "three_pt_pct_def": 33.4,
        "ft_pct": 72.5,
        "elite_sos": 36.393
    },
    {
        "name": "BYU", 
        "seed": 6, 
        "region": "East", 
        "k_off": 117.204,
        "k_def": 102.804,
        "efg_pct": 57.2,
        "efg_pct_def": 50.6,
        "oreb_pct": 33.3,
        "dreb_pct": 73.9,
        "op_oreb_pct": 26.1,
        "op_dreb_pct": 66.7,
        "two_pt_pct": 58.6,
        "two_pt_pct_def": 49.3,
        "three_pt_pct": 37.1,
        "three_pt_pct_def": 34.8,
        "ft_pct": 70.5,
        "elite_sos": 35.191
    },
    {
        "name": "Illinois", 
        "seed": 6, 
        "region": "Midwest", 
        "k_off": 115.12,
        "k_def": 102.486,
        "efg_pct": 52.3,
        "efg_pct_def": 47.3,
        "oreb_pct": 36.0,
        "dreb_pct": 73.7,
        "op_oreb_pct": 26.3,
        "op_dreb_pct": 64.0,
        "two_pt_pct": 57.3,
        "two_pt_pct_def": 46.1,
        "three_pt_pct": 31.1,
        "three_pt_pct_def": 33.3,
        "ft_pct": 75.9,
        "elite_sos": 39.298
    },
    {
        "name": "Mississippi", 
        "seed": 6, 
        "region": "South", 
        "k_off": 110.694,
        "k_def": 102.594,
        "efg_pct": 51.1,
        "efg_pct_def": 50.5,
        "oreb_pct": 25.4,
        "dreb_pct": 69.2,
        "op_oreb_pct": 30.8,
        "op_dreb_pct": 74.6,
        "two_pt_pct": 51.0,
        "two_pt_pct_def": 51.6,
        "three_pt_pct": 34.1,
        "three_pt_pct_def": 32.7,
        "ft_pct": 73.8,
        "elite_sos": 41.324
    },
    {
        "name": "Saint Mary's", 
        "seed": 7, 
        "region": "East", 
        "k_off": 114.861,
        "k_def": 95.9112,
        "efg_pct": 50.9,
        "efg_pct_def": 46.2,
        "oreb_pct": 40.5,
        "dreb_pct": 75.1,
        "op_oreb_pct": 24.9,
        "op_dreb_pct": 59.5,
        "two_pt_pct": 51.8,
        "two_pt_pct_def": 45.8,
        "three_pt_pct": 32.6,
        "three_pt_pct_def": 31.2,
        "ft_pct": 69.5,
        "elite_sos": 22.682
    },
    {
        "name": "UCLA", 
        "seed": 7, 
        "region": "Midwest", 
        "k_off": 112.395,
        "k_def": 98.9106,
        "efg_pct": 53.0,
        "efg_pct_def": 50.5,
        "oreb_pct": 32.8,
        "dreb_pct": 70.8,
        "op_oreb_pct": 29.2,
        "op_dreb_pct": 67.2,
        "two_pt_pct": 53.1,
        "two_pt_pct_def": 51.2,
        "three_pt_pct": 35.2,
        "three_pt_pct_def": 33.2,
        "ft_pct": 70.3,
        "elite_sos": 34.636
    },
    {
        "name": "Marquette", 
        "seed": 7, 
        "region": "South", 
        "k_off": 112.213,
        "k_def": 100.274,
        "efg_pct": 52.0,
        "efg_pct_def": 49.9,
        "oreb_pct": 30.1,
        "dreb_pct": 69.0,
        "op_oreb_pct": 31.0,
        "op_dreb_pct": 69.9,
        "two_pt_pct": 54.9,
        "two_pt_pct_def": 51.3,
        "three_pt_pct": 32.5,
        "three_pt_pct_def": 31.8,
        "ft_pct": 72.3,
        "elite_sos": 34.207
    },
    {
        "name": "Kansas", 
        "seed": 7, 
        "region": "West", 
        "k_off": 109.004,
        "k_def": 98.7957,
        "efg_pct": 53.1,
        "efg_pct_def": 46.2,
        "oreb_pct": 30.4,
        "dreb_pct": 72.5,
        "op_oreb_pct": 27.5,
        "op_dreb_pct": 69.6,
        "two_pt_pct": 53.4,
        "two_pt_pct_def": 46.1,
        "three_pt_pct": 35.2,
        "three_pt_pct_def": 30.9,
        "ft_pct": 71.1,
        "elite_sos": 41.748
    },
    {
        "name": "Gonzaga", 
        "seed": 8, 
        "region": "Midwest", 
        "k_off": 121.239,
        "k_def": 97.5072,
        "efg_pct": 55.7,
        "efg_pct_def": 47.5,
        "oreb_pct": 32.7,
        "dreb_pct": 73.6,
        "op_oreb_pct": 26.4,
        "op_dreb_pct": 67.3,
        "two_pt_pct": 57.8,
        "two_pt_pct_def": 49.1,
        "three_pt_pct": 34.4,
        "three_pt_pct_def": 30.2,
        "ft_pct": 80.1,
        "elite_sos": 26.112
    },
    {
        "name": "Connecticut", 
        "seed": 8, 
        "region": "West", 
        "k_off": 118.148,
        "k_def": 104.135,
        "efg_pct": 55.5,
        "efg_pct_def": 48.3,
        "oreb_pct": 35.6,
        "dreb_pct": 72.6,
        "op_oreb_pct": 27.4,
        "op_dreb_pct": 64.4,
        "two_pt_pct": 57.3,
        "two_pt_pct_def": 46.0,
        "three_pt_pct": 35.4,
        "three_pt_pct_def": 35.1,
        "ft_pct": 79.1,
        "elite_sos": 30.085
    },
    {
        "name": "Louisville", 
        "seed": 8, 
        "region": "South", 
        "k_off": 113.399,
        "k_def": 99.6724,
        "efg_pct": 53.4,
        "efg_pct_def": 49.2,
        "oreb_pct": 32.2,
        "dreb_pct": 72.8,
        "op_oreb_pct": 27.2,
        "op_dreb_pct": 67.8,
        "two_pt_pct": 57.0,
        "two_pt_pct_def": 48.3,
        "three_pt_pct": 33.0,
        "three_pt_pct_def": 33.7,
        "ft_pct": 74.4,
        "elite_sos": 29.98
    },
    {
        "name": "Mississippi St.", 
        "seed": 8, 
        "region": "East", 
        "k_off": 113.152,
        "k_def": 105.036,
        "efg_pct": 51.7,
        "efg_pct_def": 51.9,
        "oreb_pct": 34.1,
        "dreb_pct": 70.5,
        "op_oreb_pct": 29.5,
        "op_dreb_pct": 65.9,
        "two_pt_pct": 55.2,
        "two_pt_pct_def": 50.1,
        "three_pt_pct": 31.4,
        "three_pt_pct_def": 36.1,
        "ft_pct": 70.0,
        "elite_sos": 38.324
    },
    {
        "name": "Baylor", 
        "seed": 9, 
        "region": "East", 
        "k_off": 113.197,
        "k_def": 104.882,
        "efg_pct": 51.5,
        "efg_pct_def": 51.2,
        "oreb_pct": 35.6,
        "dreb_pct": 68.8,
        "op_oreb_pct": 31.2,
        "op_dreb_pct": 64.4,
        "two_pt_pct": 51.2,
        "two_pt_pct_def": 49.8,
        "three_pt_pct": 34.7,
        "three_pt_pct_def": 35.4,
        "ft_pct": 74.6,
        "elite_sos": 42.981
    },
    {
        "name": "Oklahoma", 
        "seed": 9, 
        "region": "West", 
        "k_off": 112.581,
        "k_def": 106.757,
        "efg_pct": 54.9,
        "efg_pct_def": 51.1,
        "oreb_pct": 26.5,
        "dreb_pct": 68.3,
        "op_oreb_pct": 31.7,
        "op_dreb_pct": 73.5,
        "two_pt_pct": 54.6,
        "two_pt_pct_def": 54.9,
        "three_pt_pct": 37.0,
        "three_pt_pct_def": 30.5,
        "ft_pct": 79.4,
        "elite_sos": 39.435
    },
    {
        "name": "Creighton", 
        "seed": 9, 
        "region": "South", 
        "k_off": 110.76,
        "k_def": 102.225,
        "efg_pct": 55.8,
        "efg_pct_def": 47.0,
        "oreb_pct": 26.9,
        "dreb_pct": 72.8,
        "op_oreb_pct": 27.2,
        "op_dreb_pct": 73.1,
        "two_pt_pct": 60.5,
        "two_pt_pct_def": 45.8,
        "three_pt_pct": 33.9,
        "three_pt_pct_def": 32.7,
        "ft_pct": 73.3,
        "elite_sos": 31.577
    },
    {
        "name": "Georgia", 
        "seed": 9, 
        "region": "Midwest", 
        "k_off": 110.152,
        "k_def": 101.242,
        "efg_pct": 52.5,
        "efg_pct_def": 47.2,
        "oreb_pct": 36.1,
        "dreb_pct": 68.2,
        "op_oreb_pct": 31.8,
        "op_dreb_pct": 63.9,
        "two_pt_pct": 53.8,
        "two_pt_pct_def": 47.8,
        "three_pt_pct": 33.5,
        "three_pt_pct_def": 30.9,
        "ft_pct": 71.7,
        "elite_sos": 37.778
    },
    {
        "name": "Utah St.", 
        "seed": 10, 
        "region": "Midwest", 
        "k_off": 118.7,
        "k_def": 104.996,
        "efg_pct": 56.0,
        "efg_pct_def": 51.8,
        "oreb_pct": 34.6,
        "dreb_pct": 69.7,
        "op_oreb_pct": 30.3,
        "op_dreb_pct": 65.4,
        "two_pt_pct": 57.7,
        "two_pt_pct_def": 52.6,
        "three_pt_pct": 35.8,
        "three_pt_pct_def": 33.8,
        "ft_pct": 70.2,
        "elite_sos": 23.021
    },
    {
        "name": "Vanderbilt", 
        "seed": 10, 
        "region": "East", 
        "k_off": 113.04,
        "k_def": 106.248,
        "efg_pct": 51.7,
        "efg_pct_def": 52.9,
        "oreb_pct": 32.2,
        "dreb_pct": 70.3,
        "op_oreb_pct": 29.7,
        "op_dreb_pct": 67.8,
        "two_pt_pct": 53.6,
        "two_pt_pct_def": 51.5,
        "three_pt_pct": 32.5,
        "three_pt_pct_def": 36.9,
        "ft_pct": 74.7,
        "elite_sos": 35.986
    },
    {
        "name": "New Mexico", 
        "seed": 10, 
        "region": "South", 
        "k_off": 108.691,
        "k_def": 96.5138,
        "efg_pct": 50.8,
        "efg_pct_def": 49.2,
        "oreb_pct": 31.5,
        "dreb_pct": 74.4,
        "op_oreb_pct": 25.6,
        "op_dreb_pct": 68.5,
        "two_pt_pct": 50.6,
        "two_pt_pct_def": 48.2,
        "three_pt_pct": 34.1,
        "three_pt_pct_def": 33.8,
        "ft_pct": 68.4,
        "elite_sos": 24.388
    },
    {
        "name": "Arkansas", 
        "seed": 10, 
        "region": "West", 
        "k_off": 107.931,
        "k_def": 100.726,
        "efg_pct": 52.7,
        "efg_pct_def": 48.3,
        "oreb_pct": 27.6,
        "dreb_pct": 71.7,
        "op_oreb_pct": 28.3,
        "op_dreb_pct": 72.4,
        "two_pt_pct": 54.4,
        "two_pt_pct_def": 48.5,
        "three_pt_pct": 33.3,
        "three_pt_pct_def": 31.9,
        "ft_pct": 73.4,
        "elite_sos": 36.561
    },
    {
        "name": "VCU", 
        "seed": 11, 
        "region": "East", 
        "k_off": 115.356,
        "k_def": 93.9477,
        "efg_pct": 52.4,
        "efg_pct_def": 44.4,
        "oreb_pct": 36.7,
        "dreb_pct": 70.0,
        "op_oreb_pct": 30.0,
        "op_dreb_pct": 63.3,
        "two_pt_pct": 54.2,
        "two_pt_pct_def": 43.6,
        "three_pt_pct": 33.5,
        "three_pt_pct_def": 30.6,
        "ft_pct": 74.5,
        "elite_sos": 16.375
    },
    {
        "name": "North Carolina", 
        "seed": 11, 
        "region": "South", 
        "k_off": 113.488,
        "k_def": 105.192,
        "efg_pct": 54.2,
        "efg_pct_def": 49.6,
        "oreb_pct": 29.2,
        "dreb_pct": 72.9,
        "op_oreb_pct": 27.1,
        "op_dreb_pct": 70.8,
        "two_pt_pct": 54.9,
        "two_pt_pct_def": 49.2,
        "three_pt_pct": 35.3,
        "three_pt_pct_def": 33.5,
        "ft_pct": 73.7,
        "elite_sos": 35.154
    },
    {
        "name": "Drake", 
        "seed": 11, 
        "region": "West", 
        "k_off": 113.293,
        "k_def": 98.3466,
        "efg_pct": 53.8,
        "efg_pct_def": 51.7,
        "oreb_pct": 36.0,
        "dreb_pct": 74.2,
        "op_oreb_pct": 25.8,
        "op_dreb_pct": 64.0,
        "two_pt_pct": 54.6,
        "two_pt_pct_def": 54.3,
        "three_pt_pct": 35.0,
        "three_pt_pct_def": 31.8,
        "ft_pct": 70.7,
        "elite_sos": 12.625
    },
    {
        "name": "Texas", 
        "seed": 11, 
        "region": "Midwest", 
        "k_off": 112.903,
        "k_def": 104.089,
        "efg_pct": 52.5,
        "efg_pct_def": 48.4,
        "oreb_pct": 29.8,
        "dreb_pct": 70.3,
        "op_oreb_pct": 29.7,
        "op_dreb_pct": 70.2,
        "two_pt_pct": 51.8,
        "two_pt_pct_def": 47.5,
        "three_pt_pct": 36.0,
        "three_pt_pct_def": 33.3,
        "ft_pct": 74.9,
        "elite_sos": 37.234
    },
    {
        "name": "Xavier", 
        "seed": 11, 
        "region": "Midwest", 
        "k_off": 111.584,
        "k_def": 101.409,
        "efg_pct": 53.9,
        "efg_pct_def": 50.6,
        "oreb_pct": 25.2,
        "dreb_pct": 74.8,
        "op_oreb_pct": 25.2,
        "op_dreb_pct": 74.8,
        "two_pt_pct": 51.3,
        "two_pt_pct_def": 50.5,
        "three_pt_pct": 38.8,
        "three_pt_pct_def": 33.9,
        "ft_pct": 79.4,
        "elite_sos": 28.812
    },
    {
        "name": "San Diego St.", 
        "seed": 11, 
        "region": "South", 
        "k_off": 104.984,
        "k_def": 96.3478,
        "efg_pct": 50.6,
        "efg_pct_def": 45.3,
        "oreb_pct": 29.4,
        "dreb_pct": 69.1,
        "op_oreb_pct": 30.9,
        "op_dreb_pct": 70.6,
        "two_pt_pct": 51.6,
        "two_pt_pct_def": 45.0,
        "three_pt_pct": 32.8,
        "three_pt_pct_def": 30.4,
        "ft_pct": 66.7,
        "elite_sos": 27.647
    },
    {
        "name": "UC San Diego", 
        "seed": 12, 
        "region": "South", 
        "k_off": 116.383,
        "k_def": 93.8414,
        "efg_pct": 55.4,
        "efg_pct_def": 47.7,
        "oreb_pct": 25.6,
        "dreb_pct": 71.6,
        "op_oreb_pct": 28.4,
        "op_dreb_pct": 74.4,
        "two_pt_pct": 56.1,
        "two_pt_pct_def": 46.2,
        "three_pt_pct": 36.5,
        "three_pt_pct_def": 33.1,
        "ft_pct": 74.6,
        "elite_sos": 12.106
    },
    {
        "name": "McNeese St.", 
        "seed": 12, 
        "region": "Midwest", 
        "k_off": 114.387,
        "k_def": 97.5513,
        "efg_pct": 53.3,
        "efg_pct_def": 47.5,
        "oreb_pct": 34.7,
        "dreb_pct": 68.7,
        "op_oreb_pct": 31.3,
        "op_dreb_pct": 65.3,
        "two_pt_pct": 53.2,
        "two_pt_pct_def": 46.9,
        "three_pt_pct": 35.6,
        "three_pt_pct_def": 32.2,
        "ft_pct": 70.7,
        "elite_sos": 12.768
    },
    {
        "name": "Colorado St.", 
        "seed": 12, 
        "region": "West", 
        "k_off": 112.599,
        "k_def": 100.329,
        "efg_pct": 55.8,
        "efg_pct_def": 48.5,
        "oreb_pct": 26.4,
        "dreb_pct": 74.7,
        "op_oreb_pct": 25.3,
        "op_dreb_pct": 73.6,
        "two_pt_pct": 56.5,
        "two_pt_pct_def": 47.7,
        "three_pt_pct": 36.6,
        "three_pt_pct_def": 33.1,
        "ft_pct": 77.5,
        "elite_sos": 22.886
    },
    {
        "name": "Liberty", 
        "seed": 12, 
        "region": "East", 
        "k_off": 111.512,
        "k_def": 96.8666,
        "efg_pct": 58.4,
        "efg_pct_def": 45.9,
        "oreb_pct": 18.9,
        "dreb_pct": 72.0,
        "op_oreb_pct": 28.0,
        "op_dreb_pct": 81.1,
        "two_pt_pct": 57.7,
        "two_pt_pct_def": 48.0,
        "three_pt_pct": 39.5,
        "three_pt_pct_def": 28.0,
        "ft_pct": 65.4,
        "elite_sos": 13.412
    },
    {
        "name": "High Point", 
        "seed": 13, 
        "region": "Midwest", 
        "k_off": 121.342,
        "k_def": 104.975,
        "efg_pct": 56.4,
        "efg_pct_def": 49.1,
        "oreb_pct": 34.0,
        "dreb_pct": 70.1,
        "op_oreb_pct": 29.9,
        "op_dreb_pct": 66.0,
        "two_pt_pct": 57.4,
        "two_pt_pct_def": 48.9,
        "three_pt_pct": 36.6,
        "three_pt_pct_def": 32.9,
        "ft_pct": 76.4,
        "elite_sos": 6.978
    },
    {
        "name": "Yale", 
        "seed": 13, 
        "region": "South", 
        "k_off": 117.148,
        "k_def": 101.516,
        "efg_pct": 54.8,
        "efg_pct_def": 48.8,
        "oreb_pct": 33.2,
        "dreb_pct": 74.2,
        "op_oreb_pct": 25.8,
        "op_dreb_pct": 66.8,
        "two_pt_pct": 53.4,
        "two_pt_pct_def": 47.3,
        "three_pt_pct": 38.5,
        "three_pt_pct_def": 33.7,
        "ft_pct": 73.6,
        "elite_sos": 11.606
    },
    {
        "name": "Akron", 
        "seed": 13, 
        "region": "East", 
        "k_off": 115.754,
        "k_def": 104.558,
        "efg_pct": 55.4,
        "efg_pct_def": 49.5,
        "oreb_pct": 33.3,
        "dreb_pct": 71.0,
        "op_oreb_pct": 29.0,
        "op_dreb_pct": 66.7,
        "two_pt_pct": 55.8,
        "two_pt_pct_def": 50.6,
        "three_pt_pct": 36.6,
        "three_pt_pct_def": 31.9,
        "ft_pct": 74.9,
        "elite_sos": 9.759
    },
    {
        "name": "Grand Canyon", 
        "seed": 13, 
        "region": "West", 
        "k_off": 107.787,
        "k_def": 95.8496,
        "efg_pct": 51.2,
        "efg_pct_def": 47.0,
        "oreb_pct": 32.5,
        "dreb_pct": 71.4,
        "op_oreb_pct": 28.6,
        "op_dreb_pct": 67.5,
        "two_pt_pct": 53.2,
        "two_pt_pct_def": 46.4,
        "three_pt_pct": 31.6,
        "three_pt_pct_def": 32.1,
        "ft_pct": 73.5,
        "elite_sos": 10.398
    },
    {
        "name": "Lipscomb", 
        "seed": 14, 
        "region": "South", 
        "k_off": 115.488,
        "k_def": 100.691,
        "efg_pct": 55.9,
        "efg_pct_def": 48.6,
        "oreb_pct": 24.0,
        "dreb_pct": 73.5,
        "op_oreb_pct": 26.5,
        "op_dreb_pct": 76.0,
        "two_pt_pct": 56.7,
        "two_pt_pct_def": 49.9,
        "three_pt_pct": 36.7,
        "three_pt_pct_def": 31.0,
        "ft_pct": 79.6,
        "elite_sos": 11.694
    },
    {
        "name": "UNC Wilmington", 
        "seed": 14, 
        "region": "West", 
        "k_off": 114.669,
        "k_def": 104.53,
        "efg_pct": 52.2,
        "efg_pct_def": 50.9,
        "oreb_pct": 35.4,
        "dreb_pct": 71.9,
        "op_oreb_pct": 28.1,
        "op_dreb_pct": 64.6,
        "two_pt_pct": 53.8,
        "two_pt_pct_def": 50.4,
        "three_pt_pct": 33.0,
        "three_pt_pct_def": 34.4,
        "ft_pct": 75.3,
        "elite_sos": 8.683
    },
    {
        "name": "Montana", 
        "seed": 14, 
        "region": "East", 
        "k_off": 111.586,
        "k_def": 110.248,
        "efg_pct": 56.4,
        "efg_pct_def": 52.2,
        "oreb_pct": 22.6,
        "dreb_pct": 71.0,
        "op_oreb_pct": 29.0,
        "op_dreb_pct": 77.4,
        "two_pt_pct": 57.3,
        "two_pt_pct_def": 53.1,
        "three_pt_pct": 36.5,
        "three_pt_pct_def": 33.7,
        "ft_pct": 74.6,
        "elite_sos": 15.101
    },
    {
        "name": "Troy", 
        "seed": 14, 
        "region": "Midwest", 
        "k_off": 108.553,
        "k_def": 98.9402,
        "efg_pct": 50.1,
        "efg_pct_def": 47.2,
        "oreb_pct": 38.6,
        "dreb_pct": 68.0,
        "op_oreb_pct": 32.0,
        "op_dreb_pct": 61.4,
        "two_pt_pct": 53.9,
        "two_pt_pct_def": 46.2,
        "three_pt_pct": 30.3,
        "three_pt_pct_def": 32.6,
        "ft_pct": 72.6,
        "elite_sos": 14.121
    },
    {
        "name": "Wofford", 
        "seed": 15, 
        "region": "Midwest", 
        "k_off": 112.782,
        "k_def": 108.737,
        "efg_pct": 53.3,
        "efg_pct_def": 51.8,
        "oreb_pct": 35.5,
        "dreb_pct": 73.8,
        "op_oreb_pct": 26.2,
        "op_dreb_pct": 64.5,
        "two_pt_pct": 54.6,
        "two_pt_pct_def": 51.8,
        "three_pt_pct": 34.5,
        "three_pt_pct_def": 34.5,
        "ft_pct": 66.8,
        "elite_sos": 12.682
    },
    {
        "name": "Nebraska Omaha", 
        "seed": 15, 
        "region": "West", 
        "k_off": 112.458,
        "k_def": 109.839,
        "efg_pct": 53.5,
        "efg_pct_def": 53.1,
        "oreb_pct": 29.2,
        "dreb_pct": 74.6,
        "op_oreb_pct": 25.4,
        "op_dreb_pct": 70.8,
        "two_pt_pct": 52.5,
        "two_pt_pct_def": 53.5,
        "three_pt_pct": 36.7,
        "three_pt_pct_def": 35.1,
        "ft_pct": 73.3,
        "elite_sos": 13.045
    },
    {
        "name": "Robert Morris", 
        "seed": 15, 
        "region": "East", 
        "k_off": 110.137,
        "k_def": 101.539,
        "efg_pct": 51.3,
        "efg_pct_def": 50.3,
        "oreb_pct": 35.3,
        "dreb_pct": 71.7,
        "op_oreb_pct": 28.3,
        "op_dreb_pct": 64.7,
        "two_pt_pct": 50.7,
        "two_pt_pct_def": 49.8,
        "three_pt_pct": 34.9,
        "three_pt_pct_def": 34.2,
        "ft_pct": 72.0,
        "elite_sos": 8.247
    },
    {
        "name": "Bryant", 
        "seed": 15, 
        "region": "South", 
        "k_off": 109.621,
        "k_def": 101.303,
        "efg_pct": 51.0,
        "efg_pct_def": 47.7,
        "oreb_pct": 34.2,
        "dreb_pct": 71.2,
        "op_oreb_pct": 28.8,
        "op_dreb_pct": 65.8,
        "two_pt_pct": 51.5,
        "two_pt_pct_def": 47.3,
        "three_pt_pct": 33.4,
        "three_pt_pct_def": 32.2,
        "ft_pct": 71.8,
        "elite_sos": 9.31
    },
    {
        "name": "Norfolk St.", 
        "seed": 16, 
        "region": "West", 
        "k_off": 110.269,
        "k_def": 104.695,
        "efg_pct": 52.4,
        "efg_pct_def": 49.7,
        "oreb_pct": 32.8,
        "dreb_pct": 66.2,
        "op_oreb_pct": 33.8,
        "op_dreb_pct": 67.2,
        "two_pt_pct": 54.5,
        "two_pt_pct_def": 48.9,
        "three_pt_pct": 31.3,
        "three_pt_pct_def": 33.9,
        "ft_pct": 75.3,
        "elite_sos": 12.001
    },
    {
        "name": "SIU Edwardsville", 
        "seed": 16, 
        "region": "Midwest", 
        "k_off": 104.645,
        "k_def": 100.352,
        "efg_pct": 48.9,
        "efg_pct_def": 47.5,
        "oreb_pct": 31.8,
        "dreb_pct": 70.9,
        "op_oreb_pct": 29.1,
        "op_dreb_pct": 68.2,
        "two_pt_pct": 47.8,
        "two_pt_pct_def": 46.3,
        "three_pt_pct": 34.0,
        "three_pt_pct_def": 33.0,
        "ft_pct": 67.9,
        "elite_sos": 8.164
    },
    {
        "name": "American", 
        "seed": 16, 
        "region": "East", 
        "k_off": 104.618,
        "k_def": 105.086,
        "efg_pct": 51.8,
        "efg_pct_def": 52.1,
        "oreb_pct": 23.8,
        "dreb_pct": 72.6,
        "op_oreb_pct": 27.4,
        "op_dreb_pct": 76.2,
        "two_pt_pct": 51.1,
        "two_pt_pct_def": 53.1,
        "three_pt_pct": 35.1,
        "three_pt_pct_def": 33.6,
        "ft_pct": 75.9,
        "elite_sos": 8.755
    },
    {
        "name": "Alabama St.", 
        "seed": 16, 
        "region": "South", 
        "k_off": 103.998,
        "k_def": 104.201,
        "efg_pct": 47.1,
        "efg_pct_def": 50.3,
        "oreb_pct": 28.3,
        "dreb_pct": 68.9,
        "op_oreb_pct": 31.1,
        "op_dreb_pct": 71.7,
        "two_pt_pct": 45.4,
        "two_pt_pct_def": 50.4,
        "three_pt_pct": 32.9,
        "three_pt_pct_def": 33.4,
        "ft_pct": 69.8,
        "elite_sos": 11.608
    },
    {
        "name": "Mount St. Mary's", 
        "seed": 16, 
        "region": "East", 
        "k_off": 101.563,
        "k_def": 102.06,
        "efg_pct": 51.0,
        "efg_pct_def": 48.0,
        "oreb_pct": 31.1,
        "dreb_pct": 71.7,
        "op_oreb_pct": 28.3,
        "op_dreb_pct": 68.9,
        "two_pt_pct": 50.1,
        "two_pt_pct_def": 48.7,
        "three_pt_pct": 34.9,
        "three_pt_pct_def": 31.4,
        "ft_pct": 73.0,
        "elite_sos": 8.934
    },
    {
        "name": "Saint Francis", 
        "seed": 16, 
        "region": "South", 
        "k_off": 100.249,
        "k_def": 107.927,
        "efg_pct": 51.6,
        "efg_pct_def": 51.3,
        "oreb_pct": 25.4,
        "dreb_pct": 70.0,
        "op_oreb_pct": 30.0,
        "op_dreb_pct": 74.6,
        "two_pt_pct": 52.6,
        "two_pt_pct_def": 53.4,
        "three_pt_pct": 33.4,
        "three_pt_pct_def": 32.3,
        "ft_pct": 72.5,
        "elite_sos": 12.764
    }
]
        
        # Add all teams
        db.add_all(teams)
        
        # Commit the transaction
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        # Close the session
        db.close()

if __name__ == '__main__':
    add_initial_teams()