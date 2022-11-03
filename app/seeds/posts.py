from app.models import db, Post, User
from app.utils.reading_speed import read_time_from_string

def seed_posts():

    user1posts = [{
        'title': 'The Raven',
        'image_url': "https://merriam-webster.com/assets/mw/images/gallery/gal-wap-slideshow-slide/raven%20illustration-7803-b172884dac212be4d12172c00df93ad2@1x.jpg",
        'subtitle': 'This poem is often noted for its musicality, stylized language, and supernatural atmosphere.',
        'post': 
        '''Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping—rapping at my chamber door.
"'Tis some visitor," I muttered, "tapping at my chamber door—
Only this and nothing more."

Ah, distinctly I remember, it was in the bleak December,
And each separate dying ember wrought its ghost upon the floor.
Eagerly I wished the morrow;—vainly I had sought to borrow
From my books surcease of sorrow—sorrow for the lost Lenore—
For the rare and radiant maiden whom the angels name Lenore—
Nameless here for evermore.

And the silken sad uncertain rustling of each purple curtain
Thrilled me—filled me with fantastic terrors never felt before;
So that now, to still the beating of my heart, I stood repeating
"'Tis some visitor entreating entrance at my chamber door—
Some late visitor entreating entrance at my chamber door;—
This it is and nothing more."

Presently my soul grew stronger; hesitating then no longer,
"Sir," said I, "or Madam, truly your forgiveness I implore;
But the fact is I was napping, and so gently you came rapping,
And so faintly you came tapping—tapping at my chamber door,
That I scarce was sure I heard you"—here I opened wide the door:—
Darkness there and nothing more.

Deep into that darkness peering, long I stood there wondering, fearing,
Doubting, dreaming dreams no mortal ever dared to dream before;
But the silence was unbroken, and the darkness gave no token,
And the only word there spoken was the whispered word, "Lenore!"
This I whispered, and an echo murmured back the word, "Lenore!"
Merely this and nothing more.

Back into the chamber turning, all my soul within me burning,
Soon I heard again a tapping, somewhat louder than before.
"Surely," said I, "surely that is something at my window lattice;
Let me see, then, what thereat is, and this mystery explore—
Let my heart be still a moment, and this mystery explore;—
'Tis the wind and nothing more."

Open here I flung the shutter, when, with many a flirt and flutter,
In there stepped a stately Raven of the saintly days of yore;
Not the least obeisance made he: not an instant stopped or stayed he;
But, with mien of lord or lady, perched above my chamber door-
Perched upon a bust of Pallas just above my chamber door—
Perched, and sat, and nothing more.

Then this ebony bird beguiling my sad fancy into smiling,
By the grave and stern decorum of the countenance it wore,
"Though thy crest be shorn and shaven, thou," I said, "art sure no craven,
Ghastly grim and ancient Raven wandering from the Nightly shore—
Tell me what thy lordly name is on the Night's Plutonian shore!"
Quoth the Raven, "Nevermore."

Much I marvelled this ungainly fowl to hear discourse so plainly,
Though its answer little meaning—little relevancy bore;
For we cannot help agreeing that no living human being
Ever yet was blessed with seeing bird above his chamber door—
Bird or beast upon the sculptured bust above his chamber door,
With such name as "Nevermore."

But the Raven, sitting lonely on that placid bust, spoke only
That one word, as if his soul in that one word he did outpour.
Nothing further then he uttered—not a feather then he fluttered—
Till I scarcely more than muttered, "Other friends have flown before—
On the morrow he will leave me, as my hopes have flown before."
Then the bird said, "Nevermore."

Startled at the stillness broken by reply so aptly spoken,
"Doubtless," said I, "what it utters is its only stock and store,
Caught from some unhappy master whom unmerciful Disaster
Followed fast and followed faster till his songs one burden bore—
Till the dirges of his Hope the melancholy burden bore
Of 'Never—nevermore.'"

But the Raven still beguiling all my sad soul into smiling,
Straight I wheeled a cushioned seat in front of bird and bust and door;
Then, upon the velvet sinking, I betook myself to linking
Fancy unto fancy, thinking what this ominous bird of yore—
What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
Meant in croaking "Nevermore."

This I sat engaged in guessing, but no syllable expressing
To the fowl whose fiery eyes now burned into my bosom's core;
This and more I sat divining, with my head at ease reclining
On the cushion's velvet lining that the lamp-light gloated o'er,
But whose velvet violet lining with the lamp-light gloating o'er,
She shall press, ah, nevermore!

Then, methought, the air grew denser, perfumed from an unseen censer
Swung by Seraphim whose foot-falls tinkled on the tufted floor.
"Wretch," I cried, "thy God hath lent thee—by these angels he hath sent thee
Respite—respite and nepenthé from thy memories of Lenore!
Quaff, oh quaff this kind nepenthé, and forget this lost Lenore!"
Quoth the Raven, "Nevermore."

"Prophet!" said I, "thing of evil!—prophet still, if bird or devil!—
Whether Tempter sent, or whether tempest tossed thee here ashore,
Desolate yet all undaunted, on this desert land enchanted—
On this home by Horror haunted—tell me truly, I implore—
Is there—is there balm in Gilead?—tell me—tell me, I implore!"
Quoth the Raven, "Nevermore."

"Prophet!" said I, "thing of evil!—prophet still, if bird or devil!
By that Heaven that bends above us — by that God we both adore—
Tell this soul with sorrow laden if, within the distant Aidenn,
It shall clasp a sainted maiden whom the angels name Lenore —
Clasp a rare and radiant maiden whom the angels name Lenore."
Quoth the Raven, "Nevermore."

"Be that word our sign of parting, bird or fiend!" I shrieked, upstarting—
"Get thee back into the tempest and the Night's Plutonian shore!
Leave no black plume as a token of that lie thy soul hath spoken!
Leave my loneliness unbroken!—quit the bust above my door!
Take thy beak from out my heart, and take thy form from off my door!"
Quoth the Raven, "Nevermore."

And the Raven, never flitting, still is sitting, still is sitting
On the pallid bust of Pallas just above my chamber door;
And his eyes have all the seeming of a demon's that is dreaming,
And the lamp-light o'er him streaming throws his shadow on the floor;
And my soul from out that shadow that lies floating on the floor
Shall be lifted—nevermore!''',
    },
    {
        'title': 'Annabel Lee',
        'image_url': "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1606512225i/30437491._SY540_.jpg",
        'subtitle': 'This poem is the last complete poem composed by American author Edgar Allan Poe.',
        'post': '''It was many and many a year ago,
In a kingdom by the sea,
That a maiden there lived whom you may know
By the name of Annabel Lee;
And this maiden she lived with no other thought
Than to love and be loved by me.

I was a child and she was a child,
In this kingdom by the sea:
But we loved with a love that was more than love—
I and my Annabel Lee;
With a love that the winged seraphs of heaven
Coveted her and me.

And this was the reason that, long ago,
In this kingdom by the sea,
A wind blew out of a cloud, chilling
My beautiful Annabel Lee;
So that her highborn kinsmen came
And bore her away from me,
To shut her up in a sepulchre
In this kingdom by the sea.

The angels, not half so happy in heaven,
Went envying her and me—
Yes!—that was the reason (as all men know,
In this kingdom by the sea)
That the wind came out of the cloud by night,
Chilling and killing my Annabel Lee.

But our love it was stronger by far than the love
Of those who were older than we—
Of many far wiser than we—
And neither the angels in heaven above,
Nor the demons down under the sea,
Can ever dissever my soul from the soul
Of the beautiful Annabel Lee.

For the moon never beams without bringing me dreams
Of the beautiful Annabel Lee;
And the stars never rise but I see the bright eyes
Of the beautiful Annabel Lee;
And so, all the night-tide, I lie down by the side
Of my darling, my darling, my life and my bride,
In her sepulchre there by the sea—
In her tomb by the side of the sea.'''
    },
    {
        'title': 'A Dream within a Dream',
        'image_url': "https://th-thumbnailer.cdn-si-edu.com/BgwxEbISvCGjFf8oZanaDGry_YU=/1000x750/filters:no_upscale():focal(1096x852:1097x853)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/c0/b4/c0b41ae2-b449-4157-a874-34f78c0279ee/poe-portrait.jpg",
        'subtitle': 'The poem dramatizes the confusion felt by the narrator as he watches the important things in life slip away.',
        'post': '''Take this kiss upon the brow!
And, in parting from you now,
Thus much let me avow—
You are not wrong, who deem
That my days have been a dream:
Yet if hope has flown away
In a night, or in a day,
In a vision or in none,
Is it therefore the less gone?
All that we see or seem
Is but a dream within a dream.

I stand amid the roar
Of a surf-tormented shore,
And I hold within my hand
Grains of the golden sand—
How few! yet how they creep
Through my fingers to the deep
While I weep—while I weep!
O God! can I not grasp
Them with a tighter clasp?
O God! can I not save
One from the pitiless wave?
Is all that we see or seem
But a dream within a dream?'''
    },]

    users = User.query.all()

    for post in user1posts:
        cur_post = Post(title=post['title'], 
        post=post['post'], 
        read_time=read_time_from_string(post['post']),
        image_url=post['image_url'],
        subtitle=post['subtitle']
        )

        users[0].posts.append(cur_post)

    


    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()

