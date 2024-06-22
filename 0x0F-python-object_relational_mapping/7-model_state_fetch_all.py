#!/usr/bin/python3
"""  lists all State objects from the database. """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    inputs = sys.argv
    if len(inputs) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(inputs[1], inputs[2], inputs[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    output = session.query(State).order_by(State.id).all()
    for state in output:
        print("{}: {}".format(state.id, state.name))
    session.close()
