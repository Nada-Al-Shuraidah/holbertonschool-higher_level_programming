#!/usr/bin/python3
"""
Lists all State objects containing letter 'a' from database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>
Results sorted by states.id ascending
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model_state import Base, State

if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Filter states where name contains 'a' (case-sensitive)
    states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
