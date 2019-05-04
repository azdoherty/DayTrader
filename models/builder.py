#!/usr/bin/env python
'''
Populate the database for some events and institutions
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

companySymbols = {"Apple": "AAPL",
                  "Micron": "MU",
                  "J.P. Morgan Chase": "JPM",
                  "Federal Reserve": None
                  }


def add_events():
    pass


def main():
    engine = create_engine(
        'sqlite:///../DATA/calendar.db',
        echo=False
    )
    SESSION = sessionmaker(bind=engine)
    return SESSION()




entries = []
for key, value in companySymbols.items():
    entries.append({"name}": key, "symbol": value})
print(entries)
conn = engine.connect()
ins = Institutions.insert()
conn.execute(ins, entries)



