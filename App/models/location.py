from App.database import db

class Location(db.Model):
  __abstract__ = True

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  longitude = db.Column(db.Float, nullable=False)


class HomeLocation(Location):

  def __init__(self, user_id, latitude, longitude):
    self.user_id = user_id
    self.longitude = longitude
    self.latitude = latitude
