from app.models import db, Post, User, Clap

def seed_claps():

    claps = []

    users = User.query.all()

    posts = Post.query.all()

    clap1 = Clap(amount=50)

    clap1.user = users[6]
    clap1.post = posts[1]

    db.session.add(clap1)
    db.session.commit()


def undo_claps():
    db.session.execute('TRUNCATE claps RESTART IDENTITY CASCADE;')
    db.session.commit()

