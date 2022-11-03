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



    }]

    user2posts = [{
        'title': 'THE MONKEY\'S PAW - Part I',
        'image_url': "https://ecdn.teacherspayteachers.com/thumbitem/Short-Story-Collection-Monkeys-Paw-Lady-Tiger-The-Sniper-2360283-1657528900/original-2360283-3.jpg",
        'subtitle': ' Part I of a horror story by English author W. W. Jacobs',
        'post': 
        '''Without, the night was cold and wet, but in the small parlour of Laburnam Villa the blinds were drawn and the fire burned brightly. Father and son were at chess, the former, who possessed ideas about the game involving radical changes, putting his king into such sharp and unnecessary perils that it even provoked comment from the white-haired old lady knitting placidly by the fire.

"Hark at the wind," said Mr. White, who, having seen a fatal mistake after it was too late, was amiably desirous of preventing his son from seeing it.

"I'm listening," said the latter, grimly surveying the board as he stretched out his hand. "Check."

"I should hardly think that he'd come to-night," said his father, with his hand poised over the board.

"Mate," replied the son.

"That's the worst of living so far out," bawled Mr. White, with sudden and unlooked-for violence; "of all the beastly, slushy, out-of-the-way places to live in, this is the worst. Pathway's a bog, and the road's a torrent. I don't know what people are thinking about. I suppose because only two houses in the road are let, they think it doesn't matter."

"Never mind, dear," said his wife, soothingly; "perhaps you'll win the next one."

Mr. White looked up sharply, just in time to intercept a knowing glance between mother and son. The words died away on his lips, and he hid a guilty grin in his thin grey beard.

"There he is," said Herbert White, as the gate banged to loudly and heavy footsteps came toward the door.

The old man rose with hospitable haste, and opening the door, was heard condoling with the new arrival. The new arrival also condoled with himself, so that Mrs. White said, "Tut, tut!" and coughed gently as her husband entered the room, followed by a tall, burly man, beady of eye and rubicund of visage.

"Sergeant-Major Morris," he said, introducing him.

The sergeant-major shook hands, and taking the proffered seat by the fire, watched contentedly while his host got out whiskey and tumblers and stood a small copper kettle on the fire.

At the third glass his eyes got brighter, and he began to talk, the little family circle regarding with eager interest this visitor from distant parts, as he squared his broad shoulders in the chair and spoke of wild scenes and doughty deeds; of wars and plagues and strange peoples.

"Twenty-one years of it," said Mr. White, nodding at his wife and son. "When he went away he was a slip of a youth in the warehouse. Now look at him."

"He don't look to have taken much harm," said Mrs. White, politely.

"I'd like to go to India myself," said the old man, "just to look round a bit, you know."

"Better where you are," said the sergeant-major, shaking his head. He put down the empty glass, and sighing softly, shook it again.

"I should like to see those old temples and fakirs and jugglers," said the old man. "What was that you started telling me the other day about a monkey's paw or something, Morris?"

"Nothing," said the soldier, hastily. "Leastways nothing worth hearing."

"Monkey's paw?" said Mrs. White, curiously.

"Well, it's just a bit of what you might call magic, perhaps," said the sergeant-major, offhandedly.

His three listeners leaned forward eagerly. The visitor absent-mindedly put his empty glass to his lips and then set it down again. His host filled it for him.

"To look at," said the sergeant-major, fumbling in his pocket, "it's just an ordinary little paw, dried to a mummy."

He took something out of his pocket and proffered it. Mrs. White drew back with a grimace, but her son, taking it, examined it curiously.

"And what is there special about it?" inquired Mr. White as he took it from his son, and having examined it, placed it upon the table.

"It had a spell put on it by an old fakir," said the sergeant-major, "a very holy man. He wanted to show that fate ruled people's lives, and that those who interfered with it did so to their sorrow. He put a spell on it so that three separate men could each have three wishes from it."

His manner was so impressive that his hearers were conscious that their light laughter jarred somewhat.

"Well, why don't you have three, sir?" said Herbert White, cleverly.

The soldier regarded him in the way that middle age is wont to regard presumptuous youth. "I have," he said, quietly, and his blotchy face whitened.

"And did you really have the three wishes granted?" asked Mrs. White.

"I did," said the sergeant-major, and his glass tapped against his strong teeth.

"And has anybody else wished?" persisted the old lady.

"The first man had his three wishes. Yes," was the reply; "I don't know what the first two were, but the third was for death. That's how I got the paw."

His tones were so grave that a hush fell upon the group.

"If you've had your three wishes, it's no good to you now, then, Morris," said the old man at last. "What do you keep it for?"

The soldier shook his head. "Fancy, I suppose," he said, slowly. "I did have some idea of selling it, but I don't think I will. It has caused enough mischief already. Besides, people won't buy. They think it's a fairy tale; some of them, and those who do think anything of it want to try it first and pay me afterward."

"If you could have another three wishes," said the old man, eyeing him keenly, "would you have them?"

"I don't know," said the other. "I don't know."

He took the paw, and dangling it between his forefinger and thumb, suddenly threw it upon the fire. White, with a slight cry, stooped down and snatched it off.

"Better let it burn," said the soldier, solemnly.

"If you don't want it, Morris," said the other, "give it to me."

"I won't," said his friend, doggedly. "I threw it on the fire. If you keep it, don't blame me for what happens. Pitch it on the fire again like a sensible man."

The other shook his head and examined his new possession closely. "How do you do it?" he inquired.

"Hold it up in your right hand and wish aloud," said the sergeant-major, "but I warn you of the consequences."

"Sounds like the Arabian Nights," said Mrs. White, as she rose and began to set the supper. "Don't you think you might wish for four pairs of hands for me?"

Her husband drew the talisman from pocket, and then all three burst into laughter as the sergeant-major, with a look of alarm on his face, caught him by the arm.

"If you must wish," he said, gruffly, "wish for something sensible."

Mr. White dropped it back in his pocket, and placing chairs, motioned his friend to the table. In the business of supper the talisman was partly forgotten, and afterward the three sat listening in an enthralled fashion to a second instalment of the soldier's adventures in India.

"If the tale about the monkey's paw is not more truthful than those he has been telling us," said Herbert, as the door closed behind their guest, just in time for him to catch the last train, "we sha'nt make much out of it."

"Did you give him anything for it, father?" inquired Mrs. White, regarding her husband closely.

"A trifle," said he, colouring slightly. "He didn't want it, but I made him take it. And he pressed me again to throw it away."

"Likely," said Herbert, with pretended horror. "Why, we're going to be rich, and famous and happy. Wish to be an emperor, father, to begin with; then you can't be henpecked."

He darted round the table, pursued by the maligned Mrs. White armed with an antimacassar.

Mr. White took the paw from his pocket and eyed it dubiously. "I don't know what to wish for, and that's a fact," he said, slowly. "It seems to me I've got all I want."

"If you only cleared the house, you'd be quite happy, wouldn't you?" said Herbert, with his hand on his shoulder. "Well, wish for two hundred pounds, then; that 'll just do it."

His father, smiling shamefacedly at his own credulity, held up the talisman, as his son, with a solemn face, somewhat marred by a wink at his mother, sat down at the piano and struck a few impressive chords.

"I wish for two hundred pounds," said the old man distinctly.

A fine crash from the piano greeted the words, interrupted by a shuddering cry from the old man. His wife and son ran toward him.

"It moved," he cried, with a glance of disgust at the object as it lay on the floor.

"As I wished, it twisted in my hand like a snake."

"Well, I don't see the money," said his son as he picked it up and placed it on the table, "and I bet I never shall."

"It must have been your fancy, father," said his wife, regarding him anxiously.

He shook his head. "Never mind, though; there's no harm done, but it gave me a shock all the same."

They sat down by the fire again while the two men finished their pipes. Outside, the wind was higher than ever, and the old man started nervously at the sound of a door banging upstairs. A silence unusual and depressing settled upon all three, which lasted until the old couple rose to retire for the night.

"I expect you'll find the cash tied up in a big bag in the middle of your bed," said Herbert, as he bade them good-night, "and something horrible squatting up on top of the wardrobe watching you as you pocket your ill-gotten gains."

He sat alone in the darkness, gazing at the dying fire, and seeing faces in it. The last face was so horrible and so simian that he gazed at it in amazement. It got so vivid that, with a little uneasy laugh, he felt on the table for a glass containing a little water to throw over it. His hand grasped the monkey's paw, and with a little shiver he wiped his hand on his coat and went up to bed.

---END OF PART I---''',
    },{
        'title': 'THE MONKEY\'S PAW - Part II',
        'image_url': "https://ecdn.teacherspayteachers.com/thumbitem/Short-Story-Collection-Monkeys-Paw-Lady-Tiger-The-Sniper-2360283-1657528900/original-2360283-3.jpg",
        'subtitle': ' Part II of a horror story by English author W. W. Jacobs',
        'post': 
        '''In the brightness of the wintry sun next morning as it streamed over the breakfast table he laughed at his fears. There was an air of prosaic wholesomeness about the room which it had lacked on the previous night, and the dirty, shrivelled little paw was pitched on the sideboard with a carelessness which betokened no great belief in its virtues.

"I suppose all old soldiers are the same," said Mrs. White. "The idea of our listening to such nonsense! How could wishes be granted in these days? And if they could, how could two hundred pounds hurt you, father?"

"Might drop on his head from the sky," said the frivolous Herbert.

"Morris said the things happened so naturally," said his father, "that you might if you so wished attribute it to coincidence."

"Well, don't break into the money before I come back," said Herbert as he rose from the table. "I'm afraid it'll turn you into a mean, avaricious man, and we shall have to disown you."

His mother laughed, and following him to the door, watched him down the road; and returning to the breakfast table, was very happy at the expense of her husband's credulity. All of which did not prevent her from scurrying to the door at the postman's knock, nor prevent her from referring somewhat shortly to retired sergeant-majors of bibulous habits when she found that the post brought a tailor's bill.

"Herbert will have some more of his funny remarks, I expect, when he comes home," she said, as they sat at dinner.

"I dare say," said Mr. White, pouring himself out some beer; "but for all that, the thing moved in my hand; that I'll swear to."

"You thought it did," said the old lady soothingly.

"I say it did," replied the other. "There was no thought about it; I had just—- What's the matter?"

His wife made no reply. She was watching the mysterious movements of a man outside, who, peering in an undecided fashion at the house, appeared to be trying to make up his mind to enter. In mental connection with the two hundred pounds, she noticed that the stranger was well dressed, and wore a silk hat of glossy newness. Three times he paused at the gate, and then walked on again. The fourth time he stood with his hand upon it, and then with sudden resolution flung it open and walked up the path. Mrs. White at the same moment placed her hands behind her, and hurriedly unfastening the strings of her apron, put that useful article of apparel beneath the cushion of her chair.

She brought the stranger, who seemed ill at ease, into the room. He gazed at her furtively, and listened in a preoccupied fashion as the old lady apologized for the appearance of the room, and her husband's coat, a garment which he usually reserved for the garden. She then waited as patiently as her sex would permit, for him to broach his business, but he was at first strangely silent.

"I—was asked to call," he said at last, and stooped and picked a piece of cotton from his trousers. "I come from 'Maw and Meggins.'"

The old lady started. "Is anything the matter?" she asked, breathlessly. "Has anything happened to Herbert? What is it? What is it?"

Her husband interposed. "There, there, mother," he said, hastily. "Sit down, and don't jump to conclusions. You've not brought bad news, I'm sure, sir;" and he eyed the other wistfully.

"I'm sorry—" began the visitor.

"Is he hurt?" demanded the mother, wildly.

The visitor bowed in assent. "Badly hurt," he said, quietly, "but he is not in any pain."

"Oh, thank God!" said the old woman, clasping her hands. "Thank God for that! Thank—"

She broke off suddenly as the sinister meaning of the assurance dawned upon her and she saw the awful confirmation of her fears in the other's averted face. She caught her breath, and turning to her slower-witted husband, laid her trembling old hand upon his. There was a long silence.

"He was caught in the machinery," said the visitor at length in a low voice.

"Caught in the machinery," repeated Mr. White, in a dazed fashion, "yes."

He sat staring blankly out at the window, and taking his wife's hand between his own, pressed it as he had been wont to do in their old courting-days nearly forty years before.

"He was the only one left to us," he said, turning gently to the visitor. "It is hard."

The other coughed, and rising, walked slowly to the window. "The firm wished me to convey their sincere sympathy with you in your great loss," he said, without looking round. "I beg that you will understand I am only their servant and merely obeying orders."

There was no reply; the old woman's face was white, her eyes staring, and her breath inaudible; on the husband's face was a look such as his friend the sergeant might have carried into his first action.

"I was to say that 'Maw and Meggins' disclaim all responsibility," continued the other. "They admit no liability at all, but in consideration of your son's services, they wish to present you with a certain sum as compensation."

Mr. White dropped his wife's hand, and rising to his feet, gazed with a look of horror at his visitor. His dry lips shaped the words, "How much?"

"Two hundred pounds," was the answer.

Unconscious of his wife's shriek, the old man smiled faintly, put out his hands like a sightless man, and dropped, a senseless heap, to the floor.

---END OF PART II---''',
    },{
        'title': 'THE MONKEY\'S PAW - Part III',
        'image_url': "https://ecdn.teacherspayteachers.com/thumbitem/Short-Story-Collection-Monkeys-Paw-Lady-Tiger-The-Sniper-2360283-1657528900/original-2360283-3.jpg",
        'subtitle': ' Part III of a horror story by English author W. W. Jacobs',
        'post': 
        '''In the huge new cemetery, some two miles distant, the old people buried their dead, and came back to a house steeped in shadow and silence. It was all over so quickly that at first they could hardly realize it, and remained in a state of expectation as though of something else to happen —something else which was to lighten this load, too heavy for old hearts to bear.

But the days passed, and expectation gave place to resignation—the hopeless resignation of the old, sometimes miscalled, apathy. Sometimes they hardly exchanged a word, for now they had nothing to talk about, and their days were long to weariness.

It was about a week after that the old man, waking suddenly in the night, stretched out his hand and found himself alone. The room was in darkness, and the sound of subdued weeping came from the window. He raised himself in bed and listened.

"Come back," he said, tenderly. "You will be cold."

"It is colder for my son," said the old woman, and wept afresh.

The sound of her sobs died away on his ears. The bed was warm, and his eyes heavy with sleep. He dozed fitfully, and then slept until a sudden wild cry from his wife awoke him with a start.

"The paw!" she cried wildly. "The monkey's paw!"

He started up in alarm. "Where? Where is it? What's the matter?"

She came stumbling across the room toward him. "I want it," she said, quietly. "You've not destroyed it?"

"It's in the parlour, on the bracket," he replied, marvelling. "Why?"

She cried and laughed together, and bending over, kissed his cheek.

"I only just thought of it," she said, hysterically. "Why didn't I think of it before? Why didn't you think of it?"

"Think of what?" he questioned.

"The other two wishes," she replied, rapidly. "We've only had one."

"Was not that enough?" he demanded, fiercely.

"No," she cried, triumphantly; "we'll have one more. Go down and get it quickly, and wish our boy alive again."

The man sat up in bed and flung the bedclothes from his quaking limbs. "Good God, you are mad!" he cried, aghast.

"Get it," she panted; "get it quickly, and wish—Oh, my boy, my boy!"

Her husband struck a match and lit the candle. "Get back to bed," he said, unsteadily. "You don't know what you are saying."

"We had the first wish granted," said the old woman, feverishly; "why not the second?"

"A coincidence," stammered the old man.

"Go and get it and wish," cried his wife, quivering with excitement.

The old man turned and regarded her, and his voice shook. "He has been dead ten days, and besides he—I would not tell you else, but—I could only recognize him by his clothing. If he was too terrible for you to see then, how now?"

"Bring him back," cried the old woman, and dragged him toward the door. "Do you think I fear the child I have nursed?"

He went down in the darkness, and felt his way to the parlour, and then to the mantelpiece. The talisman was in its place, and a horrible fear that the unspoken wish might bring his mutilated son before him ere he could escape from the room seized upon him, and he caught his breath as he found that he had lost the direction of the door. His brow cold with sweat, he felt his way round the table, and groped along the wall until he found himself in the small passage with the unwholesome thing in his hand.

Even his wife's face seemed changed as he entered the room. It was white and expectant, and to his fears seemed to have an unnatural look upon it. He was afraid of her.

"Wish!" she cried, in a strong voice.

"It is foolish and wicked," he faltered.

"Wish!" repeated his wife.

He raised his hand. "I wish my son alive again."

The talisman fell to the floor, and he regarded it fearfully. Then he sank trembling into a chair as the old woman, with burning eyes, walked to the window and raised the blind.

He sat until he was chilled with the cold, glancing occasionally at the figure of the old woman peering through the window. The candle-end, which had burned below the rim of the china candlestick, was throwing pulsating shadows on the ceiling and walls, until, with a flicker larger than the rest, it expired. The old man, with an unspeakable sense of relief at the failure of the talisman, crept back to his bed, and a minute or two afterward the old woman came silently and apathetically beside him.

Neither spoke, but lay silently listening to the ticking of the clock. A stair creaked, and a squeaky mouse scurried noisily through the wall. The darkness was oppressive, and after lying for some time screwing up his courage, he took the box of matches, and striking one, went downstairs for a candle.

At the foot of the stairs the match went out, and he paused to strike another; and at the same moment a knock, so quiet and stealthy as to be scarcely audible, sounded on the front door.

The matches fell from his hand and spilled in the passage. He stood motionless, his breath suspended until the knock was repeated. Then he turned and fled swiftly back to his room, and closed the door behind him. A third knock sounded through the house.

"What's that?" cried the old woman, starting up.

"A rat," said the old man in shaking tones—"a rat. It passed me on the stairs."

His wife sat up in bed listening. A loud knock resounded through the house.

"It's Herbert!" she screamed. "It's Herbert!"

She ran to the door, but her husband was before her, and catching her by the arm, held her tightly.

"What are you going to do?" he whispered hoarsely.

"It's my boy; it's Herbert!" she cried, struggling mechanically. "I forgot it was two miles away. What are you holding me for? Let go. I must open the door."

"For God's sake don't let it in," cried the old man, trembling.

"You're afraid of your own son," she cried, struggling. "Let me go. I'm coming, Herbert; I'm coming."

There was another knock, and another. The old woman with a sudden wrench broke free and ran from the room. Her husband followed to the landing, and called after her appealingly as she hurried downstairs. He heard the chain rattle back and the bottom bolt drawn slowly and stiffly from the socket. Then the old woman's voice, strained and panting.

"The bolt," she cried, loudly. "Come down. I can't reach it."

But her husband was on his hands and knees groping wildly on the floor in search of the paw. If he could only find it before the thing outside got in. A perfect fusillade of knocks reverberated through the house, and he heard the scraping of a chair as his wife put it down in the passage against the door. He heard the creaking of the bolt as it came slowly back, and at the same moment he found the monkey's paw, and frantically breathed his third and last wish.

The knocking ceased suddenly, although the echoes of it were still in the house. He heard the chair drawn back, and the door opened. A cold wind rushed up the staircase, and a long loud wail of disappointment and misery from his wife gave him courage to run down to her side, and then to the gate beyond. The street lamp flickering opposite shone on a quiet and deserted road.

---END---''',
    },]

    user3posts = [{
        'title': 'The Lady, or the Tiger?',
        'image_url': "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1553867838i/27285306.jpg",
        'subtitle': 'A much-anthologized short story written by Frank R. Stockton in 1882',
        'post': 
        '''In the very olden time there lived a semi-barbaric king, whose ideas, though somewhat polished and sharpened by the progressiveness of distant Latin neighbors, were still large, florid, and untrammeled, as became the half of him which was barbaric. He was a man of exuberant fancy, and, withal, of an authority so irresistible that, at his will, he turned his varied fancies into facts. He was greatly given to self-communing, and, when he and himself agreed upon anything, the thing was done. When every member of his domestic and political systems moved smoothly in its appointed course, his nature was bland and genial; but, whenever there was a little hitch, and some of his orbs got out of their orbits, he was blander and more genial still, for nothing pleased him so much as to make the crooked straight and crush down uneven places.

Among the borrowed notions by which his barbarism had become semified was that of the public arena, in which, by exhibitions of manly and beastly valor, the minds of his subjects were refined and cultured.

But even here the exuberant and barbaric fancy asserted itself. The arena of the king was built, not to give the people an opportunity of hearing the rhapsodies of dying gladiators, nor to enable them to view the inevitable conclusion of a conflict between religious opinions and hungry jaws, but for purposes far better adapted to widen and develop the mental energies of the people. This vast amphitheater, with its encircling galleries, its mysterious vaults, and its unseen passages, was an agent of poetic justice, in which crime was punished, or virtue rewarded, by the decrees of an impartial and incorruptible chance.

When a subject was accused of a crime of sufficient importance to interest the king, public notice was given that on an appointed day the fate of the accused person would be decided in the king's arena, a structure which well deserved its name, for, although its form and plan were borrowed from afar, its purpose emanated solely from the brain of this man, who, every barleycorn a king, knew no tradition to which he owed more allegiance than pleased his fancy, and who ingrafted on every adopted form of human thought and action the rich growth of his barbaric idealism.

When all the people had assembled in the galleries, and the king, surrounded by his court, sat high up on his throne of royal state on one side of the arena, he gave a signal, a door beneath him opened, and the accused subject stepped out into the amphitheater. Directly opposite him, on the other side of the inclosed space, were two doors, exactly alike and side by side. It was the duty and the privilege of the person on trial to walk directly to these doors and open one of them. He could open either door he pleased; he was subject to no guidance or influence but that of the aforementioned impartial and incorruptible chance. If he opened the one, there came out of it a hungry tiger, the fiercest and most cruel that could be procured, which immediately sprang upon him and tore him to pieces as a punishment for his guilt. The moment that the case of the criminal was thus decided, doleful iron bells were clanged, great wails went up from the hired mourners posted on the outer rim of the arena, and the vast audience, with bowed heads and downcast hearts, wended slowly their homeward way, mourning greatly that one so young and fair, or so old and respected, should have merited so dire a fate.

But, if the accused person opened the other door, there came forth from it a lady, the most suitable to his years and station that his majesty could select among his fair subjects, and to this lady he was immediately married, as a reward of his innocence. It mattered not that he might already possess a wife and family, or that his affections might be engaged upon an object of his own selection; the king allowed no such subordinate arrangements to interfere with his great scheme of retribution and reward. The exercises, as in the other instance, took place immediately, and in the arena. Another door opened beneath the king, and a priest, followed by a band of choristers, and dancing maidens blowing joyous airs on golden horns and treading an epithalamic measure, advanced to where the pair stood, side by side, and the wedding was promptly and cheerily solemnized. Then the gay brass bells rang forth their merry peals, the people shouted glad hurrahs, and the innocent man, preceded by children strewing flowers on his path, led his bride to his home.

This was the king's semi-barbaric method of administering justice. Its perfect fairness is obvious. The criminal could not know out of which door would come the lady; he opened either he pleased, without having the slightest idea whether, in the next instant, he was to be devoured or married. On some occasions the tiger came out of one door, and on some out of the other. The decisions of this tribunal were not only fair, they were positively determinate: the accused person was instantly punished if he found himself guilty, and, if innocent, he was rewarded on the spot, whether he liked it or not. There was no escape from the judgments of the king's arena.

The institution was a very popular one. When the people gathered together on one of the great trial days, they never knew whether they were to witness a bloody slaughter or a hilarious wedding. This element of uncertainty lent an interest to the occasion which it could not otherwise have attained. Thus, the masses were entertained and pleased, and the thinking part of the community could bring no charge of unfairness against this plan, for did not the accused person have the whole matter in his own hands?

This semi-barbaric king had a daughter as blooming as his most florid fancies, and with a soul as fervent and imperious as his own. As is usual in such cases, she was the apple of his eye, and was loved by him above all humanity. Among his courtiers was a young man of that fineness of blood and lowness of station common to the conventional heroes of romance who love royal maidens. This royal maiden was well satisfied with her lover, for he was handsome and brave to a degree unsurpassed in all this kingdom, and she loved him with an ardor that had enough of barbarism in it to make it exceedingly warm and strong. This love affair moved on happily for many months, until one day the king happened to discover its existence. He did not hesitate nor waver in regard to his duty in the premises. The youth was immediately cast into prison, and a day was appointed for his trial in the king's arena. This, of course, was an especially important occasion, and his majesty, as well as all the people, was greatly interested in the workings and development of this trial. Never before had such a case occurred; never before had a subject dared to love the daughter of the king. In after years such things became commonplace enough, but then they were in no slight degree novel and startling.

The tiger-cages of the kingdom were searched for the most savage and relentless beasts, from which the fiercest monster might be selected for the arena; and the ranks of maiden youth and beauty throughout the land were carefully surveyed by competent judges in order that the young man might have a fitting bride in case fate did not determine for him a different destiny. Of course, everybody knew that the deed with which the accused was charged had been done. He had loved the princess, and neither he, she, nor any one else, thought of denying the fact; but the king would not think of allowing any fact of this kind to interfere with the workings of the tribunal, in which he took such great delight and satisfaction. No matter how the affair turned out, the youth would be disposed of, and the king would take an aesthetic pleasure in watching the course of events, which would determine whether or not the young man had done wrong in allowing himself to love the princess.

The appointed day arrived. From far and near the people gathered, and thronged the great galleries of the arena, and crowds, unable to gain admittance, massed themselves against its outside walls. The king and his court were in their places, opposite the twin doors, those fateful portals, so terrible in their similarity.

All was ready. The signal was given. A door beneath the royal party opened, and the lover of the princess walked into the arena. Tall, beautiful, fair, his appearance was greeted with a low hum of admiration and anxiety. Half the audience had not known so grand a youth had lived among them. No wonder the princess loved him! What a terrible thing for him to be there!

As the youth advanced into the arena he turned, as the custom was, to bow to the king, but he did not think at all of that royal personage. His eyes were fixed upon the princess, who sat to the right of her father. Had it not been for the moiety of barbarism in her nature it is probable that lady would not have been there, but her intense and fervid soul would not allow her to be absent on an occasion in which she was so terribly interested. From the moment that the decree had gone forth that her lover should decide his fate in the king's arena, she had thought of nothing, night or day, but this great event and the various subjects connected with it. Possessed of more power, influence, and force of character than any one who had ever before been interested in such a case, she had done what no other person had done,—she had possessed herself of the secret of the doors. She knew in which of the two rooms, that lay behind those doors, stood the cage of the tiger, with its open front, and in which waited the lady. Through these thick doors, heavily curtained with skins on the inside, it was impossible that any noise or suggestion should come from within to the person who should approach to raise the latch of one of them. But gold, and the power of a woman's will, had brought the secret to the princess.

And not only did she know in which room stood the lady ready to emerge, all blushing and radiant, should her door be opened, but she knew who the lady was. It was one of the fairest and loveliest of the damsels of the court who had been selected as the reward of the accused youth, should he be proved innocent of the crime of aspiring to one so far above him; and the princess hated her. Often had she seen, or imagined that she had seen, this fair creature throwing glances of admiration upon the person of her lover, and sometimes she thought these glances were perceived, and even returned. Now and then she had seen them talking together; it was but for a moment or two, but much can be said in a brief space; it may have been on most unimportant topics, but how could she know that? The girl was lovely, but she had dared to raise her eyes to the loved one of the princess; and, with all the intensity of the savage blood transmitted to her through long lines of wholly barbaric ancestors, she hated the woman who blushed and trembled behind that silent door.

When her lover turned and looked at her, and his eye met hers as she sat there, paler and whiter than any one in the vast ocean of anxious faces about her, he saw, by that power of quick perception which is given to those whose souls are one, that she knew behind which door crouched the tiger, and behind which stood the lady. He had expected her to know it. He understood her nature, and his soul was assured that she would never rest until she had made plain to herself this thing, hidden to all other lookers-on, even to the king. The only hope for the youth in which there was any element of certainty was based upon the success of the princess in discovering this mystery; and the moment he looked upon her, he saw she had succeeded, as in his soul he knew she would succeed.

Then it was that his quick and anxious glance asked the question: "Which?" It was as plain to her as if he shouted it from where he stood. There was not an instant to be lost. The question was asked in a flash; it must be answered in another.

Her right arm lay on the cushioned parapet before her. She raised her hand, and made a slight, quick movement toward the right. No one but her lover saw her. Every eye but his was fixed on the man in the arena.

He turned, and with a firm and rapid step he walked across the empty space. Every heart stopped beating, every breath was held, every eye was fixed immovably upon that man. Without the slightest hesitation, he went to the door on the right, and opened it.

Now, the point of the story is this: Did the tiger come out of that door, or did the lady?

The more we reflect upon this question, the harder it is to answer. It involves a study of the human heart which leads us through devious mazes of passion, out of which it is difficult to find our way. Think of it, fair reader, not as if the decision of the question depended upon yourself, but upon that hot-blooded, semi-barbaric princess, her soul at a white heat beneath the combined fires of despair and jealousy. She had lost him, but who should have him?

How often, in her waking hours and in her dreams, had she started in wild horror, and covered her face with her hands as she thought of her lover opening the door on the other side of which waited the cruel fangs of the tiger!

But how much oftener had she seen him at the other door! How in her grievous reveries had she gnashed her teeth, and torn her hair, when she saw his start of rapturous delight as he opened the door of the lady! How her soul had burned in agony when she had seen him rush to meet that woman, with her flushing cheek and sparkling eye of triumph; when she had seen him lead her forth, his whole frame kindled with the joy of recovered life; when she had heard the glad shouts from the multitude, and the wild ringing of the happy bells; when she had seen the priest, with his joyous followers, advance to the couple, and make them man and wife before her very eyes; and when she had seen them walk away together upon their path of flowers, followed by the tremendous shouts of the hilarious multitude, in which her one despairing shriek was lost and drowned!

Would it not be better for him to die at once, and go to wait for her in the blessed regions of semi-barbaric futurity?

And yet, that awful tiger, those shrieks, that blood!

Her decision had been indicated in an instant, but it had been made after days and nights of anguished deliberation. She had known she would be asked, she had decided what she would answer, and, without the slightest hesitation, she had moved her hand to the right.

The question of her decision is one not to be lightly considered, and it is not for me to presume to set myself up as the one person able to answer it. And so I leave it with all of you: Which came out of the opened door,—the lady, or the tiger?''',
    },]

    user4posts = [{
        'title': 'The Gift of the Magi',
        'image_url': "https://i1.wp.com/historyofliterature.com/wp-content/uploads/2021/11/30487662._SY540_.jpg",
        'subtitle': 'A young husband and wife deal with the challenge of buying secret Christmas gifts with little money',
        'post': 
        '''One dollar and eighty-seven cents. That was all. And sixty cents of it was in pennies. Pennies saved one and two at a time by bulldozing the grocer and the vegetable man and the butcher until one’s cheeks burned with the silent imputation of parsimony that such close dealing implied. Three times Della counted it. One dollar and eighty-seven cents. And the next day would be Christmas.

There was clearly nothing to do but flop down on the shabby little couch and howl. So Della did it. Which instigates the moral reflection that life is made up of sobs, sniffles, and smiles, with sniffles predominating.

While the mistress of the home is gradually subsiding from the first stage to the second, take a look at the home. A furnished flat at $8 per week. It did not exactly beggar description, but it certainly had that word on the lookout for the mendicancy squad.

In the vestibule below was a letter-box into which no letter would go, and an electric button from which no mortal finger could coax a ring. Also appertaining thereunto was a card bearing the name “Mr. James Dillingham Young.”

The “Dillingham” had been flung to the breeze during a former period of prosperity when its possessor was being paid $30 per week. Now, when the income was shrunk to $20, though, they were thinking seriously of contracting to a modest and unassuming D. But whenever Mr. James Dillingham Young came home and reached his flat above he was called “Jim” and greatly hugged by Mrs. James Dillingham Young, already introduced to you as Della. Which is all very good.

Della finished her cry and attended to her cheeks with the powder rag. She stood by the window and looked out dully at a gray cat walking a gray fence in a gray backyard. Tomorrow would be Christmas Day, and she had only $1.87 with which to buy Jim a present. She had been saving every penny she could for months, with this result. Twenty dollars a week doesn’t go far. Expenses had been greater than she had calculated. They always are. Only $1.87 to buy a present for Jim. Her Jim. Many a happy hour she had spent planning for something nice for him. Something fine and rare and sterling—something just a little bit near to being worthy of the honor of being owned by Jim.

There was a pier glass between the windows of the room. Perhaps you have seen a pier glass in an $8 flat. A very thin and very agile person may, by observing his reflection in a rapid sequence of longitudinal strips, obtain a fairly accurate conception of his looks. Della, being slender, had mastered the art.

Suddenly she whirled from the window and stood before the glass. Her eyes were shining brilliantly, but her face had lost its color within twenty seconds. Rapidly she pulled down her hair and let it fall to its full length.

Now, there were two possessions of the James Dillingham Youngs in which they both took a mighty pride. One was Jim’s gold watch that had been his father’s and his grandfather’s. The other was Della’s hair. Had the queen of Sheba lived in the flat across the airshaft, Della would have let her hair hang out the window some day to dry just to depreciate Her Majesty’s jewels and gifts. Had King Solomon been the janitor, with all his treasures piled up in the basement, Jim would have pulled out his watch every time he passed, just to see him pluck at his beard from envy.

So now Della’s beautiful hair fell about her rippling and shining like a cascade of brown waters. It reached below her knee and made itself almost a garment for her. And then she did it up again nervously and quickly. Once she faltered for a minute and stood still while a tear or two splashed on the worn red carpet.

On went her old brown jacket; on went her old brown hat. With a whirl of skirts and with the brilliant sparkle still in her eyes, she fluttered out the door and down the stairs to the street.

Where she stopped the sign read: “Mme. Sofronie. Hair Goods of All Kinds.” One flight up Della ran, and collected herself, panting. Madame, large, too white, chilly, hardly looked the “Sofronie.”

“Will you buy my hair?” asked Della.

“I buy hair,” said Madame. “Take yer hat off and let’s have a sight at the looks of it.”

Down rippled the brown cascade.

“Twenty dollars,” said Madame, lifting the mass with a practised hand.

“Give it to me quick,” said Della.

Oh, and the next two hours tripped by on rosy wings. Forget the hashed metaphor. She was ransacking the stores for Jim’s present.

She found it at last. It surely had been made for Jim and no one else. There was no other like it in any of the stores, and she had turned all of them inside out. It was a platinum fob chain simple and chaste in design, properly proclaiming its value by substance alone and not by meretricious ornamentation—as all good things should do. It was even worthy of The Watch. As soon as she saw it she knew that it must be Jim’s. It was like him. Quietness and value—the description applied to both. Twenty-one dollars they took from her for it, and she hurried home with the 87 cents. With that chain on his watch Jim might be properly anxious about the time in any company. Grand as the watch was, he sometimes looked at it on the sly on account of the old leather strap that he used in place of a chain.

When Della reached home her intoxication gave way a little to prudence and reason. She got out her curling irons and lighted the gas and went to work repairing the ravages made by generosity added to love. Which is always a tremendous task, dear friends—a mammoth task.

Within forty minutes her head was covered with tiny, close-lying curls that made her look wonderfully like a truant schoolboy. She looked at her reflection in the mirror long, carefully, and critically.

“If Jim doesn’t kill me,” she said to herself, “before he takes a second look at me, he’ll say I look like a Coney Island chorus girl. But what could I do—oh! what could I do with a dollar and eighty-seven cents?”

At 7 o’clock the coffee was made and the frying-pan was on the back of the stove hot and ready to cook the chops.

Jim was never late. Della doubled the fob chain in her hand and sat on the corner of the table near the door that he always entered. Then she heard his step on the stair away down on the first flight, and she turned white for just a moment. She had a habit of saying a little silent prayer about the simplest everyday things, and now she whispered: “Please God, make him think I am still pretty.”

The door opened and Jim stepped in and closed it. He looked thin and very serious. Poor fellow, he was only twenty-two—and to be burdened with a family! He needed a new overcoat and he was without gloves.

Jim stopped inside the door, as immovable as a setter at the scent of quail. His eyes were fixed upon Della, and there was an expression in them that she could not read, and it terrified her. It was not anger, nor surprise, nor disapproval, nor horror, nor any of the sentiments that she had been prepared for. He simply stared at her fixedly with that peculiar expression on his face.

Della wriggled off the table and went for him.

“Jim, darling,” she cried, “don’t look at me that way. I had my hair cut off and sold because I couldn’t have lived through Christmas without giving you a present. It’ll grow out again—you won’t mind, will you? I just had to do it. My hair grows awfully fast. Say ‘Merry Christmas!’ Jim, and let’s be happy. You don’t know what a nice—what a beautiful, nice gift I’ve got for you.”

“You’ve cut off your hair?” asked Jim, laboriously, as if he had not arrived at that patent fact yet even after the hardest mental labor.

“Cut it off and sold it,” said Della. “Don’t you like me just as well, anyhow? I’m me without my hair, ain’t I?”

Jim looked about the room curiously.

“You say your hair is gone?” he said, with an air almost of idiocy.

“You needn’t look for it,” said Della. “It’s sold, I tell you—sold and gone, too. It’s Christmas Eve, boy. Be good to me, for it went for you. Maybe the hairs of my head were numbered,” she went on with sudden serious sweetness, “but nobody could ever count my love for you. Shall I put the chops on, Jim?”

Out of his trance Jim seemed quickly to wake. He enfolded his Della. For ten seconds let us regard with discreet scrutiny some inconsequential object in the other direction. Eight dollars a week or a million a year—what is the difference? A mathematician or a wit would give you the wrong answer. The magi brought valuable gifts, but that was not among them. This dark assertion will be illuminated later on.

Jim drew a package from his overcoat pocket and threw it upon the table.

“Don’t make any mistake, Dell,” he said, “about me. I don’t think there’s anything in the way of a haircut or a shave or a shampoo that could make me like my girl any less. But if you’ll unwrap that package you may see why you had me going a while at first.”

White fingers and nimble tore at the string and paper. And then an ecstatic scream of joy; and then, alas! a quick feminine change to hysterical tears and wails, necessitating the immediate employment of all the comforting powers of the lord of the flat.

For there lay The Combs—the set of combs, side and back, that Della had worshipped long in a Broadway window. Beautiful combs, pure tortoise shell, with jewelled rims—just the shade to wear in the beautiful vanished hair. They were expensive combs, she knew, and her heart had simply craved and yearned over them without the least hope of possession. And now, they were hers, but the tresses that should have adorned the coveted adornments were gone.

But she hugged them to her bosom, and at length she was able to look up with dim eyes and a smile and say: “My hair grows so fast, Jim!”

And then Della leaped up like a little singed cat and cried, “Oh, oh!”

Jim had not yet seen his beautiful present. She held it out to him eagerly upon her open palm. The dull precious metal seemed to flash with a reflection of her bright and ardent spirit.

“Isn’t it a dandy, Jim? I hunted all over town to find it. You’ll have to look at the time a hundred times a day now. Give me your watch. I want to see how it looks on it.”

Instead of obeying, Jim tumbled down on the couch and put his hands under the back of his head and smiled.

“Dell,” said he, “let’s put our Christmas presents away and keep ’em a while. They’re too nice to use just at present. I sold the watch to get the money to buy your combs. And now suppose you put the chops on.”

The magi, as you know, were wise men—wonderfully wise men—who brought gifts to the Babe in the manger. They invented the art of giving Christmas presents. Being wise, their gifts were no doubt wise ones, possibly bearing the privilege of exchange in case of duplication. And here I have lamely related to you the uneventful chronicle of two foolish children in a flat who most unwisely sacrificed for each other the greatest treasures of their house. But in a last word to the wise of these days let it be said that of all who give gifts these two were the wisest. Of all who give and receive gifts, such as they are wisest. Everywhere they are wisest. They are the magi.''',
    },]

    user5posts = [{
        'title': 'To Build a Fire',
        'image_url': "https://4.bp.blogspot.com/-omVj09rwe8M/Wk5MUpZzd6I/AAAAAAAACwc/hfV6dI267S0fNLXWv7miXxpOku6dO1zzQCLcBGAs/s1600/Schoonover.jpg",
        'subtitle': 'An oft-cited example of the naturalist movement that portrays the conflict of man versus nature',
        'post': 
        '''Day had broken cold and grey, exceedingly cold and grey, when the man turned aside from the main Yukon trail and climbed the high earth-bank, where a dim and little-travelled trail led eastward through the fat spruce timberland.  It was a steep bank, and he paused for breath at the top, excusing the act to himself by looking at his watch.  It was nine o’clock.  There was no sun nor hint of sun, though there was not a cloud in the sky.  It was a clear day, and yet there seemed an intangible pall over the face of things, a subtle gloom that made the day dark, and that was due to the absence of sun.  This fact did not worry the man.  He was used to the lack of sun.  It had been days since he had seen the sun, and he knew that a few more days must pass before that cheerful orb, due south, would just peep above the sky-line and dip immediately from view.

The man flung a look back along the way he had come.  The Yukon lay a mile wide and hidden under three feet of ice.  On top of this ice were as many feet of snow.  It was all pure white, rolling in gentle undulations where the ice-jams of the freeze-up had formed.  North and south, as far as his eye could see, it was unbroken white, save for a dark hair-line that curved and twisted from around the spruce-covered island to the south, and that curved and twisted away into the north, where it disappeared behind another spruce-covered island.  This dark hair-line was the trail—the main trail—that led south five hundred miles to the Chilcoot Pass, Dyea, and salt water; and that led north seventy miles to Dawson, and still on to the north a thousand miles to Nulato, and finally to St. Michael on Bering Sea, a thousand miles and half a thousand more.

But all this—the mysterious, far-reaching hairline trail, the absence of sun from the sky, the tremendous cold, and the strangeness and weirdness of it all—made no impression on the man.  It was not because he was long used to it.  He was a new-comer in the land, a chechaquo, and this was his first winter.  The trouble with him was that he was without imagination.  He was quick and alert in the things of life, but only in the things, and not in the significances.  Fifty degrees below zero meant eighty odd degrees of frost.  Such fact impressed him as being cold and uncomfortable, and that was all.  It did not lead him to meditate upon his frailty as a creature of temperature, and upon man’s frailty in general, able only to live within certain narrow limits of heat and cold; and from there on it did not lead him to the conjectural field of immortality and man’s place in the universe.  Fifty degrees below zero stood for a bite of frost that hurt and that must be guarded against by the use of mittens, ear-flaps, warm moccasins, and thick socks.  Fifty degrees below zero was to him just precisely fifty degrees below zero.  That there should be anything more to it than that was a thought that never entered his head.

As he turned to go on, he spat speculatively.  There was a sharp, explosive crackle that startled him.  He spat again.  And again, in the air, before it could fall to the snow, the spittle crackled.  He knew that at fifty below spittle crackled on the snow, but this spittle had crackled in the air.  Undoubtedly it was colder than fifty below—how much colder he did not know.  But the temperature did not matter.  He was bound for the old claim on the left fork of Henderson Creek, where the boys were already.  They had come over across the divide from the Indian Creek country, while he had come the roundabout way to take a look at the possibilities of getting out logs in the spring from the islands in the Yukon.  He would be in to camp by six o’clock; a bit after dark, it was true, but the boys would be there, a fire would be going, and a hot supper would be ready.  As for lunch, he pressed his hand against the protruding bundle under his jacket.  It was also under his shirt, wrapped up in a handkerchief and lying against the naked skin.  It was the only way to keep the biscuits from freezing.  He smiled agreeably to himself as he thought of those biscuits, each cut open and sopped in bacon grease, and each enclosing a generous slice of fried bacon.

He plunged in among the big spruce trees.  The trail was faint.  A foot of snow had fallen since the last sled had passed over, and he was glad he was without a sled, travelling light.  In fact, he carried nothing but the lunch wrapped in the handkerchief.  He was surprised, however, at the cold.  It certainly was cold, he concluded, as he rubbed his numbed nose and cheek-bones with his mittened hand.  He was a warm-whiskered man, but the hair on his face did not protect the high cheek-bones and the eager nose that thrust itself aggressively into the frosty air.

At the man’s heels trotted a dog, a big native husky, the proper wolf-dog, grey-coated and without any visible or temperamental difference from its brother, the wild wolf.  The animal was depressed by the tremendous cold.  It knew that it was no time for travelling.  Its instinct told it a truer tale than was told to the man by the man’s judgment.  In reality, it was not merely colder than fifty below zero; it was colder than sixty below, than seventy below.  It was seventy-five below zero.  Since the freezing-point is thirty-two above zero, it meant that one hundred and seven degrees of frost obtained.  The dog did not know anything about thermometers.  Possibly in its brain there was no sharp consciousness of a condition of very cold such as was in the man’s brain.  But the brute had its instinct.  It experienced a vague but menacing apprehension that subdued it and made it slink along at the man’s heels, and that made it question eagerly every unwonted movement of the man as if expecting him to go into camp or to seek shelter somewhere and build a fire.  The dog had learned fire, and it wanted fire, or else to burrow under the snow and cuddle its warmth away from the air.

The frozen moisture of its breathing had settled on its fur in a fine powder of frost, and especially were its jowls, muzzle, and eyelashes whitened by its crystalled breath.  The man’s red beard and moustache were likewise frosted, but more solidly, the deposit taking the form of ice and increasing with every warm, moist breath he exhaled.  Also, the man was chewing tobacco, and the muzzle of ice held his lips so rigidly that he was unable to clear his chin when he expelled the juice.  The result was that a crystal beard of the colour and solidity of amber was increasing its length on his chin.  If he fell down it would shatter itself, like glass, into brittle fragments.  But he did not mind the appendage.  It was the penalty all tobacco-chewers paid in that country, and he had been out before in two cold snaps.  They had not been so cold as this, he knew, but by the spirit thermometer at Sixty Mile he knew they had been registered at fifty below and at fifty-five.

He held on through the level stretch of woods for several miles, crossed a wide flat of nigger-heads, and dropped down a bank to the frozen bed of a small stream.  This was Henderson Creek, and he knew he was ten miles from the forks.  He looked at his watch.  It was ten o’clock.  He was making four miles an hour, and he calculated that he would arrive at the forks at half-past twelve.  He decided to celebrate that event by eating his lunch there.

The dog dropped in again at his heels, with a tail drooping discouragement, as the man swung along the creek-bed.  The furrow of the old sled-trail was plainly visible, but a dozen inches of snow covered the marks of the last runners.  In a month no man had come up or down that silent creek.  The man held steadily on.  He was not much given to thinking, and just then particularly he had nothing to think about save that he would eat lunch at the forks and that at six o’clock he would be in camp with the boys.  There was nobody to talk to and, had there been, speech would have been impossible because of the ice-muzzle on his mouth.  So he continued monotonously to chew tobacco and to increase the length of his amber beard.

Once in a while the thought reiterated itself that it was very cold and that he had never experienced such cold.  As he walked along he rubbed his cheek-bones and nose with the back of his mittened hand.  He did this automatically, now and again changing hands.  But rub as he would, the instant he stopped his cheek-bones went numb, and the following instant the end of his nose went numb.  He was sure to frost his cheeks; he knew that, and experienced a pang of regret that he had not devised a nose-strap of the sort Bud wore in cold snaps.  Such a strap passed across the cheeks, as well, and saved them.  But it didn’t matter much, after all.  What were frosted cheeks?  A bit painful, that was all; they were never serious.

Empty as the man’s mind was of thoughts, he was keenly observant, and he noticed the changes in the creek, the curves and bends and timber-jams, and always he sharply noted where he placed his feet.  Once, coming around a bend, he shied abruptly, like a startled horse, curved away from the place where he had been walking, and retreated several paces back along the trail.  The creek he knew was frozen clear to the bottom—no creek could contain water in that arctic winter—but he knew also that there were springs that bubbled out from the hillsides and ran along under the snow and on top the ice of the creek.  He knew that the coldest snaps never froze these springs, and he knew likewise their danger.  They were traps.  They hid pools of water under the snow that might be three inches deep, or three feet.  Sometimes a skin of ice half an inch thick covered them, and in turn was covered by the snow.  Sometimes there were alternate layers of water and ice-skin, so that when one broke through he kept on breaking through for a while, sometimes wetting himself to the waist.

That was why he had shied in such panic.  He had felt the give under his feet and heard the crackle of a snow-hidden ice-skin.  And to get his feet wet in such a temperature meant trouble and danger.  At the very least it meant delay, for he would be forced to stop and build a fire, and under its protection to bare his feet while he dried his socks and moccasins.  He stood and studied the creek-bed and its banks, and decided that the flow of water came from the right.  He reflected awhile, rubbing his nose and cheeks, then skirted to the left, stepping gingerly and testing the footing for each step.  Once clear of the danger, he took a fresh chew of tobacco and swung along at his four-mile gait.

In the course of the next two hours he came upon several similar traps.  Usually the snow above the hidden pools had a sunken, candied appearance that advertised the danger.  Once again, however, he had a close call; and once, suspecting danger, he compelled the dog to go on in front.  The dog did not want to go.  It hung back until the man shoved it forward, and then it went quickly across the white, unbroken surface.  Suddenly it broke through, floundered to one side, and got away to firmer footing.  It had wet its forefeet and legs, and almost immediately the water that clung to it turned to ice.  It made quick efforts to lick the ice off its legs, then dropped down in the snow and began to bite out the ice that had formed between the toes.  This was a matter of instinct.  To permit the ice to remain would mean sore feet.  It did not know this.  It merely obeyed the mysterious prompting that arose from the deep crypts of its being.  But the man knew, having achieved a judgment on the subject, and he removed the mitten from his right hand and helped tear out the ice-particles.  He did not expose his fingers more than a minute, and was astonished at the swift numbness that smote them.  It certainly was cold.  He pulled on the mitten hastily, and beat the hand savagely across his chest.

At twelve o’clock the day was at its brightest.  Yet the sun was too far south on its winter journey to clear the horizon.  The bulge of the earth intervened between it and Henderson Creek, where the man walked under a clear sky at noon and cast no shadow.  At half-past twelve, to the minute, he arrived at the forks of the creek.  He was pleased at the speed he had made.  If he kept it up, he would certainly be with the boys by six.  He unbuttoned his jacket and shirt and drew forth his lunch.  The action consumed no more than a quarter of a minute, yet in that brief moment the numbness laid hold of the exposed fingers.  He did not put the mitten on, but, instead, struck the fingers a dozen sharp smashes against his leg.  Then he sat down on a snow-covered log to eat.  The sting that followed upon the striking of his fingers against his leg ceased so quickly that he was startled, he had had no chance to take a bite of biscuit.  He struck the fingers repeatedly and returned them to the mitten, baring the other hand for the purpose of eating.  He tried to take a mouthful, but the ice-muzzle prevented.  He had forgotten to build a fire and thaw out.  He chuckled at his foolishness, and as he chuckled he noted the numbness creeping into the exposed fingers.  Also, he noted that the stinging which had first come to his toes when he sat down was already passing away.  He wondered whether the toes were warm or numbed.  He moved them inside the moccasins and decided that they were numbed.

He pulled the mitten on hurriedly and stood up.  He was a bit frightened.  He stamped up and down until the stinging returned into the feet.  It certainly was cold, was his thought.  That man from Sulphur Creek had spoken the truth when telling how cold it sometimes got in the country.  And he had laughed at him at the time!  That showed one must not be too sure of things.  There was no mistake about it, it was cold.  He strode up and down, stamping his feet and threshing his arms, until reassured by the returning warmth.  Then he got out matches and proceeded to make a fire.  From the undergrowth, where high water of the previous spring had lodged a supply of seasoned twigs, he got his firewood.  Working carefully from a small beginning, he soon had a roaring fire, over which he thawed the ice from his face and in the protection of which he ate his biscuits.  For the moment the cold of space was outwitted.  The dog took satisfaction in the fire, stretching out close enough for warmth and far enough away to escape being singed.

When the man had finished, he filled his pipe and took his comfortable time over a smoke.  Then he pulled on his mittens, settled the ear-flaps of his cap firmly about his ears, and took the creek trail up the left fork.  The dog was disappointed and yearned back toward the fire.  This man did not know cold.  Possibly all the generations of his ancestry had been ignorant of cold, of real cold, of cold one hundred and seven degrees below freezing-point.  But the dog knew; all its ancestry knew, and it had inherited the knowledge.  And it knew that it was not good to walk abroad in such fearful cold.  It was the time to lie snug in a hole in the snow and wait for a curtain of cloud to be drawn across the face of outer space whence this cold came.  On the other hand, there was keen intimacy between the dog and the man.  The one was the toil-slave of the other, and the only caresses it had ever received were the caresses of the whip-lash and of harsh and menacing throat-sounds that threatened the whip-lash.  So the dog made no effort to communicate its apprehension to the man.  It was not concerned in the welfare of the man; it was for its own sake that it yearned back toward the fire.  But the man whistled, and spoke to it with the sound of whip-lashes, and the dog swung in at the man’s heels and followed after.

The man took a chew of tobacco and proceeded to start a new amber beard.  Also, his moist breath quickly powdered with white his moustache, eyebrows, and lashes.  There did not seem to be so many springs on the left fork of the Henderson, and for half an hour the man saw no signs of any.  And then it happened.  At a place where there were no signs, where the soft, unbroken snow seemed to advertise solidity beneath, the man broke through.  It was not deep.  He wetted himself half-way to the knees before he floundered out to the firm crust.

He was angry, and cursed his luck aloud.  He had hoped to get into camp with the boys at six o’clock, and this would delay him an hour, for he would have to build a fire and dry out his foot-gear.  This was imperative at that low temperature—he knew that much; and he turned aside to the bank, which he climbed.  On top, tangled in the underbrush about the trunks of several small spruce trees, was a high-water deposit of dry firewood—sticks and twigs principally, but also larger portions of seasoned branches and fine, dry, last-year’s grasses.  He threw down several large pieces on top of the snow.  This served for a foundation and prevented the young flame from drowning itself in the snow it otherwise would melt.  The flame he got by touching a match to a small shred of birch-bark that he took from his pocket.  This burned even more readily than paper.  Placing it on the foundation, he fed the young flame with wisps of dry grass and with the tiniest dry twigs.

He worked slowly and carefully, keenly aware of his danger.  Gradually, as the flame grew stronger, he increased the size of the twigs with which he fed it.  He squatted in the snow, pulling the twigs out from their entanglement in the brush and feeding directly to the flame.  He knew there must be no failure.  When it is seventy-five below zero, a man must not fail in his first attempt to build a fire—that is, if his feet are wet.  If his feet are dry, and he fails, he can run along the trail for half a mile and restore his circulation.  But the circulation of wet and freezing feet cannot be restored by running when it is seventy-five below.  No matter how fast he runs, the wet feet will freeze the harder.

All this the man knew.  The old-timer on Sulphur Creek had told him about it the previous fall, and now he was appreciating the advice.  Already all sensation had gone out of his feet.  To build the fire he had been forced to remove his mittens, and the fingers had quickly gone numb.  His pace of four miles an hour had kept his heart pumping blood to the surface of his body and to all the extremities.  But the instant he stopped, the action of the pump eased down.  The cold of space smote the unprotected tip of the planet, and he, being on that unprotected tip, received the full force of the blow.  The blood of his body recoiled before it.  The blood was alive, like the dog, and like the dog it wanted to hide away and cover itself up from the fearful cold.  So long as he walked four miles an hour, he pumped that blood, willy-nilly, to the surface; but now it ebbed away and sank down into the recesses of his body.  The extremities were the first to feel its absence.  His wet feet froze the faster, and his exposed fingers numbed the faster, though they had not yet begun to freeze.  Nose and cheeks were already freezing, while the skin of all his body chilled as it lost its blood.

But he was safe.  Toes and nose and cheeks would be only touched by the frost, for the fire was beginning to burn with strength.  He was feeding it with twigs the size of his finger.  In another minute he would be able to feed it with branches the size of his wrist, and then he could remove his wet foot-gear, and, while it dried, he could keep his naked feet warm by the fire, rubbing them at first, of course, with snow.  The fire was a success.  He was safe.  He remembered the advice of the old-timer on Sulphur Creek, and smiled.  The old-timer had been very serious in laying down the law that no man must travel alone in the Klondike after fifty below.  Well, here he was; he had had the accident; he was alone; and he had saved himself.  Those old-timers were rather womanish, some of them, he thought.  All a man had to do was to keep his head, and he was all right.  Any man who was a man could travel alone.  But it was surprising, the rapidity with which his cheeks and nose were freezing.  And he had not thought his fingers could go lifeless in so short a time.  Lifeless they were, for he could scarcely make them move together to grip a twig, and they seemed remote from his body and from him.  When he touched a twig, he had to look and see whether or not he had hold of it.  The wires were pretty well down between him and his finger-ends.

All of which counted for little.  There was the fire, snapping and crackling and promising life with every dancing flame.  He started to untie his moccasins.  They were coated with ice; the thick German socks were like sheaths of iron half-way to the knees; and the mocassin strings were like rods of steel all twisted and knotted as by some conflagration.  For a moment he tugged with his numbed fingers, then, realizing the folly of it, he drew his sheath-knife.

But before he could cut the strings, it happened.  It was his own fault or, rather, his mistake.  He should not have built the fire under the spruce tree.  He should have built it in the open.  But it had been easier to pull the twigs from the brush and drop them directly on the fire.  Now the tree under which he had done this carried a weight of snow on its boughs.  No wind had blown for weeks, and each bough was fully freighted.  Each time he had pulled a twig he had communicated a slight agitation to the tree—an imperceptible agitation, so far as he was concerned, but an agitation sufficient to bring about the disaster.  High up in the tree one bough capsized its load of snow.  This fell on the boughs beneath, capsizing them.  This process continued, spreading out and involving the whole tree.  It grew like an avalanche, and it descended without warning upon the man and the fire, and the fire was blotted out!  Where it had burned was a mantle of fresh and disordered snow.

The man was shocked.  It was as though he had just heard his own sentence of death.  For a moment he sat and stared at the spot where the fire had been.  Then he grew very calm.  Perhaps the old-timer on Sulphur Creek was right.  If he had only had a trail-mate he would have been in no danger now.  The trail-mate could have built the fire.  Well, it was up to him to build the fire over again, and this second time there must be no failure.  Even if he succeeded, he would most likely lose some toes.  His feet must be badly frozen by now, and there would be some time before the second fire was ready.

Such were his thoughts, but he did not sit and think them.  He was busy all the time they were passing through his mind, he made a new foundation for a fire, this time in the open; where no treacherous tree could blot it out.  Next, he gathered dry grasses and tiny twigs from the high-water flotsam.  He could not bring his fingers together to pull them out, but he was able to gather them by the handful.  In this way he got many rotten twigs and bits of green moss that were undesirable, but it was the best he could do.  He worked methodically, even collecting an armful of the larger branches to be used later when the fire gathered strength.  And all the while the dog sat and watched him, a certain yearning wistfulness in its eyes, for it looked upon him as the fire-provider, and the fire was slow in coming.

When all was ready, the man reached in his pocket for a second piece of birch-bark.  He knew the bark was there, and, though he could not feel it with his fingers, he could hear its crisp rustling as he fumbled for it.  Try as he would, he could not clutch hold of it.  And all the time, in his consciousness, was the knowledge that each instant his feet were freezing.  This thought tended to put him in a panic, but he fought against it and kept calm.  He pulled on his mittens with his teeth, and threshed his arms back and forth, beating his hands with all his might against his sides.  He did this sitting down, and he stood up to do it; and all the while the dog sat in the snow, its wolf-brush of a tail curled around warmly over its forefeet, its sharp wolf-ears pricked forward intently as it watched the man.  And the man as he beat and threshed with his arms and hands, felt a great surge of envy as he regarded the creature that was warm and secure in its natural covering.

After a time he was aware of the first far-away signals of sensation in his beaten fingers.  The faint tingling grew stronger till it evolved into a stinging ache that was excruciating, but which the man hailed with satisfaction.  He stripped the mitten from his right hand and fetched forth the birch-bark.  The exposed fingers were quickly going numb again.  Next he brought out his bunch of sulphur matches.  But the tremendous cold had already driven the life out of his fingers.  In his effort to separate one match from the others, the whole bunch fell in the snow.  He tried to pick it out of the snow, but failed.  The dead fingers could neither touch nor clutch.  He was very careful.  He drove the thought of his freezing feet; and nose, and cheeks, out of his mind, devoting his whole soul to the matches.  He watched, using the sense of vision in place of that of touch, and when he saw his fingers on each side the bunch, he closed them—that is, he willed to close them, for the wires were drawn, and the fingers did not obey.  He pulled the mitten on the right hand, and beat it fiercely against his knee.  Then, with both mittened hands, he scooped the bunch of matches, along with much snow, into his lap.  Yet he was no better off.

After some manipulation he managed to get the bunch between the heels of his mittened hands.  In this fashion he carried it to his mouth.  The ice crackled and snapped when by a violent effort he opened his mouth.  He drew the lower jaw in, curled the upper lip out of the way, and scraped the bunch with his upper teeth in order to separate a match.  He succeeded in getting one, which he dropped on his lap.  He was no better off.  He could not pick it up.  Then he devised a way.  He picked it up in his teeth and scratched it on his leg.  Twenty times he scratched before he succeeded in lighting it.  As it flamed he held it with his teeth to the birch-bark.  But the burning brimstone went up his nostrils and into his lungs, causing him to cough spasmodically.  The match fell into the snow and went out.

The old-timer on Sulphur Creek was right, he thought in the moment of controlled despair that ensued: after fifty below, a man should travel with a partner.  He beat his hands, but failed in exciting any sensation.  Suddenly he bared both hands, removing the mittens with his teeth.  He caught the whole bunch between the heels of his hands.  His arm-muscles not being frozen enabled him to press the hand-heels tightly against the matches.  Then he scratched the bunch along his leg.  It flared into flame, seventy sulphur matches at once!  There was no wind to blow them out.  He kept his head to one side to escape the strangling fumes, and held the blazing bunch to the birch-bark.  As he so held it, he became aware of sensation in his hand.  His flesh was burning.  He could smell it.  Deep down below the surface he could feel it.  The sensation developed into pain that grew acute.  And still he endured it, holding the flame of the matches clumsily to the bark that would not light readily because his own burning hands were in the way, absorbing most of the flame.

At last, when he could endure no more, he jerked his hands apart.  The blazing matches fell sizzling into the snow, but the birch-bark was alight.  He began laying dry grasses and the tiniest twigs on the flame.  He could not pick and choose, for he had to lift the fuel between the heels of his hands.  Small pieces of rotten wood and green moss clung to the twigs, and he bit them off as well as he could with his teeth.  He cherished the flame carefully and awkwardly.  It meant life, and it must not perish.  The withdrawal of blood from the surface of his body now made him begin to shiver, and he grew more awkward.  A large piece of green moss fell squarely on the little fire.  He tried to poke it out with his fingers, but his shivering frame made him poke too far, and he disrupted the nucleus of the little fire, the burning grasses and tiny twigs separating and scattering.  He tried to poke them together again, but in spite of the tenseness of the effort, his shivering got away with him, and the twigs were hopelessly scattered.  Each twig gushed a puff of smoke and went out.  The fire-provider had failed.  As he looked apathetically about him, his eyes chanced on the dog, sitting across the ruins of the fire from him, in the snow, making restless, hunching movements, slightly lifting one forefoot and then the other, shifting its weight back and forth on them with wistful eagerness.

The sight of the dog put a wild idea into his head.  He remembered the tale of the man, caught in a blizzard, who killed a steer and crawled inside the carcass, and so was saved.  He would kill the dog and bury his hands in the warm body until the numbness went out of them.  Then he could build another fire.  He spoke to the dog, calling it to him; but in his voice was a strange note of fear that frightened the animal, who had never known the man to speak in such way before.  Something was the matter, and its suspicious nature sensed danger,—it knew not what danger but somewhere, somehow, in its brain arose an apprehension of the man.  It flattened its ears down at the sound of the man’s voice, and its restless, hunching movements and the liftings and shiftings of its forefeet became more pronounced but it would not come to the man.  He got on his hands and knees and crawled toward the dog.  This unusual posture again excited suspicion, and the animal sidled mincingly away.

The man sat up in the snow for a moment and struggled for calmness.  Then he pulled on his mittens, by means of his teeth, and got upon his feet.  He glanced down at first in order to assure himself that he was really standing up, for the absence of sensation in his feet left him unrelated to the earth.  His erect position in itself started to drive the webs of suspicion from the dog’s mind; and when he spoke peremptorily, with the sound of whip-lashes in his voice, the dog rendered its customary allegiance and came to him.  As it came within reaching distance, the man lost his control.  His arms flashed out to the dog, and he experienced genuine surprise when he discovered that his hands could not clutch, that there was neither bend nor feeling in the lingers.  He had forgotten for the moment that they were frozen and that they were freezing more and more.  All this happened quickly, and before the animal could get away, he encircled its body with his arms.  He sat down in the snow, and in this fashion held the dog, while it snarled and whined and struggled.

But it was all he could do, hold its body encircled in his arms and sit there.  He realized that he could not kill the dog.  There was no way to do it.  With his helpless hands he could neither draw nor hold his sheath-knife nor throttle the animal.  He released it, and it plunged wildly away, with tail between its legs, and still snarling.  It halted forty feet away and surveyed him curiously, with ears sharply pricked forward.  The man looked down at his hands in order to locate them, and found them hanging on the ends of his arms.  It struck him as curious that one should have to use his eyes in order to find out where his hands were.  He began threshing his arms back and forth, beating the mittened hands against his sides.  He did this for five minutes, violently, and his heart pumped enough blood up to the surface to put a stop to his shivering.  But no sensation was aroused in the hands.  He had an impression that they hung like weights on the ends of his arms, but when he tried to run the impression down, he could not find it.

A certain fear of death, dull and oppressive, came to him.  This fear quickly became poignant as he realized that it was no longer a mere matter of freezing his fingers and toes, or of losing his hands and feet, but that it was a matter of life and death with the chances against him.  This threw him into a panic, and he turned and ran up the creek-bed along the old, dim trail.  The dog joined in behind and kept up with him.  He ran blindly, without intention, in fear such as he had never known in his life.  Slowly, as he ploughed and floundered through the snow, he began to see things again—the banks of the creek, the old timber-jams, the leafless aspens, and the sky.  The running made him feel better.  He did not shiver.  Maybe, if he ran on, his feet would thaw out; and, anyway, if he ran far enough, he would reach camp and the boys.  Without doubt he would lose some fingers and toes and some of his face; but the boys would take care of him, and save the rest of him when he got there.  And at the same time there was another thought in his mind that said he would never get to the camp and the boys; that it was too many miles away, that the freezing had too great a start on him, and that he would soon be stiff and dead.  This thought he kept in the background and refused to consider.  Sometimes it pushed itself forward and demanded to be heard, but he thrust it back and strove to think of other things.

It struck him as curious that he could run at all on feet so frozen that he could not feel them when they struck the earth and took the weight of his body.  He seemed to himself to skim along above the surface and to have no connection with the earth.  Somewhere he had once seen a winged Mercury, and he wondered if Mercury felt as he felt when skimming over the earth.

His theory of running until he reached camp and the boys had one flaw in it: he lacked the endurance.  Several times he stumbled, and finally he tottered, crumpled up, and fell.  When he tried to rise, he failed.  He must sit and rest, he decided, and next time he would merely walk and keep on going.  As he sat and regained his breath, he noted that he was feeling quite warm and comfortable.  He was not shivering, and it even seemed that a warm glow had come to his chest and trunk.  And yet, when he touched his nose or cheeks, there was no sensation.  Running would not thaw them out.  Nor would it thaw out his hands and feet.  Then the thought came to him that the frozen portions of his body must be extending.  He tried to keep this thought down, to forget it, to think of something else; he was aware of the panicky feeling that it caused, and he was afraid of the panic.  But the thought asserted itself, and persisted, until it produced a vision of his body totally frozen.  This was too much, and he made another wild run along the trail.  Once he slowed down to a walk, but the thought of the freezing extending itself made him run again.

And all the time the dog ran with him, at his heels.  When he fell down a second time, it curled its tail over its forefeet and sat in front of him facing him curiously eager and intent.  The warmth and security of the animal angered him, and he cursed it till it flattened down its ears appeasingly.  This time the shivering came more quickly upon the man.  He was losing in his battle with the frost.  It was creeping into his body from all sides.  The thought of it drove him on, but he ran no more than a hundred feet, when he staggered and pitched headlong.  It was his last panic.  When he had recovered his breath and control, he sat up and entertained in his mind the conception of meeting death with dignity.  However, the conception did not come to him in such terms.  His idea of it was that he had been making a fool of himself, running around like a chicken with its head cut off—such was the simile that occurred to him.  Well, he was bound to freeze anyway, and he might as well take it decently.  With this new-found peace of mind came the first glimmerings of drowsiness.  A good idea, he thought, to sleep off to death.  It was like taking an anæsthetic.  Freezing was not so bad as people thought.  There were lots worse ways to die.

He pictured the boys finding his body next day.  Suddenly he found himself with them, coming along the trail and looking for himself.  And, still with them, he came around a turn in the trail and found himself lying in the snow.  He did not belong with himself any more, for even then he was out of himself, standing with the boys and looking at himself in the snow.  It certainly was cold, was his thought.  When he got back to the States he could tell the folks what real cold was.  He drifted on from this to a vision of the old-timer on Sulphur Creek.  He could see him quite clearly, warm and comfortable, and smoking a pipe.

“You were right, old hoss; you were right,” the man mumbled to the old-timer of Sulphur Creek.

Then the man drowsed off into what seemed to him the most comfortable and satisfying sleep he had ever known.  The dog sat facing him and waiting.  The brief day drew to a close in a long, slow twilight.  There were no signs of a fire to be made, and, besides, never in the dog’s experience had it known a man to sit like that in the snow and make no fire.  As the twilight drew on, its eager yearning for the fire mastered it, and with a great lifting and shifting of forefeet, it whined softly, then flattened its ears down in anticipation of being chidden by the man.  But the man remained silent.  Later, the dog whined loudly.  And still later it crept close to the man and caught the scent of death.  This made the animal bristle and back away.  A little longer it delayed, howling under the stars that leaped and danced and shone brightly in the cold sky.  Then it turned and trotted up the trail in the direction of the camp it knew, where were the other food-providers and fire-providers.''',
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

    for post in user2posts:
        cur_post = Post(title=post['title'], 
        post=post['post'], 
        read_time=read_time_from_string(post['post']),
        image_url=post['image_url'],
        subtitle=post['subtitle']
        )

        users[1].posts.append(cur_post)

    for post in user3posts:
        cur_post = Post(title=post['title'], 
        post=post['post'], 
        read_time=read_time_from_string(post['post']),
        image_url=post['image_url'],
        subtitle=post['subtitle']
        )

        users[2].posts.append(cur_post)

    for post in user4posts:
        cur_post = Post(title=post['title'], 
        post=post['post'], 
        read_time=read_time_from_string(post['post']),
        image_url=post['image_url'],
        subtitle=post['subtitle']
        )

        users[3].posts.append(cur_post)

    for post in user5posts:
        cur_post = Post(title=post['title'], 
        post=post['post'], 
        read_time=read_time_from_string(post['post']),
        image_url=post['image_url'],
        subtitle=post['subtitle']
        )

        users[4].posts.append(cur_post)


    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()

