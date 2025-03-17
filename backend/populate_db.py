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
            Team(name='Gonzaga', seed=1, region='West', conference='WCC'),
            Team(name='Kansas', seed=1, region='Midwest', conference='Big 12'),
            Team(name='Arizona', seed=1, region='South', conference='Pac-12'),
            Team(name='Houston', seed=1, region='East', conference='AAC')
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