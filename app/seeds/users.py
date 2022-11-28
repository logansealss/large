from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    users = []


    users.append(User(username="edgarallanpoe",
                  email="edgarallanpoe@user.io",
                  password="password",
                  first_name="Edgar Allan",
                  last_name="Poe",
                  about="American writer, poet, editor, and literary critic. Best known for my poetry and short stories, particularly my tales of mystery and the macabre.",
                  image_url="https://static.scientificamerican.com/blogs/cache/file/B548B7E6-A083-4A94-B168567B82246A81_source.jpg"
                ))
    users.append(User(first_name='W W',
                  last_name='Jacobs',
                  email='wwjacobs@user.io',
                  username='wwjacobs',
                  password='password',
                  about="English author of short fiction and drama. Best remembered story is \"The Monkey's Paw\".",
                  image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Picture_of_W._W._Jacobs.jpg"
                  ))
    users.append(User(first_name='Frank',
                  last_name='Stockton',
                  email='frankstockton@user.io',
                  username='frankstockton',
                  password='password',
                  about="American writer and humorist, best known today for a series of innovative children's fairy tales that were widely popular during the last decades of the 19th century.",
                  image_url="https://upload.wikimedia.org/wikipedia/commons/f/f8/Frank_R._Stockton.jpg"
                  ))
    users.append(User(first_name='O',
                  last_name='Henry',
                  email='ohenry@user.io',
                  username='ohenry',
                  password='password',
                  about="American short-story writer whose tales romanticized the commonplace-in particular the life of ordinary people in New York City.",
                  image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/William_Sydney_Porter_by_doubleday.jpg/220px-William_Sydney_Porter_by_doubleday.jpg"
                  ))
    users.append(User(first_name='Jack',
                  last_name='London',
                  email='jacklondon@user.io',
                  username='jacklondon',
                  password='password',
                  about="American novelist and short-story writer whose best-known works depict elemental struggles for survival. One of the most extensively translated of American authors during the 20th century.",
                  image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Jack_London_young.jpg/1200px-Jack_London_young.jpg"
                  ))
    users.append(User(username="davidrogers",
                  email="davidrogers@user.io",
                  password="password",
                  first_name="David",
                  last_name="Rogers",
                  about="🐐 The GOAT 🐐",
                  image_url="https://avatars.githubusercontent.com/u/75019436?v=4"
                ))
    users.append(User(first_name='Brandon',
                  last_name='Tasaki',
                  email='brandontasaki@user.io',
                  username='brandontasaki',
                  password='password',
                  about="hero for fun",
                  image_url="https://avatars.githubusercontent.com/u/102837663?v=4"
                  ))
    users.append(User(first_name='Jae',
                  last_name='Hwang',
                  email='jaehwang@user.io',
                  username='jaehwang',
                  password='password',
                  about="Software Engineer",
                  image_url="https://avatars.githubusercontent.com/u/103082046?s=100&v=4"
                  ))
    users.append(User(first_name='Jake',
                   last_name='Matillano',
                   email='jakematillano@user.io',
                   username='jakematillano',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/106983091?v=4"
                   ))
    users.append(User(first_name='Jessie',
                   last_name='Baron',
                   email='jessiebaron@user.io',
                   username='jessiebaron',
                   password='password',
                   about="Software Engineer",
                   ))
    users.append(User(first_name='Joanna',
                   last_name='Gilbert',
                   email='joannagilbert@user.io',
                   username='joannagilbert',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/106204127?v=4"
                   ))
    users.append(User(first_name='John',
                   last_name='Carrera',
                   email='johncarrera@user.io',
                   username='johncarrera',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/105324675?v=4"
                   ))
    users.append(User(first_name='Logan',
                   last_name='Seals',
                   email='loganseals@user.io',
                   username='loganseals',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/106628994?v=4"
                   ))
    users.append(User(first_name='Kyle',
                   last_name='Kassen',
                   email='kylekassen@user.io',
                   username='kylekassen',
                   password='password',
                   about="Software Engineer",
                   ))
    users.append(User(first_name='Michael',
                   last_name='Jung',
                   email='michaeljung@user.io',
                   username='michaeljung',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/6489585?v=4"
                   ))
    users.append(User(first_name='Na',
                   last_name='Chen',
                   email='nachen@user.io',
                   username='nachen',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/106648598?v=4"
                   ))
    users.append(User(first_name='Samuel',
                   last_name='Suh',
                   email='samuelsuh@user.io',
                   username='samuelsuh',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/106373753?v=4"
                   ))
    users.append(User(first_name='Amanda',
                   last_name='Vien',
                   email='amandavien@user.io',
                   username='amandavien',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/105696861?v=4"
                   ))
    users.append(User(first_name='Yasha',
                   last_name='Yang',
                   email='yashayang@user.io',
                   username='yashayang',
                   password='password',
                   about="Software Engineer",
                   image_url="https://avatars.githubusercontent.com/u/1794317?v=4"
                   ))
    users.append(User(username="alexdam",
                  email="alexdam@user.io",
                  password="password",
                  first_name="Alex",
                  last_name="Dam",
                  about="Software Engineer",
                  image_url="https://avatars.githubusercontent.com/u/106426283?v=4"
                ))
    users.append(User(username="garysong",
                  email="garysong@user.io",
                  password="password",
                  first_name="Gary",
                  last_name="Song",
                  about="Software Engineer",
                  image_url="https://avatars.githubusercontent.com/u/105745865?v=4"
                ))

    for user in users:
        db.session.add(user)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
