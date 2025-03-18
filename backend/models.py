from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    
    # Remove the explicit id column
    name = Column(String, primary_key=True)
    seed = Column(Integer)
    region = Column(String)
    
    # Additional stats columns
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

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)