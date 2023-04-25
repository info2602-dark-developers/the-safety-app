from App.models import User
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

#friend controllers
def add_friend(user_id, friend_id):
    user = User.query.get(user_id)
    friend = User.query.get(friend_id)
    if user and friend:
        user.friends.append(friend)
        db.session.commit()

def remove_friend(user_id, friend_id):
    user = User.query.get(user_id)
    friend = User.query.get(friend_id)
    if user and friend:
        user.friends.remove(friend)
        db.session.commit()

def get_friends(user_id):
    user = User.query.get(user_id)
    if user:
        return user.friends
    return []

def are_friends(user_id, friend_id):
    user = User.query.get(user_id)
    friend = User.query.get(friend_id)
    if user and friend:
        return friend in user.friends
    return False