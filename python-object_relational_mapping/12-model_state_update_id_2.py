#!/usr/bin/python3
"""
Changes the name of the State object with id=2 to 'New Mexico'
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
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

    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
