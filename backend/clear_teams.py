from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Team

# Create engine
engine = create_engine('sqlite:///march_madness.db')
SessionLocal = sessionmaker(bind=engine)

def clear_all_teams():
    # Create a session
    db = SessionLocal()
    
    try:
        # Delete all teams
        num_deleted = db.query(Team).delete()
        
        # Commit the transaction
        db.commit()
        
        print(f"Deleted {num_deleted} teams from the database.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    
    finally:
        # Close the session
        db.close()

if __name__ == '__main__':
    clear_all_teams()