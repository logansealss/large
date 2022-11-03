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
        'subtitle': 'The poem dramatizes the confusion felt by the narrator as the important things in life slip away.',
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
    },
    {
        'title': 'The Tell-Tale Heart',
        'image_url': "https://ichef.bbci.co.uk/images/ic/640x360/p01gd1xq.jpg",
        'subtitle': "The narrator tries to convince the reader of their sanity while describing a murder they committed.",
        'post': '''True!—nervous—very, very dreadfully nervous I had been and am; but why will you say that I am mad? The disease had sharpened my senses—not destroyed—not dulled them. Above all was the sense of hearing acute. I heard all things in the heaven and in the earth. I heard many things in hell. How, then, am I mad? Hearken! and observe how healthily—how calmly I can tell you the whole story.

It is impossible to say how first the idea entered my brain; but once conceived, it haunted me day and night. Object there was none. Passion there was none. I loved the old man. He had never wronged me. He had never given me insult. For his gold I had no desire. I think it was his eye! yes, it was this! He had the eye of a vulture—a pale blue eye, with a film over it. Whenever it fell upon me, my blood ran cold; and so by degrees—very gradually—I made up my mind to take the life of the old man, and thus rid myself of the eye forever.

Now this is the point. You fancy me mad. Madmen know nothing. But you should have seen me. You should have seen how wisely I proceeded—with what caution—with what foresight—with what dissimulation I went to work! I was never kinder to the old man than during the whole week before I killed him. And every night, about midnight, I turned the latch of his door and opened it—oh, so gently! And then, when I had made an opening sufficient for my head, I put in a dark lantern, all closed, closed, that no light shone out, and then I thrust in my head. Oh, you would have laughed to see how cunningly I thrust it in! I moved it slowly—very, very slowly, so that I might not disturb the old man’s sleep. It took me an hour to place my whole head within the opening so far that I could see him as he lay upon his bed. Ha!—would a madman have been so wise as this? And then, when my head was well in the room, I undid the lantern cautiously—oh, so cautiously—cautiously (for the hinges creaked)—I undid it just so much that a single thin ray fell upon the vulture eye. And this I did for seven long nights—every night just at midnight—but I found the eye always closed; and so it was impossible to do the work; for it was not the old man who vexed me, but his Evil Eye. And every morning, when the day broke, I went boldly into the chamber, and spoke courageously to him, calling him by name in a hearty tone, and inquiring how he has passed the night. So you see he would have been a very profound old man, indeed, to suspect that every night, just at twelve, I looked in upon him while he slept.

Upon the eighth night I was more than usually cautious in opening the door. A watch’s minute hand moves more quickly than did mine. Never before that night had I felt the extent of my own powers—of my sagacity. I could scarcely contain my feelings of triumph. To think that there I was, opening the door, little by little, and he not even to dream of my secret deeds or thoughts. I fairly chuckled at the idea; and perhaps he heard me; for he moved on the bed suddenly, as if startled. Now you may think that I drew back—but no. His room was as black as pitch with the thick darkness, (for the shutters were close fastened, through fear of robbers,) and so I knew that he could not see the opening of the door, and I kept pushing it on steadily, steadily.

I had my head in, and was about to open the lantern, when my thumb slipped upon the tin fastening, and the old man sprang up in bed, crying out—“Who’s there?”

I kept quite still and said nothing. For a whole hour I did not move a muscle, and in the meantime I did not hear him lie down. He was still sitting up in the bed listening;—just as I have done, night after night, hearkening to the death watches in the wall.

Presently I heard a slight groan, and I knew it was the groan of mortal terror. It was not a groan of pain or of grief—oh, no!—it was the low stifled sound that arises from the bottom of the soul when overcharged with awe. I knew the sound well. Many a night, just at midnight, when all the world slept, it has welled up from my own bosom, deepening, with its dreadful echo, the terrors that distracted me. I say I knew it well. I knew what the old man felt, and pitied him, although I chuckled at heart. I knew that he had been lying awake ever since the first slight noise, when he had turned in the bed. His fears had been ever since growing upon him. He had been trying to fancy them causeless, but could not. He had been saying to himself—“It is nothing but the wind in the chimney—it is only a mouse crossing the floor,” or “It is merely a cricket which has made a single chirp.” Yes, he had been trying to comfort himself with these suppositions: but he had found all in vain. All in vain; because Death, in approaching him had stalked with his black shadow before him, and enveloped the victim. And it was the mournful influence of the unperceived shadow that caused him to feel—although he neither saw nor heard—to feel the presence of my head within the room.

When I had waited a long time, very patiently, without hearing him lie down, I resolved to open a little—a very, very little crevice in the lantern. So I opened it—you cannot imagine how stealthily, stealthily—until, at length a simple dim ray, like the thread of the spider, shot from out the crevice and fell full upon the vulture eye.

It was open—wide, wide open—and I grew furious as I gazed upon it. I saw it with perfect distinctness—all a dull blue, with a hideous veil over it that chilled the very marrow in my bones; but I could see nothing else of the old man’s face or person: for I had directed the ray as if by instinct, precisely upon the damned spot.

And have I not told you that what you mistake for madness is but over-acuteness of the sense?—now, I say, there came to my ears a low, dull, quick sound, such as a watch makes when enveloped in cotton. I knew that sound well, too. It was the beating of the old man’s heart. It increased my fury, as the beating of a drum stimulates the soldier into courage.

But even yet I refrained and kept still. I scarcely breathed. I held the lantern motionless. I tried how steadily I could maintain the ray upon the eve. Meantime the hellish tattoo of the heart increased. It grew quicker and quicker, and louder and louder every instant. The old man’s terror must have been extreme! It grew louder, I say, louder every moment!—do you mark me well? I have told you that I am nervous: so I am. And now at the dead hour of the night, amid the dreadful silence of that old house, so strange a noise as this excited me to uncontrollable terror. Yet, for some minutes longer I refrained and stood still. But the beating grew louder, louder! I thought the heart must burst. And now a new anxiety seized me—the sound would be heard by a neighbour! The old man’s hour had come! With a loud yell, I threw open the lantern and leaped into the room. He shrieked once—once only. In an instant I dragged him to the floor, and pulled the heavy bed over him. I then smiled gaily, to find the deed so far done. But, for many minutes, the heart beat on with a muffled sound. This, however, did not vex me; it would not be heard through the wall. At length it ceased. The old man was dead. I removed the bed and examined the corpse. Yes, he was stone, stone dead. I placed my hand upon the heart and held it there many minutes. There was no pulsation. He was stone dead. His eye would trouble me no more.

If still you think me mad, you will think so no longer when I describe the wise precautions I took for the concealment of the body. The night waned, and I worked hastily, but in silence. First of all I dismembered the corpse. I cut off the head and the arms and the legs.

I then took up three planks from the flooring of the chamber, and deposited all between the scantlings. I then replaced the boards so cleverly, so cunningly, that no human eye—not even his—could have detected any thing wrong. There was nothing to wash out—no stain of any kind—no blood-spot whatever. I had been too wary for that. A tub had caught all—ha! ha!

When I had made an end of these labors, it was four o’clock—still dark as midnight. As the bell sounded the hour, there came a knocking at the street door. I went down to open it with a light heart,—for what had I now to fear? There entered three men, who introduced themselves, with perfect suavity, as officers of the police. A shriek had been heard by a neighbour during the night; suspicion of foul play had been aroused; information had been lodged at the police office, and they (the officers) had been deputed to search the premises.

I smiled,—for what had I to fear? I bade the gentlemen welcome. The shriek, I said, was my own in a dream. The old man, I mentioned, was absent in the country. I took my visitors all over the house. I bade them search—search well. I led them, at length, to his chamber. I showed them his treasures, secure, undisturbed. In the enthusiasm of my confidence, I brought chairs into the room, and desired them here to rest from their fatigues, while I myself, in the wild audacity of my perfect triumph, placed my own seat upon the very spot beneath which reposed the corpse of the victim.

The officers were satisfied. My manner had convinced them. I was singularly at ease. They sat, and while I answered cheerily, they chatted of familiar things. But, ere long, I felt myself getting pale and wished them gone. My head ached, and I fancied a ringing in my ears: but still they sat and still chatted. The ringing became more distinct:—it continued and became more distinct: I talked more freely to get rid of the feeling: but it continued and gained definiteness—until, at length, I found that the noise was not within my ears.

No doubt I now grew very pale;—but I talked more fluently, and with a heightened voice. Yet the sound increased—and what could I do? It was a low, dull, quick sound—much such a sound as a watch makes when enveloped in cotton. I gasped for breath—and yet the officers heard it not. I talked more quickly—more vehemently; but the noise steadily increased. I arose and argued about trifles, in a high key and with violent gesticulations; but the noise steadily increased. Why would they not be gone? I paced the floor to and fro with heavy strides, as if excited to fury by the observations of the men—but the noise steadily increased. Oh God! what could I do? I foamed—I raved—I swore! I swung the chair upon which I had been sitting, and grated it upon the boards, but the noise arose over all and continually increased. It grew louder—louder—louder! And still the men chatted pleasantly, and smiled. Was it possible they heard not? Almighty God!—no, no! They heard!—they suspected!—they knew!—they were making a mockery of my horror!—this I thought, and this I think. But anything was better than this agony! Anything was more tolerable than this derision! I could bear those hypocritical smiles no longer! I felt that I must scream or die! and now—again!—hark! louder! louder! louder! louder!

“Villains!” I shrieked, “dissemble no more! I admit the deed!—tear up the planks!—here, here!—It is the beating of his hideous heart!”''',



    }
    ]

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

