label flytoegg:
scene chibitate25 with longdissolve
play music "audio/slowpiano.ogg"
"The crisp, early Autumn night air hits my fur harder than usual, getting through to my skin."
"For the first time, Tate picked up the speed without much regard for my comfort, which isn't too bad, since I already got used to flying, at least a little bit."
y simple"We sure are in a rush tonight, huh?"
t "Yep!"
y bored"Is there any point to me asking {i}'why'{/i}?"
t "It is if you wanna break awkward silence."
y "Will I even get a response?"
t "Nope, you'll see when we get there."
t "It's a surprise!"
y "Is it a good surprise, or a murder surprise?"
un ang"I TOLD YOU!"

t "I would never murder you!"
t "You're too cute!"

y pf"You get away with it this time, on behalf of the compliment."

"One statement from him and the cold air no longer bothers me, in fact, one more and my blood will start boiling."
if adventure<=1:
    "We make our way towards a deep part of the forest."
    jump betrayfly
else:
    "I look to the side, seeing the old train tracks in the distance, but we're not going there this time."
    "Instead, this part of the forest is more dense, with taller trees and is just overall wilder looking."
    jump dinnerlabel


label betrayfly:
"The occasional clearings are the only reference points I can find."
jump dinnerlabel
label dinnerlabel:
    if dinner >=1:
        y s"By the way, did you get your room number by any chance?"
        t "Yeah, I went into Oliver's room before coming to yours, and made him tell me."
        y simple"Wasn't he asleep?"
        t "Yeah, so?"
        t "It's easiest to get what I want from him when he's half naked at 1 AM."
        un "Psycho behavior right there."

    else:
        pass


scene nightforest1 with longdissolve
stop music fadeout 2.0
play music "audio/nightsounds.ogg"
"Tate lands on a narrow path between trees and bushes."
"He grabs my hand and guides me hastily through the undergrowth."
"Mind you, it's the middle of the God damn night!"
y bored"Tate, if I hit a spider web, or some small creature falls on me, be sure I will burn this forest to the ground with you in it."
t "Relax Cinderella, it's bright enough out to see where you're going."
t"Plus, it will all be worth it."
y pf"Highly doubt it."

scene nightforest2 with dissolve

"After some time, then we come face to face with a wall of vines, through which Tate, like always, bursts through carrying me with him."
"We are now standing in a bright blue clearing, painted by the moonlight and accentuated by the white daisies growing all over."
"A large tent-like structure stands between some lone trees."
"It looks like an amalgamation between multiple, smaller tents and other materials."

show cat21smug with moveinright

t "Do you like my man hole?"
y surprised"You made it?"
y bored"Also, never call it that again."
t "Why? I thought {i}Hole Guy{/i} would love my {i}Man Hole{/i}."
t "Huehuehue."
y "ha-ha."
t "Yes, I made it from scratch, my hideaway in the middle of the forest."
hide cat21smug
show cat21smile
t "And it's not without purpose."

hide cat21smile with moveoutleft

t "Come, I'll show you something."

scene tent with longdissolve


"We enter the strange tent, bright, warm lights coming alive as Tate sets foot inside."
y surprised"It's even more spacious from the inside."
y "It must've taken you a while to make all of this."

t "I actually got a bit of help from Therium, his summoned Nightfallen were a BIG help in cleaning this place of debris and cutting some trees for me."
y"He didn't seem like the type to go explore the forest for no reason, but maybe I'm wrong."

t"Shhh."

t "Now look."

"He gestures for me to be quiet as we both make our way to the bed, where a pile of blankets and old clothes stood undisturbed."
un bored"He needs you to do his laundry, that's why you're here."
"Better than your murder theory."

show egg with llongdissolve

"Tate slowly takes off the fabrics one by one, revealing hay straws underneath, on top of which stood a large, patterned egg."

y surprised"Holy cow, that is a BIG egg..."
y "Is it real?"

t "Uh-huh."
t "I can feel it moving inside sometimes."

un suspicious"Hmmm..."

y simple"What animal makes eggs that large?"

t "I did some research."
hide egg with dissolve
"He reaches into a wooden cabinet made of sturdy sticks, where a stash of books were neatly stacked."
"He opens up a bird encyclopedia that has multiple marked pages."
show cat20smile with moveinright
t "First I was thinking simple, an ostrich, perhaps?"
y "Those are pretty big."
t "But not big enough!"
t "And not the right shape, or color."
t "Then I thought it might be a roc."
y "A roc would be alarming, considering they can easily prey on people when they're adults."
t "Yeah, those don't appear around here, and even if it did, again, the eggs don't match."
t "So none of these were right, I thought it might be a special case, like an egg laying mammal or something."
y "Could be it."
t "But this other book only has like three species of egg laying mammals, and they're all small."
t "So I was a bit stuck here..."
un sidee"Oh no..."
t "Until I found my answer."
un surprised"Could it be..."
"He takes out a large red book, flips through the pages to a specific place, then quickly flips it around to show me."
hide cat20smile
show cat20determined with vpunch
tun surprised "{b}A dragon!{/b}"
y surprised"A dragon?!"
y "How are you so sure?"
"And how are YOU so sure, Scribbles?"
un simple"It emanates a lot of magic for a simple egg, the shell color matches the description of ancient dragon eggs and the size as well."
t "Because I had a dream about it."
un bored"Sure, or that, that makes way more sense than what I just said."

y "B-but it's impossible, dragons don't exist anymore."
hide cat20determined
show cat21simple
t "Well I never found its mother; perhaps she was the last dragon, then had to abandon her baby in the woods?"
t "I don't know, {i}'how's'{/i} and {i}'why's'{/i} find a way to be a problem, always."

"Scribbles, what's your opinion?"
un simple"Honestly?"
un bored"I have no idea, I never met a dragon, personally."
un "Demons always stood out of dragons' ways, since they're not to be messed with."
un "And how did this egg get here?"
un "Once again, no clue."

"I'm so glad I decided to share my body with an ancient demon, he is so useful and helpful!"

un suspicious"Shove that sarcasm up your ass."

y simple"Well, maybe you don't know much about the egg, but can you answer this one question for me?"

t "What's that?"

y pf"Whyyyyyy at two in the morning?"

hide cat21simple
show cat20

t "Oh, right, I forgot to explain."
t "It's because I kind of wanted you to be here, since it's hatching."

y surprised"WHAT?!"
y "Like, right now?"

hide cat20
show cat20ec

t "Not this very moment, but the baby's stirring way more than usual."
t "I have a feeling it will happen tonight."
"Looking at the egg, I notice it shaking ever so often, barely noticeable."

y simple"You're right, so we just wait until it hatches?"

scene tatecuddle11 with longdissolve

"Tate climbs on the bed, caressing the egg's shell while beckoning me to join him."
t "Pretty much."
t "You don't mind a sleepover party, do you?"

y ec"Not at all."

"I take my shoes and tie off before climbing in."
"Although it's a bed made mainly from tree trunks, branches and hay, serving as a mattress, it is surprisingly comfortable and bouncy."
"The comfort is further enhanced by the numerous pillows and stuffed animals lying around."
"All kept in good condition."
scene tatecuddle1 with llongdissolve
scene CGc3
"We spend some time talking about different possibilities, since it being a dragon is not yet confirmed, not even by Scribbles."
t "I hope it's a boy."
t "I won't be able to teach her any girl stuff if it's a {i}'she'{/i}."
y "What kind of {i}'girl stuff'{/i} would you teach a dragon?"
t "I don't know."
t "{i}'How to kill prey without ruining your claws'{/i}?"
t "{i}'How to catwalk'?{/i}"
t "Actually, I'm pretty good at that one."

y smug"I don't doubt it, for some reason."


"We lay there awake, Tate shut the lights off long ago."
"We watch the egg, watch each other, watch the shadows casted on the tent's walls by the swinging branches outside."
"Watch the cat's eyes begin to close."

scene black with llongdissolve
"And finally watch... nothing."
"My heavy eyelids refuse to blink again, and I begin to drift back to sleep."
stop music fadeout 3.0
"Not even the excitement of a major discovery can keep two young men from lazing in bed."

"..."
scene snowdreambg with longdissolve
play music "audio/blizzard.ogg"
un "..."
un curious"Winter again?"
un sidee"I don't think he's cold, that cat made sure the tent was at a pretty high temperature for the egg."
un "Oh well, let's continue."
un bored"Maybe it has more content this time."
un "Where were we?"
scene snow2 with dissolve
un simple"Oh yeah, the small cloaked figure, fighting against the cruel mother nature, although at the foot of civilization, nobody is around to help him."
un "From his point of view, faint lights can be seen in the distance, but they are in vain, as he collapses from exhaustion, unable to take another step."
scene snow3 with dissolve
un simple"It appears his fate is to die in the town's arm's reach, houses with bright lights in the windows just feet away unable to be helped, not because of heartlessness, but obliviousness."
un bored"And so, he collapses."
un simple"Oh, wait, there's something...someone else?"
scene snow4 with dissolve
scene CGc50
un simple"A pair of white bunny ears, barely taller than the collapsing child."
un "Where did you come from, mysterious stranger?"
un "And what role do you play here?"
un "Friend, foe?"
stop music fadeout 2.0

scene black with dissolve


un bored"Aaaand that's it."
un "We're back to black."
un "Of course."
un "I wonder if the mortal will say anything about the dream this time."
un "I'm not sure he remembers these things when he wakes up."
un "But I won't bother bring them up because I don't care enough to do so."
"..."
un "Still a better love story than {i}Twilight...{/i}"
stop music fadeout 2.0

"..."

scene red with dissolve
play music "audio/pianorelax.ogg" fadein 4.0

"The blackness surrounding me turns into deep crimson, bright light hitting my eyelids from a crack in the tent's walls."
"Multiple of them, actually, beams of warm light hit various parts of my body, leaving a soothing sensation."
scene tatecuddle2 with llongdissolve
scene CGc4
"My eyes open to meet the calm, lightly snoring face of a cat."
"Did... did I sleep in Tate's bed?"
"Wait, what happen-"
"Hmm...why am I cold, it's supposed to be warm in here?"
un bored"Does {i}'snow'{/i} push any buttons?"
"Huh?"
un "Nevermind."
un "Guess that dream was just for me."
"Ok?"
"Oh!"
"The egg!"
"The sleep is flung out of me as I remember the climax of yesterday's night."
"I look at the nest that still holds the egg, a bit more crooked than when we left it."
"It must've moved with its little shakes the baby does inside."
"I check my phone, and since it's almost 8 AM, I decide to wake Tate up."
"Little did I know, time was not the only reason the cat needed to be woken up..."
y surprised"Tate, hey."
y "Hey, Tate!"
t "On-mr-mnt-pls..."
y angry"Tate, wake up!"
y surprised"The egg! Tate!"
t "{i}*snoooore*{/i}"
y bored"Naked twinks in your area."

scene tent
show cat20surprised with moveinright

t "WHERE?!" with hpunch
hide cat20surprised
show cat21bored

t "Oh, it's you... you're not naked."
hide cat21bored
show cat20surprised
t "Hold on!"
t "The egg!"

hide cat20surprised
show cat20simple

t "It didn't hatch yet, did it?"
y simple"That's what I wanted to direct you at..."
y "It didn't, but it is moving way more than yesterday."

"As if per command, light taps can be heard from the egg's direction, and Tate's tail shoots up."
hide cat20simple
show cat20surprised
stop music
play sound "audio/scratch.ogg"

t "IT'S HAPPENING!"
t "IT'S HAPPENING, EVERYBODY STAY CALM!"
y "I'm pretty cal-"
hide cat20surprised
show cat20scream
t "STAY FUCKING CALM!"

hide cat20scream
show cat20worried

t "WE NEED TO TAKE IT OUTSIDE!"

show cat20worried at right with move

y surprised"Why? What's wrong with the nest?"

t "I READ THAT DRAGONS NEED TO BE HATCHED UNDER THE OPEN SKY, I DON'T KNOW, DRAGON BUSINESS, NO MORE QUESTIONS!"
hide cat20worried with moveoutright

"He picks up the egg both gently and hastily, while I hold the curtain open for him."

scene black with dissolve

scene baby1 with longdissolve


t "Told you it was a good idea to get you at night!"
t "You would've missed this!"
y "No kidding, I would not have had time to come all the way over here, unless I was teleported."
play music "audio/forest.ogg" volume 0.6

scene baby2 with llongdissolve
scene CGc5
"He sits down in the golden morning grass, and beckons me over."
"I take a seat in front of him, and help hold the egg with both of my hands."
"Dropping it would be an absolute disaster."
"We hold our breaths, as more and more sounds can be heard from inside."
"Tate's eyes are getting larger with each sound and movement."
"I have to be honest, I'm very curious to see what this really is."
"If it's a dragon..."
"Even Scribbles seems to be waiting patiently, since I don't feel his presence as much as usual."
"Agonizing moment after moment goes by, when-"
scene baby3 with hpunch
play sound "audio/crack.ogg"
"{i}*Crack*{/i}"
"The cat's smirk becomes an open smile, his emotions hardly contained."
"Thankfully, he manages to not shake the egg too much with some self control."
scene baby4 with hpunch
scene CGc6
play sound "audio/crack.ogg"
"Another crack, then another."
play sound "audio/crack.ogg"
"Different emotions surge through me as I contemplate on the birth of a possible dragon."
"Then... a chirp."
play music "audio/outside2.ogg" fadein 3.0 volume 0.5
scene baby6 with longdissolve
scene CGc7
"The sides of the eggshell start to fall, until only a small top part remains, covering the creature's head."
"Seeing Tate frozen in thought, and the creature's struggle to take the eggshell off, I decide to help a bit."
"Underneath it, we find..."
"An actual living, breathing dragon?"
"Blue-violet, shimmering scales cover its whole body with tiny wings attached to its back, too small and pathetic to even be spread properly."

scene baby7 with dissolve
scene CGc8


"Our previously curious faces turn to {i}'aww'{/i} ones, as the little dragon opens his eyes to look at both of us in turn, then chirping happily."
t "Hi there, little guy."
t "I'm your papa."
t "Can you say {i}'pa-pa'{/i}?"
baby "rawr."
y pf"Preeetty sure it can't..."
t "[name], [name] I think I'm gonna cry."
y ec"Can't blame you, you made a new friend today, and what a friend..."
t "He's perfect."
"He dares touch his snout for the first time, as the dragon doesn't protest, he goes in for a pat on the head."
if betray <=0:
    y s"So this is the reason why you kept teleporting away when we were hanging out."
    y "You were checking on the egg."
    t "Yes, I was sooo stressed out over leaving him for more than twenty minutes."
    t "He was hidden, but the magic might've attracted Nightfallen... somehow he remained safe."
    t "My magic traps alerted me sometimes throughout the day, but when I got here everything was fine."
    y "I'm glad!"

else:
    pass


y s"So what now?"
y "How far ahead did you plan this?"

t "This is kind of it."

y simple"..."
y "W-what do you mean?"
t "I didn't ACTUALLY think I was good enough to hatch an egg... so I didn't have high hopes for it, despite how confident or excited I might've looked."

y "Then what are we going to do?"
y "We aren't going to tell anyone, right?"
t "God no!"
t "They would absolutely take him away from me..."
t "I don't want to lose my friend..."
t "You {b}have{/b} to promise you'll keep this a secret."
y surprised"Of course!"
y "This is a big deal."
y s"We could try to hide him in your dorm, or mine, they shouldn't-"
"He shakes his head slowly."
t "I tried that, when he was still in the egg."
t "I was not just keeping him in the middle of the forest because I felt like it."
t "He just wouldn't go through the barrier."
t "Thought he's done for when the barrier spat him back out, and fell on the grass floor."
t "Thus why I didn't think he'd survive."

y simple"Can you teleport with him inside?"
t "No... I already tried that with other Nightfallen years ago."
y pf"Why would you ever attempt that?"
t "For science!"
t "Maybe we can get someone to look after him while I'm not available?"
t "Merina? Dallan? Aiden? Oliver? Chelsie?"
y simple"Tate, they're all leaders or vice leaders, I don't think they have the time..."

t "In that case, Plan B!"
t "I'll just hide him well enough so nobody finds him."
t "You'll behave for papa, won't you little dragonet?"
"He places him on the ground, legs still shaky as he struggles to stand on all fours."
"It takes him a minute, but he gets the hang of it."
"He looks back at his {i}'papa'{/i} with adoring eyes."

"And instantly books it away from him."
t "HEY!"
"I manage to jump in its way before it gains too much distance."
y "You're a fast one for someone so young, {i}'dragonet'{/i}."

t "Bad dragon!"

un "Ugh, tell him to stop calling him that..."
"Scribbles!"
"Finally, you're here."
"What are your comments?"
"What do you think of a dragon in the modern age?"

un "Yeah, it's not a dragon."

"WHAT?!"
"But you said-"
un "I wasn't sure, since dragon eggs look and feel basically the same as wyvern eggs."
"Wyvern?"
"Then what's the difference?"
un "The difference is that wyverns are way smaller, that's why this cub fits in his eggshell like it's a small apartment."
un "Plus they're dumber, and non-magical."
un "The egg itself contains more magic than the cub would ever obtain."
un "In short, it's a wild animal, nothing more."
un "Cute as a baby, vicious as an adult."

"Should I bring the news to Tate?"
un "Sure, then he can help you kill it and-"
"WOAH WOAH WOAH!"
un curious"What?"
"We are NOT killing a baby, even if it's not a dragon, this is Tate's friend."
un "In about four years the cat will be its dinner."
un bored"You are being unreasonable."
"YOU are being heartless."
un suspicious"Then what do you propose?"
un "Teach him calculus and send him to college?"
un eyeroll"No wait, what am I even saying?"
un eyeroll"There is an academy right here in town, he can go there."
"This is serious, stop your comedy."
un "Yes, I know it's serious, that's why I think you should shove a dagger down its throat."
"Gross."
"Don't ever mention this again..."
"And I can feel those eye rolls, mister."

"Well, here goes nothing."

y simple"Hey, Tate?"
y "I have... news, not sure if they're good or bad, but they're realistic."

t "Bleh, realism, worst thing ever created by the gods."
t "I'd rather live in blissful ignorance."
y "I..."
y pf"I'm not sure what-"
t "Just tell me the news."

y simple"I don't think he's a dragon."
y "Or a {i}'he'{/i}."
t "Oh, he's a {i}'he'{/i}, for sure, cuz he's being a {b}dick{/b} already!"

y "What about the dragon part?"

t "What about it?"

y bored"He's NOT a dragon."

t "Are you a dragon expert?"

y simple"No, but I know a thing or two about them."

t "Oh really, then what is he, an oversized lizard?"
y "No, he might be a wyvern."
t "{i}'Might'{/i}?"
t "Very convincing."
y "I mean, all the clues point to it."
y "He's way smaller than his eggshell."
y "And wyverns are less intelligent, as well as magic-less, compared to dragons."

t "So... you're calling my friend scrawny and pathetic-"
y worried"Tate, that's not-"
t "You're calling him stupid-"
y "Not that way, just-"
t "AND, how would you know how magical he is?"
t "You never mentioned you had some kind of magic sensing abilities."
y "Isn't it odd that no Nightfallen found him?"
y "If he were a dragon, he'd ooze with magic."

t "Why would it even matter what he is?"
t "I love him anyway."
y "Wyverns are notoriously known for being untrainable and unpredictable once they grow up."
y "I'm just looking out for you."
t "Thanks, but no thanks."
t "I have parents for that, remember?"
t "Your theories sound interesting, but not too plausible."

t "Now, if you'll excuse me, I need to discipline my son."
"Welp, safe to say he was not too impressed with my knowledge."
t "You little rascal, stop squirming, you can't just run off like that."

"The cub looks at Tate with big glossy eyes, getting ready to scream."
t "Oh, he must be hungry already, I'm not sure when dragons-"
y simple"Wyverns."
t "-are supposed to be fed."
t "Time to take out the reserves."
scene baby8 with dissolve
"He unexpectedly starts to dig at the base of the tree we've been standing under."
"Inches from the surface, he fishes out a bag, full of different kinds of food, wrapped in leaves."

t "I prepared these to feed whatever comes out of the egg."
t "Wasn't sure if it was going to be a carnivore or herbivore or both."
t "But since he's a dragon-"
y simple"Wyvern."

t "-I'm assuming he'll want meat, but maybe some carrots as well?"
t "Here, hold these for a second."
"He hands me the leaf wrap with the rest of the food."
"He dangles vegetables in front of the wyvern; a bell pepper, carrots, cucumbers, but he wrinkles his nose, until he gets a whiff of something much better."
"So he lunges at me, or more so at the leaf pack."
"But my finger becomes collateral damage as he does so."
y worried"Ouch!" with hpunch
y "He bit me."
"I drop the meat that gets devoured in seconds by the savage baby."
t "Damn it."
"Tate brings out a small bandage and fixes it around my finger."

t "Sorry, sorry, I really thought I raised him better..."
t "In his defense, he was just born."

t "Ungrateful child!"
t "Is that how you treat your mother?!"

y confused"Mother?"
y "Are you referring to me?"

t "Who else?"

y "Why aren't I the father?"

t "You give off stronger woman vibes than me."

y bored"Hard disagree."
un "Hard agree."

y "Doesn't matter, I don't want to be his parent."

"Tate covers the baby's ears."
t "How DARE you?!"
t "First you call him a {i}'wyvern'{/i} to his face, and now this?"
t "Why can't you just accept him the way he is?!"
"The wyvern doesn't care, he got his food, so our words are meaningless to him."

t "I bet you want him dead already, don't you?"
un bored"Yes."

y surprised"What?"
y "No, I'm just worried about what we'll do with him!"

"As we continue to argue like a middle-aged married couple, our small friend found a hobby already."
"And that is throwing dirt at his supposed parents."
"An empty belly makes him act up as well, but in a different way."

t "Furthermore, rest assured I'll be waiting for that child supp- Ow!"
y simple"What is he doing?"
t "Why are you throwing dirt, little man?"

"He's digging vigorously with his tiny claws."
un "I think he's making a nest, wyverns prefer cold and humid places."
"We watch him dig for about twenty minutes, at an alarming speed for someone born less than an hour ago."
"He got deep enough that Tate's hand can't even reach the bottom of the small cavern."

y "Well, I suppose that's what we'll do, we'll let him follow his instincts and leave him alone for now."

t "Do you think he'll be ok alone?"
"Looking inside with my phone's flashlight, I can see him coiled up and asleep."

y bored"Yep."
y "Pretty sure he doesn't care about us, at least as long as it has a full belly."

t "I'm gonna have to bring him more food..."
y s"Good thing you can teleport."
y "See, it's not too bad!"

y "He can take care of himself, no matter the species."
t "You..."
t"Yes, you're right!"

t "Speaking of dragon food-"
y simple"Wyvern."
t "Let's go get breakfast!"
y ec"I'm starving!"

if betray >=2:
    "Or so I wanted to say, when a loud stomach growl cuts me off."
    t "Sorry, guess I'm even more ravenous."
    y simple"Did you not have dinner yesterday?"
    t "I couldn't really eat."
    t "Your double betrayal left a bitter taste in my mouth."

    y sad"I'm sorry."
    y "I didn't think it bothered you so much."

    y simple"Although, to be fair, I am allowed to choose who I'm spending my time with, aren't I?"
    t "You can... I just thought we... never mind."
    t "Let's go."

else:

    pass

scene tent2 with dissolve
"Before we get on the broom, Tate places all the books in a bag, except for the one about dragons, and takes them with him."
show catfly with moveinright
t "I'll need to return these to the library."
y "Look who's being a responsible member of society."
t "I do {b}not{/b} want another late fee, apparently they stack."
play music "Audio/wisp.ogg"

scene chibitatedawn with longdissolve


"We missed most of the sunrise dealing with that wyvern, but, apparently, that's not enough for the creature's {i}'papa'{/i} as he continues to worry."
"This cat is visibly anxious."
y pf"Tate, your leg bouncing makes the whole broom vibrate."
y "I don't think I need to explain why that's a bad idea."

t "I can't help it, I know he's technically pretty safe."
y simple"But it's not a guarantee, I know."
t "I-I just need to get my mind off him for now."
t "Overthinking and overreacting will not get me anywhere."
t "That's what mister Sebil always said."
"He pretends to hit the broom's behind like a horse, to make it go faster before picking up the speed with magic."
"But he hits me instead."
y simple"ow."
t "Oops, totally did that by accident, did not mean to touch your ass so roughly."
y smug"As long as it's getting your mind off of him, you can touch me as much as you want."
t "Off of whom?"
"He asks while leaning with both hands on my thighs, and stirring the broom with his legs alone."
y ec"Perfect."
"I wrap my arms over his shoulders as he looks up at me, purring."
"I'm glad I have this calming effect on him."
"Surprisingly, lewd thoughts only cross my mind {i}slightly{/i}"
y surprised"Hey, are those Aiden and Dallan signaling to us?"

t "Oooh, free breakfast awaits!"
play music"audio/outside.ogg" fadein 3.0
scene outside2 with longdissolve

"Our feet touch the ground and Dallan's tail starts wagging like crazy, while Aiden approaches casually."

show cat20smile with moveinright

show wolf20 at right with moveinright
show tiger20bored at left with moveinleft

d "Good morning, [name], hey Tate!"
t "Hewo!"
y s"Hi guys!"
a "You're up early."
t "Things happened this morning, we were a little busy."


d "What did you think of your first night at the academy, [name]?"
d "And I believe it was your first night in a dorm by yourself too, Tate."

t "Yep, but I didn't stay in my dorm, my tent is more awesome."

a "Fleas are pretty cool, I admit."
hide cat20smile
show cat21bored

t "My tent is cleaner and safer than your alcoholic burrow of an apartment."
hide tiger20bored
show tiger20iritated at left
a "You come in uninvited while I'm drunk ONE TIME!"
hide tiger20iritated
show tiger20bored at left
hide wolf20
show wolf20awkward at right
a "It was Chelsie's idea anyway..."
"Dallan chuckles awkwardly trying to change the subject."
d "A nature escapade, huh?"
d "I miss camping with my brothers."
d "Sounds like fun, did you have a campfire as well?"
d "Now I'm craving some s'mores..."

y "No, we didn't do anything fun, except sleep."

hide cat21bored
show cat20smug
hide wolf20awkward
show wolf20simple at right
hide tiger20bored
show tiger20simple at left

t "Come ooon now [name], don't be modest."
t "You can tell them."

a "Tell us what?"
y simple"I thought you didn't want to say anything to anyone about it."
t "Maybe a little tease won't hurt."
hide tiger20simple
show tiger20iritated at left
a "Are you gonna tell us or shut up already?"

t "Why so curious, Aiden?"
hide cat20smug
show cat21smug
t "If you must know-"
t "You could say me and [name] had a baby last night."
hide cat21smug
show cat21blep

t "That's all you need to know."
show cat21blep at right2 zorder 2 with ease

"Tate makes a step behind me, hiding from the tiger that looked like he was going to murder him."
hide tiger20iritated
show tiger20angryright at left
hide wolf20simple
show wolf20blush1 at right zorder 1

a "WHAT?!"
"Dallan's tail stops wagging and his face gets red."
"But nobody is more embarrassed than me."
un bored"I mean, it's TECHNICALLY the truth."
a "DID YOU JUST DRAG HIM INTO THE WOODS TO DO WHATEVER YOU-"
y blush2"No no no no, you don't understand!"
y awkward"By baby he means-"
hide cat21blep
show cat20worried at right2 zorder 2
show cat20worried at center with ease
t "AAAAAAAAHHH SHUT UP!"
t "Don't tell them!"
d "So... did you or did you not..."
y awkward"Nope, we did not, Tate was just joking."
hide wolf20blush1
show wolf20 at right
hide tiger20angryright
show tiger20bored at left
hide cat20worried
show cat20simple

"He calms down with a breath of relief."

a "Right... a joke, of course."
a "You don't seem like the type to do stuff like that on the first day anyway."
a "At least not in the woods with a perverted short cat."

y simple"Thanks?"

if blowjob>=1:
    un "He has no idea..."
    un "Maybe not in the woods, but a random classroom sucking on a juicy meat lollipop for sure."

else:
    pass

t "Joke?"
t "I was being pretty ser-"

"Activate defensive maneuvers!"

y ec"Dallan, are you hungry?"

hide wolf20
show wolf20ec at right

d "So hungry."
d "I stayed up late to finish some paperwork, so my stomach is emptier than usual."
d "I feel like collapsing at any moment..."
y "You should've said so earlier, to the cafeteria!"

hide wolf20ec
show wolf20sadsmile at right

d "I'm sorry, unfortunately I can't go with you right now..."
y simple"Why not?"

d "I have to take Tate to detention."
d "Because of course he got in trouble before classes even started..."

hide cat20simple
show cat20ec

a "Uhm, I think you're forgetting something."
t "I got out of detention!"
t "Because [name] helped me complete the list!"
hide wolf20sadsmile
show wolf20simple at right
d "Ohh, I forgot."
a "PTSD of his detention watching must be hitting you pretty hard to forget something like that."
d "It was horrible every time..."

hide cat20ec
show cat21bored

t "Detention-shmention, can someone take me to some omelets now?"
a "I'm not paying this time."
hide cat21bored
show cat21smug
t "It's so cute you think that."

hide tiger20bored
show tiger20iritated at left

a "Grrr..."

scene black with dissolve
stop music fadeout 3.0


"Tate is so close to stepping on the tiger's tail."
"Getting closer, we start hearing distant chattering as well as the relaxing guitar playlist that always plays inside."
play music "audio/lunch.ogg" fadein 3.0 volume 0.3
scene cafeteriaday with dissolve
"I walk inside the cafeteria with three hot, hungry men at my side, and today, there are no empty seats..."

y simple"Bummer."
y "I guess everyone is hungry in the morning."
show cat21bored with moveinright
t "I am not carrying my food all the way to the park, even if it's such a nice day."
show wolf20tired at right with moveinright
d "I won't survive five more feet without food."

show tiger20bored at left with moveinleft


a "I got this."

hide tiger20bored with moveoutright



"He walks towards a table for six, every seat taken by a group of friends, talking and laughing."
"Their food half finished."
a "I'll give you each twenty dollars to fuck off."
"They look at each other for a second and unanimously agree this is a great deal, since breakfast is not covered by the lunch and dinner card we're offered, this will feed them at least a couple of days."
"They gather up their things, leftovers, rubbish and swipe the table in less than a minute, then one by one take their hard earned cash from Aiden."



hide cat21bored
show cat21smug

a "Empty table acquired."
y ec"Nice!"
d "Thank goodness."
hide wolf20tired with moveoutright

t "Rich bitch privileges."
t "Gotta love capitalism."

hide cat21smug with moveoutright

t "psst."
"Tate whispers in my ear as we place our stuff on the seats."
t "By the way, I know what you're thinking."
t "Don't offer to pay him back, he gets real mad about it."
y simple"Why?"
t "I think he's offended that you think he needs the money."

t "Or because he can't express his emotions and turns them to anger."
t "I have this feeling he feels good buying me food, even if he says otherwise, so I pretend I'm the one who wants him to do so most of the time."
t "He might also offer you pay him back with sex."
t "So just don't."
y "N-noted."



d "Tate, leave your broom on the seats, so people know the table is occupied."
t "Oki doki."



y "Is it right to occupy a table like that?"
a "Yes, it's what everyone does, how else are you supposed to order your food? It doesn't have table service, and if you have no friends to watch the table, everyone has to respect the reserved seats unless more than ten minutes pass."
t "It's a whole system."

scene food with dissolve


"We go up to the counter and grab some trays."
"Thankfully, although the tables are occupied, the line is not too bad."
"My turn comes and I decide on..."
menu:
    "Hmmm, what do I want, I have to remember I'll need to pay for everything I get, unless someone offers to pay, but I won't beg if that doesn't happen."
    "Cereal with milk.":
        $ food +=1
        "I decide to get a bowl of cereal."
        "It's what I usually eat at home, so a taste of home is not so bad."
        "The bowl they come in is full, but it has a safety cap so it doesn't spill."
        jump morefood
    "Cereal with no milk.":
        $ food +=1
        "I decide to get a small bowl of granola."
        "It comes with some yogurt on the side, because what psychopath would order plain cereal? Haha..."
        "..."
        "I like the crunch, ok?"
        jump morefood

    "Cereal with no cereal.":
        $ food +=1
        "I decide to start off the day with a warm glass of milk."
        "Not much of a coffee drinker, tea is more enjoyable in the afternoon and juice has waaaay too much sugar."
        un "What about water?"
        un "Is that not even a choice in this era anymore?"
        "You're so funny Scribbles."
        un "Say that again when your body withers from dehydration."
        jump morefood

    "Cereal with no milk and no cereal.":
        "I decide to grab a bowl for now, in case I need to fill it up with anything later."
        "Down the line, I see that basically all the food is placed in bowls by the servers themselves, so I awkwardly put mine back..."
        un "That is sooo embarrassing for you."
        un "I bet you feel so insecure right now."
        "This is harassment."
        "I will be seeking financial compensation..."
        un "The only thing you seek is dick and social validation."
        un "And you won't get either with that awkward move you just pulled."
        jump morefood



        label morefood:

        menu:
            "What else should I get?"
            "Scrambled eggs and bacon.":
                $ foodsc +=1
                if foodsc >=2:
                    "I should probably not get another one of these."
                    jump morefood
                else:
                    $ food +=1
                    "Next I want some simple yet delicious scrambled eggs and bacon."
                    "I'm predicting that today will be a bit more action heavy than the first day. So some protein and fat will give me lots of energy."
                    "The portion is quite big, not surprising, considering how much physical activity students do at the academy."
                    un "Yeah, thrusting or getting impaled yourself sure is hard work, you need as much energy as you can get, to be the best whore you can be!"
                    jump morefood



            "Shakshuka and toast.":
                $ foodsh +=1
                if foodsh >=2:
                    "I should probably not get another one of these."
                    jump morefood
                else:
                    $ food +=1
                    "I'm thinking about getting a little exotic, and ordering today's special, shakshuka and toast."
                    "I love tomatoes, I love eggs and I love toast, this can not be a bad idea in any way."
                    "The serving itself is very generous, but I'm hungry enough that I should have no problem finishing it."
                    jump morefood



            "Fruit.":
                $ foodfr +=1
                if foodfr >=2:
                    "I should probably not get another one of these."
                    jump morefood
                else:
                    $ food +=1
                    "Something light but filling is what I need right now."
                    "I throw half a papaya, some clementines, a banana and apple slices onto my plate, all this for one buck!"
                    "Talk about a great deal."
                    jump morefood



            "Cream cheese bagel.":
                $ foodba +=1
                if foodba >=2:
                    "I should probably not get another one of these."
                    jump morefood
                else:
                    $ food +=1
                    $ fish +=1
                    "I'm craving the softness of a bagel, with some nice cream cheese spread all over."
                    "The fish, avocado and chives are a big plus as well."
                    "Just heaven."
                    "The server hands me the plate and it gets me confused."
                    "I'm pretty sure I asked for one, yet there are two on the plate."
                    "I don't want to waste money, so I should say something..."
                    y awkward"Ex-"
                    un squint"Stop you idiot, look at the sign."
                    "To my right there's a small cardboard cutout, {i}'Two For the Price of One During Bagel Week!'{/i}"
                    "oh..."
                    "Thanks, Scribbles."
                    un eyeroll"I can't let you be an idiot ALL the time."
                    un "Sometimes you must be spared."
                    "Guess now I have two bagels."
                    jump morefood



            "That's it.":
                if food>=4:
                    "I look down at my tray after getting my food."
                    "I..."
                    "Might've used my stomach to make these decisions, not my brain."
                    "I've never eaten so much in the morning."
                    "It's too late for changes now."
                    jump afterfood2

                elif food <=0:
                    "I look down at my tray aaand... it's empty..."
                    "Nothing out there really tickled my fancy."
                    "Or at least nothing that made me justify paying for."
                    jump afterfood2


                else:
                    "I look down at my tray aaand-"
                    "Yep."
                    "A totally normal amount of food."
                    "I did something normal for once."
                    "Hooray me."
                    jump afterfood2


        label afterfood2:
            scene cafeteriaday with dissolve

            "When we're done, we all make our way to our literally reserved AND paid table."
            "But we're met with a little surprise, when we see Tate's broom thrown on the floor nearby."
            t "MY BABY!"
            show cat20worried at center with moveinleft
            hide cat20worried with moveoutright

            show connor at right with longdissolve
            "A familiar figure standing on a chair, leaned back like he owns the place, with his legs occupying three other seats."
            "Browsing his phone."
            show wolf20simple at left5 with moveinleft
            show tiger20iritatedr at left4 with moveinleft
            "Everyone is a little surprised, except for Aiden."
            "He has fury in his red fiery eyes, but is trying his best to keep calm for now, since it's probably just a misunderstanding."

            a "Excuse me, I think you're in our spot."
            show connor at right2 with ease
            "Connor looks around, under the table and the back of the chair, then delivers a hard blow with one deadpan line."
            show connor at right with ease
            show connorbored at right
            con "I don't see a name on it."
            show cat20simple at left2 zorder 2 with moveinleft
            hide tiger20iritated
            show tiger20angryright at left4
            t "Oooooff."
            "I lightly hit Tate with my elbow, since I don't think out loud comments and reactions are necessary at the moment..."
            "Alright, now the tiger's visibly fuming."
            a "They were {b}obviously{/b} reserved."
            "He gestures to the broom, now in Tate's hand, as he's stroking it's head like a baby."
            con "That's a broom."
            t "It's a MAGIC broom."
            a "It's his belonging, so it counts towards reserving seats."
            hide wolf20simple
            show wolf20tired at left5 zorder 1
            con "And I got magic dust that reserved all the seats in the cafeteria."
            "Dallan is having some demons to fight on his own while this intense showdown is taking place."
            d "{i}*Heavy breathing*{/i}"
            d "I-I can't... I-I need... food."
            "His hands are too full to eat standing up."
            show cat20simple at left5 with ease
            show wolf20apple at left5 with dissolve
            hide wolf20tired

            show cat20simple at left2 with ease
            "Tate takes an apple from his own tray and shoves it in Dallan's mouth, calming him for the time being."
            hide connorbored
            show connor2sur at right



            a "We {b}paid{/b} for these seats."
            hide connorbored
            show connor2sur at right
            con "Oh shit, was the Headmaster here?"
            hide tiger20angryright
            show tiger20iritatedr at left4
            a "No-"
            hide connor2sur
            show connorbored at right
            con "I don't think anyone else can sell these seats legally."
            a "No, we paid the previous people to piss off."
            hide tiger20iritatedr
            show tiger20angryright at left4
            a "Something you need to do before {b}I'm{/b} getting pissed off."
            con "How much?"
            hide tiger20angryright
            show tiger20iritatedr at left4
            a "What?"
            con "How much did you pay them?"
            a "..."
            a "Twenty each."
            con "Here."
            hide connorbored
            show connor2mad at right
            show money at right with dissolve

            "He takes out his wallet, picks out a couple of bills, folds them into each other so they hold some weight-"
            show money at left4 with move
            hide tiger20iritatedr
            show tiger20angry2 at left4 with hpunch
            hide money with dissolve
            "And throws them right between Aiden's eyes."
            un s"Bullseye! Or... tigerseye."
            "That was not a smart move... and everyone that witnessed it can agree with me."
            show tiger20angry2 at center with ease
            "He comes closer to Connor and talks slowly, which is always a bad sign from an angry person."
            hide tiger20angry2
            show tiger20iritatedr
            a "Do you have any idea who this guy is?"
            "Aiden points at Dallan, with the apple still in his teeth, but half eaten."
            hide connor2mad
            show connorbored at right
            a "That's the leader of the Defender's Shard."
            con "Is that supposed to intimidate me?"
            a "No, it should reassure you."
            hide wolf20apple
            show wolf20apple2 at left5
            a "Because the only reason you still have arms to throw money around with, is because he'll stop me from ripping them off."
            hide connorbored
            show connor2sur at right
            "Indeed, Dallan looks like a cute goofy goober right now, with all the food in his hands and mouth, but his eyes are hard fixated on any and all of Aiden's movements."
            "This does get a quick worried reaction out of Connor, but not enough to make him move."

            hide connor2sur
            show connorbored at right

            t "What do you even need this table for?"
            t "You're alone!"

            "Before he can answer, five people come through the door as if summoned by Tate's words."
            hide cat20simple
            show cat20 at left2 zorder 4
            hide connorbored
            show connor2 at right
            "He lights up as he sees them, and I almost facepalm myself."

            "Somehow, people we already met give us the most trouble, I'm not sure if that's good or bad."
            "Let's call it fate."
            "It's the five nerds we convinced to sign our list."

            "They smile as well when they notice me and Tate around the table."
            "One of them in particular, is the happiest, the little dog, I think his name was... Benjie?"
            show tiger20iritatedr at left4 with ease
            show dog at center zorder 3 with moveinleft
            t "Nerds!"
            ben "Hey guys!"
            ben "I see you've already met my new boyfriend."
            con "Hey Bennie."
            hide connor
            show connor2 at right
            show dog at right2 with ease
            "They smooch each other on the lips, and all of us are a bit shocked, for different reasons."
            show dog at center zorder 3 with ease

            t "You got a boyfriend already, Big Ben?"
            y pf"You got {i}him{/i} as your boyfriend?"
            hide tiger20iritatedr
            show tiger20bored at left4 zorder 2
            a "You know one another?"
            hide wolf20apple2
            show wolf20sadsmile at left5 zorder 1
            d "Does that mean we don't get the table after all?"

            ben "I must thank you mister Tate, I followed your advice, and as soon as I entered the Sorcery Shard's room, I met Connor and we hit it off."
            con "He was just too cute to pass up..."
            ben "The others are super excited and supportive as well."

            goo "Hell yeah we are!"
            cal "It was supposed to be me..."
            t "Good for you!"
            t "Aren't you so glad I found you in time?"

            "I was honestly expecting to have a hoard of nerds coming for our heads after realizing we played with their feelings back then, but this is a far better outcome."
            hide connor2
            show connorsur at right

            "For the first time, something more than apathy shows on Connor's face, as his eyes meet mine."
            "Panic, or just pure fear?"
            "Realization must've hit him as hard as it hit me just now."
            "I have the power to destroy his relationship."
            "I give him a sly smirk, and he understands the message."

            if blowjob >=1:
                "How would his brand new boyfriend feel about his new partner getting his cock sucked hours, or minutes before meeting him?"
                "To be fair, I don't think it would bother him too much, Benjie seems too desperate for love to care."
                "But Connor doesn't know that."
                jump connorgo

            else:
                "How would his brand new boyfriend feel about his new partner telling another guy to suck his cock just hours, maybe minutes before meeting him?"
                "Then accepting money when he was denied."
                "To be fair, I don't think it would bother him too much, Benjie seems too desperate for love to care."
                "But Connor doesn't know that."
                jump connorgo


            label connorgo:

            hide connorsur
            show connor2sur at right

            con"Uhm, Benjie, honey, why don't we go eat outside?"
            con"It's a beautiful sunny day, I want fresh air."
            hide dog
            show dogsur zorder 4
            hide wolf20sadsmile
            show wolf20simple at left5 zorder 3
            hide cat20
            show cat20simple at left2 zorder 5
            ben "But then why did you come to catch a table if-"
            con "No buts, let's go."
            con "Been a pleasure meeting you all."
            con "Come on nerdy friends, outside we go."

            show connor2sur at left2 with move
            con "We could all use touching some grass."
            hide dogsur
            hide connor2sur
            with moveoutright
            hide tiger20bored
            show tiger20simple at left4
            "They are all first years aside from Cal, but Connor is much stronger than all of them, and manages to push them back towards the door, while they mumble confused goodbyes."



            show tiger20simple at left
            show wolf20simple at right
            show cat20simple at center
            with ease
            a "What the hell just happened?"
            hide wolf20simple
            show wolf20ec at right
            d "I don't know but we got our table, finally."
            "Dallan places his trays, yes, multiple, on the table and starts eating almost immediately, while me and Tate wave from behind."
            hide cat20simple
            show cat21sad
            t "Aww, we didn't even get to properly introduce Dallan and Aiden to them."
            hide tiger20simple
            show tiger20bored at left

            a "At least I got my money back."
            a "Breakfast is on me today, I guess."
            hide cat21sad
            show cat20ec
            t "Woohoo!"

            a "I swear, these first years get cockier and bolder each year..."

            d "You're the most pleasant first year to be around, [name], and that's not an exaggeration."
            a "That's true."
            y ec"Thanks, I appreciate it."
            t "What about me?"
            "They ignore his question."
            hide cat20ec
            show cat21mad2

            t "Bitches..."



            if food>=4:
                scene cafeteriaday
                show cat20surprised
                show tiger20confused at left
                show wolf20smilemad at right
                "The situation was a little heated until now, but as the waters calmed, everyone got to actually look at what I was carrying."

                t "WOW!"
                a "Are you Dallan's brother from another mother, [name]?"
                t "You are going to get at least twice as big after putting this inside you."
                d "Hey, stop teasing our friend's perfectly normal decision!"
                d "Don't you two have Sorcery auditions today?"
                d "That will require a lot of energy, even more than regular practice, which is already pretty exhausting for first years."
                a "Energy or a food coma?"
                hide tiger20confused
                show tiger20bored at left
                hide cat20surprised
                show cat20smile
                hide wolf20smilemad
                show wolf20 at right
                y scream"I was hungry, ok?!"
                y pf"I mean, I still am, but now that you brought it up, I can see it's too much."
                y "Hmm, you and Tate didn't buy that much, so maybe you could help?"
                "Aiden got a portion of eggs benedict, very sophisticated, and Tate has pancakes, which is not a lot."
                t "That's a good compromise."
                t "You are so considerate, dear friend."
                t "Don't mind if I do."
                "He takes a pancake and uses it as a big spoon to scoop up some food."
                "Aiden is more reluctant to accept the offer but gives in after his own meal disappears in two bites."

                jump afterfood5


            elif food <=0:
                scene cafeteriaday
                show cat20simple
                show tiger20angryright at left
                show wolf20simple at right
                "The situation was a little heated until now, but as the waters calmed, everyone got to actually look at what I was carrying."
                "And I have basically nothing."
                t "Hey, [name], where's your breakfast?"
                a "That bitch stole it, didn't he, I knew-"
                y awkward"No, it's fine, I didn't get anything, I'm just not that hungry."
                hide tiger20angryright
                show tiger20bored at left
                y "I might be a bit nervous."
                y sadsmile"I'm just glad to be here."
                hide wolf20simple
                show wolf20smilemad at right

                d "Nonsense!"
                d "You need energy, don't you and Tate have auditions today at practice?"
                d "You need food!"
                "Dallan had multiple plates around him, so it was no brainer from him to hand me some."
                "I'm not even sure if some of these are considered {i}'breakfast items'{/i}."
                hide cat20simple
                show cat21smile
                t "Yeah, silly, I can't let my hunter partner fail the auditions."
                "He picks some pancakes from his tray and places them on one of the plates from Dallan."
                a "Honestly, I paid over a hundred dollars to get this table for us, even if I got them back, I'll find it offensive if you don't eat."
                "He takes some of his food and gives it to me as well."
                "And so, the empty space in front of me fills up... it might be a bit much."
                un eyeroll"Of course EVeRybOdY wants to fill up your spotted hole."
                un sidee"Lucky bastard."
                y smug"Eating disorders would be impossible around you guys."
                y "I appreciate the gesture."
                hide cat21smile
                show cat21smug
                t "The least we can do for the only {i}'non annoying first year around'{/i}."
                jump afterfood5





            else:
                "We sit down and enjoy our meal."
                "Me, Aiden and Tate having a totally normal amount of plates on our trays, while Dallan... Well, he's a growing boy."
                jump afterfood5

            label afterfood5:
            scene cafeteriaday
            show cat20ec
            show tiger20bored at left
            show wolf20 at right

            y sadsmile"I don't want to be the killjoy in the room, but can we talk about this {i}'practice'{/i} session and these 'auditions'?"
            show cat20ec
            show tiger20bored at left
            show wolf20 at right
            t "Why would you be a killjoy for that?"
            t "It's LITERALLY the BEST part of the year!"
            hide cat20ec
            show cat21smile
            t "Maybe the second best."
            t "I LOVE talking about it."
            y "I just thought you wouldn't like to talk about school stuff."
            t "I LOVE talking about school stuff."
            d "Only when it involves blowing stuff up."
            a "Or if there's sex involved."
            hide cat21smile
            show cat21smug

            t "I'm a simple guy with simple needs."

            y simple"So..."

            hide cat21smug
            show cat20smile

            t "Right, practice."
            t "Basically, Chelsie makes these super cool dummies for first years to fight each year, and every time there is a twist to them."
            d "Last year they had to fight a Volley Of Incomprehensible Darkness."
            d "Or V.O.I.D."
            y "What did it do?"

            a "It was just a hologram made by a small device hidden somewhere in the arena."
            hide cat20smile
            show cat20simple
            t "A scary hologram."
            a "You had to find the device and destroy it, all while the hologram messed with your sensory abilities."
            d "It would've been a nightmare for me to fight, thank goodness I'm not a first year."
            a "A surprising amount of first years failed to even figure out what to do."
            hide cat20simple
            show cat20smile
            t "And two years ago, they had to fight an alligator."
            y "Like.. a robot?"
            hide wolf20
            show wolf20simple at right
            a "No... just a wild alligator."
            d "I thought they were crocodiles."
            a "No, she WANTED crocodiles, but the Headmaster didn't let her use any."
            "And alligators are so much better?"

            y "So in other words, I should prepare myself for the worst..."
            hide wolf20simple
            show wolf20 at right
            d "Who knows what the auditions will hold."
            hide cat20smile
            show cat20
            t "Don't worry, as a recommended student you will have no problem, I'm sure."


            y awkward"Ha ha, yeah... easy."
            "I should change the subject before they talk more about how {i}'awesome'{/i} I am."

            y sadsmile"I've been thinking, uhm, do you guys wanna exchange phone numbers?"
            y "We can still text inside the barrier, as far as I remember, right?"

            a "Certainly."
            a "Dallan, do you mind?"
            hide wolf20
            show wolf20ec at right
            d "I'm all for it!"
            show tiger20bored at center with move
            hide cat20
            show cat20simple
            show cat20simple at left with move
            "I hand Aiden my phone and he inputs both his and Dallan's numbers."
            show cat20simple at center with move
            show tiger20bored at left with move

            d "If you ever need to reach me, you should call, don't bother texting, I don't check those, you know why, right?"
            y smug"Of course, I wouldn't bother checking my inbox either if I were you."
            "I'm nobody special and my emails are always filled, I can't even imagine what someone as important and popular as Dallan has to deal with when it comes to messages."
            hide wolf20ec
            show wolf20simple at right
            hide cat20simple
            show cat21mad2
            t "Aghem!"
            y simple"Yees?"
            t "What about me?"
            a "You don't have a phone."
            t "Correct, so now I feel left out."
            t "Thank you guys, what great friends I have."
            a "We hate you with our whole being."
            hide wolf20simple
            show wolf20ec at right
            d "I like you, Tate."
            hide cat21mad2
            show cat21blush3
            show cat21blush3 at right2 with ease
            t "And I {i}LOVE{/i} you, my big strong puppy."
            show cat21blush3 at center with ease
            "Dallan was not as weirded out by the comment as me and Aiden, in fact, he starts wagging his tail."
            hide cat21blush3
            show cat21smile1
            "I take a piece of paper from my backpack and a pen."
            "I write my number on it, drawing a little heart near it as well, and hand it to Tate."
            hide cat21smile1
            show cat21simple
            hide wolf20ec
            show wolf20 at right
            y s"Here, you might not have a phone."
            y "But if you ever really need me, you can borrow it from someone, or use a public phone, and give me a call."
            "I didn't think much about what I just did, I just wanted him to not throw a fit, even if I know he's joking most of the time."
            "But my gesture might've been a bit more powerful than I thought."
            "No, he didn't start to ugly cry, no, he didn't jump in my arms and hug me with the strength of a hundred horses, but he did show genuine surprise in his contemplating eyes, before stuffing the paper in his crop top's pocket."

            show cat21blush with dissolve
            hide cat21simple
            t "Thanks..."

            y simple"Speaking of which, why don't you have a phone?"
            un squint"Why the fuck would you ask that?!"
            un suspicious"He's fucking poor."
            un "He's adopted."
            un "He basically lives in the woods."
            un "Have you no room reading abilities?"
            un "That's it, from now on, you bring every question you want to ask these idiots by me first."
            "I admit it is a bit forward, but depending on the answer, it's not as bad as it seems."

            hide cat21blush
            show cat21bored

            t "I had people offer to buy me one."
            t "But those monstrosities are expensive as HECK!"
            t "I'd rather just send letters for a dime."
            a "We could never convince him, so you won't either, most likely."

            t "I don't like Mister and Misses Mandrate buying things for me, let alone my FRIENDS!"
            hide cat21bored
            show cat21smile
            t "I rely on the money I get from hunting Nightfallen, like a REAL hunter!"
            t "It's what everyone should do, in my humble opinion."
            y s"That's an interesting and respectable view on life."
            hide cat21smile
            show cat21simple
            d "Speaking of things to do, what are your plans for today, [name]?"
            d "We could all do something together, I heard there is a sauna that-"
            hide tiger20bored
            show tiger20confused at left
            a "Wait wait wait, {i}YOU{/i} want to hang out?"

            t "Yeah, what happened to all your work?"


            d "It turns out, not having to waste time with Tate's detention made me very productive."
            d "So now I don't have anything to do."
            hide wolf20
            show wolf20simple at right

            t "Sorry Dallan, we'd love to participate in your cliché sauna episode, I'm sure [name] would love to see you both naked and wet-"
            y blush2"N-no I wouldn't!"
            "With all my being, actually..."
            t "But me and [name] have plans."
            y simple"It's true."
            hide wolf20simple
            show wolf20sad at right
            d "Awww..."
            "I can't leave Tate alone with a wyvern, even if it's just a baby."

            hide tiger20bored
            show tiger202 at left

            a "I wouldn't be able to accompany you anyway."
            a "I have to visit my ex in the hospital, he is expecting to wake from his coma before the big test begins."

            y worried"Oh no, what happened to him?"

            a "Something, something Chelsie and her inventions."
            a "Not too sure."
            hide wolf20sad
            show wolf20bored at right
            d "I keep telling her to not injure her assistants..."
            hide wolf20bored
            show wolf20ec at right
            d "If you two are so busy, then I'll come with you, Aiden."


            hide tiger202
            show tiger20sweat at left
            a "Uhm, n-no, no need, I'll be fine on my own."
            a "I need to, uhm, cry at his bedside, or something."
            d "I'm not letting you unplug his life support..."
            hide tiger20sweat
            show tiger20bored2 at left
            a "Damn it."
            "He REALLY hates whoever that is."
            hide tiger20bored
            show tiger20bored at left
            a "Then plan's changed, we could just go drinking with Chelsie instead."
            d "That's an idea I can get behind!"
            hide wolf20ec
            show wolf20 at right
            d "The hanging out with Chelsie, I mean."
            d "I would never drink on a school day."
            t "I never drink, period."
            a "Cowards."

            "They turn to look at me, expectantly."

            menu:
                "What's my relationship with alcohol?"
                "Bring the booze in!":
                    $ Aiden_points +=1
                    y s"I can handle my drinks, even if I don't look like it."
                    "Aiden seemed to like that."
                    a "You sure are full of surprises."
                    jump afterdrinking

                "On occasion.":
                    $ Dallan_points+=1
                    y s"If the occasion calls for it, I wouldn't deny a cup or shot."
                    "Dallan seemed to like that."
                    d "Fun with responsibility, that's my [name]!"
                    jump afterdrinking

                "Hell nah.":
                    $ Tate_points+=1
                    hide cat21simple
                    show cat20smile
                    y smug"Keep any alcohol that's not inside chocolate away from me."
                    "Tate seemed to like that."
                    t "Right? Glad you feel the same!"
                    if fish >=1:
                        t "Now we just have to get rid of that fish eating thing of yours..."
                        "He glares at the plate that held the salmon bagels before..."
                        t "And you'll be perfect!"
                        jump afterdrinking
                    else:
                        jump afterdrinking

                    label afterdrinking:
                    stop music fadeout 3.0
                    scene black with dissolve
                    "With that last question, we get up from the table, letting the next party sit down."
                    "We got a couple of ugly glares from people around since we occupied a table for six even if we're only four, but a table for four would not be able to hold all the food Dallan got, so we made the right choice."
                    "We cleaned up after ourselves and got a move on, Aiden and Dallan going towards the academy waving at us goodbye."

                    scene outside2 with dissolve
                    play music "audio/jazz5.ogg" fadein 3.0


                    y s"Where to now, chief?"
                    show cat20smile with moveinright
                    t "To the library!"
                    "I almost forgot Tate had a bag of books with him."
                    y simple"You just had them floating outside this whole time?"
                    t "Yep, I can pump magic into things and people and make them float, it's not very magic consuming, so it's fine."
                    t "What's a better anti-theft mechanism than gravity?"
                    y s"I admit, it's pretty smart."

                    hide cat20smile
                    show cat20smug

                    t "Care for another broom ride?"
                    t "The library tower is not far, but we just ate."
                    y "I feel like flying is worse than walking right after you eat."
                    hide cat20smug with dissolve
                    show catfly with dissolve
                    t "Not for me!"
                    t "Legs are good only to clutch a broom and to cradle a loved one's head."
                    y sadsmile"Saying no to you is hard, so... please don't go too high."
                    y "Or too fast."
                    t "Promise."
                    scene chibitatetown with longdissolve
                    "I hop on and we take flight."
                    "As promised, Tate flies with a speed slightly faster than walking, and only high enough so the tip of our shoes don't scrape the ground."
                    "The lack of cars makes the atmosphere peaceful and quiet."
                    "Townsfolk wave at Tate and greet him as we fly by."
                    st1 "Good morning little Tate!"
                    st2 "Tate, your father's suit is ready, make sure to let him know, alright?"
                    kid1 "Mister Tate! Mister Tate!"
                    kid2 "Can we fly on your broom?"
                    t "I'm a little busy right now, let's reschedule."
                    kid2 "Who is that?"
                    kid1 "Is this your Booooyfriend~?"
                    "These kids have no filter."
                    kid1 "Look, he's getting red!"
                    kid2 "Mister, are you a chameleon?"
                    T "Hey now, don't you have cartoons to go watch, or something?"
                    kid1 "{i}*Le Gasp*{/i}"
                    kid2 "Isn't today when Barbarosa's first episode comes out?"
                    kid1 "I think it is!"
                    kid2 "THEN GO GO GO!"

                    "They run away screaming and enter a house."
                    y s"A lot of people know you around here."
                    t "I'm kind of a local celebrity, one might say."
                    y "Could it be because your father was the Headmaster?"
                    t "No!"
                    t "This is my own hard earned popularity!"
                    y ec"I'm just teasing."
                    y s"Hey, Is that the library?"
                    "A grand tower, adjacent to the academy stands tall before us."
                    t "Yep."
                    y "Wouldn't have guessed it's a library from the looks of it."
                    y "Maybe a wizard's tower."

                    t "I wish."
                    t "It has only books inside."

                    y "I take it you're not a big reader?"

                    t "I am, actually."

                    y surprised"Really?"
                    t "Why are you so surprised?"
                    t "I'm smart!"
                    t "Just because I don't wear glasses or hang around with boring nerds all day doesn't mean I'm stupid."
                    y simple"I never thought you were stupid."
                    y pf"You just seem more witty and sly than wise and intelligent."

                    t "Hmmm, yeah, I like that assumption."
                    t "You can call me, {i}Sly the Wit{/i}!"
                    y s"I will literally never call you that."
                    t "Worth a try."

                    scene library2 with longdissolve
                    stop music fadeout 3.0

                    "We walk inside, being greeted by a small corridor that opens up in the actual library."
                    y surprised"I was expecting this to have multiple floors, not a spiral straight to heaven."
                    y "I can barely see the roof!"
                    show cat20simple with moveinright
                    play music "audio/catjazz.ogg"
                    t "Unfortunately the librarian usually doesn't let first years climb the stairs too much, in case they're dumb and fall."
                    y simple"Not even you?"
                    t "Nope."
                    y "But you can literally fly, float and teleport."
                    t "That's what I'm saying!"
                    t "But Mister Sebil was always worried..."

                    t "Let's get this over with, I don't want to talk to this old witch more than I have too."
                    y "Is she an actual witch or are you insulting her?"
                    t "Just an insult, she can be a big pain sometimes..."

                    "I hate mean people."
                    "I never understood why some people have to be such assholes to complete strangers."
                    "I'll get ready for the worst..."
                    hide cat20simple
                    show cat20tired

                    t "Damn it, my books are kinda filthy, hopefully she won't notice..."

                    "We walk up to the librarian's grand table, surrounded by papers, stacked books waiting to be placed on their shelves, a computer and a ton of drawers."
                    "Somebody was making a bit of a ruckus behind the counter. We approach and Tate rings the bell very lightly."
                    "The sounds stop."
                    hide cat20tired
                    show cat20simple
                    st "Visitors!"
                    st "One sec."
                    st "{b}Get- in- there{/b}, {i}phew{/i}, okay."
                    t "That doesn't sound like..."

                    show cat20simple at left2 with ease
                    show bean at right2 with moveinright

                    "Instead of an old witch, we're met with a short, red panda with a questionable fashion sense just like a certain cat I know, but in the exact opposite direction sexually."
                    un "The first person in this goddamn place not completely sexually charged when it comes to clothing."

                    "We read his name tag he keeps backwards on the desk."
                    ".neaB"
                    "..."
                    "Bean."
                    "Huh."

                    b "Hi."
                    b "Welcome to.. the library."
                    b "How can I help you?"

                    t "Yeah... hi."
                    t "Where's the witch?"

                    hide bean
                    show beansquint at right2

                    b "The what?"

                    hide cat20simple
                    show cat21bored at left2

                    t "The ugly woman with a giant snout, perfect to get in everyone's business."

                    hide beansquint
                    show beansimple3 at right2

                    b "You mean my aunt?"
                    b "That sounds like her."

                    b "She's unavailable."
                    b "I'm taking her place for the time being."

                    y simple"What happened to her?"
                    hide beansimple3
                    show beantalk at right2

                    b "Oh hi, welcome to the library, how can I help you?"
                    hide cat21bored
                    show cat20simple at left2
                    y pf"I... I was here from the beginning, hi."


                    hide beantalk
                    show beandisapointed at right2

                    b "You were?"
                    hide beandisapointed
                    show beansimple3 at right2
                    b "I was a bit distracted by your friend's six pack."
                    b "How'd you get these gains my dude?"

                    t "Digging holes mostly."

                    b "Siiiiick."

                    t "So really, what happened to her?"

                    b "To whom?"
                    t "Your aunt."

                    b "How do you know my aunt?"

                    y "You just mentioned her."
                    hide beansimple3
                    show beantalk at right2

                    b "Oh, hi, welcome to the li-"

                    y angry"{b}I was here from the beginning!{/b}" with hpunch

                    t "Chill out [name]."
                    hide cat20simple
                    show cat20smile at left2
                    t "He's just a little guy."
                    t "It's probably his first job."
                    hide cat20smile
                    show cat20ec at left2
                    show cat20ec at center with ease
                    t "Isn't that right, little Beannie?"

                    b "I'm thirty two."
                    hide cat20ec
                    show cat21simple at center
                    show cat21simple at left2 with move

                    t "Oh."
                    t "Never me mind."

                    hide beansimple3
                    show beanhappy at right2

                    b "Haha, I'm just kidding, nobody is thirty two."
                    b "You can't live that long, it's insane."
                    hide beanhappy
                    show beansimple3 at right2
                    b "I'm twenty four."

                    hide cat21simple
                    show cat21bored at left2


                    t "You're weird, Bean."
                    b "Thanks."
                    b "I moisturize."
                    hide cat21bored
                    show cat21simple at left2
                    t "What?"

                    y bored"Can we please do what we came here to do?"

                    hide beansimple3
                    show beantalk at right2

                    b "Oh hi, welco-"

                    y angry"I'M NOT NEW YOU FUCKI-"
                    hide cat21simple with hpunch
                    "Tate has to hold me back with both arms as I try to jump the counter."
                    "Bean has no reaction, he just smiles as always."
                    "Damn, he really is stronger than he looks."
                    "If Tate decides to pin me down, I don't have a chance of getting free unless I use some strength enchantments."
                    show cat21simple at left2 with moveinleft


                    b "Riiight, sorry dude, I was once again hypnotized by his abs."

                    hide cat21simple
                    show cat20smile at left2

                    t "You wanna touch them?"
                    hide beantalk

                    show beantalk2 at right2

                    show beantalk2 at center with ease

                    b "Hell yeah dude."

                    "Jealousy envelops me as I see Bean reach over and start caressing Tate's belly, feeling every muscle and sticking his finger tips through every dimple in there."

                    b "Damn."
                    b "I should hit the gym, or start digging holes."
                    t "Yeah, you could have this too."
                    b "Do you have any tips?"

                    t "Never eat fish."

                    b "Got it."
                    b "What about lobster?"

                    t "That's also a fish."

                    hide beantalk2
                    show beansquint at center

                    b "No it's not, it's like a sea spider."

                    t "I'm pretty sure those are still fish."

                    b "I don't know, I've never seen a fish with that many legs."

                    t "Hey, [name], are lobsters fish?"

                    y bored"I'm going to kill both of you."

                    t "We don't have time for your dark humor."

                    y asleep"{i}*Inhale*{/i}"
                    y asleep"{i}*Exhale*{/i}"
                    y bored"They're crustaceans."
                    hide beansquint
                    show beantalk2

                    b "Sweet, I was right."

                    y "No, you said spider, that's an arachnid."

                    b "Who are you again?"

                    y pf"{size=20}A third wheel apparently.{/size}"

                    y angry"And would you PLEASE stop feeling my partner up?"
                    hide beantalk2
                    show beantalk
                    show beantalk at right2 with ease

                    b "Oh, sorry, didn't know he was your boyfriend."

                    hide cat20smile
                    show cat20simple at left2

                    y blush2"H-he's not..."

                    b "Then why did you make that face when I touched him?"

                    y blushmad"WE CAME HERE TO RETURN SOME BOOKS PLEASE!"

                    hide beantalk
                    show beansad at right2

                    b "Why?"
                    hide cat20simple
                    show cat21bored at left2

                    t "People take books then they bring them back."
                    y bored"That's how a library works."

                    hide beansad
                    show beansquint at right2


                    b "Ooooohh, I thought people were just stealing them, so I got some anti theft precautions."
                    hide beansquint with moveoutright
                    show beansquint at right2
                    show gun at right2 zorder 2
                    with moveinright
                    hide cat21bored
                    show cat21simple at left2
                    play sound "audio/scratch.ogg"
                    "He takes out a shotgun from under the counter."
                    t "What the fuck?"
                    y angry"YOU'RE NOT ALLOWED WITH FIREARMS INSIDE LAKONIA!"

                    hide beansquint
                    show beantalk at right2 zorder 1

                    b "Chillax dude, it's got taser bullets."
                    b "I was just reloading it when you came in."

                    y pf"You were gonna shoot us?"

                    b "Only if you stole books without paying."

                    y angry"YOU DON'T HAVE TO PAY AT A LIBRARY!"

                    b "Well I know that now."

                    t "Where did you get that thing?"
                    hide gun with moveoutright

                    b "A raccoon girl with huge boobs, and I mean MASSIVE honkers came by, and offered it for free if she could test it on me."

                    t "Did it hurt?"
                    hide beantalk
                    show beansimple3 at right2

                    b "Oh I passed out from the pain."
                    b "But it was worth it."
                    b "She woke me up with a slap."

                    y simple"Why did you take this job if you know nothing about libraries?"

                    b "Mostly to meet women, I heard there are a lot of cool, half naked women here."
                    hide cat21simple
                    show cat20smug at left2

                    t "What about half naked men?"

                    b "Gross."
                    hide cat20smug
                    show cat20sad2 at left2

                    t "Wha-"
                    t "But I-"
                    t "I thought you were sexually attracted to me."

                    b "Ah, nah dude, you're cute for a guy but not enough to catch me slippin'."

                    y pf"So you were flirting with him on purpose?"
                    hide cat20sad2
                    show cat21smug at left2
                    t "Perhaps?"
                    t "More like teasing."
                    t "Well now that I know you're not really into it, I want you so much more!"
                    show cat21smug at center with move
                    t "How about a quick kiss?"
                    show beansimple3 at right with move

                    b "No thanks."

                    show cat20smug
                    hide cat21smug
                    show cat20smug at right2 with move

                    show beansimple3 at left2 with ease

                    t "Just a little one?"

                    show cat20smug at left2 with move

                    show beansimple3 at left5 with ease

                    b "I'd rather not."

                    show cat20smug at left5 with move

                    show beansimple3 at left4 with ease

                    t "A little hug?"

                    show cat20smug at left4 with move

                    show beansimple3 at right2 with ease

                    b "You're gonna rub your dick on me."
                    t "You're gonna like it."

                    show cat20smug at center with move

                    b "Please stop."

                    y angry"Tate!"

                    y "Stop sexually harassing the librarian!"
                    show cat20smug at left2 with ease

                    t "Fine, let's get down to business."
                    hide cat20smug
                    show cat21smile1 at left2

                    b "I said no, dude."

                    y "He means returning the books."

                    b "Oh, ok, let's see them."

                    "Tate hands over all the books on different animals, five in total."

                    b "They're a little filthy."

                    hide cat21smile1
                    show cat21simple at left2

                    t "That's how I got them."

                    b "Uhm, I'm not sure I trust you dude."
                    b "You did say you like to dig holes, so it makes sense you'd dirty the books."
                    hide cat21simple
                    show cat21bored at left2
                    t "Oh, so NOW you're a genius investigator, huh?"
                    b "I'll believe if your friend says this is how you got them."
                    hide cat21bored
                    show cat21simple at left2
                    t "Say yes."
                    t "[name], say yes."
                    b "Yeah, you could just say yes, I'd believe you, I need confirmation, not proof."

                    menu:
                        "Is this how he got them?"
                        "Yes. (Lie)":
                            $Tate_points+=1
                            hide cat21simple
                            show cat21smile1 at left2
                            y s"Yes, that's how he got them."
                            y "It's true."
                            y smug"Even if we met yesterday and the books are weeks old."
                            y "But yes."

                            "Tate gives me a side eye, but keeps quiet and smiles on."
                            b "Ok."
                            b "I mean, I really only needed the word 'yes' here, you didn't need to be so condescending."
                            t "Yes, [name], you didn't have to say it like that."
                            "He says through gritted teeth."
                            jump books

                        "No. (Truth)":
                            $Tate_points+=-1
                            hide cat21simple
                            show cat21mad2 at left2
                            y simple"Sorry, I'm not sure."
                            y "I only got here yesterday."
                            t "Why yo-"
                            b "Oh."
                            b "I didn't expect that."
                            b "You really just had to say yes and it would've been fine."
                            b "Uhm."
                            b "I guess I'll accept them for now."
                            "He hits me with a side-eye for almost ruining his plans."
                            "I can't help it!"
                            "I had to be honest!"
                            jump books


                        "Yes. (Truth)":
                            $Tate_points+=1
                            hide cat21simple
                            show cat21smile1 at left2
                            y ec"Yes, that is absolutely how he got them."
                            b "Ok man, I believe you."
                            y "In fact, I can show you some pictures on my phone when he got the books, they were dirty then too, they're totally not from the internet."
                            b "You don't need to, I don't care."
                            y "Then I can tell you exactly what he did that day until and after he got to the library."
                            y "You'll see how the dates match, and with the corresponding weather from that day we can-"
                            show beansimple3 at left2 with move
                            show beansimple3 at right2 with move
                            b "Oh hey, look at that, the books are in my hands and accepted, you can shut up now."
                            t "Yes, [name], I appreciate it but it would be best you stopped."
                            y "Glad to be of help!"
                            jump books

                        "No. (Lie)":
                            $Tate_points+=-2
                            $ betray +=1
                            hide cat21simple
                            show cat21bored at left2
                            y bored"No, that's certainly not how he got them."
                            b "Oh, ok."
                            t "[name]! You weren't even-"
                            y "And you were right about the holes comment, that is most likely how he got them dirty."
                            hide cat21bored
                            show cat21mad2 at left2
                            b "Got it."
                            y "Besides, they were laying on the ground of his tent for weeks, in humid weather."
                            t "Why are you sabotaging me?!"
                            y "So I'd make sure to charge him for the repairs if I were you."
                            hide cat21mad2
                            show cat21mad at left2
                            "Tate has his mouth wide open and is left speechless."
                            b "Wow, I didn't expect that."
                            b "I don't even know how to do that last part so I'll just pretend you said yes."
                            b "So I don't have to work too much."
                            "This interaction ended with Tate giving me a BOMBASTIC side eye, as Bean takes the books from his hands."
                            jump books




                    label books:
                        scene library2
                        show beansimple3 at right2
                        show cat21smile1 at left2
                        b "I think you have to sign here now."

                        t "Oki."

                        y simple"..."
                        y pf"Why'd you sign as {i}'Memento Mori'{/i}?"

                        t "So the witch can't trace it back to me."
                        t "Duh."
                        t "Plus, it's a cool name."

                        b "Can I do anything else for you?"

                        t "Do you have any books on dragons?"

                        b "Yeah, in the children's section."
                        b "The last floor."
                        hide cat21smile1
                        show cat21simple at left2
                        t "Uhm, I meant more like, actual books, like historic, or encyclopedias?"
                        b "I'm not sure what those words mean, but I think you can find something different about dragons on the third floor."
                        y "Actually, we need some on wyverns."
                        hide cat21simple
                        show cat21mad2 at left2

                        t "He's not a fucking wyvern."

                        b "Yeah, I'm a red panda, I thought that was pretty clear."
                        b "Boy, and you were mad I didn't notice you standing all the way over there."

                        y bored"Let's get one or two books, just in case."
                        hide cat21mad2
                        show cat21bored at left2
                        t "...fine."
                        t "Where can we find books on wyverns?"

                        b "I think those are on the second from the last floor, something like that."


                        b "As long as you're not first years, you are free to go there."

                        y simple"Oh, well, we-"

                        hide cat21bored
                        show cat20ec at left2

                        t "Yep, not first years, we're seniors."
                        t "See ya in a bit, Bean."
                        hide cat20ec with moveoutright

                        b "Awesome."
                        hide beansimple3
                        show beansquint at right2
                        b "..."
                        show beansquint at center with ease
                        b "Seniors..."
                        b "They look way younger than my grandma."
                        b "I should moisturize even more to catch up."

                        scene library1 with fade

                        "We climb up the stairs, and oh man, there are a lot of stairs, all going in a spiral straight up."
                        "Knowing that dragon books were on 'the third floor' was not very helpful, since there are thousands upon thousands of books on this floor alone!"
                        "Luckily there are a lot of signs guiding towards different parts of the floor, and we manage to find the 'mythical creatures' and 'Nightfallen' categories in a matter of minutes."
                        "Our luck ends when we find exactly zero real books on dragons."
                        "There are fairy tales, and folklore written books and some fantasy novels about dragons, but no information books."
                        y simple"I don't think these will be too useful."
                        t "It's worth a try, I'll get one of each."
                        t "Maybe they'll have SOME truth to them."
                        t "Man, I thought dragons were pretty common knowledge since they existed at some point, where are all the books!?"
                        y pf"Maybe it's just this particular library that doesn't have them, maybe it's dragon-racist."
                        t "Nonsense, it's the biggest library in the country..."
                        t "We should go, I want to visit my baby, he must be awake by now."
                        y bored"Hold on, we're getting that wyvern book, at least."

                        t "Ughhh!"
                        t "Alriiiight, but turn the trip there and the search into a short narration."
                        "I decide to abide by Tate's rules, we walk up a loooot more stairs until we reach one of the top floors."
                        "This time, the books we were looking for were easy to find, since wyverns actually exist..."
                        scene library2 with fade
                        show beansimple3 at right2
                        "Then we make our way down to deal with Bean again."

                        show cat20 at left2 with moveinleft

                        t "We got everything, sign these up in my name."

                        b "Ok, little dude."
                        hide cat20
                        show cat20bored1 at left2
                        t "You're the little one..."

                        y "Are we free to go now?"
                        b "You were always free to go."
                        hide cat20bored1
                        show cat20smile at left2
                        t "Thanks, Bean!"

                        t "Byeee, see you later!"
                        hide cat20smile with moveoutleft
                        b "Good day."
                        y "Hope your aunt gets better."
                        b "Haha, oh she has no chance."
                        scene black with dissolve

                        "What?"

                        b "I'll be waiting for those books back!"

                        scene outside2 with dissolve


                        "As soon as we get outside Tate starts a celebratory dance."
                        show cat20ec with moveinleft
                        t "I can't believe that wretched witch is no more!"

                        t "Now I can come to the library more often!"

                        y pf"I'm not sure {i}'Bean'{/i} is such a good replacement."

                        hide cat20ec
                        show cat20

                        t "Are you kidding me?"
                        t "He's perfect!"
                        t "He doesn't even care if I dirty the books!"

                        t "Take my hand."
                        t "I'll teleport us back to my tent."
                        y "Are you sure you want to waste the energy?"
                        t "Yes! We need to hurry!"
                        stop music fadeout 2.0
                        play sound "audio/teleport.ogg"
                        scene teleport

                        "I touch the excited cat's hand and a bright light instantly covers my eyes. The next moment, the green forest was under my feet and all around us."
                        scene tent2 with dissolve
                        play music "audio/littlehappy2.ogg"

                        "Tate hurries to the cub's burrow, and finds it still sleeping away in the deep end."
                        show cat20worried with moveinright
                        t "He's still asleep."
                        t "He's not sick, is he?"
                        hide cat20worried
                        show cat20
                        y s"That's why we have information books, to find out."
                        t "Check the fantasy one about dragons!"

                        y pf"Yeahhh, that one, one second."
                        "I place the book about wyverns inside the dragon one and start looking through the pages."

                        y simple"It says here that wyv- I mean, dragons sleep for twenty hours a day the first month of their hatching, decreasing over time, usually on high alert for predators, unleashing sharp claws and fangs upon whoever is unfortunate enough to wake one up, even a parent or sibling."
                        y "In other words, don't touch it until it wakes up on its own."

                        hide cat20
                        show cat20ec

                        t "That's great actually!"
                        t "This way we have time to set traps!"

                        y confused"Traps?"

                        t "Yes, like the one you fell into!"

                        y bored"I'm not digging holes."
                        hide cat20ec
                        show cat21smug

                        t "Not every trap is a hole, [name]..."
                        t "We can put up magic traps, rope traps, explosive traps."
                        t "All sorts of things."

                        y simple"And what if a wild animal gets caught?"
                        t "We just release it."

                        y "Wouldn't it be a good idea to feed it to the baby?"

                        hide cat21smug
                        show cat21bored

                        t "Are YOU going to butcher wild animals?"
                        t "Cuz I sure won't."
                        t "And I'm not watching my baby rip an animal to shreds."

                        y "Good point, but where are we going to get the meat for it?"

                        hide cat21bored
                        show cat21smile

                        t "We trap Nightfallen, kill them, exchange the crystals they drop for money, then buy meat."
                        t "We are Nightfallen hunters, after all."
                        hide cat21smile
                        show cat21mad2
                        t "And stop calling him {i}'it'{/i}."
                        y "Sorry."
                        scene tent with dissolve
                        "I follow Tate inside the tent and he hands me different equipment, including rope, a shovel, dirt anchors and... men's perfume?"
                        y simple"Why the perfume?"
                        t "A lot of Nightfallen like the scent of people, so they associate different unnatural perfumes with people, since you can't find these in nature without a person around."

                        y "I didn't know that, you really are pretty experienced for someone so young."
                        t "Experienced in many ways."
                        "He winks."
                        scene tent2 with dissolve
                        "We walk out of the clearing, and the first trap he places is right in front of the vine entrance."
                        "A magic trap that does no damage but alerts the person that sets it up whenever someone passes."
                        y "Did you buy these at the store?"
                        t "Nah, Chelsie made them."
                        t "At my request."
                        y "Chelsie seems like such a big help, I'd love to spend time with her in the future and get to know her."
                        t "She's Dallan's best friend, a little nuts at times, but you'd love her."
                        t "There, all done."
                        t "Let's place the rest around the hideout."
                        "I don't know much about traps, so I mostly do what he tells me."
                        scene forest3 with dissolve
                        "Most of the time I need to use strength enchantments to actually be able to do what he needs me to do."
                        "Setting traps is hard work..."
                        "Hey, Scribbles, you there?"

                        un "Hmm?"
                        un "Yeah, what's up?"

                        "You've been quiet for some time, everything alright?"

                        un bored"Yeah, I just didn't feel like talking much."
                        un sidee "I had some stuff on my mind."
                        un bored"Plus, I'm watching some of this {i}'tee vee'{/i} in your head."
                        un eyeroll"Since CLEARLY you don't have time to pay attention to my comments, because of all your cool new friends and hot twink cat."

                        "Ah, so that's it."
                        "You're jealous."

                        un suspicious"What?"
                        un "What is there to be jealous about?"
                        un sidee"YOU?"
                        un tease"HAHA!"


                        "It must pain you that you don't have friends like I do, considering you think I'm so much more inferior to you."

                        un simple"Ah... jealous of that, huh?"
                        un bored"Uhm, yeah, sure, I'm jealous."
                        "I'm sure whenever you get a new body, and don't have to put up with me anymore, you'll go and make a lot of wonderful friends."

                        un sidee"Yes... when I go..."
                        un "And never see your... your ugly ass again..."

                        "Ouch, rude."
                        "Fine, go back to your {i}'Tee Vee'{/i}."
                        un sidee"..."
                        scene forestt with dissolve

                        "I've made it clear I'm not going to start digging, so I cheer Tate from the sidelines as he does, because he just can't help himself, and needs to make at least one pitfall trap."
                        "When it comes to our tree net traps... let's just say things are going to take a bit of a turn."

                        show cat20smile with moveinright

                        t "Here we go, I'm going to climb that tree and you'll throw me the rope."
                        y simple"Can't I just throw the rope over that branch so you don't have to climb?"
                        t "No, I need to fixate it with a pulley for extra friction and power."
                        y "Can't you just fly there if-"
                        hide cat20smile
                        show cat21mad2 with hpunch
                        t "I WANT TO CLIMB A TREE! OK?!"
                        y simple"..."
                        y smug"You're cute when you're angry."
                        hide cat21mad2
                        show cat21blush3
                        t "You're cute when you're a dumbass..."
                        hide cat21blush3
                        show cat21smile1
                        t "Come on, hoist me to the nearest branch."
                        hide cat21smile1 with moveoutright
                        "I squat down and let him place his foot on my intertwined hands, and with some force, I get him high enough to reach the lowest branch."
                        "I am a mature man so I will not make any comments about his crotch practically rubbing against my snout, no sir."
                        show bush1 with dissolve

                        "He gets in the tree."
                        "I would explain what he does there, but as I said before, I know nothing about this sort of thing."
                        "He, uhm, nails the pulley there, throws the rope around it, then uses some thingies to test it? No, to fix it in place better."

                        show bush with dissolve
                        hide bush1
                        y simple"Hey, Tate?"
                        t "Yeah?"
                        y "The bushes and leaves are rustling."
                        t "No shit, we're in a forest."
                        y worried"They're louder than usual!"
                        t "Probably squirrels, it's Fall, so they're more lively."


                        t "Hey!"
                        t "Try to pull the rope a little bit!"

                        y "Is this good?"

                        t "Yeah, it's perfect, I'm coming down now!"
                        y "Careful."

                        t "It's not the first time I've climbed a tree."

                        t "I know how to-"
                        show cat21bow with moveintop
                        hide cat21bow
                        show bush with vpunch
                        t "Wo-wWHhoOAA!"
                        stop music fadeout 2.0

                        y smug"Told you..."
                        "He tried to show off after my comment, jumping from where he was to the lowest branch, but the bark was too slippery for his shoes, so he slipped and fell in the bushes that surround the tree."

                        y "Lucky for those bushes."
                        y "Fell hard enough to learn a lesson but not hard enough to injure yourself."

                        y "I suppose I should help you up, even if you kind of-"
                        y simple"Huh?"
                        play music "audio/beachfight.ogg" volume 0.3
                        "I try to take a step towards Tate, but I'm stopped."
                        "Thick vines suddenly tighten around my leg, quickly wrapping up to my torso and incapacitating my hands."
                        y worried"What the-"
                        y "Uhmm."
                        y "Tate?"
                        y "Not to underline my own problems over yours, but I think I'm in trouble."
                        stop music

                        t "I'm pretty sure my peril is still greater."
                        scene plant1 with longdissolve
                        scene CGcc4


                        "The bushes start to move out of the way, as Tate's body is getting raised up, held by the same vines holding me, except that his were smaller and looked softer, compared to my thick, with an almost wooden like density."

                        y worried"D-don't tell me, this is a..."

                        t "Nightfallen?"
                        t "Yep."

                        t "The plant kind, but that was probably pretty obvious."
                        t "My damn shoes fell as well."
                        t "Kids, don't climb trees in school provided shoes...they buy you a size too big as always."

                        y worried"You're pretty calm for someone suspended in the air by one of these plants."

                        t "I'm assessing my situation."
                        t "I can always teleport away, but I don't really want to use my energy like that."

                        y "How did we not see it coming?"

                        t "Because it didn't {i}'come'{/i} from anywhere."
                        t "It was probably dormant right here, under this tree."

                        t "I already hunted most of the Nightfallen around this part, but I missed this guy."


                        "The plant seems to be somewhat intelligent, or at least more intelligent than I'd give a plant credit for."
                        "It uses its tentacle-like vines to spread Tate's legs, and some more spawn up towards his mouth and other orifices."
                        y blush2"Uhmmm."
                        t "Yeah, this guy doesn't waste any time, it's probably really hungry for lust after sleeping for so long."
                        t "I don't feel like having an audience for this, so I'll just get away."
                        y "Probably for the best."
                        pl "..."
                        t "..."
                        y simple"..."
                        un "..."
                        y bored"You're still there."
                        t "..."
                        scene plant2 with dissolve
                        t "It canceled my teleportation..."
                        y scared4"WHAT?!"
                        y angry"WHY DID YOU LET IT DO THAT?!"



                        t "I DIDN'T LET IT DO ANYTHING!"
                        t "IT'S NOT MY FAULT EVERYBODY AND THEIR MOTHER KNOWS HOW TO CANCEL TELEPORTATION SPELLS NOWADAYS!"
                        y "IT'S PROBABLY BECAUSE IT'S SUCH A GOOD SPELL PEOPLE AND NIGHTFALLEN NEEDED TO EVOLVE WAYS TO COUNTER IT!"
                        t "I DON'T NEED YOUR LOGIC RIGHT NOW, DO SOMETHING!"

                        "The Nightfallen slows down hearing our argument, it seems to enjoy Tate's struggles which are in vain, his limbs barely moving against the plant's tight grip."
                        "Scribbles, are these things smart?"
                        "Is it teasing Tate's inability to escape?"
                        un "I wouldn't say {i}'smart'{/i}, but it probably realized he's defenseless, since why else would its prey struggle so much?"
                        un "Nightfallen like foreplay as well."

                        scene plant3 with dissolve
                        scene CGcc5

                        "The Nightfallen rubs Tate's behind, grinding the vine where his hole would be underneath the clothes."
                        t "WAIT WAIT WAIT!"
                        t "Mister plant please, can you at least turn me around so my friend doesn't have to see this?"
                        show planthead at right with moveintop
                        "The plant's head blooms from the ground, standing above Tate, shaking its corolla at him."
                        y worried"I think it wants me to watch."

                        t "Stupid pervert plant!"
                        t "Screw you and your voyeurism kink!"

                        y blushmad"Don't kink shame it, you'll make it mad!"

                        t "Oh shut up, I'm about to be used for Lust!"
                        t "Do something!"

                        if spell >=1:
                            "Scribbles, do something!"
                            un curious"Me?"
                            un "You have the spell I taught you, did you forget already?"
                            "Oh, right!"
                            "Turns out we weren't in any danger after all."
                            play sound "audio/cancel.ogg"
                            "I follow the instructions Scribbles taught me yesterday, and snap my fingers."
                            "This should do it."
                            menu:
                                "Should I tell him the good news right now?"
                                "Let Tate know.":
                                    $ Tate_points +=1
                                    y s"Tate! It's fine, you can teleport out!"
                                    y ec"Your spells work again!"
                                    play sound "audio/teleport.ogg"
                                    scene teleport
                                    "Tate doesn't waste much time thinking this over, even if my wording was a bit weird, it was worth it for him to try."
                                    scene forestt with dissolve
                                    show cat20ec
                                    "The next second he's right beside me."
                                    t "Nice!"
                                    t "Thanks, [name]."
                                    t "That was a close one, almost saw my ass back there, haha."
                                    y "Haha, yeah, deeeeffinitely wouldn't want that."
                                    t "Let's get you out too."
                                    play sound "audio/teleport.ogg"
                                    scene teleport
                                    "He touches me and takes me out of the wooden vines."
                                    jump afterplant


                                "Wait a minute...":
                                    $ betray +=1
                                    un suspicious"What are you waiting for?"
                                    un "He has to know the spell was used, or he won't try to teleport out."
                                    "I know... I just..."
                                    un bored"{i}*sigh*{/i}"
                                    un "You wanna see him naked first, don't you?"
                                    "...perhaps."
                                    un "Why did I expect any less?"

                                    "I do not have to wait too long, as the plant slowly slides Tate's pants down."
                                    "His round cheeks covering just enough from this angle that nothing explicit is actually visible."
                                    t "AAAH, IT KNOWS ABOUT THE CONCEPT OF CLOTHING!"
                                    t "HURRY UP!"
                                    y blush2"C-coming!"
                                    t "TO HELP OR IN YOUR PANTS?! BECAUSE I AIN'T FEELING MY CLOTHES BEING PUSHED BACK UP!"
                                    scene plant4 with dissolve
                                    scene CGcc6
                                    show planthead with dissolve
                                    "With a final pull, and what looks like a big grin on the plant's supposed face, Tate's pants are down to his knees, and his face goes red."
                                    "It shows me just enough to mock me..."
                                    y pf"Teasing bastard..."



                                    t "WHAT?!"
                                    t "YOU WANT TO SEE MY ASS?"
                                    t "IF YOU'RE SO DESPERATE I CAN SHOW YOU LATER, JUST GET ME OUT OF HERE ALREADY."

                                    y simpleblush"You will?"

                                    t "NOT AT THIS POINT!"
                                    "Well, there wasn't much reward in my action, so I guess I'll just end this."
                                    play sound "audio/cancel.ogg"
                                    y surprised"Hey, Tate, try teleporting out!"
                                    t "YOU THINK IF I COULD I WOUL-"
                                    play sound "audio/teleport.ogg"
                                    scene teleport
                                    scene forestt with longdissolve
                                    show cat21simple
                                    "The teleportation works and he appears next to me."

                                    t "oh."
                                    hide cat21simple
                                    show cat21smile1
                                    t "Nice!"
                                    t "What did you do?"

                                    y s"I have a a little trick up my sleeve."
                                    hide cat21smile1
                                    show cat21mad2

                                    t "Well what took you so long to use it?"
                                    t "That plant was ready to penetrate me!"
                                    y awkward"Uhmm- I didn't know exactly how to use said trick?"

                                    hide cat21mad2
                                    show cat21bored

                                    t "Very convenient for you...."
                                    t "At least you figured it out EVENTUALLY, still, you owe me an ass show for this."
                                    y smug"I can't say I would mind."
                                    y "Mind giving me a hand too?"
                                    hide cat21bored
                                    show cat21smug
                                    play sound "audio/teleport.ogg"
                                    scene teleport
                                    "He gets me out of the hardened vines with an eye roll and a smirk."
                                    jump afterplant



                        else:


                            menu plana:

                                "What can I do to help? If I make too many bad choices, it might end up badly..."

                                "Try to get out of the plant's grip.":
                                    "If I even want to get to his heart, I want to deserve it, I want to protect him on my own."
                                    "I might be covered in wooden vines, but these won't stop me!"
                                    "I pump magic strength enchantments on myself and try to free my hands first, then my legs."
                                    "Fun fact, wood is MUCH stronger than one might think, so my efforts are doing literally nothing."
                                    un tease"Haha, weak bitch."
                                    scene plant4 with dissolve
                                    scene CGcc6
                                    show planthead with dissolve
                                    t "AAH, HELP! THIS THING KNOWS ABOUT THE CONCEPT OF CLOTHING!"
                                    "I've wasted time with my failed attempt, but this isn't a turn based RPG, so the plant doesn't wait for me to finish."
                                    "As my eyes assess the situation, they're met with Tate's {i}'pantless'{/i} and {i}'underwearless'{/i} ass."
                                    "Thankfully, for now, the only one bleeding in here is my nose, so let's try something else."
                                    "If I don't get Tate free soon, I doubt he'll be too happy with me..."

                                    jump planb




                                "Ask Scribbles for help.":
                                    "Scribbles!"
                                    "I doubt I'll be able to get out on my own, please help him!"
                                    un bored"You can manipulate energy, it should be a breeze for you to get out of this situation."
                                    "Well I don't know how!"
                                    "Let us argue later, we don't have much time!"
                                    un eyeroll"Fiiiine, what do you want me to do?"
                                    "Anything!"
                                    un curious"I can't just do {i}'anything'{/i}, how would you explain if the plant caught fire?"
                                    un "You don't have fire powers."
                                    scene plant4 with dissolve
                                    scene CGcc6
                                    t "AAH, HELP! THIS THING KNOWS ABOUT THE CONCEPT OF CLOTHING!"

                                    "As my eyes assess the situation, they're met with Tate's {i}'pantless'{/i} and {i}'underwearless'{/i} ass."
                                    "Thankfully the only one bleeding in here is my nose, so far."
                                    "If I don't get Tate free soon, I doubt he'll be too happy with me..."

                                    menu:
                                        "I need to give Scribbles specific instructions..."

                                        "Use electric powers to shock the plant.":
                                            "Can you shock its roots so it lets go of Tate?"
                                            un simple"Ah, now that's something I can do."
                                            un "It will be easy to explain with your energy manipulation powers."
                                            un "Let's see how effective this is."

                                            "Tate remains somewhat calm, as the plant begins planning what to do with him next."
                                            "Before anything happens, I feel my feet letting off a powerful magic current, which travels through the ground."
                                            "It first hits the wooden vines restraining me, getting them loose, then arriving at the plant's roots."
                                            scene plant4 with hpunch
                                            scene CGcc6
                                            "It screeches in pain and starts shaking."
                                            "The shock was not enough to affect Tate, but enough to burn some roots."
                                            scene forestt with hpunch
                                            "The tentacle vines start to retract, giving the cat his mouth back and letting go of his limbs."
                                            "He pulls his pants back up and runs to me."
                                            show cat20tired with moveinright
                                            t "Finally."
                                            t "You could've hurried, but I'm thankful you managed in the end."
                                            y awkward"Sorry about that. I was... taken by surprise."
                                            hide cat20tired
                                            show cat21smug
                                            t "Can't blame you too much, I'd be paralyzed too if I saw this gift unwrapping in my face."
                                            "He slaps his own ass."
                                            y "Haha... yeah..."
                                            "He directs his attention back to the plant, the electricity was not enough to kill it, but it can't move much anymore."

                                            jump afterplant


                                        "Cut all the vines off with wind blades.":
                                            "Can you use some kind of wind blades?"
                                            un curious"Yes?"
                                            "Then cut all the vine-tentacles things off!"
                                            un ang"Are you fucking dumb?"
                                            un "You don't have wind powers or telekenisis!"
                                            un "We need something that even your useless ass could lie about!"
                                            "We managed to waste more time, so the plant makes its next move."
                                            show planthead with moveinleft
                                            t "Uhm, mister plant, is there a way to convince you I'm not as hot as you might think?"
                                            "It shakes its head."
                                            t "Fair, everyone wants a piece of this ass."

                                            t "WHY WAS I BLESSED WITH ALL THIS SEXYN- agh."
                                            scene plant5 with dissolve
                                            scene CGcc7
                                            y blush2"!"
                                            "The Nightfallen took advantage of Tate's shouts to stick its tentacle down his throat."
                                            "Using thrusting movements to mimic a blowjob."

                                            y "Don't bite down, you'll choke!"
                                            t "mmg hHhhHmmM..."
                                            "I can feel the attitude even without words."

                                            "Somehow I'm making all the wrong choices here..."
                                            "Scribbles, can you try shocking its roots to make the tentacles loosen up?"

                                            un simple"Ah, finally, a good plan."
                                            un "This way, electricity can be explained with your-"
                                            "DO IT ALREADY AND SHUT UP!"
                                            un sidee"Gee, don't need to get angsty with me."
                                            un eyeroll"Your boyfriend is going to get fucked by a plant as a worse case scenario, it ain't that deep."
                                            scene plant6 with dissolve
                                            scene CGcc8
                                            "A second tentacle forces its way inside his mouth, filling up his throat."
                                            "Not my boyfriend, yet."
                                            un simple"Oh really? Tell me more."
                                            un sidee"What intentions do you have with the cat for the future?"
                                            un simple"Marriage, sex pal?"
                                            "W-well, I'm kind of hopping...you know, maybe not {b}that{/b} far ahead, but possibly..."
                                            "I-I mean, if everything is-"
                                            "Wait."
                                            "YOU'RE TRYING TO DISTRACT ME SO THE NIGHTFALLEN GOES FURTHER!"
                                            scene plant7 with dissolve
                                            scene CGcc9
                                            t "H-hGMmMGhhHH!!!"




                                            "Now the plant spawns a cock out of its flower, covering the poor cat's butt, which is a sentence I never thought I'd say."
                                            "Tate's panic expression was a good hint that he's not looking too forward to having it shoved inside him."
                                            un pride"Whaaaaat?~"
                                            un "No waaay, I would never~"
                                            "Shut up and do what I told you to do, NOW!"
                                            un "Fiiiine."
                                            un "Here."

                                            "Before any of insertion can happen, I feel my feet letting off a powerful magic current, which travels through the ground."
                                            "It first hits the wooden vines restraining me, getting them loose, then arriving at the plant's roots."
                                            "It screeches in pain and starts shaking."
                                            "The shock was not enough to affect Tate, but enough to burn some roots."
                                            scene forestt with dissolve
                                            "The tentacle vines start to retract, giving the cat his mouth back and letting go of his limbs."
                                            "He pulls his pants back up and runs to me."
                                            show cat20tired with moveinright
                                            t "Finally."
                                            t "You could've hurried, but I'm thankful you managed in the end."
                                            y awkward"Sorry about that. I was... taken by surprise."
                                            hide cat20tired
                                            show cat20smug
                                            t "Can't blame you too much, I'd be paralyzed too if I saw this gift unwrapping in my face."
                                            "He slaps his own ass."
                                            y "Haha... yeah..."
                                            hide cat20smug
                                            show cat20tired
                                            t "God, that thing reached so far down my throat, it kinda hurt."
                                            "He directs his attention back to the plant, the electricity was not enough to kill it, but it can't move much anymore."

                                            jump afterplant





                                    menu planb:
                                        "What's plan B?"
                                        "Get Scribbles to help.":
                                            y pf"Alright asshole, you asked for it."
                                            "Scribbles, shock its roots."
                                            un simple"That is a surprisingly smart idea coming from you."
                                            un pride"Consider it done."
                                            scene plant5 with llongdissolve
                                            scene CGcc7
                                            "As Scribbles prepares a high amount of electricity, the plant has some ideas in mind..."
                                            scene plant6 with llongdissolve
                                            scene CGcc8
                                            "It uses its tentacles to open up Tate's mouth and shove another one inside."
                                            "Tate's dazed expression was a good hint that he's not too excited to have them inside him."
                                            y worried"Scribbles, can you hurry up?"
                                            un suspicious "Unless you want to lose all your energy and faint, this spell needs a couple more seconds to charge."
                                            "At last, I feel my feet letting off a powerful magic current, which travels through the ground."
                                            "It first hits the wooden vines restraining me, getting them loose, then arriving at the plant's roots."
                                            scene plant6 with hpunch
                                            scene CGcc8
                                            "It screeches in pain and starts shaking."
                                            "The shock was not enough to affect Tate, but enough to burn some roots."
                                            scene forestt with longdissolve
                                            "The tentacle vines start to retract, giving the cat his mouth back and letting go of his limbs."
                                            "He pulls his pants back up and runs to me."
                                            show cat20tired with moveinright
                                            t "{i}*cough cough*{/i}"
                                            t "Finally."
                                            hide cat20tired
                                            show cat20simple
                                            t "His sap did taste pretty good though..."
                                            hide cat20simple
                                            show cat21smile1
                                            t "Thanks for not taking an eternity to save me."
                                            y awkward"Y-your welcome, next time I'll be even faster"
                                            hide cat21smile1
                                            show cat21smug
                                            t "Hard to believe, I'd be paralyzed too if I saw this gift unwrapping in my face."
                                            "He slaps his own ass, making one of the cheeks jiggle and leaving a palm print on his baggy pants."
                                            y "Haha... yeah..."
                                            hide cat21smug
                                            show cat20tired
                                            t "God, that thing reached so far down my throat, it kinda hurt."
                                            "He directs his attention back to the plant, the electricity was not enough to kill it, but it can't move much anymore."

                                            jump afterplant



                                        "Use my powers to try and break free.":
                                            "Raw strength didn't help much, so let's try some actual magic."
                                            "I conjure an energy orb the size of a tennis ball and aim it at the Nightfallen's head."
                                            "I fire it, and watch as its momentum gets lost, missing the Nightfallen completely."
                                            y simple"..."
                                            un bored"..."
                                            un squint"That was the most pathetic display of power I've ever seen..."
                                            "Although I did no damage, at least I attracted the Nightfallen's attention."
                                            hide planthead with dissolve
                                            scene plant5 with llongdissolve
                                            scene CGcc7
                                            show planthead2 with dissolve
                                            "The flower bud which I'm calling its {i}'head'{/i} has no eyes, and the mouth is barely a mouth, but I can still see annoyance on it."
                                            "It slowly comes closer, standing now inches from my snout."
                                            y simple"Uhm, hi?"
                                            pl "..."
                                            "I thought this meant it's going to ignore Tate and focus on me, but no."
                                            scene plant6 with llongdissolve
                                            scene CGcc8
                                            show planthead with dissolve
                                            "It uses its tentacles to open up Tate's mouth and shove another one inside."

                                            t "MgghhMhh!"

                                            "I now realize it came closer just to say {i}'that was a mistake, buddy.'{/i} Even if it can't speak."




                                            y pf"Alright asshole, you asked for it."
                                            "Scribbles, shock its roots."
                                            un simple"That is a surprisingly smart idea coming from you."
                                            un pride"Consider it done."
                                            scene plant7 with longdissolve
                                            scene CGcc9
                                            "The plant spawns a cock out of its flower covering the poor cat's butt, which is a sentence I never thought I'd say."
                                            "Tate's panic expression was a good hint that he's not looking too forward to having it shoved inside him."
                                            "It is teasingly rubbing it in between his cheeks, knowing the cat can't do anything about it."
                                            y worried"Scribbles, can you hurry up?"
                                            un suspicious "Unless you want to lose all your energy and faint, this spell needs a couple more seconds to charge."
                                            "The plant seems to get bored of foreplay, and points the tip of its makeshift cock directly towards his victim's hole, ready to penetrate."
                                            t "{i}MhHMGGHmmHG!{/i}"
                                            "Before any of that can happen, I feel my feet letting off a powerful magic current, which travels through the ground."
                                            "It first hits the wooden vines restraining me, getting them loose, then arriving at the plant's roots."
                                            "It screeches in pain and starts shaking."
                                            "The shock was not enough to affect Tate, but enough to burn some roots."
                                            scene forestt with dissolve
                                            "The tentacle vines start to retract, giving the cat his mouth back and letting go of his limbs."
                                            "He pulls his pants back up and runs to me."
                                            show cat20tired with moveinright
                                            t "{i}*cough cough*{/i}"
                                            t "Finally."
                                            hide cat20tired
                                            show cat20simple
                                            t "His sap did taste pretty good though..."
                                            hide cat20simple
                                            show cat21bored
                                            t "You could've hurried a little, you know? But I'm thankful you managed in the end."
                                            y awkward"Sorry about that. I was... taken by surprise."
                                            hide cat21bored
                                            show cat21smug
                                            t "Can't blame you too much, I'd be paralyzed too if I saw this gift unwrapping in my face."
                                            "He slaps his own ass, making one of the cheeks giggle and leaving a palm print on his baggy pants."
                                            y "Haha... yeah..."
                                            hide cat21smug
                                            show cat20tired
                                            t "God, that thing reached so far down my throat, it kinda hurt."
                                            "He directs his attention back to the plant, the electricity was not enough to kill it, but it can't move much anymore."

                                            jump afterplant







                                    label afterplant:
                                        stop music

                                        scene forestt

                                        show cat21smile1
                                        play music "audio/happy2.ogg"

                                        "With Tate now by my side, and the Nightfallen dozens of feet away, I can finally breathe."
                                        y sadsmile"Are you ok?"
                                        t "I am now."
                                        t "That sure was an adrenaline rush, almost lost my virginity back there, haha."
                                        hide cat21smile1
                                        show cat21bored
                                        t "And to a plant Nightfallen, of all things."
                                        t "One of the only species that can't move."
                                        t "Well, other than it's vines."
                                        hide cat21bored
                                        show cat21smug
                                        t "The hunter became the prey!"

                                        y simple"You're a virgin?"

                                        hide cat21smug
                                        show cat21simple

                                        t "Huh?"
                                        y sadsmile"Sorry, weird thing to focus on from all you just said."

                                        hide cat21simple
                                        show cat20smug

                                        t "Curious now, are we?"

                                        y awkward"Y-you just brought it up and..."
                                        t "Oh, don't strain your little head."
                                        t "I know it's surprising for someone like me to not have a body count in triple digits by now, but it's true, I'm pure as fresh snow."

                                        y simple"Didn't you hunt a bunch of Nightfallen before?"
                                        hide cat20smug
                                        show cat21smile
                                        t "Yeah, but I didn't let them do anything to me, I just killed them."
                                        t "I know, I could've gotten A LOT more money if I got rid of their lust first..."
                                        t "And I'm not against that overall, it's just..."
                                        hide cat21smile
                                        show cat21blush3
                                        t "I kinda want to do it for the first time with a special person, you know?"
                                        t "After that I can focus on milking these Nightfallen dry."
                                        hide cat21blush3
                                        show cat21smug
                                        t "Literally."

                                        y s"I understand completely."


                                        t "What about you?"
                                        y sadsmile"Me?"

                                        hide cat21smug
                                        show cat20smug

                                        t "Yeah, did anyone get their hands in that ol' honey jar?"
                                        t "Did anyone shove the string in your sewing needle yet?"
                                        t "Popped your cherry? Glazed the donut?"

                                        y pf"Ok, stop, I got it."
                                        y blush"N-no, I've never done it before either."

                                        hide cat20smug
                                        show cat20sadsmile

                                        t "Awww, that's soooo cute."

                                        y bored"That feels condescending."

                                        y "I'm literally just like you!"

                                        hide cat20sadsmile
                                        show cat20smug

                                        t "Yeah, except that I have guys lined up to get with me."

                                        y simple"I have guys that like me too."

                                        t "Name one."

                                        y pf"I don't want to..."

                                        t "Heh, liar, liar, cats for hire."

                                        y "You should be more grateful to someone who saved your ass."

                                        hide cat20smug
                                        show cat20smug1

                                        t "You're right."
                                        t "Today, you can officially say you destroyed negative one asses."

                                        hide cat20smug1
                                        show cat20ec

                                        t "Huehuehue...he."

                                        y bored"..."

                                        hide cat20ec
                                        show cat20smug1
                                        t "Fun."
                                        t "Anyway, I might not look like it, but I'm super pissed off, so I'm gonna get revenge on this plant."

                                        y simple"What do you have in mi-"
                                        play sound "audio/teleport.ogg"

                                        show cat20teleport with dissolve
                                        hide cat20smug1
                                        hide cat20teleport with dissolve


                                        "He teleports away..."
                                        play sound "audio/teleport.ogg"
                                        show cat20teleport with dissolve
                                        show cat20smug1
                                        hide cat20teleport with dissolve

                                        "Only to come back a second later with a molotov cocktail in hand."
                                        show bush1 zorder 1 with dissolve
                                        show cat20smug1 at left zorder 2 with ease
                                        play sound "audio/fire.ogg"
                                        hide bush1
                                        show bushfire zorder 1 with hpunch
                                        "He lights it up, and throws it at the Nightfallen's roots with no hesitation or warning."

                                        y surprised"Holy shit!"

                                        hide cat20smug1 with moveoutleft

                                        t "HAHAHA, YES, {b}DIE!{/b}"

                                        "The fire makes quick work of the plant, and as soon as it stops moving, I help Tate extinguish the rest of the flames."
                                        hide bushfire with dissolve
                                        "He brought two fire extinguishers, so it wasn't a big deal, just a scare for me."

                                        y angry"This could've started a forest fire!"

                                        show cat20smile with moveinleft

                                        t "Nah, Merina can stop a forest fire from miles away with a flick of her wrist."

                                        y simple"Wow."
                                        y "She's that powerful, huh?"

                                        t "Yep, she's the complete opposite of her mom, fire and ice, tomboy and princess, both scary..."

                                        t "But enough about other people, we still have things to do."
                                        y "Did the plant drop any crystals?"
                                        hide cat20smile

                                        show cat21simple

                                        t "Ah, I forgot to check."
                                        show cat21simple at left2 with ease
                                        t "Let's see."
                                        show cat21simple at right2 with ease
                                        show gemm with dissolve
                                        "He searches through the ashes, and digs up a small, dimly glowing crystal."

                                        t "It's a blue one, kind of small, but we actually charged it a little bit, even if it didn't get to fuck me properly."
                                        hide gemm with dissolve
                                        show cat21simple at center with move
                                        show cat21smile1
                                        t "It should be enough to get some meat for the dragon."
                                        y simple"Wyvern."
                                        hide cat21smile1
                                        show cat21bored
                                        t "My {b}friend{/b}."

                                        scene forest2 with longdissolve

                                        "We fly through the woods, keeping an eye for any traps that might've been activated, and we actually spot our first catch."
                                        "A hare was hanging upside down in a rope trap we set up earlier."
                                        "Tate uses his sharp claws to cut the rope, letting it go free."
                                        "As we mentioned before, neither of us want to kill animals, these traps are only for Nightfallen, so we'll just buy meat from the market."
                                        scene market with dissolve
                                        "This is my first time seeing the market, and it's huge."
                                        "The hubbub is intense in this part of town."
                                        "I couldn't pay much attention to all the merchants, since Tate really wanted to beeline to the meat section and get back to the wyvern."

                                        "He presents the energy crystal to an exchange center, and exchanges them for money, which he uses to buy meat for the wyvern."
                                        "He even got a discount on the meat for being {i}'supercalifragilisticexpialidocious'{/i}."
                                        "Nobody makes an effort to call {i}me{/i} a super complicated sweet nickname..."
                                        "I did get some winks from people my age, so there's that."
                                        "And a lot of invitations from very friendly escorts, way too friendly..."
                                        "But I have to ignore everyone and everything for the sake of my friend!"
                                        scene tent2 with dissolve
                                        "We hurry back, and I'm proud to say that I am now completely used to flying, even at high speeds."
                                        "Everything is exactly as we left it, even the sleeping wyvern in it's burrow."

                                        y simple"Remember, don't wake him up."
                                        y "Just store the meat somewhere cool and wait."
                                        show cat21bored with moveinleft

                                        t "I know how to raise my own kid, thanks."
                                        t "But you're right."
                                        hide cat21bored
                                        show cat20sadsmile

                                        t "I just want a liiiittle peek at him."

                                        t "He's really cute when he's asleep."
                                        t "Hey there my little ange-"
                                        t "Hello?"
                                        hide cat20sadsmile
                                        show cat20simple
                                        t "..."
                                        t "He's not here."

                                        y shoked2"What?"

                                        hide cat20simple
                                        show cat20scream with hpunch

                                        t "HE'S NOT HERE!"
                                        t "HE DISAPPEARED!"
                                        t "HE'S DEAD!"
                                        hide cat20scream
                                        show cat20smile
                                        t "OH GOD, WHAT AM I GOING TO D - oh - there he is."
                                        hide cat20smile with moveoutright

                                        "As Tate started wailing at the sky, he sees the wyvern up in the tree."
                                        "Spotting us and the food, it climbs down like a cat, falling on its back at the end."
                                        "Not as graceful as a feline, are you now?"

                                        t "Aww you're hungry little buddy?"

                                        "I learned my lesson already, and throw the meat down when I see it coming at me."
                                        "It instantly jumps at the bag and tears it open, eating every last morsel in less than two minutes."
                                        "Then goes inside its burrow and coils back to sleep."

                                        y bored"Your {i}'son'{/i} sleeps and eats all day."
                                        y "I don't think he's a great investment."

                                        show cat21simple with moveinright

                                        t "He was literally born today, he'll be more active in the near future."

                                        y pf"Hopefully not in a murderous kind of active way."
                                        hide cat21simple
                                        show cat21bored
                                        t "You are very pessimistic..."

                                        t "You can make yourself useful and tell me the time."

                                        y simple"It's..."
                                        y "11:55 AM."

                                        hide cat21bored
                                        show cat20worried

                                        t "Shit."
                                        t "We're supposed to be there by noon..."
                                        t "Hold on, I'll teleport us there."
                                        hide cat20worried
                                        show cat20tired
                                        t "Hopefully I'll have enough magic to actually pass the auditions."

                                        y sad"Sorry, you wouldn't need to use so much magic if you didn't have to bring me too."
                                        hide cat20tired
                                        show cat20sadsmile

                                        t "Don't be sorry, I love having you with me, I do not regret bringing you around wherever I go."
                                        stop music fadeout 2.0

                                        "His words sound sincere, and frankly, I enjoy my time around him as well."
                                        play sound "audio/teleport.ogg"
                                        scene teleport with dissolve

                                        scene black with longdissolve
                                        play music "audio/upbeat.ogg"

                                        "Today is a big day, fact hinted by the buzz all around the arena."
                                        "Voices can be heard even before we step foot inside."
                                        scene arena2 with dissolve
                                        "The peaceful background of the forest turned into a busy, loud and lively town."
                                        show tiger20bored with moveinleft
                                        "Everyone is getting ready to start the practice session."



                                        "Our friendly neighborhood tiger is waiting for us at the main entrance, with two friends at his side, one of which is Coal."

                                        show cat20smile at right with moveinright

                                        a "Hey, [name], cat."
                                        y s"Hi, Aiden."
                                        t "Where's Dallan?"
                                        t "You know, the actual important one of the friend group."
                                        a "I'll pretend I didn't hear that."
                                        a "Dallan is getting ready to start the announcements, and I'll be joining him soon."
                                        t "He convinced you to help?"
                                        a "Not him... the Headmaster..."
                                        hide cat20smile
                                        show cat20simple at right


                                        a "Dallan did ask me to greet you when you finally decide to show up."
                                        a "Honestly, I started to think this cat convinced you to skip your audition, or even worse, run away with him and get married in a foreign country."
                                        t "I should be taking notes here."

                                        y awkward"S-sorry, we lost track of time."



                                        a "Whatever the case, he also asked me to introduce you to Rose and Coal, although I believe you met Coal already."
                                        y ec"We sure did!"
                                        a "You two can take it from here, I need to get to Dallan before we start."
                                        a "Today's practice and auditions will be spectated by the Headmaster, for whatever reason."
                                        t "We heard..."
                                        a "You four make sure not to {i}'lose track of time'{/i} again."
                                        y sadsmile"We won't!"
                                        y awkward"I mean, we will."
                                        y "I mean we won't lose track of time."

                                        a "..."
                                        a "Yeah, ok, see ya later, [name]."
                                        hide tiger20bored with moveoutleft
                                        "What did I get so flustered for?"
                                        show cat20simple at center with ease
                                        hide cat20simple
                                        show cat20smile
                                        show rosesadsmile at right with moveinright
                                        show coal at left with moveinleft

                                        r "Phew, finally, I thought he'd never stop talking."

                                        t "He's very vocal for someone so grumpy."

                                        co "You can say that again."
                                        co "Since I seem to be the new bridge here, allow me to make the introductions."
                                        co "So, as Aiden mentioned, this lovely lady here is Rose."
                                        hide rosesadsmile
                                        show roseec at right
                                        r "Pleased to meet you, fellow recommended student."
                                        co "And these two troublemakers are [name], the other recommended one, and Tate, my new Shard colleague."
                                        t "Anticlimactic title, but ok."
                                        hide roseec
                                        show rose at right
                                        y "Nice to meet you, we're only missing one now."
                                        co "We tried to find the last guy, but we didn't have much luck."
                                        r "Slippery, that one, I heard he joined the summoners."
                                        r "I personally found my place with the defenders."
                                        y s"We've heard, Dallan was very excited to have you there."
                                        hide cat20smile
                                        show cat20simple
                                        t "You're large."
                                        y angry"Tate!"
                                        y pf"You don't call people {i}'large'{/i}."
                                        hide rose
                                        show roseec at right
                                        r "Haha, it's alright."
                                        r "I AM large, actually, I would prefer the word massive."
                                        r "The ability to hug someone to death comes with hard work!"
                                        y s"A fun way to die."
                                        hide roseec
                                        show rose at right

                                        r "Ah, I heard you two and Coal have auditions today, to join the sorcerers, is that right?"
                                        hide cat20simple
                                        show cat21smug

                                        t "Yep, it's going to be much more fun than any regular practice."

                                        if scam>=1:
                                            hide coal
                                            show coalbored at left
                                            hide cat21smug
                                            show cat21simple
                                            co "For you maybe..."
                                            y worried"Oh... I forgot."
                                            y "Your device didn't come back up, did it?"
                                            hide rose
                                            show rosesimple at right
                                            co "Nope, about two hours left."
                                            co "I'm going to sit this one out, at least at the start."
                                            y "Tate, does that mean-"
                                            t "Detention is back on the table... yeah."
                                            r "You have detention already?"
                                            r "Man, Coal did not exaggerate the word {i}'troublemakers'{/i}, huh?"
                                            y sadsmile"We're not that bad, promise."
                                            hide rosesimple
                                            show rosesadsmile at right
                                            r "I believe you, the first impression is the most important, and so far, I can not imagine either of you doing anything worthy of detention, at least nothing malicious."
                                            t "It doesn't matter, I needed to get out of detention yesterday."
                                            t "If I have to stay in a room for a couple of hours now, it's whatever."
                                            y "And you'll have me for company as well!"
                                            t "Maybe our two new friends here would want to join as well?"

                                            r "I... think I'll pass."
                                            co "Yeah, same here."
                                            t "Your loss."

                                        else:
                                            pass
                                        hide coalbored
                                        show coal at left
                                        hide rosesadsmile
                                        show rose at right
                                        hide cat21simple
                                        hide cat21smug
                                        show cat21smile1
                                        r "Do you hear that? I think my leader is starting the practice."
                                        un "With those ears, I'm not surprised."
                                        co "I believe you're right, we should get going."
                                        t "Yeah, [name], I believe the auditions are held first, so we should really hurry."
                                        y ec"It's been nice meeting you Rose, and seeing you again Coal!"
                                        r "Good luck on the auditions!"
                                        r "And don't be a stranger around me when we meet again, alright?"
                                        "We both give her two thumbs up."

                                        y "Good luck on showing off at practice!"
                                        r "Will dedicate my victory to you!"
                                        co "See ya later."
                                        hide rose with moveoutright
                                        hide coal with moveoutright

                                        "We go our separate ways for now, and as soon as they leave, Tate takes my hand in his, nonchalantly."
                                        "I didn't even notice it happening until he started to swing both our arms as we walked."

                                        hide cat21smile1
                                        show cat21simple

                                        t "Those two are weird."

                                        y simple"Why do you think that? They seemed normal to me."
                                        y bored"Even more normal than anyone I met so far, actually."

                                        t "That's the thing...they're {i}too{/i} normal, the vibes are just off."
                                        "He shrugs."
                                        stop music fadeout 2.0
                                        un "He's probably not used to being around regular people."
                                        scene arena2 with dissolve
                                        play music "audio/jazz5.ogg" fadein 2.0 volume 0.5


                                        "We find some empty seats and wait patiently for Dallan's announcements."
                                        "In the distance I spot Merina and Ollie, standing by the edge of the arena, deep in conversation."
                                        "I greeted all of my friends today, except for them..."

                                        if betray <=1:
                                            jump nomerinaoliver
                                        else:

                                            menu:
                                                "Should I approach them?"

                                                "Yes.":
                                                    $betray +=1
                                                    show cat20simple with moveinleft
                                                    y "Hey, Tate?"
                                                    hide cat20simple
                                                    show cat21bored
                                                    t "Yeah yeah, I could basically hear the creak as your eyes turned towards Merina's tits."
                                                    y awkward"Wha- N-no that's not-"
                                                    t "Oh sorry, I meant Oliver's ass."
                                                    y pf"No specific body parts!"
                                                    y simple"I just thought we should go say hi, together."
                                                    hide cat21bored
                                                    show cat21simple
                                                    "He thinks for a minute."
                                                    hide cat21simple
                                                    show cat21bored
                                                    t "No thanks, Merina mothers me daily, it's nice having a break from her."
                                                    t "As for Oliver... his shy nature pisses me off."
                                                    un bored"Surprise, the cat doesn't like the mouse."

                                                    y "Oh, well, do you mind if I-"
                                                    if betray >=2:
                                                        t "No, you already ditched me for them before, might as well do it again."
                                                        y bored"Can you not make a big deal out of this?"
                                                        y simple"I still like you, I'm not replacing you or anything."
                                                        t "..."
                                                        t "Bring me a snack on your way back..."
                                                        y ec"You got it, Tate!"
                                                        t "..."
                                                        jump merinaandollie


                                                    else:
                                                        t "I'd much rather you stay here."
                                                        t "..."
                                                        hide cat21bored
                                                        show cat21simple
                                                        t "But I guess scoring points with the leader and vice leader of the Shard isn't a bad thing for you."
                                                        t "So I won't stop you."
                                                        y "Thank you, Tate."
                                                        t "..."
                                                        jump merinaandollie


                                                    label merinaandollie:
                                                    scene arena2 with dissolve

                                                    "I leave the sulking cat alone and make my way towards Merina and Ollie."
                                                    un sidee"Man, what a child that one is."
                                                    "He just likes me enough to not want me to leave."
                                                    un "Separation anxiety, if you ask me."
                                                    "Well, I didn't ask."

                                                    "They notice me approaching and signal me to come over."
                                                    "Now I have confirmation they don't mind seeing me."
                                                    "Great, one more worry gone."

                                                    show merina20 at right2 with moveinright
                                                    show ollie2smile at left2 with moveinleft

                                                    m "Hi [name], we were looking all over for you."
                                                    y simple"You were?"
                                                    o "Yes, well, we were mostly worried since we thought Tate might make you be late."
                                                    m "But it seems our worries were in vain."

                                                    y s"We had a busy morning, but teleporting sure is handy."
                                                    y "Are you going to watch us perform?"

                                                    m "We'll be part of the jury, so it would be strange not to be present."

                                                    y pf"Oh, right, the judges, that makes sense."
                                                    y confused"Wait, {i}'part'{/i}?"
                                                    y "Who else is on the jury?"
                                                    o "The Headmaster wants to partake in the final vote."
                                                    o "As a {i}'tiebreaker'{/i}."
                                                    hide merina20
                                                    show merina20bored at right2
                                                    m "Even though me and Ollie never disagreed on an audition..."
                                                    y simple"Should I be worri-"
                                                    hide merina20bored
                                                    show merina20simple at right2
                                                    hide ollie2smile
                                                    show ollie2simple at left2
                                                    "My question was cut short by Dallan's voice suddenly ringing through the whole arena, and our heads turn towards the announcements tower."
                                                    "Aiden's silhouette can be seen to his left, and the Headmaster's to his right."
                                                    d "GOOD AFTERNOON LADIES AND GENTLEMEN."
                                                    d "WELCOME TO THIS YEAR'S PRACTICE SESSION!"
                                                    play sound "audio/cheering.ogg"
                                                    "Cheers erupt throughout the whole place as he continues."
                                                    d "YOU MIGHT BE HAPPY, OR AT LEAST SURPRISED TO FIND OUT WE'VE MADE SOME SMALL CHANGES TO THIS PARTICULAR SESSION."
                                                    d "FIRST AND FOREMOST, I'D LIKE TO PRESENT TO YOU, HEADMASTER ARGUS, WHO WILL BE WATCHING OVER AND ASSESSING THE STUDENTS."
                                                    h "GOOD AFTERNOON EVERYONE, I TRUST WE'LL HAVE A FAIR AND ENTERTAINING PRACTICE SESSION, I'M LOOKING FORWARD TO SEEING THE AMAZING TALENTS THIS ACADEMY HAS TO OFFER."
                                                    stop sound fadeout 2.0
                                                    "Murmurs of confusion and protest can be heard following that statement."

                                                    m "I knew that would be the general reaction, glad I'm not the one making the announcements."
                                                    "Noticing the discomfort created, Aiden intervenes."
                                                    a "OF COURSE, HIS PRESENCE HERE IS PURELY PERSONAL."
                                                    a "YOUR PERFORMANCE TODAY WILL NOT AFFECT YOUR GRADES OR OVERALL YEARLY PERFORMANCE."
                                                    d "Y-YES, THAT'S RIGHT, THANK YOU AIDEN."
                                                    d "AS FOR THE SECOND SMALL BUT EXCITING CHANGE, BEFORE THE REGULAR PRACTICE STARTS, THE FIRST YEARS OF THE SORCERY AND SUMMONING SHARDS WILL HOLD THEIR AUDITIONS IN FRONT OF EVERYONE, INSTEAD OF IT BEING A PRIVATE SHOWCASE LIKE USUAL."
                                                    y s"So the summoners will audition too?"
                                                    m "Yes, before you, in fact."
                                                    o "Their audition is a bit different."
                                                    y simple"Different how?"
                                                    o "Well, for starters, they don't have to fig-"
                                                    show merina20simple at left2 with move
                                                    "Merina covers his mouth."
                                                    m "Shh, don't tell him yet, you'll ruin the surprise."
                                                    show merina20simple at right2 with ease
                                                    "I don't like the sound of that."
                                                    hide merina20simple
                                                    show merina20 at right2
                                                    m "Summoners have to show their summoner abilities in front of the practice opponent, that's all you need to know."
                                                    play music "audio/fight.ogg" fadein 4.0 volume 0.2
                                                    d "LET US START WITH THE FIRST AUDITION PARTICIPANT IN THE LIST."
                                                    d "WITHOUT FURTHER ADO, AIDEN, IF YOU MAY."

                                                    a "AGHEM, PLEASE GIVE IT UP FOR, ALVY, AUDITIONING FOR THE SUMMONERS."
                                                    play sound "audio/cheering.ogg" volume 0.4

                                                    scene arena with dissolve
                                                    "The crowd cheers as a small but clearly confident dog with a neutral, unimpressed expression makes his way in front of the arena."
                                                    show dummy with longdissolve

                                                    d "THIS YEAR'S OPPONENTS WILL BE SOME CLEVERLY DESIGNED SNAKE DUMMIES, CONSTRUCTED BY NONE OTHER THAN THE DEFENDER'S VICE LEADER, CHELSIE!"
                                                    d "SHE IS ALSO LOOKING FOR A NEW WORK ASSISTANT, IF YOU'RE INTO INVENTIONS AND ARE WILLING TO WORK FOR A SUB-MINIMUM AMOUNT, GIVE HER A CALL!"
                                                    d "YOU MUST ALSO BE OKAY WITH THE FOLLOWING POSSIBLE CASUALTIES, AND PLEASE KNOW THAT SHE IS NOT RESPONSIBLE FOR ANY HARM THAT WILL COME TO YOU, SUCH AS: FIRE BURNS, ACID BURNS, FRICTION BURNS, HEAD TRAUMA, LOSS OF LIMBS, LOSS OF TEETH, LOSS OF FUR, FROSTBITE...this list is long..."
                                                    "I try to ignore Dallan's extensive list, and focus instead on the last recommended student I haven't personally met yet."
                                                    "He is faced with the dummy, that is way more intimidating when there's a regular person to compare its size with."
                                                    "It has canons attached to it, as well as saws and rotating blades, not to mention that armor that looks pretty sturdy."
                                                    "He takes out a small handful of crystals, varied in size, from which a dozen Nightfallen spawn."
                                                    "All of them, except for two wolf-like creatures, rush towards the dummy."
                                                    "The dummy senses the danger it's in, so before dealing with the attacking foes, it shoots its canons towards the summoner, Alvy."
                                                    "But the wolves at his side protect him with no problem."
                                                    show dummy with hpunch
                                                    "In seconds, the other Nightfallen, less animalistic in nature, destroy, disassemble and even start devouring the dummy, leaving only scraps behind."
                                                    play sound "audio/cheering.ogg"
                                                    hide dummy with dissolve
                                                    scene arena2 with dissolve
                                                    y surprised"He has impressive summon abilities for a first year."
                                                    show merina20 at right2 with moveinright
                                                    show ollie2smile at left2 with moveinleft
                                                    m "He wasn't recommended for nothing."
                                                    un squint"God... why couldn't HE find my room first?"
                                                    un "I bet I could've been summoned in a matter of days."
                                                    "I doubt anyone but me would've accepted your proposition..."
                                                    "I was desperate."
                                                    un sidee"Touche."

                                                    y s"I didn't get the chance to meet him yet, maybe I can catch him when he gets to his seat."
                                                    o "I don't think you'll be able to do that."
                                                    y simple"Why not?"
                                                    "I watch Alvy walk away, focusing on his path so I can follow him to his spot in the crowd, but after a couple of steps, he turns into smoke and fades from reality."
                                                    y surprised"What the-"
                                                    m "Yeaaah... he does that sometimes."
                                                    y simple"Did he teleport away?"
                                                    o "No, that's not teleportation, it's some form of invisibility."
                                                    m "We heard he's shy."
                                                    "Extreme measures for a shy person."
                                                    hide merina20
                                                    show merina20simple at right2
                                                    hide ollie2smile
                                                    show ollie2simple at left2
                                                    "The combat is done, but Dallan isn't with the list of risks you take by being Chelsie's assistant..."
                                                    d "LOSS OF VISION, LOSS OF TASTE, ERECTILE DYSFUNCTION, PRIAPISM AND LAST BUT NOT LEAST, MINOR DEATH."
                                                    y pf"{i}'Minor'{/i}?"
                                                    d "BACK TO THE AUDITIONS, WOW, WHAT A DISPLAY THAT WAS, TOO BAD OUR FRIEND DIDN'T STICK AROUND TO SEE THE RESULTS, WHICH WILL BE PRESENTED SHORTLY, AS SOON AS THEIR LEADER AND VICE LEADER COME TO A DECISION."
                                                    stop music fadeout 3.0
                                                    "Aiden presented the other people while Dallan offered some commentary."
                                                    "Chelsie tried to break into the announcements cabin, in complete disregard of the Headmaster's presence, to try to shout what I'd call basically IRL ads in the mic for her inventions."
                                                    "Their struggles to contain her were clearly audible, and while the Headmaster was slightly annoyed, the crowd loved the chaos, especially when Aiden shushed the lion's complaints."
                                                    "All of this was great in retrospect, since the other summoners weren't nearly as flashy as the recommended student."
                                                    play music "audio/casual.ogg" fadein 3.0 volume 0.3
                                                    "Obviously, since a summoner is not even expecting to be able to actually summon Nightfallen on their first day, so I wonder if and how their audition is graded."
                                                    m "{i}*sigh*.{/i}"
                                                    m "I have many other things, better to do than this."
                                                    o "Same here, not to be disrespectful, but any summoner that can't yet summon is not worth watching."
                                                    y simple"Yeah... they're kind of... boring."
                                                    m "The seniors are fun."
                                                    y "Do you two have to be here?"
                                                    m "Not for this, but we can't risk missing the sorcerer's auditions."
                                                    y "How many first year summoners are this year?"
                                                    o "You'd have to ask their leader for that information."
                                                    o "I'm assuming there are more than sorcerers, in any case, right, Merina?"
                                                    m "For sure."
                                                    y "Why's that?"
                                                    m "Anyone with any magic in them can be a summoner, even if they can't cast actual spells, but you need active magical power to be a sorcerer."
                                                    "The next summoner is up, and his trick is to make a big crystal in his hand glow."
                                                    m "{i}*sigh*{/i}"
                                                    o "About twenty more minutes of this..."

                                                    "Not if I can help it."
                                                    "This might be a good opportunity to spend some time with them."
                                                    "I should get them out of here."
                                                    un curious"They won't accept, did you not hear them?"
                                                    un "They can't risk missing the sorcerers."
                                                    "In that case, I'll take one of them, and the other can notify us when to come back."
                                                    "This will also give me a reason to ask for their numbers."
                                                    un bored"Or you could've said you want their numbers because you like them."
                                                    un "Like a normal person."
                                                    "Ha ha."
                                                    "No."

                                                    menu:
                                                        "Now which one do I want to spend some alone time with?"

                                                        "Ollie.":
                                                            $ Ollie_points+=1
                                                            y simple"This really is a waste of time."
                                                            y s"Here's an idea!"
                                                            y smug"Why don't I take Ollie with me, whom I chose absolutely randomly and unbiased."
                                                            y ec"And we go relieve some anxiety in the backrooms?"
                                                            un "That sounded way more sexual than you think."
                                                            hide ollie2simple
                                                            hide merina20simple
                                                            show ollie2surprised at left2
                                                            show merina20sadsmile at right2

                                                            "Ollie is taken by surprise by my request, and Merina gives a little giggle and smiles."

                                                            m"That's very thoughtful of you."
                                                            hide merina20sadsmile
                                                            show merina20ex at right2
                                                            hide ollie2surprised
                                                            hide ollie2simple
                                                            show ollie2sweat at left2
                                                            m "I'm sure our little anxiety ball would love some {i}'relief'{/i} from you."
                                                            o "E-ermm, y-yeaaahhh, I-I'd l-love to come w-with...heh."
                                                            y "Just give us a call when we need to come back."
                                                            m "Will do, you two have fun!"

                                                            o "A-are you sure you're ok with this Mer-?"
                                                            y ec"Yes she's sure, let's not waste precious, boring time."
                                                            hide ollie2sweat with moveoutleft
                                                            show merina20ex at center with ease
                                                            "I push Ollie away, looking back and mouthing a silent thank you to Merina, she responds with a wink."
                                                            scene black with dissolve
                                                            stop music fadeout 3.0
                                                            un simple"Do you think she knows?"
                                                            "She absolutely knows."
                                                            un "I'm surprised she's letting you stick your dick in her mouse."
                                                            "We aren't going to do anything like that yet..."
                                                            "Maybe just a makeout session."
                                                            un bored"Hand holding is as far as you'll ever go."
                                                            play music "audio/jazz4.ogg" fadein 3.0 volume 0.4
                                                            scene lobby with dissolve

                                                            "He relaxes when we round the corner and Merina's eyes are no longer on him."
                                                            "The crowd noise goes down the more we walk."
                                                            "Besides the actual arena, the building has some nice indoor rooms to take a break from the madness."
                                                            "We find some seats in a nice waiting room-like area."
                                                            "Not a lot of people around, because obviously, boring or not, they don't want to miss the chance of something actually exciting happening."
                                                            show ollie2 with moveinleft
                                                            y "Hey, I started doing this without asking, but do you mind if I call you Ollie?"
                                                            y "I've noticed Merina is the only one calling you that."
                                                            hide ollie2
                                                            show ollie2smile

                                                            o "You can call me anything."
                                                            y smug"Oh really now?"
                                                            hide ollie2smile
                                                            show ollie2sweat
                                                            o "I-I mean, yeah, Ollie is fine, haha."
                                                            o "I let Dallan call me that as well, but he refuses out of respect, since I'm his senior."

                                                            y "Say, would it be effective if I were to ask you what my audition will consist of?"



                                                            o "I believe there are a lot of ways for you to get that information out of me."
                                                            o "But I'd appreciate it if you didn't try, I'm sure Merina won't be too happy about it."

                                                            y "Shame, because I reaaally want to know."

                                                            "He's sweating."

                                                            y "but I won't force you to tell me, guess that wouldn't be too fair."

                                                            hide ollie2sweat
                                                            show ollie2smile

                                                            o "Phew, thanks [name]."
                                                            y s"You know, speaking of Merina, she usually likes to have you at her side unless there's no other option, isn't that right?"

                                                            o "A bit embarrassing, but you're correct."

                                                            y smug"Yet, she agreed quite quickly for you to come here with me..."
                                                            hide ollie2smile
                                                            show ollie2blush2

                                                            o "W-well, she must trust you a lot then, s-since- uhm...we've spend time together already, a-and you seem nice enough."

                                                            y "You are kind of a bad liar."

                                                            hide ollie2blush2
                                                            show ollie2simple

                                                            o "{i}*sigh*{/i}"
                                                            o "Direct questions are my weakness, I admit."

                                                            y"Then let me take advantage of that for a bit."
                                                            o "Oh boy."
                                                            y "Why was she so excited for me and you to be alone together?"

                                                            hide ollie2simple
                                                            show ollie2go

                                                            o "W-we made a little bet..."

                                                            y simple"A bet?"

                                                            o "Y-yeah, I mean, here's the thing."

                                                            y "I'm all ears."

                                                            hide ollie2go
                                                            show ollie2side3

                                                            o "Merina was really impressed by your dedication to helping Tate, and the way you stood up to the Headmaster."
                                                            o "So she took a liking to you."
                                                            o "People sometimes say she has {i}'impossible'{/i} standards when it comes to sexual partners, unlike a lot of  students here."
                                                            o "But that's not really true, she just wants someone with that's... you know...nice."
                                                            y ec"I doubt I'm the only nice person around, I mean, look at Dallan."
                                                            hide ollie2side3
                                                            show ollie2simple
                                                            o "Dallan is gay."
                                                            y simple"oh."
                                                            o "Plus, she turned down the slayer's Shard vice leader, Aiden, in front of the whole Academy, so everyone thinks she wants someone hotter than Aiden, which is kind of hard to achieve."
                                                            y "That's true."
                                                            y confused"But doesn't all that prove the exact opposite? She was supposed to be upset that I didn't invite her first."

                                                            hide ollie2simple
                                                            show ollie2go

                                                            o "Weeell, this is where the bet comes in."
                                                            y "Bet on...me?"
                                                            o "Y-yeah, you see, when she made you shadow me, I didn't like that much, and didn't like you much for that either at the time, but once you pinned me to that wall..."

                                                            un "Ah, he's a kinky bitch, go it."
                                                            hide ollie2go
                                                            show ollie2blush2

                                                            o "Something just... sparked."
                                                            o "And after that, I realized you are actually very respectful, and fun, but not in an eccentric way, and smart, and pretty."
                                                            y blush"Pretty?"
                                                            o "Y-yes, uhm, you're kind of...the best of both worlds, to put it simply."
                                                            o "So I told Merina I liked you."
                                                            o "Unfortunately for me, she said she does too."
                                                            y simple"But you weren't sure which one {b}I{/b} like more in {i}THAT{/i} way."
                                                            o "Exactly."

                                                            o "So, in conclusion, if you don't mind me asking."
                                                            o "Do you... like me {i}THAT{/i} way?"

                                                            "Usually, when I'm around this shy mouse, I feel confident and in control."
                                                            "But now, I can't help but get as flustered as a teenage girl, who's fictional crush just did a fan service."
                                                            "Or perhaps these are other emotions rising up, creating confusion."



                                                            menu:
                                                                "I'm not sure what I'm feeling, but as we're sitting here, on these soft and comfortable couches, I know what I want to do."
                                                                "Tea?":
                                                                    $ ollieinvite +=1

                                                                    y ec"Would you be interested in a cup of tea?"
                                                                    show ollie2laugh with dissolve
                                                                    hide ollie2blush2

                                                                    "He smiles widely, his face lighting up after the embarrassing but well received confession."
                                                                    o "I'd love that."
                                                                    hide ollie2laugh with dissolve
                                                                    "After all, he did mention tea is the only love language he knows, but that's no longer true, considering he confessed with real words, so now it's my turn to turn to tea for help."

                                                                    "I brewed both a cup of jasmine tea with some lemon."
                                                                    "There are biscuits and other pastries at the self-serve station, so I grab something sweet as well."
                                                                    "For the first time, his mind is focused."
                                                                    "Focused on me, of all things, studying my movements, but looking away whenever I try to lock eyes with him, smiling awkwardly."
                                                                    "They only have single use cardboard cups here, but hey, the actual tea and the company is what really matters."
                                                                    "Ollie accepts the cup, holding it with both hands, as if trying to warm up."
                                                                    "We sit on the soft sofas, no sounds can be heard, save for our occasional munching and tea sipping, as well as the steps of people passing by, on their way to the bathroom or back to the boring summoners auditions."
                                                                    "I let the silence settle, either because I know Ollie appreciates it, or perhaps I started to enjoy it as well..."
                                                                    "That is, until he breaks it, which takes me by surprise."
                                                                    show ollie2smile with dissolve
                                                                    o "Hey..."
                                                                    y s"Yeah?"
                                                                    o "Remember when we talked about... potions and stuff?"
                                                                    y "How could I forget, you were so passionate about it."
                                                                    hide ollie2smile
                                                                    show ollie2side3
                                                                    o "W-well, I was wondering, uhm, would you like to..."
                                                                    o "Maybe help me out, sometime?"
                                                                    y ec"I'd be delighted to!"
                                                                    y "Maybe tonight?"
                                                                    hide ollie2side3
                                                                    show ollie2blush3
                                                                    o "T-tonight?"

                                                                    hide ollie2blush3
                                                                    show ollie2blush2
                                                                    o "A-actually, I was thinking the same thing... I just thought it would be a bit sudden, heh."
                                                                    y ec"Not at all, the sooner the better."
                                                                    y smug"So it's a date."
                                                                    hide ollie2blush2
                                                                    show ollie2blush3
                                                                    o "D-date!?"
                                                                    o "I-I mean, yes."
                                                                    o "Of course."
                                                                    hide ollie2blush3
                                                                    show ollie2sweat
                                                                    o "God, I'm bad at this..."
                                                                    o "Sorry."
                                                                    y s"Don't be."
                                                                    y "Your personality is one of the things I like so much about you."
                                                                    y "Would be a shame if you were just another fuckboy."
                                                                    o "That's reassuring."
                                                                    hide ollie2sweat
                                                                    show ollie2smile
                                                                    o "The laboratory in the East wing, after midnight."
                                                                    o "H-how does that sound?"

                                                                    y ec"Sounds perfect, I'll be there."
                                                                    "I grab the flustered mouse's empty cup and place it inside mine, and throw them away, as well as the small snack plate, now empty."
                                                                    jump afterollieconfesion




                                                                "Kiss him.":
                                                                    scene lobby
                                                                    show ollie2smile
                                                                    "This man is too adorable to pass up."
                                                                    "He finally cracked his shell, so why not help him come out even faster?"
                                                                    "I lean in with my eyes closed."
                                                                    hide ollie2smile
                                                                    show ollie2blush3 with hpunch
                                                                    "He is expecting a verbal confirmation, that's why he just stood there in shock as our lips touched."
                                                                    "I make sure not to push too far, or else he might just fall over."
                                                                    "This way, our lips barely caressed each other, a brush, just a taste."
                                                                    "But we don't need more right now, we'll have time for rough play later, for now, I just want him to know what I feel."
                                                                    "Unfortunately, I don't feel his mouth returning anything."
                                                                    st "Oooooo."
                                                                    "Ah, I forgot there are the occasional people walking by."
                                                                    "Don't you have boring summoner auditions to watch!?"
                                                                    "I pull away, seeing Ollie staring past my head, still stunned."
                                                                    y simple"Are you ok?"
                                                                    y smug"Was I too sudden?"
                                                                    o "Yes."
                                                                    y simple"Oh... sorry, I didn't mean to upset you."
                                                                    y "I thought it would be an appropriate response for a love con-"

                                                                    hide ollie2blush3
                                                                    show ollie2sweat

                                                                    o "No, i-it's alright..."
                                                                    o "I mean, I didn't hate it, it was just a little sudden, as you said."
                                                                    o "I didn't have time to prepare."
                                                                    o "Plus, we're in public, and that's a little embarrassing..."
                                                                    o "I didn't come here with the intention to confess let alone kiss..."
                                                                    o "This just isn't really my love language, you know?"

                                                                    y "So I ruined the moment."
                                                                    hide ollie2sweat
                                                                    show ollie2simple

                                                                    o "Yes."

                                                                    y bored"..."
                                                                    y pf"You're very sincere."
                                                                    hide ollie2simple
                                                                    show ollie2sweat
                                                                    o "I'm really sorry!"
                                                                    o "You're great, I swear, I-"
                                                                    if Ollie_points >=3:
                                                                        $ ollieinvite +=1
                                                                        hide ollie2sweat
                                                                        show ollie2smile
                                                                        o "Look, come by my office-"
                                                                        o "No."
                                                                        o "The laboratory in the East wing, after midnight."

                                                                        y simple"That's oddly specific, should I ask what for?"

                                                                        o "I'll make it up to you."
                                                                        o "You and Merina are some of the only people I can confidently say I'm comfortable to be around."
                                                                        o "So if we two are alone..."

                                                                        y ec"Say no more, I'll be there."

                                                                        o "Y-you will?"
                                                                        y "Yeah, I wouldn't miss it for the world."
                                                                        y "I so wanna know what you have planned {i}'after midnight'{/i}."
                                                                        hide ollie2smile
                                                                        show ollie2blush2
                                                                        o "I really thought I messed up."
                                                                        y sadsmile"It's my fault for forgetting your boundaries, I should've been a bit more cautious, promise to do so in the future."

                                                                        "He giggles and rubs the back of his head."
                                                                        hide ollie2blush2
                                                                        show ollie2smile
                                                                        "Both our phones make a sound the next second, at the same time."
                                                                        y smug"I can guess who this is."

                                                                    else:

                                                                        o"I'm sorry...I'm just not comfortable enough in this situation."
                                                                        y simple "Oh...I understand."
                                                                        pass

                                                                    scene lobby
                                                                    show ollie2smile

                                                                    o "We should head back now, it would be for the best."

                                                                    scene black with dissolve

                                                                    "As much as I want to hold his hand on our way there, or better yet, carry him in my arms, I have to respect his refusal for public display of affection."

                                                                    jump afterollieconfesion






                                                        "Merina.":
                                                            $ Merina_points +=1
                                                            scene arena2
                                                            show ollie2simple at left2
                                                            show merina20simple at right


                                                            y bored"This really is a waste of time."
                                                            y s"Here's an idea!"
                                                            y "Why don't I take Merina with me, whom I chose absolutely randomly and unbiased."
                                                            y "And we go relieve some anxiety in the backrooms?"
                                                            un "That sounded way more sexual than you think."
                                                            hide merina20simple
                                                            show merina20sur at right2
                                                            hide ollie2simple
                                                            show ollie2ex at left2

                                                            "Merina is taken by surprise by my request, and Ollie, surprisingly, gives a little giggle and smiles."

                                                            m"That's very thoughtful of you."
                                                            m "But I don't think I should leave Ollie alone."
                                                            o "Ah, n-no no, don't worry about me, you should just go with [name]."
                                                            o "I'm not a baby, I'll be alright on my own."
                                                            m "But what if-"
                                                            play sound "audio/siren.ogg" volume 0.4
                                                            show chelsie with moveinleft
                                                            hide merina20sur
                                                            show merina20simple at right2
                                                            ch "Do not worry Merina, I'll take care of your vice!"
                                                            m "Chelsie!"
                                                            y "Hi Chelsie."
                                                            ch "Hello hello."
                                                            o "See? I even have a bodyguard now."
                                                            hide chelsie
                                                            show chelsieec
                                                            ch "Yeah! I kind of need a word in with all the vices, so it's a perfect opportunity to get rid of his shadow."
                                                            hide merina20sur
                                                            show merina20simple at right2
                                                            m "Am I the shadow?"
                                                            ch "A-ha."
                                                            hide merina20simple
                                                            show merina20sadsmile at right2
                                                            m "I deserve that title."
                                                            m "Alright, I suppose I can go clear my mind from all... this."
                                                            "She gestures towards the current contestant, that's making what sounds like puking noises, trying to conjure a Nightfallen."
                                                            y pf"Yeaaaah..."
                                                            y "Let's go."
                                                            m "See you later."
                                                            hide merina20sadsmile with moveoutright
                                                            "Merina gives a curt nod and a polite bow to Chelsie, which she returns in a very exaggerated manner then follows closely behind as I lead the way in the backrooms."
                                                            y ec"Just give us a call when we need to come back."
                                                            o "Will do, you two have fun!"
                                                            stop music fadeout 3.0


                                                            scene black with dissolve


                                                            un "Do you think he knows?"
                                                            "He absolutely knows."
                                                            un "I'm surprised he's letting you stick your dick in his fox."
                                                            un "Encouraging to do so, even."
                                                            "We aren't going to do anything like that yet..."
                                                            "Maybe just a make-out session."
                                                            un "Hand holding is as far as you'll go."

                                                            scene lobby with longdissolve
                                                            play music "audio/jazz4.ogg" fadein 3.0 volume 0.4

                                                            "She relaxes when we round the corner and Ollie's eyes are no longer on us."
                                                            "The crowd noise goes down the more we walk."
                                                            "Besides the actual arena, the building has some nice indoor rooms to take a break from the madness."
                                                            "We find some seats in a nice waiting room-like area."
                                                            "Not a lot of people around, because obviously, boring or not, they don't want to miss the chance of something actually exciting happening."

                                                            show merina20bored with moveinleft



                                                            y "Say, would it be effective if I were to ask you what my audition will consist of?"

                                                            m "That isn't the only reason you wanted to get me out of there, is it?"
                                                            y awkward"No! Promise it's not, but it would be a nice bonus."

                                                            hide merina20bored
                                                            show merina20sadsmile

                                                            m "Good, because I wish I could tell you, but it wouldn't be fair."

                                                            y s"I understand."


                                                            y "You know, I was a bit surprised you accepted to come here, even if Chelsie is watching Ollie."
                                                            y sadsmile"Which arguably... might be worse than leaving him alone..."

                                                            "She chuckles."

                                                            m "It would seem that way, but Chelsie is actually very caring when it comes to her friends."
                                                            m "As for Ollie... well, I suppose he noticed how uncomfortable the auditions made me?"

                                                            y "Still, he agreed quite quickly for you to come with me..."

                                                            m "W-we.. had a heated argument before you came around? Yes, that's what it was."

                                                            y pf"Yep, that sure explains it, the anxious mouse argued with his favorite person in the world, he for sure stood his ground and manipulated me into getting you away from him because he's just sooo done with you."

                                                            m "Y-you're right on that..."
                                                            y s"You are a pretty bad liar."

                                                            m "{i}*sigh*.{/i}"
                                                            m "Bad liar, the one weakness I share with Ollie."


                                                            m "But unlike him, I can be direct when I want as well."
                                                            m "So, you want the truth?"

                                                            y ec"I appreciate honesty."
                                                            m"We made a little bet..."

                                                            y simple"A bet?"

                                                            m "Yes, here's the thing."

                                                            y s"I'm all ears."

                                                            m "You impressed me with your chivalry and kind heart, the way you stood up for your friend, the way you treated Ollie, so I took a liking to you from the start."

                                                            m"People sometimes say I have {i}'impossible'{/i} standards when it comes to partners, unlike a lot of students here."
                                                            m "But that's not really true, I just want someone that's... you know... nice."
                                                            y smug"I doubt I'm the only nice person around, I mean, look at Dallan."
                                                            m "Dallan is gay."
                                                            y simple"oh."
                                                            m "Plus, I turned down Aiden, in front of the whole Academy, so everyone thinks I want someone hotter than him, which is kind of hard to achieve."
                                                            y pf"That's true."
                                                            y confused"But where is this going?"

                                                            m "Because of how you treated Ollie, I started to like you, the problem is that so did he..."


                                                            m "So we had that tiny bet going."
                                                            y "On...me?"
                                                            m "Yes, we wanted to see whichever one YOU like better, so we don't fight a losing battle for something we can't achieve."
                                                            "She covers her mouth with her index finger and plays with her hair as she says the sentence, slowly realizing with each word that she's basically confessing right now."


                                                            m "Something just... sparked."
                                                            m "And after that, I realized... you're just... kind of perfect?"
                                                            y surprised"Perfect?"
                                                            m "At least as far as I can see."
                                                            m "You're smart, reliable, pretty, kind and loyal."
                                                            y sadsmile"Pretty?"
                                                            m "Very."


                                                            y "And you weren't sure which one I like {i}THAT{/i} way."
                                                            m "Exactly."
                                                            m "I realize this is a bit sudden, and perhaps bold of me, but may I ask..."
                                                            show merina20blush with dissolve
                                                            hide merina20sadsmile
                                                            m"Do you... like me {i}THAT{/i} way?"


                                                            "The most elegant and beautiful woman around just said I'm {i}'perfect'{/i} and she hopes I like her too..."
                                                            "Well, {b}of course I don't{/b}."
                                                            "Why would I like that long, silky and shiny hair?"
                                                            "The lithe, hourglass figure."
                                                            "The swing of her tail as her hips naturally sway along."
                                                            "The sly eyes and powerful gaze that hide an innocent and kind soul."
                                                            "The hardworking, talented, artistic fox that- OF COURSE I LIKE HER!"
                                                            y blush"I'd be a fool to say no."
                                                            show merina20sur with dissolve
                                                            hide merina20blush with dissolve
                                                            "Her eyes widen and all movements from her stop, as if stuck in time."
                                                            y ec"I'm glad I at least made it obvious enough for you to say all that."
                                                            "Or perhaps these are other emotions rising up, creating confusion."
                                                            show merina20blush1 with dissolve
                                                            hide merina20sur with dissolve

                                                            "She smiles."
                                                            "A beautiful, sincere smile accompanied by closed, grateful eyes."
                                                            m "The hardest part is over."
                                                            hide merina20blush1
                                                            show merina20
                                                            "Relieved, she resumes her dignified stance."
                                                            m "Why don't we take some seats, like normal people?"
                                                            scene lobby with dissolve
                                                            "I now notice the silence and emptiness of the room, soft looking sofas begging for someone to sit on them, like some weird perverts."

                                                            "I bring us a small cup of coffee each, and begin talking as all that mini confession didn't even happen, except that the words and topics used, are more personal, rather than professional."

                                                            "She tells me more about her awesome mother, the Crimson Witch, despite their difference in personality and magic, they get along very well, just like me and my mom."
                                                            "We end up talking about video games, out of the blue, and she surprised me with her superior knowledge on the topic."
                                                            show merina20bored with dissolve
                                                            m "Most triple A games these days are not as they used to be, honestly, can barely find one that isn't half baked."
                                                            y simple"So many good ideas go to waste because of corporate greed."
                                                            hide merina20bored
                                                            show merina20sadside
                                                            m "{i}*sigh*{/i}"
                                                            m "Maybe it's for the best in my case."
                                                            m "It's not like I have that much free time on my hands, especially with my other hobbies that I'd hate to neglect."
                                                            y s"Such as painting?"
                                                            m "Yes."
                                                            show merina20sadsmile with dissolve
                                                            hide merina20sadside

                                                            m "..."
                                                            m "Speaking of painting."
                                                            m "I'm working on some new magic, a new trick, if you may, that revolves around that."

                                                            y s"Painting magic?"
                                                            y "Consider me intrigued."

                                                            if Merina_points <=2:
                                                                "She considers for a moment, then-"
                                                                m "N-never mind, it's stupid, forget it."
                                                                y simple"Oh, ok then..."
                                                                "I guess she doesn't consider me a close enough friend yet to go any further with me."
                                                                jump aftermerinaconfession
                                                            else:
                                                                $ merinainvite +=1

                                                                hide merina20sadsmile
                                                                show merina20

                                                                m "Great, then you wouldn't mind helping me out, would you?"

                                                                y ec"I'd love to!"
                                                                y pf"Uhm, what would I help with, exactly?"

                                                                hide merina20
                                                                show merina20blush1

                                                                m "Let's just say my favorite art topic is life figure drawing, from reference."
                                                                m "And it's a bit embarrassing to ask just anyone to pose..."

                                                                y blush"Say no more, call on me any time."
                                                                hide merina20blush1
                                                                show merina20
                                                                m "In that case, what do you think about tonight?"

                                                                y "T-tonight?"

                                                                hide merina20
                                                                show merina20blush

                                                                m "I'm rushing into things, aren't I?"
                                                                y blush"No no!"
                                                                y "Tonight is perfect!"

                                                                m "So, it's a date then?"
                                                                y awkward"Sure, date, yes, yep, aha."
                                                                hide merina20blush
                                                                show merina20ex
                                                                "She chuckles."
                                                                m "After midnight, my studio."
                                                                y s"You have an art studio?"
                                                                m "Well, it's not supposed to be an art studio, I requested a room for training, but you can get away with things when you're a leader."
                                                                y smug"Look at you, miss rebel."

                                                                "We end our final awkward moments alone in the back rooms with some instructions on how I should get to that {i}'studio'{/i} of hers."
                                                                jump aftermerinaconfession




                                                            label aftermerinaconfession:

                                                            scene lobby
                                                            show merina20

                                                            "Merina's phone buzzes, a message from Ollie appearing on the screen."

                                                            m "It's time we head back."
                                                            stop music fadeout 3.0
                                                            scene black with dissolve
                                                            "As soon as we leave the backrooms, we're greeted by a smiling mouse, and a missing raccoon."

                                                            scene arena2 with dissolve
                                                            show ollie2smile at left2 with moveinleft
                                                            show merina20simple at right2 with moveinright
                                                            play music "audio/casual3.ogg"

                                                            o "All good?"
                                                            y smug"All good."
                                                            m "Ollie.. where is Chelsie?"
                                                            o "She got a customer for one of her inventions so she had to go."
                                                            m "Money is always more important than anything for that one..."
                                                            o "Hey, Merina, did you...?"
                                                            hide merina20simple
                                                            show merina20sadsmile at right2
                                                            m "Yup, and he knows now as well, you know how I am when it comes to lying."

                                                            hide ollie2smile
                                                            show ollie2simple at left2

                                                            o "Oh..."

                                                            y ec"Don't worry, your little bet left me flattered."
                                                            show merina20blush at right2 with dissolve
                                                            hide merina20sadsmile
                                                            hide ollie2simple
                                                            show ollie2blush2 at left2
                                                            o "I-I see."
                                                            o "That's good."
                                                            "His face becomes red."
                                                            "But Merina's even more so, the thoughts of what we talked about are probably only now settling in."

                                                            m "Heh, still, this is embarrassing."



                                                            m "E-excuse me, I need to... go prepare for the auditions, they're about to start."
                                                            m "And remove myself from this situation before I overheat."
                                                            y simple"Prepare?"
                                                            hide merina20blush with moveoutright

                                                            "She leaves in a hurry before answering."
                                                            show ollie2smile at left2 with dissolve
                                                            hide ollie2blush2

                                                            y "Do you think we made her uncomfortable or is she just that emotional?"

                                                            o "No way, she's just not used to these kinds of feelings."

                                                            y "Then why does she need to prepare?"
                                                            o "Ah, that?"
                                                            o "I guess it won't hurt to tell you now."
                                                            o "You'll have to fight her."
                                                            stop music
                                                            play sound "audio/scratch.ogg"
                                                            y angry"WHAT?!"
                                                            y worried"Fight a leader?"
                                                            play music "audio/casual3.ogg" volume 0.4
                                                            o "Don't worry, she's going to hold back and adapt to your style of fighting."
                                                            o "It's not as bad as it seems."
                                                            y "Still..."
                                                            o "That reminds me, I have to go give the rules to other participants as well."
                                                            stop music fadeout 2.0
                                                            scene black with dissolve
                                                            "Before he can walk away, Tate makes his way towards us."
                                                            "He notices Ollie's anxious fidgeting and forces him to tell him whatever he's hiding."
                                                            "The cat did not take the news too well... but I managed to hold him back and let Ollie walk away."
                                                            scene arena2 with dissolve
                                                            show cat21mad2 with moveinright
                                                            play music "audio/purplecat.ogg"
                                                            t "GET BACK HERE!"

                                                            "His cries of protest get swallowed by Dallan's loud voice."
                                                            hide cat21mad2
                                                            show cat21simple

                                                            d "WHAT A..UHMM, INTERESTING AUDITION SESSION PROVIDED BY THE SUMMONERS!"
                                                            d "BOY AM I SAD IT'S ALREADY OVER, ISN'T THAT RIGHT, AIDEN?"
                                                            a "{i}*snooooore*{/i}"
                                                            a "Huh, Wha-"
                                                            a "Are they finally done?"
                                                            d "MOOOVING ON, IT IS TIME FOR THE SECOND AUDITION SESSION, THIS TIME, FOR THE NEW SORCERERS OF THE YEAR!"
                                                            hide cat21simple
                                                            show cat21smug
                                                            "People all around groan intensely, clearly done with auditions."
                                                            t "Heh, suckers, they don't know this part will actually be fun to watch."
                                                            d "THIS YEAR'S TASK WILL BE EXPLAINED BY THE SHARD'S VICE, OLIVER, TO EACH PARTICULAR PARTICIPANT IN PRIVATE BEFORE THEIR MATCH!"
                                                            a "THAT IS A DUMBASS RULE."
                                                            a "{i}Oops, didn't mean to say that to the speaker.{/i}"
                                                            a "WITHOUT FURTHER ADO, LET'S WELCOME OUR FIRST STUDENT IN THE ARENA."
                                                            a "CONNOR."
                                                            play music "audio/fight.ogg" fadein 3.0

                                                            hide cat21smug

                                                            show cat20simple


                                                            y confused"Connor?"
                                                            t "Is that the guy who stole our table in the morning?"
                                                            "A German Shepherd wearing a red vest walks casually in the ring."
                                                            y bored"Yep."
                                                            y "The very same."
                                                            a "YOU'RE A BITCH, CONNOR."
                                                            "The dog looks up at the announcement tower with an {i}'are you serious?'{/i} expression on his face, along with other confused audience members."
                                                            t "We're not the only ones that recognized him."

                                                            t "Let's see how this whole {i}'Merina as an opponent'{/i} will play out."


                                                            "From the other side of the ring, the figure of a tall, gracious white fox comes into view confidently."



                                                            play sound "audio/bell.ogg"
                                                            "The bell rings."
                                                            "I can't quite describe what I'm seeing, since everything is a blur, or more like a blizzard."
                                                            "Merina's magic envelops the arena, and she concentrates different attacks, from long range to close, from projectiles to trickery."
                                                            "Connor is hanging in pretty strong, using a diverse set of spells as well, but in the end, two minutes is all he could muster."
                                                            "Leaving the poor woman disappointed, but victorious."
                                                            "Still, the crowd cheers for him."
                                                            stop music fadeout 2.0
                                                            play music "audio/purplecat.ogg" fadein 3.0

                                                            "Dallan and Aiden present the next contestant, while Merina resumes her initial position and makes all the extra ice she created in the battle disappear."
                                                            show ollie2 at left with moveinleft
                                                            hide cat20simple
                                                            show cat21mad2
                                                            "Oliver comes by sometime, and we try to press him for more information, but I'm not letting Tate intimidate him."
                                                            "All we get is that we don't have to defeat her, or even come close to that, we just have to show off our magic."
                                                            "Winning would be a big plus."
                                                            hide ollie2 with moveoutright
                                                            hide cat21mad2
                                                            show cat20smug1

                                                            "Just a showcase, that's reassuring."

                                                            hide cat20smug1
                                                            show cat21spark with hpunch
                                                            stop music fadeout 2.0



                                                            "Tate suddenly grabs my arm and shoulder and shakes me vigorously."
                                                            play music "audio/fight.ogg" volume 0.3
                                                            t "They're done they're done they're done!"
                                                            t "It's my turn!"
                                                            y worried"Huh, what happened to the other guy? I wasn't paying attention?"
                                                            t "I don't know, he probably died, don't care."
                                                            y worried"I care..."
                                                            t "SSSHHHHH!"
                                                            d "THAT LOOKED LIKE IT HURT."
                                                            d "I'M SURE HE'LL BE ALRIGHT, NO NEED TO MAKE A FUSS."
                                                            a "STILL, MIGHT HAVE TO ASK FOR SOME PULLED PUNCHES FROM OUR LEADER COLLEAGUE."
                                                            m "Sorry..."
                                                            d "{i}*COUGH COUGH*{/i}"
                                                            d "W-WE'LL CONTINUE WITH THE NEXT FIRST YEAR."
                                                            a "EVERYBODY WELCOME OUR LOCAL TROUBLEMAKER, TATE."
                                                            play sound "audio/cheering.ogg" volume 0.4
                                                            stop music fadeout 3.0
                                                            hide cat21spark
                                                            show cat21mad2
                                                            t "Damn it Aiden."
                                                            t "He didn't use the name I gave him."
                                                            hide cat21mad2
                                                            show cat20smug


                                                            t "No matter, I'll show Merina."
                                                            t "I'm so gonna win."
                                                            y ec"Good luck!"
                                                            hide cat20smug with moveoutright




                                                            jump tatefight


                                                            label afterollieconfesion:

                                                            scene arena2 with dissolve
                                                            show merina20 at right2 with moveinright
                                                            show ollie2smile at left2 with moveinleft
                                                            play music "audio/casual3.ogg" fadein 2.0


                                                            "The things Ollie said about Merina seem to be true, as she greets us with anticipation."
                                                            m "All good?"
                                                            y smug"All good."
                                                            m "Ollie, did you...?"
                                                            o "Y-yeah, actually, and he knows, it's okay."
                                                            hide merina20
                                                            show merina20simple at right2

                                                            m "Oh..."

                                                            y ec"Don't worry, your little bet left me flattered."
                                                            m "I-I see."
                                                            hide merina20simple
                                                            show merina20blush at right2
                                                            "Her face becomes red."

                                                            m "Heh, still, this is embarrassing."


                                                            m "E-excuse me, I'll just... go prepare for the auditions, they're about to start."
                                                            y confused"Prepare?"
                                                            hide merina20blush with moveoutright

                                                            "She leaves in a hurry before answering."
                                                            show ollie2smile at center with ease

                                                            y simple"Do you think we made her uncomfortable or... jealous?"

                                                            o "No way, she's just not used to these kind of feelings."

                                                            y "Then why does she need to prepare?"
                                                            o "Ah, that?"
                                                            o "I guess it won't hurt to tell you now."
                                                            o "You'll have to fight her."
                                                            y angry"WHAT?!" with hpunch
                                                            y worried"Fight a leader?"
                                                            o "Don't worry, she's going to hold back and adapt to your style of fighting."
                                                            o "It's not as bad as it seems."
                                                            y simple"Still..."
                                                            o "That reminds me, I have to go give the rules to other participants as well."
                                                            stop music fadeout 3.0
                                                            scene black with dissolve
                                                            "Before he can walk away, Tate makes his way towards us."
                                                            "He notices Ollie's anxious fidgeting and forces him to tell him whatever he's hiding."
                                                            "The cat did not take the news too well... but I managed to hold him back and let Ollie walk away."
                                                            scene arena2 with dissolve
                                                            show cat21mad2 with moveinleft
                                                            play music "audio/purplecat.ogg"
                                                            t "GET BACK HERE YOU!"

                                                            "His cries of protest get swallowed by Dallan's loud voice."
                                                            hide cat21mad2
                                                            show cat21simple

                                                            d "WHAT A..UHMM, INTERESTING AUDITION SESSION PROVIDED BY THE SUMMONERS!"
                                                            d "BOY AM I SAD IT'S ALREADY OVER, ISN'T THAT RIGHT, AIDEN?"
                                                            a "{i}*snooooore*{/i}"
                                                            a "Huh, Wha-"
                                                            a "Are they finally done?"
                                                            d "MOOOVING ON, IT IS TIME FOR THE SECOND AUDITION SESSION, THIS TIME, FOR THE NEW SORCERERS OF THE YEAR!"
                                                            "People all around groan intensely, clearly done with auditions."
                                                            hide cat21simple
                                                            show cat21smug
                                                            t "Heh, suckers, they don't know this part is actually fun to watch."
                                                            d "THIS YEAR'S TASK WILL BE EXPLAINED BY THE SHARD'S VICE, OLIVER, TO EACH PARTICULAR PARTICIPANT IN PRIVATE BEFORE THEIR MATCH!"
                                                            a "THAT IS A DUMBASS RULE."
                                                            a "Oops, didn't mean to say that to the speaker."
                                                            a "WITHOUT FURTHER ADO, LET'S WELCOME OUR FIRST STUDENT IN THE ARENA."
                                                            hide cat21smug
                                                            show cat21simple
                                                            a"CONNOR."
                                                            play music "audio/fight.ogg"


                                                            y confused"Connor?"
                                                            t "Is that the guy who stole our table in the morning?"
                                                            "A German Shepherd wearing a red vest walks casually in the ring."
                                                            y bored"Yep."
                                                            y "The very same."
                                                            a "YOU'RE A BITCH, CONNOR."
                                                            "The dog looks up at the announcement tower with an {i}'are you serious?'{/i} expression on his face, along with other confused audience members."
                                                            t "We're not the only ones that recognized him."

                                                            t "Let's see how this whole {i}'Merina as an opponent'{/i} will play out."


                                                            "From the other side of the ring, the figure of a tall, gracious white fox comes into view confidently."



                                                            play sound "audio/bell.ogg"
                                                            "The bell rings."
                                                            "I can't quite describe what I'm seeing, since everything is a blur, or more like a blizzard."
                                                            "Merina's magic envelops the arena, and she concentrates different attacks, from long range to close, from projectiles to trickery."
                                                            "Connor is hanging in pretty strong, using a diverse set of spells as well, but in the end, two minutes is all he could muster."
                                                            "Leaving the poor woman disappointed, but victorious."
                                                            play sound "audio/cheering.ogg"
                                                            "Still, the crowd cheers for him."

                                                            "Dallan and Aiden present the next contestant, while Merina resumes her initial position and makes all the extra ice she created in the battle disappear."
                                                            show ollie2 at right with moveinright
                                                            hide cat21simple
                                                            show cat21mad
                                                            "Oliver comes by sometime, and we try to press him for more information, but I'm not letting Tate intimidate him."
                                                            "All we get is that we don't have to defeat her, or even come close to that, we just have to show off our magic."
                                                            "Winning would be a big plus."
                                                            hide ollie2 with moveoutright
                                                            hide cat21mad
                                                            show cat21smug

                                                            "Just a showcase, that's reassuring."

                                                            hide cat21smug
                                                            show cat21spark with hpunch


                                                            "Tate suddenly grabs my arm and shoulder and shakes me vigorously."
                                                            t "They're done they're done they're done!"
                                                            t "It's my turn!"
                                                            y confused"Huh, what happened to the guy that came after Connor? I wasn't paying attention."
                                                            t "I don't know, he probably died, don't care."
                                                            y "I care..."
                                                            t "SSSHHHHH!"
                                                            d "THAT LOOKED LIKE IT HURT."
                                                            d "I'M SURE HE'LL BE ALRIGHT, NO NEED TO MAKE A FUSS."
                                                            a "STILL, MIGHT HAVE TO ASK FOR SOME PULLED PUNCHES FROM OUR LEADER COLLEAGUE."
                                                            m "Sorry..."
                                                            d "{i}*COUGH COUGH*{/i}"
                                                            d "W-WE'LL CONTINUE WITH THE NEXT FIRST YEAR."
                                                            a "EVERYBODY WELCOME OUR LOCAL TROUBLEMAKER, TATE."
                                                            hide cat21spark
                                                            show cat21mad2
                                                            stop music fadeout 3.0
                                                            t "Damn it Aiden."
                                                            t "He didn't use the name I gave him."
                                                            hide cat21mad2
                                                            show cat20smug


                                                            t "No matter, I'll show Merina."
                                                            t "I'm so gonna win."
                                                            y ec"Good luck!"
                                                            hide cat20smug with moveoutright


                                                            jump tatefight





                                                "Stay here with Tate.":
                                                    label nomerinaoliver:
                                                    scene arena2
                                                    show cat21simple with dissolve
                                                    "In the end, I decide to take a seat by Tate and ignore any other distractions, after all, it's him I want to spend my day with."
                                                    "He turns his head towards Merina and Ollie, then to me."
                                                    t "Huh, how come you're not even going over there to say hi?"
                                                    y simple"Oh, I probably should, shouldn't I?"
                                                    y "Just to be polite."
                                                    hide cat21simple
                                                    show cat21smile with hpunch
                                                    t "Nope nope nope, NOPE."
                                                    "He grabs my arm as I'm about to get up."
                                                    t "You're good, this is good."
                                                    hide cat21smile
                                                    show cat21smug
                                                    t "You don't always have to kiss everyone's ass, not literally, not figuratively."
                                                    y smug"You just want me for yourself."
                                                    t "Bold of you to assume that, did the confidence demon strike you?"
                                                    y "Are you saying it's not true?"
                                                    t "Hmm."
                                                    t "No comment."
                                                    hide cat21smug
                                                    show cat21smile
                                                    t "Meh, who am I kidding, yes, I want you for myself."
                                                    "He holds my arm even harder, resting his head on my shoulder and intentionally purring."
                                                    "HE'S SO CUTE I WANNA EAT HIM!"
                                                    un tease"FINALLY, LET'S DO IT!"
                                                    "Figure of speech, Scribbles."
                                                    un bored"Ah."
                                                    un sidee"Yes, I knew that, me too."
                                                    un squint"You little... cutie pie."
                                                    "You said that last part like it hurt."
                                                    un bored"Shut up."

                                                    "Although I decided not to leave Tate, I will also not miss out on my leader and vice leader's greetings."
                                                    "They spotted us and are making their way over."
                                                    "Everyone gets out of Merina's way, turning their heads as she passes, Ollie right behind, having a hard try not to be hit by her thick tail."
                                                    show merina20 at right with moveinright
                                                    show ollie2smile at left with moveinleft
                                                    hide cat21smile
                                                    show cat20simple
                                                    m "Hey boys."
                                                    o "Hi."
                                                    hide cat20simple
                                                    show cat20bored
                                                    t "Whatever you're selling, we ain't buyn'."
                                                    y angry"Tate! Be nice."
                                                    y ec"Hey guys, nice to see you."
                                                    hide merina20
                                                    show merina20sadsmile at right

                                                    m "I see my long time friend got a taste of new friendship and freedom, and decided to start acting up."
                                                    m "How's your magic level?"

                                                    t "We had an unfortunate Nightfallen encounter, and I had to teleport here with [name], but I'm more than ready for whatever challenge you throw at us."

                                                    m "I hope that's true."
                                                    hide merina20sadsmile
                                                    show merina20 at right
                                                    m "Come on Ollie, let's get ready for when the REAL fun begins."
                                                    o "After you, m'lady."

                                                    m "Good luck, boys."
                                                    o "G-good luck, [name], uhm, Tate."
                                                    t "Yeah yeah."

                                                    y "Thank you!"
                                                    hide ollie2smile with moveoutright
                                                    hide merina20 with moveoutright

                                                    "They walk towards the back rooms, turning more heads from the crowd along the way."

                                                    t "Can't get a minute alone around here."
                                                    y smug"Isn't that just called having friends?"

                                                    hide cat20bored
                                                    show cat20smug

                                                    t "Friends are always fake, ready to betray you at any moment."
                                                    y simple"I don't think that's true..."

                                                    t "I'm a lone wolf."
                                                    t "All I need is a mate."
                                                    show cat20wink with dissolve
                                                    hide cat20wink with dissolve

                                                    "He winks at me."
                                                    show cat20wink with dissolve
                                                    hide cat20wink with dissolve
                                                    "And again."
                                                    show cat20wink with dissolve
                                                    hide cat20wink with dissolve
                                                    "And again."
                                                    y simple"I think you have something in your eye."
                                                    hide cat20smug
                                                    show cat21wink
                                                    t "I think so too, actually..."

                                                    t "Damn it."

                                                    y simple"Need help?"
                                                    t "N-no, I think I..."
                                                    hide cat21wink
                                                    show cat21smile1
                                                    t "There, gone."


                                                    t "Hey, you have Aiden's number, right?"

                                                    y "Yeah, why?"


                                                    t "Can you send him a message? Tell him to present me as {i}'Nox'{/i} when the time comes."
                                                    t "It's my new stage name I'm trying out."

                                                    y "Isn't that a girl's name?"
                                                    hide cat21smile1
                                                    show cat20angry

                                                    t "Nuh-uh."
                                                    t "It's a cool, unisex name."
                                                    hide cat20angry
                                                    show cat20smug

                                                    t "It means {i}'Thing of Nightmares'{/i}!"

                                                    y "I think it just means {i}'Night'{/i} actually."

                                                    hide cat20smug
                                                    show cat21bored

                                                    t "Ah, I forgot you're a nerd."
                                                    t "Still a cool name."

                                                    "I find Aiden's contact at the top of the list, and write Tate's name change request."
                                                    "He sees it almost instantly, and responds:"
                                                    a "{i}No.{/i}"
                                                    y pf"hmmmm...."
                                                    hide cat21bored
                                                    show cat20
                                                    t "Oh, did he respond? What did he say?"

                                                    "I shut off my phone and stuff it in my pocket."
                                                    y "He said... if he doesn't forget."

                                                    t "Great!"
                                                    t "Aiden has a pretty good memory."
                                                    t "Somehow he just can't forget the haircut I gave him when he was eighteen."

                                                    y simple"Was it that bad?"
                                                    hide cat20
                                                    show cat20simple

                                                    t "Bald."

                                                    y "oh."

                                                    y pf"Yeah, I can see why."

                                                    d "GOOD AFTERNOON LADIES AND GENTLEMEN."
                                                    d "WELCOME TO THIS YEAR'S PRACTICE SESSION!"
                                                    play sound "audio/cheering.ogg"
                                                    "Our conversation is cut by Dallan's loud voice, cheers erupted throughout the place, and he continues once those die down."
                                                    t "Is that... the Headmaster over there?"
                                                    t "Oh right, he's watching us this year, I forgot."

                                                    d "YOU MIGHT BE HAPPY, OR SURPRISED TO FIND OUT WE'VE MADE SOME SMALL CHANGES TO THIS PARTICULAR SESSION."
                                                    d "FIRST AND FOREMOST, I'D LIKE TO PRESENT TO YOU, HEADMASTER ARGUS, WHO WILL BE WATCHING OVER AND ASSESSING THE STUDENTS."
                                                    h "GOOD AFTERNOON EVERYONE, I TRUST WE'LL HAVE A FAIR AND ENTERTAINING PRACTICE SESSION, I'M LOOKING FORWARD TO SEEING THE AMAZING TALENTS THIS ACADEMY HAS TO OFFER."

                                                    play sound "audio/crowdnoisee.ogg" volume 0.8
                                                    "Murmurs of confusion and protest can be heard following that statement."
                                                    hide cat20simple
                                                    show cat20angry

                                                    t "Damn right, we should riot over this!"
                                                    y "What's so bad about it?"
                                                    t "Practice sessions were always for us, the students!"
                                                    hide cat20angry
                                                    show cat20simple

                                                    t "Mister Sebil came by sometime, but always stood in the crowd with us."
                                                    "Noticing the discomfort created, Aiden intervenes."
                                                    stop sound fadeout 2.0



                                                    a "OF COURSE, HIS PRESENCE HERE IS PURELY PERSONAL."
                                                    a "YOUR PERFORMANCE TODAY WILL NOT AFFECT YOUR GRADES OR OVERALL YEARLY PERFORMANCE."
                                                    d "Y-YES, THAT'S RIGHT, THANK YOU AIDEN."
                                                    d "AS FOR THE SECOND SMALL BUT EXCITING CHANGE:"
                                                    d"BEFORE THE REGULAR PRACTICE STARTS, THE FIRST YEARS OF THE SORCERY AND SUMMONING SHARDS WILL HOLD THEIR AUDITIONS IN FRONT OF EVERYONE, INSTEAD OF IT BEING A PRIVATE SHOWCASE LIKE USUAL."
                                                    y "So the summoners will audition too?"
                                                    t "I think they're going first too."
                                                    t "Their audition should be a bit different than ours."
                                                    y "Different how?"
                                                    stop music fadeout 2.0

                                                    t "Summoners have to show their summoner abilities, which are never very impressive."
                                                    t "Unlike us, where we have to prove we actually have some fire power, or defensive abilities, or utility, stuff like that."

                                                    play music "audio/fight.ogg" fadein 2.0
                                                    d "LET US START WITH THE FIRST AUDITION PARTICIPANT IN THE LIST."

                                                    d "WITHOUT FURTHER ADO, AIDEN, IF YOU MAY."

                                                    a "AGHEM, PLEASE GIVE IT UP FOR, ALVY, AUDITIONING FOR THE SUMMONERS."
                                                    "The crowd cheers as a small but clearly confident dog with a neutral, unimpressed expression makes his way in front of the arena."
                                                    d "THIS YEAR'S OPPONENTS WILL BE SOME CLEVERLY DESIGNED SNAKE DUMMIES, CONSTRUCTED BY NONE OTHER THAN THE DEFENDER'S VICE LEADER, CHELSIE!"
                                                    d "SHE IS ALSO LOOKING FOR A NEW WORK ASSISTANT, IF YOU'RE INTO INVENTIONS AND ARE WILLING TO WORK FOR A MINIMUM AMOUNT, GIVE HER A CALL!"
                                                    d "YOU MUST ALSO BE OKAY WITH THE FOLLOWING POSSIBLE CASUALTIES, AND PLEASE KNOW THAT SHE IS NOT RESPONSIBLE FOR ANY HARM THAT WILL COME TO YOU, SUCH AS:"
                                                    d"FIRE BURNS, ACID BURNS, FRICTION BURNS, HEAD TRAUMA, LOSS OF LIMBS, LOSS OF TEETH, LOSS OF FUR, FROSTBITE...this list is long..."
                                                    "I try to ignore Dallan's extensive list, and focus instead on the last recommended student I haven't personally met yet."
                                                    "He is faced with the dummy, that is way more intimidating when there's a regular person to compare its size with."
                                                    "It has canons attached to it, as well as saws and rotating blades, not to mention that armor that looks pretty sturdy."
                                                    "He takes out a small handful of crystals, varied in size, from which a dozen Nightfallen spawn."
                                                    "All of them, except for two wolf-like creatures, rush towards the dummy."
                                                    "The dummy senses the danger it's in, so before dealing with the attacking foes, it shoots its cannons towards the summoner, Alvy."
                                                    "But the wolves at his side protect him with no problem."
                                                    "In seconds, the other Nightfallen, less animalistic in nature, destroy, disassemble and even start devouring the dummy, leaving only scraps behind."
                                                    y "He has impressive summon abilities for a first year."
                                                    t "He wasn't recommended for nothing."
                                                    un squint"God... why couldn't {i}HE{/i} find my room first?"
                                                    un "I bet I could've been summoned in a matter of days."
                                                    "I doubt anyone but me would've accepted your proposition..."
                                                    "I was desperate."
                                                    un bored"Touche."
                                                    stop music fadeout 3.0

                                                    y s"I didn't get the chance to meet him yet, maybe I can catch him when he gets to his seat."
                                                    t "I don't think you'll be able to do that."
                                                    y simple"Why not?"
                                                    "I look at Alvy, focusing on his path so I can follow him to his spot in the crowd, but after a couple of steps, he turns into blue smoke and fades from reality."
                                                    y worried"What the-"
                                                    t "Yeah... another freak."
                                                    t "You really are the only normal one of the recommended ones."
                                                    play music "audio/casual3.ogg"
                                                    y simple"Thanks?"
                                                    y "Do you think he teleported away?"
                                                    t "No, that's not teleportation, it's some form of invisibility."
                                                    t "Or whatever else."
                                                    y "Maybe he's just shy."
                                                    "The combat is done, but Dallan isn't with the list of risks you take by being Chelsie's assistant..."
                                                    d "LOSS OF VISION, LOSS OF TASTE, ERECTILE DYSFUNCTION, PRIAPISM AND LAST BUT NOT LEAST, MINOR DEATH."
                                                    y confused"{i}'Minor'{/i}?"
                                                    d "BACK TO THE AUDITIONS, WOW, WHAT A DISPLAY THAT WAS, TOO BAD OUR FRIEND DIDN'T STICK AROUND TO SEE THE RESULTS, WHICH WILL BE PRESENTED SHORTLY, AS SOON AS THEIR LEADER AND VICE LEADER COME TO A DECISION."
                                                    "Aiden presented the other people while Dallan offered some commentary."
                                                    "Chelsie tried to break into the announcements cabin, in complete disregard of the Headmaster's presence, to try to shout what I'd call basically IRL ads in the mic."
                                                    "As if Dallan's announcements she gave him weren't enough..."
                                                    "Their struggles to contain her were clearly audible, and while the Headmaster was slightly annoyed, the crowd loved the chaos, especially when Aiden shushed his complaints."
                                                    "All of this was great in retrospect, since the other summoners weren't nearly as flashy as the recommended student."
                                                    "Obviously, since a summoner is not even expecting to be able to actually summon Nightfallen on their first day, so I wonder if and how their audition is graded."

                                                    y s"Imagine if Chelsie had your teleportation abilities."
                                                    t "The world would not be safe."
                                                    t "She's also the only one somewhat entertaining right now..."

                                                    y simple"Yeah..."
                                                    y "I thought it would be a bit more interesting than this."

                                                    t "We shouldn't have hurried."
                                                    y "What if we missed our auditions?"
                                                    hide cat20simple
                                                    show cat20bored
                                                    t "At this rate, it would've been worth it."

                                                    "Another summoning demonstration goes by, another guy that looks like he's about to puke..."

                                                    y bored"{i}*sigh*{/i}"
                                                    y "I'll go get us a snack, popcorn?"
                                                    hide cat20bored
                                                    show cat20surprised

                                                    t "Huh, wha-"
                                                    hide cat20surprised
                                                    show cat20smugclose with hpunch
                                                    stop music
                                                    play sound "audio/button.ogg"
                                                    "I stand up to go to a snack booth or something, but my arm is being caught in what feels like a bear trap."
                                                    play sound "audio/button.ogg"
                                                    t "Huehuehue."
                                                    play sound "audio/button.ogg"
                                                    t "You just want to get your mind out of this hell of boredom."
                                                    play sound "audio/button.ogg"
                                                    t "And leave to do literally anything else."
                                                    play sound "audio/button.ogg"
                                                    y awkward"N-not true, I just want you to have something to munch on."
                                                    play sound "audio/button.ogg"

                                                    t "Who said anything about a snack? I don't want a snack, so sit your ass down."
                                                    play sound "audio/button.ogg"
                                                    y "Maybe {b}I{/b} want a snack."
                                                    play sound "audio/button.ogg"
                                                    t "We both just came from breakfast, I know you don't want no damn snack."
                                                    play sound "audio/button.ogg"
                                                    y "I want to use the bathroom."
                                                    play sound "audio/button.ogg"
                                                    t "What if you miss our auditions in the meantime?"
                                                    play sound "audio/button.ogg"
                                                    y "..."
                                                    hide cat20smugclose with hpunch
                                                    "I use all my strength to pull my hand free, and with the element of surprise on my side, I manage to do just that, and just book it."
                                                    play sound "audio/thud.ogg"
                                                    "Unfortunately, I didn't think the cat would be desperate enough to jump on me."
                                                    hide cat20smugclose
                                                    show cat21cry with hpunch
                                                    play sound "audio/wack.ogg"
                                                    play music "audio/funny.ogg" volume 0.3

                                                    t "PLEASE DON'T LEAVE ME HERE ALONE!"
                                                    t"If I watch another first year blowing smoke out of a gem and having to act impressed I'mgonnaloosemyfuckingmiiiiind."
                                                    "The commotion made by our arguing and wrestling on the ground is proven more entertaining than the arena action, so we have dozens of eyes on us."
                                                    y scream"You think I don't need a break too?!" with hpunch
                                                    t "Then why can't you take me with you?!"with hpunch
                                                    y "That is a VERY good question, why can't I?"with hpunch
                                                    stop music
                                                    play sound "audio/button.ogg"
                                                    t "..."
                                                    show cat21simple with dissolve
                                                    hide cat21cry
                                                    play sound "audio/button.ogg"

                                                    y simple"..."
                                                    play sound "audio/button.ogg"
                                                    "We stop fighting, and Tate slowly gets off helping me up as well."
                                                    play sound "audio/button.ogg"
                                                    y pf"{i}*lip smack*{/i}."
                                                    play sound "audio/button.ogg"
                                                    y "We're dumb as hell."
                                                    hide cat21simple
                                                    show cat21bored
                                                    t "Yep."
                                                    play sound "audio/button.ogg"
                                                    y s"Wanna grab a snack?"
                                                    play sound "audio/button.ogg"
                                                    hide cat21bored
                                                    show cat20ec
                                                    t "Yep."
                                                    play sound "audio/button.ogg"
                                                    scene black with dissolve
                                                    "The prying eyes seem a tad disappointed that our tussling stopped."

                                                    scene lobby with dissolve
                                                    play music "audio/jazz20.ogg"

                                                    "We walk into the backrooms, which might've been a mistake, since me and Tate end up devouring half the sweets in the self serving zone."
                                                    show cat20smug with moveinleft
                                                    t "I mean, do you see anyone around telling us no?"
                                                    y simple"There's a sign saying {i}'only three items per person'{/i}."
                                                    t "It's a sign, not a cop."
                                                    y s"Can't argue with that logic."
                                                    hide cat20smug with moveoutright

                                                    "We continue to take advantage of the scarce amount of people through the corridors to create chaos."
                                                    "Where did Tate pull out two pairs of roller skates?"
                                                    "I have no idea, but boy are these wacky shoes fun to play tag on."
                                                    "Thankfully I convinced Tate to take them off when going to the bathroom at least."
                                                    scene black with dissolve
                                                    stop music fadeout 3.0
                                                    "We end our backroom adventure with a small cup of coffee, just in case we go back and those summoners are still at it with their mediocrity."

                                                    scene arena2 with longdissolve
                                                    show cat20ec with moveinleft
                                                    t "Phew, that should be enough to keep me energized throughout this whole ordeal."
                                                    y ec"No kidding, my mind is so clear, I can stuff in ten, no, twenty boring auditions in here."
                                                    hide cat20ec
                                                    show cat21smug
                                                    play music "audio/purplecat.ogg"
                                                    t "Thaaat might not be necessary, look."

                                                    "The center of the arena is quiet, and not because some first year can't do their weak summons, but because there's nobody there."
                                                    "We wait for another minute, still nobody."
                                                    t "You know what that means?"
                                                    y smug"I think I do."

                                                    d "WHAT A...UHMM, INTERESTING AUDITION SESSION PROVIDED BY THE SUMMONERS!"
                                                    d "BOY AM I SAD IT'S ALREADY OVER, ISN'T THAT RIGHT, AIDEN?"
                                                    a "{i}*snooooore*{/i}"
                                                    a "Huh, Wha-"
                                                    a "Are they finally done?"
                                                    a "Good riddance."
                                                    d "MOOOVING ON, IT IS TIME FOR THE SECOND AUDITION SESSION, THIS TIME, FOR THE NEW SORCERERS OF THE YEAR!"
                                                    "People all around groan intensely, clearly done with auditions."
                                                    t "Heh, suckers, they don't know this part is actually fun to watch."
                                                    d "THIS YEAR'S TASK WILL BE EXPLAINED BY THE SHARD'S VICE, OLIVER, TO EACH PARTICULAR PARTICIPANT IN PRIVATE BEFORE THEIR MATCH!"
                                                    a "THAT IS A DUMBASS RULE."
                                                    a "{i}Oops, didn't mean to say that to the speaker.{/i}"
                                                    a "WITHOUT FURTHER ADO, LET'S WELCOME OUR FIRST STUDENT IN THE ARENA."
                                                    stop music
                                                    a"CONNOR."
                                                    hide cat21smug
                                                    show cat21simple
                                                    play music "audio/fight.ogg"


                                                    y confused"Connor?"
                                                    t "Is that the guy who stole our table in the morning?"
                                                    "A German Shepherd wearing a red vest walks casually in the ring."
                                                    y bored"Yep."
                                                    y "The very same."
                                                    a "YOU'RE A BITCH, CONNOR."
                                                    "The dog looks up at the announcement tower with a 'are you serious?' expression on his face, along with other confused audience members."
                                                    t "We're not the only ones that recognized him."

                                                    t "Let's see what kind of dummy he'll have to face."
                                                    y confused"Huh, what is she doing there?"
                                                    hide cat21simple
                                                    show cat20worried

                                                    t "Oh no..."
                                                    t "No no no."
                                                    t "Don't tell me."

                                                    "From the other side of the ring, the figure of a tall, gracious white fox comes into view confidently."
                                                    y surprised"He'll have to fight... Merina?"

                                                    "What the hell?!"

                                                    t "I'm not sure if I should laugh, cry or get mad."

                                                    y awkward"Let's wait and see, maybe she's there to wish him good luck?"
                                                    play sound "audio/bell.ogg"
                                                    "The bell rings, and I can say for sure now, it is not a good luck encounter."
                                                    "I can't quite describe what I'm seeing, since everything is a blur, or more like a blizzard."
                                                    "Merina's magic envelops the arena, and she concentrates different attacks, from long range to close, from projectiles to trickery."
                                                    "Connor is hanging in pretty strong, using a diverse set of spells as well, but in the end, two minutes is all he could muster."
                                                    "Leaving the woman disappointed, but victorious."
                                                    "Still, the crowd cheers for him."
                                                    hide cat20worried
                                                    show cat20simple
                                                    stop music fadeout 3.0

                                                    "Dallan and Aiden present the next contestant, while Merina resumes her initial position and makes all the extra ice she created in the battle disappear."
                                                    play music "audio/jazz5.ogg" fadein 1.0 volume 0.5
                                                    "As for me and Tate, we get a little guest waddling over to us."
                                                    show ollie2smile at left with moveinleft
                                                    y s"Oliver, hey!"
                                                    o "H-hey you two, I'm here to-"
                                                    hide cat20simple
                                                    show cat21mad2 with hpunch
                                                    hide ollie2smile
                                                    show ollie2simple at left
                                                    t "You little double crossing, disloyal little shit!"
                                                    o "Uhm, what?"
                                                    show cat21mad2 at left2 with move
                                                    show ollie2simple at left5 with move
                                                    t "You told me it was going to be a hologram of a metal dummy!"
                                                    t "You EVEN told me how to defeat it!"
                                                    hide ollie2simple
                                                    show ollie2go at left5
                                                    o "I-I couldn't tell you the truth!"
                                                    y simple"When did you even get the opportunity to ask?"
                                                    y "He's always around Merina."

                                                    t "I went to his dorm last night."
                                                    hide ollie2go
                                                    show ollie2 at left5
                                                    o "And he wouldn't leave until I told him something..."

                                                    t "Can't believe you'd betray me like that."

                                                    o "It's against the rules!"
                                                    t "Oh yeah?"
                                                    t "Is this against the rules too?"
                                                    show cat21mad2 at left5 with move
                                                    hide ollie2
                                                    show ollie2sidee with hpunch
                                                    "Tate picks the little mouse up with very little effort."
                                                    o "I-I AM PRETTY SURE IT IS!"
                                                    y angry"TATE!"
                                                    y pf"You put your vice leader down or I'm not hanging out with you anymore."
                                                    un suspicious"W-where..."
                                                    un squint"Where are his legs...?"
                                                    un squint"What...?"
                                                    hide ollie2sidee with dissolve

                                                    show ollie2 at left5 with dissolve
                                                    show cat21mad2 at right2 with ease
                                                    show cat21bored at right2
                                                    hide cat21mad2

                                                    t "..."
                                                    t "{i}*sigh*{/i} I overreacted."
                                                    t "I'm sorry."
                                                    show ollie2 at left with ease
                                                    o "I'll forget all about it by next week."

                                                    y simple"So, you came here to explain the rules?"
                                                    o "Y-yes, Tate will be the next one after the guy fighting now."
                                                    hide cat21bored
                                                    show cat21smug at right2
                                                    show cat21smug at center with move

                                                    t "Neat."
                                                    t "I'm all ears, hurry up."
                                                    o "ermm..."
                                                    o "This needs to be a one on one conversation."
                                                    o "[name], do you mind?"
                                                    t "Yes, he does mind."
                                                    y smug"I'm not going anywhere."
                                                    o "I-I can't-"
                                                    hide cat21smug
                                                    show cat21bored
                                                    t "Do it or I'll unalphabetize your potion ingredients."
                                                    hide ollie2
                                                    show ollie2side2 at left
                                                    "Oliver visibly cringes and recoils at the thought, and reluctantly starts talking."
                                                    hide ollie2side2
                                                    show ollie2 at left
                                                    o "Merina will fight you, to test your abilities."
                                                    y simple"That's pretty obvious at this point."
                                                    o "She will be holding back, depending on your abilities."
                                                    o "If you're a close attacker she will use close proximity spells and for range, same principle."
                                                    o "In short, she'll adapt based on her knowledge about your abilities and the way you fight in there."
                                                    y "Seems reasonable enough, at least we won't have to fight a leader at full power."
                                                    t "But how do we win?"
                                                    o "It's not likely you can win against her, but to pass the auditions, you simply have to... not look pathetic, and demonstrate as many abilities as you can."
                                                    hide cat21bored
                                                    show cat21smile1
                                                    t "Great!"
                                                    t "So what technique will she use against me?"
                                                    o "I don't know."
                                                    hide cat21smile1
                                                    show cat21mad2
                                                    "Tate gives him a sharp stare through squinted eyes."
                                                    hide ollie2
                                                    show ollie2go at left
                                                    o "I-I'm telling the truth! She didn't tell anyone! Not even me!"
                                                    y simple"Is this an unconventional way of conducting the auditions?"
                                                    t "Very."
                                                    y "Then why?"
                                                    hide ollie2go
                                                    show ollie2 at left
                                                    o "The Headmaster is watching, as well as the whole academy, so she wanted something a bit more special."
                                                    o "Although, just between us, I believe today first years will have an easier time passing, since she said she will take pity on them."
                                                    o "Mostly because the Headmaster is watching."
                                                    "That's reassuring."
                                                    y "Why am I not supposed to know this until my time comes?"
                                                    o "Merina wants students to adapt on the spot, instead of making some kind of plan against her, since, again, you don't have to win, just present your abilities."

                                                    hide cat21mad2
                                                    show cat21smile1

                                                    y "Got it, a showcase."

                                                    un squint"But...the legs...where?"
                                                    hide cat21smile1
                                                    show cat21spark with hpunch

                                                    "Tate suddenly grabs my arm and shoulder and shakes me vigorously."
                                                    t "They're done they're done they're done!"
                                                    t "It's my turn!"
                                                    y confused"Huh, what happened to the other guy? I wasn't paying attention?"
                                                    t "I don't know, he probably died, don't care."
                                                    y worried"I care..."
                                                    t "SSSHHHHH!"
                                                    d "I'M SURE HE'LL BE ALRIGHT, NO NEED TO MAKE A FUSS."

                                                    a "STILL, MIGHT HAVE TO ASK FOR SOME PULLED PUNCHES FROM OUR LEADER COLLEAGUE."
                                                    m "Sorry..."
                                                    d "{i}*COUGH COUGH*{/i}"
                                                    d "W-WE'LL CONTINUE WITH THE NEXT FIRST YEAR."
                                                    a "WELCOME OUR LOCAL TROUBLEMAKER, TATE."
                                                    hide cat21spark
                                                    show cat20angry
                                                    t "Damn it Aiden."
                                                    t "He didn't remember the name I gave him."
                                                    hide cat20angry
                                                    show cat20smug
                                                    stop music fadeout 2.0


                                                    t "No matter, I'll show Merina..."
                                                    y ec"Good luck!"


                                                    jump tatefight


                                                    label tatefight:
                                                    scene black with llongdissolve
                                                    play music "audio/fight.ogg" volume 0.6
                                                    pause 1.5

                                                    scene tatepractice with dissolve
                                                    scene CGc9


                                                    "We watch Tate jump in the arena pit, confidence oozing out of him."
                                                    "Before the bell even rings, he starts walking towards Merina, slowly, menacingly."
                                                    "Magic particles appearing around him."
                                                    "Something about that feels familiar..."
                                                    "Merina seems to get ready as well, this time, a bit more serious than she was with the previous guys."
                                                    "She's not allowed to move until the match officially starts, but nobody seems to have a problem with Tate doing so."
                                                    "Probably because Merina can easily fold him like an omelet as soon as the bell rings..."
                                                    "Does he actually think he can win against a leader?"

                                                    un "Absolutely not."

                                                    "You're certainly right."
                                                    "Although, why are you so confident?"

                                                    un "I can feel the magic coming from her, that woman is on a completely different level."
                                                    un "As far as I understand, she's an ice witch, you know how powerful you have to be in a single element to give off that much power?"

                                                    "Very?"

                                                    un "Very."
                                                    un "Now let's watch the confidence melt away."
                                                    play sound "audio/bell.ogg"

                                                    "The bell rings."

                                                    "Merina doesn't move a muscle still."
                                                    "She stands in a proper, innocent position, her hands kept down, only moving to keep her balance."
                                                    "Tate on the other hand, wastes no time, instantly teleporting next to her, fingers trying to touch the fox's smooth fur."
                                                    "For a moment it looked like it was game over, after all, she doesn't have a teleportation canceling ability, considering she allowed Tate to do it in the first place."
                                                    "And all it takes is a touch for her to be thrown out of the arena."
                                                    "The winning grin was already on the cat's face."
                                                    "How unfortunate he is..."
                                                    "A small chunk of ice forms between his finger and her fur, millimeters thin, but enough to protect her from his touch."
                                                    "The ice gets transported in her stead, falling on Ollie's head, shattering easily on impact."

                                                    o "Ouch."
                                                    "That was supposed to be Merina's body if his touch connected..."
                                                    "You're playing dirty, gatito."

                                                    m "The oldest trick in the book."
                                                    m "You'll have to think of something else."

                                                    "Each match has some slightly different rules and limitations for Merina, as Oliver explained."
                                                    "Tate teleports away, avoiding an icicle erupting from the ground."
                                                    "Seeing how his plan failed, he keeps his distance, and walks in circles around her, trying to find a new idea for attack."
                                                    "All the while, more icicles, pillars of ice and snow forms on the ground under his feet, which he has to dodge."
                                                    "Since the fight started, Merina has not moved, not her posture, not her hands, only her eyes."
                                                    y simple"I think I understand."
                                                    o "Oh?"
                                                    y "Here, she can only use spells on the ground itself, no projectiles or area of effect, such as blizzards, and she can not move, meaning all her spells are cast with her mind alone."
                                                    o "You caught on very fast."
                                                    o "But you forgot about protection."
                                                    y "Right, she did create that thin barrier."
                                                    y surprised"I wonder if Tate will- !"
                                                    "I don't get to finish my words, and the cat takes notice of the same pattern I did, and summons his broom."
                                                    "He is now out of harm's way, at least twenty feet off the ground, nice thinking!"
                                                    "But how will he touch her from all the way over there?"

                                                    "Another one of my questions was quickly answered by his next move."

                                                    "He conjures multiple magic balls, which he carries with him as he flies towards the static fox."
                                                    "She blocks each ball with a pillar of ice, she thought that was it, except she forgot about Tate himself..."
                                                    "The cat, in a drive-by attempt, flies past Merina, extending his arm..."
                                                    "But he gets engulfed in snow, which slows his momentum before turning into ice."
                                                    "The ice shatters a moment later, knocking him to the ground."
                                                    scene tatepractice22 with dissolve

                                                    stop music fadeout 4.0

                                                    m "Impressive, you were actually pretty close to touching me."
                                                    m "I would be less cautious if I didn't know what that means, so if I were a Nightfallen, victory would already be yours."

                                                    "The cat lies on the ground for a moment longer, contemplating whether or not it's worth to continue fighting, but it's clear his hand won't reach her fur, and although he can levitate off the ground and be safe from most of her attacks, in the end it would just waste time."
                                                    t "I ought to take the compliment and leave, right?"
                                                    m "You? Seeing reason and accepting defeat?"
                                                    t "If I understood the rules well enough, this is not a defeat, is it?"
                                                    "He gets up with a subtle smile on his face, which Merina matches."
                                                    m "Consider me impressed."
                                                    m "You may go."
                                                    play sound "audio/cheering.ogg"


                                                    "The crowd goes wild as they bow to each other for the last time, and he leaves the ring."

                                                    "Maybe he didn't win, but he sure was awesome."
                                                    play music "audio/purplecat.ogg" fadein 3.0

                                                    scene arena2 with fade
                                                    show ollie2smile at left

                                                    "He runs up to me, toppling a couple of people over in the process... sorry."
                                                    show cat20smug with moveinright
                                                    "Before he can ask anything, I can tell his toothy smile is just begging for a compliment."
                                                    y ec"You were awesome!"
                                                    t "Yeaaah, I was~"

                                                    y ec"So dynamic, so fast, so smart!"
                                                    hide cat20smug
                                                    show cat21blush3
                                                    t "Stooop, you're making me blush."
                                                    o "It was quite impressive."
                                                    o "I can say right now, you won at least one vote from me."
                                                    hide cat21blush3
                                                    show cat20
                                                    t "Heck yeah!"

                                                    t "Hey, [name]?"
                                                    t "Can I ask a favor of you?"
                                                    y s"What is it?"
                                                    hide cat20
                                                    show cat20smile
                                                    t "It's a weird one, but..."
                                                    t "Go easy on Merina, she's obviously holding back, but a recommended student that doesn't know that might go overboard by accident."
                                                    y awkward"O-of course, easy...me... sure."
                                                    t "Thanks."
                                                    "I wish was so strong I had to go easy on a leader..."

                                                    "Dallan's voice cuts our conversation off, time for the next first year."

                                                    d "A SHOW TO REMEMBER, ISN'T THAT RIGHT, MISTER ARGUS?"

                                                    "He remains unmoving and emotionless."
                                                    d "RIGHT, AIDEN?"
                                                    a "NEXT ON THE LIST."
                                                    d "SURE, EVERYONE JUST IGNORE ME, I'M OKAY WITH THIS."

                                                    a "WE'RE SKIPPING A FIRST YEAR FOR MEDICAL REASONS, AND JUMP STRAIGHT TO THE NEXT ONE, [NAME] [NAME2]!"
                                                    a "EVERYBODY CHEER."
                                                    a "THIS IS A THREAT."
                                                    play sound "audio/cheering.ogg"
                                                    stop music fadeout 3.0

                                                    "I'm glad Aiden goes above and beyond to make me feel good, but God fucking damn it, MEDICAL REASONS?!"
                                                    "Seriously?"
                                                    "Why am I not surprised the world fucks me over?"
                                                    hide cat20
                                                    show cat20ec

                                                    t "WOOOOOOO!"
                                                    t "GOOD LUCK!"

                                                    y awkward"Thanks..."
                                                    scene tatepractice2 with dissolve
                                                    play music "audio/fight.ogg" fadein 3.0


                                                    "There's no going back, so I jump inside with basically no plans, just as Merina wanted..."

                                                    y worried"Oh boy..."
                                                    y "Do I... have a plan?"
                                                    y "Do I have any idea what I'll do?"

                                                    "Scribbles..."
                                                    "Scribbles I'm panicking."
                                                    "I'm gonna have a heart attack."
                                                    "I only now realize how much trouble I'm in."

                                                    un curious"Why?"
                                                    un "You have one of the most powerful, useful and versatile magic techniques out there!"

                                                    "I can't use shit, alright?!"

                                                    "All I can do is charge my phone, something I haven't even told anyone, since I don't want them to treat me like a living charger."
                                                    "And I can make some energy balls."

                                                    "Also shock people if I touch them, that's it."


                                                    un squint"Fuuuuuuuck, what did I get myself into..."
                                                    un "I had a feeling you'll end up being a weakling."
                                                    un "The amount of energy in this body is too low to be as powerful as I was hoping..."
                                                    un eyeroll"Fine, I'll make it look like you're doing shit."
                                                    un bored"But I'm not an energy manipulation user, so hopefully nobody realizes I'm actually using lightning."

                                                    "Yes, that works!"

                                                    un "One condition."
                                                    "Anything!"

                                                    un "You go there and show me what you can do on your own, when I see you're struggling or embarrassing yourself above the average norm, I'll come in clutch."

                                                    "Not a fan of this plan..."

                                                    un ang"If you want my help, this is what I'm willing to pitch in."
                                                    un "Now do you accept my offer?"
                                                    un bored"If you don't, I'm not able to cast any spells."

                                                    "Yes, yes, fine, as long as I pass."
                                                    "I let you cast any spells you want once we start."

                                                    play sound "audio/bell.ogg"

                                                    "With those final words, the bell rings."
                                                    "I was expecting Merina to stand still and wait for me to make the first move, the same way she did with Tate."
                                                    "..."
                                                    "I could not be more wrong."

                                                    scene tatepractice3 with hpunch
                                                    scene CGc10
                                                    play sound "audio/blizzard.ogg"


                                                    "In an instant, Merina's smile fades, a powerful explosion erupting around her, creating a field of ice, in the shape of a flower, almost reaching my feet."
                                                    y angry"What the ACTUAL fuck?"

                                                    un tease"Ha haaa, she thinks you're strong, so she needs to be more serious."
                                                    y worried"I hope that's not the case."
                                                    y "First off, I need to find her limitations."

                                                    "She creates an ice rapier in her hand, it glows as if imbued with extra magic, a beautiful, yet deadly weapon."
                                                    "She dashes towards me, like a graceful skater on ice, except a regular skater doesn't move as fast as a military aircraft."
                                                    un "Let's see you dance, baby boy, the bomb is coming."

                                                    "Before I can show off any {i}'dance moves'{/i}, Merina approaches without a notice of slowing down."
                                                    "Her sword pointed directly at my chest."
                                                    "I already used my speed and strength enchantments, but those are not too useful when I'm struggling not to slip and fall."
                                                    "The only thing I manage to do on the now icy ground, is try to fall backwards to avoid the main attack, or try to stop her with my bare hands... but I'm not fast enough even for that."
                                                    "I can basically see my life flash before my eyes."
                                                    m "Huh?"
                                                    "Her head passes my terrified face, side eyeing my pitiful attempt at blocking, the serious expression turning into worry and confusion on her part."
                                                    "Seeing how I'm making no effort on dodging either, she shatters her own sword last second, before the tip touches my skin, continuing her attack with a bare hand."
                                                    "Her palm makes contact with my chest, pushing me backwards with the force of a bull, the shockwave from the impact making the snowflakes and sand particles around her dance in the air."

                                                    "Thankfully I managed to stop myself right before leaving the ring."

                                                    "Merina closes distance again, creating another ice sword in hand, but this time, she's slow enough that I can actually react."
                                                    "I dodge down as the blade scrapes the top of my ears."
                                                    "I quickly make my way in the center of the arena, just in case she decides to push me again with her unusually high strength."
                                                    "She lets me gain the distance I wanted, then turns around and runs again."

                                                    y hurt"Alright, gimmick number one, she uses melee attacks only, so far at least."

                                                    "After barely dodging the second attack, I quickly take off my shoes, for extra grip on the ice."

                                                    un simple"Good thinking!"
                                                    un bored"Now your feet can get frostbitten and fall off, making your death much faster!"
                                                    "The floor is not changing beside the first layer of ice she created, meaning she has no intention of pinning my feet down with ice, so Scribbles' sarcastic comments are not true."

                                                    "This time, I dodge the attack with more impressive acrobatics."
                                                    "The adrenaline was enough to make me do my first ever back handspring."
                                                    "I hope it looked as impressive as it felt."

                                                    un squint"Are you going to attack sometime today?"
                                                    un "You're supposed to show off your powers."

                                                    "I DON'T HAVE ANY USEFUL ONES!"
                                                    "SO HELP ME ALREADY!"

                                                    un eyeroll"Pathetic."
                                                    un "At least I now know you're not completely braindead on top of being weak."

                                                    un bored"Here, when she comes close, just place your hands on the ice."

                                                    "I do as he says."
                                                    "Merina comes closer at the same alarming speed she did at first, readying her sword."
                                                    "An electric current flows through my arms and into the ice below."
                                                    "Electric particles can be seen across the whole icy surface the next second, except for right under me."

                                                    "A spell like this would obviously be very easy for someone like her to either stop or avoid, but something about the rules of this match make her have to take the whole hit."
                                                    un simple"She probably can't raise her feet off the ice, or create more of it other than physical weapons."

                                                    "She falls to one knee."
                                                    "Is this my chance? I approach, with my guard still up, ready to touch her to perhaps make her faint with my electricity."
                                                    un bored"{b}MY{/b} electricity."
                                                    "Yes... Scribbles' electricity."

                                                    "Just ten feet away."
                                                    "Suddenly, she raises her hand, creates a spear, and impales me..."
                                                    "Instead of blood, the tip of the spear shatters on impact, exploding into a wave of ice that covers me whole, the same way it did to Tate earlier."

                                                    un bored"Can't believe you fell for it..."
                                                    un "Luckily, you gave me permission to help you for the whole match, so I can do this!"

                                                    "The ice starts to crack, precise electric bolts shooting from my body, setting me free."
                                                    "For the audience and my opponent, this process happened in less than a second."
                                                    "This time, taken by surprise, Merina didn't have enough time to create a sword, and not enough momentum to swing it as well, so I manage to touch her shoulder."
                                                    scene tatepractice33 with dissolve
                                                    stop music fadeout 4.0

                                                    "Time freezes, everyone, including me, stares in disbelief."

                                                    un "It's not THAT surprising, she was using what? Like, five percent of her power in this match?"

                                                    "Still, she gives a light chuckle and makes all the ice evaporate in thin air."

                                                    m "Nicely done, [name]."
                                                    m "If I knew about your electric powers, I might've been inclined to hold back even less."

                                                    y pf"That would not have been preferable."

                                                    m "What are you waiting for?"
                                                    m "Shock me, this way everyone will know for sure you won."

                                                    y simple"No."

                                                    m "Curious decision."
                                                    m "Why so?"

                                                    y s"You spared me earlier too."

                                                    m "Did I?"

                                                    y smug"You stopped your sword before it hit me, if you didn't, it would've been game over from the start."
                                                    y s"My chance of even showing off my powers would've been gone."
                                                    m "Heh, you caught on."
                                                    m "I admit, since I knew almost nothing about you, I decided to go hard from the first start."
                                                    m "I swear I didn't know speed was your weakness."
                                                    y awkward"Yes..speed, speed and only that."

                                                    "I take my hand off, and take two steps back."

                                                    play sound "audio/cheering.ogg"


                                                    "We bow to each other, and only then did the crowd dare start making noise, loud resounding cheers."
                                                    scene black with dissolve




                                                    "I turn back to my seat, a grin across my face, almost as wide as the cat's that was waiting for me."
                                                    "Boost of confidence achieved."
                                                    scene arena2 with dissolve
                                                    play music "audio/purplecat.ogg"

                                                    un curious"Why?"
                                                    un ang"You did basically nothing, that was ALL me!"
                                                    "You're part of me now, so we're a team!"
                                                    un "You do not get to own MY power!"
                                                    show cat20ec with moveinleft
                                                    t "Holy!"
                                                    t "You were amazing."
                                                    t "You actually did it!"
                                                    t "You got farther than I did!"
                                                    show ollie2smile at left with moveinleft

                                                    o "That's a recommended student for ya."

                                                    if scam >=1:
                                                        "All the sorcerers followed us, including the nerds we made signs earlier, and they were MUCH more powerful than we thought."
                                                        "Three of them almost managed to touch Merina."
                                                        "Of course, that's not the task that brings you victory, even if Tate and I made it look that way."
                                                        hide cat20ec
                                                        show cat20smile
                                                        t "Those guys have great tricks up their sleeves..."
                                                        t "Maybe I could take them under my wing and create a nerd elite team..."

                                                        y bored"Doubt that's a good idea."
                                                        hide cat20smile
                                                        show cat20smug

                                                        t "Don't worry, you'd be their leader!"
                                                        t "And I'd be your king."

                                                        y pf"Tempting, but I must refuse."
                                                        "We waited for Aiden and Dallan to present Coal, but his name never came up."

                                                        hide cat20smug
                                                        show cat21simple

                                                        t "Oh yeah... his device must still be resetting."
                                                        y "Does that mean we have to go to... detention?"
                                                        hide ollie2smile
                                                        show ollie2simple at left
                                                        hide cat21simple
                                                        show cat20smug
                                                        t "Not if they can't catch us, come on."
                                                        o "Uhm-"
                                                        hide cat20smug
                                                        show cat20bored
                                                        t "Ollie, if you tell a soul, I'll put powdered milk in your milk."
                                                        hide ollie2simple
                                                        show ollie2surprised at left
                                                        o "{i}*gasp*{/i}"
                                                        o "But that would be too much milk per milk!"
                                                        t "Then keep your mouth shut."
                                                        hide ollie2surprised with moveoutleft
                                                        hide cat20bored
                                                        show cat20simple
                                                        "The threat seemed effective, but in the end, futile, since we're met face to face with Dallan and Aiden before we can get out the front gate."

                                                        hide cat20simple
                                                        show cat21mad2
                                                        show tiger20iritated at left with moveinleft
                                                        show wolf20sadsmile at right with moveinright


                                                        t "Damn it..."
                                                        a "Where are you going? The practice didn't end."
                                                        y awkward"We just have, uhm, places to be, excuse us-"
                                                        d "Sorry [name], the Headmaster sent us after you as soon as he realized Coal can't participate."
                                                        t "But that's not fair! Coal is awesome!"
                                                        t "If his device was functional right now he'd {i}DEMOLISH{/i} Merina!"
                                                        y simple"I can attest to that."

                                                        a "Until he can ACTUALLY prove it, you two have to be punished, his {i}'holiness'{/i} has spoken."
                                                        y worried"Does that mean Coal won't be accepted if he can't audition?"
                                                        d "Oh no, he'll just have to present his powers in front of the jury after practice, like the good old days."
                                                        hide cat21mad2
                                                        show cat21bored
                                                        y "At least there's that."
                                                        t "Fine, let's go [name]."
                                                        t "I don't have magic to teleport away anyway."
                                                        t "Merina was kind of tough..."
                                                        jump detentionnn



                                                    else:


                                                        "All the sorcerers followed us, including the nerds we made sign earlier, and they were MUCH more powerful than we thought."
                                                        "Three of them almost managed to touch Merina."
                                                        hide cat20ec
                                                        show cat20smile
                                                        t "Those guys do have great tricks up their sleeves..."
                                                        t "Maybe I could take them under my wing and create a nerd elite team..."



                                                        y pf"Doubt that's a good idea."

                                                        hide cat20smile
                                                        show cat20smug

                                                        t "Don't worry, you'd be their leader!"
                                                        t "And I'd be your king."

                                                        y bored"Tempting, but I must refuse."
                                                        hide cat20smug
                                                        show cat20smile
                                                        "Finally, Coal is up, we get to see him in action."

                                                        "This time, the gimmick was that Merina can only use projectiles to fight, the exact opposite of my match."
                                                        "Coal had no problem dodging most attacks."
                                                        "At one point, it seemed like he was toying with her."
                                                        "The device on his hip starts to glow, brighter and brighter."
                                                        "Until a laser beam shoots from it, forcing Merina to use bigger spells to protect herself."
                                                        "She throws more icicles, but this time, instead of dodging, Coal creates a barrier around himself, blocking everything."
                                                        "He starts making slow steps towards Merina."
                                                        "Her limitations of only using ranged attacks, once again, make her very vulnerable."
                                                        "After many, many attacks, she manages to crack and ultimately shatters his barrier, a barrage of ice hitting him and throwing him to the ground."
                                                        "Instead of getting up, he starts to... turn to dust?"
                                                        "A moment later, Coal appears next to Merina, hand on her shoulder."
                                                        "Nobody was more surprised than her."
                                                        "It seems like that device of his is VERY versatile."
                                                        "In two minutes he demonstrated high attack power, great protection and utility."
                                                        "Everything a sorcerer would ever need."

                                                        hide cat20smile
                                                        show cat21smug

                                                        t "Nice!"
                                                        t "It seems like everyone that signed my list, managed to show off!"
                                                        y "I doubt the jury will fail them, since they were all awesome."
                                                        t "Not as awesome as us two."

                                                        t "Let's get a move on before anyone changes their mind."
                                                        stop music fadeout 2.0

                                                        "We say our goodbyes to Oliver and move towards the exit."
                                                        scene arena2 with dissolve
                                                        play music "audio/casual.ogg" fadein 3.0


                                                        "We're met face to face with Dallan and Aiden before we can get out the front gate."

                                                        show cat21mad2 with moveinright
                                                        show tiger20bored at left with moveinleft
                                                        show wolf20 at right with moveinright


                                                        t "Damn it..."
                                                        a "Where are you going? The practice didn't end."
                                                        y awkward"We just have, uhm, places to be, excuse us-"
                                                        t "You're not here to stop us, are you?"
                                                        d "Nah, we specifically asked the Headmaster if your punishment is officially over, and he said yes!"

                                                        hide cat21mad2
                                                        show cat20tired
                                                        t "Phew."
                                                        y ec"Not getting in detention on the second day of school, big personal achievement."


                                                        t "So then we're officially free men?"
                                                        hide cat20tired
                                                        show cat20smile

                                                        a "Same as us, since Chelsie took our place."
                                                        a "Thank goodness for that, if I had to listen to the Headmaster's annoyed grunts every time someone failed to win against Merina, I would've gone insane..."
                                                        hide wolf20
                                                        show wolf20ec at right
                                                        d "It's probably a long shot to ask this, but would you like to hang with us for the day?"
                                                        d "Aiden is taking me to get a massage."
                                                        d "Never had one of those before, at least not in this town."

                                                        hide cat20smile
                                                        show cat21smug

                                                        t "You're right, Dallan, it was a long shot, and it missed."
                                                        t "We wouldn't dare disturb your blossoming bromance."
                                                        hide wolf20ec
                                                        show wolf20simple at right
                                                        hide tiger20bored
                                                        show tiger20blushside at left

                                                        a "I-it's not like that..."
                                                        y sadsmile"Yeah, sorry, we really need to go."
                                                        hide tiger20blushside
                                                        show tiger20 at left

                                                        a "Are you at least going to tell us what you two keep doing?"
                                                        t "One of these days, probably."
                                                        hide wolf20simple
                                                        show wolf20 at right
                                                        d "Whatever it is, hope you have fun, and stay out of trouble!"

                                                        y ec"Will do!"
                                                        hide cat21smug
                                                        show cat20ec

                                                        t "And remember, if you follow me, I will teleport you both to the North Pole and leave you there."
                                                        hide cat20ec with moveoutright
                                                        stop music fadeout 3.0

                                                        "He said all that with a smile on."
                                                        "Scary..."
                                                        scene black with dissolve

                                                        "We leave the guys behind, flying again on Tate's broom, Aiden was shouting profanities after him because of the threat, shaking his fist, but Dallan wouldn't let him take a step towards us."
                                                        play music "audio/wisp.ogg"
                                                        scene chibitate22 with dissolve

                                                        y s"How magic consuming is flying for you?"
                                                        t "Almost free."
                                                        t "I charge the broom regularly with magic, so I only need a little bit to actually make it move."

                                                        y "That's handy."

                                                        y simple"Do you think he's hungry again?"
                                                        t "We'll have to check the books to see how often dragons eat."
                                                        y "Wyverns."

                                                        t "I doubt he's up already anyway, we're gonna need to find something to do if he's not."
                                                        y smug"A massage doesn't sound that bad."
                                                        t "I can give you a massage."
                                                        y simple"Do you know how?"

                                                        t "How hard can it be?"
                                                        t "I saw it on TV."
                                                        t "You just rub the other guys back, really well, going further and further down, until you get to the towel."
                                                        t "Then slowly put your hands underneath it, and squeeze gently, then put you fingers in-"
                                                        y simple"I think you watched gay porn."

                                                        t "Yeah... might've been."
                                                        t "It was on Aiden's TV, so I wouldn't be surprised."
                                                        stop music fadeout 2.0
                                                        scene black with dissolve

                                                        "Tate's thrilled expression hints that we're there."
                                                        scene forestt with dissolve
                                                        play music "audio/firstday.ogg"
                                                        "I can see the vine covered, secret path from here, and even some of the traps we've set."
                                                        "The closer we got, the heavier was the feeling that something was wrong..."

                                                        "We get off the broom and move slowly towards the hidden entrance."
                                                        "Small branches and fallen leaves cover the path to the entrance, as well as some tufts of fur, impaled in the few thorns that are only a problem for people who don't know they're there."
                                                        stop music fadeout 3.0

                                                        "The most appalling fact before our eyes is the disassembled alarm trap we set this morning..."

                                                        "From inside the hidden clearing, a shout of pain can be heard, in a language we don't recognize, but it's enough to make us act."
                                                        scene black with dissolve
                                                        "Tate is quick to sprint in action, with me close behind, but a bit reluctant."
                                                        play music "audio/beachfight.ogg" volume 0.3
                                                        scene tent2 with dissolve
                                                        "Once the vines are cleared, we come face to face with some masked... people?"
                                                        show wild1 at left with moveinleft
                                                        show wild3 at right with moveinright
                                                        "Burglars?"
                                                        "Nightfallen?"
                                                        un "They're Wild Furs you idiot."

                                                        "The scream just now was from one of the men, blood gushing out of his arm."
                                                        "He was attacked by the wyvern, who's slumber was disturbed."
                                                        "These guys are bigger idiots than me..."
                                                        "But they did manage to restrain it in a net."
                                                        "And his {i}'papa'{/i} is not happy."
                                                        t "What the fuck do you think you're doing with him?!"
                                                        wf "Zinvok, hal'gulda, val kharth?"
                                                        wf2 "Khagir, khar'volga! Gath'lok, ulvadar. Zha'mar, mal kara!"
                                                        wf3 "Kha'vath galkasha jor vok!"

                                                        "Scribbles! Do you know what they said?!"

                                                        un bored"Yeah, they're gonna shoot ya."

                                                        "What?"

                                                        "The next moment, a needle pierces my neck."
                                                        show blink with llongdissolve
                                                        "I quickly take it out and throw it to the ground, but it's too late."
                                                        "I feel myself become dizzy and lose all power in my limbs."
                                                        y hurt2"T-they...they're in the trees."
                                                        "I look over to Tate, he got the same treatment I did, but he is charging at them, instead of... of...{i}*yawn*{/i}"

                                                        un simple"Hey!"
                                                        un ang"Hey don't fall asleep!"
                                                        un "I can heal you! I can get the poison out!"
                                                        un "But you have to order me to do it!"
                                                        un "Do you hear me?!"
                                                        y asleep"Scrib..bles... g-goodnight."
                                                        scene black with llongdissolve

                                                        un ang"AGHHH YOU WEAK BITCH!"
                                                        un "These restraints make me weak as well."
                                                        un "Thankfully it's just a sleeping dart, since I don't feel any pain."

                                                        un simple"Now what is that cat doing."
                                                        un "He's very resilient for someone whose magic is at its limits."

                                                        un sidee"Wish I could read his mind..."
                                                        un ang"I can't even hear or see anything, open your damn eyes, mortal!"
                                                        un "Ughh, pathetic..."
                                                        un "I guess I'll just wait until this all ends, hopefully they don't decide to slit your throat while you sleep."
                                                        un "If you die, I'll fucking kill you!"
                                                        play music "audio/sadepic.ogg" volume 0.3

                                                        "{i}Meanwhile...{/i}" with llongdissolve
                                                        scene tent2 with dissolve

                                                        show wild1 at left with moveinleft
                                                        show wild3 at right with moveinright



                                                        wf2 "Gath'lok, ulvadar!"


                                                        ta ang "I have no idea who you are, or why you're here, or HOW you found this place, but I'm not letting you leave with my only real friend in hand."
                                                        "There goes another dart in my neck..."
                                                        "One, two, three, doesn't matter, you can throw everything at me, I'm not going down."
                                                        "The strangers are shocked by my resilience, giving me an opportunity to strike."
                                                        "No more magic?"
                                                        "I don't know these words."
                                                        show cat20teleport at left with dissolve
                                                        hide wild1 with dissolve
                                                        hide cat20teleport
                                                        scene teleport with dissolve
                                                        "I sprint towards one of the criminals, touch him, and teleport him in the middle of Lake Lacrima, getting right back before I hit the water as well."
                                                        scene tent2 with dissolve
                                                        show wild3 at right with dissolve
                                                        ta ang"Good riddance..."
                                                        ta "Hopefully he'll drown."
                                                        "I direct my attention towards the scumbag holding my friend, trying to run towards the trees, he is smaller than the rest."
                                                        show wild3 at center with move

                                                        "Unfortunately, my path is cut by another brute."
                                                        "You know what they say when the opponent is much much bigger than you."
                                                        "Kick him in the balls." with vpunch
                                                        hide wild3 with moveoutbottom
                                                        "He falls to the ground, clutching his crotch and moaning in agony."
                                                        "My mind was racing towards the kidnapper, but my knees were already to the ground."
                                                        "In my adrenaline rush, I didn't realize my body was pierced by six other poison darts, after the first two."
                                                        ta "Y-you... you have no..."
                                                        ta "No right."
                                                        ta "GIVE HIM BACK!"
                                                        "I watch as the smaller masked man retreats with my friend, keeping him far from his body, to not get even more injured like his partner."
                                                        show wild1 at left with moveinleft
                                                        show wild4 at right with moveinright
                                                        show wild3 at center with moveinbottom
                                                        "The last two come out from between the trees to help their partner off the ground, who's still holding his crotch."
                                                        show blink with dissolve
                                                        stop music fadeout 3.0
                                                        ta cry"please?"
                                                        "My vision blurs even more, until it gets dark..."
                                                        scene black with longdissolve
                                                        "At least the grass is soft."
                                                        "At least I got to feel like the main character of my own story for a minute..."
                                                        "..."
                                                        "{i}Back to you.{/i}" with longdissolve
                                                        play sound "audio/button.ogg"

                                                        un simple"..."
                                                        play sound "audio/button.ogg"
                                                        un bored"Hey."
                                                        play sound "audio/button.ogg"
                                                        un ang"HEY!"
                                                        play sound "audio/button.ogg"
                                                        un ang"It's been over an hour already!"
                                                        play sound "audio/button.ogg"
                                                        un "The cat is already up!"
                                                        play sound "audio/button.ogg"
                                                        un "And he got like seven times the amount of sedatives you did!"
                                                        play sound "audio/button.ogg"
                                                        "...sleepy."
                                                        play sound "audio/button.ogg"
                                                        un "Then tell me to remove the {i}'sleepy'{/i}!"
                                                        play sound "audio/button.ogg"
                                                        "Hghmm..."
                                                        play sound "audio/button.ogg"
                                                        "Remove... sleep, Scribbles..."
                                                        play sound "audio/button.ogg"
                                                        un bored"Finally."
                                                        play sound "audio/button.ogg"
                                                        y surprised"Wha-!"
                                                        play sound "audio/wack.ogg"
                                                        scene tent2 with vpunch
                                                        "In an instant my eyes are wide open and I'm back on my feet."
                                                        "Memories of me falling down, and leaving Tate to fend for himself came rushing back."
                                                        scene sadtate1 with longdissolve
                                                        scene CGc11



                                                        "I scan the clearing, noticing him standing on his knees."
                                                        "From behind, his torso moves up and down in spasms, his ears down to the ground."
                                                        "He's crying, or at the very least, trying his hardest not to."

                                                        "There's no point in me asking, or wondering, I know the conclusion of whatever happened."
                                                        play music "audio/triste.ogg" volume 0.8
                                                        scene tatesad with longdissolve
                                                        scene CGc12
                                                        "I approached him, worried."
                                                        "As Scribbles said, he did take a high dose of sleep poison, yet, he's here."
                                                        "Hunched over a pool of blood."

                                                        y worried"hey..."

                                                        "His ears twitch, but he remains silent in my presence."
                                                        "His eyes, usually full of life, a sparkle always lit, are now dull, uninspired, depressed."
                                                        "Magic particles flowing around him, created by his strong emotions."

                                                        y "Is that..."
                                                        "He shakes his head gently."
                                                        t "It's one of theirs."
                                                        t "He got bit."
                                                        y "Not the smartest idea to wake up a wyvern."

                                                        t "Not the smartest idea to mess with me."

                                                        y sadsmile"He bit me once too, but I suppose I got off easy, heh?"

                                                        label theytookhim:
                                                        scene tatesad2 with longdissolve

                                                        t "..."

                                                        t "They took him..."

                                                        Y sad"..."
                                                        y "Maybe it's for the best."

                                                        t "What..."
                                                        t "What do you mean?"

                                                        y worried"Tate..."
                                                        y "Listen."

                                                        "He flinches and his ears twitch again as I try to place my hand on his shoulder."

                                                        y "You can't raise a wyvern."



                                                        if betray >=2:
                                                            "He slaps my hand away."

                                                            t "How would you know?"
                                                            t "It's not like you spent that much time with me to know all my methods!"


                                                        else:
                                                            pass
                                                        scene tatesad3 with dissolve
                                                        scene CGc13
                                                        t "And why not?"

                                                        t "What am I supposed to do?"
                                                        t "You want me to just kill it?"
                                                        t "Maybe throw him off a cliff, or suffocate him in his sleep, all because he was unfortunate enough to lose his parents?"

                                                        y sad"You're right, Tate."
                                                        "Another ear twitch."
                                                        y "You do have a tough decision here, I don't know what I'd do in your place, but I know what the right thing to do is."


                                                        "He growls."
                                                        t "It's always {i}'Right'{/i} or {i}'Wrong'{/i} with you people, you just don't care enough to find the silver lining."
                                                        t "What if neither option is to my liking?"
                                                        t "{i}'Let's just force this little naive idiot to follow our ways!'{/i}"
                                                        t "{i}'He'll do whatever we say, because he's so lonely and pathetic!'{/i}"
                                                        t "Especially now, with you in the picture... your apathy towards the dragon was pissing me off from the very moment you laid eyes on his egg."
                                                        y sad"..."
                                                        y "Wyve-"

                                                        t "I don't... CARE!"
                                                        t "SHUT UP ABOUT YOUR STUPID WYVERN IDEA!"
                                                        t "HE COULD BE SATAN HIMSELF FOR ALL I CARE!"
                                                        t "HE WAS MY FRIEND!"
                                                        t "DON'T YOU GET IT?!"
                                                        t "CAN'T YOU TAKE THIS SERIOUSLY FOR ONCE?"
                                                        t "And this question is coming from me...of all people."

                                                        y worried"But I do, Tate!"
                                                        "His eye twitches."
                                                        y "At least I try to."
                                                        t "Why are you even here right now?"
                                                        if adventure <=0:
                                                            t "Just go hang around Merina, or make out with Oliver, or whatever other perverted things you came to the 'sex school' to do."
                                                        else:
                                                            pass
                                                        y "It's simple."
                                                        y "I want to be around you, Tate."

                                                        "Another ear twitch."
                                                        y sad"I know sometimes I fail to see the bigger picture."
                                                        scene tatesad4 with dissolve
                                                        scene CGc14
                                                        y sadsmile"But if there is one thing I know, it is that I like you, Tate."

                                                        "He clenches his fist, hard enough to compress the dirt trapped between his fingers, and shakes with anger."

                                                        t "For the last time..."
                                                        t "Would you stop..."
                                                        show tatesad5 with hpunch
                                                        t "CALLING ME THAT!?"
                                                        scene CGc15


                                                        t "I TOLD YOU ALREADY, TIME AND TIME AGAIN, THAT IS NOT MY NAME!"
                                                        t "I DON'T LIKE IT, IT'S NOT MINE!"
                                                        t "IT'S NOT YOURS TO CHOOSE, YOU MISERABLE EXCUSE OF A PARENT!"

                                                        scene tatesad6 with dissolve

                                                        "He stops dead in his tracks after the last statement, looks at me, terrified, then pushes me down."
                                                        "The particles multiplied after his outburst, teleporting him away."
                                                        scene tent2 with longdissolve
                                                        stop music fadeout 3.0

                                                        "I'm left alone in the clearing, still on my back."
                                                        "I feel my friend's hands scorching the place they touched to push me."
                                                        "It hurts more than any blade, punch or poison."
                                                        play music "audio/slowpiano.ogg"



                                                        Un suspicious"Sheesh, you really fucked this up."
                                                        un bored"I didn't even feel like making comments in between the lines."
                                                        y sad"The worst part is that I don't understand what I did wrong."
                                                        if betray >=2:
                                                            un squint"Are you kidding me?"
                                                            un "You ditched him twice already, or was it three times? To go hang around that fox and her... whatever the mouse is to her, friend, lover, sex toy?"
                                                        else:
                                                            pass
                                                        un eyeroll"He clearly just wanted someone that cares about him, and pets are usually a good source of unconditional love."
                                                        un "He took care of that egg for so long, and now that it hatched and it's gone, you're like {i}'maybe it's better your friend got kidnapped and is probably dead'{/i}."
                                                        un suspicious"And he kept trying to make you call him by any other name, except {i}'Tate'{/i}."
                                                        un "Even going as far as to name himself {i}'Tartarus'{/i} or {i}'The Prince of Shadows'{/i}."
                                                        un "And everyone around him, including you, treated it like a joke."
                                                        un "If that's not a cry for help, I don't know what is."

                                                        un sidee"The more I talk the more I realize how stupid you are."
                                                        un "And I don't even care about the cat that much."
                                                        un "I just think he's kinda neat."
                                                        un bored"But other than that, he could die for all I care."
                                                        un "And that tiger feels the same way, I bet many others too."
                                                        un "It must feel pretty shitty to be openly disliked by so many."
                                                        un suspicious"It's {b}YOU{/b} who should care more about him."
                                                        un "Because it's you {b}HE{/b} cares most about."

                                                        "I reflect on the truth bomb Scribbles just dropped."
                                                        "I want to argue, to explain myself, but I can't."
                                                        "He's just... right."

                                                        y sad"Perhaps there really isn't a right and wrong answer."
                                                        y "I tried to see it through a logical perspective."
                                                        y "But the most logical would've been to do whatever makes him happy."
                                                        y "Not like it costs me anything to be supportive."
                                                        y worried"Now that I think about it, what was the reason he wanted to spend time with a random first year, if not to make an easy friend..."
                                                        y sad"I wish I could be more emphatic..."

                                                        un bored"So, are you gonna go after him?"
                                                        y simple"You want me to go?"
                                                        un eyeroll"I have a heart too, you know?"
                                                        un bored"Well, not right now, in my previous body..."
                                                        un "But it kind of sucks to see you fuck up {b}THIS{/b} badly."
                                                        un "So yeah, I want you to go."
                                                        un "Do {b}YOU{/b} want to go?"

                                                        y surprised"Absolutely."
                                                        y worried"But... where can I find him? He just teleported."
                                                        if adventure >=1:
                                                            un "Oh, I think you know where."
                                                            y simple"..."
                                                            y "I think I do."
                                                            "If his automatic spell took him somewhere with high emotional value, then I've been there before."
                                                            jump findtate
                                                        else:
                                                            un s"You could ask the fox."
                                                            un bored"I'm pretty sure you would've known this yourself if you spent more time with the cat, but oh well, we already established you're an idiot."
                                                            y simple"Indeed I am, but I don't regret my time with Ollie and Merina."
                                                            un "And you shouldn't, you don't need to regret that to feel sorry for this."

                                                            un "You really need some lessons in philosophy and social interactions."
                                                            scene barrier with fade
                                                            "I run back towards the barrier, since signal doesn't work between a device inside and outside the barrier."
                                                            "After minutes of sprinting and a heavy breath I take out my phone and text Merina, asking what Tate's favorite spot to go to when he's upset is."
                                                            "She's worried and asks too many questions, but I dodge them and focus on the trouble at hand."
                                                            "She gives me some directions towards a part of the forest with a semi abandoned train track."
                                                            "I believe I saw it before, when we flew over the forest."
                                                            jump findtate





                                                        label findtate:
                                                        scene black with dissolve
                                                        stop music fadeout 2.0
                                                        "No time to waste then."

                                                        "I run like the wind, using my speed enchantments."
                                                        scene junkyard with longdissolve
                                                        "I arrive at the desired spot exhausted, I find the train tracks and start walking slowly along their rim."
                                                        "Doesn't take long until I start hearing the rustling of leaves and the scraping of sand and dirt."

                                                        "I leave the path, and round the corner through some more bushes and find a coiled up cat, sitting on the ground near an old, abandoned crashed wagon, drawing in sand with a stick, seemingly expressionless."

                                                        "I know he heard me, since I'm not trying to be sneaky, and mother nature is not known for its quiet environment when every branch and leaf is basically a mini alarm."

                                                        "I take his lack of reaction as a sign that I can approach, so I do, standing now just three feet behind him, crouched down, looking at his sand drawing."
                                                        "A mighty dragon stands with its wings spread, and two small people on its sides, with their arms raised."
                                                        "Something tells me he was expecting me."
                                                        play music "audio/slowpiano.ogg" fadein 4.0

                                                        "I decide to keep my mouth shut for a bit, and focus on listening, but the silence only lasts for a little while anyway, broken by the sad voice of a cat, the saddest I've heard him since I met him."

                                                        scene sand1 with llongdissolve


                                                        T "I'm sorry I lashed out at you..."
                                                        y simple"I don't blame you."
                                                        t "..."
                                                        t "I know he's a wyvern... I always did."
                                                        t "I just didn't want to admit it, since I know the chances are slim to domesticate one..."
                                                        t "You'd have better chances at keeping an alligator as a pet."

                                                        t "You're new, and don't know me very well, obviously."
                                                        t "If barely."
                                                        T "I'm not sure why I so expected for us to become a bonded pair, just like that."
                                                        t "I suppose it all went a bit over my head."
                                                        t "Maybe I thought I could get a genuine, awesome friend."
                                                        T "You're one of the {i}'cool'{/i} guys, new, powerful, popular, kind of naive, no offence, so I thought you'd be perfect to befriend."

                                                        "The picture he's been drawing now has multiple people around it."
                                                        "I can recognize Dallan's big muscles and sleeveless jacket, Aiden's snarky, arm crossing pose, Merina's elegant dress and two more that I don't recognize, but judging by their ears, they could definitely be members of the E.F.D. club if they applied."
                                                        "I sit down closer to him."
                                                        "Although he's trying to stay focused on the ground, I can see he's waiting for my response with a held breath."

                                                        y "..."
                                                        t "..."
                                                        y "..."
                                                        y "May I know... what's so wrong about your name?"

                                                        t "..."
                                                        t "It's stupid."
                                                        t "They named me that because of my happy-go-lucky personality."
                                                        t "It literally means {i}'Cheerful'{/i}."
                                                        t "And I just don't want to believe I'm that shallow..."
                                                        y "Forgive me for the question."
                                                        y "But is that not accurate?"
                                                        t "To be honest?"
                                                        t "I suppose?"
                                                        t "I'm happy, because I try my hardest to be."
                                                        t "I just hate when people pity me, or try to tiptoe around me just because I don't have parents."
                                                        t "So I try to show everyone I'm ok."
                                                        t "Which is true."
                                                        t "I AM ok..."
                                                        t "And it's not a lie, I just wanted a friend that knows that..."
                                                        t "But even THEY don't see it."
                                                        "He points at the drawing of the two long eared figures, which I now assume must be his adoptive parents."
                                                        t "Plus it just doesn't sound that great, in my humble opinion."

                                                        t "Although, they didn't want that name either, at first..."
                                                        t "The people around kept calling me that, since they haven't decided on a name."
                                                        t "But in the end, they kept it."
                                                        t "Too bad I couldn't remember my real name."

                                                        y "Is it that bad? To be named by the town's people?"

                                                        "He shrugs."

                                                        t "Names have the most meaning when it's given by someone you love."
                                                        t "Like your parents..."
                                                        t "I was about seven years old when they finally decided on a name, at that point...it felt a bit redundant."
                                                        t "Not very meaningful."

                                                        t "And to put more salt to the wound, they invented a last name for me too."
                                                        t "Since I was never officially adopted."
                                                        t "Can you take a guess to what it might be?"

                                                        y "Uhm... Feline?"

                                                        t "That... would be stupid too, and kinda funny, but no."
                                                        t "It's Foster, Tate Foster, the foster child."
                                                        t "Wooow..."
                                                        t "So unique, so..."
                                                        t "Stupid..."
                                                        t "Let's remind him every day of his two main distinct traits."



                                                        y "You're right, it's stupid."
                                                        t "Thank you!"
                                                        t "I legally changed it when I turned eighteen... but mister Sebil was upset, calling it disrespectful, so I changed it back..."

                                                        y "Are they good to you?"
                                                        y "Your parents."

                                                        t "Yeah, very."
                                                        t "I do have some bottled up emotions for them, still, I love them."
                                                        t "Don't get me wrong, I know I talk them down a lot, but they were great people... just not great at raising kids."
                                                        t "At least not this kid."
                                                        t "They gave me food, shelter, clothing, personal space, education, love, but there was always something missing..."
                                                        t "My problems were always overlooked, like my name."
                                                        t "Most of the time I can't even bring myself to call them by anything other than their names..."

                                                        y "I don't know what my name means either, but I like it, since it's the name my mother gave me, and I love her, so I respect it."

                                                        t "Must be nice..."

                                                        y sad"..."

                                                        y "Is that why you kept trying to change your name yesterday and today?"

                                                        t "Something like that..."
                                                        t "I'd take a stupid name too, if I feel like it's truly my own."
                                                        t "The problem is that it needs to stick to people before I decide to change it."
                                                        t "Don't want another {i}Tartarus{/i} situation."
                                                        scene sand with llongdissolve
                                                        scene CGc16

                                                        "His drawing is now done, but the dragon was erased in the process, replaced by a little wyvern."
                                                        "Same with the other people around, except for two."
                                                        "This way, the two figures next to the wyvern, the two felines, became the main attraction."

                                                        y simple"..."
                                                        Y "Can I hug you?"

                                                        T "Huh?"

                                                        "He looks surprised, but quickly recovers."

                                                        T "I'm usually the one who does that... without asking."

                                                        Y "So?"
                                                        T "..."
                                                        t "Yeah..."
                                                        stop music fadeout 3.0
                                                        scene black with dissolve
                                                        "He does not resist, but doesn't make a big effort to return it either."
                                                        "He's shaking, and I feel like he'll fall over any moment."
                                                        scene sand1 with dissolve
                                                        play music "audio/hope.ogg" fadein 3.0

                                                        y simple"Are you feeling alright?"
                                                        T "Fine, just..."
                                                        T "I just don't have much magic left..."
                                                        t "Actually, I'm almost completely paralyzed."
                                                        y worried"Are you serious?"
                                                        t "Teleporting with my mind alone, my body kind of took a hit, It hurt to even move the stick to draw..."
                                                        t "But hey, at least now I know I can do it!"
                                                        t "Isn't it awesome?"
                                                        y sadsmile"Absolutely, I'd express more joy if I wasn't so worried for you."
                                                        t "Eh, I'll be fine in an hour or two."

                                                        "I hold him for a little while longer, sharing body heat and supporting his barely standing body."
                                                        y simple"..."

                                                        y "We're going to get him back."

                                                        t "I told you."
                                                        t "I can't move."
                                                        t "And I won't be able to until I get some magic back."

                                                        y s"We don't have to do it right now."

                                                        y "We'll go tomorrow, early in the morning."

                                                        t "Do you think he'll be alright by tomorrow?"
                                                        y "Whoever took him didn't seem to want to kill him, or us, otherwise, they would've done so already."

                                                        t "But he's a wyvern!"
                                                        t "I already told you, I always knew."

                                                        y "You still consider him your friend, don't you?"
                                                        t "Yeah, but-"
                                                        y determined"No buts!"
                                                        y "I'm your friend as well, there is no question about it, and I never want you to doubt it, as your friend, I'm not letting anything happen to your other friends."

                                                        "His eyes light up with hope, and the smile comes back, even if it is smaller than usual."

                                                        T "What about the battles tomorrow?"

                                                        Y confused"Battles?"

                                                        t "Pair battles, yes."
                                                        t "Everyone pairs up and we do a two against two battle."

                                                        y simple"I forgot those are a thing."
                                                        Y "Why are you concerned about that?"
                                                        Y "Isn't this way more important?"

                                                        T "We can't miss them."
                                                        t "The Headmaster will be watching this year, the same as today."
                                                        t "To assess the students, or something."
                                                        t "I don't want to miss it, and more importantly, I don't want YOU to miss it."

                                                        y sadsmile"You just can't not take care of your friends, can you?"
                                                        t "I'm not as selfish as I let out to be."
                                                        y "Alright."
                                                        y s"As you wish."
                                                        y "We'll demolish any first years that are unfortunate enough to be paired against us."

                                                        t "Love the spirit."
                                                        t "I pity those people already."
                                                        t "I'm going to have to unleash my pent up rage on them."

                                                        t "I said before that I hate sad people, so let's cheer up."
                                                        t "Although it's hard to be happy when you can't move."
                                                        t "I get upset just by thinking at how pathetic I must've looked until now with a frown on."
                                                        t "Which is a bit ironic."


                                                        y "Want me to carry you back?"

                                                        t "You and what muscle?"

                                                        y smug"I'll make you eat those words up, little jester."
                                                        stop music fadeout 5.0
                                                        scene black with dissolve
                                                        "I get up, place a strength enchantment on myself, and pick up the unexpecting cat, placing him over my shoulder like a log."

                                                        t "Oh my..."
                                                        t "Alright, I don't mind this."

                                                        y "Don't judge a book by its cover."
                                                        y "Shall we?"
                                                        t "Lead the way!"
                                                        scene sand with longdissolve

                                                        "I turn around before starting the trip, with his butt facing the same way as me, I take out my phone, and sneak a picture of his sand drawing."
                                                        "The drawing of me, him and the little wyvern, all happy together."
                                                        "Keepsake."

                                                        t "Hey, not to ruin your protagonistic hero moment, but your shoulder is a bit too narrow, it kinda hurts my stomach."
                                                        y simple"Oh, sorry."
                                                        scene black with dissolve
                                                        "I turn him around, picking him up bridal style instead."
                                                        y s"Is this better?"
                                                        t "The cat looks into the strong, manly leopard's eyes, lewd thoughts going on through his head as he's being manhandled effortlessly."

                                                        y smug"I'll take that as a yes."
                                                        play music "audio/wisp.ogg"

                                                        scene carrytate with longdissolve
                                                        scene CGch11

                                                        "We begin our journey back to the academy."
                                                        "The trip is quiet, save for the occasional wild animal noises making my fur bristle, a fact that makes Ta- I mean, my good friend in my arms chuckle."
                                                        y bored"You realize I can easily drop you whenever, right?"
                                                        t "Then who would protect you against squirrels?"
                                                        t "Scaredy-cat."
                                                        y simple"Squirrels have a high chance of carrying rabies or other diseases."
                                                        t "Don't ruin nature for me please."
                                                        y "You asked for it."

                                                        t "Let's pass the time with something that doesn't include being a nerd."
                                                        y "What do you propose?"
                                                        T "Do you know how to play {i}'never have I ever'{/i}?"
                                                        y s"I believe so."
                                                        y "Any extra rules beside the regular ones?"

                                                        t "Instead of putting a finger down, you have to kiss the closest person to you."
                                                        y simple"You're the closest person to me."
                                                        t "{i}*gasp*{/i} No way!"
                                                        t "I guess that's true."

                                                        y bored"Yeah, we're not doing punishments."
                                                        t "Coward."
                                                        y s"I'll start."
                                                        t "Shoot."


                                                        menu:
                                                            "Never have I ever..."

                                                            "Fancied a friend's parent.":
                                                                t "You kidding me?"
                                                                t "Have you SEEN Aiden's dad?"
                                                                t "AAOOOGA."
                                                                t "Too bad he's an absolute bitch."
                                                                t "Otherwise he would have absolutely been the one I lost my virginity to."
                                                                t "He's not even that old either."

                                                                y surprised"Wow."
                                                                y "He must be REALLY handsome then."
                                                                y smug"Wish I could meet him."


                                                                t "Ha, good one."
                                                                "It wasn't a joke...but alright."
                                                                jump neverhaveiever


                                                            "Given a fake name to someone.":
                                                                t "I feel like that's targeted at me, specifically."
                                                                y surprised"No, why would- oh."
                                                                y awkward"Oops, honestly, I forgot that's literally how we met."
                                                                t "Heh, maybe you did like the name Tartarus, and lied about it all along."
                                                                y bored"Absolutely not."
                                                                t "Fair enough."

                                                                jump neverhaveiever


                                                            "Shoplifted.":
                                                                t "Nope, never."

                                                                y confused"Never?"
                                                                t "Why so surprised?"
                                                                t "I have no reason to."
                                                                t "I'm not an asshole by choice, and I don't know if I mentioned it, but my parents bought me almost anything I wanted."
                                                                t "Except that I hate relying on them for things, so I made my own money by hunting Nightfallen."
                                                                t "Would be pretty stupid to put all that effort into getting money just to start shoplifting."
                                                                t "Plus, it's a pretty small town, everybody knows everybody."
                                                                t "My reputation would be destroyed!"

                                                                y smug"Your saint reputation of local troublemaker?"

                                                                t "Exactly!"


                                                                jump neverhaveiever






                                                        label neverhaveiever:

                                                        t "My turn."

                                                        t "Never have I ever..."
                                                        t "Had a threesome in a public place with two complete strangers."

                                                        y simple"That is very specific."
                                                        y "No, no I have not."
                                                        y confused"Why would you think that anyway?"

                                                        t "I don't know, you look like the type that can pull it off."

                                                        y "Didn't we already establish that we're BOTH virgins?"

                                                        t "Oh...right, I forgot."

                                                        t "Hey, here's an idea, since we're virgin best friends, do you wanna do it together?"

                                                        "The thoughts in my mind look like a keyboard smash right now."
                                                        "What the hell is that question, so sudden, so bold, I kind of like it."

                                                        y blush"W-what do you mean?"

                                                        t "Well, if you ever find a boyfriend, I'll find a partner as well, then we can do that thing they do in movies, where bottoms fist bump while laying next to each other in bed."
                                                        t "Getting railed at the same time."
                                                        "Ah, that's what it is, the thought is still lewd as hell, but in a different way."

                                                        y sadsmile"I-I guess? Yeah, yeah sure."
                                                        y "I mean, if you want to."
                                                        t "Great, it's a promise then."
                                                        "At first I thought his question was just a joke, a real life shitpost... but his content expression and soft smile says otherwise."

                                                        y simple"What... what if it's a woman?"

                                                        t "Then I hope you don't mind if I plant my tongue in your girl's mouth while you're going to town on her."
                                                        y smug"Your gay ass could never."
                                                        t "You're right... but I'd try, for you."
                                                        t "I'd have a guy behind me to take my attention off of it, obviously."

                                                        "I'm slowly getting used to the cat's casual dirty words, paired with Scribbles' usual nonsense, conversations like these do not embarrass me as much anymore, still, can't help but blush a little in the end."

                                                        "We continue walking and playing."
                                                        "We both realize we told each other so many details about our personal lives, yet, we're both dumbasses that can't retain any information."
                                                        t "Would you...punch your father for a thousand dollars?"
                                                        y bored"I mean...he walked out on his wife and two kids, so happily, yes."
                                                        t "Fuck, I forgot."

                                                        y smug"Easiest grand ever."
                                                        y "Uhmm, let's see."
                                                        y "Least favorite food?"
                                                        t "Fish damn it!"
                                                        t "I must've told you at least twice already."
                                                        y simple"Ah...we need to take notes sometimes."
                                                        t "Yup."

                                                        "This walk is the most fun and relaxing activity I have done in a while, even if I'm carrying over a hundred pounds of cat in my arms."
                                                        "After only twenty minutes of playing and walking, the entrance to the forest and the edge of the town come into view, as we pass the barrier with no interruptions."


                                                        y s"My turn and last question."
                                                        if scam<=0:


                                                            y smug"Never have I ever: recovered from a severe lack of magic and sleeping drugs in a matter of minutes, but didn't tell my friend, because I like being carried bridal style?"
                                                            jump guilty
                                                        else:
                                                            y "Never have I ever: recovered from a severe lack of magic in a matter of minutes, but didn't tell my friend, because I like being carried bridal style?"
                                                            jump guilty
                                                        label guilty:
                                                        "He raises his hand and puts a finger down."
                                                        y smug"{i}'Paralyzed'{/i} my ass."
                                                        t "What can I say?"
                                                        t "Something about this experience feels nice."
                                                        t "My very own muscle carry man."
                                                        y "You're a rascal."

                                                        t "What gave it away?"
                                                        y "You kept readjusting your ass every two minutes."
                                                        t "I had to, you refused to change the positioning of your arms, it was getting uncomfortable..."
                                                        y ec"That's because I'm a great detective, everything was calculated!"

                                                        t "Haha..."

                                                        "I put him down, gently, since even though he's now fine, he still hasn't used his legs in a while."
                                                        jump twobros
