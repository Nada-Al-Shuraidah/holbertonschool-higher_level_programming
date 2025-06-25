#!/usr/bin/python3
"""
Prints the State id with the name passed as argument from database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>
Prints state id or "Not found" if none matches
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
