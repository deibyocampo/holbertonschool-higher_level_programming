#!/usr/bin/python3
""" List all state ibjects from the database hbtn_0e_6_usa """


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    sesh = session()

    for state in sesh.query(State).\
            filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    sesh.close()
