import model
from model import Location, Image
import csv

def load_locations(session):
    filename=("./POPOS_Listings_20140224_NO_HEADERS.csv")
    with open(filename, 'rb') as csvfile:
        openfile = csv.reader(csvfile, delimiter='\t')
        for row in openfile:
            location_name = row[0]
            location_address = row[1]
            location_description = row[2]
            location_hours = row[3]
            location_hours = location_hours.decode("latin-1")
            location_seating_info = row[4]
            location_food_info = row[5]
            location_restrooms = row[6]
            location_food_yn = row[7]
            location_seating_yn = row[8]
            new_locations = Location(name=location_name, address=location_address, 
                                description=location_description,
                                hours=location_hours, seating_info=location_seating_info,
                                food_info=location_food_info, restrooms=location_restrooms,
                                food_yn=location_food_yn, seating_yn=location_seating_yn)
            session.add(new_locations)
        session.commit() 

def load_images(session):
    filename=("./POPOS_Listings_images.csv")
    with open(filename, 'rb') as csvfile:
        openfile = csv.reader(csvfile, delimiter='\t')
        for row in openfile:
            image_url = row[2]
            new_images = Image(url=image_url)
            session.add(new_images)
        session.commit()


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_locations(session)
    load_images(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)