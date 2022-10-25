from app.models import db, Post, User

def seed_posts():

    posts = []

    users = User.query.all()

    post1 = Post(title="test", post="my post", read_time=5)
    post2 = Post(title="my title", post="this post" , read_time=5)

    users[0].posts.append(post1)
    users[1].posts.append(post2)

    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()

