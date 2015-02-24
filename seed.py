import model
from model import Location
import csv

def load_locations(session):
    filename=("./popos_test.csv")
    with open(filename, 'rb') as csvfile:
        openfile = csv.reader(csvfile, delimiter='\t')
        for row in openfile:
            location_name = row[0]
            location_address = row[1]
            new_locations = Location(name=location_name, address=location_address)
            session.add(new_locations)
        session.commit() 


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_locations(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)