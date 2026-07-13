
label starttherium2:
$ goodhorseending_points = 0
$ neutralhorseending_points = 0
$ badhorseending_points = 0
$ yessex =0
$ compliment = 0
$ samsex = 0
$ theriumhome = 0
$ refuse_points = 0
$ theriumbed = 0
$ nightfallen = 0
$ scpoints = 0
$ auditions = 0
$ thepoints =0
$ book1 = 0
$ book2 = 0
$ book3 = 0
$ yessex2 = 0
$ yessex1 = 0
stop music fadeout 2.0
scene chibitherium1 with llongdissolve
play music "audio/forgetmenot.ogg" fadein 2.0
q "The few clouds in the sky seem to disappear and the sun warms your fur with each step taken in its rays."
q "You keep a step behind your new friend, watching him walk with his tail barely swinging, a tail that separates a pair of powerful thighs, of which you just can’t take your eyes from."
q "His tight top, sleeveless shirt remains almost unmoved in the walking motion, making you wonder how it is pinned down."
q "Perhaps it’s a special material, or it’s a one piece? But thinking about how the strip of fabric surrounds the guy’s crotch is not the best idea at the moment."
q "One thing you do remember to take your mind away from lewd thoughts, is a creepy, cloaked figure that might or might not show up around the next corner, behind you, or even outside, looking in."
q "Noticing your awkward fidgeting, the horse finally decides to stop his intentional silent treatment, performed to tease an anxious, shy individual like you, successfully at that too."
q "By his reaction you assume he enjoys doing this to first years for fun."


Th "You know, [name], I’m so glad you decided to join us."
th "What exactly made you take a decision like that?"
th "Usually first years with magical abilities simply join the Sorcery Shard, it’s more versatile, some would say more fun too."
y awkward"I just like… uhm, summoning?"
th "Really?"
th "Say, what is a summoner’s job?"
Y "Uhmm, summon Nightfallen to help? Duh."

Th "Woah there cutie, easy on the details."
y blush"Cutie?"

th "To help with what?"
y pf"Hhhouse chooooores?"
th "You don’t usually summon Nightfallen inside a house, it’s a tiny bit illegal."


y simple"Oh..."

Y bored"Alright, I...don’t know much about summoning."
Y "I just found out I have magic like three years ago."


q"He stops dead in his tracks and says nothing, just turns around, slowly, smiles warmly and looks you up and down."

th "That won’t do."
th "Come with me."

y simple"Ooook?"
scene chibitherium2 with dissolve
q "He gently grabs your hand and makes you hurry along with him."
q "Shortly, the academy’s front gates are left behind, and the busy town’s life takes its place."
q "People walking by, bees and butterflies still bothering the flowers that decorate the shops and houses, simply a nice day for a walk with a handsome man."
th "Are you thirsty, [name]?"

y smug"For men…"
th "What?"
y awkward"What? I mean, yeah, kind of."
scene chibitherium3 with dissolve
scene CGch13
q "You both stop by a cafe and he pulls out a chair for you."
y ec"Thank you."
q "A minute after he brings out two large cups of liquid and offers you one, together with a thick straw and a plate of pastries, both sweet and savory."
th "Boba tea?"
y s"Ah, I heard about these but they don’t sell them where I’m from…"
th "Then I would not survive there."

q "You follow his example and stab the straw through the thin plastic lid."
q "Upon sucking the liquid, soft balls of sweetness enter your mouth, as well as a strong taste of coconut milk and vanilla."
q "It’s more of a neat, sweetness bomb than tea, but it is enjoyable nonetheless."

y boba"It’s good, really good."

th "This is my favorite drink, the milky cold tea and the chewy sweet pearls are everything I want in a snack or beverage."
y "I can see why, it’s delicious, can’t believe I never had anything like it in the city."
th "That’s the power of local businesses."
q "You spend some time in blissful quietness, with only the hubbub of the streets and nature to bother you and enjoying the little lunch break."
q "The light wind ruffles your fur and cools you down from the prevailing summer sun."
q "It is a peaceful day, so peaceful that you almost ignore your partner’s words."
th "What do you think of the town? The academy?"
y "Huh? Oh, I’ve only been here for a day, less than that, a few hours, but...I really like it already."
y "Not hearing any car honks or engines is nice, and the air is so clean."
y "Not to mention you have these delights sold here, heh."
q "You shake the ice in the soon empty cup."
q "The horse giggles together with you, but quickly switches to a more serious tone."


Th "[name]...you need a reason."
y "A reason?"
th "What do you live for, what do you strive for? What do you fight for?"
th "Why do you want to be a summoner?"
y "That’s a weird way of asking, why?"
th "You see…"
th "Slayers are either sex driven or bloodlust driven, they want to put their hands on Nightfallen one way or another."
th "Alternatively, some just want to have the easiest classes and be the most likely to graduate."
th "Defenders want to protect people, to be helpful in combating Nightfallen through other means than just murdering them."
y "Murder?"
th "I meant...killing them."
th "Defenders are also in the business to have the glory and the money of a hunter, but not actually interacting much with Nightfallen, most aristocrats and noble families become defenders."
th "Even if defending people is the last thing on their minds."
th "Sorcerers are somewhat of a jack of all traits, depending on their abilities, but most of them are either here to sharpen their craft… or just looking for fun and adventure."
th "You’ll see that everyone fits into a mold around here."
y "A good and bad mold?"
th "If you want to see it that way."
y "What about summoners?"
q "He thinks for a second, readying to respond before stopping himself last second."
th "That is for you to decide."
th "And for others to judge."
"Why do I want to be a summoner...if it weren’t for Scribbles...would I still want to be one?"
th "Of course, whatever your response is, it’s not like I’ll throw you out or anything, it just depends on how I see you in my own eyes."

menu:
    "Why? Hmmm..."
    "I feel a special bond with Nightfallen.":
        $ thepoints+=1
        jump hesees
    "I made a promise to a friend.":
        $ scpoints+=1
        jump hesees
    "It simply calls to me.":
        $ thepoints -=1
        jump hesees
label hesees:




th "I see…"
th "Well then."
th "I know what we shall do now."
y "What is that?"
y surprised"Woah-"
scene chibitherium2 with dissolve
q "Therium grabs your hand, taking both empty cups of tea and throwing them in the trash can, before starting to power-walk with you behind."
y "Where are we going?"

th "A place outside the barrier, a special place."
y s"What kind of place?"

th "I’m going to teach you some basics about summoning."
th "Whatever the reason is you want to be one, I can’t just let you fail tomorrow’s auditions."
th "It would be a shame if a recommended student switched Shards so soon."

y "That's awesome but why are we in such a hurry."

q "He slows down and lets go of your hand, which you now realize kind of hurts…"
q "However, his accidental strength does the exact opposite of scaring you, of course."
un bored"Whore."
"You’re not allowed to intervene in the narration!"
un "You do it all the time!"
"Shut up and continue."
th "You’re right, sorry, I got a bit excited."
th "I don’t often take someone under my wing."

q "Seeing the stoic horse show genuine emotion makes you feel...nice. Just a warm feeling that can’t be described surges through you."
q "He stops walking and turns towards you."
q "The back of his palm suddenly touches your forehead as his other hand holds your head in place."
th "Strange, I didn’t make any lewd remarks in a while, yet your body temperature is unusually high, are you feeling alright?"
y sadsmile"Yeah, of course, it’s just kind of hot outside, you know? Especially with all this fur."
q "He smiles while caressing his bare, short furred arm."
th "Can’t relate."
stop music fadeout 2.0
th "But no worries, the place I’m taking you to is cool and shaded."

scene forest with dissolve
play music "audio/oddish00.ogg" fadein 2.0
q"Your little walk continues for another minute or so, until the edge of the barrier and the beginning of the forest comes into sight."
q "He grabs your hand again and goes first through the barrier, sucking you out too."
y surprised"Ah!" with hpunch
q "The force of the field is high enough to make you stumble, but he didn’t hold your hand for nothing, as he caught you in his chest."

y blush"I don’t think I deserve a personal chest airbag."
show horse with moveinright
th "Why not? You’re our little special recommended student, you deserve whatever you desire."
q "He brushes off that last statement, leading the way further as if nothing has been said, but for some reason, you can’t shake the words off."

y simple"Uhmm, why exactly do we deserve the best?"
th "The Headmaster made it quite clear that we have to treat you four very well, to put it simply."
th "And they didn’t have to tell us, leaders and vice leaders twice, because as I said before, it benefits us to have you in our Shard."

y "I see."
show horse sadsmile
th "You seem disappointed."
th "I hope you don’t think that’s the only reason I want to hang out with you."
show horse smug
th "It takes more than an old, bossy lion to make me do something I don’t want to do."
y s"That’s reassuring, but if that’s not the case...why are you...you know, spending so much time for my sake?"
y sadsmile"Sorry if I’m a bit negative here, but I don’t have much to offer."
th "You’ll learn that there are very easy and straightforward answers to many complicated questions."
hide horse smug with moveoutright
q "The horse takes a couple of quickened steps and jumps over a big, fallen tree trunk, offering you his hand as you approach."
th "The answer to that question is…"
q "He pulls your hand hard, catching you for the third time in his arms today."
show horse ecclose with moveinright
th "You’re cute."
q "You can’t help but blush, almost hard enough to be visible through your fur, lasting for as long as his half closed eyes linger on your flustered face."
show horse with dissolve
q "He lets go after a moment and takes a step back, waiting for a reaction to something specific."
q "With all this self doubt and meaningless conversation you didn’t pay attention to where exactly he’s taking you."
scene swing with llongdissolve:
    blur 16
q "You only now notice the forest that turned into a clearing surrounded by bushes and tall mossy boulders, as well as some people-made objects."
q "A couple of benches and coffee tables, clearly made by amateurs, some scarecrows or perhaps makeshift target dummies."
q "A soft breeze ruffles your fur as you look around, noticing the best feature of this place: The cool air and shade from the never-ending summer sun."
th "What do you think? It’s not much, but I’m proud of it."
y s"It looks nice and feels even better."
y "Is this your personal, secluded forest getaway?"
y "It’s a pretty popular trope in romance fanfiction-"
y awkward"Not that I’m that familiar with that topic...*cough cough*."
un "Cool new plans for myself, ransack your mind for all that gay smut."
"Please don’t…"
un "Eh, don’t have time anyway, gotta continue the commentary."
"{i}*Phew.*{/i}"
q "The horse chuckles."
th "Wouldn’t say it’s necessarily ‘mine’ per se, but I was the one to come up with the idea and coordinate the work."
th "It’s a special place for the summoners to come together and hang out, or practice, or study."
th "Of course summoning ‘for fun’ is not allowed inside a barrier, but here we’re free to do whatever we want."
y angry"Shut the fuck up!"
th "Excuse me?"
y awkward"S-sorry, that was directed at this beauty right here!"
q "Your gaze falls on a tire swing hanging from a low sturdy branch."
q "Memories of your childhood come rushing in, and the desire to ride something that is not a man for the first time takes over."
q "At least your reaction is accepted by the horse, as you run towards the swing."
th "Ah, that, heh."
q "He watches as you walk around the swing, contemplating how to use it."
un "Although the courtesy would be to ask if you can use it in the first place…"
y sadsmile"Uhm, may I?"
th "I’d be insulted if you didn’t try it, let me help."

q "He bends down and lets you use his hands as a stool, the tire being hung unusually high."
q "You put your legs through the hole one by one, then hold tight as the rope makes the tire swing and rotate uncontrollably for a moment."
scene swing with llongdissolve
scene CGt3
q "You look at his grateful eyes, as he leans on the nearby tree, taking the responsibility of pushing you lightly, over and over since your feet don’t touch the ground."
th "How do you feel?"
y ec"Ten years younger."
th "I can see that by your beautiful smile."
q "You get flustered again, for the...I lost count, as your legs swing playfully like a nine year old."
th "Isn’t it curious how a thing so simple can bring so much joy to the most unexpected people?"
y smug"Am I that unexpected?"
th "Just because you’re shorter with a thin and sexy body, doesn’t mean it doesn’t come with a bit of a surprise."
q "You know it, I know it, everybody knows it, your face is once again, red as...something very red."
q "Like fresh tuna, yes."
Q "From now on, every time you get flustered or embarrassed from someone complimenting you, I’ll play this sound:"
play sound "audio/womp.mp3"
"..."
"Please, for all that is sacred, choose another sound."
q "Eh, fine, I'll use this one then:"
"..."
play sound "audio/fluster.mp3"
q "I just need any sound so I don’t have to make meaningless comments on your feelings all the time."
"Understandable."
y s"Were you against the idea of a swing?"
q "Therium looks over the swing for a moment before responding."
th "It was my idea, actually."
y surprised"Really?"
th "Yes, why? Just because I’m a bit bigger than you physically doesn’t mean I don’t like fun."
th "Besides, I’m only a year older than you."
y sadsmile"It’s just that you’re so proper, kind of like Dallan, but less tied down by rules."

th "Heh, if you ask anyone, they’d tell you it’s an honor to be compared to that wolf."

y simple"But...not you?"

th "I like Dallan, if that’s what you’re asking."

y "But there is something about his ways you don’t agree, is that right?"

q "He looks surprised."

th "My, you are one smart cookie."
play sound "audio/fluster.mp3"

th "To be honest, I just have different views on the world, compared to other people."
th "It doesn’t start with the Defender’s leader and it doesn’t end with him either."

th "In any case, let’s change the topic."
th "I assume you must have many questions."

y ec"Yes! Oh man, so many, such as..uhmm, this will definitely sound dumb, but how do I even summon something?"
th "Ha, it’s not dumb at all, first years are not expected to be able to summon anyone until the end of the first semester."
y s"Ah, that’s good to know."
th "Do you have any summoning crystals?"
y "Nope."
q "He looks surprised."
q "You search through the backpack upon seeing his reaction."
y sadsmile"W-well, I had one I was using as a flashlight once, uhmm, it must be here somewhere, but it’s probably dull at this point."
th "No, don’t bother, the ones used for light don’t work for summoning."
y simple"Oh."
th "Huh, so you really don’t know anything, do you?"
y pf"Ouch."
th "Sorry, I mean, nothing about summoning, I was just expecting a recommended student to have at least some knowledge."
y s"I was mostly chosen based on my magic alone."
y "I never really expected to actually join the Summoners."
th "So what made you change your mind?"
y pf"A...a friend, I suppose."
th "A friend?"
y s"Yeah, he’s a big fan of Summoners and Nightfallen, but it’s a delicate matter."
th "I see."

th "Well, a little context then:"
th "We have the day to day energy crystals, the ones we buy at the store, prices don’t even reach triple digits usually."
th "Do you know where those types are collected?"
y simple"I assume from weak Nightfallen?"
th "Bingo, the weakest of them all, some slimes here and there, maybe a low tier mimic."
th "Those can store energy like a battery within them and are the only ones that can be easily recharged by simply not using them for a while."
th "Obviously they don’t have that much power to them, only used for flashlights, lightbulbs and such."

y "I’ve seen people summon weak Nightfallen too, how do they do that?"
th "Not any crystal can be used for summoning."
th "Their gems must be collected with care to be used for summoning, if the Nightfallen was killed, the gem is lifeless."
th "Nothing more than wasteful energy."
y "Oh...so we don’t kill them?"
th "We’ll leave the killing to the Slayers and Sorcerers, we’re here for the fun part."
y pf"So do we still…"
th "Fuck them? Yes."
y blush"Great- I mean, good to know!"
th "Heh."
th "As a summoner you’ll learn more about that over time."
th "We could go back to the academy and get some for your level…"
q "I smell a choice menu coming up."


menu:
    q "Desperate to stay here with your new man and your swing, you quickly think of a new question and topic."
    "What about those auditions, ey?":
        $ auditions +=1
        jump auditions
    "What? That's the only question you can think of?":
        $ auditions +=1
        jump auditions
    "Who designed this menu?":
        $ auditions +=1
        jump auditions
    "Oh, wait, there's another one!":
        $ auditions +=1
        jump auditions
    "Nevermind...":
        $ auditions +=1
        jump auditions
    "I hate it here...":
        $ auditions +=1
        jump auditions
    "How about your own Nightfallen?":
        $ nightfallen +=1
        jump nightfallen
    "Would you look at that, I was wrong, there is another choice.":
        $ auditions +=1
        jump auditions

label auditions:
th "This year I’ve heard the Headmaster wants to do them publicly."
th "The summoning auditions are never very fun to watch, at least not for first years, since as I said before, most of them don’t manage to summon much."
th "After that it’s practice sessions for everybody else."
y s"Will you partake in a practice session?"
th "No, that’s once again only for the fresh meat."
if nightfallen <=0:
    jump nightfallen
else:
    jump afteraudnig
label nightfallen:
y "How about your own crystals? Do you have any?"

q "Once again, your question stuns him for a fraction of a second."
th "I do...but, they’re too advanced for you."
y sadsmile"Can you at least demonstrate what I have to do?"
q "He thinks some more."
th "Fine, I have one you might like."
th "Here, let me show you."

q "He takes out a small gem, keeping it tight between his fingers in front of you, but at a safe distance."
th "First, the most important thing is knowledge, you need to know who you’re about to summon."
th "It is impossible for you to, let’s say, steal my crystal without knowing what kind of Nightfallen resides inside it."

y worried"I would never do that!"

th "I know sweetie, it’s rhetorical."
play sound "audio/fluster.mp3"
y simple"Yeah, but still, who would want to steal someone else’s Nightfallen?"



menu:
    th "Why wouldn’t they? They’re just tools to be used, aren’t they?"
    "You’re right.":
        y simple"Yeah, for summoners at least."
        y "And for anyone who needs energy crystals, of course, although...maybe materials or fuel is a better word than tools in that case."
        th "I see."


        $ thepoints +=-1
        if auditions <=0:
            jump auditions
        else:
            jump afteraudnig

    "I don’t think so.":
        y simple"I wouldn't say {i}'tools'{/i}. More like companions, or familiars, or pets."
        y pf"Maybe even friends, don't call me crazy for saying that."
        th "I see, so that's what you really think? A unique view, but definitely not crazy."
        $ thepoints +=1

        if auditions <=0:
            jump auditions
        else:
            jump afteraudnig

label afteraudnig:
q "The horse keeps pushing your tire away gently each time you come close to him, and you’re having more fun on the swing than you’d like to admit."
th "Now, as per your earlier request, my lord:"
scene swing2 with llongdissolve
q "He concentrates for a moment, then the blue gem in his hand starts to glow, an animalistic figure getting conjured at his feet."
th "Meet Sparky."
q "An alien-like puppy appears, panting its tongue and immediately jumping at its owner's feet asking for attention."

y sadsmile"Awwwww!"

y "Can I...pet him?"
th "Sure, he likes strangers."
q "You reach down and place the tip of your fingers on its forehead, the fur is soft, but thick, with an almost otherworldly texture, if you closed your eyes to ignore its antennas or multiple eye sockets, you’d definitely think it’s a dog of some sort."
q "This makes you a tad sad, something that the horse notices fast."

th "What’s wrong? Is he so much weirder than you thought he’d be?"
y "No...the opposite in fact."
y "I think it’s sad someone would kill this little fella."
y "Considering it’s not even the kind you can, umm, charge with energy."
th "True, his gem wouldn’t even be able to generate enough power to power a light bulb."
th "And they can’t procreate either so there’s no reason to get rid of them."
y simple"It does raise some questions."
th "You know what, that’s the kind of stuff they’ll teach you about later on, there was never a year when somebody didn’t give the Ethics professor a major headache."
th "Do you know Chelsie?"
y "The Defender’s Shard viceleader, what about her?"
th "When she was a first year, one of the first things she did in her second semester was release all the captured Nightfallen from their crystals."
y "How did she do that? And more importantly why?"

th "She is magicless, so technically she didn’t do it, but she convinced someone to help her."
th "She agreed to stop and help recapture them after her scholarship was on the line."

th "As for why?"
th "The morality of the common, uninformed people got to her, to put it simply."
y "What does that mean?"
th "Cruelty against any living being, no matter the reason, is seen as a sin for anyone that doesn’t work in the field, that don’t know any better."
th "And you know what they say, if you can’t beat them, join them."

q "You nod in understanding."
y "The person who helped her-"
th "No idea, couldn’t tell you even if I wanted to."
y s"It was you."
q "For the first time, such sudden information coming from you doesn’t stun him anymore, he keeps quiet and looks down at the little Nightfallen, continuing to smile as he did before."
th "It was I, indeed."
th "I suppose I’m the main bad guy in that story now."
y "Not at all."
th "huh?"
y "Well, both of you did what you thought was right, and since nobody was hurt and it seems like you’ve never done it again either, you’re all good in my eyes."
th "Hmm."
th "You know, [name], I don’t think I gave you enough credit."
th "Not knowing anything about summoning doesn’t make you less important than someone else."

y pf"Did...did someone say something about me?"

th "Well, this is a bit of a secret, but if you promise not to tell anyone, I don’t mind sharing."
y s"I promise, now who’s the traitor?"

th "Do you remember Alvy? The other recommended student of the bunch?"
q "Your mind cringes remembering your earlier encounter."
y awkward"Yep, something sounds familiar about that name."
th "He’s going to join us, as a summoner."
y "Ooooohhh, that’s just greeaaaaaat...we’ll be in the same Shard, every day, all year, for five years, can’t wait."
Th "I’ve met Alvy as well, and I must say, you two have a lot in common."
y simple"How so?"
Th "First years, recommended students, shy, extremely cute and very talented in summoning."
y surprised"I’m not talented! I literally know nothing!"
th "Really? Not knowing how, doesn’t mean being unable to."
scene swing with dissolve
q "The puppy Nightfallen transforms into blue smoke and vanishes into the crystal."
th "Now you try, I’ll hold onto it and help you when needed."
q "You do as he says, reaching for the crystal with your fingers and thinking really hard about the small Nightafllen, trying to will it into existence."

q"You try to summon it as well, but something feels wrong."
q"Something about the crystal reminds you of...me."
q"At that moment, a small shock zaps the crystal, launching the puppy Nightfallen outside like a projectile." with hpunch
y worried"AH!"
y "Sparky! I’m sorry!"
q "Thankfully, the Nightfallen’s fall was highly reduced by the thick bushes and soft grass bed."
q "It comes back quickly, wagging its tail and breathing heavily with its tongue out, switching its attention away from his master for the first time."
scene swing3 with dissolve
th "It looks like he liked that."
th "And you."

q "The puppy runs around you trying to jump on your lap as you lightly swing back and forth, scratching your pants with its dull claws."
th "Alright, that’s enough."
q "He recalls the Nightfallen and gives you a curious look."
scene swing with dissolve
th "hmm..."
q"He grabs your tie as the swing gets close to him, holding you in place, and gets his face closer."
y blush2"W-whoa-"
q "Your snouts are only an inch apart, making your lips just as close, but his burning eyes make you stay away, even if they only contain curiosity and a bit of mischief."
th "Are you sure you’ve never done this before, [name]?"
q"A soft smile across his face, delicate, with a hint of slyness."
q"You can’t help but fill both cheeks with the warmth of blood as your eyes try not to widen too much."
y "I-I swear!"
y "I’ve never even held a summoning gem before, only the mundane day-to-day ones."
y "I’m not sure how I did it."
th "Interesting."
th "What are your powers, if I may ask?"

y"Energy manipulation!"
q"You reply hastily as if his simple question was an order."
q"He chuckles."

th "And you dare think even for a second you have no talent."
th "[name], you’ll be summoning Savage Furs out of these crystals in no time."


q"The tension in the air suddenly drops with your tie, the gentle swings of the tire rejoining its lazy trajectory."

y simple"What does that have to do with anything?"

un bored"It means you’re a special bitch, congrats."

th "Energy users are supposed, in theory, to have a very strong connection to these crystals that Nightfallen reside in."
th "I can’t say too much on the topic, since not much is known about it."
Th "There are like, what? Ten, fifteen people like you in the world?"
th "Needless to say, you’re in luck."

y sadsmile"It’s hard to believe I’m anything special…"
y "After all, all I can really do with my magic is throw some energy balls that leave me exhausted and charge phones, maybe give you a little zap too, but that’s about it."

th "You don’t need to be able to use spells to summon, all you need is a large magic pool, which you have plenty of, it seems."

th "But nevermind the Nightfallen and magic talk."

th "About those auditions, I was going to put a good word for you in case you really were as worthless as you keep saying you are."
y simple"Ouch, I stand by my words, but ouch."
th "I doubt that’s true."
th "In any case, I also doubt there is anything that can keep you out of the Shard."
th "We’d be fools to refuse you."
play sound "audio/fluster.mp3"

y blush"Stop, you’re making me blush."

th "Have I not been doing that with my flirting attempts earlier? Shame on me, I’m getting old."
y blush2"No you’re not! I-I mean, it works, trust me, it works really well, I’m just a bit overwhelmed."
y blush"I’m not, umm, used to this kind of stuff."

th "Are you saying you weren’t the heartthrob of your friend group?"
y "Not by a mile."
y pf"{size=*0.5}I’d need friends for that.{/size}"
th "What was that?"

y awkward"I’m just mumbling, hey, here’s a seamless subject change for no reason in particular:"

y "What is the gem you keep as an earring?"
th "This old thing?"
th "I use it to summon objects mostly."
th"I keep it close, since, you know, objects are not banned inside the barrier, Nightfallen are."
y surprised"That is so useful! So like a dimensional pocket?"
th "Not quite, since these objects are not real, they disappear after a short while."
th "I can use a stool to get something from a high place, a rock to throw at somebody, or even-"
y simple"A what?"
show bluerose with dissolve
q "He touches his earring and a beautiful blue rose in full bloom appears in his hand."
th "Give pretty boys a parting gift."
play sound "audio/fluster.mp3"
pause 0.5
play sound "audio/fluster.mp3"
pause 0.5
play sound "audio/fluster.mp3"
q "You look at the rose with a surprised awkward smile, not knowing what to do, neither about the flower nor with your flustered face."
q "You get a hand free from the tire swing and reach for the rose."
y blush"W-well, if you insist, and if this really is goodbye-"
scene swing with dissolve
q "More blue smoke makes it dissolve back into the crystal."
th "Of course, that’s what I’ll give you when we finally part ways, which won’t happen now."

y blush2"Huh?"

th "Dinner time approaches, and I want to treat you, there is no way I’m letting you slip through my fingers just like that."

q "With all the Summoning talk, the fun swing and the sexy man in front of you, you haven’t even realized that the sun is soon to come down."



y sadsmile"I’m...really enjoying your company, so I’ll take you up on that offer."
y "It also helps that I’m super hungry, our snack break did not make up for skipping lunch."
th "That’s why I must atone for my sin, keeping you hungry or in need is not something I ever want to do."
y blush"You sure have a way with words."
th "Judging by your red face it’s in a good way?"
y smug"No comment."
y simple"Although, isn’t it still a bit early to go?"
y "I feel like we’ll be the first and only ones eating that early."
th "We have an important stop before dinner, and it might take some time."
q "Your mind filters out his last sentence, for the sake of food."
Y s"Where are we going to eat? I bet this town has many great places."
th "The cafeteria is a nice place, a bit crowded at times but the food is delicious."


th "Now come on, it’s time to meet your new leader."

y "Seriously? He’s ready?"
th "Allegedly."

scene forestsummoner with llongdissolve
q "He helps you get down from the tire swing, not without some grunts of protest from your side."

th "You really like that thing, huh?"

y smug"I like riding things, can you blame me?"

th "Oh, noted~"
stop music fadeout 2.0

q "Slowly, very very slowly, you come to terms with what you just said, and spend the way back getting redder and redder thinking of the implications."
play sound "audio/fluster.mp3"
scene chibitherium4 with dissolve
play music "audio/forgetmenot.ogg" fadein 2.0
q "The horse didn’t seem to mind though, with a grin plastered on his face and eyes focused on the path back to the academy."

q "He guides you all the way to the main building, your eyes glued to his back and your hands also glued to him, but not metaphorically...literally...with sweat...gross."
"I’m nervous ok?!"
"Both because he’s holding my hand and because I’m about to meet my new leader!"
q "Your emotions are somewhat understandable, yet exaggerated."
q "Either way, at least they made the time pass fast."
stop music fadeout 2.0
scene theriumoffice with llongdissolve
q "Before you know it, the horse opens up a door, the summoners leader’s office."
play music "audio/horse.ogg" fadein 2.0
q "A familiar face with wide eyes greets you on the other side."
show alvy shy at right with llongdissolve
y awkward"{size=*0.5}Here we go...{/size}"

show horse frus at left with dissolve
th "Ah, good, you’re here. What a punctual little man."
q "Although his voice is bubbly, his greeting seems forced."
q "Every time his head turns from you to the dog, his smile fades ever so slightly and his expression sours."
q "The seconds of silence feel like an eternity, and something in you just can’t take it anymore, time to cut the tension."
show alvy at right
y ec"Hi! You must be Alvy, I’m [name]."
show alvy shy at right
q "You extend your hand for a shake, but the dog seems reluctant to accept it, understandably so, in his eyes, you still haven’t proven you’re not a lunatic."
q "No touching will be done in this room for now, but he does, at the very least, return your greeting."
show horse phone at left
al "Hi."
al "…"
show alvy at right
al "We..we’ll be Shard mates now, aren’t we?"
y s"Yup, that’s if we pass the auditions, but I’ve heard they’re fairly easy, so there’s nothing to worry about, right, Therium?"
q "He’s busy looking at his phone’s empty notification screen, and bumping his leg restlessly, completely ignoring you while the frown on his face intensifies."

th "Yeah yeah, sure."
th "Respond already you damn-"
play sound "audio/notification.ogg"
q"Phone rings"
show horse ec at left
th "Finally, sorry, you two discuss further about...whatever, I’ll be back in a sec."
hide horse ec with moveoutleft

q "He slams the door after walking out, a new kind of awkward silence taking over the room, a silence so awkward it needs its mom to make a doctor’s appointment for it."
q "So awkward it stayed at home during prom because it couldn’t bring itself to ask anyone out."
q "So awkward it never answers phone calls, only texts."
q "So awkward it-"
show alvy shy at right
stop music
y angry"I GET IT!"
q "…"
al "…"
y simple"…"
y pf"Sorry."
y "…"
y "I’m very normal, I swear."
al "Ok…"
q"Door opens."
show alvy at right
show horse bored at left with moveinleft
play music "audio/horse.ogg" fadein 2.0
th "Well, just got some...shitty news."
th "The leader is no longer coming today, there are some complications on the way."
y simple"Are they alright?"
th "More than alright, I’d almost say they’re amused at the situation."
th "Almost as...they like to see certain people suffer for no reason."
al "That sounds concerning."
th "It’s nothing to worry about, not for you at least."
y "So we’re not meeting the leader, does that mean we can’t get out benefits?"
show horse sweat at left
th "Umm, yeah, sure."
al "Can’t you do the paperwork? You’re a vice leader, you have the authority."

y "Yeah, we shouldn't need a leader for something so small anyway, surely the rules can be broken when there is no leader at all."

th "True but...I don’t-"
show horse sweat at left2 with move
"The horse looks around the room, paces for a bit, then looks at you two contemplating, he seems uneasy, fidgeting with his hands and almost shivering."
show horse phone at left2
th "He takes out his phone again and dials a number, then hurries towards the door without looking back."
hide horse phone with moveoutleft
th "Just wait here!"


y "Bummer, no leader and the vice leader is…"
show alvy simple at right
al "Having a mental breakdown…"
y "Yup."
show alvy simple at right2 with move
al "What’s his deal?"
q "Happy that the dog is actually conversing with you, you try your best to be as normal as possible, for real this time."
y "I’m not sure. I spent the day with him and he did have some shifts in emotion, but not like that."
al "You don’t seem too surprised either way."
y "You don’t look surprised either."
show alvy sadsmile at right2
al "I’ve already made my peace that everyone is a weirdo around here."
q "Surprisingly, he glances at you with a soft smile."
y s"Hah, you’re right, but I think it’s the good kind of weird."
al "For some people I agree for others I-"
stop music
play sound "audio/kick.mp3" volume 0.6
show alvy sur at right2 with hpunch
show door at right with moveinright
hide door with moveoutleft
q "Speaking of weird people, the door gets knocked off its hinges and it flies past you two."
q "This time, this ‘weird’ action did get a reaction out of both of you: a scared reaction, a fight or flight reaction."
play music "audio/catjazz.ogg" fadein 2.0


ch "LISTEN UP, YA CHUMPS!"
show chelsieangry at left2 with moveinright
show alvy sur at right with ease
q "An eccentric raccoon girl, the culprit behind the flying door, comes in with high demands."
ch "I WILL NOT TOLERATE THIS! THIS IS TREASON! I DEMAND A WITCH TRIAL!"
y simple"Hi?"
hide chelsieangry
show chelsiemad at left2 with hpunch

ch "Ooooooh [name], you’re making mama MAD!"
y worried"Umm, why? What did I do?"
show wolf20awkward at center with moveinright
d "Come on Chelsie, let them breathe; it’s not the end of the world."
ch "It’s MONEY Dallan!"
y "Context please?"
show alvy at right
d "Sorry, we came in with the wrong foot."
y pf"You literally came in like a wrecking ball, that’s more than a wrong foot."
ch "And rightfully so."
hide wolf20awkward
show wolf20sadsmile at center
d "Well you see, Therium messaged us and asked if we could help with your benefits, since the Summoner leader isn’t here yet and he said he has some business to take care of."
y simple"What kind of business?"
d "He didn’t specify."
hide chelsiemad
show chelsiebored at left2
ch "Aghem."
ch "Me, he asked me, actually. Me specifically."
hide wolf20sadsmile
show wolf20ec at center
d "Yeah yeah, I know, but I just couldn’t miss the opportunity to say hello to yet another recommended student, and hearing [name]’s voice is always a delight."
y blush"Aww, thanks, I like hearing… and seeing you too."
d "Hmmm?"
y s"Oh, yeah, Dallan, this is Alvy, Alvy, this is Dallan."
show alvy shy at right
d "Nice to meet you! I hope you’ll have a great stay at the academy!"
al "Thanks…"
ch "Would be a better stay if you were a Defender, just sayin’."
hide wolf20ec
show wolf20sadsmile
d "It’s fiiiine, Chelsie, it’s their choice."

ch "Don’t you have stuff to do, mister leader man?"
d "I… do but-"
ch "Sweety, you can’t treat all recommended students like your own little escapade."
d "But I don’t know where Aiden and Tate are… and you’re busy too."
ch "Since when do you not want to do work?"
d "Since…"
q "He looks at you with puppy eyes, ears dropping a little while his smile widens."
d "Never mind, you’re right, I should really go."
d "Please don’t traumatize them."
ch "No promises!"

hide wolf20sadsmile with moveoutright

q "The wolf walks away while waving goodbye to all three of you."
y simple"Hey so..."
y pf"I couldn’t help but notice you walked in a little mad at us… why?"
hide chelsiebored
show chelsieec at left2

ch "Oh that? Don’t worry about it! I mean, you did cost me about a 60 percent salary increase by not joining my Shard, but it’s all good. Your choice, as Dallan said, haha, I’m not going to get revenge or anything."
show alvy worried at right
al "I’m scared."
hide chelsieec
show chelsiesmug at left2
ch "I’m just kidding, we still got a recommended student, and the sorcerers as well. Poor slayers though."
ch "At least we’re not them."
show alvy at right
ch "Anywhooo~"
show chelsiesmug at left with move
q "She walks toward the computer and starts typing away, focused on the screen but that doesn’t stop her mouth from talking."

ch "Dallan made a point that I should congratulate you for managing to get this far and for choosing a Shard and yada yada, you get the point."
y simple"Thanks?"
hide chelsiesmug
show chelsiemad at left
ch "Damn it, Therium seems like such a proper and meticulous guy but his database is a damn mess."
hide chelsiemad
ch "What are your full names again?"
y"[name] [name2]."
ch "Weird."
y worried"It’s not!"
y "Therium said it's nice."
ch "We all lie from time to time, don't take it out on him."
y bored"I'M NOT-{i}*sigh*{/i}."
ch "And you little guy?"
al "Alvy..."
ch "Aaaaand?"
al "Arufar..."
ch "Huh, a rich boy."
q "The dog doesn’t seem to like the comment, less so than you and your weird name."
"It’s not weird!"
show chelsie at left
show chelsie at left2 with move
ch "Ok… yeah, you’re good, all done."
ch "Officially welcome to the academy. You are now both members of the Summoner’s Shard, of course, the title can be removed if you don’t pass the auditions. But then maybe you’ll join the Defenders instead."
ch "Hmm, that gives me ideas…"
al "We..."
hide chelsie
show chelsiesimple at left2
al "We were already members."
ch "Oh..."
hide chelsiesimple
show chelsiepf at left2
ch "What am I doing here again?"

y simple"We just needed the food cards? At least I think so."
hide chelsiepf
show chelsieec at left2
ch "Oooh, that, of course."
show chelsieec at left with move

ch "Click click clickity click."
ch "Click."
ch "Boom. Easy as that."
show chelsieec at left with move
ch "Your card's balance iiis-"
play sound "audio/scratch2.ogg" volume 0.5
hide chelsieec
show chelsiebig at left with hpunch
ch "{size=*1.5}OH MAMA THAT'S A LOT OF MONEY!{/size}"
hide chelsiebig
show chelsiesmug at left
ch "I mean-"
ch "I have one too, no big deal, I'm cool like that, haha."
al "And those cards are...where?"
hide chelsiesmug
show chelsieec at left
ch "Oh, here!"
show chelsieec at center with move
q "She takes out two small metal cards from between her breasts and hands them to you."
ch "Always wanted to do this."
y bored"Of course you have."
al "They’re warm."
y "How long have they been in there?"
ch "Less than a day."
y "Concerning still."
hide chelsieec
show chelsie zorder 1
ch "Are you done with the meaningless questions? We have stuff to discuss still."




ch "Such aaaaasssss-"
show alvy sur at right
show book zorder 2 with hpunch
q "She takes out a small book from between her breasts."
y pf"How many things do you have in there?"
ch "Shh, it’s for comic relief, just accept it."
al "I need to sit down."
hide alvy sur with moveoutright
ch "Great idea, Dallan would be very upset if I don’t read every single word from this."
ch "The Summoner’s rule book!"
ch "Buckle up, this will be a boring ride."
ch "Aghem."
q "You take a seat next to the worried dog, who looks a little pale."
q "Poor fella just can’t avoid weirdos."
ch "Let’s start with the most important ones: Students shall not enter the leader’s office without the leader or vice leader present, for that is where the Shard’s gems are to be stored."
show chelsiepf zorder 1
hide chelsie
ch "We kind of broke that one already..."
hide chelsiepf
show chelsieec zorder 1
ch "So to the next one!"
show chelsiepf zorder 1
ch "The door of the office shall always stay closed… Does it count if the door is off its hinges?"
show chelsiesweat zorder 1
stop music fadeout 2.0
ch "Anyway, next one!"
scene black with llongdissolve

"Meanwhile..." with llongdissolve

play sound "audio/knocking.ogg"

h "Ah, enter, mister [name2]."
play music "audio/hm1.ogg" fadein 2.0
play sound "audio/dooropen.ogg"
scene hmoffice with llongdissolve
show headmaster20foxy with dissolve
h "Great timing, I was just-"
show headmaster20angry with dissolve
hide headmaster20foxy

th "Hello, mister Kiraman."

h "Therium… I was not expecting you here."

th "Well you probably expected somebody to pick up that luggage, right?"
"I glance towards the bag next to the lion’s desk."

h "Yes, of course. Somebody like its owner."
h "It’s going to have to wait for [name] to come pick it up."

th "Mister [name2] is busy with Shard business. He will not be able to accompany you today, yet he needs his things."
hide headmaster20angry
show headmaster20smile1
h "Accompany? I think you have the wrong idea, I just wanted to protect his personal belongings, I can’t just give it to anyone barging in."
th "I am a vice leader; I am aware and accept any consequences if my new Shardmate complains about stolen or missing items."
th "Surely you don’t think I’ll leave the country with a random first year’s things in a burlap sack on my back, do you?"
hide headmaster20smile1
show headmaster20foxy
h "Of course not, you are the last person to set foot outside of this country."
"His comment scrapes my ears, making them twitch, but I let it slide."
Th "Wrong words to focus on from what I said."
h "I think they were pretty accurate."
h "What kind of ‘Shard business’ is he up to? His vice leader isn’t around and not to mention the leader, who hasn’t arrived yet."
h "Didn’t think you’d just leave him alone like that, since, you know, all the leaders want the recommended students in their Shard."
h "There must be a reason."
th "The reason does not concern you."
"The large lion gets up from his table, slowly grabbing the leopard’s luggage and dragging its wheels towards me."
h "Daring today, as always. Here."
th "Thank you, Headmaster."
h "Tell him to be more careful next time. The wrong people might get a hold of his chattels one day, and we wouldn’t want that to happen."
th "I’ll see what I can do."
stop music fadeout 2.0
th "Good day."
scene black with llongdissolve
play sound "audio/wind.ogg" volume 0.2
"I walk out, scraping the floor with the one non-crooked wheel of the luggage bag following my heels."

"Unfortunately for me, the deep frown forming on my face has to be hidden, yet."
"It’s not enough that I had to stay in the same room as those two. Their faces together almost made me vomit, but I just had to talk with this man again as well."
"This day just keeps getting worse."
"No matter how much I want to make the frown known, maybe some other time. Maybe if I snap one day, but this is not that day."




stop sound fadeout 2.0
"Back to you…" with llongdissolve
scene theriumoffice with llongdissolve
play music "audio/catjazz.ogg" fadein 2.0
show chelsie with moveinright
ch "And that is why you never summon Nightfallen inside the barrier."
ch "Now for the part Dallan loves the most! Class cleaning duty, sanitation days and-"
hide chelsie
show chelsiebored
alvycody "{i}*snoooore*{/i}"
ch "Wish that were me...*yaaawwn*"
hide chelsiebored
show chelsiemad
ch "Wait! No, Chelsie, you have to do this for your friend!"
ch "Hey!"
ch "Wake THE HELL UP!" with hpunch
Y surprised"Agh! Wasn’t sleeping!"
show alvy sur at right with moveinright
al "Totally awake!"
hide chelsiemad
show chelsiebored
ch "{i}*Sigh*{/i} Should’ve accepted Merina’s proposal to come too, at least for the company."
show alvy simple at right
al "Excuse me, but why do the rules have to be read to us two in particular?"
ch "I dunno, ask someone who cares."
al "Oh."
stop music
hide chelsiebored
show chelsiesimple
m "Because you two missed the Shard’s group rule reading, and Dallan wanted to make sure you’re familiar with them."
play music "audio/slowpiano.ogg" fadein 2.0
show merina20sadsmile at left with moveinleft
y ec"Merina!"
hide chelsiesimple
show chelsieec
ch "My thoughts summoned her!"
ch "Her and her accompanying angelic background music!"
un "{size=*0.5}You're not the only one who hears it?{/size}{nw=2}"
ch "Thank God you’re here, I should go get the toolbox for that door…"
m "Yeah, you probably should."
hide chelsieec with moveoutright
show alvy shy at right
m "Hey [name], I’m glad we got to meet each other at the gathering, but I heard some other recommended student can be found here and I couldn’t keep away."
al "That would be me...Umm, does anyone else know where to find me out of the blue?"
hide merina20sadsmile
show merina20 at left
m "Probably, it didn’t take me too long to find the information."
al "I see…"
y sad"Sorry, I know, you’re probably disappointed too."
hide alvy shy with moveoutright
m "Disappointed? I don’t think so, unless I should be for some reason?"
y simple"Just that we didn’t join your Shard. Chelsie seemed upset by that."
hide merina20
show merina20sadsmile at left
m "Oh don’t mind her, she’s the only one who cares much. Besides, we got one too."
y s"Really?"
y "Hey, maybe we two should go meet-"
q "You look to your side but nobody is there; the dog has vanished from his chair and from the room."
hide merina20sadsmile
show merina20simple at left
m "Huh, he’s quick. I didn’t even notice him disappear."
y sadsmile"He’s shy, I think."
hide merina20simple
show merina20 at left
m "Heehee, checks out for a summoner.{nw}"
stop music
th "Aghem."
play music "audio/horse.ogg" fadein 2.0
q "The horse stands by the...hole where the door was supposed to be, or where it soon will be again as the raccoon girl struggles to screw its hinges back."
m "Oh, looks like your ride is here. I’ll leave you to it; good luck [name]."
hide merina20 with moveoutleft
y ec"Thanks a lot!"
ch "Don't forget about my party, Merina!"
m "I'll try to."
ch "Haha, yeah."
ch "Wait...you'll...try? What do you-"
ch "HEY! COME BACK HERE!"
show horse with moveinright
q "The horse squeezes through and approaches you with a new-found smile, his usual personality returned."
y s"Hey Therium, are we- I -free to go now?"
y pf"Alvy had to go…as you can see."
show horse smug
th "I heard he does that sometimes."
th "No matter, his job here is done anyway; we have no business with him."
th "And you’re all done as well."
th "Ready for dinner?"

y sadsmile"I’d almost forgot about food until I was presented with the lunch and dinner cards with unlimited money on them."
show horse simple
y ec"Dinner’s on me!"

th "...I have one too."

y simple"Oh."
show horse ec
th "But the thought is very much appreciated."
show horse
th "You haven’t seen the cafeteria yet, have you?"

y s"Nope, but as long as it doesn’t have stale, moldy pizza, and milk that looks and tastes like glue, it’s already better than my high school."
stop music fadeout 2.0
th "Oh don’t worry, the food there is great."
play music "audio/forgetmenot.ogg" fadein 2.0
scene chibitherium1 with llongdissolve
th "They commission different local restaurants every week, and the locals sure know their food."
y "Probably because there’s so much variety in immigrants."
th "That’s definitely a piece at play there. This is a heavily diverse town after all."
stop music fadeout 2.0
scene cafeteriaday with llongdissolve
play music "audio/guitar.ogg" fadein 2.0
q "The lively cafeteria, its noisy patrons and the smell of fresh, hot dishes fill all of your senses as the building comes into view."
q "A building the size of a small football field, with many small tents for outside seating."
play sound "audio/notification.ogg"
q "A phone rings."
show horse phone with moveinleft
q "The horse checks his phone with a frown."
th "God damn it."
th "Sorry [name], this will take one second."

y s"Don’t worry about it, maybe I can grab us a table in the meantime."
th "You’re the sweetest."
hide horse phone with moveoutleft

q "He walks away, the phone already to his ear."
y pf"Let’s see... How or where do I find some-"

t "[name]! Heeeeeeyyyy!"
show cat20
show tiger20bored at left
show wolf20 at right
with moveinright

q "You see the trio of men that attempted to adopt you earlier, waving at you from a table for four."
q "The cat seems the most excited to see you, along with the world, and even though the tiger shows no sign of happiness, he is the only one blushing out of the three."
d "How did the signing go?"
y s"Didn’t really sign, just got our cards and-"
t "Never mind that, how was your whole day?"
a "You should sit down; here, there’s an empty spot next to me."
hide cat20
show cat20simple
t "I’m sitting next to yo-"
hide wolf20
show wolf20awkward at right
show tiger20bored at center with move
hide cat20simple
show cat21mad
show cat21mad at right2 with move and hpunch
t "AGH!"
t "Bitch…"
show tiger20bored at left2 with move
show cat21mad at center with ease
hide cat21mad
show cat21mad2
hide wolf20awkward
show wolf20sadsmile at right
q "You sit down awkwardly at the edge of the seat."
y sadsmile"Thanks, but I can’t stay long. I was actually looking for a bigger place for me and Therium, he’s just around the corner, he had a phone call to take care of."
d "Aah, I’m surprised he’s still with you. We thought you’d be free after you signed in."
a "So he wasn’t using you to get a raise?"

y "No, definitely not. He’s also helping me with the auditions, since I’m kind of new to all this summoning stuff."
d "I take it that you’re the one who follows him around then?"
y s"Pretty much. I like to be a bother I suppose, heh."
T "Ah, so you want some horse cock."
hide cat21mad2
show cat21scared
hide wolf20awkward
show wolf20simple at right
hide tiger20bored
show tiger20simple at left
t "Eeep."
q "The cat closes his eyes and ducks, while you get as red as a beet."
q "The other two just look at you two in a very casual way."
hide cat21scared
show cat20
T "Huh, nobody’s gonna smack me this time? Nice!"
A "Well… I can’t deny that."
D "It’s plausible."
Y angry"HEY!"
Y worried"There is more to people than their personal… rods."

hide tiger20simple
show tiger20bored at left
hide wolf20awkward
show wolf20 at right

A "Yeah, like their holes."

T "Don’t forget their toes."
hide tiger20bored
show tiger20simple at left
hide cat20
show cat20simple
A "What?{nw}"
T "What?{nw}"


D "Come on guys, he obviously meant their heart."
hide tiger20simple
show tiger20bored at left
hide cat20simple
show cat20
a "Huh, didn’t know Therium had one of those."

Y simple"What’s that supposed to mean?"

D "That is, once again, an exaggeration. Therium simply likes to keep to himself."
D "Just a very private guy."
Y "Aiden, aren’t you kind of like that too?"
A "Well I-"
hide cat20
show cat20smug
t "He likes to fuck too much to hide in his room all day."
hide tiger20bored
show tiger20angryright at left
A "Can you fucking stop saying stuff like that so confidently?"
A "It sounds worse than it is."
hide tiger20angryright
show tiger20bored at left
A "But it’s true…"

y "Do you guys not get along?"
hide wolf20
show wolf20sadsmile at right
d "We do! At least whenever he actually talks to us instead of avoiding us."
hide cat20smug
show cat20
T "Actually, he’s helped me a lot before. The reason my forest fort is so awesome is because his Nightfallen cut down some trees for me."
hide wolf20sadsmile
show wolf20 at right
D "And he loves animals!"
D "A lot!"
A "Maybe a bit too much."
D "That’s not a bad thing."
A "Yes it is, when his love transcends animals and goes to Nightfallen."
hide wolf20
show wolf20simple at right
hide cat20
show cat20simple
hide tiger20bored
show tiger20simple at left
y "Sometimes that can be good too, right?"
q "They exchange unsure glances."
hide tiger20simple
show tiger20bored at left
A "If you’re the type to fall in love with a hooker, then sure, it’s a good thing in your eyes."
hide wolf20simple
show wolf20ec at right
d "Look at the bright side guys! The loner and the new kid are getting along!"
hide cat20simple
show cat20
t "Over there, I think he’s looking for you [name]."
y s"Yeah, I should go. Nice seeing you again."

d "Good luck with him."
a "Cya."
hide cat20
hide tiger20bored
hide wolf20ec
with moveoutright
scene black with dissolve
scene cafeteriaday with dissolve
y s"Hey, everything alright?"
show horse simple with moveinleft
th "Yeah, just friends from outside the academy checking in."
th "And looking at the state of things… we have a problem."
y simple"Why do you say-"
q "You turn around and scan the cafeteria."
y worried"Every single seat taken? Seriously?"
y "Damn it, it’s my fault. I got distracted and wasn’t looking for empty seats."
y sadsmile"It’s fine, we can get food and…sit on some stairs, or maybe just wait for someone-"
show horse smug
stop music fadeout 2.0
th "Heh, it’s fine [name], I anticipated this happening. It’s the norm at dinner time, especially at the start of the year."
play sound "audio/heart.mp3" loop volume 1.0
show lust with llongdissolve
th "Come to my place, I’ll cook us something quick."
y surprised"I..."
q "You were about to bark your response in an instant, when a weird mixture of thoughts and emotions take over your mind, almost pushing the narrator out."
un "What the hell?"
q "One of those thoughts is how the horse seems to have dialed down on the flirting and sexual remarks: why? Perhaps he considers you wrapped around his finger already, and there’s no point in trying, you think."
q "In any case, that last part, of a strong man owning you… of someone wanting you to be theirs… it-"
q "It ignites something, something more than a simple feeling."
"What’s… happening?"
un simple"Lust Rush."
"What?"
un sidee"Yyyyeah… one of the adverse reactions to me possessing you...basically cum brain."
"You little…"
play music "audio/guitar.ogg" fadein 2.0





q "There’s no time to for you to insult the demon inside your head of course, there are more pressing matters at hand, such as:"
menu:

    q "Do you try to ignore it and walk away with the horse, or refuse his invitation and find a way to relieve it? One is an investment, one a quick and well deserved release, choose wisely."

    "Try to ignore the feeling and continue on.":
        stop sound fadeout 2.0
        jump nosextime

    "Excuse yourself.":
        $ refuse_points +=1
        y lust"No thanks."
        th "No?"
        y "No…"
        y "You know… I’m kind of busy, and tired."
        y "I think I’ll just order some pizza and go home..."

        show horse hand
        th "..."
        y "..."

        Th "I’m getting veeery mixed messages here…"

        y "Sorry!"
        show horse simple
        "Damn it...this feeling is so strong I didn't even realize."

        th "So you’re refusing my invitation, is what I’m getting here?"

        y "Uhm, yeah… but not because I don’t want to accept! I just have to… I just… can’t right now."
        q "You are starting to sweat, you’re getting red, your heart is pounding faster and faster."
        q"The horse chuckles after moving his eyes up and down, it sounds like a defeated laugh."
        show horse sadsmile

        Th "I understand."
        Th "Well, I wouldn’t want to be a hindrance."

        Th "In that case, I guess we’ll see each other tomorrow, perhaps?"

        y "Y-yes, tomorrow! For sure!"
        y "Would love that!"
        y "Bye now!"
        stop sound
        jump sextime


label sextime:
$ yessex +=1
stop music fadeout 2.0
scene black with dissolve
q "You hurry off around the corner and stop by a dumpster, slouching down with heavy breaths."
scene alley with dissolve
un "What now?"
y"I don’t fucking know, you tell me!"
un "Just start jerking off or something, it’s not like anyone will see."
y "At this point that is not enough, I need someone to help."
un "Yeah… I’m feeling it too actually."
un "Everyone around here is a slut, you should be able to ask around and find someone."
y "Do you think I have time to-"

st "Dude, I am NOT setting foot in there."
st1 "Come on dude, that tiger is not gonna recognize you."
play music "audio/catjazz.ogg" fadein 2.0
show theboyz angry with moveinleft
st "Nuh uh, he almost killed me. He hates my guts, I don’t want my other ear shredded."
st1 "But nearly every slutty student is in there, there is barely anyone available."
st "Then let’s go to a brothel or something, or a club."
st1 "You and what money?"
st "I hate when you bring logic into sex talk…"
q "This is it, the stars have aligned. You catch a glimpse of the talking figures and conclude that they are good enough."
q "Attractive, available, but best of all: desperate."
q "You stand up from behind the dumpster, a little dizzy from the lust accumulated, and walk towards them."
show theboyz simple
q "They both notice you and instantly raise their hands."
st "We’re not perverts!"
st1 "We’re just browsing sluts-SEATS! We’re looking for seats!"
q "You roll your eyes, not in the mood to deal with this."
y bored"Names?"

j "Uhmm, jack?"
show theboyz angryspot
st "Don’t tell him, he might be a cop."

y bored"And you? NOW!"
show theboyz simple2
sp "Spot."
show theboyz pf
sp "Fuck."
j "Nice one."
show theboyz angryspot
sp "Look at him, he’s a hot, nerdy, demanding twink, I can't resist."
j "Your favorite, I know."
y pf"Where did {i}'nerdy'{/i} come from?"
show theboyz
sp "Sooo, what is a cutie like you doing here?"
y smug"Trying to see if there’s anyone up for a quick fuck round, interested?"
sp "Oh. He’s straightforward."
show theboyz angryspot
j "Say yes, dude, dude, say yes, say-"
sp "Obviously, I’m saying yes, man."
show theboyz
sp "We are actually interested, so your place or ours?"
show theboyz angryspot
j "Umm, my sister is crashing at our place tonight so… we can’t-"
sp "Dude! Shut. Up."
j "I just don’t wanna create awkward scenes you know how she is and you-"
show theboyz sadsmile
sp "I know, I know, I get it, sorry, forgot that-"
y "Let’s do it right here."
show theboyz simple
sp "What?"
j "Huh?"
y "Nobody is here, they’re all inside, and even if they do come outside we’re in a private enough space."
sp "Threesome with a smoking hot kitty from the academy and a hint of voyeurism?"
show theboyz simple2
sp "Hell to the yeah."
j "Seriously?"
sp "Come oooon, something like this doesn’t happen every day, do it with me."
j "Ok ok, just one question first, to see if you pass my test."
y "Shoot I guess."
show theboyz pf2
j "Do you swallow?"
y "Can’t swallow If you pump it directly into my stomach."
j "Fuck, he’s good, fine."
stop music fadeout 2.0

sp "Nice!"
sp "So, how do you wanna do this? Change-ups? Double stuff? Tag-team?"
label theboyzsex20:
$ persistent.unlocked_spotandjack20 = True
scene black with llongdissolve
play music "audio/dogs.ogg" fadein 2.0 volume 0.6
q "You roll your eyes once again, the feeling of burning lust nearly unbearable at this point. You’re just thankful you found someone to agree to this so fast."
scene codyroast1 with longdissolve
q "In mere seconds, you take off your belt and pants and throw them nearby with disregard for their safety. You approach the jackal, cupping his heavy crotch, making him moan already."
y bored"I’ll suck your dick while you fuck me; it’s simple and fair enough. Any objections?"
sp "No sir!"
j "Not one!"
q "Without another word you unzip his- nope, they’re already unzipped and his red, pre-stained underwear is all that stands in your way."
q "The growing erection in his underwear makes his overwhelming arousal and anticipation clear."
q "The hyena already has his cock out and ready, letting it rest on your butt cheeks while you savor the smell of the member in front of you."
q "At last you unwrap your present, revealing an impressive length that hits the side of your face. which you immediately start licking and working it with your tongue from the base to the tip, not forgetting to show his balls some love as well."
q "Of course these horndogs came prepared: the hyena took a second from his precious sex time to lube up his own shaft and your hole."
scene codyroast with llongdissolve
q "Thankfully, this Lust Rush has left your anal muscles relaxed and the adrenaline pumped into your blood makes the pain of him shoving an eight whole inches of thick meat into you bearable."
q "Quickly the hyena starts to move his hips, shoving his wet cock in and out with heavy slapping sounds, while his hands grip your love handles like he’s on the ride of his life. He might as well be with an ass like that in front of him."
sp "God daaamn this is some nice ass. You’re so fucking tight, don’t mind if I lose myself a little in there."
q "As for the Jackal, as soon as the tip of his cock hit the back of your throat he threw his head back and moaned at the sky, or maybe he’s asking God for forgiveness. All you know is that his eyes are rolled back and his tongue out and panting."
q "Silly jackal, he thinks that the back of your throat is the end. Clearly he’s never had a professional slut like yourself to show him how far that really goes."
q "You deepthroat his entire length until your snout hits his stomach, your long and soft tongue running along the shaft keeping it moist and slick."
q "One of the guys is gripping his own hips for dear life, the other is holding your hips, both of them in paradise."

q "As the pounding goes on, each passing minute brings your lust rush down bit by bit until, finally, you feel throbbing and groaning from both sides."
j "I-I’m close…"
sp "Me too buddy, let’s fill this slut up."
scene codyroast2 with dissolve
q "Their hips start rocking back and forth more in sync and move violently, until hot liquid spills all over your guts, as well as straight into your stomach, as promised before."
q "Jet after jet of seed filling you up, two horny men deep inside you, spitroasting you between them. If not for the pleasure felt along the way, these thoughts alone are enough to send you to climax, making you spray like a fountain onto the ground below."
q "Both of them hold their cocks inside you for a moment longer, savoring the moment as their cocks grow softer."

j "That was…. fucking awesome."
sp "Up top."
q "They high five each other on top of you, while their cum still drips from both your holes."
sp "Thanks dude, you take dick like no other, seriously."
j "Yeah, you took it like a champ, especially Spot's, and his cock is huge, I’d know."
sp "You’re making it weird again."
j "Sorry..."
q "Thankfully they do at least help you clean up a bit, though you’re probably going to need more than their wipes."
sp "Umm, I know they like to do this in porn movies sometimes, but I’m umm… I’m not cleaning you with my mouth, sorry."
j "Yeah I’m not sucking up Spot’s sweet, hot cum either."

y bored"Nobody’s making you do that, it’s fine."
stop music fadeout 2.0
scene black with llongdissolve
q "Indeed, any kind of sexual desires, at least the exaggerated lustful ones, are gone. All you really want, now that the sun is going down, is to get to your dorm room."
if from_gallery:
    # Reset the flag so it doesn't affect the normal gameplay flow
    $ from_gallery = False
    jump return_to_gallery
else:
    pass
scene alley2 with llongdissolve
play music "audio/catjazz.ogg" fadein 2.0
show theboyz with moveinright
sp "Ok, great, umm, one more thing, do you wanna go out on a date, or something?"
show theboyz simple
j "No no no no, you can’t."
sp "Huh, why not?"
show theboyz awkward
j "Becaaaause… I wanna date him too, haha, and we’d have to fight over it."
y pf"{i}'it'{/i}?"
sp "Oooh, right, I don’t wanna have to give up on our friendship because of a slut."
y "I’m right here."
show theboyz pf
j "Well you never told us your name, so what else do you wanna be called?"
sp "Hey, that’s right! I had a feeling I wasn't appreciated enough, but didn't know why."
j "Let’s go Spot, he clearly only values your huge, meaty, juicy cock and not your heart."
sp "I’m beginning to feel the same waaaay."
hide theboyz pf with moveoutright

q "They walk away backwards and around the corner, watching you through squinted eyes."
un "They do have a point… you could’ve at least told them your name."
y "Oh shut up, you made me clinically horny."
un "But hey, it ended up winning you a great time, huh?"
y simple"I could’ve had a great time with Therium instead…"
un "Not THIS great! You got spitroasted! Yeeey! Right?"
un "And lost your virginity too! What a way to go!"
un "Come oooon, repeat after me, ‘Hoooraaay spitroasts!’"
y bored"I’m hungry."
un "Killjoy."
y s"From the hit game Valorant?"
Un "What the fuck did you just say to me?"
stop music fadeout 2.0
scene black with llongdissolve
un "Seriously, I have no idea what that means..."

scene eveningtown with dissolve
play music "audio/evening.ogg" fadein 2.0
q "As you walk away from the cafeteria, you discover both good and bad news"

q "The bad news is that most places are not documented on the map, something to do with the internet and barrier issues…"
q "The good news is that finding a food place is one of the easiest things to do in this town, you just have to follow your nose."
q "Soon, you find that one pizza place you’ve been dreaming of for a while now and order a large pie with different kinds of meats, mushrooms, peppers and olives, as well as a bag of potato chips and, while you’re at it, some soda because why not?"
q "The order is ready after about ten minutes, and you walk home with the arousing thought of eating all of this by yourself."
y s"Arousing is certainly the right word for once."


q "It takes some time to find your dorm building, but thankfully the buildings themselves are some of the tallest around, other than the academy itself, so they’re easy to spot from a distance; it’s just a matter of finding yours."
q "The streets are already starting to get quiet, but the local establishments and shops are only now getting busy."
scene dorm with dissolve
q "The evening air was starting to get to your skin as you open the door to your dorm building."
q "The main corridor looks cluttered, but in a good way."
q "Magic items, books, and curios decorations on every shelf and every wall, with a grand staircase as the main attraction."
scene dormhall with dissolve
q "You walk up the stairs, admiring the ancient dust that hasn’t been cleaned off of some of the items along the walls for months, or longer."
Q "The key to your room is a digital card that you scan at the door."
q "Something isn’t working out when by your fourth attempt the door doesn’t open."
q "You think that perhaps you confused the room number, but upon a closer inspection you realize the key is brand new and has a protective layer that needs to be removed."
un "Dumbass."
y sleepy"Like you have any idea how technology works…"
un "I’d still find the solution faster."
y "I don’t have the mental capacity for this."
stop music fadeout 2.0
scene dormroomnight with dissolve
q "Outside is already dark. You turn on the lights and-"
q "Nope, the lights are not working."
y sleepy"Amazing first impression."
play music "audio/nightsounds.ogg" fadein 2.0
y sleepy"Eh, don’t need light right now, I’ll check out the details in the dorm tomorrow, for now I’ll just-"
q "You place the food and drinks on the table while your mind processes a catastrophe."
y simple"I..."
q "Biiiig fuck up on your part."
y bored"I forgot my damn luggage at the academy…"
y angry"How. Can. I. Be. So. Stupid?!"
un "Then what’s that right there?"
y simple"What?"
q "On top of your bed stands a luggage bag with a note on top."
y surprised"But… how?"

un "Maybe read the note?"
y simple"Right."
show thenote with moveinright
q "It reads:"
q"{i}No need to thank me, cutie, smiley face, signed -Therium{/i}"
y bored"Yeah, I know how to read."
un "It's my job, stupid."
y blush"Therium… you sly, sexy, amazing man; you saved me from a night of boredom."
un "Why? What’s in that thing? A bomb?"
y confused"What? No, why would that be fun?"
un "I dunno."
y bored"My laptop’s in here."
y s"We’re gonna watch a movie while eating pizza, a heavenly combo."
un "Hmm, yes, I see memories of this style of eating in front of a Tee Vee."
un "Alright, I’m into it."
scene codypizza with longdissolve
scene CGt6
q "You immediately strip down to your underwear, take the laptop out of the bag, and quickly start a preselected movie."
q "The top of the pizza box comes off and a hot meal is presented to you. A can of soda is popped open and the bag of chips gets opened with yet another, different, kind of pop."
q "You slouch on the bed, stuffing your face with an extremely delicious piece of culinary masterpiece."
un "Wow, that tastes good."
y nakedfood"Mmmhhm, they’re using wood-fired pizza ovens. Amazing."
q "It is still early into the evening, the moons rose not long ago to replace the sun and its fiery sky."
q "This movie you started is surprisingly interesting as well: the struggle of a working, lower class woman that has to take advantage of the rich to survive."
q "Is it morally correct? Is it okay for such a big difference in class to even exist? Should I do the same when I get my body back? I hope to answer these questions by the time it ends… or not, interpreting the subtext seems to be part of this movie's theme, make your own conclusions about the world she lives in..."
q "I think I’ll stop narrating for a bit and enjoy this."
y nakedsmug"Good call."
y nakedsimple"..."
y nakedpf"What was that question about your body again?"
scene black with longdissolve
pause 0.5
scene codypizza with longdissolve
"Some times passes and pressing matters appear on your host's mind, and in the middle of the movie, your companion asks you a question."
un "You don't need to use the second person pov with me. What is it? Make it quick."

y nakedsimple"I was just thinking..."
Y "What did you think of what we did earlier, Scribbles?"
un "The sex to satisfy your lust?"
un "It was kind of like the what this character in the movie does, something necessary for your well being."
y "But how did you feel during it?"
un sidee"Oh, you mean for me sexually?"
y "Yeah."
un "Well, umm…"
un "It was… something! Y-yeah, they… sure did things."

y "You seem nervous… were you even there?"
un suspicious"What kind of question is that? I was narrating the whole thing. Plus you got what you wanted out of that encounter, right? No need to question me."
y nakedpf"Hmm, you were indeed narrating, but you were a little vague about your wording… did you… feel it?"
un sidee"I certainly felt good talking about what was happening at that moment."
y nakedangry"That’s not a response! It’s a yes or no question!"
y "Did you, or did you not, feel everything I was feeling?!"
un "…"
un "Yyyyyy… I don’t know, I can’t risk lying."
y naked"Ha! So you were dodging the question!"
un suspicious"Yeah genius, good job, you caught me lacking, go boast about it to all the people who know I exist- oh wait, that’s right you’re the only one."
y nakedsimple"I don’t want to have one up on you, I’m just wondering: why did you not want to feel it? And how did you do it? And most importantly, why didn’t you want to tell me the truth?"

un bored"{i}*sigh*{/i}"
un "As you know, I can go to the back of your mind to not feel things, or to feel things less... and I just… I don’t know. I suppose I wasn’t ready to have sex so soon, so fast."
un "I was barely out of reach to see what was happening and hear some things."
y nakedconfused"So soon? How long has it been?"
un "…"
un "Like… two thousand years, give or take? Mostly give."
y nakedsimple"Damn."
un sidee"Still! It happened too suddenly."
un ang"But that’s it! I’m not letting you take advantage of my non-consensual truthful nature."
un "We’re dropping the subject."
y nakedss"Alright, but FYI, if you ever want not to do it-"
un pride"No, it’s your body, I don’t care what happens to it. Besides, it’s my fault you have those Lust surges in the first place."
y "…"
un bored"That reminds me: you still have cum inside you."
y nakedpf"Damn it! I knew I forgot something."
scene shower with dissolve
q "You pause the movie and rush to the bathroom to clean up. As soon as you finish, you hop in the shower as well since you’re already here."
q "At least the lights work unlike the main room, and the water is hot even if the shower head is missing."
y nakedbored"Why is it missing and who do I need to talk to for a replacement?"
play sound "audio/shower2.ogg" volume 0.1

q "The water feels heavy soaking into your fur, but relaxing, as thoughts linger at the edge of your mind."

Y nakedsmug"Isn’t Therium so hot?"
un suspicious"Don’t think about stuff like this in the shower, please."
y "Heh, don’t worry, I’m more than satisfied from the earlier encounter, no lewd thought is going to ambush me this time."
y "So answer the question."
un bored"If you think so, then sure."
y nakedsimple"You don’t think he is?"
un simple"What do you even want with him?"
y "What do you mean?"
un "A relationship? A hookup? Someone to cheat off of and help you graduate?"
y "No, I’m not seducing him into becoming my knowledge sugar daddy..."
y "As for the other things… I don’t know. Either one, I suppose?"
y nakedconfused"But what is it to you?"
un "I’m just curious, that’s all."
un "He doesn’t seem like your type."
y "You know my type?"
un bored"Anything that walks."
un "Actually, scratch that, anything that has a dick or a hole."
y nakedpf"That includes cheese graters… I would not fuck a cheese grater."
un "Oh just give yourself a month with no cumming and it’s all over."
y nakedsimple"But Therium walks, doesn't that mean he's my type?"
un "So you admit you'd fuck anything that walks?"
y nakedpf"...no?"


y nakedbored"I think I will ignore you now."
un "Fine by me."
q "You step out of the-"
y "Nope, I said I’m ignoring you, that includes the narrator."
un simple"But I-"
y nakedasleep"Nah ah."
un "I have to-"
y "Shut!"
un "{i}*sigh*{/i}"
scene codypizza with llongdissolve
"The movie is quickly over after the shower and the last slice of pizza is also devoured by your one and only."
"Even while ignoring Scribbles I could still feel him cry at the ending, or at least try his hardest not to."


"Some would say it’s not a good idea to go to sleep with a full stomach, but it’s getting close to midnight and I need this sleep for tomorrow, no exceptions!"
scene dormroomnight with dissolve
stop music fadeout 2.0
play sound "audio/sheets.ogg"
"The covers are soft and cool, and so is the pillow my head smashes into."
"I swear I wasn’t THIS tired when I got out of the shower, but now I’m almost dying."
scene black with llongdissolve
"As soon as my eyes closed… end of sentence...and end of day."

jump firstdream

label aftertheriumrefusedream:
scene red with llongdissolve
q "You slowly open your eyes to morning rays hitting your eyelids and the sounds of birds chirping."
scene dormroom with dissolve
q "The alarm clock might’ve been another factor in your wake."
y nakedsurprised"What the hell was that dream?"
y "If we can even call it that."
un "Do not bring it up. I know you want to, but you’ll get no answer from me so just conserve your thoughts."
y nakedbored"Meaningless mysteries, my favorite."
y "Fine, have it your way."
Y "Don’t come crying to me when you want to actually share secrets."
un "Trust me honey, I won’t."

q "You decide to stop arguing with a superior being and get dressed; you have a long day ahead of you."
y "The fact you call yourself {i}‘superior’{/i} and it’s not considered a lie has to be the most narcissistic thing I’ve witnessed."
un "I mean, it’s true. The universe says so."
q "The same kind of jeans, and white shirt and tie, because 'why change perfection?' You think to yourself."
un "Perfectly boring."
y "Why don’t you-"
play sound "audio/knocking.ogg"
q "A knock at the door prevents you  from delivering a super cool and devastating comeback."

y "Uhmm, who is it?"

th "Hey, it’s me. I brought breakfast!"

y "Therium!"

scene dormhall with dissolve
play sound "audio/dooropen.ogg"
q "You open the door more excitedly than you thought you’d be upon hearing his voice again."
show horse smug with moveinleft
show horse blush with dissolve
th "Well hello there sailor~"
y nakedawkward"H-hey, why you say it like tha-{nw}"
un "You're naked."
y nakedscared4"{size=*2}AH!{/size}"
play sound "audio/doorclose.ogg"
scene dormroom with hpunch
y "Umm, sorry! One minute please!"
th "Oh take your time, I need to process the imagery."
"WHY DID'T YOU SAY SOMETHING SOONER?!"
un "It's funnier this way."
"FUCK YOU!"

q "You quickly get dressed with the usual uninspired attire."
"Fuck you times two..."
scene dormhall with dissolve
play sound "audio/dooropen.ogg"
show horse smug with moveinleft
th "Good morning, princess."
y awkward"Hehe, hi."
y "Sorry about that..."
th "Don't be, it was nothing to complain about on my part."
y sadsmile"More importantly, sorry about yesterday I-"
show horse
th "Don’t even worry about it; I was a bit too forward, I know."
th "It was a long shot."
show bag with dissolve
th "Here."
q "He hands you a small bag of food."
hide bag with dissolve
q "An egg salad sandwich as well as a BLT."
th "Wasn’t sure what you like so I made a variety."
y sadsmile"Oh gosh, thanks. Thankfully I’m not picky."
q "The appetizing smell prompts  you to immediately start eating, even though some of last night’s pizza is still inside you."
y food"So goooood!"
th "Glad it’s to your liking."
y awkward"Oh, sorry, where are my manners? Do you wanna come in?"
y sadsmile"I actually haven’t really checked the dorm out myself. The lightbulb is missing and I couldn’t see much last night, so we can do it together."
th "If you’re inviting, it would be rude to refuse."
q "He says slyly."
y awkward"Yeah, what kind of snob would ever refuse an invitation, haha..."
scene dormroom with dissolve

jump invitetherium



label nosextime:
$ thepoints+=1
$ theriumhome +=1
scene cafeteriaday
show horse smug
y blush"I’d love you, I-I’d love TO go to your place, h-haha."
y "Sounds nice."
stop music fadeout 2.0
th "Follow me then."
show horse
hide horse with moveoutleft
play music "audio/forgetmenot.ogg"
scene chibitherium2 with llongdissolve
q "As if it had a mind of its own, the Lust Rush seems to notice that its host is giving up on appeasing it, and in turn mellows down. But that doesn’t stop Therium from noticing your behavior."

Q "You grab his arm and hold tight close to his body, while trying your hardest not to flirt inappropriately."

y lust"I need you to fuck-fu-fucking get me some fooood, haha."
y "Fill me up to the brim."

th "Heh, don’t worry, I’ll make sure you’re satisfied once we get to my dorm."

y "Yup, that’s what I want, you to satisfy me…"
"Damn it all..."
q"The road there is more of a blur imprinted in your mind. A road of dicks, and clits and ass that your imagination made up."
q"Without your guide literally holding your hand, you would’ve definitely derailed into a brothel or bar."
stop music fadeout 2.0

Q "By the time you arrive the lust goes away completely, and a feeling of ease washes over you."
play music "audio/guitar.ogg" fadein 3.0
play sound "audio/dooropen.ogg"
scene theriumroom00 with llongdissolve
q "Now you can focus your attention on the disbelief you’re feeling upon seeing his {i}‘dorm’{/i}."

y simple"Dorm?"
y surprised"DORM?"
y "This is a penthouse!"
y "How many rooms are there?"
th "Heh, there is my room, the office I turned into a guest room, bathroom, living room and kitchen."
y "Is my {i}‘room’{/i} going to be the same?"

th "Sorry, I doubt it."
th "But you can stay here as long as you want."
q "As soon as he steps inside, he walks toward the kitchen and starts dinner, but not before handing you a clean, neatly folded white towel."
th "You can go shower in the meantime, it will only take twenty minutes to prepare everything."

y smug"Is this an invitation to stay the night?"
th "Your dorm is pretty far away, it's already getting dark and it will be nighttime by the time I let you go."

y worried"B-but what about my clothes? My luggage is in my room."
th "No worries, it will be here when you get out."
q "He smiles warmly, his confidence and sincerity making you stop questioning him."
y sadsmile"Alright then, thanks."

th "…"
stop music fadeout 2.0
play sound "audio/dooropen.ogg"
scene black with llongdissolve
play sound "audio/doorclose.ogg"
scene theriumroom00 with dissolve
play sound "audio/tension1.mp3" volume 0.3
th "..."
th "Get the luggage."
st"Yes, master."
th "Now: dinner time."
th "I didn’t get to cook for someone else in a long time."
scene black with llongdissolve
th "This might be, dare I say, fun."
play music "audio/guitar.ogg" fadein 2.0 volume 0.2
scene shower with dissolve
un simple"How you feelin’? No more lust traces?"
y nakedsimple"Nope, I’m all good."
y nakedpf"But I should curse the hell out of you for this."
un bored"You made a pact."
y nakedbored"I made a promise you lied to get me into."
un ang"I did NOT lie, I was simply vague."
y "That should be considered lying."
un eyeroll"Oh, so demons should just die every time they don’t offer a novel’s worth of information with every comment they make? Great idea, just kill us all like that, you genocidal maniac."
y nakedangry"You’re taking the wrong words out of context!"
y "Just make yourself useful and narrate."
un bored"It’s boring, you’re just showering! Here:"
un "The water gets on your fur then shampoo, the shampoo make bubble, and bubble make fur clean."
un "There, happy?"
y nakedbored"You’re so talented, you should write a book."
un sidee"Maybe I will!"
un "Just to spite you."
q "One period of silence in your mind and a boring shower later, you get out and wrap a fresh towel around your waist."
scene theriumroom00 with dissolve
play music "audio/evening.ogg" volume 0.5 fadein 3.0
q "You step into the living room and see Therium working in the kitchen."
th "Everything is ready in the guest room, last door on the second floor."
q"One thing that catches your eye is that he’s no longer in his uniform; the proper little pony boy is wearing casual clothes for once."
y nakedss"Thanks! I’ll be down in a minute!"

q "You run up the stairs, towel almost falling down, intentional, no doubt-"
"It wasn’t."
un "So you’re just a boyfailure by design, got it."
q "You find the guest room and your sweet luggage you’ve missed so much."
q "Taking out some casual clothes as well, you get dressed and walk back down the stairs to meet the horse face to face."
scene theriumroom111 with dissolve
q "Two plates of hot food consisting of meat, potatoes and some veggies, as well as a small basket of bread, await you on the coffee table in front of the TV."
q "Therium notices your intrigued expression."

th "Sorry, is this too casual? I thought eating in front of the TV would be less awkward than the kitchen table, but I could take everything back-"
y blush"No! Don’t bother, this is perfect, I’m just surprised at your sudden drop in… properness."
th "I don’t like bringing my job into my personal life."
y s"That’s a great way to live life, if you ask me."
q "The table is a little further away from the couch, so to not have to hold your plate in your hands at all times, you decide to just sit on the floor while the horse sits like a normal person on the couch."
q "You take the first bites of food in silence, but the intense flavors just won’t let you stay quiet."


y food"Mhhhmmm! Delicious."
y "How’d you make it so fast?"

th "I had the meat marinated and ready, but the potatoes are reheated on the stove, unfortunately."
y "No misfortunes found here, it’s good."
y "You are talented at this."

th "You’re just saying that."

y sadsmile"I swear I’m not!"

th "You sure it’s not because of these?"
q "He holds his plate with one hand and flexes his bicep, smiling slyly."
q "After a moment of seeing your unimpressed face he… melts, would be the best term to describe it."
q "His smile drops and arm slowly lowers."
th "Oh, you really are serious."


q "In an instant you return to your awkward boy-failure state."
y simple"S-sorry, was that a pop culture reference I didn’t get? I’m not good with anything that isn’t catered specifically to my tastes."

th "No, I mean, yeah, it’s from an old movie. It’s fine, it wasn’t too funny anyway."


Q "For the first time, Therium seems slightly uncomfortable, or at least not ready for small talk."
q "He looks at the TV without a smile on, eyes concentrating in the corner of the screen, trailing away on the wall behind it."
q "’Perhaps I offended him’, is the first thought that comes through your head."
q "Maybe he just doesn’t know how to hold a conversation without being flirty."
q "After all, those three guys earlier did say he’s a bit weird and so far, aside from being smoking hot, you haven’t seen many flaws in him."

y simple"Okay, okay. So... umm..."
q "You tap your chin thoughtfully before finally coming up with something you might share common ground on, to get him back in a conversational mood."
y "Have you seen any good movies recently? I've been meaning to catch a new horror flick myself."
q "You turn your attention back towards the TV and your plate of food while attempting to make small talk."
y "There is this new movie that you might like, well, anyone would like, since it has the best actress in the world starring in it, at least in my opinion, but anyone with eyes should agree too, haven’t seen it myself yet either, although I’m not sure how the cable even works around here."
y "Speaking of cable, how does it work? And why can’t I have access to it in my dorm?"
y s"Actually, forget cable, who even cares, I need internet!"
y "Do you have internet, Therium?"
q "He looks at you, a bit curious."
th "You’re not very good at small talk."
q "He says in a serious, silent tone, which shifts back into his usual proper and sly demeanor."
th "You’re supposed to wait for an answer after the first question before throwing the next one."
y sadsmile"Shoot, I’m always either talking too much or not enough, no in-between."
q "At least you managed to snap him out of his little depressing episode, whatever that was about."

y smug"Oh, I’m sorry, why don’t we hold a thought provoking conversation then, mister professional conversation enjoyer?"

th "All right,"
q "He ponders for a moment."
th "How about this? Do you believe that animals have feelings and emotions like people?"
q "Now his tone is neutral, almost curious, though there's a hint of mischief lurking beneath the surface."
q "You’re surprised at his sudden question, but decide to give it a minute and really think about it."
q "As you do, he gets up, his food nearly finished, and brings from the kitchen a bottle of wine, some kind of fruit juice, and a bottle of sparkling water, as well as two glasses."
q "He places the wine bottle on the right corner, the juice on the left corner and water in the middle of the table."
q "He gestures towards them and you understand the assignment, in a way, but at the same time, you can feel your brain frying."
q "Such a simple choice, but knowing this man, it is not as it seems."

menu:
    "My choice of beverage is my answer to his question, and my answer is…"


    "Of course they do.":
        Q "You point at the wine and Therium smiles, popping the cork out easily and pouring two glasses."
        th "Alcohol is dangerous, a bit too much and you can find yourself on a downward spiral."
        y simple"Not so much to get drunk."
        th "But do you have the self control to stop? Or the heart to resist social pressure?"
        y s"I like to believe so."
        th "People judge you for it as well; God forbid you drink it in public. They place all these… conditions and demand so much from you just to acquire it, yet they almost force it down your throat."
        q "Images and news of false animal activism, and large scale protests in the streets against the big meat and dairy corporations blink into your mind."
        q "As well as the faces of hypocrites who stuff their bag with dirty money while crying over someone’s poor choice in dog food."
        y simple"You do bring… a point, some kind of point, I’m not sure which one it is just yet."

        th "Yet you ask for it over the other options? While doubting your decision?"
        y "Can this just be about a beverage for now?"
        y bored"My head already hurts."
        th "Certainly, that’s what it was all this time."
        q "He smiles while filling up your glass."
        th "Although, truth be told, I don’t think wine is the best thing for a headache."
        y smug"To. The. Brim."
        th "If you say so, cutie."
        q "As the wine hits your lips and the crimson liquid disappears, the stallion’s words become somewhat of a blur."
        q "Not because you’re drunk already, but because they’re simply so strange…"
        th "You are much more...thoughtful."
        th "And brave."
        th "For your own good."
        th "Much more than I gave you credit for, at least."
        y "I’m glad my beverage choice made you deduce that."
        jump afterbeverage







    "I’m not convinced enough.":
        q "You take the water bottle for yourself."
        th "The safest option, nobody can get mad at you for picking it."
        th "Water is neutral, no real flavor to write home about."
        y simple"I’d say water differs in taste quite a bit."
        th "Still, it is not as bold as wine or as sweet as juice."
        th "Undecided or unbothered."
        th "The good news is that you can still be easily pushed towards whichever direction others want."
        th "The bad news…"
        th "You can be pushed towards whichever direction others want…"
        q "You open up your water bottle and stare at its crystal clear top, almost overflowing from your light squeeze."
        y s"Water is important."
        y "Do you see water as no more than an ingredient to make juice or alcohol?"
        th "It will ultimately be used for one or the other, it’s up to you to see who uses you."
        y smug"Or."
        q "You tilt your head all the way back, your neck cracking from the sudden movement after sitting on the floor and leaning forwards for so long."
        q "The cold water hits your throat and it does not stop until the bottle is empty."
        y ec"Aah."
        th "Someone’s thirsty."
        y smug"Don’t change the subject."
        y "Water can be great on its own; it helps keep you hydrated without getting drunk or getting your sugar levels too high."
        y ec"It can easily be a choice on its own, and it’s healthy!"

        th "You are very… just."
        th "And pure."
        th "For your own good."
        y "I’m glad my beverage choice helped you deduce that."
        jump afterbeverage





    "They definitely do, but different from us.":
        q"You pour yourself a glass of juice from the labeless white container, with only the word ‘JUICE’ written with a marker on it; a deep red juice."
        q "You look at it, swirl it around and ponder taking a sip. A strange odor hitting your nostrils, making you halt for a moment."
        th "Risk taker, huh? You have no idea what kind of juice that is, it could be the bitterest grapefruit beverage in the world, or tomato juice, but you made up your mind and won’t hear it any other way, right?"
        y simple"Any kind of juice is good for you; even if it was from a fruit or vegetable I don’t like, there’s no reason to not drink it."
        q "You chuckle awkwardly as your snout gets closer to the edge of the glass."
        th "So you would drink even disguised blood just to not offend your host?"
        q "Your head moves back slowly and your eyes widen."
        th "Ha, I jest, it’s beet juice."
        y awkward"Phew."
        q "You say, while still wondering if that is any better than blood..."
        th "I only have that because I just finished a special diet. I should get rid of it, I understand if it’s not to your taste."

        menu:
            "Drink it.":
                q "With newfound confidence, and before the stallion can take your glass, you gulp down the liquid without stopping, leaving you with a funny look on your face and a deep red mustache."
                y determined"I’m not a quitter."
                th "Interesting."
                th "You would even drink something disgusting just to not offend your host."
                y sadsmile"It wasn’t thaaat bad."
                th "I had to drink it, it’s disgusting."
                y bored"Yeah, it is…"
                q "He gets up and brings you some actual juice, apple juice to wash everything down with."
                y sadsmile"I guess sometimes, the sweetest choice can also taste the worst."
                th "Nobody knows what’s hidden behind closed doors, or white containers labeled {i}‘juice’{/i}."
                y smug"Is that foreshadowing?"
                th "Watch out, the fourth wall isn’t that thick, you might break it by accident."
                y "Haha…"
                th "You are very… nice."
                th "And kind."
                th "For your own good."
                y "I’m glad my beverage choice made you deduce that."
                jump afterbeverage

            "Switch it with something else.":
                y bored"I’m pretty sure I’m going to throw up if this hits my stomach so… give me some water please."
                q "Although he was the one to propose you switch the juice, he seems a bit saddened by your decision."
                q "Perhaps he is actually proud of the beet juice he made? Maybe he wanted all the water for himself? Whatever it is, you won’t know without a question, and a question is not what you need right now."

                jump afterbeverage









label afterbeverage:

q "He shifts into his cool persona once again and rearranges his long mane, his dangling crystal earring reflecting in his pupil, which shies away from your face."

th "I’m sorry, I’m spouting nonsense again, aren’t I?"
y s"No don’t be! I like this kind of conversation, deep but also meaningless in a way."
y sadsmile"It’s my fault; I’m so bad at small talk that we had to result in this anyway."
y "Can’t say I was able to keep up with every metaphor and analogy we threw in the mix but I tried my best."

th "You are sharper than you think."

th "I’m aware that my divination methods are a bit more obscure, sometimes unwanted, I’ve been told."
y surprised"Divination?"
y "Now that you mention it, it did seem a bit like a personality test of some sort."
th "Heh, spot on once again, but it’s not as shallow as personality."
th "Little questions, gestures, mimics, the way someone dresses, talks and walks can all be good indicators of who they really are. Might even predict their destiny."
y "You can tell my future?!"
th "Oh no, not more than any run of the crowd carnival seer could."
th "There is no such thing as ‘seeing someone’s future’, time is much too malleable to predict, it always slips through the tiniest cracks."
th "I dabble in other ways."
th "But that is not what matters most about me or about you."
th "As a summoner all that matters is your ability to summon Nightfallen with whatever kind of magic you have, we don’t discriminate."

y s"That’s good to hear."

y "So..."


y "What about you?"
th "About…"
y smug"The question, the one I almost had an internal meltdown over, you have to answer too. It’s only fair."
th "Oh?"
th "Hmm."
th "I mean, I don't know for sure,"
q "He says truthfully with an unusually sincere tone."
th "But you can tell that animals show signs of happiness and sorrow sometimes, right? Like when a dog wags its tail or when a cat purrs? That is undoubtful, it’s just a matter of how relevant it is to our question."
q "He scratches his chin nonchalantly, contemplating."

th "And what about us? Do we have emotions too?"
y simple"You can’t possibly think we don’t."
q" His gaze drifts downwards, lingering on your chest briefly before returning to meet your eyes."
th "Perhaps we do have some, but if they aren’t deep enough, true enough, then they’re no different than animals."
th "I mean, lust is an emotion, we both know how that’s going in this world."
y "Yeah..."
th"Are we just machines designed to reproduce and survive?"
th "It’s hard to judge the meaning of another being’s life, when you don’t know your own purpose."

y "So, the final drink you choose is?"
th "Heh."
Th "I’m not thirsty."

y "So you just...refuse?"
th "I put it on pause."
th "There is such a thing as taking action too early. Some hints may appear along the way that will change my opinion."
th "Such as, a piece of stale bread that needs to be washed down. When the moment comes, I’ll make my choice, don’t want to regret it until then."

y "But what if you had to choose."
th "I choose nothing."
y "But the question only has three choices."
y "You have to choose one of the three."
th "Then I refuse the questions, as I said."
y smug"Not this time, you have to choose, or else you get zero points."
th "Can I choose a cup of tea?"
y "Nope, no fourth option, no bs."
th "I don’t think that’s how-"
y "Wine. Water. Juice."
th "But I can’t-"
y determined"Choose!"
th "God, let me-"
y "ONE, TWO THREE AND-"
th "{size=*1.5}IT’S NOT THAT SIMPLE!{/size}" with hpunch

q "For the first time, you made him lose his cool for only a second."
q "His intense eyes: encircled by wrinkled skin, and his perfect hair: now has a few strands standing upright."
q "He realizes it as soon as you do, and starts laughing."
th "A-alright, heh, you win."
th "I guess you don’t always get to have another choice, not when there is a...noisy, demanding leopard ready to jump at your throat."
y smug"Guilty as charged."
th "If I had to choose something, and it was life or death, I’d choose...what you chose."

y simple"That is either a flattering answer, a boring one or a dumb one."
y smug"Funny, somehow you managed to answer the question exactly how I wanted, yet it is still technically a fourth choice."
y s"Nicely done."
th "It’s your turn to flatter me, huh?"
th "What can I say, I like to leave my guests satisfied, but that doesn’t mean I won’t get what I want in the end."




y ec"Thanks again for the meal. I was fully expecting to only eat cafeteria meals and junk food or convenience store items for my whole year."
th "And thank you for the thought provoking conversation, Nightfallen don’t usually respond to me that way."
y simple"Night-"
y surprised"Oh!"
y "I saw the dog bed and chew toys in the corner. I was going to ask if you own a pet, but now I realize."
th "Yup, maybe not a pet, but a familiar for sure."
q "Deja Vu."
th "Sparkle loves his alone time in the bed, bathing in the moonlight."
y ec"You can let him out, he seemed very friendly when I met him."
th "Ah, that...Sparky, I don’t think you’re ready to meet Sparkle just yet…"
y pf"Oh, that makes me intrigued...and also scared."
th "Reasonable reaction, but don’t worry, this isn’t some kind of big sacrifice for your sake."
q "He says while bringing two small bowls of ice cream from the kitchen."

y sadsmile"You’re spoiling me."
th "What am I expected to do when an angel is sitting in my living room, but treat him with utmost respect and adoration?"
play sound "audio/fluster.mp3"
y blush"Oh you…"
q "Conversation? What conversation? Whatever words the horse was spilling after that cheesy remark went through one ear and left through the other, as the rest of your face hole was stuffed with the frozen delight."
q "The few moments of clarity were, in turn, occupied by the sound of the TV, screams of agony can be heard at this point in the show."

th "You don’t seem too fazed."
y smug"I have high horror movie tolerance."
y "I used to watch them since I was like four, with my mom and my cousin."
th "I suppose there is no chance or reason to snuggle together on the couch, you brave cat."
y s"Yeah, probably not."
q "Somehow you manage to push any kind of lust in your cumbrain away in a critical moment, not even a personal narrator in your head could break you away from the screen and the spoon."
q "Thankfully, your man is not too sad about your denial. In fact, he’s smiling warmly while looking your way."

q "It’s only by the end of the movie, when he got bored and came closer, massaging your shoulders with his strong, meaty fingers, his thighs touching your cheek and his foot brushing against your arm, that you finally realize the tension in the room."

q "But it’s a little late for that."
q "There are more pressing matters to turn to."


y sadsmile"Hey, uhmm, So...where do I sleep?"
y "Should’ve asked this earlier probably."

th "Glad you asked."
th "Well, you have two options."
th "You can either take the guest room on the second floor, which is unfortunately not too well prepared to actually house guests."
th "Or...my bed is big enough, I believe."

q "Yup, those lustful thoughts come back faster than that young, attractive woman died to the serial killer in the movie. The pretty ones are always the first."
q "Keep that in mind, pretty boy."

menu:
    "Guest room.":
        $ thepoints -= 1
        y sadsmile"I-I appreciate the thought, but a room by itself is more than enough. I don’t need anything fancy, and I certainly don’t want to intrude on your privacy."
        th "I understand, it was a shot in the dark on my part anyway."
        th "As your first day here you must be exhausted, you should go to bed right away. Tomorrow there are a lot of things to do."
        y "Shouldn’t I shower first at least?"
        q "He comes closer, and tilts your head to the side ever so slightly, taking a long whiff."
        play sound "audio/fluster.mp3"
        th "You smell lovely, dear, besides, there’s always morning."
        y blush"Y-You’re right, I am kind of sleepy."
        y "Uhmm, good night?"
        th "Sweet dreams."
        stop music fadeout 2.0
        scene dormroomnight with llongdissolve
        q "At last, you are left alone, or at least alone with the demon inside-"
        play music "audio/nightsounds.ogg" volume 0.2
        y pf"Ughh, shut up for a second."
        un simple"What’s up?"
        y simple"About Therium, is he…you know?"
        un bored"Fruity? Yes."
        y bored"No...into me."
        un simple"Are-"
        un suspicious"Are you fucking stupid?"
        un squint"Are you dense?"
        y scream"I KNOW!"
        y worried"He’s been flirting all day basically, but I know people who do that just because that’s their personality...they don’t actually like you…"
        un bored"That could be the case, after all, you’re ugly as fuck, right?"
        y sad"Oh...really?"
        un ang"NO YOU DUMBASS!"
        un "YOU’RE HOT!"
        y scream"YOU’RE GIVING ME MIXED MESSAGES SCRIBBLES!"
        un "GOOD! MAYBE MY MIXING WILL DISLODGE A NEURON OR TWO INSIDE THAT NOGGIN OF YOURS!"
        y sad"{i}*Sigh.*{/i}"
        y simple"These thoughts are useless right now."
        un bored"You’re right...Bickering like an old couple doesn’t solve your overthinking."

        q "Looking around, you see a regular, small room with a bed, a window, a small wardrobe, nightstand and even clean, ready to use sheets."
        y simple"Huh, if this is an {i}‘unprepared room’{/i} I’d like to see how he actually prepares one."
        un simple"Why’d you choose the guest room anyway?"
        y simple"I need some time to think…"
        y "Not necessarily anything lustful, just think."
        un "What about?"
        y "About you? About this school? About Therium, and about how my luggage is already here?"
        un simple"That is peculiar indeed."
        y "About a lot of things…"
        y "Everything’s so new, and as tempting as Therium’s offer was, I need my alone time in the moonlight too, just like Sparkle…"
        y sleepy"That is, if sleep doesn’t steal me away too early… I really am tired, more tired than I thought…"
        y "{i}*Yaaawn.*{/i}"
        show blink with dissolve

        un sidee"…"
        un "Hey, about that...horse."
        un "Can I be honest with you?"
        scene black with dissolve
        y simple"Sure, go ahead."
        un bored"He was lying, you do need a shower. You smell like shit."
        y angry"FUCK OFF!"



        "Meanwhile..." with llongdissolve

        jump theriumconvo






    "Therium’s room.":
        $ theriumbed +=1
        $ thepoints +=1
        y blush"I-I appreciate the thought, and I think I’ll take you on that offer."
        y "Uhmm, wouldn’t want to stay in an unprepared room, r-right? Haha…"
        q "His eyes lit up and he clapped his hands together once."
        th "Splendid! Everything is prepared in my room, it’s the first door on the second floor."

        th "As your first day here you must be exhausted, you should go to bed right away, tomorrow there are a lot of things to do."
        y simple"Shouldn’t I shower first at least?"
        q "He comes closer, and tilts your head to the side ever so slightly, taking a long whiff."
        play sound "audio/fluster.mp3"
        th "You smell lovely dear, besides, there’s always morning."
        y blush"Y-You’re right, I am kind of sleepy."

        y "Uhmm, w-when are you coming?"
        th "Oh, I have some things to do before bed. I hope my pacing through the rooms won’t keep you up."
        y "O-of course, no problem, erm, good night?"
        stop music fadeout 2.0

        th "Sweet dreams."
        scene theriumbedroom with llongdissolve
        play music "audio/nightsounds.ogg" volume 0.3
        q "At last, you are left alone, or at least alone with the demon inside-"
        y simple"Ughh, shut up for a second."
        un simple"What’s up?"
        y"About Therium, is he...you know?"
        un bored"Fruity? Yes."
        y"No...into me."
        un simple "Are-"
        un suspicious"Are you fucking stupid?"
        un squint"Are you dense?"
        y scream"I KNOW!"
        y worried"He’s been flirting all day basically, but I know people who do that just because that’s their personality...they don’t actually like you…"
        un bored"That could be the case, after all, you’re ugly as fuck, right?"
        y sad"Oh...really?"
        un ang"NO YOU DUMBASS!"
        un "YOU’RE HOT!"
        y scream"YOU’RE GIVING ME MIXED MESSAGES SCRIBBLES!"
        un "GOOD! MAYBE MY MIXING WILL DISLODGE A NEURON OR TWO INSIDE THAT NOGGIN OF YOURS!"
        y simple"{i}*Sigh.*{/i}"
        y "These thoughts are useless right now."
        un bored"You’re right...Bickering like an old couple doesn’t solve your overthinking."

        q "Looking around, you see a large bedroom with a king sized bed in the middle and a wide balcony overlooking the sea side, the moon’s already shining brightly through the glass door."
        q "The horse did not lie when he said ‘prepared’ the room."
        q "There are delicate, thornless roses on the bed, with a tantalizing aroma so strong, that it can be smelled without picking them up."
        q "Underneath them fresh, warm sheets and two small chocolates on both of the soft pillows, which you unwrap and consume bit by bit, savoring it as you look for more things."
        q "A pair of  night robes and eye masks prepared over the nightstand as well as a book on how to sleep well."
        q "You don’t really need any of the extra items, since your usual plan for tackling sleep is the same as your ideal sex scenario, get naked, plop on the bed, raise your ass and close your eyes."
        q "The only thing you didn’t think about is pray, since you’ll need all the help from God when that horse comes into the room and shoves his whole co-"
        y pf"Stop…"

        un bored"Why? Am I making you horny or uncomfortable?"
        y bored"Both."
        un "Why’d you choose his room anyway?"
        un "Isn’t that exactly why?"
        un "You’re hoping for something, aren’t you?"
        y simple"Maybe…"
        y "Or maybe I’m just an idiot."
        un eyeroll"You’re not...such a big idiot."
        y "There are a lot of things on my mind anyway, I can’t be thinking about this kind of stuff right now."

        un simple"Such as?"
        y "You? Also about this school? About Therium, and about how he already has 2 sets of everything prepared?"
        un bored"That is peculiar indeed."
        y "About a lot of things…"
        y "As much as I want to think what Therium’s offer could imply and bring...I just need to sleep."
        y sleepy"And I really am tired...he was right."
        y "{i}*Yaaawn.*{/i}"
        scene black with dissolve


        un sidee"…"
        un "Hey, about that...horse."
        un "Can I be honest with you?"
        y simple"Sure, go ahead."
        un bored"He was lying, you do need a shower. You smell like shit."

        y angry"FUCK OFF!"




        "Meanwhile..." with llongdissolve

        jump theriumconvo



label theriumconvo:
stop music fadeout 2.0
scene theriumroom00 with llongdissolve
play sound "audio/sheets.ogg" volume 0.4
"The sound of my sofa’s cushions being compressed is not something I like to hear, unless it’s me who does it."
play music "audio/dark2.ogg" fadein 3.0 volume 0.5
"I guess he’s already here."
scene theriumroom11 with dissolve
"No matter, I have to make preparations for tomorrow’s meals before starting a conversation with this-"
nu "Nice ass."
th "deviant..."
th "A very appropriate greeting coming from you."
nu "Not my fault you decided to get naked as soon as your little toy went to bed."
nu "I thought he’d never leave."
th "Don’t call him that."
nu "Already attached, huh?"
nu "Since when do you prepare food so late at night? There must be a new, special reason."
th "Did you come here just to get on my nerves?"
nu "Not at all, I just wanted to check on things."
nu "And I have to say, I’m satisfied with what I’m seeing."

th "Shut up…"
nu"The other two are looking for him."
th "And what am I supposed to do?"
nu"I’m just bringing the news, not the solutions."

nu"He really likes you."
th "He likes my body."
nu"That’s what YOU want him to like."
nu"I know it’s hard to admit you got out-philosophied."
th "That’s not a word."
nu"But it’s the truth."
nu"I heard you two talk, and I heard your heart beat rise and fall… rise and fall, rise-"
th "Are you done?"
th "What do you even want?"
nu "Sigh, I’ll get to the point I guess."

nu "Be honest."
nu"How do you think he’ll do?"
Th "I don’t think he’s ready."
nu"Why? Are you still jealous, Therium?"
nu "Or perhaps insecure?"
nu "Or maybe both?"
Th "…"
th "No."
nu "Then come ooon, give him a chance."
nu "You know what happens, if he fails…"
th "Then he better not."
nu "That depends entirely on us...and him."



nu "What about the auditions?"
Th "For him? You were right, it will be a joke."


jump firstdream


label firstdream:
scene black with llongdissolve
play music "audio/wind.ogg" volume 0.3 fadein 2.0
"…"
y simple"…"
y "Uhmm."
y "ok."
y "…"
y "Scrib?"
y "Scribbles, are you going to narrate?"
y bored"Are you...not there or are you just mad at me for what I said before bed, because frankly, I should be the annoyed one here."
y "…"
y simple"Ok, I guess you’re not here."
y "But more importantly, where am I?"

y "I find myself in darkness, but my eyes are open."
y "I can move freely around, although I don’t know if I should."
y "This certainly feels like a dream, my skin is not cold or warm, I feel no breeze or even air itself."
y "There’s just...nothingness, a deep, comforting void."
y "Maybe I should take a nap here, even if it’s a dream, it’s not like there’s anyone-"
stop music
unn "Just turn around already…"
scene scribblesdream with longdissolve
scene CGt7
play music "audio/unspoken.ogg" fadein 2.0
y surprised"Oh."
y s"So, we meet again."
y "What’s the occasion?"
unn "No idea."
y simple"Did you not summon me?"
y "Like all the other times?"
unn "I didn’t {i}‘summon’{/i} you now, nor did I any other time. I don’t know what your deal is and this mind of yours."
unn "You’re the one that’s trapping me in your dreams...stupid, at least this time..."
y bored"You’re... you’re turning your head very far, hey, you’re gonna break your neck, look at me!"
y simple"Are you blushing?"
unn "N-NO! SHUT UP!"

unn "I just didn’t expect you here, that’s all!"

unn"Last time I used a lot of magic to be able to get to you, but now…"
unn "It might have something to do with our bond kind of...strengthening, in a way."
unn "Since we’re sharing a body and all..."



Y surprised"You think so?"
unn "I have noticed that I was rapidly gaining new abilities, knowledge and strength here."
unn "In the real world I’m even able to see things you don’t keep your eyes on already."
Y sadsmile"Aww, we’re becoming closer and closer friends."

unn "Or maybe I’m starting to consume you from the inside and take over."

y pf"Whyyy are you ruining the moment?"

unn "’Moment’? Like we can have any kind of good moments in the darkness."
unn "There is only misery and boredom here."

y simple"Where are we anyway?"

unn "{i}*sigh*{/i}"
unn "Welcome to my prison, make yourself comfortable."
y "Your...prison? You mean we’re inside your crystal?"
unn "Not quite, it is visually an exact replica, but you're still dreaming, so it’s not like you can feel anything."
y "Now that you mention it, I don’t even have a desire to breathe in here."
unn "It is definitely nicer than my actual prison."
y bored"Dark, gloomy, creepy… yup, this explains everything."
unn "I don’t like that condescending tone..."
y s"Heh, I’m just kidding, you are…"
unn "What?"
unn "Annoying? Dumb? Ugly? A nuisance to have around? Ha, you can say it all to my face now I suppose. It’s not like I ca-"
y sadsmile"Pleasant."
unn "Huh?"
y "In a way."
unn "Explain yourself."
y "I’m not sure how to explain it, you just seem like a not so bad guy sitting over here, in front of me."
y "It’s different from the real world, for some reason."
y "Maybe because you have a real person’s body instead of a cloud of scribbles."


unn "P-probably because you can’t hear all the nasty things I’m saying in my mind."
y simple"Oh, about me?"
unn "No...just...in general."


Y "This is a little awkward, now that I think about it."
unn "Why? You said you like my body."
y pf"That’s also the problem."
y "Well, we kind of... we almost fucked before, in my previous dream."
unn "Oh...well, in my defense, you’re the one that jumped at my feet."
y bored"You should’ve said it was a dream, or just said no in general."
unn "Well I stopped the dream before you could do anything, didn’t I?!"
unn "That’s something."
y surprised"That was you? Not my alarm?"
y bored"Huh...guess I underestimated your self control, good job, {i}‘lust demon’{/i}."
"I’m glad that at last he won’t be able to hear my thoughts, because of what I’m about to say, but he is...extremely cute, and I mean that in a completely innocent way."
"The blush that appears over his scribbles make as much sense as a snowman in the desert, but it keeps appearing as he talks, his face turning away from me as much as possible."
"He might be embarrassed about the scribbles, or maybe his mostly naked body?"
"After all, I do get to be fully clothed in my own dream, even if I went to sleep in my underwear."
"Maybe I’m the weird one...actually."

unn "What are you thinking so intensely about?"
y sadsmile"Oh, sorry, I was just…"


Y "Can I touch you?"
"His head, once again turns and shuffles but he doesn’t say a word."
Y "I could before, why wouldn’t I be able to now?"
y sadsmile"You didn’t shy away before..."
unn "That was...a special case."
y simple"How so?"
unn "I wasn’t inside your body back then, it wasn’t real."
y "Are you saying this...is real?"
unn "Aghh, I don’t know!"
unn "I never had to possess anyone before, this is all new to me as well."
unn "It’s not something I expected."
unn "But still, I thought I knew all there is to know about mind spells."

y sadsmile"So...do you want to experiment? See what we can and can’t do?"
unn "I mean… you can try, I guess… if you want."
unn "But I’m not expecting much."

"I take a few slow steps towards the mighty demon."
"A compliment I add just for the off chance that he actually hears my thoughts, this is technically my mind, after all."
show scribblesdreamhand with llongdissolve

"I extend my hand towards him, who in turn, raises his hand to match mine."
"Memories of our encounter earlier today flow back, the same emotions, same darkness, same scenario."
"Even in a dream, the heat of his scales warms my fingertips as we get closer."
"Closer…"
"Closer….."
play sound "audio/crack.mp3"
scene scribblesdream2 with hpunch
unn"!"
"A crack appears in the forever darkness."
"The light sipping through traces the outline of our hands, fingers phasing through one another."
y simple"I guess we really can’t touch."

unn "You have to get out."

y surprised"Huh? Why? What’s wrong? Is the light bad? It’s just a dream."
unn "Please, just…"
stop music fadeout 2.0
unn "This isn’t your mind." with longdissolve
if refuse_points>=1:
    jump aftertheriumrefusedream
else:
    pass
play sound "audio/alarm.ogg"
scene black
y surprised"!"
stop sound
y "Scribbles!"
if theriumbed >=1:
    scene theriumbedroom3
    jump guestorhorse
else:
    scene guestroom
    jump guestorhorse

label guestorhorse:
un bored"Sup?"
play music "audio/firstday.ogg" fadein 2.0
y angry"Don’t {i}'sup'{/i} me, explain yourself."
un "What dream?"
y "Don't gaslight me! You know very well what dream, so start talking."
un "I don’t want to."
y bored"Just like that? That’s your final answer."
un suspicious"Why do you feel entitled to every truth in the universe? Just. Drop. It."
y angry"You are SO!-"
y bored"Aghh, I won't get far arguing with someone with no body."
y "Fine, since you're so grumpy all of a sudden, I'll drop it, but only for the time being."
y "Because for now, I have other things to worry about."


if theriumbed >=1:
    y simple"Like where Therium is…"
    unn "You turn your attention towards the empty side of the bed, wrinkled sheets hinting someone slept there, and the still warm spot that the person only got up not long ago."
    y blush"I can’t believe we slept in the same bed…"
    un "But different blankets."
    y smug"Still."

elif theriumbed <=0:
    y "Like if Therium woke up yet or not."
    y "I should go check, and maybe wake him up if he hasn't yet."



else:
    pass
q"You look down at your semi naked self, noticing the erection forming out of nowhere."
y smug"Eh, just morning wood, thankfully no magic lust or anything."
y "I can ignore that for now."
q"You get some of the clothes from the luggage that of course is with you and has always been with you except for the times it wasn’t. Don’t think too much about it, you’re just thankful it is here now."
q"You get dressed with the same ol’ clothes as ever, jeans, shirt and tie."
y "Why change perfection?"
stop music fadeout 2.0
scene black with dissolve
q"You walk out the door and down the hallway, looking around at the few paintings and potted plants on the way."
play sound "audio/clutter.mp3" volume 0.1
q"Feet stomping and pots clinging can be heard from down below."
y simple"Guess that’s him, I hope he didn’t wake up earlier just for me…"
scene theriumroom0 with llongdissolve:
    blur 20


play music "audio/horse.ogg" fadein 2.0
q"You slowly descend down the stairs, the kitchen coming into view as soon as the last few steps are passed."
show horse apron with moveinleft
th "Good morning, early bug."
y sadsmile"H-hi."
q"The stallion woke up earlier and already showered, judging by the glistening fur and lustrous hair, almost shining in the morning sun rays, bent over the stove with a wooden spatula in hand."
q"An apron and underwear is all he’s wearing, a detail that is very relevant at the moment."
q"Remember when you didn’t have any unnatural lust inside you?"
q"Well, turns out seeing an almost naked, hung horse in front of you quickly changes your emotions."
q"You start bleeding."
show horse apronsur
"I start to what?"
th "Hey, your nose."
"Fuck."
y bleed"O-oh, oops, I...uhm, hit myself...in my sleep."
th "Let me help-"
y "No no! It’s fine, it will go away in a sec, I’ll go shower."
th "Alright."
th "There are some medical supplies in the cabinet there if you need any."
y "I’ll be fine! Not the first nose bleed, not the last, haha."
un bored"Not around him, at least."
scene shower with dissolve
play sound "audio/doorclose.ogg"
"Damn it Scribbles, this effect is so strong that it literally makes me bleed?"
"I thought nose bleeds only happened in cartoons."
un "It’s only strong if the lust rush comes right as something hot happens in front of you."
un "Who knew you’d drool so hard over some exposed skin."
un "Or was it the male-wife behavior that turned you on like that?"
stop music fadeout 2.0
scene black with llongdissolve
"Meanwhile..." with llongdissolve
scene theriumroom1 with llongdissolve
play music "audio/dark2.ogg" fadein 2.0
nu"Nice ass."
th "Again?"
th "Do you have nothing better to do?"
th "Or better conversation starters?..."
th "Did you even leave my dorm last night?"
nu "Too many questions, too early in the morning."
th "Just make it fast, before he’s done."
nu"The other two are looking for him."
th "And what am I supposed to do about that?"
nu"I’m just bringing the news, not the solutions."
nu "It’s on you to figure it out."

nu "Of course they’re looking for the other one too, but I doubt you care about him much."
th "I have no reason to care."
nu "Technically you do care, just in the opposite way…as in, you don’t like him one bit."
th "I told you before, once [name] came in, he became irrelevant to me, just apathy."
nu "And I’m saying you’re lying."
nu "You almost vomited while being in the same room as him."
th "Do you have anything important to say or can I throw you out the window now?"
nu "Sheesh, I’m going, Rudy McRudeness…"
nu "But remember, no attachments, for your own sake."
th "..."
stop music fadeout 2.0
nu "Adios."
scene black with llongdissolve
"Back to you..." with llongdissolve
scene shower with dissolve
play music "audio/purplecat.ogg" fadein 2.0
q"The water washes away the last few drops of blood while your second erection of the morning stands up proud."
y nakedbored"It’s not funny."
un "I never implied it was."
y "Damn it, what do I do with this?"
un curious"Uhmm, do you have no hands? Or is a dick in your ass an absolute must for you to cum?"
y nakedsad"It’s...kind of embarrassing to do it here, and maybe even disrespectful?"
un bored"Blood or semen down the drain, what’s the difference?"
un "It’s a lust rush for crying out loud, I can feel how it literally hurts you, just get rid of it."
menu:
    "Ignore it for now.":
        jump finallyshower
    "Let me think of something.":
        q "In this crazed mind of yours, the stallion's body appears behind you, pushing you donw on your knees."
        q "Kneeling beside you, he traces paths along your torso using oiled digits drawing intricate patterns that leave trails of shimmering droplets. His gaze lingers on every muscle flexing appreciatively while he works."

        q "Afterwards comes the main event; his large callused hands grip your hardened length tenderly stroking it gently till pre-cum emerges. Swirling motions follow followed by firm pumps causing an almost imperceptible moan to escape your lips."

        q "While massaging softly yet firmly, his other hand traces your thigh bringing chills down your spine. Every caress seems tailored to bring forth hidden desires aching to break free."

        q "Then he stands over you once more with a sense of purposefulness - each breath drawn out long and steady thrusts of his hips."
        q "You can only imagine his tip smashing against your muzzle, parting your lips and cutting your breath."
        q "Five? Six? Seven inches? Maybe more? Who knows how much that bulge of his holds, but for now, it is enough to graze the back of your throat and more, hypothetically, of course."
        q "But even this thought or idea has to disappear before it's finished, together with the Lust Rush that goes down the drain in the form of white, thick liquid seconds after."
        q "A sigh of satisfaction escapes your mouth, as you take a moment to regain your senses before getting back up on your feet."
        y nakedss"Fuck...this kind of orgasm is ten times better than regular ones."
        un "I really don't need a description."
        un "Are you done now? Can you start to actually shower?"
        y nakedsmug"Yes sir!"
        jump finallyshower





label finallyshower:

q "The unfamiliar shower surprises you with ice cold and scalding hot water, changing the temperature respectively at the slightest touch."
y naked"I already miss my own shower."
y "At least Therium's shampoo smells nice, I'll need to remember the brand."

q "You step out, dry your fur as much as possible and get dressed right then and there."
q "You feel refreshed and satisfied, today is a good fur day."
scene theriumroom with dissolve
scene CGt2
q "The horse waits for you in the living room, with two plates on the table and a now clothed body, greeting you with a smile, the smile he’s been throwing towards you since the moment you two met."

th "Sit down and enjoy, we have lots of things to discuss."
q "You do as he says, your mouth almost watering at the sight in front of you, was it a reaction for the food or the man? We shall never know."
q "The plate does not hold anything too special, eggs and some kind of fatty protein with lightly charred tomato slices and some toast, but it is the presentation that is so striking."
q "Immaculate, unbroken and evenly cooked eggs, with an almost mathematical distribution of black pepper on its surface, each ingredient spaced out, yet gently touching each other’s edges."
q "The taste, as well, holds a curious natural distinction, where the flavor comes from no spice you can name from the top of your tongue."
q "This simple creation might’ve captured the narrator’s attention more than yours, but still, one descriptive word escapes your full mouth nonetheless."
y food"Delicious!"
y "Again, as expected from the master chef himself."

th "I had a feeling you’d say that."
y smug"Those exact words?"
th "Would you believe me if I said yes?"
y "I am quite predictable."
th "Then yes, those exact words."
y surprised"Wow!"
th "Heh, but really, this time I can actually believe you, I’m almost forced to master breakfast items, since you know, no free breakfast cards."
y pf"I’ll have to get down to the bottom of this breakfast scam mystery."
th "Good luck with that, you’ll probably have the support of at least half the academy."

y s"You mentioned something about...discussing things?"

th "Right, that."




th "So first off, the auditions start at noon, keep that in mind in case I’m not around."
th "I’ll be part of the judges, so don’t expect me to be too harsh, not for now, at least."
q"He winks."
play sound "audio/fluster.mp3"
y blush"W-why so?"
th "I know what you’re capable of, no matter what you do out there."
th "You might not be very talented but you definitely have what it takes, it’s understandable you’d be chosen."
th "To enter the Shard, that is."
y simple"Great?"
q "You’re not quite sure if what he said was a compliment or not, but it was the truth, that’s for sure."

y s"Alright, so noon and I don’t have to worry much, that’s nice."
th "Now, to more important matters..."
th "What do you want to do until then?"

y simple"Uhmm."

y s"I still haven’t seen my dorm, that might be a good place to start my day."

th "Oh goodness, I’m probably to blame for that, let's go then."
y surprised"Like, right this moment? -Ah!"
q "You stuff a last morsel of food in your mouth as the excited stallion brings your luggage from your room, barely managing to grab your bag of essentials with you as he drags you along."
scene dormhall with dissolve
y sadsmile"Let me help with that, it’s my luggage after all."
th "We stay in different dorms, but yours is pretty close so it’s fine, it’s not like it’s that heavy, these muscles aren’t just for show."
y blush"I can tell that much."
stop music fadeout 2.0
y ec"To dorm building number three we go!"
play music "audio/outside2.ogg" fadein 2.0
scene chibitherium2 with llongdissolve
q "The walk is peaceful and quiet, being so early in the morning it seems like the townsfolk like to start the day slow."
q "Few shop owners wave at you two as they sweep the front of their establishment, getting ready to open for the day."
y s"People are friendly around here."
th "Isn’t that what the whole nation prides itself in? Happy, kind and satisfied people."
y pf"There are nasty people everywhere, they’re like cockroaches, appearing out of nowhere, some of them can even fly."
th "That I can’t argue against, but I do have to admit that this place is unique, those roaches haven’t crossed my path much since I came here."
y "Same with me actually, but I literally got here yesterday so it’s not telling much."

q "Continuing with your ethics mumbling, you don’t realize you arrived at your destination, and almost pass the building."
y simple"Oh oops, isn’t that it? Dorm three?"
th "It is, we got here faster than expected."
th "Or maybe it’s the beautiful scenery that took my attention."
y "Haven’t you seen these rounds hundreds of times?"
th "Wasn’t talking about that scenery."
y "oh…"
play sound "audio/fluster.mp3"
y blush2"OH!"
y blush"Heh, I-I get it, uhmm, let’s go inside."
th "After you."
stop music fadeout 2.0
scene dorm with llongdissolve

q "The inside of the building looks almost exactly the same as the previous one."
q "The students living in it put their own little spin and items through the hallways, overall the architectural structure is similar."
scene dormhall with dissolve
q "While ascending from floor to floor you just can’t keep those anxious thoughts away, ‘I shouldn’t be making him carry my stuff all the way up.’, ‘should I offer to help?’ ‘Am I an awful person that deserves to die alone?’"
q "All while the horse clearly doesn’t break a sweat and is not bothered by the insignificant weight."
un suspicious"Seriously, relax, you and your noodle arms won’t help much anyway."
"Hey! I have strength enchantments...but you’re right, asking if he needs help would be like asking the ocean if it’s thirsty."

q "At last, you arrive in front of your door, double checking just in case you’re mistaken, then use the keycard to open it."


Y s"Well, here we are."
jump invitetherium

label invitetherium:
play music "audio/horse.ogg" fadein 2.0
scene dormroom with dissolve
q "You hold the door open with an inviting gesture."
Y ec"Here is my personal little hole."
y pf"That sounded weird, my humble hut."
show horse with moveinleft
th "Looks nice, cozy."
th "Especially once you finish decorating it."
y smug"Already ahead of you."
q "You open up your luggage and take out some wrinkled clothes, some posters and other small personal belongings, excited to place them inside and make this room truly your own."
q "All while the horse checks out the main room and the bathroom."
q "After a couple of minutes you both sit on the surprisingly soft bed, looking out the window and around the room."

y "It really ain’t much, but it’s fine, at least no roommates."

show horse simple

th "You both sound and look disappointed."
y simple"Well yeah, compared to the luxurious apartments I’ve seen leaders and vice leaders getting this is...a little small."
y "Not even a kitchen, I haven’t read the rules, but I doubt I can have an induction stove here."
y "Maybe a microwave or an airfryer..."
show horse smug
th "A whole room to yourself, plus bathroom?"
th "A soft bed and cushions? A nice wardrobe and storage area, a desk, a cozy windowsill with a beautiful view?"
th "I don’t know...seems like the dream."
show horse bored
th "It sure is more than I ever had before coming here."
y "Here?"
y "The academy?"
y s"Ah, right, well, you are a vice leader after all."
show horse smug
th "No, not the academy."
th "The country."
th "Sure, now my dorm can almost be considered a penthouse because of my position, but it wasn’t like that when I had to pay rent in the city."
th "Although my life truly turned around once I came to the academy, heh, it sure wasn’t easy when I had to-"
show horse bored
q "He stops mid sentence, looking into the distance towards the sun still obscured by the distant mountains."
q "His lip and eyes quiver for a second, but his smile still stands."
q "You almost want to question him, but decide it might not be the best idea, for now at least."
q "For the moment to not remain in this awkward state, you decide to change the subject."

y s"Hey so what’s up with the leader? Now that I have a guarantee of getting in the Shard-"
q "You wink at him."
y smug"I’m even more excited to meet them."

show horse boredside

q "The subject change worked wonders, he seems to think hard about what to say."
th "It’s... difficult, you’ll certainly meet them at some point, everyone’s buzzing with the same question, and frankly, I’m not sure how much I can share."
y "I understand, important people confidentiality."
y s"But here’s something you can share, what’s your favorite Nightfallen type?"
show horse smug
th "Heh, that I could share, a simple {i}‘get to know you’{/i} question, but you go first, you intrigued me quite a lot now."

menu:
    y "Oh, for me it might be…"
    "Mimics.":
        y s "I like mimics."
        y "The way they imitate objects and people is very interesting, even if they're not great at it."
        th "One of the Nightfallen with the smallest IQ, yet they're trying so hard to be like us, and almost succeeding."
        y "They're one of the most harmless types."
        y "They're also eager to offer a good time before they're defeated."
        y "They also drop a decent gem for how easy they are to charge and defeat, no risk high reward."
        th "So that's your opinion."
    "Plants.":
        y s"Probably the plant kind."
        y "Most of them can't move much aside from a few appendices, so you can easily strategize against them."
        th "Unless you're ambushed by one."
        y "Most of them are harmless aside from the penetration thing, but that's a positive for some."
        un "Like you?"
        "No comment."
        th "So that's how you see it."
    "Cryptids.":
        y s"Cryptids are my favorites, for sure."
        y "They're just so...unique, you never know what you can find."
        y "Big, small, aggressive, friendly, weak or powerful, fleshy or furry."
        th "You're a fan of the unknown, huh?"
        y "I like surprises."
        jump choosenightfallen
    "Wildfurs.":
        y s"Wildfurs are definitely for me."
        y "Even the laws are on my side, being illegal to kill them and all."
        y "I also heard a lot of them can speak English, wouldn't even mind befriending one."
        th "You would be friends with a Nightfallen?"
        y "If a Nightfallen offers me dinner and invites me over to meet their family in my own tongue, I'd be a fool to not strike a friendship or more."
        th "Interesting answer, can't say many people would say the same."
        jump choosenightfallen
    "Savages.":
        y s"Big fan of Savage Nightfallen."
        y "Love their scales and rough, wild nature."
        th "What about all their flaws?"
        y "The risks are worth the reward."
        th "Really?"
        th "The torture of their prey, cannibalizing nature, blind and bloody berserk state they get into when they're hungry, horny or angry?"
        th "All those risks are worth it?"
        y awkward"Ummm....they're not all true, haha, r-right?"
        th "Course not, but not everyone knows."
        th "A spun story here and there and the crowd becomes a bunch of savages."
        th "Pun intended."
        y s"Thank goodness, because I certainly wanna meet one some day, just...maybe from a distance."
        jump choosenightfallen
    "Wyverns.":
        y s"Wyverns are cool."
        y "They're like Savages but...bigger."
        th "Much bigger."
        th "Much wilder, much...stronger."
        y "You like them too?"
        th "They remind me of my own favorite Nightfallen types, so yes, I'm quite fond of them."
        jump choosenightfallen
    "Demons.":
        y smug"Deeefinitely Demons."
        un "The only correct answer."
        y "I know they're sadistic, and should be avoided at all cost buuuut-"
        th "The danger allures you in, doesn't it?"
        y s"Yup."
        y "Hey, it's not my fault they're the most inteligent type."
        y smug"It's unfortunate they're such dicks though."
        show horse simple
        un "Bitch!"
        y ec"Yeah, and they're very bitchy, can't forget that."
        un "SLUT!"
        y "And don't get me started on how such sluts can be so bad at sex-"
        un "SHUT UUUP!"
        y "And their overall attitude, unpleasant creatures really-"
        show horse bored
        un "YOU-"
        th "I think that's enough."
        y simple"..."
        q "He stops you with a serious expression on."
        y sadsmile"S-sorry, got a little carried away."
        th "You have strong opinions about Demons for someone who loves them."
        y "Oh you know how it is, you hate the things you love most, haha."
        th "Not a saying I've heard thrown around much."
        th "In any case..."
        jump choosenightfallen


label choosenightfallen:
show horse smug
Th "Why the sudden question though?"
y s"My next five years are going to be surrounded by Nightfallen, I’d like to know everyone’s opinions on the different types, it’s also just an interesting personality question, don’t you think?"
th "I suppose favorite food or color are indeed boring questions."
y smug"Your turn."
show horse simple
th "My favorite type...honestly I thought it would be the same as yours."
y s"It’s not? What is it then?"
show horse smug
th "Dragons."

q "He turns his head towards you with a light smirk, which disappears slowly after noticing your confusion."
show horse simple
y simple"Oh, I didn’t even take them in consideration, sorry, I should’ve specified, only the types that exist."
th "You don-"
show horse ec
th "I mean, of course they don’t, and if I can’t choose that, then I’ll settle for wyverns."
y smug"A fan of big lizards, huh?"
stop music
show horse mad
play sound "audio/doorhit.mp3"
pause 0.8
play sound "audio/doorhit.mp3"
play sound "audio/button.ogg"
th "Dragons are NOT-"
show horse simple
play sound "audio/button.ogg"
q "A quick and light knock on the door interrupts your conversation, a sound as if somebody hit the door by accident."
play sound "audio/button.ogg"
q "You two turn your heads towards it, look at each other then get up to check."
play sound "audio/button.ogg"
hide horse simple with moveoutright
q "Approaching the door you hear murmured voices."
play sound "audio/button.ogg"

st1 "What was that?! You said you’re gonna knock."
play sound "audio/button.ogg"
st2 "I’m nervous, give me a sec."
play sound "audio/button.ogg"
st2 "It’s so early, he could be sleeping."
play sound "audio/button.ogg"
st1 "He’s not sleeping on the day of the auditions…"
play sound "audio/button.ogg"
st2 "You do it then."
play sound "audio/button.ogg"
st1 "I-"
play sound "audio/button.ogg"
play sound "audio/creak2.ogg"
scene dormhall with dissolve
show dormdoor with moveinright
q "You unlock and open the door, meeting face to face with the two bickering arrivals."
play sound "audio/button.ogg"
show rosesur at center
show coalsur at left
with dissolve
y simple"Can I...help you?"
play sound "audio/button.ogg"
hide rosesur
hide coalsur
show roseec at center
show coalec at left
st2 "Oh, Hi!"
play sound "audio/button.ogg"
st1 "Told you so."
play sound "audio/button.ogg"
hide roseec
hide coalec
show rose at center
show coal at left
r "My name is Rose and this is Coal."
play sound "audio/button.ogg"
y ec"Ah, the recommended students!"
play sound "audio/button.ogg"
hide dormdoor with moveoutright
play music "audio/littlehappy.ogg" fadein 2.0
q "You open the door fully now and get a bit more comfortable talking to the new people."
r "You remember! That’s a relief."
y s"I’m [name], nice to meet you."


st2 "Sorry, we didn’t come at a bad time, did we?"
y "Definitely not, wanna come in?"
r "That’s alright, we’re not going to intrude for long."
co "We didn’t want to show up uninvited at all, but we’ve kind of been looking everywhere for you and we were all out of ideas for your whereabouts."

th "So why come here at all?"
show horse bored at right with moveinright
show coalsimple at left
show rosesimple at center
q "The stallion shows up from behind you, the rabbit and panther seem very surprised by his presence."
q "He leans by the door right behind you, looking at them with crossed arms and with a-"
q "No, not the usual charming smile anymore, apathy taking its place, resting in his eyes."

hide rosesimple
hide coalsimple
show rosesadsmile at center
show coalsadsmile at left
r "Oh, you have a visitor, our appearance now is even more awkward, isn’t it?"
co "Who’s your friend [name]?"
th "I’m pretty sure you know me very well."
show coalec at left
co "That’s right, we’ve met before, vice leader of the Slayer’s Shard."
th "Summoners."
hide coalec
co "Ah, apologies, we’re both new, not just in the academy but the country in general."
y "I could tell by your accents but didn’t want to make assumptions."
th "What business do you have here?"
r "Of course, straight to the subject, well, besides meeting [name] In person-"
q "She winks at you."
r "we wanted to ask him, have you seen Alvy by any chance?"
r "The last recommended student."
co "He’s even harder to find than you, heh."



y "Yeah, I have actually!"
y sadsmile"I know he’s kind of slippery, doesn’t seem to want many new friends."
q "You decide to leave out all the awkward moments you had with him."
y "I have no idea where he is though, have you tried his dorm?"
r "Yeah...no luck."

r "A shame, I hoped we could get the gang all together and have a chat."
y s"Maybe some other time."
r "Since you have company we’ll get out of your fur, come on Coal, maybe we’ll find him at breakfast."




co "Yeah, we wouldn’t want to stand between you two, and certainly hope we didn’t ruin the mood."

r "It’s morning Coal, I’m sure they weren’t doing it this early."
hide coalsadsmile
show coalsmug at left
co "I don’t see a problem with doing it early, gets the blood rushing."
co "Mornings are the busiest when it comes to guys, you wouldn’t know."

q"Realization settles in slowly, thankfully, the horse left the conversation right as they started their goodbyes, so you manage to contain your redness at skin level."
play sound "audio/fluster.mp3"
y blush"W-we’re not! I mean we didn’t do anything!"
y "Not this morning, not ever!"
y "Not like that, at least."

r "Oh, silly us, sorry for assuming."
co "We wouldn’t blame you though, heh, maybe you’re losing a good catch if you don’t act sooner."

r "But we should really go now."
hide coalsmug
show coal at left
hide rosesadsmile
show rose
co "Don’t be a stranger around us now, alright?"
co "Recommended students stick together!"
y ec"Of course, have a nice day!"
hide rose with moveoutleft
co "Oh, almost forgot, the Headmaster mentioned he wants a word with you in private."
co "Ok byeee!"
stop music fadeout 2.0
hide coal with moveoutleft
q "Hearing that the horse steps behind you again, but the two are already on their way down the hallway."
scene dormroom with dissolve
show horse bored at center with moveinright
play music "audio/horse.ogg" fadein 2.0
y simple"The Headmaster? With me?"
y "What do you think it is?"
y "I’m not in trouble, am I?"
show horse sadsmile
th "No, of course not, why would you be?"
th "But I’d lie if I said I know the reason."
y "Should I...go now?"
th "Definitely not, I doubt he has time."
th "Usually if the Headmaster doesn’t specify the time it means whenever you have time, not sure how mister Argus does things but if he wanted special treatment he should’ve told you the time."
y "That’s true…"
show horse bored
y worried"Auditions...meetings...ughh, I’m just a student and the responsibilities are already getting to me, haha."
q "The horse is not amused."
y sadsmile"Ah, sorry, you’re a vice leader, my complaining must sound silly."
th "You’re going to have to get used to it, I’m afraid, it’s only getting harder from here."
y "Tests...classes, yeah, I don’t doubt that."

y s"So...uhm, where do you want to go?"
show horse simple
th "Me?"

y "Yeah, I doubt staying in this cramped room is any fun."
y "I don’t mind hanging out outside."
y "If you’re not too busy, that is."
show horse
th "Course not."
th "Let’s see..."
show horse ec
th "Well, I quite enjoyed teaching you things and seeing you learn yesterday, so why don’t we continue?"
y ec"Great! Back to the Summoner’s spot?"
th "Oh no no, I’m assuming you haven’t seen the market yet, right?"
y s"No sir, no market has reached my eyes nor my ears, but I am intrigued."
show horse smug
th "Then follow me, cutie."
play sound "audio/fluster.mp3"
hide horse smug with moveoutleft

q "Excitedly you start following the horse trying to hide your blu-"
th "Don’t forget to lock the door."
y sadsmile"Oops, almost forgot."
scene dormhall with dissolve
un squint"Motherfuckers be cutting the narrator off like I’m some sort of extra in a movie."
"Don’t get huffy, you get to talk more than all of us."
stop music fadeout 2.0
"That just comes with the job, gotta deal with it."
play music "audio/forgetmenot.ogg" fadein 2.0
scene chibitherium2 with llongdissolve

un sidee"This is harder than I thought...maybe I signed up for more than I could handle…"
"Don’t give up now! You’re doing such a good job!"
un "You...you really think so?"
"Yeah, I’d almost say better than myself even."

un "Well...I guess I have to continue, wouldn’t want to switch to an inferior narrator then."
un pride"{i}*Aghem*{/i}"

q "The way to this market is quiet, but not awkward."
q "The horse stays silent for the most part, as if getting ready to present a surprise, and is refraining from spoiling it."
q "His silent treatment didn’t matter much, as more and more locals got the courage to greet and talk to you."

loc1 "You’re a new face, hope you have a nice stay, don’t let the monsters get you at night, haha!"
y awkward"I am, and thank you so much! I hope the barrier will keep them away, heh."

loc2 "Another student I presume? Good luck with those nasty Nightfallen."
y ec"I’ll dedicate my next fight to you, random citizen!"
loc3 "Come by my shop for big student discounts, little leopard, more Nightfallen slain the bigger the discount!"
y s"Thanks I’ll keep that in mind!"
y "Not like I’ll have a big number in my first year though, heh, isn’t that right, Therium?"

q "While talking with and greeting all these strangers you slowly realize something’s a bit strange."
q "Nobody pays any mind to the horse, and he doesn’t mind them either."
q "As for your question, he, like usual, thinks about the answer for a long time, as if he wanted to stay silent and ignore it altogether, but changed his mind."
th "Let’s just say me and the locals...we have different views on the world."

y simple"You don’t get along with them?"
th "Not that, I’m not a renegade, [name], they simply know small talk and forced ideologies won’t work on me."
th "In a society, everybody builds their reputation through surface level images, and my image just so happens to be the silent, mysterious type."
th "For better or for worse, usually better for me."
y s"Loners and mystery, my favorite combo."
th "Is that why you chose me?"
y "Chose you in what way?"
stop music fadeout 2.0
th "Ah, never mind, we’re here!"
play music "audio/market.ogg" fadein 2.0 volume 0.8
scene market with llongdissolve

th "Surprise!"
th "Although it’s not much of a surprise, I already told you where we’re going and what we’re doing here, to some extent."

q "You look around for the tents holding fruits and vegetables for sale, silks and clothes, magic items and scrolls, street food and live animals, and although you do see some of the desired shops, most of them are actually filled with-"
y surprised"Gems!"
y ec"Energy crystals!"
y s"Is this whole area filled with crystal vendors?"
show horse with moveinleft
th "Bingo, guess I don’t have to explain what we’re doing here then."
y sadsmile"Oh no, please, do explain everything in detail, I’m stupid."
show horse ec
th "Ha, that’s harsh, but fine."
show horse
th "The auditions, as I said will not be too complicated for you, but there is one thing you need, and that is a Nightfallen gem."
th "We could get one from the academy, like most other students, but you’re not like any other student, are you?"
y s"I like to think I’m special, but definitely not in the ways of summoning."
th "That’s why it would be best to get you a gem you connect well with."
y simple"Connect with?"
show horse simple
th "You...don’t know about personal connections?"
y awkward"S-should I?"
show horse bored
th "{i}*sigh*{/i}"
th "Yes, it is a pretty important part for beginners."
th "And unfortunately it’s not something I can really explain, you’ll just...know when it happens."
show horse
th "For now, let me give you a rundown of the available gems."
y smug"Please do, assume I know nothing."
th "Of course."
th "After that you can choose one that resonates with you, hopefully it won’t be one that’s too expensive."
th "Or one from a scammer."
y surprised"There are scammers?"
th "Of course, most of them are, that’s why we won’t buy anything unless you specifically resonate with it, and even then, we’ll be careful."
hide horse with moveoutleft
q "He guides you to the first tent, holding many big blue gems with an uneven and stony but still shiny texture, small holes visible on its edges."
th "First lesson, do you see how rough these are?"
y simple"Yeah, does that mean they’re lower quality?"
th "In a way, it means they’re dead."
y surprised"Huh?"
y worried"I thought...all Nightfallen summons are dead."
show horse simple at left with moveinleft
th "Really? You never heard of a Nightfallen living inside their gem?"
y simple"Uhmmmm…..no?"
q "You chuckle awkwardly."
show horse smug at left
th "Heh, no, my friend, certainly not all, but even so, you won’t find any live ones anywhere around."
y "Why’s that?"
play sound "audio/excuseme.mp3"
q "Hearing your conversation, the owner, a tall, well dressed man, who has been watching you two attentively decides to throw his cigarette down and approach his clients, at last."
show vendor at right with moveinright
q "His expression is sour as he steps on the discarded smoke."
q "His deep and hoarse voice almost makes you shudder, but it does not faze the horse."

v "They’re high quality gems, bought directly from the hunters of this very academy."
v "There is nothing wrong with them."
th "Of course sir, never said there’s something wrong, well, except for the outrageous prices on what is basically mere energy fodder."
v "Werewolves are hard to kill."
th "I doubt you’re the one who hunted them."
q "The tension around thickens with each word exchanged, you decide to say something."
y sadsmile"I-I’m sorry for my friend here, he’s very picky and might I even say, judgmental."
show vendor smug at right
q "The vendor calms down and softens up, directing his attention towards you, the customer who has not yet insulted his products."
v "You can say that twice, only guy in town to have a problem with my stuff."
show vendor at right
th "Only one with common sense."
q "You swear you just saw electricity forming between their eyes."
show vendor smug at right
v "Aaanyway...what can I do for you, little guy? Anything tickling your fancy"
y smug"My attention was caught at {i}‘werewolves’{/i}."
v "Aah, you have fine taste."
show horse bored at left
th "He says that to everyone."
y "How much for all of them?"
show horse mad at left
th "[name]!"
v "Oho, you want to form a whole pack, huh? Won’t even ask why, I’m sure you have totally innocent and non perverted reasons."
v "I’ll tell you what, if you buy 5, I’ll cut the price down a little."
v "How about...forty five."
show horse bored at left
y sadsmile"...dollars?"
v "…"
v "Bwahaha, you’re a funny little guy, ain’t ya?"
v "Keeping me on my toes."
v "Grands, forty five grands."
y simple"Therium…"
th "Yes, [name]?"
y pf"I just found some extra respect for you here in my wallet."
q "You say still wide eyed."
q "Your werewolf harem will have to wait..."
hide horse bored with moveoutleft
th "Yeah...can’t say I’m surprised, let’s go."
show vendor smug at center with ease
v "Come ooon, they’re the highest grade summons you can find! Come back! Forty? Thirty five? Final price!"
scene market with dissolve
q "You continue down the rows of boutiques, one of which catches your eye, mostly because the gems it sells are much much smaller than the previous ones, with a lot of variety in shapes and colors."

y s"Oooh, how about these?"
y laugh"Look, this one’s twenty dollars! They’re so cheap!"
show horse sad with moveinleft
th "Uhmm, [name]...do you know what kind of gems those are?"
y sadsmile"Nightfallen gems?"
show horse simple
th "Yeah, but surely you know the different kinds of gems right?"

y pf"Yyyyee-"
y bored"No."
show horse smug
q "Instead of sighing at your stupidity, this time, the horse chuckles to himself, as if he finally realized there is no point in being surprised anymore."
"In my defense, I never thought I’d be a summoner until I met you…demon."
q "Nonetheless, his expression softens and a kind voice comes out."

th "These are energy crystals, do you know how these are created?"
y s"By killing Nightfallen, right?"
th "Yes, and what you need to know is that these are worthless for summoning, they don’t contain any Nightfallen, nor dead nor alive."
th "A regular hunter will kill the Nightfallen and collect the crystal, while a summoner will push the Nightfallen inside the gem, trapping them for a while."
y simple"About that, what do you mean...dead or alive?"
th "Usually these gems people sell are filled with the memories of Nightfallen, weaker, fainter versions of what they once were."
th "The ones that are trapped alive, can be released at any point without harming them."
th "The benefits being a stronger bond with them and much stronger Nightfallen."

y "I never knew that, and it seems like a lot of people don’t know either."
show horse ec
th "Oh, but of course they do, it’s just too much of a hustle to keep live Nightfallen for sale, the memories will never disobey their masters and won’t act out of turn."
stop music
show horse shock
show light with hpunch

q "A flash of light followed by terrified screaming can be heard just up ahead."
play music "audio/crowdd.ogg" fadein 2.0
q "You two drop both the gems and your conversation and direct your attention towards the commotion."

q "Dozens of people run past you, a lot of them seem more confused than anything."
show horse shock at left with move
y worried"W-what is that?"
show bigdog at right with moveinright
hide light with dissolve
q "Rounding the corner, you see a creature, a big, bull like Nightfallen with big boulders growing from its back."
q "You are thinking about doing a quick heel turn and run in the opposite direction, but your partner here doesn’t look too concerned."
show horse ec at left
th "Ladies and gentlemen, please do not be alarmed!"
th "This is an academy exclusive training exercise and everything is under control!"

loc1 "Hey, that’s the Summoner’s vice leader!"
loc2 "Oh thank Goodness."
loc3 "I thought we're in actual danger, haha."

q "Any kind of panic buzzing around disappears, and the people around watch you two and the Nightfallen attentively, just...from the sidelines."
q "Some of them cheer on, some laugh and gossip among themselves, but nobody is running."
q "The Nightfallen stops as well, somewhat sad that his toys stopped running, until his red glowing eyes focus on you and the horse, the only people still in the middle of the road."
q "Then...he charges."

y sadsmile"What a relief this is only a drill, I have no idea what to do in a situation like this, hah, who is coming to take care of it?"
th "Nobody."
y shoked"What?"
th "It’s not a drill."
stop music
th "Run."
hide horse ec with moveoutleft
y shoked2"WHAT?!"
play music "audio/chase.ogg" fadein 2.0 volume 1.0
hide bigdog with moveoutleft
show chase20 with moveinright
q "Your hand is suddenly snatched by the powerful stallion, and within seconds your peak acceleration is reached."
y "AAAAHHH!"

th "Use a speed boost [name] and keep up!"
q "You do as he says after recovering from the short lived shock."
q "This chase taught you one thing from the start, and that’s that horses can truly run like the wind."
q "You wonder what other stereotypical qualities about them might be true, do they have a gigantic co-"
"NO I’M NOT WONDERING THAT! I’M TERRIFIED!"
un "Wha-really?"
q "It would seem the narrator made a mistake for the first time, the adrenaline is too strong even for this dirty leopard’s mind."
q "But can you really blame me?"

y scream"What is a Nightfallen doing inside the barrier?!"
th "No idea!"
y "Why is it chasing US of all people?"
th "Would you rather it chased civilians?"
y "I’d rather it chase an experienced hunter!"
th "I am literally the vice leader of a Shard."
y "Great! Then team up with another one instead of me!"
th "If you want we can split up and-"
y "NO WAY!"
y "That’s how you die in horror movies!"
th "This is not a horror movie."
y "Of course you think that, with that smile on your face!"
th "Hah, I’m just enjoying the wind, don’t you feel it running through your fur? Doesn’t it feel so free?"
q "Your breath starts to go away as fatigue sets in, and can barely muster a word."
y worried"Where are we running?"
th "We’re almost there, just a little more."

q "The monster behind you is getting closer, having much more stamina than you two."
q "You can feel his angry eyes scorching the back of your head."
"Scribbles! Can you do anything?!"
un "I could, but the horse has everything under control, just trust him, he’s a summoner."
y angry"IT’S KIND OF HARD TO DO THAT RIGHT NOW!"
th "Huh? Do what?"
y awkward"R-RUN! IT’S HARD TO RUN! I’M TIRED!"

th "Well, good news."
show chase21 with hpunch

q "He lets go of your hand suddenly and turns around."
th "We're here."
q "Now face to face with the incoming beast, he plants his feet hard in the ground, far apart, taking a defensive fighting position."
q "The fast break made you lose balance and fall on your back, just behind him."

y surprised"What are you doing?!"
"Scribbles, get ready to protect him."
un "You heathen little fool… just watch."
show chase22 with dissolve
q"Without responding and with the confidence of a God, he extends his arms forward."
q "The Nightfallen’s momentum does not slow down, but…"
q "His material body does."
q "It’s body transforms to smoke and energy, going inside a little gem from between the horse’s hands."
q "You swear there was no gem there before, but it’s not like you were that focused on what he held when that thing was coming closer."
q "Within seconds the Nightfallen is no more, only a last loud, echoing roar can be heard as the last traces of black smoke gets sucked into the green gem, making it glow brightly."
th "Ta da!"

q "The horse turns to you, bows deeply, presenting the newly acquired gem, before tossing it over your head."
q "You only now realize you are basically at the exact edge of the barrier, one more step back and you’d be sucked out."
q "The gem phases through with no difficulty, but once it hits the ground, the Nightfallen gets released."
q "It looks back at you with annoyance, but no more hatred, at least, and trots away towards the forest."

th "Poor guy was probably scared out of his mind."
th "How are you holding up, [name]?"
th "You must be even more so-"
stop music
show chase20:
    blur 10
show chase21:
    blur 10
show chase22:
    blur 10
with dissolve
play sound "audio/fluster.mp3"
show chase23
th"Oh..."
th "Guess, you're fine?"
show chase24
"Brrrr."
show chase25
play music "audio/happy20.ogg" fadein 2.0 volume 0.5
y laugh"I don't even know what happened but YOU WERE AWESOME!"
y "I think I got a little too excited for a moment."
th "You mean what I just did was awesome or-"
y ec"Everything."
y "Everything you did!"
y "From start to finish!"
y sadsmile"I have sooo much to learn from you!"

th "Heh, you can’t teach someone without spilling your own secrets, so here’s something you didn’t know about me, [name]."

th "I have a special little ability that allows me to trap Nightfallen inside a gem whenever I want under no conditions, the only downside is that it only lasts a couple of seconds."
th "It’s not that impressive under normal circumstances, but it does leave Nightfallen disoriented, not that mention that-"
y surprised"-gems can go through barriers no problem!"

th "You catch on quick."
y "I noticed you didn’t have a gem before, I assume you just...created one from thin air?"
th "Not quite, I stole the Nightfallen’s gem from within him, which forced the rest of his body to follow."
y s"That is so cool!"
y simple"But why did it attack? And who summoned it?"

th "For the second question, I have no idea, for the first, well, as I said, he was scared."
th "It wasn’t a savage fur, it didn't have murderous instincts, and it was certainly not lustful, so it was simply doing what it thought was best to survive."
th "A cornered animal is most dangerous."
y sadsmile"I would attack someone too if it seemed like the only way to stay alive."
th "Exactly."

y simple"Who do we report this to?"
y "The mayor? The Headmaster? Some leader?"

th "Oh no no no, we do not speak a word of this again."

y "Why not?! It’s a big deal, isn’t it?"

th "That is precisely why. We don’t want to create a commotion."
y "Ah, you did call it a {i}‘drill’{/i} before."
th "This place is supposed to be the most secure place in the country, from Nightfallen at least, if word gets out that there was an attack…"
th "It’s best we do our own detective work before jumping to conclusions."
y sadsmile"I understand."
y "I take it you don’t hold the Headmaster’s confidentiality to high regard, or any public figure for that matter."
th "Why should I? People are flawed, even the most trustworthy person you know can end up spilling your secrets."
th "Bribes, foolishness, mistakes whatever the reason, it can happen."
th "Even Dallan."

y simple"Why Dallan specifically?"
th "Sorry, I forgot context, you don’t know him well enough, it’s not like you spent many intimate moments with him alone, hah. Dallan is simply known to be very reliable, unless you break rules."

y smug"Hmmm, I’m not sure if your argument is coming from a place of trauma or deep wisdom, but I’m willing to listen to someone who can trap Nightfallen without killing or seducing them."
y surprised"{i}*Gasp*{/i} Is that one of the reasons you’re a vice leader?"
stop music fadeout 3.0
th "Among other things."
show blink with dissolve
q "Abruptly as you speak, you begin to feel lightheaded and your feet turn to noodles."
th "Hey, you alright?"
q "The horse steps forward to catch you, but you manage to balance yourself enough to stay up, and I…"
q "I don’t know why this is happening."
q "And neither do you."
hide blink with dissolve
play music "audio/horse.ogg" fadein 2.0
y tired"Sorry, I just felt dizzy for some reason."
y sadsmile"Might be from running so much, haha."
y "The adrenaline rush is only now disappearing."

th "That might explain it, but the auditions will start soon, will you be ok?"
y "Of course, there won’t be much fighting involved anyway."

q "You check your phone for any notifications and the time."

y simple"Hey, what do you mean soon? We still have two hours."

th "You forget you still don’t have a gem to summon, since we didn’t find one at the market."

y bored"Oh yeah, in my defense, I doubt we would’ve found any at those prices."

th "I’ll drink to that."
th "As I said, scammers."
th "Now, shall we?"

q "He offers you his hand with a smirk, which you accept with sweaty palms and warm face."
y blush"We ran all the way here holding hands, makes sense we go back the same, haha, r-right?"
th "Sure...and I want to guarantee that you won’t faint."
y pf"Oh...of course."
un sidee"Awkwaaard."
stop music fadeout 2.0
"Shut up…"
play music "audio/forgetmenot.ogg" fadein 2.0
scene chibitherium2 with llongdissolve
q "The two of you walk side by side, this time at a slow, steady pace."
q "Destination? The arena."
q "On the way, many town’s folk appear to congratulate you."
q "Some of them, especially naughty kids, ran all the way from the market behind the Nightfallen to witness your ‘drill’."
q "While others found out through word of mouth and didn’t shy from throwing a compliment or two."

q "The horse didn’t seem to mind them much this time either, but you can tell that somehow...he’s more content with this situation."
stop music fadeout 2.0
scene arena2 with dissolve
q "You arrive at the arena, the whole place already buzzing with students and getting slowly filled up."

q "Instead of the main gate, the horse takes you through a side entrance."
play music "audio/catjazz.ogg" fadein 2.0
scene underarena with dissolve
q "The room you walk in is cold and quiet, a small room that is a mere distraction from the actual Nightfallen shards storage space."
q "The horse takes you down a set of stairs, into a sort of large, modernized cellar, you’re happy to find out that it isn’t completely empty."
show horse at left2 zorder 3 with moveinleft

th "Meet some of your new Shard mates, all the students here are, or at least should be, first years of the Summoner’s Shard."

q "Upon entrance the people in the room look at the tall horse, realizing their vice leader just walked in. They murmur excitedly but none of them dare approach while you’re at his side."

y simple"I wonder if he’s here…"
q "You look around for a small dog, but he’s nowhere to be seen."
y "Hmm, maybe he already got a gem shard."
show table zorder 2 with dissolve
q "The main attraction of the room is a fancy looking wooden booth, with certain a character managing it."
show luis at right2 zorder 4 with moveinright
st "Hey Therium, here to check on the fresh meat?"
show horse smug at left2 zorder 3
th "I’m more occupied with this specific specimen."
q "He grabs your shoulders and presents you to the man."
show luis simple at right2 zorder 4
st "This little guy? Why on earth- oh."
show luis at right2 zorder 4
st "He’s one of them special ones, aren’t you, lil' fella?"

y ec"If by special you mean recommended then yes, sir."
y pf"{size=*0.5}And I'm not that small...{/size}"
show luis smug at right2 zorder 4
show horse mad at left2 zorder 3
st "Huh, how come you’re riding his dick?"
q "Your eyes get wide at the sudden comment and the horse frowns."
show luis at right2 zorder 4
st "Not a fan of strong language I see, my bad."
st "I’m just surprised a loner like you has someone tailing them, that’s all."
show horse bored at left2 zorder 3
q "He gives you a little smirk and a head nod."
st "I’m Luis, by the way, nice to meet you."
q "He extends his hand which you accept immediately, but try your hardest to ignore the metallic feel on your fingers."
q "It is almost as hard to ignore as his uncovered torso."
q "He seems to like the attention it brings, as many other students steal glances at him while pretending to look at the array of gems behind him."
y s"Nice to meet you, are you a student? Or perhaps a teacher?"
lu "Nah, neither, just an employee."
lu "I’m here to take care of the gems."

th "Speaking of, he needs a gem, would be lovely if you could do your job."
show luis smug at right2
lu "Oh, like I’ve been doing since early morning?"
hide luis smug with moveoutright
q "He gestures to the whole room, many of the students are indeed checking out the new gem they burrowed."
show luis smug at right2 zorder 1 with moveinright
lu "Also, really? You don’t have your own gem? Hard to believe as a recommended one."

y sadsmile"I was scouted for my magic abilities, not summoning expertise."

lu "That would explain it."
y simple"Did the other recommended student not get a gem yet either?"
show luis simple at right2 zorder 1
lu "Y’all got two of them?"
lu "Hardly seems fair."
th "What’s it to you?"
show luis smug at right2 zorder 1
lu "Me personally? Absolutely nothing, but the drama these recommended fellas bring is always fun."
lu "Remember when you came around?"
lu "Half the defenders swore they’ll off themselves since you didn’t join them, heh, that was funny to watch."
y simple"Sheesh…"
lu "It's not every day that the Headmaster himself recommends someone, after all."
y "You were recommended by the Headmaster?"
lu "Might as well call it a formal invitation to join at that point."
th "Can we get on with it? Just get him a shard please."
lu "Fine, full name please?"

y s"My name is [name] [name2]."


lu "[name] [name2], heh, kind of funny, alright, and what level would you say you are with summoning?"
y pf"{size=*0.5}What's so funny about it?{/size}"
lu "Maybe this will be the first time I’ll actually bring out a demon from the back since Therium."
lu "Haven't opened those Demon safes in ages."
show luis simple at right2 zorder 1
y awkward"Uhmm, beginner is fine, haha."
lu "Seriously?"
Th "He said he was scouted for his magic, didn’t he?"
hide luis simple with moveoutright
lu "Right right...well, here is our low to intermediate batch."
show luis at right2 zorder 1 with moveinright
lu "See if there’s anything you like."
show gembox zorder 5 with moveinright
q "The man brings out a box with five shards, rough, small gems, some of them looking like broken glass, and presents them to you."
th "Don’t rush, [name]."
y simple"Let’s see."
q "You hover your hand from one corner to the other, trying to decide, when you all notice one of the gems starting to glow...ever so faintly."
th "Looks like we have a winner."
show luis simple at right2 zorder 1
lu "Huh."
y simple"Something wrong?"
lu "Oh no, it's just that I never saw that one glow before."
lu "I mean, everyone always avoided it anyway since it is broken in half, but still."
hide gembox with moveoutright
show luis at right2 zorder 1
q "You pick up the stone and inspect it, it is significantly bigger than the others, but also indeed more damaged, looking like a crescent moon with sharp edges."
y s"I really like it actually, it gives in an interesting shape."
lu "Glad it resonated with you."
lu "Now sign here, and don’t forget to bring it back when you’re done with it, I assume that will be after the auditions."
y ec"Yup, right after."

lu "Nice, good luck on those auditions, magic man."

y "Thanks! See you around, Luis."

lu "I sure hope so."
hide luis
hide table
with dissolve
hide horse bored with dissolve
q "He winks before turning away."
y s"What a nice guy."
th "Yeah, too nice for his own good, poor man."
y simple"What do you mean?"
stop music fadeout 3.0
scene black with llongdissolve
th "Let's just say he wasn't born without an arm."


scene arena2 with llongdissolve
q "You walk out and make your way to the actual arena."
play music "audio/happy20.ogg" fadein 2.0
q "Thankfully the place is big enough to host the entire academy and another one on top of it, so there are plenty of empty seats even if the event is as popular as it is."

q "Before your butts could even touch the seats properly, the horse’s phone rings, and he excuses himself for a moment."
y bored"Again."

q "The whole arena fills with the voices of the wolf friend of yours and his vice leader raccoon."
y ec"Dallan and Chelsie!"
d "WELCOME TO THIS YEAR'S NEW AND IMPROVED AUDITIONS!"
ch "Allegedly."
d "WE’LL BE KICKING THINGS OFF WITH THE SORCERERS, MORE SPECIFICALLY-"
ch "WOAH WOAH WOAH, EASY THERE PARTNER-"
d "HUH?"
ch "YOU DON’T WANNA PRESENT THE FIRST PARTICIPANT BEFORE YOU FIND OUT MORE ABOUT HOW TO TAKE CARE OF YOUR PRECIOUS FUR!"
d "OH BOY…"
ch "TIRED OF BALDING SPOTS? GOT A NASTY RASH THAT MAKES YOUR ONCE BEAUTIFUL FUR FALL OUT?"
h "Chelsie…"
ch "YOU WANT A GORGEOUS, LUSTROUS MANE AS THIS BREATHTAKING LION SPECIMEN BESIDE ME?"
h "Go on…"
ch "FOR ONLY 398.95 A MONTH, I CAN HELP YOU AND YOUR LOVED ONES-"
q "Her voice trails behind as the voice of another eccentric friend of yours comes in."

show cat20 with moveinleft
T "Hole guy! You came!"
y simple"Hmm? Oh-"
y pf"Yeah yeah...listen, is it allowed for someone to sell unlisted pharmaceutical products on campus?"
hide cat20
show cat20simple
t "Huh? Yeah, sure, I don’t know, maybe, no? why?"
t "I’ve done nothing of the sorts, especially not anything related to enlargement pills that worked a little too well on some people."
y "I...Let’s change the subject."
hide cat20simple
show cat20ec
t "Yes! Absolutely, here is Coal, say hi to Coal."
show coalec at left with moveinleft
t "My new best friend!"
t "Besides you, of course."
show coalsadsmile at left
t "A promise I would never give you up, let you down, run around or desert you!"
play sound "audio/rick.mp3"
t "Coal is great but you're my number one, [name]!"
co "{i}{size=*0.5}I don't even know his name, help.{/size}{/i}"
q "For the first time you notice the politely smiling panther next to him."
y smug"Oh, hey again."
co "Hi, [name]."
hide cat20ec
show cat20
t "Oh, you know each other? Great, don’t need to continue boring introductions."
t "So, you’re auditioning too for the summoners!"
t "Me and Coal will demolish the competition for the sorcerers, sorry to say but we’ll be the center of attention today."
hide coalsadsmile
show coalsimple at left
co "There is no competition...it’s auditions."
t "That’s what losers say to feel better."
t "We’re the first ones on the list, make sure to cheer for us!"
y s"Oh I sure will, you’ll definitely hear me all the way from here."
t "That’s the spirit!"
hide coalsimple
show coal at left
d "WITHOUT FURTHER ADO! Hopefully…"
co "This is our queue."
t "Yup yup."

y ec"Good luck!"
hide cat20 with moveoutright
hide coalec
hide coal with moveoutleft
q "The cat is the first one to jump into the arena, and his task is to simply destroy a dummy with magic."
q "Easier said than done...the dummy being a four meters tall snake like wooden structure enforced with metal armor and weapons."

q "Even so...the cat had absolutely no problem with it, none whatsoever."
q "He simply shot a spell at the dummy, which made it teleport high into the air, and the rest of the damage was done by gravity."
q "Next thing the audience knows, the dummy is in pieces, non functional."

q "Cheers can be heard all around, clearly a crowd favorite, but not as many cheers as the panther got."
q "His peculiar device didn’t seem like much, but as soon as the bell ran, a laser beam shot from its mouth and the dummy just...disintegrated."
q "Students have up to ten minutes to complete the auditions, and they did it in seconds."
q "With the shock you kind of forgot to cheer...but it’s fine, they wouldn’t have heard you anyway, let’s be honest."
show horse boredside with moveinleft
q "Soon, the horse comes back among the applause and sits back next to you."
q "There isn’t much talking involved for the next hour or so, each sorcerer gets their turn and most, if not all of them look like they’re going to pass, all of them have great magical powers."
q "The headmaster seems pleased, but even more so the gracious white fox Merina, the Sorcerer’s leader together with their vice leader, Oliver."
q "Those two were jumping with joy, literally."


q "At last, the announcers call forward the first summoner."
Q "Groans can be heard throughout the arena."
d "WE PROMISE THIS SEGMENT WILL BE OVER QUICKLY, BUT IT IS VERY IMPORTANT TO OFFER OUR TALENTED COLLEAGUES THE RESPECT AND ATTENTION THEY DESERVE."
y simple"Why is everyone upset?"
show horse bored
th "The summoner's auditions can be...a bit boring, definitely less interesting than sorcerers."
y "What is the capability expectation like for first years?"
th "I probably mentioned it before, but as long as you can even show a connection to the gem you pass. A glow, a puff of smoke, a sound, anything really."
th "So it's understandable that watching dozens of students doing almost nothing is not very entertaining."
y "Why can't we all Summoner first years do our auditions at the same time? Since it's so quick but boring."
th "That is exactly how we used to do it. Everyone gets into a room and try to summon a Nightfallen."
th "The whole ordeal would be done in minutes."
th "But the Headmaster really wants to study each individual in particular, for some reason."
y bored"I think the reason is pretty clear, he needs some overtime money by doing this meaningless wate of time."
th "Heh, he might as well."
q "For the next couple of minutes, which feel like hours, you play with the little gem you picked earlier, trying to keep that faint connection you had with it."
q "The horse sees you and pets you on the head as a sign of encouragement."
q "You slouch down into the chair more and more as yet another summoner is being called into the arena."
q "Five students so far, zero Nightfallen yet seen, but that might change now, seeing who is being presented."
y simple"Hey is that-"
th "Yup."
d "NEXT UP, ALVY! ONE OF OUR BELOVED RECOMMENED STUDENTS!"
y smug"Beloved, ey?"
th "{size=*0.5}Let's see what you're on about, doggy.{/size}"
stop music fadeout 2.0
q "The arena has been quiet for a while, but with this announcement, murmurs start to stir up as a little dog emerges in the midst of all."
q "He walks confidentily, yet his eyes betray timidity."
scene arena with dissolve
show dummy with dissolve
q "He is now face to face with the same dummy snake his peers had to face."
q "Clean, untouched, untarnished wooden snake structure. His target."
hide dummy with dissolve
show alvy with dissolve
q "Patiently waiting for the bell until..."
play sound"audio/bell.ogg"
q "The dummy moves for the first time since the auditions started, perhaps considering its opponent a real threat."
q "But it is already too late."

show alvy fight1 with dissolve
q "The dog grabs three gems of various sizes and colors from his pocket, concentrating for a moment just like all the other students before him..."
play sound "audio/tension1.mp3"
q "And then-"

play music "audio/fight.ogg" fadein 2.0
show alvy fight2 with hpunch
q "Three large, feral creatures spawn around him."
q "He orders the feline and canine to attack the raging dummy, while the third...thing protects him from any incoming attacks, which mostly consist of cannonballs."
y surprised"Wow, three for the price of one."
th "Is that it?"
q "Your partner seems disappointed, almost angry at the display, clutching the armrests of his seat with his nai- claws, sharp claws that you only now notice for the first time."
"I-is he expecting something more than that? Is he expecting something more than that FROM ME?!"
"Be reasonable man!"
q "Anxiety returns again to haunt you, but you keep your attention to the summoner in the arena."
q "The two attacking Nightfallen are quick, and attack the dummy viciously."

y simple"What kind of Nightfallen even are those?"
th "The feral type."
y pf"Oh. Duh."
y "Uhm, where do they fall on the Nightfallen chart again?"
th "Just bellow the Wildfurs, they have some inteligence but not enough to be considered smart, nor do they posses enough people-like qualities to advance."
y simple"I'm surprised I haven't seen many of those."
th "They're usually treated like wild animals more so than Nightfallen, since their gems are less valuable than a mimic's, but they're great for summoning..."
q "While that exposition and lore dropping takes place, the fight- or more like the show- is over."
q "The dummy is no more, only scraps of metal from it's armor remains in the sand, and the three Nightfallen already disappearing into smoke."
stop music fadeout 2.0
scene arena
show alvy
with dissolve
ch "Sure, just violate my baby I worked so far on just like all those sorcerers, who cares?"
q "The dog looks around for a moment, waiting for a response from the silent crowd when-"
play sound "audio/cheering.ogg"
q "The whole arena errupts in cheers."
q "Cheers louder than any sorcerer got so far, most likely because everyone was so bored until this point, and you join in as well."
y laugh"YEAAAAAHHHH! GOOOD JOOOOOOOB! THAT'S MY MATE! MY SHARD MATE THAT IS! NOT MY ACTUAL MATE! WE DON'T KNOW EACH OTHER LIKE THAT-"
th "I think you should stop."
y pf"Yeah I should..."
play music "audio/happy20.ogg" fadein 2.0
scene arena2 with dissolve
y smug"But come on, admit it, that was impressive."
th "I saw better displays."
y "Right...Luis did say you summoned a demon at your auditions."
th "Guilty as charged, but I've seen other talented people as well."


d "THAT WAS AN INCREDIBLE DISPLAY OF POWER FROM A FIRST YEAR! LET’S SEE SOMEONE TOP THAT!"

y smug"That probably won't be me."

ch "NEXT IN LINE IS: [NAME]!"

y smug"Fuck my life."

th "Your turn, good luck, make your vice leader proud."
stop music fadeout 2.0
y awkward"I will certainly try."
scene codysummons1 with llongdissolve
play sound "audio/fight.ogg" fadein 2.0
q "You step inside the arena with more anxiety than you’ve ever felt in your life, borderline panic attack, but as you trace your finger along the gem’s ridges, it calms you down a notch."

y sadsmile"Please little Nightfallen, I don’t know what you are, who you are or how you are, but please come out and show yourself."
y "No need to fight, no need to work, just be pretty, I believe in you, and myself."

q "With those last words something peculiar seemed to happen, the gem glowed bright blue only for a moment and a cold shiver coursed through you."
q "Then…"
play sound "audio/bell.ogg"
q "The bell rings."


y "The moment of truth."
q "The arena is quiet, everyone waiting with held breath for you to do something similar to the other recommended student and…"
play sound "audio/raye.ogg" fadein 1.0 volume 0.8
scene codysummons2 with llongdissolve
scene CGt4
q "The gem glows brightly, light blue smoke making the appearance of a small, floating creature, a child of light."
q "It might not be the coolest Nightfallen ever seen, and it will certainly not demolish a dummy with its powers, but it is undoubtedly cute."
q "The crowd seems to agree, as sounds of {i}‘awww’{/i} can be heard all around."
q "From up close it is almost blinding, but beautiful, the way it floats there, eyes closed and eepy."
q "After getting over your own shock oand awe, you reabsorb the creature into the gem, then with a final bow signal the end of your audition."
stop sound fadeout 2.0
q "A quick, effective and entertaining display."
play sound "audio/cheering.ogg" volume 0.5 fadein 1.0
q "The people in the arena might not be as loud as the ones applauding for the dog before you, but they were still not shy to show their excitement for your talents, as simple as they were."
stop sound
q "Seems like it was a success after all."
scene arena2 with dissolve
play music "audio/happy20.ogg" fadein 2.0
q "You go back to your seat, almost skipping along with happiness."
show horse ec with moveinright
y laugh"I did it!"
th "I knew you could do it!"

y smug"Did you really think?"
show horse sadsmile
th "Well I’d lie if I said I didn’t have my doubts, but it worked out in the end, some faith was still there."
show horse bored
th "Unfortunately the rest of the auditions will most likely not be as exciting as yours or... the dog's."

y ec"Then let’s get out of here!"

th "I wish, but I’m the vice leader, I have to pay close attention to each audition and grade them afterwards."
th "Especially since we don’t have a leader present yet."

y sadsmile"Aww...in that case I’ll-"
show horse sadsmile

th "You really don’t have to stay too, [name], I won’t be able to talk much while concentrating here and I’m afraid you’ll just get the same mind numbing boredom I’ll get for no reason."
th "Go have some fun and we’ll meet each other after."

y "Alright...if you think that’s best."
y "See you in a bit."

q "He nods while smiling and you part ways."
hide horse sadsmile with dissolve
y bored"I want a snack."
stop music fadeout 2.0
y s"I heard there is a snack baaaaar- this way!"
scene lobby with dissolve
show snacktable with dissolve
play music "audio/catjazz.ogg" fadein 2.0

y ec"Bingo!"
y "Nice! They have the tea he likes, last two cups as well, Therium will-"
y simple"Uhmm, maybe he’ll have to waaait?"
show cat20simple at right with moveinright
show tiger20simple at left with moveinleft
q "You come face to face with two figures, hastily taking as many snacks and filling a bag with them, mostly cookies and other pastries, but their paws also graze the cups."

q "The tiger and cat, partners in crime, all three of you freeze in place, watching each other with wide eyes, nobody else in the room."

y simple"Hey..Aiden, Tate."
a "Hi."
t "Hey again."
y "Lovely day we’re having."
show cat20pf at right
t "We need these foooor….secrets."
Y "I didn’t even ask about those yet."
T "Good, because they’re for us, just for us, two gluttons."
y "Ok?"
t "Don’t tell Dallan please."
y "Why? I thought those are just for you."
q "The tiger intervenes."
show tiger20sweat at left

A "Hey, we heard there was some kind of...Nightfallen attack drill in town?"
a "People said it was fun to watch, but I’ve never heard of a drill like that before."
show cat20simple at right
t "Didn’t they say it was like a show?"
show tiger20bored at left
a "All they said is that a snow leopard and a horse were the ones that reassured them."
t "Hmmmm, what do you have to say, [name]?"

y pf"Oh, that...uhmm."

"Shoot, what do I say?"
"I know the truth, it was not a drill at all, but Therium doesn’t want anyone to panic, and I’m not sure if these two are part of the people who shouldn’t know."

menu:
    "Therium did it as a test for me.":
        y ec"I was hanging out with Therium and he wanted to test me to see if I'd be able to pass the auditions."
        y "You know, make sure a recommended student has what it takes, or something."
        a "Did it have to be in a crowded area?"
        y awkward"He said it would make it more realistic, you know how he is, weird like that."
        y "Him and his ways."
        t "He is really weird."
        a "Wouldn't put it past him, actually."


        jump notguilty
    "We were suddenly attacked!":
        y worried"It wasn't our fault!"
        y "We were attacked!"
        a "By a Nightfallen inside the barrier?!"
        y sadsmile"Oh no no, it was just a really big dog, a huge dog, massive, people thought it's a Nightfallen but it was just a big ball of fluff."
        y "Big guy just wanted to have his ball thrown but everyone started running away."
        t "Who has a big dog like that around?"
        a "Might be mister Shazu, he can't even keep his shop open for more than a couple of hours because he can't stay away from his dogs for long."
        t "True, it would make sense that one of his dogs got out and went to the market looking for him."

        jump notguilty
    "About those snacks…":
        y bored"We did what we had to do, hunter business, students business, but the real question is, what are you two doing stealing all the snacks?"
        t "S-stealing? No no, these are for everyone."
        a "That's right!"
        a "You're the one acting suspicious and evasive."
        y "I don't know what to tell you, nothing happened, especially nothing that would need to be reported, to someone like Dallan, for example, certainly not."
        t "We are not going to Dallan with these snacks, if that reassures you."
        y simple"It does..."
        t "And we were never here."
        y "I was extra hungry and ate too many snacks."
        a "Exactly, and we didn't hear anything about any incident or who was involved in it, right Tate?"
        t "Oh I ain't seen nothing, matter of fact: I'm blind in my left eye, and forty three percent blind in my right eye, I don't see much of nothing, matter of fact, I don't even see you, miss."
        a "Fucking dumbass..."
        jump notguilty



label notguilty:
y simple"Alright...so, I’m gonna go now, and not ask anymore things about what you’re up to and doing with those."
t "Sounds good to me."
y "And you’ll keep quiet about what you just asked me as well…"
a "Never even heard a thing."
y bored"And leave the last two boba drinks."

t "B-but-"
a "It's not worth it, just leave them."
stop music fadeout 2.0
y smug"Great, thanks, so…"
y "Bye now."
scene black with llongdissolve
scene arena2 with llongdissolve
play music "audio/happy20.ogg" fadein 2.0
show horse boredside with dissolve

y ec"Heeey, got you a drink, last two cups, had to bargain for them too."
show horse simple
q "You hand him one of the drinks and he seems...stunned."
Th "Oh...thanks."
q "He accepts it a bit reluctantly but gratefully."
th "You remembered I like these."
y ec"Of course!"
th "What did you 'bargain' for them?"
y "Oh...just some, secrets."

th "I saw you talk with Aiden and Tate."
th "Did they ask about the incident?"
y awkward"You did? I thought you couldn’t take your eyes off the arena."
show horse smug
th "Who said I did?"
y pf"That’s a creepy response, do I want to ask more? Probably not."
y s"Anyway, yeah, I did, but they had their own dirty secrets to hide, so I got away."
th "Heh, good, you’re a cunning one, aren’t you?"


y smug"I try my best."

y s"How are the others doing?"
show horse bored

th "All of them seem to pass so far, except for one guy that doesn’t have any magic, I’m not really sure why he decided to try to enter into the Shard with magic at its core but who am I to judge, beside the...vice leader."

y "Maybe it’s a dream of his to be in this Shard."

th "Who knows what the common folk think."

q "You sit back and watch more students audition as you suck the sweet pearls from the cup one by one."
q "The horse did not lie, this truly is a boring experience, most participants would go inside the arena to do...nothing."
q "Or almost nothing, except puffing out some smoke from their gems."

y simple"Oh, I almost forgot, I should go give the gem back."
show horse smug
stop music fadeout 2.0
th "Hurry, it seems we’re near the end of the auditions, at last."
scene underarena with dissolve
play music "audio/catjazz.ogg" fadein 2.0
q "You walk down the stairs and then more stairs into the summoner's gem burrowing cellar."
show table zorder 2 with dissolve
show luis zorder 1 with moveinleft
q "The man behind the counter is already waiting for you."

lu "Hey [name], you remembered to bring it back, how did it go?"
y ec"Amazing actually! I managed to summon whatever Nightfallen was inside this."
lu "Nice! So you really are worthy of being recommended, maybe I should’ve given you a more advanced gem."
y pf"That would not have been preferable, no…"
show luis smug zorder 1
lu "Heh, I’m just kidding, is Therium not going to grace me with his presence?"
y s"He’s still busy with watching the auditions, doubt he’ll come here just for a chat."
lu "Yeah, he does not like talking for the sake of talking, I’ll tell you that much."
lu "Anyway, good luck on your summoning journey, hopefully soon you won’t need to borrow a gem from me."
stop music fadeout 2.0
y ec"I hope so too, thanks again!"
scene arena2 with llongdissolve
play music "audio/outside.ogg" fadein 2.0
q "You wave goodbye and run back up to the horse’s place."
q "As soon as you got between the crowd, you could feel the sigh of relief all around making the air itself warmer."
show horse bored with dissolve


y bored"Thank God it’s over."
th "Yeah, definitely thank him."
th "I think I'll send my scores a bit later, for now..."

show horse
th "Lunch?"

Th "We have an appointment in an hour, just enough to grab a bite, maybe on the way there even."

Y surprised"Appointment?"
Y s"What do you have in mind this time?"
show horse smug
th "Well, spending time with you made me realize you’re always a little tense."
th "Like having a critter on your shoulder that pushes you down."

y bored"You can say that."
un "You’re thinking of me, and if that thought doesn’t disappear soon I’ll snap your neurons in half."

y smug"And let me guess, your treat again?"

th "I would never let my prince pay for things he wholeheartedly deserves."

y s"Do I deserve five werewolf shards?"
show horse smug2
stop music fadeout 2.0
th "Don’t push it."

y smug"Worth a shot."
play music "audio/forgetmenot.ogg" fadein 2.0
scene chibitherium2 with llongdissolve


q "You and the horse make your way through the town's bustling streets, heading towards this spa he talks about so nicely about. "
q"The town, alive with the chatter of locals and the gentle clatter of daily life, after all, it is the afternoon, the middle of the week and a big event is taking place in the middle of town, of course the streets are as busy as they can be."
q "On the way you also grabbed a couple of street food items, mostly meat filled pastries with some kind of sweet and sour sauce."

th "You’ll love it, it’s going to make wonders for these stiff shoulders of yours."
y pf"Are they that stiff?"
th "And maybe they’ll get to relax your jaw and eyebrows."
y "Are my face muscles looking tense?"
th "The more I look the more problems I see."
q "He circles you with a confused expression, poking and grabbing your fur from every angle, but you stop him when he raises your tail."
y worried"Ok! I get it! I am super stressed, but can you blame me?"
th "Absolutely not, you have all the reasons to be stressed, but this place should solve everything."
th "It’s a very popular spot for students specifically."
y s"Do they offer discounts?"
th "No… but it’s the only spa in town and students are the most in need of this kind of stuff."
y pf"Just what happens at this academy?"
th "You’ll see when you start your classes, wouldn’t want to ruin the surprise."
q"The buildings and crowd grow more scarce, gradually giving way to a more serene atmosphere as you approach your destination."
q "The spa itself is nestled at the end of a quaint street, its front yard a beautifully manicured garden."
q "Lavender and jasmine perfume the air, blending with the faint sound of a bamboo water fountain, creating an immediate sense of tranquility."
stop music fadeout 2.0
scene black with dissolve
play sound "audio/doorslide.mp3"
th "After you."
q "He slides the thin door open for you."
play music "audio/oddish00.ogg" fadein 2.0
scene spa with dissolve
q "As you step into the spa's waiting room, you're greeted by an ambiance of understated elegance."
q "The room is spacious and bathed in natural light, with large windows offering a view of the garden."
q "Comfortable chairs are arranged thoughtfully around low tables adorned with fresh flowers, house plants, and wellness magazines. The decor is a harmonious blend of modern chic and traditional comfort, creating a welcoming space that promises relaxation and peace."
q "The horse, standing calmly by your side, breathes in the new air, his eyes reflecting a quiet contentment beneath the smile."
q "When you look down, you see his shoes placed at the side of the door, you wonder how he did that so fast while struggling to take yours off."
show massie at left with moveinleft
q "In the meantime, while you’re awkwardly bent down, a lioness appears to greet you."
q "Her demeanor and tone is calm and collected, as if she’s been expecting you."
st "Good afternoon, Mister {i}Bellamy{/i}, [name2]."
"Huh, so he's from {i}that{/i} country."
th "Just in time I presume."
st "On time indeed."
q "She chuckles."
st "This is the new face you were talking about."
y "That's me, hi, I'm [name]."
mas "You can call me Maicy."
mas "Speaking of new faces-"
mas "Before I show you to your spots, let me introduce you to Sam."
show sam at right with moveinright
q "A tall calico cat enters the room holding a box of supplies, creams and towels can be seen poking through the top, he gives a curt nod and a forced smile."
mas "He is our newest employee and will accompany me to your session."
mas "I hope that won’t be a problem, both me and the owner can vouch for his skill and everything will be done under my eyes and guidance."
th "No complaints here."
q "In fact, you secretly hope he’ll be the one to take care of you, but the thoughts are not very specific, so I’m not sure why…"
un "Who are we kidding here? We all know why."
mas "Great, in that case-"
y ec"I volunteer!"
q "You might’ve said that too loud and too fast, all three people are now looking at you in silence."
y awkward"Uhmm...he looks strong? For my nodes?…"
un "Smooth."
mas"I was going to ask if you would, at the end, be willing to provide some feedback on his performance?"
mas "But I suppose that answers my next question as well."
mas "Sam, let’s go."
hide massie with moveoutright
hide sam with moveoutright
mas "Follow us please."
scene massage with llongdissolve:
    blur 20


q "The next room you’re guided to is similar to the waiting room, in that it’s very well illuminated by the sun, with plants in every corner, the only exception being that it’s much bigger, and instead of chairs stand the massage tables."
q "A single divider parts the place in two semi-private confinements."

mas "Please undress to your comfort level."
q "They both leave the room for a minute, most likely to give you privacy to undress."
q "The horse sits on the other side of the divider and takes off all his clothes, including his underwear."
q "That is definitely not on your {i}‘comfort level’{/i}, but you don’t want to be the odd one out, so you follow his example."
y nakedss"W-what now?"
th "Just cover yourself with the towel, plant your face in the cushion and relax."
th "They’ll adjust the towel if needed, don’t worry about it."

y nakedsimple"O-ok...why naked though? How far down does the massage...go?"
th "Curious, are you shy being naked?"
y nakedawkward"It’s just my first time, in a place like this, that is, I don’t know the norms."
th "I’m teasing, I’d have to be deaf, dumb and blind to not figure you’re the awkward type, and I think that’s very cute."
y nakedbored"A straight observation, flirting attempt, or insult, I will never know with you."
th "Everything I’ll ever say about you is either constructive criticism or flirting."
y nakedawkward"N-noted."
th "One more thing I should mention about our time here is that they will not hear a thing when they come back, they’ll have earplugs."
y nakedsimple"Our masseurs? Why?"
th "So we can talk in private of course, it’s the norm."
y nakedsmug"Feels like a plot device for our otherwise awkward silence."
th "Can’t be a plot device if we’re aware of it."

y "Can’t argue with that logic."
y naked"And another thing, what kind of massage are we even getting?"
th "A general relaxation bundle, nothing too crazy."
scene massage with dissolve
scene CGt5
q "The workers come back after a little while interrupting your chat."
q "The cat, Sam, stands at your side, sprays his paws and your back with some kind of warm, fragrant oil and gets straight to work."
q "His gentle paws go through your fur, guiding the oils down to your skin."
q "After that he switches to a comb for the thicker parts of your fur, mostly the neck and the base of your tail."
sam "Let me know when I’m being too rough."
y naked"It’s great so far, no worries."
th "He can’t hear you, [name]."
y nakedsimple"Oh, sorry, Sam."
th "He still can’t hear you."
y nakedpf"fuck…"
y "How do I let him know if he’s being too rough then?"
th "Just signal with your hand."
y "Oh right, the second most popular form of communication, gestures, of course."

q "As the massage progresses, you can feel the stress melting away, replaced by a deep sense of calm and wellbeing."
q "The horse lets out a groan from time to time, making you raise your head to look, but nothing outside of the tip of his head is really visible, unless you count the slightly translucent divider as ‘visible’."
q "Nothing the cat does so far is provoking you to make a sound, except maybe a sigh of boredom."
q "Perhaps he’s afraid of not hurting you, seeing how skinny and fragile you are."
"Omg, so you think I’m skiiiiinny!"
un "Keep it in your pants, that was not a compliment."
"I don’t have pants."
un "Touche."
q "Nevertheless, the pressure applied by the fingers of a gentle man going through your fur makes you more relaxed than you’ve ever been."

th "Aughh, God."
q "Another satisfied groan from the horse."
y nakedsmug"How you holding up, Therium?"
th "Don’t mind me, I have a few nasty bruises and sore muscles from training, but it will all feel better after this, I’m sure."
q "Maybe you judged Sam too hastily, a valuable lesson learned."
y "Need a distraction?"
th "If you could provide one that would be lov- Agh! {i}*sigh*{/i}-ly"
Y nakedpf"Umm, they can’t hear...anything we’re saying, right? Just triple checking."
th "Nothing we say or do, nothing at all, I promise."
th "Otherwise they’d hear my pain."
y nakedsmug"Ha."
y "Then let’s discuss."
y "What better distraction than uncomfortably personal questions you can’t escape from?"
th "Oh God, I’m going to regret this, aren’t I?"
y "Perhaps."
th "What do you want to know?"
th "More about gems?"
th "How to be a great summoner?"
th "Actually you said ‘personal’."
th "Perhaps how to become a vice leader?"

y nakedss"Actually, I just want to know more about you, as a person, outside of the academy, that is."

th "About...my abilities?"

y "No...not professional abilities."
y "Just you."
y "Where are you from?"
y "What’s your favorite food?"
y "What do you do when you aren’t the {i}‘Summoner’s vice leader’{/i}?"
q "Whatever sounds he was making before stop completely, for the next thirty seconds - there is only silence."
un "You sure gave him a lot to think about, one’s favorite food can’t be said without proper thought."

th "I am…"
th "Not a local."
y "I could figure that one out by your name and accent."
y "But I can’t put my finger on where from exactly."
th "There are...a lot of things I can’t talk about."

y "Eh, can’t blame you, I was told you’re a mysterious one, there had to be a reason."


y naked"In that case, how about you ask me anything?"

th "What?"

y "I’m a completely open book."
y "My life is somewhat boring and I have basically no secrets, I can start answering first."
y "No pressure on you alone, I just feel like you’re more...interesting than me."

th "Alright, if you insist."

th "What are your life’s ambitions?"

y nakedsmug"Ah yes, I forgot mister philosophy likes these kinds of questions."
th "Is it not a good one?"
y naked"It’s a perfect one, I just need to think for a second."


menu:
    y nakedsimple"My life's ambitions..."
    "To be a successful hunter.":
        th "Recommended student at one of the most prestigious hunter's academies in the world? Wouldn't have guessed."
        y nakedss"It's not too creative, but it is something our society values a lot."
        y "I like being recognized in a positive light, and the job itself pays well and is, dare I say, fun."
        th "There's nothing wrong with simple ambitions, just make sure not to lose yourself in your carreer."
        th "Your personal life means a lot as well."
        jump secondquestion
    "To own up to my responsabilites and duties.":
        th "What kind of duties?"
        y naked "All of life's duties."
        y "Be a good student, friend, boyfriend, husband."
        y naked"Fulfill any promises I make, stuff like that."
        th "Your companions will be lucky to have you around then."
        th "Does your idea of responsibility extend to civic duty?"
        th "Would you ever sacrifice your time, or well being for the greater good?"
        y nakedsimple"Umm, probably, I did do a lot of volunteering back in middle school and high school, most of it was forced though so I'm not even sure it counts."
        th "I suppose that's good enough."
        jump secondquestion
    "To live peacefully.":
        y naked"I truly believe if there is peace then all other problems become simple chores."
        th "What about sickness? Or debt? Or the love of your life refusing you?"
        y "Those are all bad, but I still believe in peace above all else."
        th "That is very brave of you, that you can push away personal problems for the sake of peace."
        y nakedss"I wouldn't pat myself on the back just yet, I'm still choosing it for greedy, personal reasons."
        y "I just want to live unbothered by war, or politics, or society."
        th "I see, that explains some things."
        jump secondquestion


label secondquestion:
th "I have a second question."
y nakedsmug"Bring it on."


menu:
    th "Who do you love most?"

    "My mom.":
        y naked"It has to be my mother."
        y "I doubt I can respond with any other person ever."
        y "She worked her butt off as a single mother with two kids."
        y "I love and respect her."
        th "Parents, always first to come to mind."
        th "I had a feeling your father figure wasn't present but this just confirms it."
        y nakedpf"Do I give off {i}'daddy issues'{/i} vibes?"
        th "No comment."
        jump massagesex


    "My sister.":
        y naked"This response surprises me, to be honest, but it it's probably my sister."
        y "She can be a pain, but I really can't imagine living without her."
        th "Sibling rivalry is a classic, but if you truly believe your words, then I bet you two will have a flourishing relationship."
        y "Eh, maybe when I'm done with my studies."
        jump massagesex
    "My friends.":
        y naked"I love my friends more than anything."
        y "Well, my future friends at least."
        th "A person that values friendship with no friends?"
        y "I know, it's sad but I've been jumping schools too much for friends."
        th "That's okay, there are many who already have their eyes on you on that regard."
        jump massagesex

    "Myself.":
        y naked"I love myself, of course!"
        y naked"The most reliable person that I could never bring myself to hate."
        th "Not surprised, I almost picked the same answer."
        y nakedpf"Me or yourself?"
        jump massagesex
    "You.":
        y nakedsmug"I love the person that took precious time out of his busy schedule to help me out and show me around, and the person who's paying for my massage."
        th "Aww, how sweet."
        th "I almost wish you weren't joking."

        "If only you knew how close I am to not be joking..."




if theriumhome>=1:
    Th "And I’ll do one more."
    y nakedsmug"Shoot your best shot."

    th "Is there some kind of...belief or value you hold, that has shaped your life until now?"
    y nakedsimple"Hmm, that sounds like something my therapist would ask."
    y "A belief or a value…"
    y naked"I’m still very young, but I've always held the belief that love and deep, meaningful relationships are the most important aspects of life."
    th "Love, huh?"
    th "Is love not going to be an obstacle at the school of lust?"
    y nakedss"That’s the second part, I don’t feel guilty about doing anything uhmm, sexual when there are no romantic feelings involved, in other words, doing my job."
    y "Is that not something everyone here thinks too? Or at least should think."
    th "It is, for most, but it’s worth checking if the new ones have the same opinion."

    jump massagesex



else:
    jump massagesex
label massagesex:

th "This doesn’t feel fair, I’m asking very personal questions, I’m finding out so much about you as a divinator… and you don’t care if I refuse to tell you anything?"
y naked"I can’t force you to open up if you don’t want to."
y "I’ll forgive this transgression if you answer just one simple question."
th "I’ll try…"
y "What is your favorite animal?"
th "..."
th "…heh"
q "He chuckles quietly for a solid ten seconds."
th "Butterflies."
q "With that final answer your personal discussion is done, silence occupies the room, you managed to distract him from the pain, and he distracted you from the boredom."
q "As the cat’s hands glide down your spine, you feel a wave of relaxation wash over you. His movements are rhythmic and soothing, almost like a dance across your back."
q "He occasionally uses his elbows for deeper pressure, expertly finding those spots that need extra attention, the fun has finally begun."

q "And a special kind of fun begins when he moves to your lower back."
"What’s that supposed to mean?"
un "Don’t worry about it."
q "Sam applies a gentle but firm pressure that soothes the aches you didn't even realize were there. The soothing ambiance of the room, combined with the rhythmic movements of the massage, lulls you into a state of peaceful relaxation, his warm palms sending shivers down your spine."
q "He moves the towel from under your tail even lower, starting to massage the base of your tail and lower, as well as your upper thighs, rubbing them through the towel with circular motions."
show lust with dissolve
play sound "audio/heart.mp3" loop
"Oh no."

q "Your previously calm, empty mind suddenly fills up with all kinds of thoughts that I won’t be mentioning as it would corrupt this humble and innocent narrator."
"Fuck fuck fuck."
q "That’s definitely a part of those thoughts, yes."
"Now?!"
q "A rush of lust takes over, and you thank the Gods you’re turned on your stomach."
q "The few sounds that were escaping your mouth when the cat applied pressure now turn into moans, making him slow down and the horse to ask:"
th "Is everything alright?"
y nakedhurt2"Yup, yes, aha, perfectly fiiiiine, you know, the fun begins, haha, I mean, he’s getting rougher, you know? With his hands, on my back, just my back, above my tail, from the outside."
th "They are known for mind numbing massages, it happens when they go harder, try to endure it."
y nakedlust"I’m certainly trying."
un "Will you though?"
"I don’t know! I’m waiting for the choice screen to appear!"
un "Of course, here you go:"


menu:
    q "What will you do?"
    "Lure Sam in.":
        label massagesex20:
        $ persistent.unlocked_massagesex20 = True
        $ samsex +=1
        $ yessex +=1
        scene massage with dissolve:
            blur 15
        stop music fadeout 1.0
        stop sound fadeout 2.0
        q "You decide that this lust prison’s agony is too much"
        play music "audio/dream.ogg" fadein 2.0
        q "But the challenge of implying something lewd and testing the waters without a single word spoken is proving a big challenge."
        q "You use your previously static tail to brush the cat’s legs while swinging it in a somewhat seductive way."
        q "You turn your face towards him and smile, giving him a thumbs up."
        q "Congratulations, you surprised him and made him blush."
        q "Next step is, of course, as our master seductor figured, arching your back while keeping those bedroom eyes on the cat, because nothing says ‘fuck me’ more than Lordosis."
        un "And of course you’re a huge bottom...great."
        q "This plan also allows you to pretend like you’re simply stretching, nobody’s gonna buy that but hey, it’s an excuse nonetheless."
        sam "Umm."
        q "Seeing that the cat is a bit confused, but not weirded out by your action, you give him a final wink."
        q "Bingo! The fish bites."
        q "He touches your towel, this time, on the part where your butt cheek is, squeezing and rubbing, pretending like he’s still giving you a massage with a blush on his face."
        q "Having confirmed this intern’s feelings you decide it’s time for la piece de resistance!"
        show massage2 with moveinleft
        q "You grab the towel and with one swift movement throw it down, leaving your whole body naked, and more importantly, your entrance opened and inviting."
        show massage3 with moveinright
        q "Although he knew it was coming, he's still looking around over his shoulder uncertain, trying not to make eye contact while he thinks it over."

        q "At last, the cat decides that what he sees in front of him is worth risking everything for."
        q "And I have to admit, the cake is definitely something to be proud of."
        "Rare compliment from Scribbles."
        un "It was the narrator, not me, get it right."
        q "He walks over to the supply table and grabs a bottle of lotio- oh, nope, that is straight up lube, high quality, fresh bottle of anal lube."
        q "He had that on hand."




        q "After that it doesn’t take long for his clothes to be thrown away in haste as he begins to mount you."
        q "Sam positions himself, still looking wary around, while you beckon him to put it inside."
        q "This desire and lust is killing you, especially when its antidote is being lubed up as we speak."
        q "He puts some on his fingers as well, trying to massage your entrance, but your impatient ass, literally, doesn’t care about foreplay."
        q "Something you tell him by wiggling your butt back and forth and giving him a frowned look, a message which he receives successfully."
        scene massage4 with llongdissolve
        q "The cat positions himself at your entrance, and slowly begins to push."
        q "His cock begins to disappear, inch by inch, until the base hits your cheeks with a light slap, and you feel his balls caress yours."
        q "Surprisingly, the feeling of being stretched out and filled does not hurt...at all, in fact, it makes the lust rush bearable and your face and body finally relaxes."
        q "Can’t say the same thing about Sam."
        q "Feeling the warmth of your insides hugging his length, his face loses composure and his mind seems to go blank, or perhaps feral is the better word."
        q "The cat's movements became more urgent, his thrusts deep and powerful as he drove himself to new heights of pleasure."
        y nakedhurt2"Didn’t get that in a while, huh?"
        th "What was that?"
        y nakedawkward"AAHHMM, I-I-You must’ve been so busy with work and stuff, bet you haven’t been here in a while, huh?"
        un "Saved."
        th "Funny story, actually-"
        q "The horse’s words get drowned in your head, as the cat’s dick just becomes faster and harder, sliding in and out with difficulty."
        q "Your ass becoming a mess of lube and precum as this seemingly shy, inexperienced intern dominates you, looming over you and keeping your thighs pressed against the table."
        q "As the extra lust fades away, his rough movements start to get a hold of you, light moans escaping your lips and your body twitches when the occasional long and deep thrusts come into play."
        sam "You’re so...tight...aghh."
        th "And that’s why the owner and me- huh, tight?"
        y "Yup! I have these tight spots that need fixing, haha."
        th "A student without tight spots is unheard off, but what’s with the wet slapping?"
        q "The cat has indeed turned your ass into a party, leaving you an absolute mess just trying desperately to handle the hurricane of feelings attacking your body. It was beyond description, so unceasingly intense yet so amazing. Your cock had never felt this hard, and it was making a clear mess on its own between your legs."
        y "I-it must be some new technique, he’s new after all."
        th "Ah, of course, all these new people with their new ways, I should thank you for volunteering to take him, by the way, does his technique work?"
        y "No complaints so far, it’s pleasurable, though hurts a little."
        th "No pain no gain."
        un "And the gain is a litter of cum inside you."
        "I hope so…"
        q "Five minutes later and the cat was still pounding you relentlessly. At this point, you’re enjoying the sex for what it is, no more cheating with lust, the feeling of being full of another man’s meat, of having someone pleasure themselves with your body and having that sweet spot be your saving grace in this submissive behavior of yours."
        un eyeroll"Disgusting bottom."
        "Getting bred feels awesome..."
        q "Your body shudders with pleasure, the kind of pleasure you haven’t felt in months, maybe years or maybe...ever."
        q "You feel Sam’s cock twitch inside you, without a hint of stopping any time soon."
        show massage5 with dissolve
        q "Warm liquid suddenly fills you up, shooting deep inside and spilling out as the cat keeps breeding your messy hole."
        q "At the same time, the table underneath gets covered in your fresh, thick, white seed."
        q "The cat slows down as you both try to keep any kind of moans and other verbal sounds at a minimum."
        q "He pulls his softening member out, not before keeping it warm inside you for another minute."
        q "For me, it was an experience, for you, it was a great one, and for Sam it seems like it was the time of his life, having to tap him on his arms multiple times to get him out of the trance."
        scene massage4 with llongdissolve:
            blur 15
        sam "S-sorry- I’ll get a towel...or two, actually, I’ll just bring the whole basket."
        y nakedsmug"That would be great, thanks."
        if from_gallery:
            # Reset the flag so it doesn't affect the normal gameplay flow
            $ from_gallery = False
            jump return_to_gallery
        else:
            pass
        th "Oh, are you two done, [name]?"
        y naked"Y-yeah, I mean, almost, just gotta take all these oils off of my fur."
        th "You leopards and your long fur, couldn’t be me."
        y nakedsmug"It’s a tough life."
        th "I think I’d just kill myself, if I had fur like that."
        y nakedpf"That is...certainly a comment of all time."
        q "Thankfully your attention is stolen away by the cat’s rough, hurrying paws trying to clean you off with wet, warm, soapy towels."
        q "They’re doing a great job at removing that kind of stuff from your fur, or maybe it’s the desperate employee that’s doing the miracle work right now, with a frightened look on his face."
        un "Poor fella, he’s probably getting fired."
        "Not after the performance review I’m giving him, hehe."
        q "You might be a horny monster, but you’re a kindhearted horny monster, and that’s enough to pat yourself on the back."
        q "In the meantime, the horse finishes up his session as well, and of course, his {i}‘clean time’{/i} lasts less than a minute."
        q "You both get dressed, the employees take the ear plugs from their ears and the divider is removed. Your eyes are not stuck to a meaty horse doing a big stretch."
        th "That was sooo nice, thanks again darling."
        q "He kisses the lioness on the cheek, something she gladly accepts."
        mas "Glad to be of service."
        if samsex>=1:
            mas "I hope Sam offered you a pleasant time too, I noticed his silhouette doing some unusual movements."
            mas "A style I’m not too familiar with, but hey, I’m still young, I’m happy to learn new methods from anyone."

            q "Both you and the cat blush and almost begin to sweat, refusing to meet each other’s eye."
            y ec"Y-yup, had a great time, let’s go, Therium! No time to waste! Have a whole day ahead of us!"

            jump donemassage
        else:
            jump donemassage



    "Endure.":
        q "No, you decide that despite the agony in your chest and the fires of desire in your dick, it is not the time nor the place to do anything inappropriate."
        un curious"Are you sure? It would clear your mind and let you blow off some steam, it would feel good, you know?"
        "Nice try, I’m not falling for it, just call me a slut and stop joking about it."
        un sidee"I’m serious! I can feel the lust rush too, for your information...It kind of...hurts, and not in a good way."
        "Oh...well, I’m sorry, but either way, it really is not a good time."
        "We’ll both have to endure it."
        un bored"If you say so."
        un curious"Is it crazy that I want you to be an overall hornier person?"
        "Any more horny in me and there will be no soul."
        un bored"Touche."
        un pride"Back to narrating then."

        q "Because of this lust, a feeling almost impossible to ignore, the massage itself can barely be felt."
        stop sound fadeout 2.0
        q "The gentle hands of the cat sometimes press harder between your ridges, shoulder blades or rogue knots, but other than that, your mind is stuck to the thought of penis."
        q "Your session comes to a halt just moments after the lust left your mind, and with a relieved sigh you begin to get up."
        q "In the meantime, the horse finishes up his session as well, grunting satisfied."
        q "You both get dressed, the employees take the ear plugs from their ears and the divider is removed."
        q"Your eyes are not stuck to a meaty horse doing a big stretch."
        th "That was sooo nice, thanks again darling."
        q "He kisses the lioness on the cheek, something she gladly accepts."
        mas "Glad to be of service."
        mas "I hope you had a great first visit too, [name]."
        y ec"Sure did, never knew I was so stiff, expect me and my tight shoulders to be back throughout the year."

        jump donemassage




label donemassage:
play music "audio/oddish00.ogg" fadein 2.0
scene spa with dissolve
show massie at left with moveinleft
show sam at right with moveinright
mas "One more thing before you go."
mas "On a scale from one to ten, how do you rate your experience with Sam today?"
q "The cat shuffles awkwardly waiting nervously for a response, but trying his best to act uninterested."
y ec"Ten out of ten, no complaints!"
mas "I see, I’m glad he managed to satisfy you, do you happen to have time for a few more questions about your time here? We like to get in-depth feedback from newcomers."
y sadsmile"Well we-"
play sound "audio/notification.ogg"
q "A phone rings and breaks the conversation."
q "The horse looks at the screen and sighs."
th "Sorry, I have to take this, it’s important."
q "He hurries towards an empty, small room, perhaps the bathroom, and shuts the door behind him."
y s"Oh, in that case I should have time for those questions."
stop music fadeout 2.0
mas "Wonderful! Follow me."


scene black with llongdissolve
scene bathroom with dissolve
show horse phone at left2 with moveinleft
th "Yeah, what do you want?"
phone "…"
th "Hello?"
show horse mad at left2
th "God Damn it..."
play sound "audio/canyoufeel.mp3" fadein 2.0
show cloak at anim_a

nu "{i}~Caaan you feeel, the looove toniight?~{/i}" with longdissolve

stop sound fadeout 2.0

play music "audio/inventor.ogg" fadein 2.0

th "Why are you following me?"
nu "Those are just my orders, don’t take it to heart, at least not the same way you’re taking him to heart."
th "I’ll ask one more time, what do you want?"
nu "I’m just here to ask about the situation."
th "Why? You seem to know enough about us, seeing how you’re following us everywhere."
nu "I can’t read your mind, can I? Who knows what stew you’re cooking in that noggin’ of yours."
nu "Did you like that? It’s a new phrase I learned from a child, cook a thought."
nu "Isn’t the youth so creative?"
th "I haven’t even done anything worth reporting on."
nu "I think you falling madly in love is great news."
th "Pff, don’t be absurd."
nu "I know you swore it won't happen, but cheer up, we’re happy about it…I think."
th "I don’t even know him."
nu "He knows you even less, and he’s already falling for you too, ain’t that cute?"
nu "Fools falling in love."
th "I’m done here."
nu "Aren't you even going to ask about the market situation?"
th "I know it was you, why bother?"
nu "Oh, then that explains that sour look on your face."
th "No, that's just because of your overall presence, your prank is still a factor though."
th "But let me guess, 'father's orders'."
nu "Nope, I was just bored."
th "Why am I not surprised?"
nu "Father was a little upset you were the one to defeat it, still."
th "There was no other choice, he can't do anything on his own."
nu "Still, would've been fun to watch things unfold on their own."
nu "Maybe he would've showed his superior summoning abilities to save his new boyfriend~"
th "I'm done here."
show horse bored at left2
nu "Can I at least know what your next move is before you storm out in anger?"
th "Why? You'll be there, like you always are."
nu "Actually, I have some plans for this evening. Found a group of young minds to mould, it will certainly be entertaining."
nu "And if your plans include him, then I must know too, you know the rules."
th "{i}*sigh*{/i}"
th "I am just going to give him some answers."
nu "Oooooh! Big news, hopefully that doesn't include me, father, or HIM."
th "No, just...me."
th "That is, if he ends up deserving answers, I'm still not fully convinced."
nu "Huh."
nu "..."
show horse mad at left2
nu "When are you fucking him though?"
th "{size=*2}GOOD DAY!{/size}" with hpunch
hide horse mad with moveoutleft
show cloak at center with move
scene black with dissolve
stop music fadeout 2.0
nu "So sensitive this one."
nu "But he's fun, hah."

scene spa with dissolve
show sam smile with moveinright


sam "Thanks for your review, she seemed to really, really like it."
y ec"No problem, glad I could help."
y s"Oh, there’s Therium."
y "Thanks again for the service!"
sam "Come back anytime."
play music "audio/hospital.ogg" fadein 2.0
scene park2 with llongdissolve
show horse sad with dissolve
q "You walk up to the horse, his smile noticeably smaller than before, walk out and close the door behind you."
q "As soon as you leave behind the lush garden, your partner stops in place, looking at the ground."
y simple"Huh? Something wrong?"
th "About those personal questions earlier…"
y sad"I’m sorry again."
Y "I know, I’m being a bit forward, and you don’t like to overshare."
q "He ponders for a while then shakes his hand."
Th "It’s not that...I just think a place more private would be better for spilled secrets and past mistakes."

th "I’m not completely against spilling my thoughts if the right person is with me, but I have to be cautious about it."

y simple"What do you mean exactly?"
th "..."
show horse sadsmile
Th "Do you like to read, [name]?"

y ec"My second favorite activity."

th "Bring your favorite book to this place…"
play sound "audio/notification.ogg"
q "A notification with a message pings on your phone."
th "And I’ll bring mine."
th "I'll give you a special, private divination session."
th "You probably find this strange, but I assure you I have my reasons."
q "He sounds sincere, apologetically so, and you swear you saw a blush cross his face."

y simple"Alright?"
y s"Let me go grab it, then we can-"

th "Not we, only you."
th "I’ll wait for you when the sun sets."

y bored"Ok, I know you like riddles and stuff, but this feels unnecessarily poetic."
q "He doesn’t respond, just chuckles and reaches for the side of your face, caressing the soft tufts near your cheeks."
q "Something in his eyes, in the way he looks at you says just how fed up with your silliness he is, yet how much he loves it."
hide horse sadsmile with easeoutright
q "The horse lets go and turns his back towards you."
th "At sunset."
q "With the final reminder his unstoppable steps make their way further and further away, while you stand in place like a statue, a wide eyed statue."
y simple"…"
y pf"{i}Where though?{/i}"
un ang"ASK HIM NOT YOURSELF! HE’S WALKING AWAY!"
y scream"AAAHH, YOU’RE RIGHT, THERIUM WAAAAIT! WHEEEEERE SHOULD WE-"
y simple"Oh, wait, he texted me, duh."
un eyeroll"Fucking dumbasses."
y "A top the hill with the lone tree, West of the academy."
y "…"

y bored"Huh."
un curious"What?"
y simple"Now I know where, but don’t know...why?"
y "A divination session, he says."
y "Guess I just didn’t expect any of this."
un "What DID you expect?"
y "To...spend more time together I guess."
y "Or for him to WANT to spend more time with me."
y sad"I know I know, {i}‘why would he want to spend time with a loser like you’{/i}?"
un bored"That is not what I was gonna say."
un "I think you’re pretty neat, for a mortal."
y sadsmile"You do?"
un "Why not?"
un "You’re very normal, regular, plain, boring."
y bored"None of those are compliments."
un "In other words, you’re safe."
un "And your persistent horny state is definitely a benefit for a lust demon."

y s"I can get behind that."

y simple"But Therium…"
un "Who knows? He has his own demons to battle."
y s"Like you?"
un "Much worse than me."
y pf"So I’m just supposed to accept that my life is a K-drama?"
un "Over the top romance scenarios and mundane life turned into epic adventures?"
un "Sounds like something you’d love."
y smug"You know me so well already that I can’t even complain anymore."
un "Trust me, wish I didn’t..."
y simple"Now the question of the day...what do I do until the time comes?"
y "Ooh, or I could try to find Dallan, Aiden and Tate."
y "I should take advantage of the people who want to be around me."
y "Not in a bad way though…"
un "Do you ever stop yapping? You can talk while walking, you know?"
y sadsmile"S-sorry, I’m just nervous and anxious I guess."
scene chibialone with dissolve
un simple"Strange, doesn’t seem that way."
y simple"What do you mean?"

un "Your heart is not beating fast, in fact, it’s...slowing down."
un "A lot."
y "I don’t feel anything out of the ordinary."
un sidee"I think you should lay down."
un ang"Lay down, lay down NOW!"
y "Geez alright, if you say so."
y bored"Are you a service dog or something?"
q "You sit down on the pavement a block or two away from your dorm, sitting criss-crossed and watching the people walk through the street."
y "My pants are gonna be dusty now…"
stop music fadeout 2.0
show blink with dissolve
y sleepy"Eh, doesn’t matter, I-I’m going-{i}*yaaaawn*{/i}-"
y "I’ll need a shower a-anyway...after-"
scene black with llongdissolve
q "Slowly but surely, your eyes start to close against your will, your head falls limp to your side while the rest of your body follows."
st "Are you...ok?"
st "Hello?"
st "HELLOOO?!"
play music "audio/blizzard.ogg"
scene theriumdream2 with llongdissolve
scene CGt12
thug "HELLOOOO?!" with llongdissolve
thug "HEY! DID YOU HEAR WHAT I SAID YOU USELESS MAGGOT?"
thug "SCRAM!"
thug "Next time we see you in our spot you’ll lose your other eye too."
"Life just isn’t fair sometimes."
Child "Please...I just want some fo-"
thug "TOO BAD!"
thug "Should've taken care of your mommy and daddy better then."
thug "The streets aren’t for you."
thug2 "He should go live in the woods."
thug "Haha, yeah, maybe then he’d be useful as a fleshlight for those monsters."
thug2 "Or just straight up food."
Child "YOU AREN’T ANY BETTER THAN MONSTERS!"
scene black with llongdissolve
stop music fadeout 2.0
"Not everyone is treated equally by nature."

play sound "audio/beatingchild.mp3"

"Aren’t people supposed to be above survival of the fittest?"
play sound "audio/beatingchild.mp3"
"So why am I...at the bottom of the food chain?"
play sound "audio/beatingchild.mp3"
pause 0.5
play sound "audio/beatingchild.mp3"

thug "Leave him alive, we’ll find him again tomorrow, naughty kids must be taught the lesson until they learn it."
"Remind me again...who are the monsters I should be afraid of?"

"…"
un sidee"What the hell are these dreams?"

scene dormroomsunset with longdissolve
play music "audio/evening.ogg" fadein 2.0

q "Your eyes slowly open inside the familiar dorm while tears pour down your cheek."
un "Hey, you’re awake and...why are you crying?"
un "Did you have a nightmare?"

y cry2"I-"
y "I think so."
un "What about?"
y "I don’t remember."
y "But I felt like the world started to crumble for a minute."
y "Did you happen to see it?"
un "No, sorry, I was locked out of this one. All I saw was the darkness from my special corner."
y simple"How did I get here, and what happened?"
un "Now that’s something I can help with."
un "You fell asleep spontaneously after that massage and the talk you had with the horse."
un "Your heart slowed down and your eyelids became heavy, it was like a factory reset."
un "Don’t ask how I know what that term means."

y "Do you know why that would ever happen?"
un "Maybe, you were much more exhausted than you thought, although I doubt that’s it since I was feeling absolutely fine too."
un "Doubt there was any poison or magic involved, since again, didn’t sense any."
un "So my only explanation is that it must have something to do with our growing bond."
y bored"Even more side effects? You said lust rushes would be the only ones!"
un "I didn’t know of all the extra stuff either!"
y "Do you at least know how we got back to my dorm?"

un "Didn’t get to see anyone too clearly, it was a small figure with a shaky voice, that’s all I remember."
y simple"It doesn’t seem like they wanted to stick around, unless-"
y pf"Hmm."
q "You take a long look around the room through squinted eyes."
un "What are you looking for?"
y "Maybe they’re here...just invisible...or they are veeeery small."
un "Or maybe they left a note and left, dumbass."
y s"Nah, there is no way they- oh, there is a note indeed."

q "The note is folded neatly underneath a glass of water on the table."
q "You now realize how dehydrated you are and thank the stranger silently while raising the glass and unfolding the paper."

show alvynote with moveinright
q "It reads:"

q"{i}Hey, you passed out on the street and I took the liberty of bringing you back to your dorm, it wasn’t too far away and your key with your room number was in your backpack, I hope that’s not a problem.{/i}"
y ec"Why would it ever be a problem? Thank you kind stranger!"
q"{i}Make sure to drink water, have a snack and sleep, and maybe visit a doctor.{/i}"
q"{i}P.S I swear I didn’t see the massive toy at the bottom of your bag, and if you think I did, I certainly didn’t touch it, I promise.{/i}"
y pf"God FUCKING damn it!"
un "You keep a dildo in your backpack at all times?"
y worried"For...emergencies."
un "Slut."
y angry"Don’t judge me! I’m a victim!"
un "Who is that even from?"


y simple"let’s see, uhmm, on the back maybe?"
hide alvynote with moveoutright
show alvynote2 with moveinright
y "Yup…"
y "Alphonse?"

y pf"Well, thank you again Alphonse, just pray I don’t find a memory erasing machine anytime in the near future."

un "Hey...look outside."
hide alvynote2 with moveoutright
y simple"Hmm? What about it?"
y s"It’s beautiful."
un "It’s getting red."
y bored"Yeah, that’s what happens at-"
y simple"Sunset…"
y worried"SUNSET! THERIUM!"
y "Shit shit shit!"
y "Uhmm, what was it? A book, I need a book."
y "Aghh, but I didn’t think about it enough, am I going to be late?"
un "Maybe you can find a book underneath all of your sex toys."
y angry"Zip it."
q "You spend the next two minutes frantically searching through your backpack, luggage and even the internet, turning the room into a cartoon fight scene."
q "No idea where you even found a stepping ladder to throw around, or who’s grandma that is."
q "In the end, you found a couple of worthy choices, which you lay down on the table."
show books with moveinright
y worried"I don’t even know what the task is, he just wanted to see my favorite book."
y "What does a book have to do with divination anyway?"
y "Maybe it’s for a book club? Maybe he’s simply curious and it doesn’t really matter what I choose, or maybe it was a trick question from the start…"
y simple"Let’s see..."

menu:
    "What do I take?"
    "The Lakonia Academy Student Handbook.":
        $ book1 +=1
    "The Philosophy of Monsters for Monsters- by Raymond K.":
        $ book2 +=1
    "The Adventures of Firefly, the Warrior Cat.":
        $ book3 +=1





un simple"Is that what you’re choosing?"
y s"Yeah, what do you think?"

un eyeroll"No comment."
y smug"No bitches."
un surprised"Wha-"
y ec"Let’s go!"
un squint"{size=*0.5}I’ll show you bitches you pesky cat, insulting me like that...{/size}"


q "That shower you’ve been hoping for will also have to wait. You dust off your clothes from sitting on the sidewalk earlier and put on some deodorant."
y s"Alright, I’m ready!"
scene dorm with dissolve
q "You walk out the door confidently and lock it behind you."
q "Small worries pass your mind with each step you take down the stairs, and when the cool air of the evening atmosphere brushes your fur, as well as when you see the fiery sky, your worries grow, together with the speed of your steps."
scene eveningtown with dissolve
q "What a useful thing would be to know how to use all those bikes sitting on the side of the road or the front of renting shops, instead, you’ll have to be thankful for fast legs and weak lungs."
y tired"I-I have to work out on...on more than just weight loss exce...exercises."
un bored"That’s what happens when you put your looks above your health and performance."
scene sunsethill with dissolve
q "Step by step, the buildings are left behind and the big hill you agreed to meet the stallion on comes into view."
q "A large tree standing tall on top of it, the reference point you’ve been told about, your destination."
q "That run all the way from your dorm lasted less than ten minutes, but you already regret it more than anything. The steep slope is bending your ankles and the smooth grass is not helping your ascend much."
y "Imagine if I’m not even in the right place."
un "You want to kill me with laughter?"
q "At last, after another ten or more agonizing minutes, the flat surface of the hill appears below your feet, a hill filled with wildflowers and a singular large tree, with its thick branches low to the ground."
q "But that is not the specimen you’re here to observe, except that…"
stop music fadeout 2.0
y worried"He’s not here…"
q "You scan the surface of the hill quickly, circling the tree’s trunk and looking through the tall grass, for a sliver of hope."
y "Am I...too late?"
th "No, you’re just in time."
play music "audio/horse.ogg" fadein 2.0
scene black with longdissolve
scene horsesunset with longdissolve
scene CGt8
th "The scenery is beautiful enough that it was worth the wait."
y ec"Therium!"

q "In your tired and semi panicked state you didn’t even think of raising your head."
q "There, just about two meters high, on a large branch surrounded by foliage, sits the awaiting stallion."
q "His eyes calm, his pose collected. He looks comfortable in his own world."

y sadsmile"Sorry, I kind of passed out, literally, but I’m here now, and I brought the book!"
y "Uhmm...should I join you up there?"

th "Do as you wish, my dear."
th "We’re here to have a good time chatting, as long as we can hear each other it’s perfect."
th "But sit down nonetheless, you seem exhausted."
q "You think about jumping on the branch below him, but it doesn’t seem sturdy enough to hold you, plus you’re a bit embarrassed to admit, but you’re not the biggest fan of trees or heights in general, so you take a seat by the tree’s trunk, on the soft grass."
q "It is surprisingly comfortable, thick weeds cooling off your bottom after the tiresome little journey."
q "The view you see before you is definitely something to write home about, the busy town with the Academy’s shadow looming over on one side, the vast blue ocean on another and the thick lush forest on another, complemented by the reds, yellows and oranges of the sky."

y "It’s beautiful…"
th "That’s why I chose this place."
y "We’re alone now, aren’t we?"
y "Completely alone...with nobody to distract us."

th "It would seem that way."

q "You know well enough this stallion is not dumb in the slightest, so you let the silence after his deadpan responses linger for a moment longer."

y s"I brought the book."

th "Let’s hear it then, your thoughts, your ambitions, your future."
y "As you said, it's a divination session, isn’t it?"
th "It will certainly dictate your future, but not in the way you think, and not because of a book, that’s for my own entertainment and curiosity."

if book1 >=1:
    y ec"The book I chose iiiiiis! Drum rolls please!"
    y "Tadaaa!"
    q"The Lakonia Academy Student Handbook."
    q "He looks at it for a while then laughs."
    th "Hah, good one, if you didn’t have any other book in your dorm you didn’t have to bring it physically."
    y surprised"No no, I’m serious! This is literally my favorite book, I’ve read it over and over, dozens of times in less than a year."
    y s"It’s written by the old Headmaster himself, and he sure loves his magic history."
    y "Usually nobody cares for a book full of rules and history and lessons, but when you’re the one who will have to experience all of those, it becomes much more entertaining."
    y "Kind of like browsing restaurant menus of a new city you’re about to visit, or vacation resorts, or even an online shop that you need to use."
    y "As long as it concerns me, then it’s entertaining."

    th "I’ll admit, a surprising answer from you."
    y sadsmile"Do you still think it’s dumb?"
    th "Nah, not at all, I didn’t think it’s dumb to begin with, I’d be a hypocrite if I did, since that is actually my third favorite book."
    y surprised"Really?"
    th "Yes, I...fell in love with this place at one point, and when I became a student I wanted to dedicate my full body and heart to my duties, so I also read that over...and over again."
    th "What’s your favorite chapter?"
    y s"Hmm, probably the mechanism behind the barrier, it is so much more complex than a regular barrier, as well as the barrier itself, after all, that’s what dictates our lives here."
    y "It protects us but also limits us from reaching the outside world."
    y "Since I’ll be here for years to come, that was the most interesting aspect."
    y "What about you?"
    th "I liked the footnotes."
    y simple"The footnotes?"
    th "Yes, the Headmaster’s footnotes, his encouragement, the jokes he’d make after a longer, boring chapter and of course, his wisdom."

    y s"I remember them now, I thought a lot of those were notes made by students, he really has a sense of humor, heh."
    th "He did."
    jump booksharing



elif book2 >=1:
    y blush"The book I chose might seem a little out of character but it’s, umm, this:"
    q"The Philosophy of Monsters for Monsters- by Raymond K."
    th "Huh...it really is."
    th "It’s your favorite?"
    y sadsmile"Yeah, I mostly started reading it because the author is my therapist, I just thought that was cool, someone I speak to every week has a book that’s not about my problems."
    y "I gave it a try and hey, it’s really good."
    y "I admit about half of it was almost gibberish to me, but his thoughts were very intriguing, especially when he was right there in front of me, and I could imagine those same thoughts flowing from his head, to his hand and into the paper."
    th "The idea of people as an unfinished project of some mad God, that we should fear man more than monsters…"
    y surprised"Oh, you read it too?"
    th "Yes, I did, in fact, it is my second favorite book…"
    jump booksharing

elif book3 >=1:
    y ec"My book is this!"
    q"{i}The Adventures of Firefly, the Warrior Cat.{/i}"
    th "Is that a children’s book?"
    y pf"A young adult book, actually, thank you very much."
    y ec"I just thought I’d bring a lighthearted book with me, one I enjoyed reading for the sake of reading."
    y sadsmile"It is a little childish, about the adventures of a little cat, venturing into the unknown after his owners died, with no place in the world."
    y "He finds a gathering of his own kind and now has to prove himself worthy to be among them."
    y "Unfortunately they all hate people, all except for him."
    y "It kind of turns into a little bit of horror...when they plot to murder some people, but hey, that just proves that it’s not for kids!"
    th "I might’ve judged too hastily then...it truly tells a unique story."
    th "Not every book you read has to have a deeper meaning, after all."
    y s"Exactly, dumb entertainment is important."
    jump booksharing
else:
    pass

label booksharing:

th "In any case, glad you shared your book with me."
y s"So...what spell did you use?"
th "Spell?"
y "You know, for divination."
th "Just something called logical analysis."
y simple"Ah...so...no magic?"
th "Trust me, some people are easy enough to read without magic."
th "Your response shows me enough."
y s"Alright, in that case-"
y "What did you choose?"

th "I don’t remember saying I’ll bring my own book."
y smug"Yet you sure are holding what looks to be a book."

th "Would you look at that, must be fate."
show scribble with dissolve
th "But this isn’t really a book, it’s more of a diary, an incomplete one at that. The author died tragically before finishing it."

y simple"Is that the original?"

th "No no, I wouldn’t dare touch the original."
hide scribble with dissolve
"Did I just see something in my peripherals, or..."
th "But the writing holds true to it nonetheless."
th "The transcriber has a good reputation around here."

y simple"Why did you choose it?"

th "Ironically, I hate the contents inside it more than anything, almost every line clashes with my own ambitions and desires, and the writing itself is mediocre at best."
y confused"You love and hate it at the same time? How does that work."
th "I told you it’s ironic, I suppose it’s because it intrigues me."

th "I am trying to understand what made the writer such a beloved person, what about his views makes this diary so precious to some."

y "Who is the author?"
play sound "audio/static.ogg" volume 0.3
th "Why it’s {b}{i}redacted{/i}{/b}, of course."
th "You might be familiar."

q "A stupid, infuriating, hideous smirk appears on his face, making your blood boil."
"No it doesn’t...what are you talking about?"
y simple"I don't think I heard of them."
"The name itself kind of slipped my mind as he said it, I must still be a little tired."
th "In the end it is entertaining, and isn’t that why we read books? Sure, information and knowledge is great, but if it provides zero mind stimulants then what is the point?"
th "Was that a satisfactory answer?"

y s"Definitely, I learned a lot of things about you with that one."
th "Such as?"

y smug"It tells me you are way more open minded than I thought, if you’re willing to read and study something written by a person you openly dislike and don’t agree with."
y ec"It also tells me your empathy levels are through the roof!"

show horsesunset2 with dissolve
th "Is that really your final takeaway?"
th "Only positive things?"
th "What about comparing it to an unreasonable obsession? Or calling me a masochist for angering myself with this kind of stuff?"
Th "There are many bad takeaways from my words depending on who I speak with, and there is no way you of all people agree with everything."
th "We are way too different."

y sadsmile"You’re right, I don’t understand a lot of your ways."
th "So why…?"
y "You’re giving me too much credit, the simple answer is that…"
y ec"I just don’t care."
y s"I don’t really care for our differences, because just like you and the diary, it’s fun to work through them."
y "It’s true, I don’t know a lot about you, I’m sure you must have some kind of dark, edgy secret beneath the skin, but for now, all I know is that I like you, so yeah...take that I guess."

y "My ultimate reasoning will always be-"
y sadsmile"Some things are worth fighting and hurting for...you know?"

th "…"
th "Fine. You win. You weakened me enough."
th "What’s your question?"

q "Your eyes sparkle and your back straightens, at last, your long awaited opportunity is presenting itself, and you have one chance, one question, one answer."
q "Make it count…"

y simple"Who…"
y "Are you, exactly?"
hide horsesunset2 with dissolve
q "From above you a chuckle can be heard and the rustling of leaves as the stallion readjusts his position, preparing himself."
th "You’re not as goofy when the stakes rise high, you might just have hope in you."

th "Have you heard of Eldor?"
Y "Umm, it is a city in the Kingdom of Lordanna, correct?"
th "It WAS."
y confused"Is it not...anymore?"
y "But I read-"
show horsesunset2 with dissolve
th "It’s all fake."
th "Anything the media says about Lordanna is either speculation or fabrication."
th "Eldor is its prime example."
th "The place is a ghost town, few buildings remain standing occupied by gangs, thugs and thieves, no sane person lives there anymore."
th "Of course, the name still stands on the map because the King wouldn’t possibly allow the world to think his perfect paradise has problems."
y simple"I’m assuming you were born there, in Eldor."
th "That would be my curse, yes."
th "To be unfortunate enough to be born in a place plagued by war."
th "Father died fighting in it, mother slain by it."
th "And even the King claims it never happened."
th "But hundreds of blown up buildings and thousands of lost souls would say otherwise."
th "All that was left for me was to flee."

th "And what better place than the country that these useless people's conflicts never touched."
th "The sheer density of Nightfallen keeps whole armies away."
th "Without trained hunters and specialized equipment, a handful of demons are enough to wipe them out."
th "Of course, there are downsides, you can’t leave a barrier without the risk of being raped or on occasion even murdered, unless, of course, you have hunters by your side."
th "However, that is the price you pay for peace."
show horsesunset3 with dissolve
th "These monsters considered ‘pests’ by most are, in the end, the saving grace and the driving economy of the country."
th "Nightfallen have shown me kindness, my kind have shown me horrors beyond belief."
th "I am someone that knows the difference between bad and evil."
q "While clutching the book in your hands, a drop of crystal clear liquid splatters on top of it."
"Is it...starting to rain?"
q "Of course not, you knew that already, it was a tear, a tear replaced quickly by laughter."

th "Haha."
th "You know...it’s funny."

Th "Only about four people know about my past, and now you’re the fifth."
th "I can’t even wrap my head around how we got here."
th "It wasn’t in my plans to tell you all that."

th "For years I’ve been trying to find my purpose, to find ways to achieve my own personal agenda."
th "And I thought the impossible was about to become reality…"
th "I thought I’ll finally do something other than sulk for the first time in over two decades…"
th"But I wasn’t good enough...apparently."

show horsesunset4 with dissolve
Th "What about you?"
th "What’s so SPECIAL about you?"
q "He asks with a hint of venom in his voice."
y simple"Not much…"
y "Not compared to you at least."
th "My sorrows do not make me special, and neither do my talents, which you’ll probably surpass in a matter of years, or less."
y sadsmile"I doubt I’ll ever get close to your level."
th "Come on, are you playing dumb on purpose now?"

th "You summoned my own pet out of my own crystal better than I can."
th "And you’ve never even summoned before."
th "You didn’t even know the difference between the types of gems, or even the price of a Nightfallen."
th "How can you hunt them when you don’t even know their worth?"

th "So give me a reason, some information, anything, there must be something worthwhile about you."

y "I guess, well, my dad left when my sister was born, if that counts for anything."
q "He chuckles again."
y "It is pretty funny compared to your life, I admit, I know that much."

th "That’s not why I’m laughing."
th "It’s not your fault you grew up privileged."

th "Having everything handed to you on a platter."
th "Energy manipulator..."
q "He looks at the darkening sky, contemplating."
th "We are so very different, [name]."
th "And yet...you’re so much like the author of the diary, that I can’t help but be intrigued, although angry at the same time."
th "I am a summoner that refuses to kill Nightfallen."
th "That’s not normal, that’s not what a good summoner does."
th "{i}'If you want to stand on the side lines, become a Defender'{/i}."
th "So many times people have told me to join the Defenders, but I don’t want to just...not participate in the problem…"
th "I want to solve it."
y simple"It might not be a good time, or the answer you’re looking for at the moment, but that seems...impossible."
y worried"You can’t change the core of the world, can you?"

q "He looks down at you with a frown on, which starts to soften as he meets your eyes."
th "I can’t, not anymore."
th "But that won’t stop me from trying."
th "And the more I think about it, the more I realize that, perhaps...it’s for the best."

y "I’m not sure I follow."
hide horsesunset4
show horsesunset2
th "You will understand, in time."
th "Your future is still yet to be determined."

y sadsmile"If not even a divinator can see my future then I’m in rough waters, huh?"

th "You like surprises, don’t you, [name]?"

y "As long as they’re good surprises."
scene horsesunset with dissolve

th "But that takes away half the fun."

y simple"I think it just turns into gambling with extra steps."

th "Gambling with fate, the most beautiful thing to witness as a divinator."
scene horsesunset with dissolve:
    blur 15

q "The few Nightfallen creatures around him turn into smoke, along with the diary, and the stallion jumps down beside you."
th "Our conversation was eye opening for sure, I just have to figure if the image before me is ugly or not."
y sadsmile"I’m sorry for making you cry, but I appreciate the honesty, more than you know."
th "…"
th "Opening me up like that the way you did is turning out to be more troublesome than I thought, I admit."
th "Hard decisions are foreseen in the near future."
th "Thank you for your answers as well."


stop music fadeout 2.0
th "For now, it’s goodbye."
scene sunsethill with dissolve
q "With the wind playing through his mane and the setting sun turning his silhouette dark crimson, he takes the first steps down the hill, leaving you alone with your thoughts."
y determined"One thought being the loudest."
y "Scribbles! I need you to fetch me something, pronto!"
un "Already read your mind, literally...I’m on it."
scene black with dissolve
scene sunsethill with dissolve
q "You run after the stallion who moves painfully slow, with his hands in his pockets and head kept down."

Y ec"Therium! Wait up!"
play music "audio/horse.ogg" volume 0.4 fadein 0.5
show horse bored with dissolve
q "He turns his head surprised and halts."
y ec"One last thing, since we’re parting ways."
show bluerose2 with dissolve
show horse shock with dissolve
q "You take out a beautiful, half bloomed blue rose and hand it to him, a real rose, a rose which the setting sun is forcing to close."
y sadsmile"Figured it’s my turn to be a bit of a flirt, even if it’s not my style."

th "Why…"
th "Are you doing this?"
show horse sad with dissolve
show horse mad with dissolve
show horse sad2 with dissolve
q "His surprise turns to sadness then anger and finally acceptance in a matter of seconds."
y smug"Remember what you said back then? A real rose for when we say goodbye."
y "This is the first time we’re saying goodbye since I came here."
if theriumhome>=1:
    y "Well...other than yesterday evening…"
    y "But you know what I mean."

else:
    pass

th "You even remembered that little thing?"
hide bluerose2 with llongdissolve
show horse rose with llongdissolve
q "He scoffs, then accepts the flower with shy hands brushing against your fingers."
q "He grabs the flower bud close to its base, sniffs it from a distance, the fragrance being strong enough to notice even from where you’re standing, then-"
q "Gently breaks the head from its stem, placing it into his summoning pouch."
q "You’d be a bit disappointed by that if you didn’t know just how important a summoner’s pouch is to them."
q "His faint smile fades as his next words are spoken."

show horse sad2 with dissolve
th "[name]...remember how I flirted with you uncomfortably obvious at times?"
th "Many times, in fact."
play sound "audio/fluster.mp3"
y blush"Uhmm, y-yeah?"
y "I don’t mind, I actually liked it, if that’s what you’re-"
th "I want you to forget all about that."
y simple"Oh."

th "You deserve better."
th "And thanks...you gave me a lot to think about."
hide horse sad2 with dissolve
q "This time, as he turns around and walks away, his steps are more rapid and head kept higher."
q "It could be an attempt to hide his emotions or maybe you really did make him feel better."
stop music fadeout 2.0

y sad"I don’t know...I feel like I completely killed him today…"
un "Why do you say that?"

y simple"Ever since-"
un "Sorry, just a sec, I don’t want to have to narrate you leaving this place. So can you do it while explaining whatever you’re about to explain?"
y "Oh, ok, sorry."
play music "audio/evening.ogg" fadein 2.0
scene eveningtown with dissolve
Y worried"As I was saying, ever since he got that call earlier he seemed sad."
y "Or angry?"
y simple"He gave me that invitation and made me bring a book, I thought we’ll have a great time talking about them, then we’ll give each other questions about our personal lives in a place that nobody is around to hear, but-"
y "I guess I underestimated what {i}‘personal’{/i} means to others."

un "What does it mean to you?"
y "Nothing."
y "Literally nothing, or barely something."
y "The personal stuff is usually the embarrassing things that happen to me and family issues."
y "Then half the things he said…"
y "He was obviously in turmoil, but what exactly about?"
un "Maybe his dead parents or home country plagued by war?"
y "No, that was not it, it had something to do with me."
un eyeroll"He’s just jealous of your abilities, duh."
y worried"That is also not it! How can he be jealous when I displayed almost no skills!"
scene cafsun with dissolve
stop music fadeout 2.0
y "He must know something I don’t, something about me, about...my energy powers maybe? Or even about-"
un eyeroll"Ughh, it’s not that deep, maybe he’s just a bad person, did you think about that? Many people put on a face and it turns out they’re evil pieces of shit."
y bored"And your attitude-"
un "Oh here we go."
y simple"You don’t like him, do you?"
un sidee"I don’t...hate him."
y "But you dislike him?"
un "…"
un "No comment."
y "{i}*sigh*{/i}"
y angry"Everyone wants to give me a migraine these days."
y bored"People’s emotions really are way too complicated."
play music "audio/montage3.ogg" fadein 2.0
t "[NAME]! [NAME]! [NAME]!"
y "Speaking of headaches."
a "{size=*1.5}COME BACK YOU FILTHY $*#@& SLUT!{/size}"
un "Huh, your mind automatically censors the extra bad no no words, neat."
show cat21scared with moveinleft
hide cat21scared with moveoutright
q "The loud purple cat from earlier comes running up to you while screaming at the top of his lungs, turning heads as he passes."
q "He jumps into your arms then immediately gets behind you, using you as a meat shield against the approaching, fuming tiger."
show tiger20angry at left with moveinleft
a "ACCEPT YOUR FATE AND DIE!"
show cat21cry at right with moveinright
t "I SWEAR I DIDN’T SEE ANYTHING!"
a "LIES!"

y surprised"Whaaat is happening?"
a "[name], please get out of the way, I need a clear view of his throat."
t "Go deep throat yourse- AH!"
q "He covers his own mouth fearing for his life, whatever he was going to say, he realized he better not."
y "It’s not up to me to move, he’s kind of just man-handling me around."
un "He’s extremely strong for a twink."
show wolf20sad with moveinleft

d "Guys, come on, you’re gathering eyes upon you and you’re scaring [name]!"
y worried"Very much so."
t "As my best friend, you have to protect me, [name]."
y bored"We’ve only interacted like four times in total."
y simple"Why do you want to kill him anyway?"
a "Let’s just say… he saw something he shouldn’t have."
t "Dallan saw it too! He was with me!"
a "You know Dallan didn’t see shit! SO STOP LYING!"

d "Aiden, whatever Tate saw, I’m sure he wouldn’t tell anyone, right?"
t "Yes! Yes, I promise!"
show tiger20angry at left2 with move
a "That is not good enough! I need to make sure."
a "The tongue and fingers have to go, for starters."
t "{i}*Gulp*{/i}"
show tiger20angry at left with move
hide cat21cry
show cat21scared at right
t "Look! Why can’t we make a compromise, you already know MY biggest secret, now I technically know yours, allegedly, so we have black mail on each other, isn’t that enough?"
a "I do have your biggest secret in my claws since I helped you with it, it’s true…hmm."
hide tiger20angry
show tiger20bored2 at left
a "That can be a good compromise, better than manslaughter anyway."
hide tiger20bored2
show tiger20bored at left
a "Why didn’t you say anything sooner?"
t "I WAS TOO BUSY RUNNING FOR MY LIFE!"


hide cat21scared
show cat20simple at right
q "Finally, the cat feels slightly more secure and lets go of your shoulders, his claws leaving small holes in your shirt."
d "{i}*sigh*{/i}"
d "Sorry, [name]."
d "They’ve been like this all day, and they refuse to tell me what these ‘secrets’ of theirs are."

a "It’s for your own good."
t "Actually, it’s for ours, you’re too obedient, Dallan."
hide wolf20sad
show wolf20simple
d "That’s a good trait to have! Isn’t it?"

y ec"I love obedient boys!"
hide wolf20simple
show wolf20ec
d "See?"

t "Ew."
a "Ew."
un "Ew."
y angry"Not THAT way!"
stop music fadeout 2.0

d "Anyway, after so much running around, I need some good food, table for four, here we come!"
scene food with dissolve
play music "audio/lunch.ogg" fadein 2.0
q "You take a metal tray and start to fill it up with whatever the cooks have made, and for tonight, dozens of stir fried dishes, from chicken, pork or beef, to veggies, seafood and different types of noodles."
q "You take a little of everything and a bowl of egg drop soup to balance everything out."
q "You didn’t realize it until now, but you’re on the verge of starvation, having only eaten breakfast."
scene cafsun with dissolve
q "You follow the other three guys to an empty table and sit down."
q "Their earlier conflict quickly disappears and they start laughing among themselves like friends, well, the cat and the wolf are laughing, while the tiger is barely chuckling."
q "This new friendly vibe almost made you forget about him, but a simple thought is enough to sour your face as you look at your reflection in the silver spoon."

q "The cat is the first to stop the jokes."
show cat20simple with moveinleft
t "Hey, something wrong?"
t "Why the long face?"
show tiger20simple at left with moveinleft

a "Talking of long faces, where’s Therium, weren’t you hanging out with him earlier?"
show wolf20simple at right with moveinright
d "Did he have something to do with it?"
y simple"Well… yes and no."
y sad"You guys were kind of right before, he’s weird, not necessarily in a bad way...but weird for sure."
y simple"I just don’t really know how to read him."
hide tiger20simple
show tiger20iritated at left
a "Fucking hell, he didn’t break your heart already, did he?"
a "That’s it, I’ll kill him."
hide cat20simple
show cat21bored
t "Sit down avenger."
t "You’ve broken ten times more hearts than he ever did."
y worried"Please… don’t, he didn’t really do that...I mean, its not like we were together or anything."
y "I literally met him yesterday."
hide wolf20simple
show wolf20sadsmile at right
d "So?"
d "I met Chelsie on day one and we’ll be best friends till the end of time."
hide cat21bored
show cat21smug
t "Yeah, and Aiden meets a guy on the first day then sends them to the hospital in the same day."
a "Continue like this and I’m not helping you anymore."
"He makes a zip up motion on his mouth."
d "What we’re trying to say is that time is irrelevant, starting something is always the most complicated part, ending them is easier."

a "You only live once after all."
d "It is the experiences you share together that matter."


t "Can’t believe you two have similar views on relationships, to some extent."
hide cat21smug
show cat21scared
q "The tiger shoots him an ugly look."

t "A-and that’s not an insult! Just an observation, I swear."

un "I agree with them."
un "It’s better to regret a relationship than to regret missing out on one."

"I thought you didn’t like Therium that much."
un "I don’t have to be in love with him to tell the truth."

y sadsmile"Can’t have a broken heart that easily, can I?"
y "I mean, I didn’t even know I liked him this much before… by before I mean minutes ago, actually."
hide tiger20iritated
show tiger20bored at left
hide cat21scared
show cat20smile
a"Love is weird, sometimes it’s just lust disguised as something more."
d"Or admiration."
t "Or pity."
d "But you won’t know unless you dive in."


y simple"So… you’re saying I should just go for it?"

a "We’re saying you have to make up your mind now, and come up with a reasonable response now."
d "And throughout your journey you’ll find out if that answer was correct!"
T "Or if you were meant to die alone surrounded by cats."
t "I volunteer if anything."
stop music fadeout 2.0
a "So...do you like him now?"

q "A butterfly lazily flies in through the window and lands on your shoulder."

menu:
    y butt1"Do I?" with llongdissolve
    "Not really…":
        $ thepoints +=-1
        play sound "audio/drum.mp3"
        y butt1"I...I don't think so."
        play music "audio/horse.ogg" fadein 2.0
        y "I think I was just happy he spent so much time with me."
        d "Well, that settles it."
        t "Don't worry, [name], you'll find someone desperate enough."
        a "That someone could be very close."
        y butt2"Thank you, Aiden."
        a "Maybe in an arm's reach, right under your nose."
        y "Gosh, wouldn't that be lovely?"
        a "..."
        a "Incredible."
        t "Anyway-"
        jump battlepartner

    "Yeah…":
        $ thepoints +=1
        y butt1"Now that I think about it-"
        play music "audio/hope.ogg" fadein 2.0
        y butt2"Yes, I think so."
        y "For so many reasons yes."
        show cat20ec
        show wolf20ec at right
        t "Yey!"
        d "Yey!"
        show tiger20ec at left
        a "Damn it- I meaaan, yey!"
        d "That settles it!"
        y butt2"I’ll think about what I should do."
        hide tiger20ec
        hide wolf20ec
        hide cat20ec

        t "And if by any chance he rejects you and you don’t hit it off, and things become awkward and he hates you forever-"
        a "This better lead somewhere."
        jump battlepartner



label battlepartner:
play music "audio/lunch.ogg" fadein 2.0
t "-do you have any plans for tomorrow’s pair battles?"

y simple"I forgot about those for a while. I’m not exactly sure about my strategy or even who I’ll be with, do you have any suggestions?"

t "Personally I’m taken, and we already registered, so as much as I’d want to I can’t go back."
hide cat20smile
show cat20angry
a "I could get rid of my partner if you’re in need of a pair."
t "I’m your partner!"
a "As I said, easy to dispose of."
hide cat20angry
show cat20bored
y bored"I think I’ll pass…"
d "I’ll be fighting alongside another first year."
hide wolf20sadsmile
show wolf20 at right

d "But maybe you could set him up with Monty, Aiden."
hide wolf20
show wolf20simple at right
a "Not a chance."
t "Is he still in the hospital?"
a "Yup."

y simple"What happened to him?"

adt "Chelsie."

y pf"That...doesn’t tell me much."

y simple"In any case, is it bad if I stay out of the battles?"

d "You could...but-"
hide cat20simple
show cat20
t "It’s so much fun! You can’t just stay on the side lines!"
a "And it’s a good time to show off, might impress some teachers, classmates or even the Headmaster."

d "You could always go alone, it’s not against the rules, but highly unlikely you’ll win, teamwork is better than personal strength."
hide cat20
show cat20smug
t "Not if the opponent is someone like you, Dallan."
hide wolf20
show wolf20awkward at right
d "Come on, I’m not THAT strong."

a "Sure…like you couldn’t destroy the whole town in one move if you wanted."

d "Haima and Merina can do that too."
stop music fadeout 2.0
y simple"That’s scary…"
scene black with llongdissolve

q "You continue eating while being amazed at these people’s abilities, making you feel more and more insecure with each passing word."
q "With your trays empty and stomach full, you part ways with the three men with some hearty goodbyes, and walk towards your dorm."
q "The moons are out already, illuminating your path alongside the scarce street lamps, and the evening’s air has lost a couple degrees since you entered the cafeteria."
play music "audio/nightsounds.ogg" fadein 2.0
scene dorm with dissolve

q "It isn’t too late, but your eyes are already beginning to close on the way, hoping and praying you won’t pass out like earlier."
q "The familiar stone stairs make a satisfying stomping sound beneath your feet with a light echo."
q "You open the door to the dorm building and walk up what feels like an infinite number of stairs."
q "The desire for an elevator is almost as strong as the one for a soft bed."
scene dormroomnight with dissolve

q "You unlock the door and step inside, not bothering with the lights."

un "Aaare you going to shower?"
un squint"I feel sticky and filthy."

y sleepy"Do I haaaave to?"

un suspicious"Yes! I’m not sleeping like this!"

y "Don’t you feel my fatigue too?"

un "My standards are keeping my head leveled and my wits sharp."
y "What the hell are you saying?"

un ang"Get up and go WASH YOURSELF!"

y "FIIIIIIIIIIIINE!"

scene shower with dissolve

q "You begrudgingly take off your clothes one by one and throw them on the bed, stepping in the bathroom already naked."
q "The shower is still missing its head, but other than that, everything looks great, they even have their own shampoo and soap brands ready for you, as well as a nice towel."
y nakedbored"Let’s hope the water’s hot."
q "Except for the fact that it feels like being hosed down with...well, a hose, because of the missing shower head, the water feels nice on your skin as it soaks into your fur."
q "The relief and relaxation comes over you almost instantly, clearing your mind with each passing second and with each square inch of fur getting wet."
q "You certainly don’t regret listening to a certain demon inside your head."
y "For once."
q "Your sleepiness slowly fades, not completely, but enough to make way for extra thoughts of that annoying stallion that just won’t go away whenever you close your eyes."
y nakedsimple"No...not annoying, I’m mistaken."
y "It’s my fault for falling for people so easily."
un "Yet you can’t stop imagining him naked, here, with you in the shower."
y "I can’t control my mind, and it’s not like it is lying, I’m just...confused right now."
un simple"Can I be honest?"
y "Are you gonna say something mean?"
un sidee"Nnn-noo...yes."
y nakedbored"{i}*sigh*{/i} Just spit it out."
un "I don’t understand what you see in him."
un "Like...at all."
y "How do I put it?"

label compliments:
menu:
    y nakedsimple"He’s…"
    "Really nice.":
        $ compliment +=1
        y nakedss"He's very nice."
        y "Ever since I met him he did absolutely nothing to make me uneasy."
        y "He was nothing but helpful and supportive so far."
        jump compliments
    "Extremely hot.":
        $ compliment +=1
        y nakedss"So incredibly hot."
        y "You don't even know how hard it is to contain my emotions when I see those muscles, that smirk, those eyes, that bulge..."
        un "Trust me, I know..."
        jump compliments
    "Just my type.":
        $ compliment +=1
        y nakedss"My type for sure."
        y "Smart, kind, mysterious, hot, and talented."
        un "There's also the size difference."
        y "See? You get it."
        un "Hardly."
        jump compliments
    "He’s smart.":
        $ compliment +=1
        y nakedss"Extremely smart, cunning and...foxy, in a way."
        y "The way he speaks and walks is so sophisticated."
        un "I can...kind of see that?"
        jump compliments
    "He’s unique.":
        $ compliment +=1
        y nakedss"A unique guy."
        un "Incredible reason."
        y "He has something about him I never saw in anyone else before."
        un "New type of mental illness discovered, I guess."
        y nakedbored"Is it even worth to continue with you?"
        jump compliments
    "What else…?":


        if compliment <= 0:
            "I should give at least one reason..."
            jump compliments
        elif compliment >=3:
            $ thepoints +=1
            pass
        else:
            pass

y nakedsimple"What else...let’s see, umm."
un bored"I get it, I don’t need any more excruciating details."

y nakedsmug"You asked for it."

un suspicious"No, I simply stated that I don’t understand, not that I want an explanation."
un bored"Congrats, you bummed me out, just get out of this shower before I have to narrate how you get a boner and jerk off thinking of him."

y nakedsimple"…"
y nakedpf"Did you have to mention it?"

un eyeroll"UUUUGHHHHH, here we go again."

q "These recent thoughts of the stallion make you blood rush downwards, creating a big problem you have to take care of."
q "Take care of by squeezing, rubbing and massaging it rapidly with your eyes closed and knees bent."
q "Before you know it, you’re kneeling on the floor of the shower, with your head tilted upwards and your maw wide open in a silent moan."
q "Seconds later, the water carries away down the drain the last hint of lewdness that happened this evening, even your mind starts to dress the stallion back up in his usual attire, but doesn’t erase the smile on his face as he looks warmly into your eyes."
q "This time, the blood rushes into your heart and face."
scene dormroomnight with dissolve
q "You decide to step out of the shower and dry off before anything more can happen, again…"
q "Since you’re alone, clean and naked, you decide to get under the covers as is."
y nakedbored"And with sleep nowhere to be found."
un bored"I hope you’re not trying to say the shower took the tiredness away, because it absolutely was your own horniness that did that."

y "I’m not pointing fingers."
stop music fadeout 2.0
show blink with dissolve
y "I’ll just try to close my eyes and hope I pass out."
scene black with dissolve
play music "audio/nightsounds.ogg" fadein 2.0
un simple"Since you’re going to be awake for at least a couple of minutes let’s discuss."

un "So, what’s your plan for tomorrow?"
y nakedsimple"Good point, that is something I might want to think about."
un "Yes! A plan! Let’s hear it."
y "…"
y nakedss"The best course of action would probably be to take my heart in hands and just ask him on a proper date."
un bored"No dumbass, for the battles! Who are you pairing with and how do you plan on winning?"
y nakedsimple"Oh…"
y nakedbored"Don’t know and don’t know."
un "Are you gonna stay out? Just like that?"
y nakedsad"No! I can’t! I’m a recommended student after all, even if there’s not much for me to show off."
un simple"So yes battle?"
y nakedhurt2"Aghh, but I don’t want to have my face shoved in the dirt!"
y "That would be even more embarrassing than not participating."
un bored"Beg."
scene dormroomnight
y nakedsimple"Excuse me?"
un bored"Beg for my help and I’ll help you."
y nakedangry"I didn’t even ask for your help in the first place, what makes you think I’ll beg?"
un suspicious"Come on, just because no magic rules forbid you from lying doesn’t mean I can’t smell bullshit."
un tease"Do it and I’ll make you stronger overnight."
y nakedsurprised"You can do that?"
y "Overnight?"
un "Yup, with very little effort, in fact."
y nakedpf"How?"
un bored"It’s a little demon magic, and I was trying to figure out if you’re worthy of it or not."
y naked"And I am?"
un "Ohoho, no no no...no, not even a little, but! I feel so bad for you that I’ll still share it with you."

un "If you beg."
y nakedpf"Demon magic..."
y "…"
y nakedbored"Fine."
y "Scribbles, please help m-"
un pride"No no, properly, on your knees."
y nakedangry"Are you serious? I am literally heartbroken! Have some mercy for God’s sake."
un "I kneel to no false Gods, but mortals do in times of need, so come on, hurry up, mortal!"
un bored"Besides, {i}‘heartbroken’{/i} is a strong word for what you’re feeling, not to stir that pot again."
play sound "audio/sheets.ogg"
y nakedpf"…"
un tease"Yeeee, good boy!"
q "You place one knee down then the other, slowly, grumpily, as if a heavy weight impairs you, then start your begging chant."

y nakedasleep"I beg of you, oh powerful Demon inside my head, please give me the power to be less than useless and defeat my foes."

un simple"Huh."
un sidee"That was actually better than I thought."

un bored"Alright, I’m satisfied, nice job."
un "Here’s the deal."
un "The fact that you can already summon small Nightfallen is great! But you’ll need muuuuuuuch more than that."
un "So, I’ll help with a little boost."

un "We go at midnight!"

y nakedsimple"Where exactly?"

un tease"I wasn’t just a powerful demon, I was a RICH one!"
un simple"Some of the old toys from my treasury are still on this campus, and it just so happens I know how to get to them."
un squint"But you must NOT be seen!"
un "I don’t need just any random idiot to know about my place."
un simple"Stealth mission! That’s why at midnight."

y nakedbored"You’re underestimating how bright and busy a town like this can be at night, but fine, I’ll get behind that."
y nakedsimple"Should I set an alarm?"
un bored"Eh, I’ll wake you up."

y "Hope that won’t be proven a problem."
un curious"Why would you say that?"
show blink with dissolve
y nakedasleep"Cuz I’m kind of...kind of-{i}*yawn*{/i} getting super tired again."
y "It kind of...feels like earlier today...and I-"
stop music fadeout 2.0
un "Great…"
scene black with llongdissolve
scene theriumdream3 with llongdissolve
scene CGt13

Demon "Fear not, young one."
play music "audio/unspoken.ogg" fadein 2.0
Demon "We shall make sure to escort you to a place of safety."
Demon "Beyond the vast expanse of land and seas, lies a sanctuary untouched by conflict."
Child "Almost sounds too good to be true."
Child "Will you come as well?"
Demon "..."
Demon "Perhaps in a time yet to come, when our mere presence is no longer met with the desire to tear our hearts out."
Demon "Your kind must grow, still, but you shalt grow with them."

Child "Did I ever tell you I like the way you speak? It’s funny."
Demon "About a thousand and one times, dear one, it is amusing to think about."
stop music fadeout 2.0
Demon "How our learning roots dictate our tongues, ways and desires."


scene black with llongdissolve
play music "audio/violin.ogg" fadein 3.0 volume 0.3
un simple"Dear diary."
un "Today…"
un sidee"Was actually a lot of fun."
un "Being a narrator for a mentally ill mortal wasn’t on my bucket list, but it’s more entertaining than I thought."
un simple"I feel like I’m growing as a writer, even if I’m not writing anything down other than in my diary, of course."
un "It also opens my eyes to a whole new world, when I have to watch and describe every room, every step, every sound and every smell."
un "The mortal seems to like it a lot as well, his mind is much calmer whenever I do it, I’m not sure if that’s a good thing or not."
un "Maybe that’s a reason my mind control never worked on him, but who the hell knows, thousands of years and the secrets of arcane spells are still a mystery to me."
un "I’ll continue to do this, because it’s fun, and because it benefits us both."
un bored"As for what’s happening now..."
un "The vessel is once again dreaming of something weird."
un curious"Ever since he stopped dreaming of me, he's dreaming of...stories? Of other people and other Nightfallen."
un simple"Can't say I understand their meaning."
un "I decided to skip the one from tonight, even though they can prove somewhat entertaining at times, just so I have time to write in my diary."
un "Forever trapped in this wee dark corner o' mine as I do so, alone, the only private place I can write in peace."
un sidee"Until yesterday's dream proved me wrong...but we don't talk about that."

un sidee"Well, got to go, as the time to wake him and take him to my secret dungeon is here."
un bored"I am going to use a new technique I learned while being inside his head, I call it: {b}Brain Scratch{/b}."
stop music
un "Volume warning."
un "You have been warned."
play sound "audio/loudsound.mp3" loop

scene dormroomnight with hpunch
play music "audio/chase.ogg" fadein 2.0 volume 1.0
y nakedscared4"AAAAAHHH!"
y "WHA-WHERE THE HELL, WHAT’S HAPPENING, WHERE AM I?!"

y nakedangry"WHAT IS THIS?"

un bored"Are you awake yet?"

y "SCRIBBLES?!"
y "YES! YES! I’M UP! CUT IT OUT!"
stop music
stop sound
un tease"Oki, just making sure."
play music "audio/nightsounds.ogg"
y nakedhurt2"Why’d you have to be THAT loud? And inside my head too? How do you even do that?"
un simple"I had to be loud to make sure I interrupt your dream."
un "It didn’t work when you passed out earlier today, so I wasn’t sure if it would work now."

y "You’re lucky my dream wasn’t too action heavy."

un simple"What did you dream about?"
y nakedsimple"I think it was-"
un bored"Just kidding, don’t care, let’s go."
y nakedpf"Bitch..."
un "Whatever you dreamed about it had nothing to do with me since I wasn’t there, so have fun with your silly night adventures in the dream world, dreams of sluts and cocks, no doubt."
y "You seem a bit triggered."

un ang"Get dressed and move! We don’t have all night."
stop music fadeout 2.0
scene dorm with llongdissolve
q "You decide to stop pestering the demon and slowly open the door."
y bored"I did not decide to stop."
q "Yes you did."
y "No I didn’t."
play music "audio/nightsounds.ogg" fadein 2.0
scene theriumkiss0 with dissolve:
    blur 15
q "The darkness of the corridors cloud the voices in your mind as you walk out into the street."
y bored"{i}*sigh*{/i}"
q "Almost in an instant you regret not grabbing a jacket. The light wind ruffles your thin shirt and carries your tie over your shoulder."
un suspicious"Stay in the shadows, make the night your veil, be like an assassin."
y "Literally nobody cares if they see me."
un bored"That...might be true, for now."
q "Indeed, the streets and establishments are much more lively than we thought in this part of town."


q "Still, you continue to be guided towards the academy, with each block traversed, less lights in the windows and less people on the street."
q "Soon, even guards and police officers can be seen patrolling the area around the academy."
q "You think to yourself that it should be fine if you’re caught, staff members and students alike often must spend their late evenings or nights inside the academy, right?"
un "Well, yeah, but you don’t want to have it on your record that you were here, after all, you have no alibi."
y simple"Good point."
un "No worries, we’re almost there."

q "The moons are obscured by thick, dark clouds, and the stars remain the main source of light when the town’s street lamps disappear as you walk off path."
q "You follow directions and move all the way to the back of the academy’s main building, through some bushes, and a tight, short tunnel."
un "There! Just around that corner you’ll see a moss covered staircase."
y worried"Please tell me we’re not going underground or something?"
un "What kind of above ground dungeon have you ever been in?"
scene stairs with dissolve
y bored"Damn it...gigantic earth spiders, here I come…"
q "You round the corner and approach the stairs."
y simple"Now what? Climb them perhaps?"
un bored"You wish."
un "My dungeon is protected by a powerful yet easy spell."
un "You might get a little dizzy after doing it, so be prepared."
un "Repeat after me-"
stop music
nu "[name] [name2]…"
un scared"!"
y confused"My name? And why’d you change your voice all of a su-"
q "You feel a tap on your shoulder."
play music "audio/pianosoft.ogg" fadein 2.0
scene black with hpunch
y surprised"!"
q "You turn around and you jump back, tripping over the stairs and falling over, heart racing fast."
scene stairs
show cloak
with llongdissolve

y worried"It’s...you."

q "The cloaked figure reaches into an inner pocket and takes out…"
show medallion with dissolve
q "A medallion…"
q "A golden, glowing artifact held on by a string and the remnants of a past sturdy chain."
q "It holds it before you with an invisible menacing aura, it’s long, furless arms waiting for you to reach over."
q "You dust yourself off, then with a sheepish hand grab the medallion slowly."
hide medallion with moveoutbottom
show cloak close with dissolve
q "The figure grabs you tightly as you do so, and speaks:"


if thepoints <=2:
    nu "One last chance, make it count."
    y simple"O-ok?"
    jump aftercloak
else:
    nu "Good luck, make sure to amuse me."
    y awkward"T-thanks?"

    jump aftercloak
label aftercloak:
hide cloak with llongdissolve
stop music fadeout 2.0
q "T-the thing fades away before your eyes."
y pf"Cool cool cool cool cool..."
y "So-"
Y "That was-"
y simple"Him."
y "It."
un simple"The myth, the legend."
play music "audio/nightsounds.ogg" fadein 2.0

y "Is this thing what we came here for? A medallion"

un bored"Yuuup."

y simple"We’re not going in a dungeon then…"

un "Nooope."

y "But it was supposed to be in the dungeon…"

un "Yuuup."

y "And that thing wasn't supposed to have it."

un "Nooope."

y bored"You’re not very useful."

Y "Who was that and why did it have your medallion?"
un sidee"Uhm, no idea, but hey, now we don’t have to waste time, lets go."
y surprised"Wha-"
y angry"Are you just going to dismiss them like that?"
un ang"I don’t know! I don’t feel like solving mysteries now!"
un bored"Whatever that thing was it made our jobs easier."
un "Now we don’t even have to go into my secret lair."
y simple"Kinda disappointing...but aren’t you worried someone else knows about it?"
y "Maybe you should check on it."

un "Your fatigue is catching up with me as well, I can’t think of much else other than sleep."
un "Maybe after that test of yours or something we can explore more."
un "For now, tuck that thing away in your shirt and keep it out of sight at all times."
y pf"hmm..."
"Scribbles clearly doesn’t want to talk about it, but a big, fat question is...why?"
"Seems like a pretty big deal to me."
"I begin walking back- oh, wait."
"I’ll leave the narration to him before he gets pissy."
q "Hey, are you there? I’m talking about how the night’s air feels on your skin again, you listening?"
y simple"Yup, I’m here and focused."
q "Great, so, the cold air makes your pelt fluff up and bristle, but on the inside, your body is as warm as it gets."
y "That’s odd, could I have caught a fever?"
q "Your rapid beating heart says otherwise, perhaps that cloaked figure got you flustered-"
y "No shot."
q "Or maybe something from tonight’s experience made you think of a special someone, or a hot someone, at least."
y blush"I am beginning to think about someone now...and my heart is indeed racing."


scene theriumkiss0 with llongdissolve:
    blur 10
q "The town’s night lights are within view, just a block or two to go."
q "You follow the same path you took to the academy, and make sure to watch your surroundings for any guards or other strangers to question you."
q "That feeling of adrenaline keeps intensifying, as you now feel like you're being watched."
q "The clouds are now making way for the moons to shine bright over the streets, and from behind, a shadow looms."
stop music fadeout 2.0
y simple"Hello?"
y worried"I-Is anybody there?"
"..."
th "Curious seeing you here, [name]."
play music "audio/pianosoft.ogg" fadein 2.0
scene theriumkiss1 with longdissolve
scene CGt11

q "For some reason you aren’t too surprised about who’s voice you’re hearing, as you turn around, to see the familiar stallion resting under a street lamp."
q "His eyes are looking down, saddened, and his greeting did not contain any of his usual flare or ostentatious accents."
q "Less noble, less graceful and more direct."
q "You’d describe his overall appearance here as...dull."

y sadsmile"Hey...Therium, I was just thinking about you."
q "He scoffs."

th "Course you were."
th "The only path you ever do."

y simple"I’m not sure I follow."

th "Never mind that, what brings you here? Thought you’d be dreaming by now."

y sadsmile"I just couldn’t sleep, needed some fresh air, a lot of thoughts in my head, especially after our...meeting."
th "Yes, I’ve heard you had a lot to say about that to your friends at dinner time."

q "Your face flushes embarrassedly as you recall the events."

th "These two days since we met were…"

y blush"Wonderful?"

th "Hell."
y simple"oh."

th "Because I just couldn’t bring myself to believe that I’ve completely fallen for you."

y surprised"Oh!"

q "His words, their implication stuns you and roots you in place, your heart beats once again as fast as ever and sweat drips down your forehead."
y blush"I-I like you too..."
q "The stallion leaves his spot and walks closer to you, with a bored expression that turns into a soft frown."
q "He’s noticeably taller, especially once your knees start to give in to the pressure created."
q "His long front mane hangs close to your face and his snout directed straight towards you, eyes interlocked."
q "While your pupils were trembling and growing bigger, his were getting smaller, the fire in his eyes intensifying."
stop music fadeout 2.0

q "Something is...wrong here, but all your fantasies seem to be coming to life with that last statement of his, and you’re caught in a trance."
play music "audio/horse2.ogg"
play sound "audio/tension1.mp3" volume 0.2
scene theriumkiss1 with longdissolve:
    blur 10
show theriumkiss2 with longdissolve
th "You don't understand...I do not like you, not as much as the dirt between my claws."
th "But I love you more than life itself."
th "It is torture."
th "And I want this feeling to end."
yy "Love...me?"
q "His words should be a wake up call, an indication of this reality, but our leopard is too smitted by the moonlight reflected in his angry eyes."
q "One needs more than one working braincell to process those words."
th "You..."
"How did I get here?" with llongdissolve
"I barely know you, yet you dared steal my heart without my consent."with llongdissolve
yy "Is he..."
"You robbed me of my future, my destiny, my dreams...and now even of my humility."with llongdissolve
"His neck, his soft neck between my fingers, under my firm grasp a tumultuous storm of emotions raging within me, I could...I could still have a chance."with llongdissolve
"If only…"with llongdissolve
"If only you didn’t make me love you."with llongdissolve
"I hate it, I hate that I love you, why do I love you?"with llongdissolve
yy "Is he going to..."
show theriumkiss3 with llongdissolve
"And more importantly...why do YOU love me?"with llongdissolve
"He can't love me, I am not even an option in his sea of choices."with llongdissolve

"Your fur softer than fine silk, your scent: fresh and pure, your eyes hold the universe in them, looking at me like I deserve it."with llongdissolve
"His prestine white, spotted fur, his large, fluffed up tail quivering as his chin raises to meet my eyes."with llongdissolve
"Stop...you can’t...do this to me."with llongdissolve
yy "...do what I think he is?"
show theriumkiss4 with llongdissolve
"I need to put a stop to this."with llongdissolve
"But I can't, at least not this way."with llongdissolve
show theriumkiss5 with llongdissolve
"Why couldn’t you just stay where you came from?"with llongdissolve
"Why couldn’t you resist his call?"with llongdissolve
"Why are you so fucking STUPID?!"with llongdissolve
"YOU!"with llongdissolve
"You..."with longdissolve
show theriumkiss6 with llongdissolve
"..."with llongdissolve



"There is no point wishing for miracles now, what’s done is done."
"But what if the happy moments of the present are the saddest ones? Is that normal?"
"His adoring eyes have not left mine, yet, these words hold true."
"What thoughts do you hold behind them in this moment? Are you scared? Are you mortified? Are you apathetic? Or-"
yy "Please, please, please...do it."
"O'Lord, my Lord, what do you see in him so different from me?"
"Weaker than me, weaker than even my replacement."
"Is it the same thing I see now? This irresistible desire?"
"If so, my rage might not be satiated, but I understand completely."
scene black with llongdissolve
"The next thing I know, our lips are intertwined." with longdissolve
scene theriumkiss0:
    blur 20

show theriumkiss7
with longdissolve
yy "Finally!"
q"The moons hung low in the sky, casting a silvery glow over the secluded clearing where you two stand."
q "Abruptly, after a long lasting staring contest, the look in the stallion’s eyes softened."
q "A single, defeated tear pours down his cheek as the distance between you rapidly vanishes."
q "Your lips collide with a passion as raw and fierce as a tempest. It takes more than a moment for you to realize and accept that this is happening, but when you finally do, you melt on the spot."
q "His hands once hovering below your chin now grabbing hungrily at your fur tufts, pulling you closer with an urgency that left no room for doubt."
q "Your lips met in a kiss that was anything but gentle, a clash of desire as fiery as the heart of a star. It is a kiss born of long-denied longing, a maelstrom of feelings that had been simmering beneath the surface."
q "On your part fueled by lust, on his part by rage, which one’s better? You decide."
q "For now, what matters is the moonlight’s glow outlining your momentary sin."
q "What matters is tasting him, his mouth, his tongue, consuming any drop of this yearning."
q "You can feel that invading tongue do the same, making you shiver with delight."
q "Your body still feels paralyzed from his words, the kiss bringing in the antidote slowly."
q "As the initial blaze of your passion began to ebb, the kiss evolved. What started as a conflagration of need and desire slowly morphed into something deeper, more profound. "
q "The intensity that had fueled your violent union gave way to a tenderness as soft as the moonlight that bathed you."
q "Your movements became languid, exploratory, savoring each moment, each sensation. The ferocity that had ignited your kiss transformed into a gentle dance, lips caressing lips with a newfound reverence."
q "After what felt like an eternity of sweet heaven the warmth of his lips breaks away, making you long for more."
show lust with dissolve
q "You open your eyes to a world softened by rose-tinted glasses, gazing at your partner whose half closed eyes shimmer with pleasure and a thin layer of liquid."
q "The thin bridge of saliva between your mouths holds still until it breaks from his words:"
th "I love you [name], and unfortunately not just in a lustful way, the heart’s way."
y blush"Nothing unfortunate here, I love you too."
scene black with dissolve
q "Even though you’re bursting from excitement and anxiety saying those words, he is sadder still under the soft smile, but recovers quickly."
scene theriumkiss0 with dissolve
show horse smug with dissolve
play sound "audio/heart.mp3" fadein 4.0 loop volume 0.5
show lust with dissolve
Th "Come to my dorm, right now."
y blush"Y-you’re being forward again, is this your usual quirky flirting or-"
th "No, I need you to spend the night with me, I’ll be as forward as I have to be, to test these feelings or lock them away forever."
y "I’m not gonna refuse, but why now? Heh, I mean, what can we possibly do in the middle of the night other than sleep? Haha….ha."
th "Allow me to make it clear then."
Th "[name], I want to be inside you, all night."
th "I want to hear you moan under me and make you scream my name."
Th "Because you trapped me, and now I’ve fallen in love."
Th "I know it’s sudden, unexpected and perhaps stupid, but you’re the one that did it, so take responsibility."
Th "Do you like me enough to accept this?"
q "The lust rush creeping in and the new circumstances are screaming YES in your mind, but the demon in there is whispering no…"
stop music fadeout 2.0

Th "Ignore the lust inside you, think of all the other emotions you have towards me, based on them, can you accept me?"

menu:
    "Do I accept?"
    "No.":
        $ thepoints +=-2
        jump noooo
    "Yes.":
        $ thepoints +=1
        jump yeeee

label yeeee:
play music "audio/horse.ogg" fadein 2.0
y sadsmile"I already said I love you, and I mean it with all my heart, might as well show it with more than a kiss, huh?"
q "The stallion smiles brightly for the first time in a long time and grabs your hand firmly."
th "Then let’s get a move on."
scene black with dissolve
y surprised"Lead the- Woah!"
q "The ground disappears from beneath your feet as he picks you up and holds you close."
th "The way? Yeah, I’m on it."
stop sound fadeout 2.0
scene nighttown with dissolve
y ec"Glad you’re as excited as me."
th "Of course I am, after all, only I know the things I’ll do to you."
q "Face redness appears for the hundredth time today."

q "The wind and the hurried, heavy steps of your new partner are the only sounds occupying your ears, those, and the rapid beating of his heart near your ear."
q "He takes you through the illuminated streets until the fated building comes into view."
scene dorm with dissolve
q "You think he’ll let you down, but he kicks the door open and runs up the stairs."
q "Even in front of his own door, he holds you with a hand under your tail using the other to unlock the room."
play music "audio/cicadas.ogg" fadein 2.0 volume 0.7
scene theriumbedroom with dissolve
q "Only inside his bedroom, he finally throws you on the bed."

y smug"I’ve never been manhandled like that before, I...like it."
q "The room is dark, but the natural moonlight casts more than enough light to see all the important parts."
show horse smug3 with moveinleft
th "Where do you want to start, baby?"
y "I think clothes are the main things stopping us."

th "Then what are you waiting for?"
show horse smug3close with dissolve
q "He comes closer grabbing you gently by the waist."
th "I'm all yours."
y pf"Umm, I wish, but I have no idea how to take that off."
show horse smugclose
th "Yeah, fair enough."
hide horse smugclose with moveoutleft

q "He quickly unlocks the pins across his torso and moves on to his pants."

th "Are you gonna follow through?"

y awkward"Oh, sorry, got a bit distracted."
q "You unbuckle your belt and slide off the pants first, then fumble awkwardly with the buttons of the shirt for a minute, all while having your eyes locked to every inch of skin that the stallion undresses as well."
scene black with dissolve
q "Now only the white t-shirt remains, your eyes get covered by the soft fabric and when your vision comes back, you’re greeted by a new, exciting and arousing image."
scene theriumbedroom
show horse naked
with dissolve
q "Both of you are now only in underwear, a single piece of cloth standing in between you and your desires."


y nakedsmug"Looking...amazing over there."

q "Indeed, your mouth is almost salivating looking at his toned, muscular chest, his hard earned abs covered by pristine white fur, the athletic legs of a runner and arms of a fighter."
q "Summoner or Defender? What’s the difference when you have him on your team?"
q "Not to mention the bulge your eyes keep moving towards."

th "And you’re looking even better than I imagined, not that I had high expectations to begin with."

y nakedpf"What a passive-aggressive thing to say…"
y nakedsmug"I kinda like it."

q "Surprisingly, you make the first move this time, seeing him standing there, eating you up with his eyes, you decide to slide down your underwear, revealing your hardening cock beneath."
q "You sit back on the bed taking them off completely, and holding them up with one finger, teasingly."

q "The large bump in the stallion’s cloth gets visibly bigger and he follows through."

th "That was a daring thing to do."
th "Did I finally manage to break out of your shell?"
y "I hope you break more than my shell tonight."
y nakedss"But yes, very much so, thanks a lot for that."
show horse nakedclose with dissolve
th "You haven’t done this with anyone else before, have you, [name]?"

if yessex >=2:
    y nakedss"I...have, twice."
    th "Oh, then excuse me, I took you as a virgin."
    y nakedawkward"In your defense I was one up until yesterday."
    q "He gives you a curious look."
    y "Maybe I shouldn’t have said that."
    th "Heh, don’t worry, I already knew, you’re not as sneaky as you think."
    y nakedss"Of course you knew...I’m not sure if that’s a relief or if I should be worried."

    th "Let’s just say that I’m happy I know you can handle larger things inside you with little to no preparation."
    y nakedsimple"What do you-"
    jump theriumsexstart

elif yessex <=0:
    y nakedawkward"Umm, yeah, I mean, no,  I haven’t done it with anyone."
    th "Then it might be a bit of a problem."
    y "I know, I’m sorry, I’m super inexperienced."
    y "I do own some toys if it means anything, I also practiced my hip movement a lot, I know that’s pretty import-"

    th "No, no [name], your performance will not be an issue."
    th "I’m just afraid you’ll have a hard time handling me."

    y nakedsimple"What do you-"

    jump theriumsexstart



else:
    y nakedss"I...have."
    y "Once."
    th "Aww, I was too late then, would’ve loved to be your first, but it’s probably for the best, at least now I know you might be able to take me."
    y nakedsimple"What do you-"
    jump theriumsexstart



label theriumsexstart:
$ persistent.unlocked_therium = True
stop music fadeout 2.0
play music "audio/dream.ogg" fadein 2.0
scene thesex1 with longdissolve:
    blur 20
scene thesex1 with llongdissolve

q "He slowly slides down his underwear, inch by inch, revealing his massive length until it all springs up in a final show of flair."
q "It takes you...multiple seconds to process what you’re seeing in front of you."
q "Thick, girthy, hard, heavy looking piece of stallion meat, dripping with precum."
q "The size alone made you think it must be some kind of joke, maybe a prank with a hidden dildo in his pants, but those theories are debunked in moments as you watch it throb with anticipation and leak precum."

th "What do you say?"

y nakedblush"I...I-"
y "Fuck...you’re a monster."

th "In more ways than one, I’ve been told that many times."
y "H-how big is it?"

th "Do billionaires count their every penny?"
th "It's long enough to fill you up, stretch you tight. It's thick enough to make you beg for mercy. It's big enough to pleasure you in any way you want and need."
q"His voice is low, almost threatening but seductive."
th "And right now, it's aching to be inside you."

y nakedblush3"Am I really supposed to fit all that?"

th "That’s what I was worried about as well, you decide, you are still the main attraction tonight."
th "But keep in mind, once you say yes...you’re all mine."

q "Your mind gets over the initial shock but keeps on buzzing, out of fear and excitement, can you really say no to that thing?"
q "Your own member is shivering as well, barely keeping in its elation, betraying your needs and wants."

q "At last, as the stallion awaits your response hungrily, you smirk."

y nakedsmug"Bold of you to assume a big dick will turn me away, in fact, it only makes me want you so much more."
q "Of course, nobody is surprised by the slut’s response, except for his partner, perhaps, but he accepts your compromise."

th "Those words make me happy, but I do hope your eyes are as big as your holes for this."
th "Now turn around for me, hands on the bed and relax."
scene thesex3 with longdissolve
y nakedsmug"Yes, sir."
q "You do as instructed, a little embarrassed to be so exposed, even if your legs are not fully spread."
y nakedss"We’re getting straight into action, huh?"
q "The intense heartbeat in your chest warms you up in the dark, yet, you can’t help but tremble as you smile back at him."
th "What a beautiful view."
q "He takes a second to savor this ‘view’, before kneeling down behind you."

q "Your tail coils up as his gentle hands grab your cock and rubs it slowly, before a soft, warm tongue presses against your hole."
scene thesex2 with longdissolve
y nakedhurt2"Oooh, we’re really getting into it fast."
q"The other hand placed on your bare ass cheeks. He massaged them vigorously with that one single hand, spreading them apart to reveal your tight hole for better reach."
q"His tongue darted out, tracing the crack of your ass, teasing the sensitive flesh between your cheeks."

th"Relax, you’re tensing up"
q "He growled, his breath hot against your skin."
y "Sorry, it just feels so warm but so...weird."
th "In a good way?"
y nakedsmug"Very good way."

th "Don’t worry, I’m going to make sure you're ready for me."
q "His tongue circled your tight hole, teasing it mercilessly, before he plunged inside you, his tongue probing deeply into your ass, stretching you open. His fingers take turns to stretch you as well, gently at first, until three whole fingers press against your prostate."
q "You moan with animalistic pleasure as his fingers twist and thrust inside, especially thinking of how much bigger his shaft is than three fingers."
scene thesex3 with longdissolve
q "After another minute of preparation and bliss, he stops, with a last kiss on your cheek he gets up."
q "{i}'This is it'{/i}, you think, {i}'I’m ready for him, I hope.'{/i}"
q "When you feel a tap on your shoulder."
th "Get up."
y nakedsimple"Huh?"
th "What? You don’t think I’ll put it in before you have a taste, right?"
q "He stands proudly in front of you and gestures to get on your knees."
y nakedss"Can’t believe I almost skipped this part."
th"Open your mouth."
scene theriumbedroom2 with longdissolve
show thesex4 with llongdissolve
q "He commanded, his deep voice holding an underlying note of authority. His cock twitched in anticipation, begging to be taken."
q "You place a hand on his thigh and another on the ground, touching your snout to his wet, dripping tip."
q "The smell is enticing but the length was still intimidating."
q "His belly looks so far away from your point of view."
q "After you’re done stalling for time with your sniffing, you finally hold your tongue out and lick around his cock head, before popping it into your mouth."
q "The horse groaned softly, his hips bucking slightly as your warm, wet mouth enveloped the head of his cock. Your tongue swirled around the head, teasing the sensitive flesh, while your hands gripped his thighs for support."
q" The sensation was unlike anything you've ever experienced, mostly because you never experimented with something of this size."
q "You try to go further, but after a few attempts you realize the head is all you can manage, sadly."

th "Something the matter?"
y nakedblow"Ughh-aghum, mhhm."
th "I completely understand, you need a helping hand or two."

y "Hehghi hahg?"
show thesex44 with longdissolve
hide thesex4
"!"
q "A pair of dark blue, floating hands are summoned near your face."
q "One positions itself on your shoulder and one behind your head."
th "Don’t worry, they’re here to make you realize your full potential, I know you can do it."

q "At that moment, the hands begin to push your head and body forward."
q "You protest only for the first inch or two, before realizing that...it does indeed go in easier than you thought."
q "Your jaw relaxes more as the stallion’s cock reaches halfway in, and then-"
show thesex444 with vpunch
q "The hands slam your head against the stallion's fur, his whole length going down your throat."

q "The summoned hands let you relax and adjust to the girth, then even pull out for a deep breath, before pushing back further than before."
q "The pressure in your throat makes you grateful for that breath."
q "Your partner enjoys watching you take it all with his hands on his hips, he’s certainly pleased with your performance, giving you a pet on the head while running his fingers through your hair."
show thesex4444 with llongdissolve
th "You have such beautiful eyes, especially when you look up at me like that, so innocent...just knowing that your whole mouth is filled with my meat makes me want you more."
hide thesex4444 with vpunch
q "The cycle continues, the hands let you breathe again, only to push your snout against the horse’s crotch, but this time with a faster, more even pace, his cock moving in and out of your mouth, the grip of those hands tightening."
q "The sounds of you gagging and choking, as well as the wet slurps filled the room, the louder they get, the more your partner moaned and groaned."
th "That's it, suck me off, you’re doing so good."
q "He growled, his voice filled with desire."
q "For the grand finale, the hands push your head and hold it still at its maximum range, while he slams into your throat one last time, his cock pulsing with his impending release."
q "You’d like to say you’re swallowing every single drop, but it’s not really swallowing when everything is pumped directly down your stomach, is it?"
show thesex4444 with longdissolve
q "As he came, his juices filled your throat, a mix of his cum and your saliva. The only real taste you got was when he pulled out completely, his cock popping free with a soft slurp and the summoned hands disappearing."
q "Almost immediately a coughing fit rushes over you, and your partner kneels down next to you to slap your back."
scene theriumbedroom with longdissolve
show horse nakedclose with longdissolve
stop music fadeout 2.0
th "Heh, you did great, I’m proud of you."

q "You put on a frown when you’re done and look at him disapprovingly."
y nakedbored"..."
th "What? Are you mad about the hands? Sorry, maybe I went a little-"

y nakedsimple"No no, I loved the hands, I loved everything."
th "Then why do you seem upset?"

y nakedpf"Well...I kind of wanted more, like, a lot more."
y nakedbored"Cumming in my mouth wasn’t bad, but I wish it was somewhere else…"

th "Oh."
th "But darling."
show horse nakedclose2 with llongdissolve

q "He holds your head close to his, cum dripping from your chin still."
play music "audio/horse.ogg" fadein 2.0 volume 0.5

th "This is only the beginning, we have the whole night ahead of us."
show lust with dissolve
play sound "audio/heart.mp3" volume 0.5 loop
q "Those words sparked something in you, ignited your lust again, and there’s nothing powerful enough to get it out of you, except for a big, meaty horse cock."
q "And luckily there’s one perfect for the job right here."

show horse nakedclose with dissolve
y nakedsmug"Recovery time?"

th "About two minutes."

y "Amount of seed?"

th "As much as pumped down your throat just now, every time."

y "Fatigue?"

th "Not before yours sets in, that’s a promise."

y nakedsmug"Then what are we waiting for?"
stop sound fadeout 2.0
play sound "audio/sheets.ogg"

scene theriumbedroom2 with llongdissolve:
    blur 15
scene theriumbedroom2 with llongdissolve
show thesex5 with longdissolve
q "You jump back on the bed and resume a similar position to before, face down, ass up and ready."

q "Needless to say, this night will be one to remember…"



q "The stallion’s eyes lit up with pure animalistic desire as he saw your perfect ass presented to him."
q "His massive cock, still coated in a thin film of your saliva and now even fresh, slick cum."
q "He positions it against your tail and resting on your cheek, and with a devilish grin asks."
th "You want it?"
y nakedlust"What kind of question is that?"
th "I just want to hear you say it."
y nakedlust"Y-yes, I do."
th "You want what?"
y "Please fuck me, I want- no, I NEED your cock inside me, Therium!"
th "That’s more like it."
th "Now let’s see if the kitty is as good at taking dick as he is at swallowing it."
q"With a growl of lust, he rubs his shaft against your crack, then his cockhead presses against your tight hole."
show thesex55 with longdissolve

q "He paused for a moment, savoring the anticipation before thrusting forward, his head breaching your tight entrance. You let out a sharp cry of pain mixed with pleasure as he slowly pushes himself deeper into your ass, stretching you wider than ever before."
q "Unlike the blowjob, this time you don’t get the privilege of taking it only halfway, balls deep or nothing."
y nakedlust"Ooh. My. GoOood."

th "That's it, take it all."
q "He growled, his voice husky with desire. He began to thrust in and out of your tight hole, his cockhead rubbing against your sweet spot with each powerful thrust. His hands gripped your hips, digging into your flesh, holding you steady as he claimed you completely."

q"Your eyes roll back in your head and your teeth are clenched enough that it feels like they’ll break."
q "You feel his heavy balls slap against your thighs and your insides being stretched more than any toy ever did so in the past."
y nakedhurt2"C-can you b-be a bit more gentle, p-please?"
q "Your voice shakes together with your body as his hips slam into you."
q "Like waking up from a trance, the horse’s expression softens and his movement slows down by a lot."
th "Sorry, I got a bit carried away, you’re just so fucking hot."
th "You know what?"
show black with llongdissolve
q "He slowly pulls out completely, leaving behind a well lubricated and needy hole."

y nakedsurprised"Hey! I still want it."

th "Heh, just turn around for me."
play sound "audio/sheets.ogg"

y nakedss"Like this?"

th "Yeah, that’s perfect."
show thesex6 with llongdissolve
th "Now I’ll see your pretty face better and know when to slow down, and in this position, it will be harder to fuck you balls deep."
y nakedss"That might be for the best."

q "Soon, most of the horse’s length was back inside you, your moans of pleasure now being right next to his ears, making him wild with lust, a controllable lust this time."
q "Your hole filled again with rhythmic thrusts, which move surprisingly smooth through your tight hole."
q "The night rages on, and with it, the sounds of flesh pounding and moans of pleasure fill the air."
q "Lucky that the apartment is so large, otherwise there would definitely be angry neighbors at the door, or maybe there already are, banging at it almost as hard as the horse’s cock bangs into you, but you won’t hear them against the sounds of rough sex."
scene thesex7 with llongdissolve
q "After some time, he raises his body and holds your legs high."

th "Hey, eyes here buddy, wanna see something hot?"
y nakedlust"I’m seeing and feeling something hot right now."

th "Heh, even hotter than that."
th "Watch."
scene thesex77 with hpunch
q "He points towards your belly, then, with a powerful thrust, fills you up with is cock enough that a bulge forms."
q "After the pathetic squeak you let out, you look at it satisfied."

y nakedblush"H-holy fuck, is that your dick?"
th "What else could it be?"
y nakedblush2"That’s...hot."

th "Told you."

scene thesexx with dissolve

q "He continues the show as you both watch the bump inside you grow larger and smaller with each movement, until finally, his second orgasm comes and your first."
q "You paint your own belly with hot cum while he fills your insides."
y nakedlust"It’s so warm inside me, and so much."
y "I - Ah- never thought this felt so good, I thought it was just- Ah...fun to watch."

th "I’ll take that as a compliment."
th "And an invitation to hurry up the pace."
scene thesexxx with dissolve
y nakedlust"N-no- waAaAAH! Ah! Ah! AAH!"
y "OH GOood! YES!"
q "He was certainly not kidding when he said {i}‘all night’{/i}."
q "Many more positions and climaxes follow through, the lust, and, dare I say, romance is flying in the room."
q "Might also just be the scent of breeding that’s happening as we speak."
q "Hour after hour of restless pounding, a pair more desperate than an infertile couple longing for a child."
scene thesexx with dissolve
q "But at last, this couple slows down."
q "Their breaths heavy, movement sluggish and the stallion’s deep rams are no longer so powerful or uniform."
scene black with llongdissolve
q "And for the first time since you started...you kiss."
scene thesex8 with dissolve
q "Your partner kisses your lips, he kisses your ears, he kisses your neck before biting it."
q "Part of you thought he’s turning you into a vampire, but it’s probably just the delusion from lack of sleep and hours of being fucked."
q "This round is more intimate, the position chosen is more personal and tender and even the sounds are leaving some space for the long awaited peace and quiet."
q "There’s not much moaning or screaming going around when you’ve had a horse cock inside you for so long."
q "With a hearty, violent throb he cums once again inside the poor leopard’s ass, making him throw his head back in satisfaction."
q "The moons are shining brightly through the window, reflecting the light into the puddles of cum on the bed and on their bodies, and even the saliva around and in between their mouths."
q "The night’s cold breeze ruffles the curtains as well as your fur, but the heat of your sins is keeping you warm."
q "With a last, long lasting kiss on the lips, the stallion’s softening cock pulls out from inside him."
q "They both plop on the bed defeated, spooning each other and drifting off to sleep."
q "Should they clean up first? Probably. Did they do it all night? No, but dawn is not far, so I’d give them the credit."
stop music fadeout 3.0
scene black with llongdissolve
q "Over all, they both seem to be happy about this ending, so I am too, even if it hurts."
if from_gallery:
    # Reset the flag so it doesn't affect the normal gameplay flow
    $ from_gallery = False
    jump return_to_gallery
else:
    pass
q "I also think I drifted off from a third party narrator into a more personal space, but hey, the author’s notes are important too, especially when the action is already done."
play music "audio/wind.ogg" fadein 2.0
"..."
scene theriumdream4 with longdissolve
scene CGt14

th "An Academy for hunting Nightfallen."
th "The last place I thought I’d find my place in."

h "So you accept your position?"

th "Heh, sure old man."
th "I love this place more than I ever thought I would."

h "A place to love and someone to love, two halves of a whole, and the meaning of life."
h "You’re one of the lucky ones to have completed half the puzzle already."

th "I have the other half as well already."

h "Oh? Who would that be?"

th "It's not really a person, and haven't even met him yet, but when I do, I’ll never leave his side."
stop music fadeout 2.0

#Final Day!
scene black with longdissolve
scene red with llongdissolve
play music "audio/firstday.ogg" fadein 2.0
Q "The sun shines brightly into your eyes and the birds chirp outside the window."
Q "You wake up from a deep slumber in a moist bed."

y nakedhurt2"Ughh, what time is- wait...moist?"
q "You touch the sheets and throw them off you immediately and run to the bathroom."

y nakedsurprised"EW!"
scene theriumbedroom3 with vpunch
scene shower with llongdissolve
y nakedsurprised"What is that?"
y nakedsimple"Did I…"

un "No, you didn’t pee yourself."
y "Phew...then what?"
un "It’s semen."
y nakedpf"That feels even worse for some reason."
un "You swallowed like a gallon last night, there’s no way it’s worse."
y "You’re...right."
q "Memories of last night flow back and hit you like a truck."
y nakedss"Man, I really did all that, huh? I took him ALL in…"
y "I’m…"
un "A slut?"
y naked"An AWESOME slut."
un "You know what? I like the confidence."
y nakedhurt2"Ow, ow ow, God damn it."
un "It’s hard to walk, huh?"
y "Yeah, who would’ve thought having a ten inch-"
un "It was twelve."
y nakedblush"TWELVE?!"
y "Did you...measure it?"
un "I don’t need to, I have enough experience to figure this stuff out with feel alone."
y nakedbored"And I’m the slut?"
un "Well I’m proud to be one, you’re kind gets embarrassed about it."
y nakedbored"Touche."

y nakedsimple"Now...where is Therium?"
un "Maybe he’s making breakfast?"
y "What time is it?"
un "Clock on the nightstand said eleven thirty."
y nakedsurprised"Almost noon?!"
un "Well, you did have sex until dawn, almost."
y "True, but the battles start at noon, we have to hurry."
scene theriumroom0 with dissolve
q "You run downstairs and find an empty apartment, but the sweet smell of maple syrup tickles your nose."
q "On the table in the main living room you find a stack of fluffy, still warm pancakes, drenched with syrup, butter and berries."
y nakedsimple"I am actually starving...but do I have the time?"
q "You decide to stuff your face with half a pancake you roughly cut with the fork lying near the plate."
q "Near that same plate you notice a piece of paper that you’ve mistaken for a napkin the first time your eyes laid on it."
y "A note perhaps?"
q "You unfold it and it reads:"
th "Apologies [name], I had to run early in the morning for some leader business, I hope you don’t mind a cold bed and cold breakfast-"
y nakedfood"{i}Mmf, the phancakesh are shomewhat warm shtill, but-{/i}"
un squint"Swallow before you talk, God damn, didn’t think I’d have to teach you that."
y naked"{i}*gulp*{/i} ahh, but the bed could’ve used some spare sheets before he left."
th "I’ll wait for you inside the arena, the balcony in front of the announcement tower."
th "And don’t worry about being late, just try to be there before 1PM."
th "I’m going to make all the necessary arrangements so don’t worry about a thing."

y nakedss"That is so sweet of him."
un eyeroll"Sweet as a lemon, that one."
y nakedpf"I wonder what he means by...arrangements."
y nakedsmug"There is just no way we can know."
un bored"It’s probably about the pair battles."
y "No way to know."
un "It’s pretty clear."
y "Not a clue."
un "{i}*sigh*{/i}"
un "Go take a shower, cum stain Joey."
stop music fadeout 2.0
y naked"Yes sir!"

scene black with llongdissolve
jump arenabattletime




label noooo:
    stop music
    play sound "audio/buildup2.mp3" volume 0.4
    show horse shock
    th "Ha…"
    show horse smug2
    th "Hahaha."
    th "Of course."
    Th "Of course not."
    show horse mad
    th "What did I even expect?"
    Q "He attempts to leave, but you anticipated this reaction from him."
    stop sound
    q "You grab him firmly and confidently, your frown deeper than his, which takes him by surprise."
    play music "audio/pianorelax.ogg" fadein 3.0
    Y worried"I do like you a lot."
    y "And I mean a LOT."
    show horse bored
    Y sad"I want to spend more time with you, but there are too many worries on my mind to make such a decision in the middle of the night."
    y "I don’t have TIME for a relationship or even one night stands."
    show horse sadsmile
    q "For the first time, he smiles."
    Q "He smiled before, but not like this."
    Q "This one does not feel flirty, seductive, cold or fake, or sly, or mad."
    Q "It’s a real smile."

    Th "If you managed to say that through a lust rush then, I have to take your word for it."

    y surprised"!"
    Y "How do you-"

    th "Being angry at you is truly...not the way to do this."
    th "You’re right, there is no time to waste with romance or lust."
    th "Goodbye, [name], for real this time."
    hide horse sadsmile with dissolve

    y simple"Good...bye."
    stop music fadeout 2.0
    scene black with llongdissolve
    play music "audio/wind.ogg" fadein 2.0
    "I stayed awake all night, trying to comprehend what he meant."
    "Why did he agree with me so suddenly? How did he know about my Lust Rush?"
    "Scribbles is nowhere to be found in my mind, he must’ve buried himself deep."
    "Even his narration stopped."
    "I have to admit, having to word my own thoughts in my mind again feels a little weird now."
    stop music fadeout 2.0
    "Yet another mystery….why? Where the hell are you Scribbles?"

    "Morning rolls around unexpectedly."
    "When did I even fall asleep? Did I even fall asleep?"
    "It's all kind of a blur."
    "But those battles aren't going to...battle themselves- fight, fight themselves."
    "I can barely thing...think."
    y nakedsad"Well, I better get ready."


    jump arenabattletime2



label arenabattletime:
"Meanwhile..." with llongdissolve
play music "audio/wind.ogg" fadein 2.0
"It is no longer a question of {i}'if'{/i}, just when and how…"
"That leopard will, as foreseen, never leave my mind, which is the worst outcome imaginable."
"Since it happened despite the warnings, I might as well make sure nothing else goes south, which includes taking care of a certain lion."
play sound "audio/knocking.ogg"
h "Come in, Mr. [name2]."
play music "audio/hm1.ogg" fadein 2.0
play sound dooropen
scene hmoffice with dissolve
show headmaster20smile1
h "You are-"
show headmaster20bored with dissolve
h "Here again...{i}*sigh*{/i} Why am I not surprised?"
th "You wanted to meet [name], I heard?"
h "Yes, I had some proposals and future opportunities that both he and his fellow recommended-"
th "I don’t care."
th "Whatever business you have with him, let me assure you, he won’t be your toy."
hide headmaster20bored
show headmaster20smile22
h "Heh."
h "I see."
h "And...if I may ask."
h "What makes you so sure?"
scene black with llongdissolve
th "Because we found a better use for him."
stop music fadeout 2.0

scene hallway with llongdissolve
show cloak with dissolve
play music "audio/dark.ogg" fadein 2.0
nu "Since you said that to him just now..."
nu "I take that you’ve made up your mind?"
th "Not yet."
nu "Really?"
nu "The whole of last night didn’t nail the final verdict into your skull?"
nu "Cause you sure nailed him more than-"
th "ENOUGH!"
th "Why are you so keen to protect him?"
nu "Me? Maybe because I don’t want to die, or let father die."
nu "Why are YOU denying his potential? Jealousy?"
th "Didn’t your daddy tell you to drop that subject and not interfere?"
nu "My father wants results, something you’re very slow in offering."
stop music
play sound "audio/buildup.mp3"
nu "And too emotional going about it, lover boy.{w=0.5}{nw}"
scene black with llongdissolve
th "Like I fucking chose this shit.{w=1.0}{nw}"
th "Mmmph—aaargh…{w=1.5}{nw}"
play sound "audio/shatter.mp3"
show glass with hpunch
th "{size=*2}GRRRAAAH!{/size}{w=2}{nw}"

scene theriumroom0 with llongdissolve
"Back to you..." with llongdissolve
play music "audio/wisp.ogg" fadein 2.0
y surprised"I was NOT expecting the amount of cum in my fur."
y "It really soaked it in good."
un "It was pretty disgusting."
y smug"And a little hot."
un suspicious"Nope, juuust disgusting, and sticky."
y simple"Surprisingly sticky…"
y s"But hey, now I’m fresh, clean and ready to fight."
y "Just to clarify-"
un eyeroll"for the millionth time…"
y "This medallion only works when I touch someone, right?"
un bored"Yes, and think of draining their magic source."
un "It will give you back more power, which in turn will let me be able to cast spells in your stead."
un "Because...you know, you’re fucking useless."
y smug"I’m pretty good at summoning."
un "Except that you don’t have anything to summon."
y simple"Oooooh."
y pf"I just thought of that."
un "Yup."
y ec"Well, in that case, thanks for the help, hopefully my opponents won’t be too strong."
un "Imagine if it’s the wolf and tiger."
y surprised"Aiden and Dallan? No way, they wouldn’t fight together, they’re both too powerful...right?"
un simple"I don’t know, anything possible."
y simple"They also have partners already, so I hope I don't fight any of them...period."
stop music fadeout 2.0
scene black with dissolve
q "The demon inside your head successfully managed to induce a seed of anxiety, for his own amusement."
play music "audio/fight.ogg" fadein 2.0
scene arena2 with dissolve
q "You’re now stepping inside the arena, which is almost filled to the brim with cheering furs and excited faces."
q "And no wonder, since the battles have already begun, you peer into the ring and your voice immediately joins the cheering, as you see two familiar figures fighting side by side with surprising synergy."
y laugh"Wohooo! Go Aiden! Go Tate!"
q "Your voice is certainly drowned among the crowd, but somehow the two managed to spot you."
q "Your presence is not much of a distraction for them, since they seem to be holding on pretty well against the two strangers in front of them."
q "The fight just started, but the ending is already clear."
q "Although both their opponents look like senior students, they do not stand a chance against the duo."
play sound "audio/bell.ogg"
stop music fadeout 2.0
q "Soon, the voice of your wolf friend sounds the conclusion."
d "LOOKS LIKE WE HAVE A VICTOR! IT JUST GOES TO SHOW AGE DOESN’T DICTATE TALENT!"
crowd "{i}*murmurr murmurr*{/i}"
D "N-NOT THAT OUR SENIOR COLLEAGUES AREN’T TALENTED, THEY’RE JUST INFERIOR!"
play sound "audio/gasp.mp3"
crowd "{i}*GASP!*{/i}"
D "I-IN MAGICAL ABILITIES I MEAN!"
d "{i}*sigh*{/i} I need a co-host urgently…"
ch "Did somebody caaaaall?"
h "Oh for God’s sake."
play music "audio/happy20.ogg" fadein 2.0
y sadsmile"Aww, poor Dallan, I doubt he had any ill intent with any comment ever."

t "Yeah, don’t worry, nobody will ever be mad at Dallan."
show cat20smile with moveinleft
y ec"Tate! Aiden! Hi!"
show tiger20bored at left with moveinleft
a "Sup?"
y s"Not much, just coming through, I slept a little longer than I was planning and-"
t "Yeah yeah, you can congratulate and tell us how awesome we were just now."
a "Let him talk for fuck’s sake."

y sadsmile"You really were awesome, pity it ended so soon."
t "Yeah, turns out when my opponent doesn’t know how to cancel my teleportation fights are very easy."
a "The fight was a little unfair, I could’ve taken someone much bigger."
hide cat20smile
show cat20smug
t "Ain’t that right?"
hide cat20smug
show tiger20angryright at left
show cat21scared with hpunch
q "The tiger smacks him."
t "Ouch."
y smug"{size=*0.5}Not as big as me...{/size}"
hide tiger20angryright
show tiger20surprised at left
a "What?{nw}"
y simple"What?{nw}"
hide cat21scared
show cat20simple
hide tiger20surprised
hide tiger20bored
show tiger20simple at left
t "Shoot, what are we doing here still?"
t "We’ll be late!"
a "I thought we’re asking Dallan to come as well?"
t "Eh, I’ll come back for him if things get dire, he might be against our plan anyway."
y simple"What are you up to? Same secret as yesterday?"
hide cat20simple
show cat20smile
t "Yup, would love to tell you, babe, but it’s too dangerous for you."
y confused"Babe?"
hide tiger20simple
show tiger20smile2 at left
a "We will definitely be back to watch your performance [name], don’t worry, we wouldn’t miss it."
y sadsmile"That’s very sweet of you, but I can’t promise it will be super interesting."
t "Yup, that’s a promise from your number one crush, come on lover boy, adventure awaits!"
hide cat20smile
hide cat20simple
show cat20smugclose with vpunch
hide tiger20smile2
show tiger20surprisedblush at left
q "The tiger blushes pink from the first comment, and red with anger after the cat runs by you kissing you on the cheek, a peck, if you may."
hide cat20smugclose with moveoutright
show tiger20angryright at left
hide tiger20surprisedblush
a "H-how DARE YOU?!"
hide tiger20bored
hide tiger20angryright with moveoutright
scene arena2
q "He runs after him while turning his face away."
un simple"Aren’t you going to say anything?"
y bored"I am not even phased at this point."
un bored"Fair enough."

th "Phased by what?"
show horse smug with moveinleft
q "The horse approaches from behind, placing his big hands on your shoulders and squeezing lightly, like a massage."
y s"Oh! Therium! Just, umm, the fights, not even phased by them anymore."
th "Yeah, they used to be much bloodier back in my day."

y pf"How bloody?"

th "Heh, I jest, have you been waiting long?"

y s"I just got here when Aiden and Tate entered the arena, they just left."
th "They seem to really like you."
y "You think so?"

th "Do they know about that thing we did?"


y blush"I-I mean, your performance is certainly something to brag about but I didn’t get to tell them in detail-"
th "The chase...[name], the Nightfallen that chased us."
y pf"Oh…"
y simple"No, I don’t think so, at least they didn’t hear it from me if anything."
th "Good, good."
q "A hint of mischief in his eyes glistens, as if he knew exactly what he was asking."
y pf"Sly dog...horse."
y "I'm pretty sure we already discussed this yesterday."
th "Well, my mind must've slipped that part, oops."

show horse bored with dissolve
q "The smile he was trying to keep through trembling eyes and teeth disappears little by little."
y simple"Is...something wrong?"
th "No, course not."
th "Just a lot on my mind, I suppose."
y s"Is it something I could give advice on?"

th "In your dreams."
y simple"Oh, ok."
th "I mean..."
th "Wish I could tell you all about it, but I can’t."
y s"Important people secrets, got it."

y blush"For now...about last night."

th "Please don’t talk about it here."

y sadsmile"Right, you like your privacy, I won’t bring it up."

th "Thanks..."

y s"In that case, let’s focus on the present. Who do you think will win?"

th "Huh? Win?"

y "In the arena."
show horse simple
th "Oh, that’s still going on, umm-"
q "Four people unfamiliar to you throw wild spells at each other while running chaotically through the sand."
show horse bored
th "Hard to say, does it even matter? It’s not us there."
y s"So? Other people matter too, it’s not like we’re the protagonists here."
th "Aren’t you surprised I said ‘us’, more than anything?"
y sadsmile"I kind of knew already, or at least had a hunch when you said you’d take care of everything."
show horse smug
th "So what do you say? Do you think you’re ready?"
y simple"I don’t know…"
th "You’re gonna have to make up your mind sooner or later."

q "For some reason, you feel his words press against your chest more than they should, their weight heavier than usual."



y "I...think so."
show horse mad
th "You think? That is not good enough, I’m afraid."

th "What if we have to fight Dallan himself next?"
th "What will you do then?"
y "Is he that strong?"
show horse bored
th "I certainly can’t take him down myself."
y s"We could, together."
th "Teamwork won’t solve everything."

y sadsmile"But it does make things easier, doesn’t it?"

th "What’s easy is relying on yourself, then you can’t make mistakes."

y "You can, but then you don’t have someone to blame them on, except yourself…"
y sad"I know you’re probably much much stronger than me, but still, I can be useful."
y sadsmile"And who knows, maybe I’ll surprise you."

th "I hope so."

y s"Even if our opponent is super strong, perhaps a leader, perhaps two leaders, we can at least have a chance at winning."
y "You seem to know for a fact you can’t defeat a leader, so with another person’s help that might just be possible."

th "You know I don’t like relying on others...right?"
y smug"And you know that making a little personal sacrifice for the greater good won’t kill ya, right?"
show horse smug
th "Heh."
th "Lot of funny words you got there, magic boy."
y "I’m good with my tongue."
un "And it was going so well..."
y s"And hey, together we can cover each other’s weaknesses."
show horse bored
th "And what would mine be?"

y smug"Your lack of teamwork."

th "…"
q "He laughs softly."
show horse smug2
th "You silly leopard, you already convinced me a long time ago, but you keep making your life easier and mine harder."
y simple"Yey? Wait, I only convinced you now? Was there a chance we weren’t going to fight together oooor..."
show horse smug
th "Oh, sorry, don’t mind my rambling, we’re going to do a great job out there."

q "That moment, the bell rings, signaling the end of the match finalizing in an anticlimactic tie."
q "The wolf wastes no time and presents the next pair...you and Therium."
stop music fadeout 2.0
y s"Hey, that’s us!"

scene arena with llongdissolve
play music "audio/fight.ogg" fadein 3.0
q "You move out and enter the arena, Therium keeps a few feet in front of you, and a tear seems to form in his eye, something you don’t get to question him about just yet."
d "AGAINST ROSE AND CHELSIE, VICE LEADER AGAINST VICE LEADER, RECOMMENDED STUDENT VERSUS RECOMMENDED STUDENT, DEFENDERS AND SUMMONERS, EQUAL FOOTING SO FAR, LET’S SEE WHO WILL BE VICTORIOUS!"
d "BEST OF LUCK TO BOTH SIDES!"

y s"Oh boy, they really made sure the power scale is as balanced as possible, huh?"

ch "WOOHOO! LET’S GO ROOOOSE!"
ch "[NAME]! HEY [NAME]!"

y awkward"Y-yeah?"

ch "{size=*2}YOU’RE DEAD MEAAAAT!{/size}" with hpunch
ch "{size=*2}WE’RE GONNA CRUSH YOUUUU!{/size}" with hpunch

y "O-ok, please don’t."

r "Chelsie, calm down a lil’."

ch "{size=*2}LOOK AT HER FUCKING AXE, THERIUM, IT’S HUUUUGE!{/size}" with hpunch
r "It is pretty big...aha…"
ch "{size=*3}WE’RE GONNA FUCK YOU UP!{/size}" with hpunch
y "Good luck to you too."
Th "[name]...do me a favor and step back."
y surprised"Huh? But my whole thing kinda requires me to get close to-"
th "Do as I say."
stop music fadeout 2.0
y simple"O-ok."
th "And please, answer me this."
scene theriumwyvern1 with llongdissolve
scene CGt9
play music "audio/wind.ogg" fadein 3.0 volume 0.3
th "Do you promise to give it your all...at all times?"
th "Do you promise to upkeep your responsabilities when push comes to shove?"
y sadsmile"Yeah, that’s kind of the plan, I don’t like losing, especially getting beaten up, or possibly dying."
th "Then I'll ease your burden for today, and maybe you'll do the same for us, in the future."
th "So another step away would be preferable."

q "You do as he asks, noticing the new hope in his voice."
q "Whenever you think you figured him out, he does a one eighty on ya. A vice that would drive most people away, allures you in deeper."
q "{i}'Maybe I’m just as fucked up as him'{/i}, you ponder."
play sound "audio/bell.ogg"
q "The bell rings."

ch "SPIDER ROBOTS, GO! TORPEDO SHOES, LASER GLOVES, GUN!"
ch "ROSE! TAKE OUT THE TWINK BEFORE-"
th "You are all such a pain, hindrances, and nothing more..."
q "From his pouch, a Nightfallen is summoned-"
stop music
play sound "audio/wyvern.mp3"
scene theriumwyvern2 with longdissolve:
    blur 15
scene theriumwyvern2 with llongdissolve
scene CGt10

q "A Savage Fur, the worst of all, a Wyvern, not only that, but the biggest one you’ve ever see."
q "Its coiled wings block out the sun, a colossal shadow looming over its opponents, and a thick, spiky tail protects its master."
q "The head, with piercing eyes visible from the darkness and the smoke, ready to deliver a devastating blow, you can feel the heat of its charging breath even as it’s only charging."
r "{size=*0.5}Before?...{/size}"
ch "I am not paid enough for this shit…"
play sound "audio/wyvern.mp3"
show bluefire with hpunch
q "In the following moment, any and all of the raccoon’s tech toys are melted, the rabbit’s axe: in flames, as for the two girls…"
q "When the flames, smoke and dust finally settle, they’re spotted inside a protective, golden barrier."

play sound "audio/bell.ogg"
q "The bell rings."
scene arena with longdissolve


d "And...with an unnecessary overkill from the Summoner’s part… THEY WIN!"
play sound "audio/cheering.ogg"

q "The crowd erupts in cheering, and you feel a bit embarrassed, mostly because you didn’t get to do anything."
play music "audio/tulip.ogg" fadein 2.0 volume 0.5
Un "Alright...guess we didn’t need that medallion for this part."

y pf"You old, withered son of a bitch…"
q "Y-you’re getting angry, uhmm, might be a good time to retreat."
y angry"YOU MADE ME BEG ON MY KNEES!"
un worried"In my defense you’re still going to need the medallion! It won’t be useless!"
y pf"You better hope not…"
y "I’m not done with you just yet."
stop music fadeout 2.0

q "Your attention is grabbed by your opponents, who rush towards you for a handshake."
play music "audio/happy20.ogg" fadein 2.0
show roseec at right2 with moveinright
r "I had no idea the summoner’s vice leader is that strong."
show chelsiepf at left2 with moveinleft
ch "Me neither…"
hide roseec
show rosesimple at right2
r "Really? Didn’t you know him for years?"
ch "Yeah but...he’s always been- never mind, good match [name], shame we didn’t get to fight more."
y simple"Yeah..."
hide rosesimple
show rosesadsmile at right2
r "It’s also a shame we couldn’t shake hands with that beast of a man."
y "What do you mean? He’s right-"
q "Your partner is much stronger than you thought, yes, but he’s also slippery like a snake."
y "Damn it...I need to talk to him."
y "What the- where did he go?"
q "You look up amongst the crowd-"
show rosesimple at right2
show chelsiesimple at left2
hide roseec
hide chelsiepf
y s"And you see Therium going towards the exit, and you follow him."
un ang"HEY! THAT’S MY LINE!"
y ec"You’re too slow!"
y "Sorry girls! Talk to you later!"
stop music fadeout 2.0
ch "Ok? Bye."
r "..."
r "Who was he talking to?"
ch "Meth?"
r "Could be...sick world we live in."
r "Even this country."
scene arena2 with llongdissolve
play music "audio/crowd.ogg" volume 0.5
q"As you run towards the exit, more and more people try to corner you."
st "Wow! That was such a quick fight compared to the other one!"
st "You summoners are very skilled!"
st "I wanna know more about the vice leader, do you know how he got a Wyvern?"
q "{i}'Maybe ask him, not me?'{/i} you think while trying to get past them."
y angry"Ex-cuse! ME!"
y "Coming through!"
stop music fadeout 2.0
scene park2 with dissolve
q "While following the stallion trying to get away, a peculiar blue butterfly sits on your nose."
play music "audio/horse2.ogg" fadein 2.0 volume 0.5
y butter1"You’re very pretty, but I’m trying my hardest not to smack you right now…"
q "And another one, on your ear."
y butter2"Where are these coming from?"
q "And another one...and another one."
y butter3"Scribbles? A little help please?"
show butterfly with dissolve
q "Your eyes get covered by butterflies…."
y "SCRIBBLES?!"
show butterfly2 with dissolve
q "Your voice is muffled by butterflies…"
y"Mhmmh!"
q "Your consciousness is stolen...by butterflies."
play sound "audio/tension1.mp3"
stop music fadeout 2.0
scene black with llongdissolve
q "The last thing you remember is the back of the stallion, slowly walking away from the arena, head down and tail unmoving."

al "Hey! Hey, are you alright?"
al "I’m calling a medic, hold on."

nu "Oh, you silly boy, he doesn’t know...nobody can wake you from a dream, not a real one, at least."
play music "audio/lullaby.ogg" fadein 2.0 volume 0.5
show cloak with longdissolve
nu "You had to drag him over here like that? In broad daylight?"
nu "Eh, no matter, his fate is in your hands anyway."
nu "Not like we are capable of such a decision."
nu "So, Therium…"
nu "That sure was a spectacle."
nu "Father was looking forward to seeing him perform today, nonetheless."
nu "I take it that you think he’s more than qualified for the task then?"
th "No...he still has a lot to learn."
nu "You deduced that without letting him fight?"
nu "I thought we agreed, no more divination, it is not accurate enough."
nu "We saw that first-hand with your...failure."
th "I didn’t read his future!"
th "But I believe it is not the fighting that’s important."

nuu "He’s right."
th "There you are, finally letting yourself seen?"
nuu "I like stretching my wings sometimes too, you know?"
nuu "I agree with you, Therium."
nuu "Their connection has grown in a strange way in the past few days, it is curious to say the least."
nuu "He is and isn’t ready."
nuu "If you truly believe in him, then I’ll give him another chance."
nuu "But just know...you’ll completely lose him. Is that truly what you want?"
th "Why are you asking me? It’s not like any of this is real…Everything is preordained."
nuu "Aah, number one rule of divination, so you have been peaking! What a naughty boy."
nuu "Curiosity kills the cat, you know that, right?"
th "My curiosity is why the cat is alive."
nuu "That’s why you’re so sour about your relationship."
th "It just isn’t meant to be..."
nuu "Hah, true."
nuu "Still, would’ve been more fun if you didn’t know."
nuu "Oh how I wish I was the one to hold his fate in my claws, but that is not a great idea."
th "So you burdened me with it..."
nuu "Not this again, you know we can't-"
nuu "Oh?"
nuu "Oh, I think he’s waking up. Places everyone, places!"
th "W-wait, you're not actually doing it, are you?"
th "If you do, he-"
th "He won't-"
nuu "Won't love you anymore? Aww, but I thought you don't care."
th "I don't!"
th "But all his progress will be lost for no reason!"
nuu "Oh don't worry, a certain someone will retain the memories for him, he won't lose much."
th "..."
scene black with llongdissolve
nuu "Well, if there are no more interuptions:"

nuu "Ah, you magnificent little freak, wake up again, and show us what you're made of." with longdissolve
nuu "Good luck."
jump thegoodending



label arenabattletime2:
scene black with llongdissolve
"Meanwhile..." with llongdissolve
play music "audio/horse2.ogg" fadein 2.0
"This growing pain in my chest is going to fade, like always."
"It was simply not meant to be."
"He is talentless, not worth the risk..."
"I'm happy I went back to hating him, hate is a much easier emotion."
"{i}Father{/i} would agree."

"I was going to take care of a certain lion, to make sure he doesn't interfere in the future... but there is no future anymore."
scene dorm with longdissolve

y sad"I haven't been narating my own thoughts for a while, and frankly...I don't feel like doing much of an effort at this moment."
"I'm not even sure if I should go to those battles, after all, I was hoping Therium would be my partner, but that might not happen."
"Oh well, I should at least stand on the sidelines and watch Dallan, Aiden and Tate fight."
stop music fadeout 2.0

scene arena2 with dissolve
"The arena is almost filled to the brim with cheering furs and excited faces."
play music "audio/fight.ogg" fadein 2.0
"And no wonder, since the battles have already begun, I peer into the ring and my voice immediately joins the cheering, as I see two familiar figures fighting side by side with surprising synergy."
y "Wohooo! Go Aiden! Go Tate!"
"My voice is certainly drowned among the crowd, but somehow the two managed to spot me."
"My presence is not much of a distraction for them, since they seem to be holding on pretty well against the two strangers in front of them."
"The fight just started, but the ending is already clear."
"Although both their opponents look like senior students, they do not stand a chance against the duo."
"Soon, the voice of your wolf friend sounds the conclusion."
d "LOOKS LIKE WE HAVE A VICTOR! IT JUST GOES TO SHOW AGE DOESN’T DICTATE TALENT!"
crowd "{i}*murmurr murmurr*{/i}"
D "N-NOT THAT OUR SENIOR COLLEAGUES AREN’T TALENTED, THEY’RE JUST INFERIOR!"
play sound "audio/gasp.mp3"
crowd "{i}*GASP!*{/i}"
D "I-IN MAGICAL ABILITIES I MEAN!"
d "{i}*sigh*{/i} I need a co-host urgently…"
ch "Did somebody caaaaall?"
h "Oh for God’s sake."

y sadsmile"Aww, poor Dallan, I doubt he had any ill intent with any comment ever."

t "Yeah, don’t worry, nobody will ever be mad at Dallan."
show cat20smile with moveinleft
y ec"Tate! Aiden! Hi!"
show tiger20bored at left with moveinleft
a "Sup?"
y s"Not much, just coming through, I slept a little longer than I was planning and-"
t "Yeah yeah, you can congratulate and tell us how awesome we were just now."
a "Let him talk for fuck’s sake."

y "You really were awesome, pity it ended so soon."
t "Yeah, turns out when my opponent doesn’t know how to cancel my teleportation fights are very easy."
a "The fight was a little unfair, I could’ve taken someone much bigger."
hide cat20smile
show cat20smug
t "Ain’t that right?"
hide cat20smug
show tiger20angryright at left
show cat21scared with hpunch
q "The tiger smacks him."
t "Ouch."
y smug"{size=*0.5}Not as big as me...{/size}"
hide tiger20angryright
show tiger20surprised at left
a "What?{nw}"
y simple"What?{nw}"
hide cat21scared
show cat20simple
hide tiger20surprised
show tiger20simple at left
t "Shoot, what are we doing here still?"
t "We’ll be late!"
a "I thought we’re asking Dallan to come as well?"
t "Eh, I’ll come back for him if things get dire, he might be against our plan anyway."
y simple"What are you up to? Same secret as yesterday?"
hide cat20simple
show cat20smile
t "Yup, would love to tell you, babe, but it’s too dangerous for you."
y confused"Babe?"
hide tiger20simple
show tiger20smile2 at left
a "We will definitely be back to watch your performance [name], don’t worry, we wouldn’t miss it."
y sadsmile"That’s very sweet of you, but I can’t promise it will be super interesting."
"Or if it will happen at all..."
t "Yup, that’s a promise from your number one crush, come on lover boy, adventure awaits!"
hide cat20smile
hide cat20simple
show cat20smugclose with vpunch
hide tiger20smile2
show tiger20surprisedblush at left
q "The tiger blushes pink from the first comment, and red with anger after the cat runs by you kissing you on the cheek, a peck, if you may."
hide cat20smugclose with moveoutright
show tiger20angryright at left
hide tiger20surprisedblush
a "H-how DARE YOU?!"
hide tiger20bored
hide tiger20angryright with moveoutright
scene arena2
"He runs after him while turning his face away."
y simple"Huh, I am not even phased by that."

th "Phased by what?"
show horse smug with moveinleft

y ec"Oh! Therium! Just, umm, the fights, not even phased by them anymore."
th "Yeah, they used to be much bloodier back in my day."

y pf"How bloody?"

th "I jest, have you been waiting long?"

y simple"I...no, but I was ready to wait even longer, didn't think...never mind."



show horse bored with dissolve
"The smile he was trying to keep through trembling eyes and teeth disappears little by little."
y "Is...something wrong?"
th "No, course not."
th "Just a lot on my mind, I suppose."
y sad"I'm sorry..."
th "..."

"After minutes of awkward, silent minutes later, the bell rings, and Dallan gets ready to announce the next pair."

th "Looks like we're up."
y surprised"W-we? We two?"
th "Don't worry, I'm going to make it quick."
th "We don't have to force ourselves to be around each other."
y simple"That's not..."
y sad"Do we need some kind of strategy?"
th "No need. I don't have much time on my hands, so nobody will stop me."
stop music fadeout 2.0
y simple"Alright?"


play music "audio/fight.ogg" fadein 2.0 volume 0.5

scene arena with llongdissolve
"I move out and enter the arena, Therium keeps a few feet in front of me, and a tear seems to form in his eye, something I don’t get to question him about just yet."
"Dallan announces our names proudly-"
d "AGAINST ROSE AND CHELSIE, VICE LEADER AGAINST VICE LEADER, RECOMMENDED STUDENT VERSUS RECOMMENDED STUDENT, DEFENDERS AND SUMMONERS, EQUAL FOOTING SO FAR, LET’S SEE WHO WILL BE VICTORIOUS!"
d "BEST OF LUCK TO BOTH SIDES!"

y sadsmile"Oh boy, they really made sure the power scale is as balanced as possible, huh?"

ch "WOOHOO! LET’S GO ROOOOSE!"
ch "[NAME]! HEY [NAME]!"

y awkward"Y-yeah?"

ch "{size=*2}YOU’RE DEAD MEAAAAT!{/size}"
ch "WE’RE GONNA CRUSH YOUUUU!"

y "O-ok, please don’t."

r "Chelsie, calm down a lil’."

ch "{size=*2}LOOK AT HER FUCKING AXE, THERIUM, IT’S HUUUUGE!{/size}"
r "It is pretty big...aha…"
ch "{size=*3}WE’RE GONNA FUCK YOU UP!{/size}"
stop music fadeout 2.0
y sadsmile"Good luck to you too."
th "Step back, [name]."
scene theriumwyvern1 with llongdissolve
play music "audio/lullaby.ogg" fadein 2.0 volume 0.5
y simple"You look pretty serious so...I'll do just that."
y "What else do I do? I have to be able to help somehow."
th "Stand on the sideleines and watch what a true summoner should be capable of."
th "Your time to impress me is over."

"I do as he asks, noticing the new venom in his voice."
"Whenever I think I figured him out, he does a one eighty on me."
"Maybe he's really not worth following around..."
play sound "audio/bell.ogg"
"The bell rings."

ch "SPIDER ROBOTS, GO! TORPIDO SHOES, LASER GLOVES, GUN!"
ch "ROSE! TAKE OUT THE TWINK BEFORE-"
th "Useless...everyone useless...everyone but me."
play sound "audio/wyvern.mp3"
scene theriumwyvern2 with dissolve
"A Savage Fur, the worst of all, a Wyvern, not only that, but the biggest one I’ve ever see."
"Its coiled wings block out the sun, a colossal shadow looming over its opponents, and a thick, spiky tail protects its master."
"The head, with piercing eyes visible from the darkness and the smoke, ready to deliver a devastating blow, you can feel the heat of its charging breath even as it’s only charging."
r "B-before?..."
ch "I am not paid enough for this shit…"
play sound "audio/wyvernfire.mp3"
show bluefire with hpunch
"In the following moment, any and all of Chelsie’s tech toys are melted, Rose’s axe: in flames, as for the two girls…"
"When the flames, smoke and dust finally settle, they’re spotted inside a protective, golden barrier."

play sound "audio/bell.ogg"
"The bell rings."
scene arena with llongdissolve
stop music
d "And...with an unnecessary overkill from the Summoner’s part… THEY WIN!"
play music "audio/happy20.ogg" fadein 3.0 volume 0.5
play sound "audio/cheering.ogg"
"The crowd erupts in cheering, and I feel a bit embarrassed, mostly because I didn’t get to do anything."



"My attention is grabbed by my opponents, who rush towards me for a handshake."
show roseec at right2 with moveinright
r "I had no idea the summoner’s vice leader is that strong."
show chelsiepf at left2 with moveinleft
ch "Me neither…"
r "Really? Didn’t you know him for years?"
ch "Yeah but...he’s always been- never mind, good match [name], shame we didn’t get to fight more."
y simple"Yeah..."
r "It’s also a shame we couldn’t shake hands with that beast of a man."
y "What do you mean? He’s right-"
"My partner is much stronger than I thought, yes, but he’s also slippery like a snake."
y bored"Damn it...I need to talk to him."
y surprised"What the- where did he go?"
"I look up amongst the crowd-"
show rosesimple at right
show chelsiesimple at left
hide roseec
hide chelsiepf
y s"And I see Therium going towards the exit, and I follow him."
stop music fadeout 2.0
y ec"Sorry girls! Talk to you later!"
ch "Ok? Bye."
r "..."
r "Who was he talking to?"
ch "Meth?"
r "Could be...sick world we live in."
r "Even this country."
scene arena2 with llongdissolve
play music "audio/crowd.ogg"
"As I run towards the exit, more and more people try to corner me."
st "Wow! That was such a quick fight compared to the other one!"
st "You summoners are very skilled!"
st "I wanna know more about the vice leader, do you know how he got a Wyvern?"
"{i}'Maybe ask him, not me?'{/i} I think while trying to get past them."
y angry"Ex-cuse! ME!"
stop music fadeout 2.0
y "Coming through!"
scene park2 with dissolve
play music "audio/horse2.ogg" fadein 2.0
"While following Therium trying to get away, a peculiar blue butterfly sits on my nose."
y butter1"You’re very pretty, but I’m trying my hardest not to smack you right now…"
"And another one, on my ear."
y butter2"Where are these coming from?"
"And another one...and another one."
y butter3"Scribbles? This would be a great time to show yourself again, need a little help."
stop music
show butterfly with dissolve
"My eyes get covered by butterflies…."
y butter3"SCRIBBLES?!"
show butterfly2 with dissolve
"My voice is muffled by butterflies…"
y "Mhmmh!"
scene black with dissolve
q "Your consciousness is stolen...by butterflies."

q "The last thing you remember is the back of the stallion, slowly walking away from the arena, head down and tail unmoving."
q "I'm...sorry."
al "Hey! Hey, are you alright?"
al "I’m calling a medic, hold on."

nu "Oh, you silly boy, he doesn’t know...nobody can wake you from a dream, not a real one, at least."

if thepoints <=1:
    jump thebadending
elif thepoints >=2 and thepoints <=3:
    jump theneutralending




label thebadending:
$ badhorseending_points +=1
$ thehorse +=1
play music "audio/lullaby.ogg" fadein 2.0 volume 0.5
nu "So, Therium…"
nu "That sure was a spectacle."
nu "Father was looking forward to seeing him perform today."
nu "I take it that you think he’s more than qualified for the task?"
th "No...he’s not ready, and he’ll never be ready."

nu "Are you sure? You’re not saying that because he broke your heart, right?"

th "You’re not giving me enough credit if you think I’d fall for him like that."

nu "If you say so."
nu "Pity, he was growing on me."

nu "I suppose we’re going for the next plan then?"

th "It would seem so…"

nu "Then what are you waiting for? Bring out the False Hydra."
nu "We’re starting from the beginning."
nu "Where did I put that thin- aha!"

nu "Throw him in there, I can’t stand to look at that thing for too long, the hands freak me out."
nu "Ironically, heh."

th "Goodbye [name], as I said before, it would’ve been better if you stayed out of all of this…"
th "I admit, it hurts, a tiny bit, but as soon as your body is gone, I won’t remember you, so did you ever exist in my mind or at all? What are we? if not memories…"
th "That’s something we could’ve talked about, over a cup of tea, if only the circumstances were different."
play sound "audio/growl.mp3"
th"Here boy, lunch."
scene falsehydra with longdissolve
stop music fadeout 2.0
th "I’m sorry...[name]."
th "It's for the sake of the world, you'd understand, right?"
th "...right."
nu "Look at the bright side, we can go back to our original plan."
nu "Well...the original plan B, after your failure, of course."
nu "And your mind will never be lingering on [name] again."
th "I think you're right, but..."
th "Who is...[name]?" with longdissolve
scene black with longdissolve
pause 3.0
play sound "audio/dooropen.ogg"
scene bedroom2 with longdissolve
play music "audio/firstday.ogg" fadein 2.0 volume 0.4
sis "Mom? Why is there so much...guy stuff in the guest room?"
mom "I...I don’t remember."
mom "When was the last time we were here?"

sis "Umm, wasn’t it when dad visited? I'm not sure either."
mom "Oh, that’s right, he probably put all these up, he always liked things a certain way, including decoration."
play sound "audio/drawerslam.mp3"
"{i}*Drawer door slams closed.*{/i}"
mom "What was that? What’s in that drawer?"
sis "Nothing!"
sis "I certainly didn’t learn anything new and gross about dad just now."
mom "Ughh, he’s just incredible..."
mom "Enough, let’s go, we’ll be late to our reservations, I’ll clear out some of his stuff later."
sis "Coming!"
scene black with dissolve
"..."
play sound "audio/crack.mp3"
scene crack1 with hpunch
pause 2.0
scene black with llongdissolve
$ persistent.first_playthrough_completed = True
jump oneofthree

label thegoodending:
    $ goodhorseending_points +=1
    $ thehorse +=1
    scene black with longdissolve
    "..."
    play sound "audio/crack.mp3"
    scene crack1 with hpunch

    "So it begins..."
    $ persistent.first_playthrough_completed = True

    jump oneofthree

label theneutralending:
    $ neutralhorseending_points+=1
    play music "audio/lullaby.ogg" fadein 2.0 volume 0.5
    $ thehorse +=1
    nu "So, Therium…"
    nu "That sure was a spectacle."
    nu "Father was looking forward to seeing him perform today."
    nu "I take it that you think he’s more than qualified for the task?"
    th "No...he still has a lot to learn."
    nu "You deduced that without letting him fight?"
    nu "I thought we agreed, no more divination."
    th "I didn’t read his future."
    th "But he's weak, fragile, lacks talent."
    th "He's simply not feet."
    nu "Oh SPARE me...I told you this will be his response, father."

    nuu "He could be right."
    th "Finally letting yourself seen?"
    nuu "I like stretching my wings sometimes too, you know?"
    nuu "I can't say I truly agree with you Therium."
    nuu "I am afraid you might be letting your emotions run aloof."
    th "We. Need. Someone. Else."
    nuu "..."
    nuu "What kind of parent would I be if I won't give my own son a second chance."
    th "The kind of parent who cares about this world?"
    nu "I agree with father."
    th "You're the one to talk, you're barely a walking corpse, why would you care if the whole world-"
    nuu "ENOUGH!"
    nuu "My decision is final."
    nuu "One more chance."
    nu"At least this time, he'll spend his time with someone worthwhile."
    th "..."



    nuu "Oh, I think he’s waking up. Places everyone, places!"
    scene black with longdissolve
    "..."
    play sound "audio/crack.mp3"
    scene crack1 with hpunch
    "..."
    pause 2.0
    $ persistent.first_playthrough_completed = True

    jump oneofthree
