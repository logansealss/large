from app.models import db, User

def seed_follows():

    users = User.query.all()

    david = users[5]
    for user in users:
        if(user.username != 'davidrogers'):
            david.followers.append(user)

    db.session.commit()


def undo_follows():
    db.session.execute('TRUNCATE follows RESTART IDENTITY CASCADE;')
    db.session.commit()