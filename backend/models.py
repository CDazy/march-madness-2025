from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    seed = Column(Integer)
    region = Column(String)
    
    # Ensure these match exactly with the dictionary keys
    k_off = Column(Float)
    k_def = Column(Float)
    efg_pct = Column(Float)
    efg_pct_def = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    op_oreb_pct = Column(Float)
    op_dreb_pct = Column(Float)
    two_pt_pct = Column(Float)
    two_pt_pct_def = Column(Float)
    three_pt_pct = Column(Float)
    three_pt_pct_def = Column(Float)
    ft_pct = Column(Float)
    elite_sos = Column(Float)