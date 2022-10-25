from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    users = []

    users.append(User(username="9ziggy9",
                  email="davidrogers@user.io",
                  password="password",
                  first_name="David",
                  last_name="Rogers",
                ))
    users.append(User(first_name='Brandon',
                  last_name='Tasaki',
                  email='brandontasaki@user.io',
                  username='brandontasaki',
                  password='password',
                  ))
    users.append(User(first_name='Jae',
                  last_name='Hwang',
                  email='jaehwang@user.io',
                  username='jaehwang',
                  password='password',
                  ))
    users.append(User(first_name='Jake',
                   last_name='Matillano',
                   email='jakematillano@user.io',
                   username='jakematillano',
                   password='password',
                   ))
    users.append(User(first_name='Jessie',
                   last_name='Baron',
                   email='jessiebaron@user.io',
                   username='jessiebaron',
                   password='password',
                   ))
    users.append(User(first_name='Joanna',
                   last_name='Gilbert',
                   email='joannagilbert@user.io',
                   username='joannagilbert',
                   password='password',
                   ))
    users.append(User(first_name='John',
                   last_name='Carrera',
                   email='johncarrera@user.io',
                   username='johncarrera',
                   password='password',
                   ))
    users.append(User(first_name='Logan',
                   last_name='Seals',
                   email='loganseals@user.io',
                   username='loganseals',
                   password='password',
                   ))
    users.append(User(first_name='Kyle',
                   last_name='Kassen',
                   email='kylekassen@user.io',
                   username='kylekassen',
                   password='password',
                   ))
    users.append(User(first_name='Michael',
                   last_name='Jung',
                   email='michaeljung@user.io',
                   username='michaeljung',
                   password='password',
                   ))
    users.append(User(first_name='Na',
                   last_name='Chen',
                   email='nachen@user.io',
                   username='nachen',
                   password='password',
                   ))
    users.append(User(first_name='Samuel',
                   last_name='Suh',
                   email='samuelsuh@user.io',
                   username='samuelsuh',
                   password='password',
                   ))
    users.append(User(first_name='Amanda',
                   last_name='Vien',
                   email='amandavien@user.io',
                   username='amandavien',
                   password='password',
                   ))
    users.append(User(first_name='Yasha',
                   last_name='Yang',
                   email='yashayang@user.io',
                   username='yashayang',
                   password='password',
                   ))
    users.append(User(first_name='Yibo',
                   last_name='Guo',
                   email='yiboguo@user.io',
                   username='yiboguo',
                   password='password',
                   ))
    users.append(User(first_name='Kermit',
                   last_name='Frog',
                   email='kermitfrog@user.io',
                   username='kermitfrog',
                   password='password',
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
