#!/usr/bin/python3
"""prints the State object with the name passed as argument"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import State, Base

    inputs = sys.argv
    if len(inputs) < 5 or ";" in inputs[4]:
        exit(1)

    connection_string = 'mysql+mysqldb://():()@localhost:3306/{}'
    engine = create_engine(connection_string.format
                           (inputs[4], inputs[2], inputs[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)
    session = Session()
    my_query = session.query(State).filter(State.name.like(inputs[4])).all()
    if len(my_query) == 0:
        print('Not found')
    else:
        print(my_query[0].id)
    session.close()
