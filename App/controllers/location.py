from App.models import Location, User, HomeLocation
from App.database import db

def create_home_location(user_id, latitude, longitude):
    home_location = HomeLocation(user_id=user_id, latitude=latitude, longitude=longitude)
    db.session.add(home_location)
    db.session.commit()

def update_home_location(user_id, latitude, longitude):
    home_location = HomeLocation.query.filter_by(user_id=user_id).first()
    if home_location:
        home_location.latitude = latitude
        home_location.longitude = longitude
        db.session.commit()

def delete_home_location(user_id):
    home_location = HomeLocation.query.filter_by(user_id=user_id).first()
    if home_location:
        db.session.delete(home_location)
        db.session.commit()

def get_home_location(user_id):
    home_location = HomeLocation.query.filter_by(user_id=user_id).first()
    if home_location:
        return home_location
    return None
