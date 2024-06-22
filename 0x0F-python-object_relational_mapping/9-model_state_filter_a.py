#!/usr/bin/python3
"""lists all State objects that contain the letter a."""
import sys
from sqlalchemy import create_engine
from models.state import Base, State
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()
    for aninstance in session.query(State).filter(State.name.like('%a%'))
    print(aninstance.id, aninstance.name, sep=": ")
