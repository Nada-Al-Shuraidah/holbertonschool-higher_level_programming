#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>
Prints the state with the smallest id or "Nothing" if empty
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query first state by id without fetching all
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()
