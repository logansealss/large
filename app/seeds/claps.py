from app.models import db, Post, User, Clap

def seed_claps():

    users = User.query.all()

    posts = Post.query.all()

    clap1 = Clap(amount=50)
    clap1.user = users[8]
    clap1.post = posts[0]
    db.session.add(clap1)

    clap2 = Clap(amount=7)
    clap2.user = users[9]
    clap2.post = posts[0]
    db.session.add(clap2)

    clap3 = Clap(amount=15)
    clap3.user = users[12]
    clap3.post = posts[0]
    db.session.add(clap3)

    clap4 = Clap(amount=12)
    clap4.user = users[9]
    clap4.post = posts[1]
    db.session.add(clap4)

    clap5 = Clap(amount=29)
    clap5.user = users[20]
    clap5.post = posts[2]
    db.session.add(clap5)

    clap6 = Clap(amount=1)
    clap6.user = users[19]
    clap6.post = posts[2]
    db.session.add(clap6)

    clap7 = Clap(amount=48)
    clap7.user = users[18]
    clap7.post = posts[3]
    db.session.add(clap7)

    clap8 = Clap(amount=14)
    clap8.user = users[10]
    clap8.post = posts[4]
    db.session.add(clap8)

    clap9 = Clap(amount=3)
    clap9.user = users[17]
    clap9.post = posts[4]
    db.session.add(clap9)

    clap10 = Clap(amount=8)
    clap10.user = users[19]
    clap10.post = posts[5]
    db.session.add(clap10)

    clap12 = Clap(amount=14)
    clap12.user = users[17]
    clap12.post = posts[5]
    db.session.add(clap12)

    clap13 = Clap(amount=13)
    clap13.user = users[15]
    clap13.post = posts[6]
    db.session.add(clap13)

    clap14 = Clap(amount=8)
    clap14.user = users[14]
    clap14.post = posts[7]
    db.session.add(clap14)

    clap15 = Clap(amount=15)
    clap15.user = users[7]
    clap15.post = posts[7]
    db.session.add(clap15)

    clap16 = Clap(amount=22)
    clap16.user = users[13]
    clap16.post = posts[8]
    db.session.add(clap16)

    clap17 = Clap(amount=11)
    clap17.user = users[20]
    clap17.post = posts[9]
    db.session.add(clap17)

    clap18 = Clap(amount=36)
    clap18.user = users[10]
    clap18.post = posts[9]
    db.session.add(clap18)

    clap19 = Clap(amount=41)
    clap19.user = users[16]
    clap19.post = posts[9]
    db.session.add(clap19)

    db.session.commit()


def undo_claps():
    db.session.execute('TRUNCATE claps RESTART IDENTITY CASCADE;')
    db.session.commit()

