#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from database hbtn_0e_6_usa
Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>
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

    states_to_delete = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
