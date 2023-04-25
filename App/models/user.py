from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

friends = db.Table(
  'friends',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
  db.Column('friend_id',
            db.Integer,
            db.ForeignKey('user.id'),
            primary_key=True))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(120), nullable=False)
  friends = db.relationship('User',
                            secondary='friends',
                            primaryjoin='User.id==friends.c.user_id',
                            secondaryjoin='User.id==friends.c.friend_id',
                            backref='friends_of')
  home_location = db.relationship('HomeLocation',
                                  uselist=False,
                                  backref='user',
                                  cascade='all, delete-orphan')

  def __init__(self, username, password):
    self.username = username
    self.set_password(password)

  def get_json(self):
    return {'id': self.id, 'username': self.username}

  def set_password(self, password):
    """Create hashed password."""
    self.password = generate_password_hash(password, method='sha256')

  def check_password(self, password):
    """Check hashed password."""
    return check_password_hash(self.password, password)
