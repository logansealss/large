from app.models import db, Post, User, Response

def seed_responses():
    pass

    # reponses = []

    # users = User.query.all()

    # posts = Post.query.all()

    # response1 = Response(response="this is my response")
    # response2 = Response(response="this is another response")

    # response1.user = users[0]
    # response1.post = posts[1]

    # response2.user = users[7]
    # response2.post = posts[0]

    # db.session.add(response1)
    # db.session.add(response2)
    # db.session.commit()


def undo_responses():
    db.session.execute('TRUNCATE claps RESTART IDENTITY CASCADE;')
    db.session.commit()


