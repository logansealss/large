from app.models import db, Post, User, Response

def seed_responses():
    users = User.query.all()
    posts = Post.query.all()

    response1 = Response(response="Very interesting. Thanks for sharing.")
    response2 = Response(response="I liked this very much! You are such a great inspiration for me!")
    response3 = Response(response="This is great! Having studied Romantic and Gothic literature, I’m a huge fan of Poe and his influence on the genre.")

    response1.user = users[7]
    response1.post = posts[0]

    response2.user = users[9]
    response2.post = posts[0]

    response3.user = users[6]
    response3.post = posts[0]

    db.session.add(response1)
    db.session.add(response2)
    db.session.add(response3)

    response4 = Response(response="Poe is beyond reach, that is a fact. But we can learn a lot from him. He is one of my favorite writers ever!")
    response5 = Response(response="I have loved Poe since I first read his works in Jr. High.")

    response4.user = users[10]
    response4.post = posts[1]

    response5.user = users[12]
    response5.post = posts[1]

    db.session.add(response4)
    db.session.add(response5)

    response6 = Response(response="I’m copying down this poem into my notebook.")
    response7 = Response(response="Nice.")
    response8 = Response(response="Your post is great. I think you should also read my posts.")

    response6.user = users[15]
    response6.post = posts[2]

    response7.user = users[13]
    response7.post = posts[2]

    response8.user = users[1]
    response8.post = posts[2]

    db.session.add(response6)
    db.session.add(response7)
    db.session.add(response8)

    response9 = Response(response="The Tell-Tale Heart has been the only story (short or long) that has genuinelly scared me.")
    response10 = Response(response="So much suffering for one person to endure.")

    response9.user = users[21]
    response9.post = posts[3]

    response10.user = users[17]
    response10.post = posts[3]

    db.session.add(response9)
    db.session.add(response10)

    response11 = Response(response="Excited to read part 2")
    response12 = Response(response="Classic horror tale.")

    response11.user = users[6]
    response11.post = posts[4]

    response12.user = users[9]
    response12.post = posts[4]

    db.session.add(response11)
    db.session.add(response12)

    response13 = Response(response="Read a while ago but this was unforgettable. Very, very Creepy!!")

    response13.user = users[15]
    response13.post = posts[5]

    db.session.add(response13)

    response14 = Response(response="Be careful what you wish for")
    response15 = Response(response="Atmosphere, subtlety, thought provocation, quality prose and lingering horror…")

    response14.user = users[22]
    response14.post = posts[6]

    response15.user = users[18]
    response15.post = posts[6]

    db.session.add(response14)
    db.session.add(response15)

    response16 = Response(response="I remember loving/hating this open-ended story in high school, and it’s still an intriguing and memorable read.")
    response17 = Response(response="Another well-worn classic that deserves to be read in the original. Concise and thought provoking and great writing as well. This is enduring for a reason.")
    response18 = Response(response="A thought provoking 5 minute read. Worth reading.")

    response16.user = users[13]
    response16.post = posts[7]

    response17.user = users[12]
    response17.post = posts[7]

    response18.user = users[17]
    response18.post = posts[7]

    db.session.add(response16)
    db.session.add(response17)
    db.session.add(response18)

    response19 = Response(response="This is a short and lovely story. The main theme here was love and the sacrifice you made for your loved ones.")
    response20 = Response(response="Are you ready to sacrifice your most prized possession, for your loved one?")

    response19.user = users[7]
    response19.post = posts[8]

    response20.user = users[11]
    response20.post = posts[8]

    db.session.add(response19)
    db.session.add(response20)

    response21 = Response(response="I haven't read anything by Jack London since I was a child. The writing is beautiful and immersive.")
    response22 = Response(response="Wear something warm when you read this excellent story")
    response23 = Response(response="It's easy to see how this is considered one of the great short stories in literature.")

    response21.user = users[7]
    response21.post = posts[9]

    response22.user = users[6]
    response22.post = posts[9]

    response23.user = users[10]
    response23.post = posts[9]

    db.session.add(response21)
    db.session.add(response22)
    db.session.add(response23)

    db.session.commit()


def undo_responses():
    db.session.execute('TRUNCATE claps RESTART IDENTITY CASCADE;')
    db.session.commit()


