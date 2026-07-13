label nightfallencamp:
scene black with dissolve

"Still, my friend takes me back to my dorm to get a change of clothes, before visiting the nurse's office, to get patched up."
"The cat takes my hand and holds on tightly, before the usual flash of light covers my vision, but instead of the Nightfallen camp, my dorm room appears in front of us."
"I get it, he's more thoughtful than I am."
stop music fadeout 2.0
"I get a new change of clothing, before visiting the nurse's office as well."
play sound "audio/teleport.ogg"
scene teleport with dissolve
scene gate with dissolve
play music "audio/forestwalk.ogg" fadein 3.0 volume 0.2
"Only then, does he take us both in front of the Nightfallen camp's main gate."


"A masked Nightfallen guarding the gate gets the scare of his life, pointing a spear at us before recognizing who we are and relaxing."
y ec"Hello again."
show cat20smug1 with moveinleft
t "Your prestigious guests have arrived."

ra "[name]! Unnamed cat!"
ra "You came."
show ragnar ec at right with moveinright
show cat20smug1 at left with ease
"Ragnar jumps down from a tree, greeting us with his usual smile."

t "You sure like taking us from behind, don't you?"
ra "Behinds are my area of expertise."

y confused"What were you doing in the tree?"
show ragnar at right
ra "Just came back from a scouting mission."
ra "I decided to stay out of camp specifically to wait for you."
ra "I thought you'd appear on the same path as this morning, so my surprise appearance is technically your fault."

y simple"Before I forget, what does your magic level feel like?"
y "After the battle?"
hide cat20smug1
show cat20smile at left

t "It's fine, I still have a lot of energy in me, don't worry."
ra "Ah, the battle, you mentioned it before."
ra "How did it go?"

if spell>=1:
    hide cat20smile
    show cat20ec at left
    t "We won!"
    y ec"We sure did!"
    jump won
else:
    hide cat20smile
    show cat20ec at left
    t "We won!"
    y simple"N-no we didn-"
    hide cat20ec
    show cat20simple at left
    t "Shhhhh!"
    y pf"Uhmm...yeah, we won."
    jump won
label won:
show ragnar ec at right
hide cat20simple
hide cat20ec
show cat20smile at left
ra "Fantastic, I knew you could do it."
ra "It must've been a very easy fight to be left unharmed after it."

y sadsmile"Oh no, we were very much harmed, but we have good medics."
show ragnar simple at right
ra "Wow, VERY good medics, if your wounds are already healed."
show ragnar at right
ra "Speaking of medics, you have to meet our herbalist as well!"
hide cat20smile
show cat21bored at left
t "Not before I see my friend again."
ra "Certainly."
hide cat21bored
show cat21smile1 at left
ra "How much time do you have on your hands right now?"
y s"We are free for today, actually."
y ec"So let the celebration begin."
show ragnar ec at right
ra "Couldn't say it better myself."
ra "Gigyki sa!"
stop music fadeout 2.0

scene camp1 with llongdissolve
play music "audio/celtic1.ogg" fadein 2.0 volume 0.4

"The Nightfallen guarding the gate opens it for us, revealing the same busy and peaceful landscape we left behind in the morning."
show wilddance with moveinright
"But now, a small crowd surrounds and greets us in their weird language."
"Or threaten, or harass, they could say anything really, not like we understand any of it."
show cat20 with moveinright
hide cat20 with moveoutleft
"The cat pushes past them, unimpressed, and rushes towards the wyvern, which is no longer asleep."
"He is chewing on a thick animal bone, with multiple smaller ones around him."
"Somebody just had a royal meal."
show ragnar at right with moveinright
show wild1 with moveinright
show wild2 at left with moveinleft
y awkward"H-hi everyone."

wf "Kinta'sh va seela?"
y simple"What did he say?"
ra "He's asking if you'll stay for the celebration."

"I nod then bow slowly with my hands tucked down."
y ec"Yes, thank you for having us."
"Fascinated by my gestures, they all emit an intrigued, synchronized murmur of awe, then repeat the bow to me."
show ragnar ec at right
"Ragnar chuckles at us."
ra "We usually only bow at individuals that are higher rank, and guests are always just below the Chief in that regard."
ra "It is certainly interesting for them to see you bow to them first."

y simple"Sorry, I don't know the norms yet."
y pf"Actually, we don't even bow that much in my culture, I'm not sure why I did it."
hide wild1
hide wild2
with moveoutleft

ra "It is alright, as long as you don't kill anybody, we can't blame you for... how do you say, cultural mistakes?"
y smug"Killing someone is universally frowned upon, huh?"

ra "Obviously, now let's regroup with my brother."
y surprised"Your broth- oh, right, I have to remember he's your step sibling."
ra "Honestly, I am very surprised he cares so little about his past, about us, about me."
ra "Do you think he has a stigma against my kind?"
ra "Or perhaps just me in particular?"
y bored"You did kidnap his friend."
y "Wouldn't you be upset if we kidnapped a friend of yours?"
show ragnar sadsmile at right
ra "..."
ra "If I found out you gave a friend of mine a better life, took good care of them and protected them from all danger while worshiping him, I would thank you."

y simple"Then we have different moral agendas."
ra "It is only natural, although hard to understand, we just have to accept these differences."
ra "I did live among your kind for many moons, and that just made me realize how different our morals really are."
"We push past the Nightfallen surrounding me, some of them desperately wanting to touch me, but abstaining, while others gave in to their intrusive thoughts."
"My tail specifically is a big attraction, being the longest and thickest one around."
scene camp3 with dissolve

show cat20smile at left
show ragnar at right
with dissolve
y s"Hey, how is Ki'vaathi doing?"
t "He let me pet him."
show ragnar simple at right
ra "While eating?"
t "Yeah, he growled at first, but calmed down when I went for it."
t "I don't want to bother him anymore, so I'll let him eat in peace."
show ragnar at right
ra "You truly have a strong bond with Ki'vaathi."
t "I suppose."
show cat21sad at left with dissolve
hide cat20smile with dissolve

t "I...I'm sorry."
show ragnar simple at right
ra "What for?"

t "You were right, even though taking him away like that was an asshole move, I have to admit, you're offering him way more than I could ever."
t "If he were with me, he'd have to sleep in worry of predators, eat old, butchered, cheap meat, and stay in constant hiding from hunters..."
hide cat21sad
show cat21sadsmile at left
t "He is happy here."
t "And the fact that I can visit him whenever, it's just the best thing that could've happened to him."

t "I was too blind by anger to see it from the start."
show ragnar tear at right

ra "All is forgiven, I am happy the bad blood between us can stay behind- ah- look, I'm tearing up."
"My heart is fluttering from excitement, Ragnar is almost crying from happiness and the cat is getting a wider smile by the second."
show ragnar sadsmile at right
hide cat21sadsmile
show cat21smile1 at left

y ec"This calls for a group hug!"
show ragnar sadsmile at right2 with ease
show cat21smile1 at center with ease

"I grab the big, hard bicep on my right, and the soft and delicate one from my left, dragging them closer."
"I squeeze them both as close as I can, until the new confusion on their faces disappears."
"They return the hug, cementing the new bond created by the cat's acceptance."

hide cat21smile1
show cat21simple at center

t "I think this is enough."
y "Just one more second."
t "Since when did you become so handsy?"
"Since I get to hold a mostly naked, buff man in my arms."

y smug"You did a one eighty on your opinion, why can't I turn around on my handsiness?"
hide cat21simple
show cat21bored at center

t "Suuure."
show cat21bored at left with ease
show ragnar sadsmile at right with ease

t "Back to the elephant in the camp."
show ragnar simple at right
ra "Where?!"
hide cat21bored
show cat20smile at left
t "It's just a saying, means I want to talk about something important."
ra "Interesting."


t "I would kind of like to know more about your sibling theory, Ragnar."
show ragnar ec at right

ra"Yes!"
ra "About that, lets go answer some questions!"

hide ragnar ec with moveoutleft
hide cat20smile with moveoutleft

"He takes our hands, and for the first time I realize how strong these Nightfallen are."
"Like feathers in the wind, our bodies were swept after him with no chance of resisting."
show bear with moveinright
ra "Ruth, get the lizard to clean up Ki'vaathi's bones."
"He addresses a large bear with only half a mask, who grunts in response."
"So far, he's the biggest around."
"Will have to remember that in case I need to take out the biggest one among them to assert dominance."
show bear at left with ease
show lizard at right with moveinright

"The {i}'lizard'{/i}, apparently being a savage Nightfallen in shackles, who I only see for a couple of seconds before I'm dragged away."

"The bear says something to the lizard in the Wild Fur's language."
"The first thing I notice is that the lizard understands his orders."
"The second is that the bear sounds like he's ashamed or embarrassed to tell him what to do, fidgeting with his fingers and almost whispering those orders."
"The lizard dips his head in understanding and walks away, leaving the bear relieved the interaction is over."

hide bear with moveoutleft
hide lizard with moveoutright
scene black with dissolve
"I would ask some questions if there weren't more important things on my mind right now."



scene forestpath with dissolve
y simple"Where exactly are we going?"

ra "You're going to meet my father, the Chief."
ra "He knows the full story of my brother better than I do."
t "So my supposed stepfather?"
ra "Right."
ra "Plus, obviously the Chief has to greet guests, especially the ones that found Ki'vaathi."
ra "Some thank you's are in order."

y simple"Ermm, sorry if I'm being too judging, but aren't Nightfallen very...lustful and stuff..."
ra "Yes, we are, in fact, the first thing you have to do when entering the Chief's quarters is dropping off your pants and bending over to him, letting him choose his favorite guest to penetrate."
y blush"O-ok, I guess if it's cultural, we can't be rude and refuse, haha."
t "He's joking, [name]."
"Ragnar looks back at me with a smirk."

y "I-I knew that."
y "Obviously."
y "Double joke, that's what I was doing."

ra "Do not worry, I am quite familiar with your kind, so I made sure to pause any traditions that are seen as vulgar for you."
ra "The hardest part was convincing the women to cover up their breasts."
ra "Nobody, including me, could understand why your kind hides them away, but let the males hold theirs free."

t "Meh, I'm gay, I don't know anything about that."
y "I know too little to talk."
y "But I appreciate the thought."

scene camp2 with dissolve
stop music fadeout 3.0

"Soon, the main camp is left behind, as we walk further through the trees, arriving at yet another clearing, with a larger building as the main attraction."
ra "Come, come."
"He excitedly drags us close to the large, wooden door, guarded by two fully masked Nightfallen with spears."
"As soon as they spot Ragnar approaching, they both bow deeply, before one of them knocks on the door."
c "Commence."
"A deep man's voice, with an accent similar to Ragnar gives us permission to enter, then the other guard opens the door with an inviting gesture."
play music "audio/chief.ogg" fadeout 3.0 volume 0.2
scene chiefoffice with llongdissolve
"We step inside warily but curiously."
"The interior is well illuminated by the many glassless windows, with shadows cast by the few makeshift bamboo blinds."
"The main room is spacious and empty, save for the few cabinets and a large table in the middle, with chairs all around and a throne facing the door, on top of which a Nightfallen is sitting."
"He lets go of a piece of charcoal he's been using, dusts his paws off, then rises up to reveal a monster of a man."
show chief with longdissolve
"This Nightfallen makes Dallan look like a child, especially with that excuse of a loincloth, that I would argue makes his overall demeanor much more suggestive than being simply naked."
"He holds a confident and imposing stance, eyeing us carefully through his skull mask, even with no eye holes, but I'm sure there is an explanation for that."
"His super revealing 'clothes' don't make it any easier to look directly at him."
show ragnar bow at right with moveinright

ra "Father."
c "Ragnar."
"Ragnar bows, while the Chief gives a curt nod."
c "Are these Ki'vaathi's caretakers?"
show cat21simple at left with moveinleft
show ragnar at right
ra "Yes, this is [name], and this is..."
c "..."
show chief ec
c "You have finally returned home."

t "Yeeeah."
t "Just a heads up, I don't remember anything or anyone here, especially not you, so if we could keep this less personal and more informative, that would be great."

y pf"{i}*Cough Cough*{/i}"
t "Oh, right."
hide cat21simple
show cat21bow at left
"We both bow to the Chief, since as Ragnar said, our importance here is below the Chief."
c "Heh, I appreciate the thought."
c "I wasn't going to demand our ways be followed down to greetings, but I see you already made a point to impress me, and it is working."
c "Rise up, children."
hide cat21bow
show cat21simple at left
show chief

c "I understand this must be complicated for you, so sudden too."
c "Ragnar told me all about the two of you, and it would be my pleasure to bring back those lost memories of your childhood."
hide cat21simple
show cat21smile1 at left
c "But first, I want to focus on the present."
c "You, [name], was it?"
y simple"Yes sir."
c "As a stranger to our tribe, you didn't have to show us kindness, but here you are."
c "We want to thank you, specifically, for Ki'vaathi's safety."
c "And, as my stepson's mate, we will-"
y blush2"What?"
hide cat21smile1
show cat21simple at left

t "What?"
y blush"W-we're not, uhm, 'mates'."
show chief simple
show ragnar simple at right
"The Chief's looks at Ragnar confused."

ra "That's my fault."
show ragnar ec at right
ra "My apologies, you two reminded me so much of my mate and I, that I must've gotten confused and jumped to conclusions."
c"Just comrades then?"
y awkward"Yeah, you can say that."

show chief ec

"He grins subtly."

show ragnar at right

c "Now, as you might know, if my son didn't get confused about delivering this information as well, we're holding a celebration."
c "The preparations are already ongoing, you just lay back and relax, our home is your home."

y ec"Thank you sir, we are already feeling very welcomed."

y s"I am actually very curious to find out more about your lifestyle."
y "I hope my presence and curiosity won't bother anyone."

c "On the contrary, you were the talk of the tribe the whole day, everyone wants a piece of you."
y pf "Literally or metaphorically?"
show chief simple

c "Meta-?"

ra "I believe it means using words to talk about one thing, but meaning something else."

show chief

c "Ah, I understand."
c "All of these words in this intriguing language."

c "So, family history time."
c "Where shall we start?"
"So literally oor...."

ra "The beginning would be preferable."

t "Wait."
hide cat21simple
show cat20sadsmile at left
t "Before you begin..."
t "[name]?"
t "Do you mind if I listen alone?"

y surprised"What? But why?"

t "I want to form my own thoughts, opinions and conclusions about this whole thing."
t "With you here, I'm afraid I'll think too much with my heart and not enough with my brain."

y bored"Are you saying I'm making you stupider?"
t "More like emotional and irrational."

"I contemplate for a second."
"I do understand his point, this is obviously none of my business in the end."
"He probably doesn't want me to convince him whether or not the story is real, or judge him in any way."
"All I can do is show my support to this part of his life without intervening."
y sadsmile"Alright, if that's what you want."
t "Thank-"
hide cat20sadsmile
show cat20simple at left
y determined"BUT!"
y "If your conclusion is a positive one in the end, then I'm going to want {b}ALL{/b} the details."
y "And I won't let you get away with your usual 'everyone has their secrets' bs."
"He looks a bit surprised, like I made a very bold move, but ultimately, he chuckles."
hide cat20simple
show cat20ec at left
t "Of course!"
t "Why would I hide a happy story from you?"
hide cat20ec
show cat20smile at left
t "I'm going to brag about this for years if it's the case."

"I extend my arm for a fist bump, which he immediately returns."

hide cat20smug
show cat20smug at left

t "See ya at the celebration, fatherless leopard."
y smug"I'll save you a spot, twice adopted cat."

show chief
c "Wonderful, in that case, we'll have a one on one meeting."
c "Ragnar?"

show ragnar simple at right

ra "Huh? You want me to leave?"
ra "I was kind of curious to hear everything as well."
ra "I only know vague bits and pieces."

c "You're not going to push our guest out into unfamiliar territory alone, are you?"

show ragnar sadsmile at right

ra "Ah, you're right I forgot to introduce him to Eureka or Ruth."
ra "No matter, we'll have our own fun and write our own story."
show ragnar at right
ra "Come on, [name]."
ra "Time to satisfy that thirst for knowledge of yours."
stop music fadeout 3.0
hide ragnar with moveoutright

y ec"Right behind you."

scene camp2 with llongdissolve
play music "audio/celtic1.ogg" volume 0.5

"I follow my guide outside, forgetting how bright the sun can be when not obscured by walls and blinds."


"Ragnar slides his hand in mine as we step away from the Chief's hut, nonchalantly, so naturally that I can't find reasons or time to complain."
"He takes me by the pond, towards a narrow path that goes to another part of the camp."
scene flowers2 with longdissolve
"This area is deeper into the woods, the shadows enveloping most of the festive decorations already places all around."
"Flowers, totems, wooden statues and more, the main attraction being a huge round table set around a pillar identical to the one the wyvern sits under."

"Sweet and savory aromas hit my nose as we approach, smoke rising from inside a couple of open tents, as well as from campfires that slowly roast meat and cook stews, or soups, or whatever you cook in a big pot."

"All this curiosity made me forget to even ask where he's taking me, but that question is answered once he lets go of my hand, and an intriguing figure makes its way out of one of the huts."
"A tall and lithe Nightfallen emerges, locks eyes with us and hurries our way."

"Ragnar's eyes sparkle with happiness, and perhaps other personal emotions as well."
show ragnar ec at right2 with moveinright
ra "Eureka!"
show eureka at left2 with moveinleft
"Ah, so that's her."
"Now that she's closer, I can offer exposition about her appearance to myself, for no reason in particular, like I always do."
"She seems to be a feline, a lynx, to be more precise, although I'm not sure how related to animal species Nightfallen can be."
"Large, piercing eyes and garments that, for once, are covering more than ten percent of her body."

show eureka bored at left2
eu "Look who remembered to visit me."
eu "Finally done with your self assigned missions?"
show ragnar sadsmile at right2
ra "I'm sorry, Ki'vaathi's situation took me away for a while, you know? The same reason you've been stuck in camp cooking, decorating and your...medicine stuff."

show eureka sadsmile at left2
eu "As long as you remember our deal, you can forget about me as much as you want."
show ragnar smug at right2
ra "How can I forget, the more time I spend away from you, the wilder our reunion nights are."



show ragnar smug at left4 with ease

"He embraces her playfully, trying to kiss her neck while she holds back laughter."
eu "S-stop it."
eu "Those are the conditions YOU made up."
eu "I'm just thankful that the better you do your job, the more safe Ki'vaathi will be."
eu "Speaking of..."

show ragnar at right2 with ease
show eureka bow at left2 with dissolve


"She pushes past Ragnar and stops before me, bowing deeply."

eu "The white leopard."
eu "You must be [name]."

y ec"I am, it's nice to meet you."

show eureka at left2 with dissolve

eu "I heard so much about you, through third party mouths, since Ragnar simply doesn't have time for me."
show ragnar sadsmile at right2
show ragnar sadsmile at left3 with ease
"He hugs her again, apologetically."
show ragnar sadsmile at right2 with ease
y blush"I take it you're the mate he's been talking about."
show eureka bored at left2
eu "You're doing that again?"
eu "I told you we can't be mates."
eu "It simply makes no sense."
ra "I know, I just like the idea."

show eureka at left2

eu "So no, to answer your question, we're not."
eu "Being {i}'mates'{/i} is just a title for male and female couples."
eu "We are simply partners."

show eureka simple at left2
show ragnar simple at right2

"I give myself a nice, fat facepalm after the realization hit."
eu "Is something wrong?"
y awkward"Sorry, I just kind of assumed you were female..."
eu "Based on...appearance?"
y "Y-yes?"
show eureka ec at left2
show ragnar ec at right2
"He turns to Ragnar, both of them chuckling."
eu "Do I present myself as female?"
ra "Well, you do have the child bearing hips, I can see how that would be misleading."
show eureka sadsmile at left2 zorder 2
show ragnar smug at right2
show ragnar smug at left4 zorder 1 with ease
"Eureka turns around and checks his behind, while Ragnar pokes it and grabs his lumps with both hands."
ra "And the amount of seed you can hold is just so-"
show ragnar smug at right2 with ease
show eureka blush at left2
eu "Ragnar!"
eu "That's enough, not in front of our guest, you know how shy they are with these things."
ra "I'm just being honest, don't tell me you're not trying even a little bit to be more eye catching today."
ra "You don't usually roll up your sleeves."
show eureka blush2 at left2
"Eureka blushes and looks away, caught in hypocrisy."
"Now that I think about it, his voice should've been a giveaway from the start, although soft and soothing, it still has a more masculine, deeper tone to it."

y sadsmile"Actually, I don't mind your ways."
y "Or how should I put it better..."
y "It would bother me more if I knew you don't feel at home just because of my presence here."
y s"Besides, you'd be surprised how similar the academy is to this place, when it comes to lewd stuff."

ra "Are you saying you want to be more included?"
show eureka at left2
eu "He's saying he wants to FEEL more included."
show ragnar at right2
ra "Well that can be arranged."
ra "I think the first step would be to get more accustomed to the camp."
show eureka smug at left2
eu "Yes, that's why {b}I'll{/b} take it from here."
show ragnar smug at right2
ra "What? You think I don't know my own camp well enough to be a guide?"
eu "You have to prepare the music and make sure the table is set for when we come back."

ra "Come back?"
ra "You're already stealing [name] away from me?"
show eureka close at left2
"Eureka sticks to me with both arms wrapped around one of mine, looking at Ragnar with a sly gaze."
eu "It's my turn for a while."
eu "Besides, I've been working my ass off the whole day, while you were playing in the trees."
ra "That is...fair enough."
ra "See you in a little bit."

eu "Come, let us gather everyone from the main camp."
stop music fadeout 3.0
hide eureka close with moveoutleft
scene black with llongdissolve
"{i}Meanwhile...{/i}" with dissolve
play music "audio/chief.ogg" fadein 2.0 volume 0.3
scene chiefoffice with llongdissolve
show cat20simple at left2
show chief at right2
with dissolve
c "What do you think so far?"
t "I had NO idea Nightfallen can cast magic."
c "It is much, much weaker than what you and your people can do."
c "Ragnar is more talented than me, but I know all the spells I need to know to protect my tribe."
c "What about your backstory?"
t "It is definitely believable, and it makes a lot of sense."
t "Mr. Sebil said I came from the forest...never went into details."
hide cat20simple
show cat20sad at left2
t "Still...why would I run away in the first place?"
t "And why don't I remember anything? I was five!"
t "Kids remember things since they turn three..."
show chief simple at right2
c "I could not tell you."
c "Soon after, Ragnar started his journey as well...making me lose two cubs in such a short period...and a mate."
t "So...what happened to my stepmom?"
c "She was killed by hunters one unfortunate winter night."
c "The prey and recources around camp were scarce, so she decided to go further, towards a city populated by your kind, despite my warnings."
c "Only six moons after we found you."
hide cat20sad
show cat21sad at left2
t "I am...sorry."
c "It is not your fault."
c "I always considered you part of us, so I can't hold a grudge against you."
c "A lot more of our tribe mates suffered the same fate along the moons."
c "That is why I want Ki'vaathi to grow strong...and make sure nothing like that ever happens again."
t "At least it is now illegal to hunt...you."
c "..."
c "Yes, yes, it's good news."
show chief at right2
stop music fadeout 3.0
c "Let's go back to happy memories."
c "Now, do you want to know about the name we've chose for you back then?"
hide cat21sad
show cat20ec at left2
t "Hell yeah!"
scene black with longdissolve
"{i}Back to you...{/i}" with dissolve
play music "audio/celtic2.ogg" fadein 3.0 volume 0.5

scene forestpath with dissolve

"Today I've been dragged along a lot by many people, and Eureka is no exception, once again, I'm surprised by the strength he has being a Nightfallen."
"His arms are definitely not thicker than mine...It's not fair."

"More bushes and low tree branches hit my face as we walk back on the narrow path."

eu "It sounds like the celebration has begun in these parts."

scene camp5 with longdissolve

"Indeed, the quiet, peaceful atmosphere of the main camp turned to excitement and laughter all around."
"Nightfallen playing on improvised drums and singing in their language with high pitched voices."
"The unnaturally tall trees surrounding the camp give enough shade that you might mistake the time of day for evening."
"The somewhat obscure place is being illuminated more by fire than sun."
"Fire made by torches, campfires, but also a huge pyre in the middle of the camp, where the wyvern used to reside."

y surprised"Why is Ki'vaathi's place burning?"
y "Is he okay?"
show eureka sadsmile at left with moveinleft

eu "Agh, I keep failing to provide simple information, thinking it is common knowledge."
eu "You see, we are supposed to prepare a new place for Ki'vaathi to sleep on every day while he is in his growing stage."
eu "After he awakes from his long, daily slumber, we burn the offerings, believing that this way, it will burn his earthly attachments, and grow faster."
y worried"This is all so confusing."
eu "I would be happy to answer any questions you have, just perhaps later."
eu "For now, let me show you the rest of our camp."
eu "I really want to meet your friend and Ki'vaathi's saviour, but I'm assuming the Chief must need him a little longer."
scene camp4 with dissolve
"I follow Eureka again through different parts of this so called camp."
"Most of it is empty, since people are celebrating around the pyre already."
"He shows me where food is stored, the bathrooms with impressive sewage systems, and the trading huts."
show eureka at center with moveinleft
eu "You can help yourself with any food, cloth or people you need, anyone would be happy to provide our guests with anything."
y confused"'People'?"
show eureka ec
eu "Yes, if you need lust release, just enter one of those barracks and somebody will be with you shortly."
eu "You can then turn them away if their bodies are not to your liking, or-"
y blush2"W-wait wait, j-just like that?"
show eureka
eu "Why yes."
eu "As I said, it would be an honour for anyone."
"Looking around, the few Nightfallen still around throw glances in my direction, as if waiting for the moment I step in said barracks."
y awkward"I-I'll pass for now."
eu "As you wish, in that case, let's move on."
hide eureka with moveoutleft
"We walk past his medicine hut, of which Eureka is very proud of."
eu "Nobody gets sick with me around."
"After a minute or two of walking, and after a couple of history lessons about the camp's walls, I realize he reminds me a lot of a certain cat I know..."
"A little surprise encounter makes him get quiet and stop in place."
show eureka simple at left2 with moveinleft
show lizard at right2 with moveinright
"The lizard from earlier is done with his task given by the bear."
"He looks at me with an intense gaze, before shaking his head and turning to eureka."
"He seems to be looking for his next order."
show eureka simple at left with ease
eu "Uhm, Kuli stu'h guru?"
"Eureka looks uncomfortable with him around."
show lizard at right with ease
"He dips his head and walks away slowly, turning his head towards me one last time."
hide lizard with moveoutright
eu "Sorry about that."
eu "We should go back, we don't want to miss your friend's arrival."
stop music fadeout 2.0
"I'm keeping my mouth shut about the lizard for now, since nobody is in a hurry to explain his presence to me."
play music "audio/celtic3.ogg" fadein 3.0 volume 0.5

scene camp5 with longdissolve
show eureka ec at left
eu "{i}*gasp*{/i}"
eu "Look, it's your partner, the other savior of Ki'vaathi."
show eureka sadsmile at left
eu "I want to make a good first impression so badly, what is his name?"
eu "Do you mind introducing me?"
y ec"Course not, come on, I bet he'll like you, he likes cheerful and happy people."
hide eureka sadsmile with moveoutleft

show wilddance zorder 2 with moveinright

"It's proving a little hard to get to him, a group of Wild Furs dancing around the fire, blocking our way with unpredictable movements."
"We get to see the wyvern, safe and sound, following a large bear around, who's name I believe was Ruth."
show ruthtate zorder 1 with moveinleft
"My cat friend atop his shoulders, any kind of worry, doubt or anger completely gone from his face, replaced by the cheerfulness he was originally named after: Tate..."
"I miss him."
"The wyvern is desperately trying to fly its way in his arms, like a puppy begging for attention, but his pitiful wings are not developed enough."
"Yells of encouragement are still being thrown at him from Nightfallen all around."
y "His meeting with the Chief must've been a success then."
eu "Should we perhaps not bother them?"

"At that moment, the cat's eyes target us like arrows as we stand at the edge of the crowd that is just getting bigger and bigger."
t "Ruth! Taki'ki!"
hide ruthtate with moveoutleft
"He points towards us, and the bear with the cat on his shoulders, who towers over everyone else, steps through towards us."
"Obviously, being the life of the gathering here, and the ones Ki'vaathi follows, most Nightfallen follow them, bringing the deafening voices along."

show ruthtate zorder 3 with moveinleft

y ec"Hey!"
y "Look who is feeling much better."
y "You even learned some of their language already?"

t "Yep!"
t "The Chief told me so many things in surprising detail, it's hard not to believe him."
t "Get this, apparently, my real name, or at least the name he gave me when they found me, is {b}Ku'sani{/b}, which means something like {i}'The one that does it'{/i}."
t "Not sure what that really means, but it sounds like I actually have a purpose now."
y s"That's great, is that the name you'll use from now on?"
t "Yeah, do you like it?"
y smug"It's interesting, much better than {i}Tartarus{/i} in any case."
t "Don't even remind me."
ku "From now on, refer to me by Ku'sani please."
y s"If that's what you wish."
"At least now I have a name to adress him by."
ku "And this is Ruth! You saw him before."
y ec "Sure did, can't forget that towering body."
"He grunts satisfied in response."
ku "He was apparently my caretaker, and the Chief's left hand! Ragnar's the right, of course."
show eureka sadsmile at left5 zorder 3 with moveinleft

eu "{i}*cough cough*{/i}"
y "Oh, Ku'sani, this is Eureka, Ragnar's partner and my guide for today."

show eureka at left5
show eureka at left with ease

ku "I heard your name before, Ruth here can't stop talking about you."
ru "Eureka pretty."

y smug"Aww he has a crush."

show ruthtate smug

ku "Actually, he has a crush on you [name]."
y blush2"Me?"
show ruthtate smugblush
ku "He just loooooves you~"
"Hearing the word {i}'love'{/i}, Ruth gets flustered, panicked even, immediately getting red beneath the mask."
ru "K-ku'sani, n-no, not true."
ku "Yeaaah, he does, he's been eyeing you as soon as we stepped through the gate."
ru "I-I danger! I look for danger then."
ku "Yeah, because these five feet tall kitties are suuuch a danger to you, big boy."
ru "Ruth... like little [name], only little...little love."
"Don't judge a book by its cover, because apparently this huge, intimidating Nightfallen is actually just a big teddy bear, letting a cat five times smaller in mass play with his ears, accessories and even squeeze his muscles jokingly."
"I might need some help in this foreign social interaction."
"I squat down and turn around, signaling to Eureka to do the same."
show eureka close2 at left with dissolve
y pf"psst, Eureka, how do you respond to confessions around here?"
eu "Usually you go to the breeding hut and see how you both like it."
eu "If you're both satisfied in the end, you move on to be partners, if not, you can try again later or go see other furs."
y "Is there something closer to the way my culture does it?"
eu "You... can claim you're sick, but I doubt it would work."
y bored"Very helpful."
eu "I'm sorry!"
eu "It's quite unheard of to refuse a public invitation like that."
eu "Look, I'll tell him you're just not interested and you go sit down somewhere and-"
y "It's ok, I'll think of something myself."
show eureka at left with dissolve
show ruthtate simple
ku "What are you two whispering there about?"
ku "You're making Ruth feel anxious."
"The crowd around us are now making less noise as they are caught up to the situation."
show ruthtate smug
"Ku'sani has a stupid grin on his face, obviously enjoying watching introverts suffer."

y awkward"Ermm, Ruth."
y pf"Me..uh, you?"
y "You big, strong."
y "Grrrr."
"I flex my arms, and I believe Ruth takes these words as compliments."
y simple"Me?"
y worried"Me weaaak, me little."
ru "Yes, little partner, big partner, like Eureka Ragnar."
show eureka sadsmile at left
y awkward"No no no, Eureka strong."
y "Very very strong."
y "Me?"
y "Me nerd."
show ruthtate simple
ru "Nerd?"
y simple"Erm, weak like female."
ku "That's sexist, [name]."
show ruthtate smug
show ruthtate smug at right with move
ru "Sex? Yes, this way."
y blush2"NO!"
y "No no no, that's not what I meant."

ku "Oh you awkward, hot, bitch."
y blush"Thanks?"
show ruthtate smug at center with ease
ku "Here, I'll help you."
ku "Ruth, shu'shk [name] twerp stu."
show ruthtate smug2
ru "Ah, twerp..."
"Everyone listening seemed disappointed, almost as much as Ruth."
y blush2"What?"
y "Eureka, what did he say?"
eu "It means you're already taken."
y bored"Of course, the good ol' {i}'I have a boyfriend'{/i} excuse, how did I forget about it?"
show eureka ec at left

eu "Let's change the subject."
y "Please."
eu "How do you find our camp so far, Ku'sani?"
show ruthtate
ku "It's awesome!"
ku "It's like living in my tent, but with a community and at a larger scale."
ku "I got like...twenty hookups lined up, but I'm gonna have to deny them all because I only have eyes for one person."
y blush"Awww."
show ruthtate down
"He looks lovingly at Ki'vaathi biting at someone's tail."
show eureka sadsmile at left
eu "Awwwww."
y bored"ok..."

y simple"Well, me and Eureka are actually here to tell you that the feast is in preparation, so you should all get ready soon."
show ruthtate
ku "Oh man, I'm starving actually, we haven't eaten anything all day, have we?"
ku "Just please tell me you don't serve fish here."
eu "A large variety of dishes in our culture requires we use fish to-"
show ruthtate bored
ku "No fish."
show eureka simple at left
eu "But we have-"

ku "No. Fish."

show eureka sadsmile at left
eu "No fish...got it."

y bored"You can't just tell them to not serve their hard work because you don't like it."
ku "Alright, fine, just don't put it on my side of the table."
eu "Do you have any meal preferences, [name]?"
y pf"No, because I'm not a spoiled little brat."
ku "Hmph."
show eureka at left
eu "Understood."
show eureka at left5 with ease
"He whispers a couple of words to a random fur who books it towards the narrow path."
show eureka simple at left5
show eureka simple at left with ease

show ruthtate simple
stop music fadeout 2.0

ku "Something is wrong..."
"Deathly silence follows that statement from every Nightfallen within earshot, apparently even the ones that don't speak English know that tone of voice."
"They wait and listen to the cat."
show ruthtate
show eureka at left
play music "audio/celtic3.ogg" fadein 3.0 volume 0.6
ku "The MUSIC isn't playing loud enough! LUK'SA TURNI MUSA!"
play sound "audio/cheering2.ogg" volume 0.2

"Of course..."
"The drums, now accompanied by other instruments as well, start playing a joyful tune, and everybody's feet catch fire."
"Metaphorically."
ku "Hey, [name], how old are you?"
y confused"Huh? Why?"
ku "Just tell me."
y "Nineteen? You know that."
show ruthtate smug
ku "Are you sure?"
ku "I thought it was more like ninety, judging by your stiff, unmoving body."
show ruthtate
ku "Come ooon, move those juicy hips!"
y bored"You're the one talking, just standing on Ruth's shoulders like that, all you're doing is throw your hands in the air."
show ruthtate smug
ku "Pff, at least I have a pair to dance with."
ku "Eureka, do you dance?"
show eureka blush at left
eu "Only if I have a pair."
"He glances at me, shuffling his feet and batting his eyelashes."
y bored"{i}*sigh*{/i}"
y "I guess I didn't come here {i}NOT{/i} to have fun."
y smug"Would you give me the honor of hurling your limbs around in sync with mine?"
eu "It would be my pleasure."
show ruthtate
ku "WOOHOOO!"
hide eureka blush
hide ruthtate
with dissolve
"I would like to say I danced like a professional, that my moves were unmatched, but something even better happened."
"It might be hard to believe, but secluded wild people don't have the same standards we have for dancing, nor the popular pop or electro music we're so used to, so I got away with acting like an unpredictable hurricane in the middle of the crowd, with Eureka adding his own moves."
"At one point, Ku'sani turned around on top of Ruth's shoulders, holding tight with his legs around his head, while he spun him around at high speed."
"It was a little weird seeing my friend stick his whole ass and bulge in Ruth's face, but hey, they were having fun, and nothing sexual came out of it, so I shut my mouth."
"Twenty minutes of energized movements around the fire later, I was met with damp, sweaty clothes."
"Eureka makes way for us to get out of the crowd, and we settle on watching the others continue to mess around."
play music "audio/celtic3.ogg" fadein 3.0 volume 0.2
scene camp6 with longdissolve


show eureka ec with moveinleft
eu "That was fun."
y tired"Yeah, too bad I don't have the stamina, how do you do it?"
eu "Living in the wilderness might have something to do with it."
y "Of course, physical activity... something I avoided all my life."
show eureka
eu "You dance really well."
y simple"You think so? I literally fell down twice."
show eureka simple
eu "Were you not heroically jumping in front of Ki'vaathi so he doesn't throw himself into the pyre?"
y pf"...nope."
eu "ah."
show eureka
eu "Your falls still stopped him from doing so, which means that in my eyes, you're a masterful dancer."
y sadsmile"You're gonna make me blush."
eu "Did I not already? My...I'm getting old then."
y surprised"No, don't say that, you're still hot, I-I mean- young."
y pf"I think..."
eu "Why thank you."
"Change the subject change the subject change the subject."
"Thankfully, he changes it for me, so we don't dwell on awkward silence."
show eureka sadsmile
eu "Your clothes are...wet."
y simple"yeah, low stamina comes with a price."
eu "Would you like to change them? We can put them up to dry in the sun."
y "I didn't bring a spare, and I don't want to make my friend teleport me all the way back."
y "So I'll endure it."
show eureka
eu "Didn't you say before you want to be more included?"
eu "Why don't we go find you a little something to cover up while somebody washes and dries your clothes?"
y pf"Hmmm, alright, I'm into it."
show eureka ec
stop music fadeout 2.0
eu "Fantastic, come with me."
hide eureka ec with moveoutright
play music "audio/littlehappy.ogg" fadein 2.0 volume 0.3
scene camp4 with dissolve
"We avoid the big crowd of loud furs and walk across the camp, following the lines of huts and tents near the fence."
"Although it is a day of celebration, a lot of residents are going about their daily life as if nothing happened."
"Washing clothes, preparing leather, carpentry and many more activities don't necessarily have the privilege of taking a day off."
show lizard with longdissolve
"I can't help but turn my head towards the lizard Nightfallen from before, who especially can't catch a break."
"He's on his knees, weeding a patch of grass around one of the tents as we walk by, before being sent to fetch water from the pond, to put out the pyre when the time comes."
"He points towards two large buckets filled with water, saying something under his breath, in a language that seems a bit different than what the Wild Furs are using."
"That is not something the Wild Fur Nightfallen in front of him wanted to hear, winning him a heavy backhand slap in the face, before being sent again with a warning."
hide lizard with dissolve

"I'm not sure how to react, or if I should ask questions about it, but Eureka doesn't bat an eye, so I'll keep it to myself as well."
"The working people around give me a lot of different looks, either because I'm their chosen, savior guest, or because they think I look weird."
y simple"Hey, do you think my clothes are weird?"
eu "Why do you ask?"
y pf"Well, some of your tribe mates are looking questionably at me."
eu "Weeeell...yeah."
eu "It is definitely weirder than your friend's outfit."
y "How is MY outfit weirder?"
eu "First, the colors are too bright, too white, easy to spot in the wild."
y pf"What a revelation."
eu "Secondly, every part of your body save for your head and hands is covered."
eu "That is highly unusual, especially since your friend is more uncovered."
eu "They might think you are his personal sex object, something very alluring to the eye, prohibited to touch by anyone else, you're forced to dress more so others don't get dirty thoughts."
y "I suddenly feel really good about changing..."

scene tent3 with dissolve

"Eureka lets me enter first inside a tent, more colorful than the others, decorated with animals made of cloth and butterflies of silk, their own, different take on origami."
"This place screams {i}'come here to get dressed'{/i}."
"Inside is a single, petite mongoose lady, who bows to us, but stays out of our way as much as possible otherwise, unlike retailers and vendors in normal society."
show eureka with moveinleft
eu "I'm thinking about something simple, something comfortable, that will turn heads but not in a bad way."
"The selection wasn't large, a lot of shades and textures, but ninety percent of {i}'clothes'{/i} consist of loincloths and some makeshift bras."
show eureka at right with ease
eu "How aboooout..."
show eureka ec at center with ease
eu "This."
"He picks out a long and wide silky piece, which he wraps around my waist and over one shoulder."
"I'm pleasantly surprised he is taking into consideration our {i}'naked is bad'{/i} policy, but honestly, as I said before, I WANT to fit in."
"And most of all...I rather not look like a roman peasant from ancient times..."
y simple"Uhmm, I was thinking of something simpler."
show eureka
y "You know, like most men wear around here, so I don't look too out of place."
eu "Something like Ruth's?"
y pf"More like Ragnar's."
y "I still want to have my front and back covered."
show eureka ec
eu "Yes! I chose Ragnar's garments for this occasion, I bet I can get something suitable for you as well."
show eureka ec at right with ease
"There really isn't much to choose from when your choices are: big piece of cloth, small piece of cloth, this color, or that color, feathers or stones?"
eu "How about this?"
show eureka ec at center with ease
show eureka
eu "It matches your eyes, and I promise this one is not see-through when wet like the others."
y s"It is acceptable."
eu "Come on, pants off, let's let Mira fit and sew it."
y blush"Off? Like, right now?"
y bored"Meh, who am I kidding, I'm just embarrassing myself by delaying."
eu "That's the spirit!"
scene black with dissolve
"I get completely undressed, pausing a little at the underwear, but the loincloth is supposed to wrap around everything, so those would just make everything less comfortable."
"The mongoose, Mira, sews the cloth around my waist with Eureka's help."
"I even managed to not get too excited whenever their soft, warm hands were near my goods."
scene tent3
show eureka
with dissolve

eu "Walk around a little."
show eureka at left with ease


eu "Now run and jump."
show eureka at right with ease
show eureka at center with ease
show eureka with vpunch

"This reminds me of childhood, whenever I had to get new shoes."
y naked"Fits like a glove."
eu "And it looks great on you as well."
eu "Mira, do you mind taking care of these?"
stop music fadeout 2.0
"He hands my clothes to her, which she accepts emotionlessly."
scene camp6 with longdissolve
play music "audio/forestsound.ogg" fadein 3.0 volume 0.6

"By the time we go back outside, the torches are no longer lit, and the pyre is being extinguished by the lizard as we speak, under an older Nightfallen's supervision."
"The music has stopped and the last of the camp's folk can be seen making their ways through the narrow path."
play sound "audio/stomach.ogg"
"My stomach gives off a low growl, reminding me that there are countless ways I can embarrass myself in front of new people."
show eureka sadsmile with moveinleft
eu "Ku'sani mentioned you two haven't eaten anything all day, your town's resources must be scarce, I am sorry for that."
y nakedss"Yes, we haven't eaten, but that's because we just didn't have the time, don't worry."
show eureka simple
eu "No time...for food?"
eu "Yet another difference I will have to simply accept between us."
y "I'm assuming you take meal time more seriously around here?"
show eureka
eu "Of course!"
eu "How can we be of use to our tribe if we don't have energy to work."
play sound "audio/horn.ogg"
"A loud horn can be heard in the distance followed by faint music."
play sound "audio/celtic1.ogg" fadein 3.0 volume 0.1
y nakedsurprised"Is it starting? We're going to be late!"
show eureka smug
eu "We will be late to Ragnar's boring speech, you mean?"
eu "Still, we don't want to upset anybody, so we should hurry."
hide eureka smug with moveoutright
"This time, the camp feels empty, no souls remain, even the lizard and his watchers began to make their way to the feast upon hearing the horn."
scene camp2 with dissolve
"The Chief's door no longer has guards either, no man left behind today, huh?"
scene flowers2 with longdissolve

play music "audio/celtic3.ogg" fadein 3.0 volume 0.3
stop sound
"This part of the camp is almost unrecognizable since we left, with dozens of Wild fur's occupying a big portion, blocking a lot of the background."
"New light given off by torches replaced the almost non existing natural light, blocked by trees."
"Aside from torches, there are glowing crystals inside makeshift lamps of bendy sticks."
"The empty, round table is now filled to the brim with things I will need help naming."
"At the foot of the floral pillar, lies none other than the wyvern, torn between going to sleep or attacking the food."
show ragnar ec at right
show cat21bored at left3 zorder 3
show ruth simple at left5 zorder 1
with dissolve
ra "And this is why, we should all be thankful to, and congratulate our guests, for reuniting us with Ki'vaathi."
ku "For like the fifth time..."
ra "Furthermore-"
show ragnar simple at right
hide cat21bored
show cat20awkward at left3 zorder 3
show ruth at left5 zorder 1
ku "H-HEY EVERYBODY, [name] and Eureka are here!"
ku "Let's switch our attention to them!"
show eureka with moveinleft
"Everybody seemed relieved to get a break from Ragnar's rambling, especially when more than half of them don't even know what he's saying."
show wild2 at left5  zorder 2 with moveinleft
hide cat20awkward
show cat20smile at left3 zorder 3
wf "Ah! Good evning!"
ru "No no, noon, goodnoon."
wf "Ooh, su su, goodnoon, [name], Eureka."
ru "Yes, goodnoon."
hide wild2 with moveoutleft
y nakedss"Hi."
y "I see you're getting the hang of our language, Ruth...kind of."
"He nods proudly."
hide cat20smile
show cat20smug at left3 zorder 3
ku "Heeey, looking good [name]."
ku "Finally decided to embrace sluttiness?"
ku "And why were you so late?"
ku "Did you, in the words of the Wild Furs, {i}'claim'{/i} Eureka as your own?"
y nakedbored"..."
ku "Careful, might make Ragnar jealous."
show ragnar at right
ra "Jealous? Of my new friend and partner bonding?"
ra "No way, I'm looking forward to that."
hide cat20smug
show cat21smug at left3 zorder 3
ku "Hear that [name]?"
y nakedsimple"..."
ku "Get what he's saying?"
ku "He wants you....to-"
y naked"..."
hide cat21smug
show cat21simple at left3 zorder 3
ku "To go and-"
y "..."
hide cat21simple
show cat21mad2 at left3 zorder 3
ku "Ok, what is this? Why are you just standing there smiling?"
ku "Can you hear me?"
y nakedss"Yes, I hear you, I just...missed your teasing."
hide cat21mad2
show cat21smug at left3 zorder 3
ku "Huh."
show ruth simple at left5 zorder 1
ku "Of course you can't keep away from me, I'm just too irresistible."
show ruth tongue at left5 zorder 1 with dissolve
y "You sure are..."
hide cat21smug
show cat21simple at left3 zorder 3
"A droplet of water falls on the cat's snout."
"Don't tell me it's gonna rain- nope, it's not water, it's drool."
"A huge bear is towering behind the cat, his mouth open and tongue out."
ru "[name]...pretty."
hide cat21simple
show cat20smug at left3 zorder 3
ku "I think the word you're looking for is {b}'spicy'.{/b}"
ru "{i}*huff*{/i}spy-si..."
show eureka ec at center
eu "I was thinking of {b}'provoking'{/b}."
ru "{i}*huff huff*{/i} provo-king..."
show ragnar smug at right
ra "What about {b}'come-hither'{/b}."
ru "{i}*huff huff huff*{/i} cum..."
y nakedbored"When do I put my foot down?"
ku "Knowing you? Never."
ku "Now come on [name], give us a spin."
"Everyone, including other furs nearby, that have no business with this conversation, watch me closer, patiently."
y "{i}*sigh*{/i}"
"I turn around, leaning my weight on one leg, then the other, switching my hand from hip to hip."
scene flowers2
show cat20 at left3 zorder 3
show ruth blush at left5
show eureka ec at center
show ragnar ec at right
with dissolve
"Lastly, I finish it off with a twirl that gives everyone a more in-depth look without being too explicit."
play sound "audio/claps2.ogg"


"Then everybody clapped."
"No, that is not a joke, everybody quite literally started clapping, including the Chief, who has been sitting on a special throne on the other side of the table, with his guards nearby."
ru "Ruth like you."
"I would've never guessed, Ruth."
ra "We're happy you're embracing our traditions already."

ku "Hey, what about me? I'm already getting the hang of your language."
eu "Praise be all who act selflessly to show respect for others."
ku "I'll take that as an {i}'you too'{/i}."
show ruth simple at left5
show ragnar at right
show eureka
hide cat20
show cat20smile at left3 zorder 3
play sound "audio/stomach.ogg"

ru "..."
ru "Ruth want look naked [name], but Ruth want food more..."
y nakedsmug"Same."
y nakedsimple"I-I mean, just the food part."
eu "Then let the feast begin."
show ruth at left5
show eureka bored
eu "That is, if a certain Chief's son is done with the speech our guests heard multiple times already."
show ragnar bored at right
ra "Apparently...since everyone can't help but fall asleep, even my own brother..."
t "Sorry, try harder not to bore me next time."
hide cat20smile
hide ruth
with moveoutright


"Ruth takes Ku'sani to the Chief's side of the table, while Ragnar and Eureka hang on to both my arms on either side, guiding me to the opposite part."

y nakedsimple"Aren't we going to sit all together, you know...the two guests and their friends with the Chief?"
y "It just makes sense."

eu "Ku'sani requested a section with no fish in the dishes or his vicinity in general."
eu "I'd hate for you to miss out on our cuisine because of him."
stop music fadeout 3.0

ra "My father is not a big seafood lover either, so they go hand in hand."

y naked"You're right, living so close to the ocean and not capitalizing on it would be a shame."
play music "audio/celtic2.ogg" fadein 3.0 volume 0.6

scene feast with longdissolve
scene CGc22


"As soon as we, the main guests, and the most important figures of the tribe choose our seats, everyone else joins around us."
"No more signals or waiting for approval, everyone digs in immediately."
"The music would stop from time to time, so that the musicians can be switched and get some plates themselves as well."
"{i}'Plates'{/i} is a strong word, huge, clean leaves were used instead, with occasional wooden bowls for more soupy dishes, and as utensils: thankfully the carpentry side evolved enough that we have forks and spoons."
"I'm not a fan of fur in my mouth, if I had to use my paws to eat."
"Eureka is very proud of the whole celebration, but especially the food."
"Apparently, he's the tribe's main herbalist, main cook, sewing expert, event planner and manages all cleaning duty as well as resource stocks manager, such as: wild fruit, vegetables and wild game."
y naked"Just what DON'T you do around here?"
ra "He's not the best breeding mount."
y nakedawkward"Hahaha."
y nakedsimple"Ha...?"
"Eureka looks away embarrassed."
y "Oh, that's not a joke."
eu "I can't help it, every time someone wants me to follow them to the breeding hut, I can't but think of all my duties and how much time I'd waste."
ra "Until I come in and have to basically drag him inside and give him the ol' seed pump for hours."
eu "You're always annoying when you do that..."
ra "Yet you can't stop moaning the whole time."
ra "How did you even survive without me for so long?"
eu "I'd just...you know...pass out until someone did what you do until I'm back up and running."
y nakedconfused"I'm sorry, {i}'pass out'{/i}?"
y "I feel like I'm missing information."
ra "Of course, your kind doesn't have this."
ra "You see, Nightfallen don't just WANT to get rid of their lust through sex, they HAVE to."
eu "And it only works with partners."
eu "I mean, it feels good alone too, but you need someone else to get rid of lust."
y "So it works kind of like energy?"
ra "Yeah, imagine if you ate only grain and water for weeks, you would survive, but you wouldn't have the energy to do anything."
y nakedsimple"I didn't even know Nightfallen can do that with one another."
eu "It's not as effective as having someone of your kind as partners, it's true, that's why we keep open doors for anyone."
eu "We're talking too much about lust right now, [name], here, this is my speciality."
eu "I used spices Ragnar brought from his adventures."
ra "So I helped."

"He says, very proud of himself."

eu "Savory Braised Wild Boar: Tender chunks of succulent boar, slow-cooked to perfection in a rich and aromatic broth, infused with wild herbs and earthy spices, resulting in melt-in-your-mouth goodness."
"I never had any meat that's not a farm raised animal or a fish, so boar is a little intimidating."
"As I said before, I'm taking risks today, I'm having fun, so it's boar time."
"The meat is cut into small cubes across the skin."
"I stab a piece with my fork, which makes it shred in smaller pieces."
"A great first hint it really is a {i}'melt in your mouth'{/i} experience."
"I use my spoon to help scoop some out, with Eureka's eyes following my every move."
"Then..."

"With a resounding crunch, my teeth broke through the outer layer of crispy, golden skin, revealing a tender, flavorful interior. The meat yielded effortlessly, releasing a burst of rich, savory juices that danced upon my tongue."
"The intricate blend of herbs and spices infused the boar with an irresistible depth of flavor that transports me to the heart of the untamed wilderness."
ra "Woah, did you just take a bite of meat or have the best orgasm of your life?"
eu "Shut up, shut up, he loves it, you love it, don't you?"
y nakedfood"{i}Thish ish the besht thing I ever tasted! Tashtes jusht like pork, *chews* might ash well shay It'sh an orgashm in my mouth! You're *swallows* amazhing, Eureka!{/i}"
y "{i}*Swallows*{/i} I could eat like this for the rest of my life."
eu "I am overjoyed beyond words and so very honored!"
eu "I know your kind has very intricate, and explosive flavors, so I'm glad you enjoy my simpler recipe."
eu "What about this? Oh, and this, please try this as well, Ragnar, give that whole plate in here!"
ra "He'll choke, slow down!"
eu "Oh please, it is fine."
"This is where the intense lunch session really starts."
"Eureka makes sure to tell me the story and recipe of every dish."
"The Grilled River Trout with Citrus Zest, freshly caught trout, delicately seasoned and grilled to perfection, boasting a tantalizing smoky flavor. "
"Forest Harvest Salad: A vibrant medley of foraged treasures from the forest, including crisp wild greens, tangy berries, and crunchy nuts, all tossed in a light vinaigrette made from hand picked herbs. Each bite delivers a symphony of flavors and textures, celebrating nature's bounty."
"Herb-infused Root Vegetable Medley: A colorful array of hearty root vegetables, roasted to caramelized perfection."
"Exotic Mushroom Skewers, at least for me they're exotic."
"Smoked Venison with Wild Berry Reduction."
"I could go on forever, because the variety is simply infinite, and Eureka is proud of all of them."
"Stomach ache? I don't know her, all I know is great food and even greater company."
"Two completely different, but equally hot men, rubbing against me, trying to stuff my mouth as much as they can."
"In other words, heaven."
stop music fadeout 3.0

scene black with llongdissolve

"{i}In the meantime...{/i}" with longdissolve
play music "audio/celtic3.ogg" fadein 2.0 volume 0.2

scene feastblur with llongdissolve

"I can smell the scent of fish all the way over here... there's just no way to hide it, it's too strong, even half a table away."
"These people are already breaking their backs to take care of my every need, I can't demand any more favors."
"But God, how I wish to throw it all back in the river..."
"[name] looks like he's having a lot of fun, Eureka and Ragnar are all over him, and Ruth over here is distracted by the food, otherwise, he'd be on top of [name] right now..."
"Am I jealous? I'm not jealous, who would I be jealous of?"
"[name]? For getting so much attention from people other than me, or jealous on the people that give him the attention themselves?"
"No, neither, I found my family, well, step family."
"I'm happy."
"Aren't I?"
"I'm not jealous."
"I'm...content."
c "Son?"
kus sad "..." with longdissolve
kus simple "Huh?"
kus sadsmile"Oh, me, right... erm, what?"
c "You are not eating, why?"
"In my overthinking and attempts to please everyone with my talkative nature, I forgot to stuff my mouth, and the truth is, I really am hungry, even if something just feels wrong..."
kus eat"N-no no, I am, look, see?"
kus "Mmmhhmm, roasted carrots, so sweet."
kus "And this meat, delicious, quail?"
c "Rat."
kus spit"{i}Pfffuuuuu!{/i}" with hpunch
kus bored"I'll...stick to vegetables."
"Ki'vaathi finally decided, after minutes of hard thinking, that he's going to jump on the table and help himself with some food."
"The meat right in front of him is apparently not good enough, so he walks on the table's edge, demanding everyone feed him whatever they have on their forks, which they do gladly."
"He finally stops in front of me, arching his back, asking for pets, before jumping off again and going to sleep under the flowery pillar, with a large bone in his mouth, suckling at it until light snores can be heard."
"He's cute, even if he's kind of dangerous when not in the mood."
c "You know...Ku'sani, I'm glad you came home."
c "Your arrival here, with Ki'vaathi in hands, brought not only hope, but joy to us all."
kus "And all it took was a bit of kidnapping."
c "And for that I apologise, I didn't even know where you were, or if you were alive."
kus s"Don't worry, I'm over it."
kus "Blessed be your secluded tribe."
c "Your friend seems to be getting along pretty well with my other son and his partner."
kus simple"Yeah..."
c "Perhaps well enough that he decides to settle here with them in the future, that way he can be closer to you as well."
c "His exotic fur caught the eye of a lot of your tribemates."
kus "Yeah... wait-"
kus "Here with them? Me?"
c "Well you're staying here with us, aren't you?"
c "We're a family, I thought you made up your mind about your destiny here."
kus sad"I-I have another family as well."
kus "I'm not abandoning them, I can't."

c "Didn't you say they...disappeared one day?"
kus sadsmile "Yeah but...they'll come back."
kus sad"It's not like they're dead or anything, I just...don't know where they are..."
kus sadsmile"Besides, I can teleport, I'll definitely do so to visit both you and Ki'vaathi."
c "I see."
kus simple"Uhm, what was that about [name]?"
c "What was what?"
kus "You don't think he'll want to stay, do you?"
kus "He's a city boy."
kus "He won't fit in."

c "You're the one that refused to wear our traditional clothing, correct?"
kus simple"..."
kus sad"I guess he does like it here, huh?"
"I look at the laughing leopard, getting his face stuffed by two lovely peopl-"
"Nightfallen."
scene black with llongdissolve
kus sad"And them..." with dissolve
stop music fadeout 2.0

"{i}Back to you...{/i}" with longdissolve

scene feast with llongdissolve
play music "audio/celtic2.ogg"fadein 2.0 volume 0.3

"Everyone was ravenous, either from hard work, or dancing, or because they forgot to eat all day, but even after we all filled our bellies, the table still remains rich."
"Yep, this is what I call a feast."
"Some Wild Furs got up and started telling stories and recalling battles past."
"Others decided a nap under the huge, shaded trees is in order."
"Some became very touchy, and decided to get into a hut together, either in pairs or in groups."
"Gotta get rid of that lust after a good meal, am I right?"
"As for me...I have questions, sooo many questions."
"The first and most important being..."
"{size=60}WHERE THE FUCK ARE YOU, SCRIIIIIIIBBLEEEEEEEEEES?!!!{/size}" with hpunch
un surprised"AAGH!"
un "WHAT?! What?"
un "Is the world ending?"
"No, but my patience is."
"Where were you all this time?"
un bored"Why? Missed me?"
"A little, yeah."
un simple"Oh."
un sidee"W-well, I was just watching some of these movies in your mind."
un "A little hard to find something other than porn around here, but I managed."
un "I especially like {i}'The Firm'{/i}, it's this comedy about a group of people working at a firm, selling paper and-"
"I know the one, it's in my mind, after all."
un bored"So what else do you want?"
"How come you didn't show up for so long?"
"My mind feels like it will explode with lust, everybody here is so sex driven."
"You can't even IMAGINE all the sex jokes and inappropriate touching we did today."
un bored"So nothing new."
"You would usually jump at the first opportunity to call me a slut, or be sarcastic."
"We just found out my friend was adopted as a baby by these Nightfallen, and his real name is {i}'Ku'sani'{/i}, isn't that interesting?"
un "Ew, family drama."
"I thought your whole point of taking over my body was to experience new and interesting things."

un "Hey, [name], what am I?"
"Huh?"
un "What species?"
"Ermm, demon?"
un suspicious"Right, so do you honestly believe, that in my centuries of living as a LITERAL Nightfallen, I never experienced a Wild Fur's celebration before?"
un "That I've never set foot in a camp like this?"
"..."
un squint"I've been in more orgies with freaks like these than I can remember."
un bored"And people claiming they were raised, or even birthed by Nightfallen are not new either."
un "To me, this is as exciting as it is for you to watch paint dry."

"Now that you explained it, I can give you a pass, although you could've done so with less attitude."
un eyeroll"Excuse me, your majesty."
un sidee"For the record, I do take a peek sometime, so I know a lot of things that happen in the real world."

un "I have to say, these are some very tame Wild Furs."
"Explain."
un "I mean, they're usually friendly, but not {b}this{/b} friendly to strangers."
"We're not strangers, we rescued their god or whatever, plus one of us is their Chief's adoptive son."

un eyeroll"Yeah, and I bet they reaaally want his 'son' to stay."
"What are you saying?"
un "I'm saying that you're going to lose your boyfriend to these Nightfallen."
"What?"
"No...he would never just...leave the academy."
un "Why not?"
un bored"He said it before, nobody gives a real shit about him there."
un "He seems like he'd fit nicely."
un simple"But in the end it's his choice, right?"
un "You wouldn't want to take that away from him."




"Right..."
un"In the end, I don't care what you do."
un "Take my advice or don't."
un "I'll go back to my show."
un squint"Call for me if you need me, but do it quietly, please..."
"..."
"Scribbles is an old demon, old enough to know a thing or two."
"But as he said, it's his choice to stay or not, it's not like I can force him to keep away, especially since his wyvern friend will stay here for sure."
"These Nightfallen aren't THAT bad, right?"
"I mean, just because I don't like what they're trying to do, doesn't mean it's wrong."
"Aghh, Scribbles just popped in, made me question my new and old friends, and dipped without another word."
"The definition of an evil demon."
"It's time I find out more about these mysterious, intricate, hot Nightfallen."
"It will be a good distraction for Ragnar and Eureka as well, since judging by those bedroom eyes, they look like they're going to jump at each other and fuck right here on my lap."
y naked"Do you guys want to play a little game?"
ra "Absolutely!"
eu "Hopefully not one that involves running right after a meal."
y "Nah, just a question game."
y "I realize I have MANY questions unanswered still, about you two as individuals, but of this place as a whole."
y "And you can ask things about me and my kind in return."
eu "Lovely, I did actually have some things I wanted to ask but didn't know how."
ra "I'd love to help you learn more about us."
ra "Hit it!"
y "Ok, I'll go first."

menu wildquest:
    "What do I want to know about...?"

    "Naming culture and masks?":
        $ questions +=1
        y "So, I noticed that only some of you wear masks."
        eu "Ah, the masks."
        eu "Ragnar, do you remember your first mask?"
        ra "Clear as day, all those feathers kept making me flick my ears."
        ra "I don't know how I lived like that."
        eu "Mine was a simple doe, I got lucky."
        y "Soooo, why?"
        eu "Ah, right, here's how we do it."
        eu "The Chief chooses an animal, object or shape that represents us when we start training in whatever field we'll be working in."
        eu "Hunting, carpentry, sewing, that kind of stuff."
        ra "The mask is placed on with magic that only the Chief possesses, so that you can't remove it."
        y nakedsimple"So Ruth has regular eyes under the dark mask?"
        ra "Yes, Ruth is at level two."
        y "Level two?"
        eu "You only need to wear a mask over your eyes at level two, that is for those who are close to getting their names."
        y "What about the Chief, why is he wearing a mask?"
        y "Does he not have a name?"
        ra "He does, but it is forbidden to be used or known by just anyone."
        ra "As for the mask, just tradition that the Chief wears one for the rest of his life."
        ra "Don't ask how he sees through that thing...it's a mystery."
        y nakedsimple"Oh, there goes my next question."
        y "Speaking of names, how do you get those?"
        y nakedconfused"I think you mentioned you sometimes name each other?"
        eu "Names are not given, they are won."
        ra "I named Eureka, he gave me his heart, and I gave him a name."
        ra "Mine, for example, was chosen by my father, meaning 'warrior' in our tongue."
        eu "And he named me when we became partners, as mentioned."
        ra "Because, when I met you, I knew I found a priceless treasure."
        eu "Aww you~"
        y nakedss"That is so sweet."
        y "Did you also get the idea from our tongue?"
        ra "Yes, while traveling your lands, I came across this word."
        ra "I loved the sound of it, and when I found out what it meant, I knew I had to save it for my special someone."
        "I'd be melting with cuteness if they weren't squeezing me to death trying to nuzzle each other."
        y nakedconfused"What about Ruth?"
        y "What does that mean?"
        ra "It's from your tongue again."
        ra "His full name is {i}Ruthless{/i}, but we call him Ruth until he takes his mask off."
        y "What did he do to win a name like that?"
        eu "It's a bit ironic, he solves all conflicts with kindness in the camp."
        ra "Ruthless would never hurt a fly, so the Chief wanted to have some fun."
        y nakedss"It is pretty funny, I admit."
        y "Is that the only reason?"
        eu "Weeell, another reason would be that he has to do whatever task the Chief tells him to do, with no questions."
        eu "That's why he must remain ruthless."
        ra "But my father never even had him gut a fish before, so his innocence is in good hands."
        y nakedsimple"It just turned slightly scary."


        ra "Our turn."
        y naked"Shoot your shot."
        ra "How is the sex culture at that academy town?"
        y "This town specifically?"
        eu "Yes, we heard you're way more open about that than the regular folk."
        eu "Still, we made sure not to make you uncomfortable with our public displays, just in case."

        y nakedsmug"I'd say we're kind of like you, in a way."
        y "Except that we're not allowed to be naked in public, or have sex in public."

        ra "So your ways are more personal, that's why you're so shy."
        y nakedawkward"Y-yeah, more personal."
        eu "Interesting."
        jump wildquest

    "Ragnar.":
        $ questions +=1
        y naked"Questions for Ragnar."
        y "Starting off simple, what's with the tattoo?"

        ra "These ones on my chest?"
        y "Yeah."
        ra "It's the two moons in the sky."
        ra "Moonlight is the source of magic for all demons. Nighttime is when they're most powerful, and it's theorized the same for dragons as well."
        ra "I just wanted to pay my respects by having this symbol imprinted upon me."
        eu "And fur tattoos are hot."
        ra "He's the second reason I decided to get it..."
        ra "One of your kind made it, actually."
        y "About that, tell me more about those {i}'adventures'{/i} of yours."
        ra "Where to even begin!?"
        ra "As you might know, in our tribe, names have to be won."
        ra "Usually somebody would win a name by doing something grand, or unique."
        ra "In my case, I decided to be adventurous."
        eu "Which was very extra, and very rude of you."
        y nakedsimple"Why's that?"
        ra "Weeeell..."
        eu "Because he was gone for one hundred forty four moons"
        eu "Twelve years."
        y nakedsimple"Wow."
        ra "In my defense, I brought home spices for these delicious meals, made connections with your kind and also accumulated a lot of knowledge."
        ra "A whole new tongue for the whole tribe!"
        ra "It's the only reason we can communicate with [name] right now."
        y "Our whole language in twelve years?"
        y naked"That's pretty good."
        y "You two, and the Chief are very fluent, even when it comes to slang."
        ra "Eureka is a smart one."
        eu "I learned it in only two, alongside math."
        ra "Which is knowledge I brought with me as well."
        ra "You're welcome!"

        eu "In truth, I really am grateful by how much Ragnar helped the tribe, even if he left me alone for so long."
        eu "Ironically, your whole adventure culminated to a single point."
        eu "Isn't that how you got your name?"
        ra "It is, and I'm proud of it."
        ra "I slayed a huge wyvern with my bare hands."
        ra "You can see its front teeth in the main camp."
        ra "On top of a watch tower."
        y naked"I think I did!"
        y "I was wondering what animal or Nightfallen was so big to have those bones."
        y "You truly are a warrior."

        ra "You're gonna make me blush."
        y "What about your scars Ragnar? How did you get them?"
        ra "Ah, the symbols of my victories."
        ra "I'm ashamed that I don't have more."
        eu "A good warrior doesn't need many scars."
        ra "That's true, I never got injured fighting beasts or Savage furs."
        y nakedsimple "So how..."
        ra "These were made not that long ago actually."
        ra "A rogue Wild Fur from our tribe went behind the Chief's back, so I had to fight him to the death."
        ra "Fortunately for him, he escaped, but not before we gave each other some nasty scars."
        ra "Too bad, he was a good tribemate up until that point..."
        "That sounds a bit too gruesome for a table discussion, so I'll drop the subject."


        eu "If you're done with your story, may I address the next question?"

        y naked"Be my guest."


        eu "What is your relationship with Ku'sani?"
        eu "You're not partners, are you?"
        ra "I think they use the word {i}'boyfriend'{/i} over there."
        y nakedblush3"We use both– I-I mean, not that we are either, haha."
        eu "You're just friends?"

        y "Yep, aha, juuust friends."
        ra "You did mention that in the Chief's hut, I forgot."
        y nakedawkward"We're both totally virgins too."
        "Why did I say that...?"
        eu "Oh my."
        "Eureka covers his mouth in shock."
        ra "That is new information."

        eu"You weren't kidding when you said they're shy."
        ra "See?"
        eu "Just how many moons without sex is that...?"
        ra "Too many, dear...too many."
        y nakedpf"Let's move on to the next one..."
        jump wildquest


    "Eureka.":
        $ questions +=1

        y nakedsimple"Eureka, how come you're so...dressed?"
        y "Everyone else has some cloth covering their junk at most."
        y nakedbored"Looking at you, Ragnar."
        ra "I'll let you know that your kind loved the way I dressed."
        "Yeah...because you're hot."
        eu "I wear more layers so that everybody knows I'm not easy access."
        y nakedsimple"What does that mean?"
        y nakedbored"Never mind, I know actually, sex things."
        eu "Exactly."
        eu "I'm too busy all the time to just have a go whenever, so I dress more proper."
        eu "Especially because of all the jobs I do, I need something to protect my fur."
        y nakedsimple"Speaking of, why so many jobs in the first place?"

        eu "I, ermm, I just feel embarrassed."
        eu "As we mentioned before, I'm not good with repeated breeding, I'm not a good warrior, or hunter, but I love my tribe, and I want to be of help."
        eu "So I want to be as useful as possible with the jobs that I'm best at."
        ra "Which is a lot of them."

        y naked"With your brains, who needs muscle?"
        y "Although you're still way stronger than me."

        eu "Heh, thank you, you're very kind."
        ra "May I give you the next question?"
        y "Let's hear it."

        ra "Considering you don't live in a tribe, what work will you do in the future?"
        ra "What is, or will be your job within your society?"
        "That is a pretty deep question about my future."
        "The answer is obvious: Nightfallen hunter, but do I want to tell the literal Nightfallen that?"
        y nakedawkward"Uhhhh."
        "Quickly, what's the closest thing to a Nightfallen hunter?!"
        y "A hooker."
        "Really, brain?"

        ra "Ah, noble profession."
        ra "You will bring a lot of use to your kind."
        eu "Way more than me, that's for sure."
        y "I don't know about that one."

        y "We should go to the next one."

        jump wildquest


    "Lizard.":
        $ questions +=1
        y nakedsimple"I noticed...a lizard in your camp."
        ra "An eye sore, isn't it?"
        ra "We're sorry you had to see him, he's-"
        y nakedsurprised"No no, not at all."
        y "I'm fine with him."
        y nakedsimple"I was just wondering...why is a Savage Fur here?"
        ra "Why, he's doing the tedious jobs we don't have time to do, what else?"
        y "No, I mean, why do you own a slave?"
        y "You've been in our society, Ragnar."
        y "Don't you think that's wrong?"
        ra "Huh."
        ra "I've never had someone of your kind react poorly to this information before."
        ra "They would either slap my palm in agreement or not care."
        eu "I also thought that your kind doesn't like...what do you call the violent ones?"
        ra "Savage furs."

        y nakedsimple"Well..."
        y "Uhmm."
        y "We do hate them but..."


        y "I'll drop the question, for now."

        jump wildquest


    "Children?":
        $ questions +=1

        y nakedsimple"I haven't seen any children around, how do Wild Furs even reproduce?"
        y "Our biology teacher did not care to teach us anything useful."
        ra "The same as you, we need a male and a female, then the female will carry the baby for seventeen moons until-"
        y nakedsurprised"SEVENTEEN?!"
        y nakedsimple"Sorry, that was a little loud."
        eu "How long do your females carry it?"
        y "Nine moons."
        ra "Wow, no wonder there are so many more of them."
        eu "As for the ones that are born but not matured yet, we have a separate part of camp."
        ra "The young have the highest level of protection, and they are not allowed in these parts of the camp, since you know..."
        ra "Breeding sessions."
        y "Makes sense."

        eu "Our turn."
        eu "A simple one."
        eu "What is your age?"
        Y naked"I'm nineteen years old."
        ra "Years?"
        eu "That is twelve moons for one year, remember?"
        eu "You taught me this."
        ra "So...nineteen would be...twelve times nineteen?"
        ra "Twelve...nineteen..."
        ra "That is impossible to calculate!"
        eu "No no, here is an easier method."
        eu "How many moons is ten times nineteen?"
        ra "Ermmm...wait, don't tell me."
        ra "You add nothing at the end, zero, so somehow it's supposed to make it... one hundred and ninety?"
        eu "Correct!"
        eu "Now do two times nineteen."
        ra "It's...twenty...two times ten...two times nine..."
        ra "Thirty eight?"
        eu "Correct again!"
        eu "Now add them."
        ra "Add what?"
        eu "{i}*sigh*{/i}"
        eu "It's two hundred and twenty eight moons, Ragnar."
        ra "This math thing is too hard."
        ra "In other words, [name] is not a cub, as we thought."
        eu "Not even close."
        y nakedss "Yey?"
        "Even someone as sharp as Ragnar can be defeated with Math."
        jump wildquest



    "That's about it.":

        if questions <=1:
            "I should ask at least {b}TWO{/b} questions, it would be weird if I stopped so soon."
            jump wildquest
        else:
            jump afterwildquest

label afterwildquest:

eu "I feel like we bonded further with these questions."
y naked"And I know enough to say that I find your kind even more interesting and captivating than before."
ra "You are certainly more interesting than most people I met on my travels."
y nakedss"That is a bigger compliment for me than you think."
"We continue to lazily feast while sharing stories."
"Some Nightfallen got dressed in big robes, covering their heads, then jumped over the table with powerful leaps to get to the empty space in the middle."
"Apparently, the entertainment has begun."
"Three of them dance to the music, fluttering their robes around, while everyone else claps in rhythm with the music."
"I feel like a king whose jesters have been unleashed."
"The Chief and Ku'sani seem to be the most entertained, thus the 'jesters' pay special attention to them."
"I wish I were the one to put a smile that big on the cat's face..."
stop music fadeout 2.0
scene black with longdissolve

"It's now been a couple of hours since we got here."
"The arena battles already feel like an eternity ago."
"The remaining Nightfallen are either going straight back to their daily duties, or finding empty huts to drain their lust in."
"The Chief and his guards left the cat with a final goodbye, returning to his chamber."
"Eureka, Ragnar and Ruth went urgently to investigate a trap that went off somewhere around the camp and will be back shortly."
"Only one fur remains playing an out of tune string instrument, slowly, emotionally."
scene flowers2 with dissolve
play music "audio/guitar.ogg" fadein 3.0 volume 0.3

"The silence and lazy energy is cut suddenly by the eccentric cat I grew to like so much."
show cat20 with moveinleft

ku "Hey!"
ku "How was your feast?"

y naked"Eureka knocked it out of the park, I didn't think wild game could taste so good."

y nakedss"Too bad fish kept us apart."
ku "Heh, yeah, another reason they're my sworn enemy."
y "..."
ku "..."
hide cat20
show cat20sadsmile
ku "I feel like I'm dreaming."
y "Me too."
y "Is your dream a good one?"
ku "It's not a nightmare, that much I know."
ku "But this whole family thing, and prophecies and celebrations and feasts...it's so..."
y "Unreal?"
ku "Kind of."


y nakedss"Speaking of, since we're alone for the first time we got here, what do you think of everything?"

ku "I like it here."
y nakedsimple"You do?"
hide cat20sadsmile
show cat20simple
ku "Don't you?"
y "I think so, but you're the nature enthusiast with a wild step-family around here, so it's a more important question to you."
ku "To be honest?"
hide cat20simple
show cat20ec
ku "I feel amazing, I feel free, and like I finally found my purpose."
y nakedsurprised"Isn't your purpose and dream to be a hunter?"
hide cat20ec
show cat20smile

ku "That is different."
ku "I thought you were getting along well with Eureka and Ragnar, like, really well."
ku "Do you have second thoughts about them now?"

y "It's not that I dislike them...just-"

y nakedsimple"..."
y "I think we should leave."
y "We have to go home."
hide cat20smile
show cat20angry

ku "What?"
ku "Now?"

y nakedangry"Yes, now."
hide cat20angry
show cat21bored

ku "Ok killjoy, does a full stomach turn you ungrateful?"
ku "I agree that the Chief can be a bit weird, and everyone is a bit overly joyful...but you can't not like them."

y "They use slave labor!"
hide cat21bored
show cat21mad2

ku "Is that what this is about?"
ku "I knew you were keeping too quiet around it."
ku "You do realize that lizard is a Savage Nightfallen right?"
ku "In the wild, he wouldn't think twice before chomping your head off."
y "Then how come he's doing everything he's told?"
y nakedbored"A regular Nightfallen doesn't understand when you tell it to go fetch some water."
ku "An alligator can be taught to do tricks, doesn't mean you have to leave one to babysit your child!"

hide cat21mad2
show cat20angry

ku "Damn it [name], are we seriously having this discussion?"
y nakedangry"Are YOU seriously defending slavery?"
ku "It's an ANIMAL, a NIGHTFALLEN."
hide cat20angry
show cat21mad2
ku "Do you even realize that these people, who praised us, fed us, took care of us the whole day, were still being hunted down by hunters when you were alive, living a pampered life in the city?"
ku "You were already a toddler when the government protection service for Wild Furs started, and that's only talking about OUR country."
ku "These people suffered so much in the past because of us..."
ku "And you're trying to defend an even more primitive Nightfallen species?"

ku "{size=30}But of course you're defending whatever walks on two legs and has a dick...{/size}"
y nakedsimple"That's not-"

ku "AND ANOTHER THING!"

ku "If they're treating that other Nightfallen soOoOo horribly, then say it."

ku "Let me hear you say it, what do {b}we{/b} do with Savage Nightfallen we find in the wild? Huh?"
y nakedsimple"..."
ku "I'm not hearing anything."
y nakedsad"We...kill them...for energy."
hide cat21mad2
show cat20angry
ku "I rest my case!"
ku "They are clearly better than us in that regard."
hide cat20angry
show cat20bored
ku "What's next? Mimics have rights to bear arms?"
ku "Maybe that plant that attacked us just wanted a friend?"
y"I don't know much about the Nightfallen world, I was just a nerd that got lucky getting into this academy, but I know from today's experience at least some of all that...Nightfallen 'philosophy' must be wrong."
y nakedangry"This guy deserves better!"
hide cat20bored
show cat21bored
ku "{i}'Guy'?{/i}"
ku "Trust me, there are people in our society who have it worse than that lizard, I should know."
ku "But..."

ku "Never mind, look..."
ku "You do you."
ku "I do have the viewpoint that the world is not just black and white, so whatever you think about that situation, it's your opinion."
ku"Just don't get in trouble with my family...alright?"
y nakedsimple"I'm not going to stir anything, if that's what you're implying. I'm not a revolutionist."
ku "Good."
ku "In any case, was that the only reason you wanted me to go home?"
y "I just thought we might've overstayed our welcome."
y "Don't you miss your other friends?"
y nakedss"Dallan, Aiden, Merina?"
ku "I am with family, [name]."
y nakedsad"I get it, then I'll stay and-"
hide cat21bored
show cat21simple
ku "No!"
y nakedsimple"?"
hide cat21simple
show cat20sadsmile
ku "I mean, you don't have to."
ku "I'll only stay a little longer."
ku "If you want to go home, that's fine, I'll teleport you later."
ku "I just need enough magic to teleport us there, then myself back."

y nakedsimple"But you'll be here alone."

ku "Not alone, just, without you..."
"That simple statement, for some reason, hurt more than I thought it would."
ku "I'm happy, [name]."
ku "I just want to look past the bad, ignore the dark and just smile until I can smile no more."
ku "That's kind of my life motto."
y nakedsad"I understand."
"My convincing was not the best, my points were too personal for him to care about."
"Is there anything in the world that matters more to me right now, than making this cat happy?"
"No."
"So I will bend to his wishes."

ku "Ki'vaathi is going to wake up again soon, and I want to be there to feed him."
y"I see... Well, I'll meet you later in the main camp then."
ku "Yes, main camp."
ku "Don't venture too far."
ku "I'll be with you once I have enough magic to spend."
ku "See ya."
stop music fadeout 2.0
hide cat20sadsmile with moveoutright
scene camp6 with longdissolve

"I walk to said main camp, just in time for the trio to arrive through the main gate, empty handed but not injured, at least."
play music "audio/celtic1.ogg" fadein 3.0 volume 0.2

y naked"Hey, what's with the trap situation?"

show ragnar sadsmile at right with moveinright
show eureka sadsmile at center with moveinright
show ruth at left5 with moveinleft

ra "False alarm, it was one of the big Nightfallen traps we set, so we got a little excited."
eu "Even I wanted to be a part of that."

ru "Ku'sani where?"

y "He's waiting for Ki'vaathi to wake up, so he can feed him some leftovers."
show eureka
show ragnar at right
eu "So he's too busy to spend time with you?"
y nakedss"Yeah, kind of, why?"


ru "Come us! Come us!"

y "What?"
ra "He wants you to come with us if you're free."
eu "We're going into the forest again to gather some plants, as well as wood for a new pyre and carpentry, while we're at it."
eu "After such a feast some of our tribemates might be sick, but I'm kind of out of the needed herbs to treat them."
eu "My supply is a little low, as embarrassing as that is to admit, so I'll be looking for that."
show eureka smug

eu "Ruth will carry the wood and Ragnar is our pretty face."
show ragnar bored at right
ra "I will be your bodyguard, thank you very much."
eu "That's what he likes to tell himself to feel useful."
ra "Grrr."
show eureka
eu "It will be way more fun with you there."
eu "That is, if you don't have any other plans."


"In my mind, the response is almost instant, but can I afford to leave my friend alone here?"
"My mind flies to the cat, sitting patiently and waiting for his wyvern friend to wake up, alone."
"But he's not the only one on my mind."
"On the other end of the camp, the lizard slave is carrying a bucket of grains, when someone's leg just so happens to get in his way, completely by accident, for sure, making him fall and spill the bucket."
"A scene is about to happen, maybe I should get away before that happens..."



menu:
    "With all that in mind, do I want to go with them?"

    "Go gathering.":
        y naked"I'd love to go."
        show eureka ec
        show ragnar ec at right
        y "The camp is very quiet, and Ku'sani is busy, so a little adventure can't be too bad."

        "Eureka clutches his herb bag excitedly while the other two grunt satisfied."


        eu "No time to waste then!"
        hide eureka ec with moveoutright
        hide ragnar ec with moveoutright
        hide ruth with moveoutleft
        "He gets behind me and pushes me towards the gate, of course, with both hands on my butt."
        "A gesture that I do not make a fuss about, even if there are no pants in the way to block the contact."
        "Maybe that's why I don't mind it, I'm used to their ways already."
        play music "audio/forestwalk.ogg" fadein 3.0 volume 0.4
        scene forest20 with longdissolve

        "Our little trip is peaceful and fun."
        "I can definitely see how this trio became so close."
        "Ragnar is kind of the jokester of the group, as well as the leader."
        "Eureka is the pretty face and definitely brings the brains."
        "While Ruth is the lovable goof, the himbo, if you may."

        "I help Eureka collect some plants in a small ravine, while Ruth gets distracted by a snail on a leaf that is carrying an even smaller ladybug on its shell."
        y nakedsimple"What is Ragnar doing?"
        ru "Small tree, old tree."
        show eureka with moveinleft
        eu "He's looking for the smallest and oldest trees, some that are perhaps hollow inside, or started to rot."
        eu "We take those and use the bad parts for fires, and the good ones for carpentry."

        ra "Ruth! Over here! This one!"

        "The bear leaves the snail and ladybug alone with a final wave goodbye, before approaching a {i}'small'{/i} tree Ragnar found."
        "It is still larger than a regular tree, but not even half as big as the others."
        y "Who's job was it to bring the ax?"
        y nakedpf"It wasn't mine, was it?"
        show eureka ec
        eu "Heh, no, silly, look."
        "Ruth takes a few good looks at the tree, from all directions, then punches it five times rapidly."
        "The first one makes the bark fly away, the next three destroy the semi withered wood, and the last one just to direct it into an empty part, not to damage other trees or anything important."
        "Like me and Eureka."
        y nakedsurprised"Wow!"
        y "You're super strong, Ruth."
        "He flexes smugly in response as I clap."

        show ruth at left5 with moveinleft

        ra "Oh yeah? Well watch this!"
        "Ragnar then uses his razor sharp claws to chop all the branches off, so we are left with an empty trunk."
        "He wanted to impress me with that move, buuuut it takes him way too long to finish."
        show eureka
        "Eureka, Ruth and I start gathering wild flowers as we wait, making flower crowns for each other."
        "They both give theirs to me. Eureka places his on my head, but Ruth's is a little big, turning into a necklace."
        y flower"I still love it."
        "I am left with one flower crown in hand, and four intense eyes watching me and each other."
        show eureka ec
        eu "It's too small for you, Ruth, I should take it."
        show ruth simple at left5
        ru "Hmmm, bracelet."
        "I don't want them to fight, and I don't want to choose, so I do the most obvious thing."
        show ragnar simple at right with moveinright
        y "Here, for our hardworking leader."
        y "You've been going at it for the past twenty minutes, have a flower crown."
        show ragnar flower at right with dissolve
        ra "Thank you, [name], it's beautiful."
        show eureka sadsmile
        eu "That's fair, we didn't even offer to help."
        show ruth at left5
        ru "Yes."
        ru "Fair, sorry."
        ra "At least I got to properly sharpen my claws and practice some wood cutting magic."
        y "I didn't even know Nightfallen other than Demons had magic."
        ra "It's weak, but it's there."
        ra "And not many have it, I'm one in a million."
        eu "We should get a move on, before we run out of energy or before his ego inflates too much."
        ra "You're right, love, that would not be great."
        scene forest22 with dissolve
        "The trunk of the tree is left where it is for now."
        "They'll come another day, with tools and cut it into pieces, for now, the branches are more than enough."
        "Ruth and Ragnar carry the wood back to camp while Eureka and I jump gleefully holding elbows in front of them."
        "We place our beautiful yet useless flower crowns where the wyvern's slumber space once was, as an offering."
        stop music fadeout 3.0
        scene camp6 with dissolve

        show ragnar at right with moveinright
        show eureka with moveinright
        show ruth at left5 with moveinleft
        play music "audio/outside.ogg" fadein 3.0 volume 0.4

        ra "This should do it for today."
        ra "Thanks for the help, [name]."
        y nakedawkward"I didn't help much."
        y nakedpf"No, scratch that, I didn't help at all."

        eu "You were emotional support for our strong working men here."
        eu "Ruth was concentrating on your behind more than the effort of carrying the wood."
        "I look at the bear with a dazed, satisfied expression on, and the hints of a bloody nose."
        y nakedsmug"{size=20}I was hoping the loincloth would have that effect on men.{/size}"

        show ragnar tired at right
        show eureka simple
        show ruth simple at left5

        ra "Hey, I think I'll go lay down for a bit."

        y nakedss"Are you not feeling alright?"

        ra "It's okay, most of our tribe mates got rid of their lust after or before the feast."
        ra "I didn't get to do that today at all."
        show eureka tired
        show ruth tired at left5
        eu "Ah, so that's the fatigue I've been feeling all this time, I completely forgot about it."
        ru "Ruth tired too..."
        eu "I'm sorry [name], I'm afraid we'll leave you alone for some time."
        ra "{i}*COUGH COUGH*{/i}"
        ra "Unless..."
        show ragnar sadsmile at right
        ra "Would you... like to join us, [name]?"
        y nakedss"J-join you?"
        y nakedblush2"Uhm, all three of you?"
        "Ruth doesn't say a word, but I can feel the earth shaking as he trembles with excitement at the thought."
        eu "You don't have to, of course."
        ra "But you would do us a huge favor."
        ra "Your kind is very effective in getting rid of lust."
        ru "[name], hard, there."
        "The bear points at the piece of cloth hiding my junk, rising rapidly."
        show eureka smug
        show ragnar smug at right
        "The other two look slyly at each other."
        eu "Didn't you say their kind are shy, but still very freaky?"
        ra "I did say that, usually they're simply afraid of asking."
        y nakedawkward"I-I wouldn't say afraid..."
        "I am SUPER afraid of asking."
        "I have almost no experience, yes I've used toys a lot before, but those don't count...do they?"
        "What if I'm not even close to the standard for these insanely hot Wild people?"
        "They definitely sense my restrained excitement and awkward, indecisive movements."
        show ruth blush at left5
        show eureka close with dissolve
        show ragnar close at right with dissolve

        "The two felines come closer, one of them hugging me from behind, the other from the front, both nuzzling my neck and talking softly."
        eu "Say, [name], are you the type to take control of your partners?"
        y nakedblush3 "I, uhmm-"
        ra "No, he's the type to submit to commands, aren't you, [name]?"
        y "In a way-"

        ra "I bet he can take two in the same hole."
        eu "I bet he can hit all the right spots."

        "Ragnar parts my lips gently, then my teeth with his claw, sliding a finger in."
        ra "What can this mouth do with a cock inside it?"
        eu "You must be full as well, if not with lust, at least, creamy, hot seed, ready to share it."
        "He cups the bulge formed underneath the thin cloth."
        "My hands just hang there in the air, not knowing what to do when all my fantasies spontaneously come true as whispers in my ears."
        "Ruth stands there watching patiently and blushing, bumping his pointy fingers together."
        eu "Is this proof enough we want you there with us?"
        ra "A {i}'yes'{/i} is all we need, not another word, and we'll give you the pleasure of a lifetime."
        "Their words, like spicy honey, hot and sweet, tickle my brain too much to refuse."
        "And such a simple task for heaven...just mutter a word."
        y nakedss"Yes." with longdissolve
        show eureka smug at center with dissolve
        show ragnar smug at right with dissolve
        "They both grin satisfied."

        ra "Ruth?"
        show eureka smug at left with move
        show ruth blush at center with move

        "The bear wastes no time and sweeps me off my feet, holding me bridal style."
        eu "Bring him to the breeding tent."
        "Hell yeah!"
        ra "No."
        ra "The {i}mating{/i} lodge~"
        ru "Ooooh, yes."
        y nakedblush3"W-what's the difference?"
        eu "The mating lodge is more comfortable and private, since it's made for those trying to have an intimate..."
        eu "Uninterrupted..."
        eu "Loving moment."
        ra "We can spare occupying it for an hour or two for our special guest."
        hide eureka smug with moveoutleft
        hide ragnar smug with moveoutright
        hide ruth blush with moveoutright
        "A whole HOUR?!"
        "OR TWO?!"
        "Scribbles?! Are you hearing this?"
        "Am I in actual heaven?"
        un eyeroll"Yeah yeah, I'm seeing your incredible charisma getting all the bitches."
        "You don't sound too impressed."
        un bored"You are going to fuck three Nightfallen that would do almost anything to fuck ANYONE from your kind."
        un "Trust me, it's not that impressive."
        "What matters is that I'm going to have a good time."
        un "Aha, sure, as a side note, you want me to cast an anti pain aura on you before you start?"
        "Why would I want that?"
        un suspicious"{i}*Cough Cough*{/i}"
        un "Do you not feel anything poking you in the back?"
        un bored"Cause I do."
        "Now that you mention it... there is an arm hitting my spine every so often..."
        "It's Ruth's dick isn't it?"
        un "Yup."
        "..."
        "I bet I can fit him."
        un "I don't doubt you'll try and succeed, slut, but do you want it to hurt like hell or feel actual pleasure?"
        "Alright, I give you permission to cast antipain auras on me, but not super strong ones."
        un "Thanks, maybe this way I might enjoy myself as well, instead of having to hide in the back of your mind to not get traumatized."
        un squint"Seriously, mortals these days are getting too brave."
        stop music fadeout 2.0
        scene black with llongdissolve
        play sound "audio/doorclose.ogg"

        "Before I realize it, my feet touch the ground, and a door closes behind me."
        "We're here."
        play music "audio/jazz2.ogg" fadein 3.0 volume 0.3
        scene wildsex1 with longdissolve
        "The lodge is indeed more spacious and a bit secluded from the main camp."
        "The interior is full of silks, tapestries and most importantly, a large, soft looking bed with countless pillows around it."
        "It looks like something you'd find at a fancy love hotel."
        "Natural aromas fill the air from the burning incense, wild roses and daisies in particular."
        eu "What do you think?"
        y nakedss"You didn't lie about it being {i}'comfortable'{/i}."
        ra "Wait until you actually feel it."
        scene wildsex2 with longdissolve
        scene CGcc24
        "They unpin my loincloth from behind and push me on the bed."
        "I turn around as my garment slides down, covering my front perfectly from the six, predatory eyes, staring at me from the foot of the bed."
        "All three men attractive in their own ways, all three impatient to do unspeakable things to me."
        "With all that being said, a moment of clarity comes through between the horniness, I can't help but ask myself..."
        "In a world where hunters watch their job partners have sex with Nightfallen on the regular, would my cat partner be upset about me doing my job?"

        menu:
            "Should I continue this?"

            "Invite them further.":
                $ sex2 +=1
                "I absolutely should."
                "This is a once in a lifetime experience, since Wild Furs should technically be left alone."
                "There is no reason for a hunter to ever have sex with Wild Furs... unless you have a special bond with them and are doing it for pleasure alone, like me."
                if sex >=1:
                    "Besides, it's not like I'm a virgin anymore, so that's out the window."
                    jump wildsexx


                else:
                    label wildsexx:


                    "These three stand in front of me, with smug expressions and lust in their eyes."
                    "I still can't shake the feeling this is a dream, or that they're just too good for me, so the shyness stereotype is not wrong at all."
                    "That doesn't stop me from making the first, major move."
                    scene wildsex3 with dissolve
                    scene CGcc25
                    "I grab the cloth off my crotch, revealing my growing erection."
                    "They seem a little surprised by my bold move."
                    y nakedss"I guess I'll be the first one to get naked, if we got this far."
                    ra "Only natural for the guest to do the honor."
                    "I expected to be suffocated by three bodies all at once, but of course these are not amateurs."
                    "Ruth and Ragnar grab pieces of Eureka's clothes, lifting them up or unpinning any clasps that keep the outfit together."
                    "As the one with the most layers, without help, he'd be the last to join the action. With teamwork, he's the first to greet me in bed."
                    "What a pair of gentlemen."
                    scene wildsex4 with llongdissolve
                    scene CGcc26
                    "Eureka's hourglass figure slithers through the sheets, until he's behind me."
                    "He nuzzles my neck as I try my hardest not to blush."
                    eu "Let's start simple, darling."
                    "With a playful yet firm grip, the feline's velvety, fur-covered hand closes around my now hard shaft."
                    "The softness of his touch combined with the intriguing texture of his fur sends waves of pleasure coursing through my body."
                    "His agile fingers skillfully caress me, tracing tantalizing patterns along my most sensitive areas, which are all the areas when someone like him touches me."
                    "His paws move with expert precision, alternating between gentle strokes and firmer squeezes, perfectly attuned to my reactions."
                    y nakedhurt2"Ah!"
                    eu "Slower?"
                    y "Mmhmm..."
                    eu "How about a little spin?"
                    y "Oohh..."
                    "Time seems to blur as the feline's relentless movements intensify."
                    "The friction created between his fur heightens the sensations, amplifying the erotic symphony playing out between us. "
                    "When suddenly, everything stops."
                    y nakedsurprised"Huh?"
                    eu "We don't want to make you pop just yet, do we?"
                    scene wildsex5 with llongdissolve
                    scene CGcc27
                    "The other two have been enjoying the show while undressing, and Ragnar is the next to join us."
                    ra "I hope you don't mind me keeping something on."
                    ra "I learned from your kind that sometimes {i}some{/i} clothes are better than none."
                    "His large, throbbing cock now resting on my shoulder right next to my face is hot enough on its own, but combine it with the wavy, wrinkled piece of silk it comes through, oh man..."
                    y nakedawkward"You did some good, successful research."
                    ra "Hope you can fit it all, because I want to give you more than just a taste."
                    "One of his hands caresses the back of my head, while the other moves his cock across my lips, teasingly."
                    "I open my mouth obediently despite the awkward angle."
                    ra "Nuh uh, it's not time yet, the star of the show still needs his turn."
                    "The scent of his meat almost puts me in a trance."
                    "A trance that is broken by rising anxiety."
                    eu "Come on, big guy."
                    "The whole time, Ruth has been stroking his shaft, waiting for permission."
                    "The bear's large, hot rod is releasing steam from the cold, thick substance he used to cover it with."
                    eu "Be gentle now."
                    y nakedblush2"Yes please."

                    "He followed Ragnar's lead and left an ornament around his waist, simply for aesthetics."
                    "Thankfully he's not as large as I thought, still massive, but not an ass destroyer."
                    "At least not with the anti pain aura on me, I hope."
                    "He has some courtesy to prepare me, kneeling down and shoving his tongue in and around my hole."
                    "My loud moan makes Eureka hug me tighter and bury his nose deeper into my neck."
                    "Soon, long, meaty, furry fingers are probing me, before going inside as well."
                    "After some more thrusting and stretching, he gets up and places the slippery tip of his penis resting on the base of my tail."
                    "Both guys around me come closer and hold me tighter, basically immobilizing me."
                    y nakedss"What are you-"
                    scene wildsex6 with llongdissolve
                    scene CGcc28
                    y nakedsurprised"OooOoh-"
                    y nakedhurt2"Aah!"
                    eu "Shhshh, it's okay."
                    y "Holy FUCK, y-you're big."
                    ra "Stop a second."
                    "Ruth stops moving as I regain my breath."
                    ru "Sorry."
                    y "I-it's fine, you can try again now."
                    "This time, I grit my teeth and focus on Eureka's words of encouragement and Ragnar's thighs pressed against me."
                    ru "Tight..."
                    "Before I know it, my insides are completely filled, a pair of heavy balls gently touching my cheeks."
                    eu "Good job, you took him balls deep."
                    eu "How does it feel?"
                    y "Full...so very full."
                    ra "Is that a good thing?"
                    y nakedss"The best."
                    ru "Hmm, I move."
                    "The bear pulls his hips back, holding on to my leg, before thrusting forward cautiously."
                    "Each shove is slightly rougher than the last, until the fat and muscle all over my body jiggle like jelly when the force of his powerful thighs hits my ass."
                    "The other two participants have to hold me from getting pushed too far back on the bed, as my partner gets lost in lust."
                    "The bear's grunts echo through the room, overwriting whatever noises of pleasure I was making, until it all builds up to an intense climax."
                    "Finally, in a moment of ecstasy and a couple more hard shoves, the girthy cock inside me pulses intensely, erupting with hot, satisfying seed."
                    "His essence of lust travels deeper inside than any dick can reach, almost making me lose control, in a phenomenon often referred to in the modern word as simply 'cum brained'."
                    "A name well deserved."
                    "I feel his heavy breaths wash over my face, then the pressure inside slowly leaves, letting the intrusive fluids spill out, warming up my whole bottom side as it runs down like a waterfall."
                    scene wildsex65 with longdissolve
                    eu "Good job Ruth, you managed to avoid making him cum."
                    ra "Now we can take care of that."
                    "He was specifically trying to avoid my sweet spots inside, and yet, it still felt heavenly."
                    "Ruth has a satisfied expression on, and a blush crosses his cheeks stronger than ever before, as if thinking 'I can't believe I actually did it'."
                    "He grabs the base of my tail and runs his fingers through my fur, up to the tip, which I interpret as a kind of thank you gesture."
                    y nakedsmug"Feels good getting rid of all that lust, huh bud?"
                    "He gives me a thumbs up and a hearty, toothy smile, before sinking into a chair, watching the rest of the show with lazy eyes."

                    "Next up, Eureka and Ragnar take the stage, teaming up for a final, powerful, double attack."
                    eu "Your tail hole got filled up, it's only fair if you fill one up yourself, right?"
                    y nakedblush3"I'd say that's a good deal."
                    "The feline's lithe, tall body moves slowly and tantalizingly on top of me."
                    "I can feel the same substance Ruth used covering his hole as he grinds back and forth along my shaft."
                    "A completely unnecessary gesture, cruel even."
                    "His grey-ish brown pelt shimmering in sunlight, accentuating his flexible figure."
                    y "Do I have to beg? Because I can't wait to be inside you."
                    eu "I know it's true if you're bold enough to say it, but first..."
                    ra "You don't think you get to fill up my partner without consequences, do you?"
                    ra "A fee must be paid."
                    y "I'll pay any price."
                    ra "Good, then open up wide for me, and we'll be even."
                    eu "Please do it [name], I want you inside me so bad."

                    "Nightfallen like to roleplay as well, apparently, and how lucky am I for that?"
                    "The spotted cat gets up from his knees, standing in front of me, dangling his cock and lightly slapping me with it, before resting it on my snout, between my eyes."
                    y "If that's what it takes."

                    scene wildsex7 with longdissolve
                    scene CGcc29

                    "I open my mouth obediently."
                    "Ragnar's dripping rod gives my tongue the first taste of what is going to invade my mouth for the next couple of minutes."
                    "Although not as intimidating as the bear's cock, this one's going somewhere I'm far less experienced."
                    "Soon, the salty, musty tip hits the back of my throat, and my leader gives Eureka permission to go."
                    "Another heavenly sensation hits my body the next second."
                    "Since Ruth and Ragnar's actions can hurt me, they both start gently, while the skinny feline slams down ferociously, absorbing my dick whole in an instant."
                    "The warm, soft, cushioned feeling engulfing my dick takes me by surprise."
                    "His hip movements are vicious and confident."
                    "There are three sensations overwhelming my body right now."
                    "The pleasure created by an experienced, talented ass."
                    "The pressure the intrusive cock creates trying to go down my throat."
                    "And the soft yet deadly paws, with sharp claws sticking out, resting on my belly as Eureka bounces like I'm his personal trampoline."
                    "Ragnar meets no resistance from me, as I try to keep my arms down and enjoy the moment."
                    "That prompts him to shove his whole length in, satisfied when his balls meet my chin."
                    "Every couple of pushes, he takes it out just to ask me questions, teasingly."
                    ra "How's that ass feeling swallowing your cock?"
                    y nakedhurt2"{i}*Heavy breathing*{/i} He's really some-Agh-"
                    ra "Oops, sorry, were you saying something?"
                    ra "My dick was getting cold."
                    "His dominating manners excite me more than anyone can imagine."
                    "The taste of his meat now imprinted in my mouth, or throat, to be more exact."
                    ra "Don't be shy, you can squeeze me if you need some air."
                    ra "Although it seems like so far, you're doing better even than my partner."
                    eu "Are you trying to make me jealous?"
                    ra "Look who's asking, I never even knew you can move like that, you little cock dancer."
                    eu "Heh, I had to go all out for our guest here."
                    "I curl my toes and clench my cheeks."
                    "The libido created by these two's synchronized movements is through the roof."
                    "I grab Ragnar's left butt cheek and give it a panicked squeeze."
                    ra "Me too little guy, me too."
                    "Instead of pulling out he goes in deeper and harder, tilting my back further in the process."
                    eu "Ah! I'm about to-"
                    scene wildsex8 with longdissolve
                    scene CGcc30
                    "I grab on for dear life, as two other voices moan and grunt at the same time as me."

                    "I've experienced cum inside my backside, but having it pumped in from the front is something else."
                    "His shaft pumps load after load, until he gets it out only half way, so he can paint the inside of my mouth as well."
                    "My lips sealed tight around it, trying to contain his lust, but ultimately failing, it is just too much."
                    "In the meantime, on my own end, Eureka drops down on my dick one last time, containing as much of it as he can inside, before I bust in sync with him."
                    "His hot seed covers my stomach, while mine fills him from the inside, spilling out and running down my balls and in between my thighs."

                    "Both men slowly remove the used tools, before falling on top of the bed on either side of me."
                    "All three of us breathe heavily, grunting and even moaning, since the pleasure from the excessive amounts of cum are giving us reasons to do so."

                    scene wildsex9 with longdissolve
                    scene CGcc31

                    eu "What,{i}*huff*{/i}, what did you think?"
                    y nakedblush3"I-I think I'll taste cum for moons."
                    y nakedsmug"And I didn't expect such violence from someone like you."
                    eu "I told you deepthroating him with that monster is a bad idea-"
                    y "I was referring to you, Eureka."
                    eu "Oh!"
                    "He giggles."
                    eu "Well, I wasn't lying when I said I wanted you inside me."
                    eu "I thought I was going crazy."
                    y "Crazy with lust?"
                    ra "Now it's gone, thanks to you."
                    un sidee"I...I enjoyed this as well, actually."
                    un "Surprisingly."
                    "Ha!"
                    "Knew you'd like the slut life."
                    "I'm happy for you."
                    un "..."
                    "Ruth brings us towels to clean up."
                    ru "Now...what?"
                    ra "Stick to the plan."
                    ra "Hope you didn't fall in love or anything, Ruth."
                    ru "Hmm..."
                    ra "Eureka?"
                    eu "Yeah yeah."
                    "The two of them get up, walking in opposite parts of the room."
                    eu "Hey, [name], look over here for a second."
                    y naked"What is it?"
                    eu "I had fun, I really did, we all did, you're amazing!"
                    eu "I never knew your kind can take it and give it like that."
                    eu "The Chief does not allow us to do these kind of things with your kind, so this was my first experience, a great first impression."
                    y nakedss"Thanks, but you three were the real mvp's here."

                    eu "So I just want you to know that I'm sorry."
                    y nakedsimple"Sorry? What are-"
                    stop music
                    play music "audio/dramatic.ogg" fadein 3.0 volume 0.9
                    scene wildsex10 with hpunch
                    "A cold, sharp dart pierces my neck, and paralyzing liquid gets pumped into me."
                    un surprised"Fuck."
                    un "That's a sleeping dart, just tell me to nullify it."
                    scene wildsex11 with dissolve
                    "N-no, it's f-fine..."
                    un ang"WHAT?!"
                    un "WHAT DO YOU MEAN {i}'FINE'{/i}?"
                    un "I CAN'T DO SHIT IF YOU'RE UNCONSCIOUS!"
                    un "LET ME CURE THE POISON, ORDER ME TO HELP YOU DAMN IT!"
                    "T-they're nice...nice people."
                    "I'm sure it's just a..."
                    "{size=30}Misunderstanding.{/size}" with llongdissolve
                    un scared"Hello?"
                    stop music fadeout 2.0
                    scene black with llongdissolve
                    play sound "audio/button.ogg"
                    un ang"HELLO?!"
                    play sound "audio/button.ogg"
                    un "ARE YOU FUCKING KIDDING ME?!"
                    play sound "audio/button.ogg"
                    un squint"AAAGGHH! WHY ARE YOU SO STUPID?!"
                    play sound "audio/button.ogg"
                    un sidee"What do I do, what do I do, what do i-"
                    play sound "audio/button.ogg"
                    ra "What are you so upset for?"
                    play sound "audio/button.ogg"
                    un simple"I can still hear..."
                    play sound "audio/button.ogg"
                    ra "He's asleep, he can't see you act like you care."
                    play sound "audio/button.ogg"
                    eu "I'm not acting...I kind of liked him."
                    play sound "audio/button.ogg"
                    ra "You ride his dick once and catch feelings?"
                    play sound "audio/button.ogg"
                    ra "I had to do that to you dozens of times before you finally gave in."
                    play sound "audio/button.ogg"
                    eu "Because I was unconscious almost every time..."
                    play sound "audio/button.ogg"
                    ra "Well it's not MY fault you decide to keep your lust in until you faint."
                    play sound "audio/button.ogg"
                    eu "He wasn't even supposed to be the one to-"
                    play sound "audio/button.ogg"
                    ra "I'm not using my brother for the ceremony."
                    play sound "audio/button.ogg"
                    ra "We had to do this."
                    play sound "audio/button.ogg"
                    ru "Step...brother."
                    play sound "audio/button.ogg"
                    ra "Not you too."
                    play sound "audio/button.ogg"
                    ra "I liked [name] as well, okay?"
                    play sound "audio/button.ogg"
                    ra "I didn't think I would but I did."
                    play sound "audio/button.ogg"
                    ra "I'm not necessarily {i}THRILLED{/i} about this."
                    play sound "audio/button.ogg"
                    ra "Just... take him to the place, make sure my brother doesn't see you."
                    play sound "audio/button.ogg"

                    un curious"What...ceremony?"
                    play sound "audio/button.ogg"
                    un sidee"Have I heard of any rituals with Wild Furs and Dragons?"
                    play sound "audio/button.ogg"
                    un sidee"Hmmmm."
                    stop music
                    jump meanwhile




            "I can't do this...":
                "I have to put a stop to this."
                un "Huh, didn't expect this decision from you."
                un "I really thought you're dying to try some Nightfallen dick."
                "My affection for a certain cat is stronger than my lust."
                "Even if I almost forgot about my priorities..."
                ra "Well, Eureka, wanna do the honors?"
                eu "As the one with the most clothes on, it would be my pleasure, just let me-"
                y nakedsurprised"W-wait, wait."
                ra "something wrong?"
                y nakedsad"I'm...I'm sorry, I can't do this."
                y "I know I led you on a lot, and I shouldn't have."
                y "I guess I succumbed to the power of lust myself."
                y nakedss"But the truth is...there is somebody I like, somebody I love, and I don't want to betray them."
                "The three men look at each other, Ruth sadly, Eureka worryingly and Ragnar with a slight flown in his brow."
                ra "You...want to stop?"
                y "If you don't mind, I apologise again."
                eu "We...understand, [name]."
                y "Thank you."
                ra "Eureka?"
                eu "I'm on it..."
                eu "[name], would you look here for a second? I wanna show you something."
                "He moves on the other side of the room."
                y "What is it?"
                eu "I...We, really like you, [name]."
                eu "You're truly a nice, beautiful person, even if we're not the same."
                eu "So that's why..."
                eu "I'm sorry...we're sorry."
                y nakedsimple"You're sorry? For wha--"
                stop music
                play music "audio/dramatic.ogg" fadein 3.0 volume 0.9

                scene wildsex20
                "Something cold and sharp pierces my neck, numbing liquid pulsing through my veins a second later."
                un surprised"Fuck."
                un "That's a sleeping dart, just tell me to nullify it."
                scene wildsex21 with dissolve
                "N-no, it's f-fine..."
                un ang"WHAT?!"
                un "WHAT DO YOU MEAN {i}'FINE'{/i}?"
                un "LET ME CURE THE POISON, ORDER ME TO HELP YOU DAMN IT!"
                "T-they're nice...nice people."
                "I'm sure it's just a..."
                stop music fadeout 2.0
                scene black with dissolve
                "Misunderstanding."
                play sound "audio/button.ogg"
                un simple"Hello?"
                play sound "audio/button.ogg"
                un surprised"HELLO?!"
                play sound "audio/button.ogg"
                un ang"ARE YOU FUCKING KIDDING ME?!"
                play sound "audio/button.ogg"
                un "AAAGGHH! WHY ARE YOU SO STUPID?!"
                play sound "audio/button.ogg"
                un sidee"What do I do, what do I do, what do i-"
                play sound "audio/button.ogg"
                eu "What do we do now?"
                play sound "audio/button.ogg"
                un "Huh?"
                play sound "audio/button.ogg"
                un simple"Oh, I can hear them."
                play sound "audio/button.ogg"
                eu "We failed...the Chief is going to-"
                play sound "audio/button.ogg"
                ra "We only failed if anyone checks, and nobody will check his holes."
                play sound "audio/button.ogg"
                eu "But the ceremony!"
                play sound "audio/button.ogg"
                eu "It asks for someone that is NOT a virgin."
                play sound "audio/button.ogg"
                ra "We don't even know that for sure."
                play sound "audio/button.ogg"
                eu "Oh be serious, look at him, how can he not be?"
                play sound "audio/button.ogg"

                un sidee"Ouch, good thing you aren't here."
                play sound "audio/button.ogg"
                ra "Didn't you say you like him?"
                play sound "audio/button.ogg"
                eu "I mean, he's nice, but definitely not made for our wild sex life..."
                play sound "audio/button.ogg"
                ru "Fuck? Now?"
                play sound "audio/button.ogg"
                ra "No, you idiot, he had to consent to it, it's useless if we force him, that was the whole point of kissing his ass the whole day."
                play sound "audio/button.ogg"
                ra "And my own whore ruined everything."
                play sound "audio/button.ogg"
                eu "How is it my fault?!"
                play sound "audio/button.ogg"
                ra "Oh I don't know {i}'YoU cAn SaY No If YoU Don'T wAnT tO Do iT.'{/i}"
                play sound "audio/button.ogg"
                ra "I thought I taught you their idea of {i}'peer pressure'{/i}."
                play sound "audio/button.ogg"
                ra "I put too much trust in you."
                play sound "audio/button.ogg"
                ra "Ruth, take him to the place, make sure my brother doesn't see you."
                play sound "audio/button.ogg"
                ra "Hopefully my father doesn't check...or he'll want another one."
                play sound "audio/button.ogg"
                ra "I can't afford to lose another one."
                play sound "audio/button.ogg"
                ra "Lets just hope this works, once and for all..."

                un suspicious"What...ceremony?"
                play sound "audio/button.ogg"
                un sidee"Have I heard of any rituals with Wild Furs and Dragons?"
                play sound "audio/button.ogg"
                un "Hmmmm."
                jump meanwhile



    "Stay in the camp.":
        scene camp6
        stop music fadeout 3.0
        show eureka
        show ragnar at right
        show ruth at left5
        "There are too many things in this camp my mind is focused on for me to go wandering about."
        "And I don't want to leave my friend far out of my sight."
        show ragnar sadsmile at right
        show eureka sadsmile
        show ruth simple at left5
        play music "audio/celtic1.ogg" fadein 2.0 volume 0.4

        y nakedss"Sorry, I'd love to spend time with you, but if you don't mind, I have some things I want to do around camp."
        eu "Oh, that's fine."
        eu "We would've loved to spend some more time with you before we have to say goodbye too, but I get it."
        "He looks towards the narrow path, where Ku'sani resides right now, and smiles back softly."
        ru "[name] no come?"
        y "Sorry big guy, maybe another time."
        ra "I suppose after a whole afternoon spent here, and with your new attire, nobody should give you trouble."
        show ragnar at right
        ra "If anyone does, tell me and I'll take care of them."
        y "Most of your tribe mates are locked in huts anyway."
        show ragnar smug at right

        ra "Heh, of course, the common afternoon lust."
        ra "We should do that too when we get back, Eureka."
        show eureka smug
        eu "Been waiting for that all day."
        show ruth at left5

        ru "Ruth want join!"
        ra "The more the merrier."

        scene camp6 with llongdissolve

        "They leave the camp, hand in hand, talking and laughing like best friends."
        "I almost feel bad I refused their invitation."
        "Who knows, maybe it would've blossomed into something more than a forest trip."


        "No more overthinking, live in the present not the past, and the present tells me to move my attention to the spilled bucket."
        show lizard down at right2 with dissolve
        show wild2 angry at left with dissolve
        "The Wild Fur responsible is now screaming and kicking at the lizard, gesturing at the mess created."
        show lizard down at right2 with hpunch
        wf "Stupid lizard, look where go."
        show lizard down at right2 with hpunch
        wf "Go down and every pick up grain."
        wf "Or you want more no food day?"
        wf "Ahg chul'li piost tol'ta..."
        hide wild2 angry with moveoutleft
        "Although the violence is leaving a bad taste in my mouth, I can't help but worry for the Wild Fur."
        "His kicks are like a toddler's hits, against the tough, scaly skin of the lizard's sides. Barely even flinching."
        "I think he hurt his foot, trying to hide his limp as he walks away."
        show lizard down at center with ease
        "Not to mention that the lizard could simply bite his head off and be done with it, but instead, he kneels down and starts gathering each grain by hand, until the Wild Fur gets bored and walks away with a last spat and scornful look."


        "That is going to take forever..."
        "The fact that most of the camp is covered by grassy patches with small rocks scattered around won't make it any easier."




        "I don't want to make assumptions, but I haven't seen the lizard eat anything while I was here."
        "His job at the feast was making sure the torches were kept lit and no fire started by accident, as well as pouring drinks whenever the actual servants were busy with something else, like massaging the Chief's shoulders and feet."
        "I have to keep in mind that intervening would also be a bad idea, especially without Ragnar, Eureka or Ruth around."
        stop music fadeout 2.0
        scene camp2 with llongdissolve

        "I make my way back to the feast part of the camp."
        "The excitement about these new {i}'guests'{/i} has died down, nobody gives me more than a glance."
        scene forestpath with fade

        "At least I won't attract attention to what I'm about to do."
        play music "audio/forgetmenot.ogg" fadein 3.0 volume 0.4

        scene flowers2 with fade
        "Oh, would you look at that, I was wrong again!"
        show wilddance zorder 1 with dissolve

        "Everything is so peaceful in other parts, because my friend decided to show off his powers in this clearing, stirring a crowd."
        "The cat is flying Nightfallen very high in the air, before letting them drop slowly with his floaty magic, however that works."
        "He does it again, and again, and again, while being cheered on, wails of excitement even scaring the wyvern."
        "He notices me and teleports in my face next."
        show cat20teleport zorder 2 with dissolve
        show cat20 zorder 2
        hide cat20teleport with dissolve

        ku "Hey, what'cha doing?"
        ku "Want a go in the Ku'sani ride?"
        y nakedsimple"No thanks, I know what that's like."
        t "Your loss."
        y "Are you sure it's wise to fly multiple people like that?"
        y "Combine it with teleporting and other things?"
        y "You know we just had a battle earlier, right?"
        y "You should be conserving your energy."

        hide cat20
        show cat20smile zorder 2

        t "Pff, it's fine, mom, I'm full of magic and energy after that meal."
        t "And I can't let everyone down, look how happy they look while falling!"
        y "I just want you to be safe."
        t "I will make sure to leave a little bit so we can go home."
        t "And if I somehow go overboard..."
        t "We can just stay here one more day! No big deal right?"
        hide cat20smile
        show cat20smug zorder 2
        t "Just you...and me...sharing a tent, noooobody else around."
        y nakedbored"We have a TEST tomorrow!"
        y "Did you already forget?!"
        hide cat20smug
        show cat20simple zorder 2
        t "Oh...that."
        t "Well..."
        y "..."
        hide cat20simple
        show cat21bored zorder 2
        t "Don't make that face, I promise I'll have enough magic to get us back, ok?"
        hide cat21bored
        show cat21simple zorder 2
        t "Promise."
        hide cat21simple
        show cat20smile zorder 2
        t "In fact, we'll go right after I'm done here."
        t "Give me like, twenty minutes."
        y nakedsimple"{i}*sigh*{/i}"
        y nakedss"Alright, I'm just glad you're fitting in with your family."
        t "Thank you."
        t "Now, if you'll excuse me."
        show cat20teleport zorder 2 with dissolve
        hide cat20smile
        hide cat20teleport with dissolve
        "He teleports back to the cheering crowd, picking another Nightfallen to {i}'give a ride'{/i} to."
        hide wilddance with moveoutleft
        stop music fadeout 3.0

        "He values honesty above all else, so I shouldn't be worried he'll break his promise."
        "I have other things to worry about, after all."
        "There are a lot of leftovers, I would be surprised if they won't throw at least some of it away."
        "Hopefully that means nobody will realize some of it is missing."
        "I choose a wide piece of flatbread, that I stuff with as much meat as it can hold. Fish, boar, duck, whatever the blue colored one is, you name it."
        play music "audio/celtic1.ogg" fadein 3.0 volume 0.4

        scene forestpath with fade
        scene camp6 with fade


        "I bring my food package back to the main camp, where the lizard's progress in picking up the grain is barely noticeable."

        "As I approach, despite the smile I'm trying to keep, he starts collecting the grain faster."

        show lizard down with dissolve

        y nakedss"Hey..."
        y "Hey, wait."

        "He stops, but doesn't raise his head to look at me."
        "I squat down in response."
        "Seeing his head dip even lower, I get on my knees, to be as small as possible."


        y "Here."
        y "You must be hungry."
        show lizard

        "He only now dares raise his gaze, his eyes wide, fixated on my offering but not making a move."

        "I gently and slowly place my hand on his, and raise it."
        "His chained, rough hand, almost twice my size."
        "Dangerously sharp claws in sight, pared with hands strong enough to crush skulls, information that makes me nervous, but I can't back down now."
        "I place the food in the reluctant palm, and he starts eating, there and then."
        show lizard eat
        "Thankfully, the thin pieces of cloth around his muzzle do not do much to slow him down."




        y naked"Now what's this all about then?"

        "I start gathering the grain in his stead while he's busy."
        "Something I quickly realized is completely ridiculous."
        "It really feels like there's no end, each piece I grab seems to spawn another, not to mention the dirt you have to clean."
        show lizard
        "The lizard finishes the food with a last satisfying bite and rushes to help."
        "His large fingers, although furless, are even less useful in this situation."
        "They spend more time brushing against mine than picking grain."

        un bored"Cool, you're having a moment with a literal animal."
        un "Somebody call the police."
        "He's not an animal, you ignorant excuse of a demon."
        un simple"Wow, that felt a bit personal."
        un bored"Call me when it strangles you to death, so I can laugh."
        "Better yet, I'll call you right now, to help us with this stupid grain that dumbass wild fur made him spill."
        "And if you hit me with the {i}'why should I'{/i} question one more time, I'm holding my breath until I pass out."
        un simple"..."
        un suspicious"You're becoming more and more unlikable."

        show lizard surprised


        "My request, or more like threat, worked, as all the remaining grain (which was a lot more than I thought) rises up through the grass and dirt and flies into the bucket."
        "It's so nice of you to show up again, by the way, even if it was just to insult me, what's the occasion?"
        un "My favorite character in that show moved jobs...they just got him out for no reason."
        "Ah, I remember that part, it did suck."

        "The lizard seems surprised by the spontaneous magic."

        y naked"Don't worry, that was me."
        y "Here."
        show lizard bucket

        "We get up and I hand him the bucket, I wouldn't mind carrying it myself, but we're already getting weird looks from the few Nightfallen still around, just because I stand so close to him, if he walked around empty handed while the guest was carrying the weight, that would not generate good responses."
        y "Do you have a name?"

        "He does not respond, but glances my direction."

        y nakedsimple"I suppose if so many Wild Furs don't have a name, a Savage one won't have one either, huh?"
        y naked"Do you mind if I call you {i}'lizard'{/i}?"
        "He cringes for a second, but no response again."
        y nakedss"Perhaps not."
        y "Do you mind me giving you a name?"
        "He..nods?"
        y "Oh, ok, in that case..."
        "It's best to stay away from the Wild Furs' traditional way of naming."
        "Something simple, something that defines him but not in an obvious way?"
        y "What about Gael?"
        show lizard blush
        "The lizard looks startled for just a moment, before...blushing?"
        "Blushing and nodding slowly."
        "He likes it way more than I thought he would."
        "My heart will never be strong enough to tell him that I took the name from a video game character, a slave knight."
        "Not that he'd even know what a video game is."
        "I can feel Scribbles' muted laughter in the back of my mind."
        "What's so funny?"
        un tease"Do you even know what that name means in the old language?"
        "No? I just took it because it fits him."
        "What does it mean?"
        un "Beautiful and generous."
        un "You're basically flirting at this point."
        "That just makes me like the name more."
        un simple"B-but, wait, you're supposed to be embarrassed."
        un ang"I thought you missed my teasing!"
        "You're gonna have to try harder."
        scene camp4 with dissolve

        "In the meantime, we get to a storage area that slumps underground a couple of feet."
        show lizard with dissolve
        "He dumps the bucket in a large barrel before coming back out."
        show lizard angry with hpunch
        "I attempt to follow to our next destination, but he turns around and blocks my way, looking me in the eyes with a determined look, as if asking {i}'what's your deal?'{/i}"
        y nakedss"I just think you deserve a break, but I don't have the authority to give you one, so I decided to help you."
        y "Can we go now?"
        show lizard angry with hpunch
        "That is not a satisfactory answer for him."
        y nakedsimple"Look, my friend, you know, the little black cat, is too busy with his new life."
        y "The new friends I made are away from camp, so if you want to know why I won't leave you alone, it's because I'm bored."
        y "Can you accept love out of boredom?"
        y "It's not fake kindness, it's just conditional."
        show lizard with dissolve
        "I don't know how much of that he understood, but it was enough for him to soften his expression and body language, and allow me to accompany him further."
        y naked"So, where to, chief?"
        "He cringes again."
        y "Right, the Chief is your leader...uhmm, where to, boss?"
        "Gael points towards the burned up pillar."
        scene camp55 with dissolve
        "Ashes of flowers and other offerings that were around the pillar littered the ground and the immediate vicinity."
        "Not to mention the half burned pillar that still stands, looking black and fragile but still heavy."
        show lizard down with dissolve
        "He picks up another, larger bucket than the one before, and starts gathering the ashes with his bare hands, as they crumble to dust at the faintest touch."
        y nakedsimple"You...you have to gether all the ash?"
        "He nods."
        y nakedsurprised"Everything?"
        "He nods again."
        y nakedangry"What is this?"
        y "Who the hell do they think you are? Cinderella?"
        show lizard surprised
        "Gael stops to look at me, curious about my little outrage."
        y "Nuh uh, gather the grain from the grass, then the ashes from the sand and dust, what's next? You're not allowed to the ball?"
        show lizard
        "He tilts his head curious."
        "Scribbles, do something about this."
        un curious"What do you want me to do?"
        "Can you teleport all this crap out?"
        un bored"I'm not good at teleportation, but even if I was, I could only work with the big pieces."
        "I don't know your powers, just find something useful!"
        un "I could probably gather every piece of ash in the camp in one spot, and then throw everything as far as I can."
        "How far is far?"
        un "A mile over the trees?"
        "Perfect! Do that!"
        un "Hold your lizards, you don't have the energy for that."
        un "A spell like that takes a lot of resources."
        un "You need to find a source."
        "Would one of those crystals from the feast work?"
        un "Those would be perfect, but I doubt you want to be caught sucking off the light from one of those."
        "Well said..."
        "Do you think... Gael?"
        un simple"Oh, ermm, yeah, sure."
        un "If he has enough energy, then he might work."
        un "You're trading the energy he would typically use to do this job to do it instantly, so I see nothing wrong there."
        un bored"Just make sure not to take too much, since I doubt anyone is fucking a Savage Fur regularly, so his energy could be on the lower side."
        "Got it."
        y nakedss"Gael, do you mind if we hold hands for a moment."
        "I kneel in front of him and hold my hands patiently."
        show lizard down
        "He looks at his own chained wrists and black palms, trying to decide."
        show lizard close with dissolve
        "Finally, he gives in, and gently pushes his fingers forward, as I intertwine them for maximum contact."
        "I focus and imagine draining him."
        "I can feel his anxiety as the energy flows away from him, but he keeps calm."
        "Is this enough, Scribbles?"
        un "Barely."
        "Can you perform the spells anyway?"
        un "Yeah, but it will take a bit of a toll on your body, not as bad as it would have if you didn't do this, but still."
        "It's okay then, just do it, I don't want to steal too much from him."
        un "Your wish."
        show lizard with dissolve
        "I gesture to Gael to get up and take a few steps back."
        "Then the pillar begins to rise, removing itself from the ground, leaving a deep hole of at least four feet."
        "How is anyone supposed to take that out...?"
        "Small flakes of ash then fly towards it from all directions."
        "From the roof of huts, from the branches of trees, even someone's loincloth."
        scene camp6

        show lizard surprised
        "All of it sticks tightly to the pillar, even the smallest particle of ash, then it shoots in the air like a rocket, disappearing above the trees."
        show blink with dissolve
        "Gael's expression in complete awe, is the last thing I see before my eyes close."
        stop music fadeout 1.0
        scene black with dissolve
        un "Yep, I knew it."
        un "Hopefully somebody finds you before he eats you alive."
        "Although my eyes are closed and I lost most of the control in my body, I can feel big, trembling hands wrapping around me."
        "After a short while, I sense the comforting warmth of hay against my back, followed by the sound of hasty footsteps fading into the distance."
        "Someone gently presses a cool, damp cloth onto my forehead before settling down in silence for the next ten minutes or so."

        "Finally, my fingertips regain their mobility, and I cautiously open my eyes, greeted by the sight of the hut's ceiling."
        play music "audio/outside2.ogg" fadein 3.0 volume 0.4
        scene lizardtent with longdissolve
        "A wide eyed lizard stares at me from a couple of feet away."
        show lizard surprised with dissolve
        "I sit up slowly and smile at him."
        y nakedss"Magic is a little dangerous to use sometimes, you know?"
        show lizard
        "Gael nods."
        y "Thank you for caring for me, I should probably-"
        show lizard close with dissolve
        "He hands me a clay cup, with some green-ish liquid, smelling strongly of wild herbs."
        y nakedsimple"What is that?"
        "He insists I take it."
        "It's warm, but that's where any positive adjectives stop. It tastes bitter, revolting, like medicine."
        y nakedhurt2"This is medicine, isn't it?"
        y "Did you get it from Eureka's place?"
        y "Please tell me you didn't leave hints you were there."
        show lizard with dissolve
        "He gets up, showing me a small burrow, filled with leaves and weeds."
        y nakedsimple"You have your own medicine, huh?"
        "Whatever I forced myself to drink just now does have good effects."
        "Soon, I no longer feel dizzy or fatigued, but still a bit weak."
        y "I appreciate you watching over me, but...what about your duties?"
        y "Won't you get in trouble?"
        "Gael shakes his head, showing his still ashy palms."
        y "They didn't think you'd be done with the ash cleaning so fast, so nobody gave you more tasks, is that right?"
        "Another nod."
        y naked"Good, because I don't want to work either."
        "I pat the seat next to me, on the makeshift hay bed, and he shyly complies, but not without complications."
        hide lizard with hpunch
        "As he gets up, his knees give in and he falls on top of me, quickly scrambling to get off."
        y nakedhurt2"Wow, you're heavy."
        show lizard blush with dissolve
        y nakedss"I-in a good way."
        y "Is everything alright?"
        "He looks away embarrassed, with his arms between his thighs."
        "The energy drain must've been a hit to him too..."
        "I'm gonna need to make it up to him, but first..."
        y naked"So, mister Gael, I want you to answer me this."
        y "Can you understand what I'm saying?"
        y "In general?"
        show lizard
        "Gael thinks for a second, then confirms my suspicions."
        un "What {i}'suspicions'{/i}? I thought it was obvious..."
        y nakedsimple"But you can't talk back?"
        "Negative response."
        "Why's that, Scribbles?"
        un "Savages can learn a language, even if slower than the average Wild Fur, but they don't have what it takes for actual speech."
        un "Grunts, roars and moans are all you'll hear from them."
        y nakedss"Did you learn my language from listening to Ragnar and Eureka?"
        "He nods, exuding a newfound confidence, as if my questions are beginning to appear more friendly rather than incriminating in his mind."
        y "How long have you been stuck here for?"
        "He raises eight fingers."
        y "Eight?"
        y "Years or moons?"
        show lizard down
        "Gael picks up a stick and writes in sand...eight X twelve..."
        show lizard
        y nakedpf"So eight years, and of course you know how to write numbers and some math, because why not?"
        "Gael scratches the side of his mouth, not used to others being impressed by his actions."
        "His chains clank and jiggle as he moves."
        "Scribbles...please remove his shackles."
        un s"Are you sure?"
        "Will that put me back to sleep?"
        un "No, it's a very simple spell."
        "Then yes, I'm sure."
        "A deep cut appears on the metal's surface out of thin air, and both wrist braces fall to the ground with a thud."
        show lizard freesur
        "Gael touches and rubs his wrists surprised."
        "In his eyes, I probably resemble some kind of powerful wizard that's solving all his problems with my magic."
        y nakedss"I want you to be free."
        y "You've served these Nightfallen enough, you deserve to-"
        show lizard freesur with hpunch
        "He shakes his head frantically upon hearing my words, reaching for the chains and trying to put them back on."
        y nakedsurprised"Huh?"
        y "Hey, what are you doing?"
        y "Don't you want to get out of here?"
        y nakedss"Don't worry, I'll help you get far away, they won't find you."
        show lizard freeclose with dissolve
        "For the first time, he touches me out of his own accord. Besides when I was unconscious, obviously."
        "His hands grab my shoulders, and he stares into my eyes, shaking his head again, slower, more determined."
        y nakedsurprised"I...don't understand..."
        y "Are you that afraid of them?"
        "Another head shake and an exasperated sigh follows."
        "He points to the bed."
        "Points to the roof."
        "Points to the bucket of water in the corner."

        "Shelter, warmth, water..."
        y "..."
        y nakedsimple"I understand what you're trying to say, but I still don't get it..."
        y nakedsad"Excuse me, I need some air."
        y nakedpf"Not that this place is that sealed shut...the door is a curtain."
        show lizard free with dissolve

        "He lets go with a last sad look in his eyes."
        "He didn't look sad while being kicked, or humiliated, or bossed around, but watching me walk out the door is another story."
        stop music fadeout 2.0
        scene camp4 with longdissolve
        play music "audio/outside.ogg" fadein 3.0 volume 0.4

        "I squat right outside, leaning on the hut's walls, not having the energy to take more steps."
        "Not like I need to run away or anything, but I do need to clear my mind."

        un "So?"
        y nakedsimple"So?"
        un "Finally realized you're not the hero of your self-crafted tale of fantasy?"
        y nakedsad"Did you ever taste defeat, but still have no idea how that happened?"
        un "I was locked in a crystal and reduced to this form, wasn't I?"
        un "A mystery to this day."
        y "So why am I always wrong about everything every time?"
        un simple"Your cat friend explained it perfectly."
        un "The world is not black and white."
        un "You decided to see his imprisonment as nothing more than the evilest of deeds."
        un "You flipped your opinion of these Wild Furs completely, upon seeing them mistreat someone that your kind literally kills for energy."
        y nakedsad"But what about him?"
        y "Does he even know about how unfair his situation is?"
        un "Safage Furs are solitary creatures."
        un "In the wild he would have to fend for himself, hunt, stay away from any tribes of Wild Furs or other Savage Furs as well, and demons."
        un "Not to mention the hunters that would kill him on sight."
        un "Didn't that Headmaster of yours say it at the opening speech two days ago?"
        un "Exterminate all Savage Furs on sight."
        un "Here, this Gael of yours has a bed, a roof over his head, food, water."
        un "He's protected from other tribes as well as hunters."
        y nakedsimple"And since he isn't allowed out of camp, he won't be forced to battle, or risk his life hunting for game..."
        un "Are you getting it now?"
        y "Yes..."
        y "I think I do."
        y "but he's also being deprived of lust draining."
        un "A small price to pay for a safe life."
        y "Yeah..."
        "Hopefully, my cat friend, {i}'Ku'sani'{/i}, doesn't have anything against my next decision."
        menu:
            "There is just one thing for me to do now."

            "I'll still help Gael, just in other ways.":
                $ sex2 +=1
                y naked"Alright, I made up my mind."
                un bored"Does that include leaving the lizard in peace?"
                y nakedsmug"No, quite the opposite."
                y "Everyone can be helped, you just gotta find the right way."
                stop music fadeout 2.0
                scene lizardtent with llongdissolve
                show lizard freesur with dissolve
                play music "audio/outside2.ogg" fadein 3.0 volume 0.4
                "I walk back in, Gael surprised to see me, sitting in the same spot."
                "I waste no time, kneeling in front of him and taking his hands in mine."
                "As big and strong as he is, his hands are gentle."
                "I brush away some more ash, while speaking softly."
                show lizard free
                y nakedss"Gael?"
                y "I get it now."
                y "You like your life."
                y "And just because I refuse to acknowledge it, doesn't mean it's not true."
                show lizard free
                "He seems satisfied with my answer."
                y "So, before I go, I want to give you something."
                y "A mutual benefit, or a parting gift, take it however you want."
                "I have to stand up to be at the same head level as he is now while sitting down."
                "Then-"
                show lizard freecloseblush

                "I plant a gentle kiss on his mouth."
                un eyeroll"God damn it."
                "I leave room for him to back away if necessary, and make sure I'm not too rough."
                "It's a loving kiss of kindness, soft and delicate."
                show lizard freeblush
                "I back away after a couple of seconds, watching for a reaction."
                "My head is still here, so that's a good start."

                "He stares into my eyes, his green scales turning red like a chameleon's."
                "His hand reaches for mine before I take another step back, holding it with care."
                "He opens his mouth, as if wanting to ask a question, but forgot he can't speak."
                "I don't need words to understand this kind of reaction."
                y nakedss"I doubt anyone in this camp slept with one of my kind in moons."
                y "Would you like to be the first one to satisfy your lust completely?"

                "He nods with a mixture of excitement and embarrassment."
                y "I'll be honest, I'm not very experienced in this sort of thing, especially not Nightfallen."
                y nakedsmug"So I give you permission to do whatever you want to me."
                "He looks taken aback."
                y nakedss"That sounded a bit kinkier than expected."
                y "Just, show me what I have to do and I'll do it."
                y "There's almost nothing I don't want to try, so you don't have to be afraid to offend or hurt me."
                y "If anything hurts, I'll tell you to stop."
                un bored"Lord knows what fucked up shit goes through the lizard's brain."
                show lizard free
                "Gael relaxes and drops his guard."
                "He looks around for a second, before coming to a conclusion."
                "He points to my loincloth."
                y "You want me to take it off first?"
                "He nods."
                "This is good, it shows him I'm serious about going further with this, even if our kiss should've been proof enough, in my opinion."
                "I unpin the cloth with a little difficulty, then let it drop on the ground, kicking it away with my foot."
                "My already erect penis in on full display."
                y nakedsmug"Ey?"
                "He contemplates, then starts rotating his finger in the air, telling me to turn around."
                y nakedsimple"Really?"
                y "Ok."
                show lizard freebleed
                "I oblige to his wishes, arching my back when my bare butt is in front of him, as an extra surprise."
                y nakedsmug"What do you think?"
                "He gives me two thumbs up nodding again determined."
                y "What now?"
                show lizard free
                "Gael gestures for me to come closer."
                "We are now face to face, or would be if he wasn't so tall."
                "Face to chest is a good compromise."
                "He clearly has many ideas going on behind those golden eyes, looking around, checking me out, raising his hands then lowering them, kind of unsure how to approach the next step."
                y "Do whatever you want, I'm all yours."
                hide lizard free with moveoutright
                "He turns away."
                y nakedpf"Whatever you want except for running away."
                "He searches through the hay bed, making a bit of a mess in the process, then turns back to me with a succulent leaf in hand."
                show lizard free with moveinright
                y nakedsimple"What's that?"

                "Gael finally drops the small piece of cloth covering his crotch, revealing something I did not expect."
                show lizard freenaked with longdissolve
                "A completely normal looking dick, growing harder by the second."
                "I'd estimate it at around eight inches, with a generous girth to it as well."
                stop music fadeout 3.0
                "In one word, intimidating."
                "It's hard for me not to blush, but who needs a red face to show their excitement when their penis is throbbing at the view?"

                show lizard freeclose2 with dissolve
                "He comes closer with newfound confidence, grabs my shoulders and turns me around."
                play music "audio/jazz2.ogg" fadein 3.0 volume 0.4
                y nakedblush3"I'm the one who asked to be manhandled, I shouldn't complain."
                scene lizardsex1 with longdissolve

                "He pushes me down on the floor, which is covered by surprisingly soft animal furs, and makes sure my legs are nice and spread out."
                "I look back to see him use the leaf's sticky juices to cover his fingers, then rub some around my entrance as well."
                y nakedss"We're starting huh?"
                "Gael drops on top of me, not letting his weight suffocate me, but not leaving me much room to squirm around either."
                "His fingers reach down again and press against my hole. He looks me in the eyes intensely and waits."
                "What a gentleman."
                y nakedsmug"Do it big guy."
                "One of his thick fingers penetrates, the slimy substance from the plant working wonders already."
                "Not only does it make the finger slide in like butter, but the slight numbing effect relaxes my muscles down there further."
                "It was so nice, that I barely noticed when the second finger slid in, but the third was hard to miss."
                "I try to keep my moans to a minimum, but his masterful fingers, rotating and shoving restlessly make my job hard..."
                "Not having fur makes the insertion smoother and more pleasurable."
                "Claws? What claws?"
                "Apparently claws can feel really nice inside you as long as the one using them is gentle enough."
                scene lizardsex2 with longdissolve
                scene CGcc32
                "After about a minute of constant movement, he takes them out one by one, leaving a well trained and relaxed hole behind, ready to invite his cock in."
                "Gael's long tongue slips out, licking the side of my face, as his pelvis gains distance."
                "He takes a couple of tries to position the tip in its place, then gives me one last pleading look."
                "This time, instead of {i}'can I do it'{/i} it says {i}'PLEASE let me do it'{/i}."
                y nakedsmug"Go, pump me full of your lust."
                scene sex with longdissolve

                y nakedblush"!"
                "Those words, like a switch, turn on his hips, and in an instant his whole length fills my insides and puts immense pressure on my walls."
                "Thanks to the miracle plant and Gael's careful preparation, the pleasure far outweighs any pain."
                y nakedhurt2"Oh good heavens..."
                "This time, the sounds I make are no longer up to me."

                "Each shove from him hooks to the surface new interjections and combinations of letters I would never make otherwise."
                y nakedhurt2"A-ah, MhHmMhmm~ghFff"
                y "Y-yeah, h-How are- ah- you so- oh God- so GOOD at this?!"
                "Of course he doesn't respond, but he does kiss me with his tongue more as if accepting the compliment."
                "His movements are not wild, not violent or vicious."
                "Not savage at all."
                "He's not trying to go as deep as possible beside the first thrust, or trying to fuck at rabbit speed."
                "He's gentle, slow, but damn be I, if his cock doesn't hit All. The. Best. Spots."
                "The whole time, my mouth is kept open from the moaning, closing it only when a new, harder thrust is about to happen."
                "Even then, I sing through my teeth the song of our sin in the secluded tent."
                "For the first time, I hear Gael's voice, in the form of grunts that grow louder."
                scene CGcc33
                scene sex2 with dissolve

                "He thrusts with an uncomfortable amount of length, faster than before, but compensates with the precision that stimulates my sweet spots like never before."


                "Minutes go by like seconds, since we're having the best kind of fun there is."
                "His movements intensify and become more uneven."
                "I feel him shivering and shaking moments before climax."
                y nakedhurt2"I-inside—cum inside me—Fill me up, don't h-hold back."
                "The large arms keeping his torso up suddenly wrap around me, heavy weight laying now on top of me."
                scene CGcc34
                scene lizardsexcum with longdissolve
                scene CGcc35
                "Not as heavy as his hips, slamming down one last time, before his cock starts to pulse and pump hot, thick seed, with enough force to bury it further up than any dick can go."
                "At the same time, my last button is pressed... hard, releasing my own load on the ground underneath."
                "It takes him an entire minute to drain all his lust, and every drop feels better than the last."
                scene lizardsexcum2 with longdissolve
                scene CGcc36
                "At last, he takes his now softened, empty shaft out, then opens his eyes, waiting for approval while breathing heavily."
                y nakedblush"{i}*Heavy breathing*{/i} That was....the best...orgasm I've ever had..."

                "He smiles and nods."
                un sidee"I liked it a lot too, actually...I'm a little ashamed of it."
                un "Never thought Savage Furs could be so intense..."
                y nakedsmug"That should take care of your lust levels for a while."
                y "Don't let any nasty hunters take your newly energy filled gem, you hear me?"
                y "Heh, I'm just joking."
                stop music
                scene lizardsexcum3 with hpunch
                "My funny man persona is cut short by a cold, sharp stab in my neck, followed by paralyzing liquid pulsing through my veins."
                un bored"Damn it..."
                "Gael?"
                play music "audio/dramatic.ogg" fadein 2.0 volume 0.8
                "I look up at the lizard, with six darts in his neck..."
                scene lizardsexcum4 with llongdissolve
                "Before my eyes close, I see my friends at the door."
                "I wonder what they want..."
                un squint"Obviously they drugged you, moron."
                un "Tell me to get rid of the poison."
                un suspicious"Then we'll kill those fuckers."
                "N-no.. it's ok."
                un simple"What?"
                un ang"WHAT DO YOU MEAN IT'S OK? YOU'RE PASSING OUT ANY MOMENT NOW!"
                stop music fadeout 3.0
                scene black with dissolve
                "They're...good, they're friends."
                play sound "audio/button.ogg"
                un ang"HEY!"
                play sound "audio/button.ogg"
                un "GIVE ME ORDERS GOD DAMN IT!"
                play sound "audio/button.ogg"
                un "DO YOU HEAR ME?!"
                play sound "audio/button.ogg"
                un "HELLO?"
                play sound "audio/button.ogg"
                un scared"Hello?"
                play sound "audio/button.ogg"
                un "[name]...?"
                play sound "audio/button.ogg"
                eu "He really did it."
                play sound "audio/button.ogg"
                un simple"!"
                play sound "audio/button.ogg"
                un sidee"I can hear them still."
                play sound "audio/button.ogg"
                ra "Of course he did it, I told you he's even more desperate for dick than you are."
                play sound "audio/button.ogg"
                eu "I'm not that desperate..."
                play sound "audio/button.ogg"
                ra "Well you should be, you can literally die without it."
                play sound "audio/button.ogg"
                ru "Lizard?"
                play sound "audio/button.ogg"
                ra "Just leave him, he'll wake up and forget everything, his dose was big, just to be sure."
                play sound "audio/button.ogg"
                ra "The fucker is surprisingly strong."
                play sound "audio/button.ogg"
                ra "Didn't want to have to deal with him, in case he caught feelings for [name] or something."
                play sound "audio/button.ogg"
                eu "I can't believe he decided to fuck the lizard instead of us..."
                play sound "audio/button.ogg"

                ra "His kind is weird, don't think about it too much."
                play sound "audio/button.ogg"
                eu "Well, I'm not cleaning lizard cum off of him."
                play sound "audio/button.ogg"
                ru "Not it."
                play sound "audio/button.ogg"
                ra "Grrr...fine."
                play sound "audio/button.ogg"
                ra "But you're carrying him to the ceremony, Ruth."
                play sound "audio/button.ogg"
                ra "And make sure my brother doesn't see you."
                play sound "audio/button.ogg"
                eu "Are you sure everything will be ok if the lizard was the one to do it?"
                play sound "audio/button.ogg"
                ra "He is supposed to be a consensual non virgin, that's all the rules state, and if the cum dripping from his tailhole says anything, he's no fair maiden no more, if he ever was."
                play sound "audio/button.ogg"
                eu "Then the dragon will be pleased."
                play sound "audio/button.ogg"
                ra "Like it fucking matters..."
                play sound "audio/button.ogg"
                eu "You never know."

                un sidee"...Ceremony..."
                play sound "audio/button.ogg"
                un "Do I know of any ceremonies that include dragons?..."
                play sound "audio/button.ogg"
                un "Hmmmm..."
                jump meanwhile



            "His life never needed a nosy leopard in it to begin with.":

                y nakedsad"It's time I let go."
                y "I know, I get attached too fast."
                y "I met a cat that I now can not imagine life without only three days ago, I met hot Wild Furs that won't leave my mind, whom I met today, and a lizard that simply deserved all my kindness, even if we only started to interact an hour or two ago."
                y "So for once, I'm going to let go."
                un simple"It's for the best."
                y nakedsimple"I should probably help him put the shackles back on at least, so he doesn't get in trouble."
                y nakedss"A final goodbye might be in order as well."
                stop music fadeout 3.0
                scene lizardtent with llongdissolve
                "I walk back in, to find Gael lying asleep on the hay bed, his back towards me."
                "He does lack energy, so it's only natural..."
                "I better not disturb him any longer."
                "Good bye, and take care."
                "I turn back around and-"
                scene black
                "{i}*WACK*{/i}" with hpunch
                un curious"Huh? What just happened?"
                play sound "audio/button.ogg"
                eu "What are you doing?!"
                play sound "audio/button.ogg"
                eu "We were supposed to drug him, not punch him unconscious."
                play sound "audio/button.ogg"
                ra "He's asleep, isn't he?"
                play sound "audio/button.ogg"
                ra "That was the point."
                play sound "audio/button.ogg"
                ra "Now what about the lizard?"
                play sound "audio/button.ogg"
                eu "Asleep, poked him with the darts."
                play sound "audio/button.ogg"
                ra "You think it's enough?"
                play sound "audio/button.ogg"
                eu "I gave him enough to knock out a wyvern, he won't make trouble."
                play sound "audio/button.ogg"
                eu "I doubt he'll remember anything when he wakes up."
                play sound "audio/button.ogg"
                ra "Good, too bad he didn't get to stick his dick in him..."
                play sound "audio/button.ogg"
                eu "But if they didn't breed, what do we do?"
                play sound "audio/button.ogg"
                ra "We'll just say they did, nobody will check."
                play sound "audio/button.ogg"
                eu "The ceremony says he mustn't be a virgin."
                play sound "audio/button.ogg"
                ra "Well the ceremony also says it has to be consensual, so if you still think you can make him fuck you when he wakes up, then by all means."
                play sound "audio/button.ogg"
                eu "I knew we should've insisted more..."
                play sound "audio/button.ogg"
                ra "I thought the lizard had it covered, okay?"
                play sound "audio/button.ogg"
                ra "[name] clearly had eyes for him, I just thought it would be more lustful..."
                play sound "audio/button.ogg"
                ra "Now, Ruth, take him away, make sure my brother doesn't see you."
                play sound "audio/button.ogg"
                eu "What will happen to the ceremony if we're not-"
                play sound "audio/button.ogg"
                ra "Shut up already, it has never been about this stupid ceremony, remember my plan and don't mess it up."
                play sound "audio/button.ogg"
                eu "Of course...your plan."

                jump meanwhile


        label meanwhile:
        stop music
        "{i}Meanwhile...{/i}" with longdissolve



        kus bored "I. Am. Exhausted." with dissolve
        play music "audio/wisp.ogg" fadein 3.0 volume 0.4
        scene forest4 with longdissolve
        kus bored"These people act like they've never experienced magic before."
        kus bored"I had to pretend like my teleportation spell AND broom malfunctioned and it wouldn't work properly."
        kus "Seriously, one more person and my magic reserves would've been completely gone."
        kus pf"I'm barely standing as is."
        kus smug"[name] will be so impressed by my fortitude."
        kus "A promise is a promise, just enough to get us back."
        kus s"Althought I might collapse as soon as we get home...but at least we'll be home!"
        kus simple"I should go find the Chief before anyone else finds me in this tree I hid in."
        kus "Which wouldn't be too hard because I'm just talking to myself out loud over here."
        kus s"But oh man, what a relief it was that [name] actually {b}wants{/b} to go home."
        kus bored"I really thought he'd stay here, and get married and have gay kids with... wait- that's not how that works."
        kus "Anyway, he wants to go home because that lizard situation pissed him off."
        kus "I didn't want to feel desperate and agree to go immediately."
        kus simple"I might've been a bit hard on him, now that I think about it, but what was I supposed to say?"
        kus "{i}'Yeah, let's go right now, my new family is not worth my time and they're terrible people?'{/i}"
        kus sad"I wanted to stay...I still do, but not as much as I want to be around [name]..."
        kus "It's infuriating how much I like it here, and despise it at the same time."
        kus ang"Make up your mind, Ku'sa-"
        kus simple"..."
        kus "Ku'sani..."
        kus bored"Yet another name for Aiden to tease me about."
        kus "It sucks..."
        kus ang"I suck."
        kus "{b}Aghhh EVERYTHING SUCKS!{/b}"
        kus simple"Everything and everyone but [name]."
        kus ang"Even Ki'vaathi, like, seriously people, it's a damn {i}WYVERN{/i}, not a dragon deity."
        kus bored"I now know how [name] must've felt every time I insisted."
        kus "Of course I knew the truth, but I wanted it to be true, just for the fun of it."
        kus sadsmile"If it really were a dragon, that meant that in a matter of weeks I'd have someone to talk to, someone who will be around me always and never leave..."
        kus bored"{i}*sigh*{/i}"
        kus "That just means I'm probably never coming back."
        kus simple"I should at least say goodbye to Ruth, and my stepdad, and my step brother...and Eureka."
        stop music fadeout 2.0
        scene black with dissolve
        play sound "audio/jump.ogg"
        "I try my best not to fall on my face while getting down from the tree without magic."
        scene forest22 with dissolve
        "Mission accomplished so far, with one or two minor scratches, now to find everyone."
        "One person I know for sure where to find, so I'll go to him first."
        scene forestpath with fade
        scene camp2 with dissolve
        play music "audio/celtic1.ogg" fadein 3.0 volume 0.4


        kus ang "Huh, what do you mean {i}'no'{/i}?"
        grd "No entry."
        kus "Why not?"
        grd "Chief say no."
        kus "I am his SON!"
        grd "No son, nobody entry."
        grd "Chief busy, he say."
        kus bored "Well this is annoying, in that case, tell him that his {b}SON{/b} is going home, I wanted to say goodbye, but if he's just soooo busy, I guess I'll go without a final farewell, how about that?"
        grd "Uhhhhh, repeat?"
        kus "Never you mind..."
        kus "Ragnar will have to be enough."
        scene camp6 with dissolve

        "I make my way to the main camp, disappointed but not discouraged."
        "The first thing I notice is the missing pillar that was burning in a pyre a couple of hours ago, a deep hole left in its place and no ashes to be seen around."
        "Good workers, fast too."
        "They even planted new, unburned grass, neat."
        "Other than that there isn't much around here."
        "As far as I understand, it's still nap time, or breeding time, so no Nightfallen roaming around."
        "I'd lie if I said I wasn't curious what {i}'breeding'{/i} with a Nightfallen would be like, since, obviously, that will literally be my job in the future, but I promised to remain a virgin until that special someone comes along."
        "After that, my ass will become an open mic comedy show, and that's a promise."
        "A single pair of people catch my attention, showing up from behind a hut."
        kus "Hey! Ragnar! Eureka!"
        show ragnar at right2 with moveinright
        show eureka at left2 with moveinleft
        ra "Hey, look who's finally free again."
        ra "Did our tribe mates finally leave you alone?"
        kus "I had to run away from them, or else they would've drained all my magic, heh."
        show ragnar ec at right2
        show eureka ec at left2
        "They both try to contain laughter."
        eu "What a coincidence, we also had to run away from your friend before he could completely drain us."
        ra "That's right, oof, that man can not be satiated with just the two of us."
        kus sadsmile "H-hehe, what, uhmm, what do you mean by that?"
        eu "[name] insisted that we commence in a session of breeding, he's just that invested in knowing our ways better, you know?"
        kus simple"So...the three of you fucked, is what you're telling me?"
        ra "A simple way of saying it, but yes."
        ra "It's safe to say he drained all the lust I had in me, for at least the next moon, heh."
        kus "And where is he right now?"
        show ragnar smug at right2
        show eureka smug at left2
        eu "Oh he's not done yet, far from it."
        eu "You know Ruth caught his eye in that beautiful white, spotted fur, so he's not tapping out like we did."
        ra "They're still in a hut somewhere, if you hurry, maybe you can join them."
        eu "He runs out of stamina fast while dancing, but give him some cock and ass and he'll go at it forever."
        kus sad "I-it's alright, I'll pass."
        show eureka simple at left2
        show ragnar simple at right2
        ra "Then why are you looking for him?"
        kus "He said before that he wants to go home..."
        kus "I wanted to see if he'd stay another day, but he seemed very determined to go back."
        kus "I just wanted to teleport him."
        show ragnar at right2
        show eureka at left2
        eu "He seems much more determined to drain all the lust he can at the moment."
        ra "You should probably come back for him tomorrow morning."
        ra "We heard you have some kind of important assignment, so we wouldn't want you to miss it, but we would also hate to deprive [name] of his needs."

        kus "Y-yeah, that makes sense."
        kus sadsmile"I'll just... come back later, simple."
        kus "In that case, I guess this is goodbye, for now."

        show ragnar close at right
        show eureka close at left

        ra "You're not leaving without hugging your brother, right?"
        eu "And your brother's partner needs one as well."

        "The hug is tight, almost violent, these people are strong."

        kus simple "Ok ok, that's enough."
        kus bored"We'll meet later anyway."
        play sound "audio/teleport.ogg"
        stop music fadeout 2.0
        scene teleport with dissolve

        "With some final waves, a flash of blue light takes away my vision, before the main gate of my dear town appears."
        play music "audio/slowpiano.ogg" fadein 3.0 volume 0.4
        scene outside2 with longdissolve
        kus sad "Home sweet home..."
        "Why did I come back again?"
        "What was I usually doing before [name] came around?"
        "Get myself in trouble?"
        "Or the second thing, waste my time sulking..."
        scene tatedorm with llongdissolve
        "I go back to my dorm, and jump on the creaking bed, closing my eyes, trying to take a nap."
        "..."
        kus bored"Like I could ever sleep with these emotions flying around."
        "Maybe I should find Dallan and Aiden, it should be close to dinner time, even if the sun refuses to go down."
        "As if trying to trap me in this daytime nightmare, where everything goes so well, yet so bad."
        "Having a phone in a moment like this would be useful, since I have no idea where those two could be."
        "Especially now that [name] appeared, their plans are so random I can't predict them."
        "I mean, a massage? Really?"
        kus "Maybe some ice cream will make me feel better."
        scene park1 with llongdissolve
        "I pay for a cone and stare at the frozen,  chocolate flavored dessert."
        "I look at the waffle cone, I look at the small chunks of chocolate, I look at the drip slowly running down on the side, until it hits the ground."
        kus bored"I don't feel like eating anything, actually..."
        kus "Did I just waste a perfectly good ice cream?"
        kus simple"Lets see..."
        kus s"Hey kid! Come here, I have free ice cream, want some?"
        kid "Stranger Danger!"
        "He books it in the opposite direction, yelling."
        kus bored"Ah, right, I'm an adult, technically."
        kus "At least someone's parents taught them right."
        kus "Even if now I have to waste a perfectly good ice cream."
        "I already said that..."
        "Even my thoughts are sulking and won't let the wheels turn."
        "I place the cone gently on the ground."
        "A murder of crows will have a field trip with this one."

        "It's weird that I don't feel like eating, since my energy level is down, together with my magic."
        "If I were to take [name] back with me, I might've actually collapsed on the spot."
        "But hey, then I would've had a pair of soft arms to catch and cuddle me while I get better."

        "I keep my hands inside my pockets as I walk down the street, which is just as empty as the camp was after I stopped giving everyone rides."
        scene park2 with dissolve
        "It feels lonely."
        "A small piece of paper brushes against my fingertips along with the other little trinkets I keep with me at all times."
        kus simple"Huh?"
        kus "I don't remember this, what is-"
        kus "oh."
        "A series of numbers, written on this wrinkled little thing, signed [name], under it."
        "..."
        kus"There's no harm in trying."
        scene outside2 with dissolve
        "I find the nearest public phone booth, pop some coins inside, then with a deep breath, I type in the number."
        "I've only done this about three times in my whole life, since other people usually needed to get a hold of me, not the other way around."
        "As far as I know, these phones should work even if the other person is outside the barrier."
        play sound "audio/phone.ogg" volume 0.2
        "It better work, if it makes you pay it money."
        "The unsettling beeps invade my ear, before a voice speaks."
        stop sound
        kus s "HEY, HI! [NAME], I WAS JUST-"
        play sound "audio/hangup.ogg"
        "{i}The number you have dialed is currently out of coverage area or cannot be reached at the moment. Please try again later.{/i}"
        kus bored "Ah. Of course."
        kus "Did I really expect the signal to work in that giant forest?"
        kus "I just wanted to see if he's okay..."
        kus simple"Maybe he'll get bored of sex, at some point."

        "I'm just gonna have to wait for my magic to come back up, then I'll teleport to him."
        "Surely he doesn't want to stay there until morning."
        stop music fadeout 3.0
        scene black with llongdissolve




        "Right now, I'm going to settle for daisies..."
        play music "audio/hope.ogg" fadein 3.0 volume 0.3
        scene tatelayblur with longdissolve
        "The daisy filled hill, overlooking the ocean on one side, and the academy on the other."
        "With a clear view of the sun, soon to be setting."
        "This is the most peaceful place on earth, the warm rays of light are perfect for a lazy afternoon, and the view is amazing all day round."
        "The grass is soft, and delicate."
        "The ground is fertile, sprouting these beautiful white flowers that tickle my nose whenever I dare fall asleep here."
        "Unfortunately, not even the best place in the world can make you forget about your friends."
        scene tatelay with longdissolve
        scene CGc23

        ku "Why did you decide to stay?"
        ku "You wanted to come home so badly, and I just didn't listen."
        ku "Did you really change your mind that fast? Or are you just a big playboy?"
        ku "And most importantly, why do I even care so much?"
        ku "We're hunters, we have sex with Nightfallen, that's what we do."
        ku "But isn't there a saying that you're not supposed to take your job into your personal life?"

        ku"My head hurts..."
        ku "And not just because I'm tired and drained of magic."

        if betray >=3:
            ku "What am I even so upset for?"
            ku "Of course he'd want to stay in the sex camp."
            ku "He couldn't keep his dick in his pants for two days around regular people, let alone hot, horny Wild Furs that are drooling over him..."


        else:
            pass

        ku "I wish mister Sebil was here."
        ku "He'd know what to do."

        "I lay here with the wind in my fur, the cool earth contrasting the warm grass nicely."
        "I can almost see him in front of me, if I only squint my eyes and hope."
        "Daydreaming of exactly what you want is hard sometimes."
        "Images of my stepparents, my REAL stepparents, appear around me."
        "Soon to be replaced by the Headmaster's sly grin."
        "My thoughts are interrupted by stormy clouds covering the sun and a more intense wind hitting my side."
        stop music fadeout 3.0
        "Familiar darkness..."
        "No, there's no way the clear sky went away that fast."
        "I open my eyes, finding them shielded from the light by a large body, covering me in shadow."
        ku "Do you mind? I'm trying to bask in-"
        play music "audio/inventor.ogg" fadein 3.0 volume 0.3
        scene tatelayblur with longdissolve
        show unknown20 with llongdissolve
        "The towering man's face is covered by a mask, and a loincloth is the only thing he's wearing."
        "I jump up, not scared, but surprised for sure."
        kus simple "Who are you?"
        "The Wild Fur with the black void mask says nothing, and hands me a piece of paper."
        "I reluctantly take it."
        kus "Thanks?"
        kus "Am I not inside the barrier?"
        kus "How did you get here?"
        "I take a quick look at the paper, a couple of messy words written on it."
        "{i}Your friend is in grave danger.{/i}"
        hide unknown20 with moveoutleft
        "He turns around without another word and walks back to town."
        kus ang"Wait! You can't go there!"
        kus "But more importantly, what the hell do you mean by danger?!"
        "He shows no sign of stopping or turning around."
        show unknown20 with moveinleft
        "I run after him, blocking his path, almost falling and rolling down the hill in my panicked attempt."
        kus "Oh no, you don't get to be a mysterious figure that disappears with no explanation."
        kus "Who are you?"
        kus "How do you know this?"
        unk "..."
        kus "Tell me or I'll teleport you to the sun."
        "I wish I had that much magic in me right now..."
        unk "I am an ex member of the Nightgale tribe."
        kus simple"Ex?"
        unk "I was exiled for defending someone from your kind, going as far as to allow him to become my master."
        kus simple "But...they're friendly towards our kind, at least, that's what I got from my experience..."
        kus "What's that about my friend? Who do you mean by that?"
        kus "The wyvern?"
        stop music fadeout 2.0
        unk "[name]." with longdissolve
        "My face goes pale and my pupils shake in horror."
        play music "audio/hm1.ogg" fadein 3.0 volume 0.4
        "There's nothing more he has to say, I was hoping his name wouldn't be brought up."
        "Everything started to click."
        "He wanted to leave as soon as possible, then all of a sudden, didn't."
        "I accepted the fact that he's just {i}'having fun'{/i} from Ragnar's and Eureka's words."
        "In my jealousy and anger, I forgot to think rationally."
        kus scared"What-"
        kus "What kind of danger?"
        unk "The tribe's deity, Ki'vaathi, needs a ceremony dedicated in his name, so that his powers may awaken."
        kus "But we already had a celebration...did we not?"
        "Thinking back on it, not once was the wyvern the center of attention, except for when it was sleeping in the middle of the round table."
        "Nobody mentioned him, other than when thanking us for taking care of him."
        kus "So what next?"
        unk "They need a sacrifice, a sacrifice from your kind."
        "Anger surges in me hearing those words."
        "Why? Why him?"
        "Why not me?"



        kus "How much time do I have?"
        unk "..."
        unk "Minutes." with dissolve

        "Yet another simple, common word that hits like a truck, making my heart skip a beat."

        kus "Aiden...no."
        kus "Dallan...no."
        kus "Merina?"
        kus ang "AGHH FUCKING HELL, I DON'T KNOW WHERE ANY OF THEM ARE AND I DON'T HAVE TIME TO FIND THEM!"
        kus "WHY DIDN'T YOU COME TO ME SOONER?!"
        stop music fadeout 3.0
        hide unknown20 with dissolve
        "The Nightfallen dips his head, as if relating to my hopelessness, before turning slowly away and disappearing over the hill."
        scene field with llongdissolve
        kus sad"No, it's not his fault, it's not anybody's fault."
        kus "It's mine."
        kus "I wasted my magic like an idiot, and would've done so with even less regard to my energy if [name] didn't remind me to keep some..."
        kus sad"[name]..."
        kus "I can't just lay here and sulk, even if I'm an idiotic, useless cat."

        kus "If something happened to him because of me..."
        play music "audio/whoiam1.ogg" fadein 2.0 volume 0.6
        scene cat1 with longdissolve
        "There is no more time to waste, no time to think this through anymore."
        "I put my hood back on, watching the forest with tall trees in the distance intensively."
        kus ang"I'm coming home again, {i}'father'.{/i}"
        kus"But before that, I have one thought for the world to know."
        kus "Ku'sani..."
        tt "Is a dumbass name." with llongdissolve

        "Echos of my heartfelt thoughts disperse through the air, carrying my quiet words as far as the eye can see, at least that's what I felt happening when they left my mouth."
        scene cat2 with dissolve
        "Instead of tears, my eyes are filled with determination."
        "Images of [name]'s soft fur against mine invade my mind."
        "I'm not letting any friend of mine be no God. Damn. Sacrifice."

        "My feet carry me towards my friend, gaining speed each second until I feel like I'm flying downhill."
        "A race not for distance, or time, but adrenaline and courage, since the blink of an eye and a flashing blue light is all it really takes..."
        stop music fadeout 2.0
        scene CGc24

        scene teleport with dissolve

        scene forest20 with llongdissolve
        play music "audio/wind.ogg"
        "The bright, green and white hill turns into the dark forest with trees taller than a building."
        "The main gate is wide open, with nobody defending it."
        play music "audio/dramatic.ogg" volume 0.7
        scene confruntation1 with longdissolve

        "I walk in as confidently as I can muster."
        "The once empty looking camp now full to the brim with either smiling or anxious looking Wild Furs, masked and unmasked."
        "A wide path is left in the middle, as if specifically made for me to walk further in, everyone going as far as to take a step back if I try to get closer to any particular Nightfallen."
        "This choreographed meeting is pissing me off more and more."
        scene confruntation2 with llongdissolve
        scene CGc25
        "I can no longer take hearing the low murmurs around me building up."
        tt "WHERE IS HE?!"

        tt "TELL ME, WHERE IS THAT COWARD?!"
        stop music fadeout 2.0
        "Few figures in the crowd, understanding some of my words, or at least predicting them, turn their heads upwards to the side."
        play music "audio/chief.ogg" volume 0.6

        scene confruntation3 with llongdissolve

        "Upon a watchtower, he stands proudly, with his usual, stupid grin on his face."
        tt "You..."
        c "Welcome, son!"
        c "I'm glad you could join us."
        tt "Don't you dare call me your son."
        tt "You know why I'm here."
        c "Back for some more delicious skewered rat, I presume?"
        tt "WHERE IS MY FRIEND?!"
        c "Who? [name]?"
        c "Why, he's having the time of his life somewhere in a hut."
        c "His moans of pleasure could be heard across the whole-"
        tt "Cut the crap."
        tt "I know all about your plans."
        tt "I'm here to take him back, and there's nothing you can do to stop me."
        "It takes every bit of strength to keep my chest forward and my legs from buckling under me."
        "Even my vision is cloudy."
        "As I said before, my magic was not even close to coming back up, and this one single teleportation almost made me black out."
        "The Chief looks over the crowd of Nightfallen through his impractical mask."
        "The grin turns into a sad smile."
        c "It seems we have a traitor among us."
        c "They shall be dealt with later."
        c "Now..."
        c "Nothing to stop you, you say?"
        play sound "audio/cancel.ogg"
        scene confruntation4 with dissolve

        "The Chief snaps his fingers in my direction, an echoing, familiar sound taking over the quiet camp."
        "Then a pair of guards, one of which is none other than Ruth, appear behind me to restrain me."

        tt "You know that spell too?"
        tt "Why aren't I surprised?"
        tt "And I guess you're using...Ragnar as an anchor..."
        tt "Which is why not even he can dethrone you..."
        c "My own child would not betray me...well, not both of them, at least."
        c "And your kind are not the only ones that can learn new tricks."
        scene confruntation5 with llongdissolve
        scene CGc26
        "I would be more revolted at the new, unexpected move he pulled, but to be fair, even without that spell, I would not be able to even run, let alone teleport."
        "The guards holding me from either side are almost a relief, letting me rest on something."
        "But there was no other choice."
        "I either come here and be useless, or waste time looking for someone with actual power to help, and be too late to save [name]."
        "In my position, begging is all I'm good for."

        tt "Please, please just let [name] go."
        tt "I'll do anything."
        c "Begging?"
        c "That is not the first thing that comes to mind when I think of someone that has {i}'nothing that can stop him'{/i}."
        c "It's a little late to change our minds."
        "He waves his hand towards a group of trees growing close together."
        "The trunks start to move and bend and even the roots look like they're trying to grow feet and walk out of the way, revealing a horrific image."
        play sound "audio/horror.ogg" volume 0.9

        scene codytie2 with longdissolve
        scene CGc28
        "A white, black and red leopard is tied to a large, runic stone, blue fires lit all around."
        tt "No..."
        tt "No."
        tt"What are you doing?"
        tt"Let him go."
        tt "Please, just let him go."
        tt "Ruth, please, help me."
        scene confruntation6 with dissolve   #front view of tate
        "I look at the large bear with pleading eyes, someone I truly thought could be my friend."
        "He remains stoic, peering ahead, devoid of expression."
        tt "I taught you how to flirt, Ruth."
        tt "We danced together."
        tt "[name] liked you, and you liked him, {b}and I liked both of you!{/b}"
        "My begging does no good."
        "Something wet falls from under Ruth's mask, being soaked up by the fur before it can drop."

        "He takes a step back, without letting go, so that I have a hard time looking at him."

        "As a last resort, I squirm with whatever bit of strength I have left, but to no avail." with hpunch
        scene confruntation5 with dissolve

        tt "Why?"
        tt "Why are you even doing this for?"
        tt "For the name of a God?"
        tt "What do you hope to get from raising a God?"
        scene confruntation7 with dissolve

        c "A dragon's power under our wings..."
        c "With him, we will live peacefully."
        tt "Don't you already?"
        tt "I've seen nothing but peace until now."
        tt "All you do is eat, fuck and nap."

        c "TELL THAT TO ALL OUR LOST CLANMATES, WHO WERE HUNTED BY YOUR KIND TO BE USED FOR WHATEVER SELFISH REASON YOU HAD!"
        tt "{size=30}But Wild Furs are no longer allowed to be hunted...{/size}"
        c "Ha!"
        c "As if that's supposed to make us feel better."
        c "It's not as if people we held dear were taken away from less than a hundred moons ago, before that {i}'rule'{/i} of yours was made."
        tt "Is that your idea of vengence?"
        c "It's my idea of judgement."
        c "I will not live with the fear that any day your kind can change their mind because they need more crystals from us."
        tt "It's hard to believe Ragnar would ever agree to your genocidal ideas."
        c "Actually, he is the one that planned most of it."
        c "I can't take all the credit myself."

        tt "..."


        c "Unfortunately, Ragnar couldn't bring himself to watch the ceremony unfold."
        c "Poor boy, his feelings caught up to his plans."

        tt "You want to live in peace, but if you're going forward with this, you will never find it."
        tt "This is a promise."

        c "Threatening you are, little one."







        c "I am afraid that intimidation attempt isn't very effective when you're right in front of me, defenceless and useless."
        c "Still, I don't want to take too many risks, so I'm worrying...that you'll get in my way too much..."
        scene confruntation8 with dissolve
        "He raises the hand nearest to me."
        "Dozens of figures emerge from behind the verdant veil, perching upon low, sturdy branches."
        "Archers, bows trained upon me, pulled strings poised, and arrows poised to be unleashed, awaiting the signal."


        "More anger comes to the surface, but this time, I'm angry at myself for ever trusting this monster..."

        tt "Are-"
        tt"Are you seriously going to kill me?"
        tt "Just like that?"
        tt"After that {i}'touching'{/i} reunion we just had?"
        tt "After a whole day of celebration, and stories and dancing and shared meals."
        tt "After we found and cared for your precious deity."
        tt "After everything we did for you..."
        tt "IS THIS HOW YOU REPAY US?!" with hpunch



        tt "I thought I was your {i}'son'{/i}."

        tt"WAS THAT ALL A LIE?!"
        tt "I HATE LIARS!" with hpunch
        tt "YOU KNOW THAT!"

        tt"DO IT THEN!"
        tt "SHOOT ME!"
        tt "It's not like a lot of people would miss me."

        c"My dear Ku'sani-"

        tt "Don't call me that."

        tt "{b}That's not my name!{/b}"
        tt "I deny it, the same way I denied every stupid name everyone keeps trying to give me, like I'm some sort of stuffed toy, or pet."

        c "Look at you."
        c "{i}*Sigh*{/i} You were such a promising cub."
        c "I thought you could rival your brother."
        c "He fought so hard to protect you."
        c "Or more like rob you of your destiny."
        c "Even if you were never truly one of us."

        c "Pity."
        scene confruntation9 with dissolve

        "His hand gives a signal, but not in my direction..."
        "All the archers turn their bows slightly, aiming at something else."




        tt "What..."
        tt "What are you doing?"

        tt"Chief, stop."
        tt"This is not funny."
        tt"I'm over here!"
        tt "Ragnar! What's up with them? Are they blind?!"
        tt "Ragnar? Where are you?!"

        tt "HEY!" with hpunch
        tt "THAT'S THE WRONG WAY!"
        tt "YOUR TARGET IS HERE!"
        tt "LOOK AT ME!"


        c "You were right, Ku'sani, I'm too soft to kill my own cub, even if he's as... disrespectful and naughty as you."
        c "Yet, at least."

        c "Even so, you must still be taught a lesson."
        c "You should be thankful to me."
        c "You were supposed to be the sacrifice all along, but fate spared you."
        tt "The fuck is that supposed to mean?"
        c "That was the whole purpose for your existence."
        c "We found you, sent by the Nightfallen King himself, cared for you, fed you, so you can be the savior of our tribe one day."
        c "Unfortunately, you ran away upon finding out the truth."
        c "We thought you must've died in the harsh blizzard, bare footed."
        c "But it seems you found your nest among those hunters."
        c "Then, you came back, I thought you brought your friend as a way to ask for forgiveness, and exchange your life for his."
        c "Apparently I overestimated your resolve."
        tt "Ah."


        tt "I understand better now..." with llongdissolve
        c "Oh?"
        c "You do at last?"
        tt "I understand that you're just crazy {b}son of a bitch.{/b}"
        c "Hmm, {i}bitch{/i}... I'm not familiar with the word."
        c "Eureka, put it in my {i}'to learn'{/i} list."
        eu "Yes sir..."
        c "Now..."
        c "The dragon demands sacrifice."
        c "We shall not delay any longer."

        c "So he can become the ultimate protector of out tribe."
        play sound "audio/button.ogg"


        tt "Dragon?"
        play sound "audio/button.ogg"
        tt "DRAGON?!"

        tt "{size=60}IT'S A FUCKING WYVERN, YOU MORON!{/size}"
        tt "IT'S NOT A DEITY, IT WILL KILL YOU ALL WHEN IT GROWS UP!"
        tt "IT DOESN'T NEED A SACRIFICE!"
        tt "{b}YOU'RE DOING EVERYTHING FOR NOTHING!{/b}"
        stop music fadeout 3.0





        c "SILENCE!"
        c "You do not belong to the Nightgale tribe."
        c "You do not know our ways, THE ways!"

        play music "audio/whoiam1.ogg" fadein 2.0 volume 0.9

        tt "Because your ways are {b}STUPID!{/b}"



        scene confruntation12 with hpunch
        scene CGc29






        tt "I should've listened to [name]!"
        tt "He figured you out first."
        tt "While I'm just a fool to the end."
        tt "I'm sorry..."


        "I try to teleport nonetheless, weak sparks of magic being the only progress I make."
        "Weak..."
        play music "audio/whoiam2.ogg" fadein 1.0 volume 0.9



        tt "{i}I'M SORRY I LEFT YOU!{/i}" with hpunch










        scene eye with longdissolve






        tt"{size=60}PLEASE, DON'T TAKE AWAY MY ONLY FRIEND!{/size}" with hpunch


        scene codytie with dissolve
        scene CGc27
        
        
        play sound "audio/whoiam3.ogg"volume 0.9
        stop music fadeout 1.0
        pause 0.4




        scene codyarrows2
        pause 0.8
        scene final12
        pause 0.8
        scene codyarrows2
        pause 1.5
        play music "audio/whoiam4.ogg" volume 0.9
        stop sound fadeout 1.0
        scene final10 with llongdissolve

        pause 2
        scene final11 with llongdissolve
        scene CGc30
        pause 3.5
        scene final111 with dissolve
        scene codyarrows2
        pause 0.5

        scene codyarrows3 with dissolve
        pause 2.5
        scene codyarrows4 with dissolve
        scene CGc31
        pause 2
        scene final13
        scene CGc32
        pause 2
        scene final14 with dissolve
        scene CGc33
        pause 0.5
        scene black
        pause 0.5
        scene final15
        pause 0.5
        scene black
        pause 0.5
        scene final16
        pause 1
        scene black
        scene final166
        pause 0.5
        scene black
        pause 0.5
        scene final11
        pause 1
        scene final18 with dissolve
        pause 1
        scene final17 with llongdissolve
        scene CGc34



        pause 4
        scene codytie2 with llongdissolve
        stop music fadeout 2.0





        "All the Nightfallen look in horror at their Chief's bloody body, falling from the watchtower."
        "The guards are too stunned to keep their grip on the nameless cat, who wastes no time, and runs towards his tied up friend."
        play music "audio/whoiam5.ogg" fadein 3.0 volume 0.9
        "It seems like it's all over."
        "It seems like a happy ending might still be possible."




        if betray >=3 and sex<=0:






            "When a voice stops him, whispering, calm and pleading..."
            c "Ku'sani, please think about us."
            "The cat does not turn around, but despite all odds, despite the adrenaline, he stops and listens while breathing heavily."
            "After all, judging by the particles of ash flying gently his way, the voice's body will become nothing more than a gem any second."
            c "This man is a traitor to you, a liar, a deceiver."

            c "He brought you only sorrow."
            c "He left you, again and again, while promising he is a friend."
            c "He would build you up, and betray you in the end."
            c "Going off to breed with your friends, rather than spend time helping you."

            c "I see you have no more magic, if you take him with you, you might even die."
            c "Why risk yourself with someone like this?"
            c "You got your revenge on me, spare your brethren, and let the ceremony commence."

            "The cat's gaze turns to sadness over anger."
            "Whatever is going on inside his head, it does not look too promising for the leopard's fate."
            stop music fadeout 3.0
            scene finaltp1 with llongdissolve
            "Tears stream down his cheeks, a last look at his once friend, before a bright flash of blue takes him away."
            play music "audio/hm1.ogg" volume 0.5
            scene codytie with longdissolve

            un scared"What--"
            un "What just happened?"

            wf "Cat gone!"

            wf "Arrows back ready!"
            un "No..."
            un "The- the cat, he was supposed to-"
            un "He was suppsoed to save-"

            wf "Set!"
            un "[name], wake up..."
            wf "Fire!"
            stop music
            scene codyarrows2
            eu "{b}NO!{/b}"



            scene black

            un scared"..."
            un "[name]?"
            un "You can't just leave me like this."
            un "It's dark...I-"
            un "I can't breathe."
            un "Not again..."
            play music "audio/brokenpiano.ogg" volume 0.5


            xx "Ughhh, finally, that critter is out of the picture."
            un scared"!"
            un "Who's there?"
            xx "My magic investment in that Chief proved to not only be useless...but a hindrance."


            un ang"Show yourself!"
            xx "It is a pity, really, I had a lot of uses for this little white one, but if fate brought him death, so be it."
            un scared"It's...it's you."
            xx "Can you believe it?"
            xx "After so long."
            xx "At least now you'll stop playing your little games."
            xx "Did you have fun, {i}'Scribbles'{/i}?"
            un sad"I-"
            xx "No no, you don't respond to rhetorical questions, silly."
            xx "You look stupid when you do that."
            xx "What is that?"
            xx "Are you crying?"
            un sad2"My friend is no more..."
            xx "Yes, well, it's not like it's the first time."
            xx "Get over it already."
            xx "Now come on, back to the crystal you go."
            xx "We'll have to meet some other time."
            xx "When the next idiot stumbles upon you."
            un "Yes, sir..."
            "..."
            "Later that night."
            scene tentnight with longdissolve
            show eureka sadsmile at left with dissolve
            show ragnar mad at right with dissolve

            eu "Hey...aren't you going to give a speech?"
            ra "What for?"
            eu "Your father is dead, and you'll be our next Chief, you should at least show up to the pyre."
            ra "{i}*scuff*{/i}"


            eu "What's wrong?"
            eu "Isn't that what we wanted?"
            eu "He's finally gone, no more dangerous missions inside their cities, no more meaningless sacrifices for any lizard that comes by..."
            eu "We won."

            eu "What...what are you doing?"
            ra "I'm packing our things, what does it look like I'm doing?"
            show eureka sad at left
            eu "..."
            eu "Look, I know this wasn't exactly the plan..."
            eu "[name] wasn't supposed to die, in the end, I feel pity, might even say I miss him."
            ra "You were supposed to protect him..."
            eu "I didn't think Ku'sani would ever abandon him."
            eu "The Chief used his last breath to change his mind."
            ra "I should've been there...instead of hiding like a coward..."
            ra "This is my fault."
            eu "Don't say that...you didn't let the final arrow go."
            ra "But they can't be blamed for that, they were born and bred to follow his commands...even in death."
            show eureka sadsmile at left
            eu "At least he's no more."
            eu "We got out from under his madness."
            show eureka ec at left
            eu "We're finally free, Ragnar!"
            show eureka sad at left
            show ragnar mad2 at right
            ra "{size=60}SHUT UP!{/size}" with hpunch
            ra "Don't you get it?!"
            ra "We KILLED one of their own."
            show eureka sad at left
            eu "That's not true, {b}we{/b} didn't do anything the Chief was the one-"
            ra "Do you honestly think they'll march in our camp and ask us who did it?"
            ra "As early as tomorrow morning, our tribe will be massacred."
            ra "My brother will tell the story, and we'll be punished for what we did."
            eu "I thought their rules didn't let them kill our kind."
            ra "That is only if we stay out of their business..."
            ra "Killing one of them is definitely a hole in the rules."
            ra "That's what we've been trying to avoid the most, it was just a matter of time until he caught on that our missions to kill their kind were not just failures...but planned to fail."

            eu "We will defend ourselves then, they can't just do that."
            ra "The reason we were powerless against our father was because he had very weak magic at his side, their kind make HIS magic look like a JOKE!"
            ra "Yes, we can kill some of them with some luck, but that would only make them angrier."

            ra "So you're coming with me, to survive."
            eu "We can't just leave our people behind, what about the children?"
            ra "The more people know, the faster the panic sets."
            ra "Should've made a higher effort of saving [name], if we wanted to save everyone..."
            show ragnar sad at right
            ra "So?"
            ra "Last call, love."
            eu "..."
            scene black with longdissolve
            eu "All of a sudden, a dragon God sounds like a nice thing to have right now..."
            eu "I'm coming..."


            jump worstending



        elif betray>=3 and sex>=1:
            "When a voice stops him, whispering, calm and pleading..."
            c "Ku'sani, please think about us."
            "The cat does not turn around, but despite all odds, despite the adrenaline, he stops and listens while breathing heavily."
            "After all, judging by the particles of ash flying gently his way, the voice's body will become nothing more than a gem any second."
            c "This man is a traitor to you, a liar, a deceiver."

            c "He brought you only sorrow."
            c "He left you, again and again, while promising he is a friend."
            c "He would build you up, and betray you in the end."
            c "Going off to breed with your friends, rather than spend time helping you."

            c "I see you have no more magic, if you take him with you, you might even die."
            c "Why risk yourself with someone like this?"
            c "You got your revenge on me, spare your brethren, and let the ceremony commence."

            "The cat's gaze turns to sadness over anger."
            "Whatever is going on inside his head, it does not look too promising for the leopard's fate."
            stop music fadeout 3.0
            scene finaltp1 with llongdissolve
            "Tears stream down his cheeks, a last look at his once friend, before a bright flash of blue takes him away."
            scene codytie with longdissolve
            un scared"What--"
            un "What just happened?"

            wf "Cat gone!"

            wf "Arrows back ready!"
            un "No..."
            un "The- the cat, he was supposed to-"
            un "He was suppsoed to save-"

            wf "Set!"
            un "[name], wake up..."
            wf "Fire!"
            scene codyarrows2
            eu "{b}NO!{/b}"
            scene black with hpunch
            un scared"!"
            un "[name]?"
            un sad2"[name]...there's no way, you can't leave-"
            un "..."
            un sidee"Hold on."
            un "This heart..."
            un surprised"This heart still beats."
            un "We're still breathing."
            un "What's happening?"
            play music "audio/blizzard.ogg"
            un suspicious"Brrrr, it's cold."



            scene frozen with longdissolve

            "The forest all around the lonely leopard turns to ice in an instant."

            "Every arrow shattered into a million pieces before they can reach their target, every Nightfallen's feet unmoving, stuck to the ground."
            "A graceful white fox with pink hair takes slow elegant steps towards the ex-sacrifice."
            "Her expression full of anger."
            "She creates a sharp icicle above each Wild Fur's head, but decides to stop her spell when her eyes meet the bloodied, full of arrows body of the once Chief, which turns to ash before her eyes."
            "The fox cuts the leopard's ropes with two clean swoops, holding him gently in her arms."
            "Nobody dares make a sound, for all they know, God herself descended to save their sacrifice, and damned be the ones that look her in the eyes with anything other than fear."
            "And if this {i}'God'{/i} wasn't fearful of the law, no witnesses would've been spared, mark her words.."
            "A wave of snow carries the leopard's clothes."
            "A blue light can be seen inside one of the pockets, matching the one the fox carries around her neck."
            "The stone proved useful sooner than expected."
            stop music fadeout 2.0
            scene black with llongdissolve
            pause 2
            play music "audio/hospital.ogg" fadein 2.0 volume 0.5
            scene hospital with longdissolve


            "Our leopard remembers nothing of what happened, and neither does the little voice inside his head."
            "He made a full recovery the following day, such are the miracles of healing magic."
            "He is even still determined to ace whatever test the Headmaster throws at him."
            "But no matter how much blissful ignorance he lives in, one thing he can not shake."
            "Why does the cat avoid him like the plague?"

            "He might've been more concerned with finding out why, but he made friends in others, such as Merina, and Oliver, and Coal, Aiden, Dallan, Rose and more."
            "He needs not the cat, so he decides to let go of the few days of memories they shared."
            "Faint memories..."
            stop music fadeout 2.0
            scene black with dissolve
            "That night's sleep, although in the hospital room, it was peaceful and restful."
            scene outside2 with llongdissolve
            play music "audio/outside2.ogg" volume 0.5
            "The following day he and the friends he gathered along the way, showed up in town's square, where the Headmaster is about to give start to the test."
            "And who am I? So vested in the leopard's life?"
            "Some might say I'm someone he loved."
            "Some might say I'm a nameless individual, looking for my place in the world."
            "Some might say I'm the devil."
            "Ironically, the leopard is the only one who would respond positively to all of the above."
            "And the only one who would respond positively to ANY of the above."
            "Everybody should hate me, yet nobody does, because the truth is kept by me and me alone."
            "Nobody knows what happened, but the fox's gaze is no longer soft when her eyes meet mine."
            "I'd lie if I said it doesn't eat me from the inside out, but it's not much different than how it was before we met, so I can cope."
            "In the end, I'm just a cat, a stupid, flawed, sad kitty-cat."


            "Anyway, if you've been here before, you know the drill."
            "It's almost time."
            scene endforest with dissolve
            "The Headmaster gives the starting speech and wishes his good luck."
            "The leopard and the other students are teleported inside a forest."
            "In the sky, appears a countdown."
            play sound "audio/timeup.ogg"
            "5"
            play sound "audio/timeup.ogg"
            "4"
            play sound "audio/timeup.ogg"
            "3"
            play sound "audio/timeup.ogg"
            "2"
            play sound "audio/timeup.ogg"
            "1"
            play sound "audio/button.ogg"
            "The test begins."

            jump badending



        elif betray <=2 and betray>=1:
            "When a voice stops him, whispering, calm and pleading..."
            c "Ku'sani, please think about us."
            "The cat does not turn around, but despite all odds, despite the adrenaline, he stops and listens while breathing heavily."
            "After all, judging by the particles of ash flying gently his way, the voice's body will become nothing more than a gem any second."
            c "This man is a traitor to you, a liar, a deceiver."

            c "He brought you only sorrow."
            c "He left you, again and again, while promising he is a friend."
            c "He would build you up, and betray you in the end."
            c "Going off to breed with your friends, rather than spend time helping you."

            c "I see you have no more magic, if you take him with you, you might even die."
            c "Why risk yourself with someone like this?"
            c "You got your revenge on me, spare your brethren, and let the ceremony commence."

            "The cat's gaze turns from anger to rage, with a scornful look and a wrinkled snout, he turns to look at the mangled, withering body."
            tt "If there is Nightfallen Hell, I hope I sent you there successfully."
            stop music fadeout 3.0
            scene finaltp with dissolve
            scene CGc35
            "The wild Furs around start to snap out of the initial shock, cowering in fear at their Chief's killer."
            "Eureka's sad ears disappear behind some trees, while Ruth sinks to his knees, looking at the ground."
            "Thankfully, the cat has bigger problems on his plate than to deliver vengeance."
            play sound "audio/teleport.ogg"
            scene finaltp2 with dissolve
            "With his path blocked by no other soul, he touches his friend's wounded face gently, disappearing together in a flash of blue light."

            jump hillsleep



        else:
            "A dying voice attempts to call his name for the last time."

            scene finaltp with dissolve
            scene CGc35

            "Unfortunately for whoever that is, the nameless cat is in no mood to listen to whatever nonsense any Nightfallen has to spit."
            "Twice kidnappers, attempted murderers, betrayers..."
            "He pushes further without looking back, with no intention of stopping, or listen to anyone."
            stop music fadeout 2.0
            play sound "audio/teleport.ogg"
            scene finaltp2 with dissolve
            "With nobody else daring to interfere after their Chief's fate, he touches his friend's wounded face gently, disappearing together in a flash of blue light."
            jump hillsleep




        label hillsleep:
        scene black with longdissolve
        pause 1
        play music "audio/slowpiano.ogg" fadein 2.0
        scene tateflowersblur with longdissolve
        "Birds are singing, daisies are still in full bloom."
        "Daisy...the flower of innocence, of purity, of new beginnings."
        scene tateflowers with dissolve
        scene CGc36
        "The fading rays of evening sunshine gently caress the two sleeping felines, casting a warm glow upon their peaceful forms."
        "The leopard still remains under the lingering influence of the drug, while the cat has exhausted his magical reserves completely."
        "Not only did he exceed the limits of teleportation, but he also employed a potent spell fueled by intense emotions, further straining his fragile body."
        "Against all odds, he mustered the last vestiges of his power to race to the side of his ailing companion."
        "With tender eyes, he gazes upon his friend, relieved to find that the once visible wounds have vanished without a trace."
        "Whatever the mysterious cause may be, a sense of contentment washes over him, filling his heart with gratitude."
        "And with a final smile adorning his weary face, he allows his eyelids to close, embracing the well-deserved respite."
        scene tatelaysmile with llongdissolve


        "He was warned before, that magic will be his doom."
        "Yet, he can not bring himself to hate magic for his own recklessness, the same way you don't hate a knife for self-inflicted wounds."
        tt "You'll be okay, you're home now..."
        tt "Don't worry about me, I was never afraid of death..."

        tt "It's just...{i}*yaaaawn*{/i} sleeping, but longer."
        scene black with longdissolve
        tt "..."
        tt "..."
        tt"..."
        "As the last flicker of magic fades, the remnants of birdsong and rustling wind subsides as well, leaving behind serene silence."
        "..."
        "Soft fur tickles his ears."
        "Warm fingers caress the back of his head."
        "The wind runs chill through his body again."
        x naked"Good morning, sleepyhead."
        tt"..."
        scene tateflowersblur with longdissolve
        "The sweet embrace of death played tricks on him, or perhaps he simply overreacted."
        "The only things he knows for sure...is that the light at the end of his tunnel is smiling warmly at him on a flowery hill."
        tt "Hi."
        stop music fadeout 2.0
        "..."
        scene black with llongdissolve

        "{i}A couple of minutes prior.{/i}"
        scene tateflowers with llongdissolve
        play music "audio/wisp.ogg" fadein 2.0 volume 0.2
        un scared"You're out!"
        un "WE're out!"
        un surprised"He saved us!"
        un "THE CAT SAVED US!"
        un "[name]! Wake up!"
        "Mhhhmm....ten more minutes."
        un ang"YOU WERE DRUGGED AND YOUR LIFE WAS ON KNIFE'S EDGE!"
        "Five more minutes?"
        un bored"Ughh, you're still under the influence."
        un "Do you have the mind to tell me to heal you?"
        "Huh?"
        un "Say this, {i}'Scribbles, heal me'{/i}."
        "Hmmm..."
        "Scribbles...heal me?"
        un eyeroll"THANK YOU!"
        un "I'm not much of a healer, but I can remove some poison, wounds and stabilize a person."
        un bored"There."
        stop music
        y nakedsurprised"!"
        "My eyes shoot open in a panicked state as I try to get up."
        y "I WAS KIDNAPPED!"
        un "Too late."
        un "You're okay now."
        play music "audio/wisp.ogg" fadein 2.0 volume 0.2
        "I look around me."
        "Instead of the dark forest, I see a vast blue sky going pink to settle for the evening."
        "The green and gold hill of white flowers, with grass soft as a mattress."
        "The evening wind flutters through my half naked body, the fur doing little to stop it."
        "Memories slowly coming back."
        "To my side I see my hero."
        "Peacefully sleeping tuxedo cat, innocent and pure, cute and beautiful."
        y nakedss"He looks alright, I hope he didn't go through too much trouble to get me."
        un bored"He's not breathing."
        stop music
        play sound "audio/scratch.ogg"
        y nakedsurprised"WHAT?!"
        un "He's not-"
        y nakedangry"THEN DO SOMETHING!"
        play music "audio/wisp.ogg" fadein 2.0 volume 0.2
        un suspicious"His wounds are not physical you idiot, he's not only out of magic, he went sub zero."
        y "You have to have something to give his magic back."
        un squint"I do, it's the medallion, why did I ever give it to you if you can't remember to fucking use it."
        y nakedbored"You mean the medallion that was in the pocket of my jeans?!"
        un bored"..."
        un eyeroll"UUUUGHHHHH, fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiine."
        un "I'll save the day again."
        un bored"Pray they didn't lock it in a safe or underground or something."
        stop music fadeout 3.0
        scene tateflowersblur with llongdissolve
        "I rush to my friend's side and place his head on my lap."
        "Please please be okay."
        "You have to be okay."
        "My life is not worth yours."
        play sound "audio/wack.ogg"
        "Please Scribbles hurry up whatever you're doi-Agh!" with hpunch
        "A pair of pants hit me in the face all of a sudden."

        un "Welp, here it is."
        "I take the medallion out in a hurry, and use it immediately to pump magic into him."
        un suspicious"Oi! Slow down!"
        un "Don't kill yourself in the process!"

        "I stop when fatigue takes over my body."
        scene black with dissolve
        "I watch nervously, Scribbles watches, the whole world is watching, hearts racing."
        play music "audio/outside2.ogg" fadein 2.0 volume 0.2
        "Then..."
        scene tatelaysmile with llongdissolve
        "The cat's eyes open."
        "A truck of relief hits me at that moment."
        "All I can say is something stupid, something goofy that nobody should ever say in a situation like this..."
        y naked"Good morning, sleepyhead."
        tt "..."
        tt "Hi."
        tt "..."
        tt "You're the most beautiful person I've ever met."
        y nakedsmug"Is that really the first thing you're going to say?"
        tt "I told you I like honesty above all else, and there is nothing more true I can think about."
        y "I did mention I missed your teasing at one point...didn't I?"
        tt "Yup."
        "His eyes sparkle with sincerity and admiration."
        "While mine shine because of the tears that wish to drop for him."
        "He will never know, but I almost lost him, the same way he almost lost me."
        tt "Your thighs are nice, I like them."
        y nakedbored"That is totally something normal to say."
        tt "Heh, I just want to make sure I speak out my mind before I die."
        tt "It can happen any day, you know?"
        tt "Cats don't actually have nine lives."
        y nakedss"I know..."
        y "Can you move?"
        tt "Am I making your lap too hot? Too bad, I like it here."
        y "No, I mean literally, can you move, like at all?"
        tt "Oh, uhmm..."
        tt "I think I can a little bit, but I barely feel my legs."
        tt "I am not walking anywhere before some rest, and I'm deeeefinitely not using magic any time soon."
        y nakedsimple"Same with me."
        y nakedss"Although, do you mind if I put my clothes back on? It's getting chilly up here."
        tt "Yeah, sure."
        scene black with dissolve
        "He raises his head with a bit of struggle, and I get up just enough to slide my pants, shirt and tie back on."
        scene tateflowersblur with dissolve
        tt "Where did you get your clothes from?"
        y awkward"They...were just here when I woke up."
        tt "Perhaps my spell brought them here."
        tt "Oh! Speaking of, did you see how cool I was?"
        y sadsmile"Sorry, I don't remember much after I was made unconscious."
        y "You'll need to catch me up on that."


        tt "Is there a better time than now?"
        tt"Neither of us can go anywhere."
        tt "Unless you want to play {i}'I spy with my little eye'{/i} or something, I see nothing else."
        y simple"Tell me..."
        y determined"EVERYTHING."

        tt "O-ok, wow, you're excited, here I go then."
        tt "{i}*cough cough*{/i}"

        "The cat starts off from the moment he ran away from the Wild Furs that kept asking for teleportation rides."
        "Their whole purpose was to drain him of magic, but because of me, he managed to restrain himself and conserve some."
        "He speaks of the Chief's stories, and hints of madness."
        tt "He was evil...but he was also broken by us, hunters."
        y sad "His deeds can't be excused, but they can be understood."
        "He tells me about our ex-friends' lies about my whereabouts and the only reason he got to me on time."
        scene field with llongdissolve
        y simple"A Mysterious Nightfallen with a mask on? Inside the barrier?"
        y "That is troubling."
        tt "It's because of him I managed to get to you in time, so I'm not going hunting for him, he's obviously not a threat."
        tt "And if he is, I'd defend him."
        "He continues with his step-father's speech, about the ceremony, and his past, as well as the huge mind powered spell he managed to pull at the last second, even if it almost cost him his life."
        tt "I'm sorry...it's me they wanted, not you."
        tt "They should've attacked me instead."
        y surprised"Never mind that, you KILLED him?"
        tt "Not intentionally!"
        tt "The spell just acted on emotions...and my emotions were of hate towards him, and desperation for your safety."
        tt "I don't regret it though."
        tt "They were raising me like cattle..."
        tt "I don't consider them family anymore."
        tt "I know they didn't have much of a choice under that madman's rule, but still..."
        y simple"What about...the wyvern?"

        tt "Eeh, I hope he grows up and eats them all."
        y "Ragnar says he killed a wyvern with his bare hands once."
        tt "Huh, so they're stronger than they look."
        tt "In any case, I got over him a long time ago."
        tt "I was being irrational because of my fear of being alone."
        tt "But I don't have to fear that now, do I?"
        "We look at each other with smirks growing wider."
        y smug"If I ever betray you again, shoot me."
        tt "Will do!"
        y simple"Wait no, don't actually."
        scene tatelaysmile with llongdissolve
        "We both laugh, hard enough to fall back over, laying on the grass side by side again."
        y "So...is this a happy ending?"
        tt "So far, it looks like it."
        tt "Still a lot of questions unanswered."
        y simple"Like how did the Chief and Ragnar get their hands on magic...?"
        tt "And how did he manage to use THAT specific spell on me...?"
        y "And who was the masked Nightfallen that helped you...?"
        tt "And why do you look so good in a loincloth...?"
        y blush"Oh, shush you."
        "We spend the next hour or so watching the few clouds still present in the sky."
        "It is peaceful, quiet, stress-free."
        tt "That one looks like a penis."
        y confused"What kind of messed up penis did you had the displeasure of seeing?"
        tt "I'm telling you."
        y bored"You don't even know what a penis other than yours looks like, do you?"
        tt "Maybe you should show me."
        y simple"I-"
        y blush"Shut up."
        y smug"Before I take you seriously..."
        tt "Heh."
        tt "Are you able to walk now?"
        y s"Yeah."
        tt "Do you want to stay here a little longer?"
        y sadsmile"..."
        y "Yeah."
        "Why ruin a beautiful moment with something as trivial as walking?"
        "Laying next to a loved one in a field of flowers in the evening is the ultimate form of tranquility."
        stop music fadeout 2.0

        play sound "audio/buzz.ogg"

        "Until your pants start to buzz."
        "Intensely."
        tt "Vibrator?"
        y bored"Phone."
        tt "Boring."
        "It's an unknown number."
        "Why not? A prank can't bring me down at this moment."
        "I put it on speaker."
        y simple"Hello?"
        play music "audio/forgetmenot.ogg" fadein 3.0 volume 0.2
        ch "{i}[name]?{/i}"
        y "Ye-"
        ch "{i}{size=50}OMG IT'S YOU!{/size}{/i}"
        "My head hurts and my ears feel like they're bleeding."
        ch "{i}DALLAN! DALLAN HE PICKED UP!{/i}"
        "Heavy hurried steps run to the phone."
        d "{i}[name]?{/i}"
        d "{i}Thank goodness you're alright.{/i}"
        d "{i}Is Tate with you?!{/i}"
        "The cat recoils slightly."
        y "Yeah, he's right here."
        d "{i}Where are you?{/i}"
        ch "{i}I SEE THEM!{/i}"
        ch "{i}ON THE FIELD IN THE NORTH EAST, BETWEEN THE FOREST AND THE OCEAN!{/i}"
        d "{i}Stay right there, we're coming.{/i}"
        "{i}*click*{/i}"
        tt "We?"
        y simple"And how does Chelsie see us?"
        play sound "audio/buzz.ogg"
        y surprised"Oh, another call, this one's from Aiden."

        tt "You'll want to keep that a bit further away from your ear."
        y simple"Why's that?"

        a "{i}{size=65}WHERE THE FUCK HAVE YOU TWO IDIOTS BEEN?!{/size}{/i}" with hpunch
        a "{i}WE'VE BEEN SO FUCKING WORRIED FOR YOU!{/i}"

        y simple"Nice to hear you too?"

        a "{i}Aghhh, wait for us.{/i}"
        "{i}*click*{/i}"

        tt "That's what we were going to do."

        y worried"Do you think we're in trouble?"
        tt "Is that what you're concerned about?"
        tt "Those nerds?"
        tt "We're too badass to get in trouble."
        y smug"That's true, we are, after all, the infamous troublemakers."
        tt "The purple and white demons."

        y simple"Oh, I hear people running up the hill."
        tt "I bet there are three of them."
        y "I bet there are four."
        stop music fadeout 2.0
        scene field with longdissolve
        "With heavy steps and heavy breaths, three bodies appear over the hill."
        "Me and my friend, the two lazy cats, struggle to get off the grass to face our visitors, not because we can't but because we don't feel like it."
        play music "audio/slowpiano.ogg" fadein 3.0 volume 0.4

        "They look kind of angry."

        ttt smug "Sup?"
        show wolf20angry2 at right with moveinright

        d "Is that all you have to say for yourselves?"
        show tiger20angry at left with moveinleft
        a "I thought we made it clear to stay out of trouble."
        y simple"how'd you know where we are?"
        y "Chelsie said she {i}'saw'{/i} us."
        show merina20bored with moveinleft
        m "She's on top of the academy, looking around with a telescope for the two of you."
        a "For the past three hours..."
        d "Together with Oliver..."
        a "That mouse is deathly afraid of heights too."
        y "Oh..."
        ttt bored "I'm sorry, but I still don't get it, what's the big deal here?"
        ttt "Why are you all so riled up?"
        ttt simple "I've been missing before."
        d "Yeah, for like, two hours, and under supervision most of the time."
        a "The PROBLEM now, is that you dragged [name] into this as well, two first years that nobody has seen since the battles."
        d "And we know you like to venture outside the barrier often."
        m "Theory confirmed when we kept calling [name]'s phone and it was outside the area of reach."
        m "And after exiting the barrier, your phone still didn't have signal."
        hide wolf20angry2
        show wolf20angry3 at right
        d "So we got worried, obviously."
        a "Especially since tomorrow we have a big, important test."
        a "We can't have you skip it so willy-nilly."
        hide tiger20angry
        show tiger20iritated at left
        y "I'm sorry we worried you, we should've come home earlier..."
        ttt simple "Yep...that would've been for the best..."
        d "Well, at least you're owning up to your mistakes."
        m "But will you explain where exactly you've been the whole day?"
        m "And why do you look so...defeated?"
        ttt bored "It's a long story."
        a "At least have the courtesy to get up when your leaders are talking."
        ttt "I literally can't."
        d "Why is that?"
        ttt simple "Our {i}legs don't work like they used to before.{/i}"
        hide wolf20angry3
        show wolf20simple at right
        hide merina20bored
        show merina20simple
        hide tiger20iritated
        show tiger20bored at left
        "They look surprised and skeptical, casting me a glance of confirmation."
        y simple"Well, we can use our legs, but we don't have the energy to stand much."
        a "And that's because..."

        y bored"As he said, long story."
        d "We got time, tell us all about it."

        ttt "Will you carry us if we do?"
        a "Ughhh."
        scene field with dissolve

        "And so, Dallan picks up the cat, and Aiden takes me on his back."
        scene campus1sunset with dissolve
        "We walk through the familiar streets, which are now starting to get illuminated by the energy lamps."
        "On the way, we tell them that we picked a fight with some Nightfallen, and that although we won, we lost a lot of magic, and didn't even get to collect our bounty."
        d "What kind of Nightfallen?"
        y "Oh you know...regular ones."
        a "Very descriptive."
        "Obviously we left out any mention of Wild Furs, or wyverns, or sacrifices etc."
        "Still, the story seemed to impress, scare and satisfy our escorts in the end, after the cat perfected the lie."
        "They all unanimously decided they should take us to the nurse's office, despite our protests."

        scene hallway3 with dissolve

        m "I'm just happy I didn't lose two new members and friends on the same day."
        d "I'm sorry you went through that, it must've been very scary."
        ttt smug "You have no idea."
        a "They got in that mess by misbehaving, I'd say it's deserved."
        a "Maybe next time they'll let somebody know where they're going."
        ttt bored "We're not children..."
        m "No, you're not, because children are far less reckless."
        stop music fadeout 3.0
        "You know you messed up when Merina is upset at your actions."

        scene hospital with llongdissolve
        play music "audio/hospital.ogg" fadein 2.0 volume 0.4



        "Oliver, Chelsie, Coal and Rose are already waiting for us in the nurse's office."
        "Personally, I'm just happy I made so many friends that care about me so quickly."
        "They express their joy, but it's hard to focus on them, when I still have so much to say to this amazing cat, I just need some time with him alone."
        "The nurse said the same thing we said, the problem is that we're out of magic and the remedy is to eat and rest..."
        show wolf20sadsmile at right with moveinright
        show merina20sadsmile with moveinright
        show tiger20bored at left with moveinleft
        d "Well, it seems like you'll be okay."
        ttt smug "We'll survive? Thank you Lord!"
        m "You two must be starving, why don't we go grab a bite?"
        m "Dinner time is almost over."

        hide wolf20sadsmile
        show wolf20smug at right
        hide merina20sadsmile
        show merina20smug

        d "You read my mind, m'lady!"
        m "Then after you, m'lord."
        a "At least I won't have to put up with those two now that you're back."
        a "Let's go, you heard the nurse."
        a "You gotta eat."
        hide wolf20smug with moveoutright
        hide merina20smug with moveoutright
        hide tiger20bored with moveoutright
        "Everyone in the room heads for the door and we follow without complaining."
        "Aiden and Merina both speak as if on the edge of bursting with anger at any comments we make, so it's better we shut up..."
        stop music fadeout 2.0

        scene cafsun with longdissolve
        play music "audio/lunch.ogg" fadein 2.0 volume 0.2

        "Our friends push multiple tables together making a large one instead."
        "We sit down and drink, some people prefer booze, some juice, others tea, as we wait for new food to be made for us."
        "All the girls are gathered together talking about preferred weapon types, a discussion in which Dallan was quick to join."
        "Oliver and Coal seem to get along surprisingly well, considering how shy the little mouse is, and Aiden is more than interested in Coal's magic device."
        a "Ten thousand."
        co "It's...not for sale, sorry."
        a "Twenty."
        co "{i}*sigh*{/i}"
        "It's hard to join a group, since I don't feel like socializing at the moment."
        "And frankly, after some time, I realize I want to be somewhere else, somewhere specific."
        "That I want to be WITH someone else, alone."
        "I love these people, but I love this one person a bit more...and I can't simply stand by idly."
        "I whisper part of my idea into the cat's ear and he happily agrees."
        y sadsmile"Uhm, hey guys."
        y "Thanks for everything, but we have some plans we have to get to."
        show wolf20 at right with moveinright
        show tiger20bored at left with moveinleft
        a "Plans?"
        d "What kind of plans?"
        y "We want to celebrate our little victories against the Nightfallen alone, up on the hill."
        show merina20 with moveinright
        m "A group picnic perhaps?"
        d "That sounds amazing actually."
        y awkward"N-no no, just the two of us."
        hide merina20
        show merina20sadsmile
        hide wolf20
        show wolf20sadsmile at right
        "Everyone in earshot saddens for a moment, before something clicks in all of their brains, at the same time."
        d "Of course, you two, together, alone, I have nothing against it."
        m "Let me prepare a dinner basket for you."
        hide merina20sadsmile with moveoutright
        hide tiger20bored
        show tiger202 at left
        a "Just make sure to use protectio-I meaaan...hey Merina, need some help over there?"
        hide tiger202 with moveoutright
        hide wolf20sadsmile
        show wolf20simple at right
        d "Although....hmmmm."
        d "Chelsie?"
        show chelsie with moveinleft
        ch "At your service."
        d "Can you put some kind of tracker device on [name]'s phone?"
        ch "If he lets me."
        y "Uhmmm, what for?"
        hide wolf20simple
        show wolf20bored at right
        d "I think you know exactly what for."
        y "Yeah..I do, here."
        ch "Alright, just a minute."
        hide chelsie with moveoutleft
        show merina20sadsmile with moveinright
        "Merina comes back with a bunch of food arranged neatly inside a basket that she hands to us."
        show chelsie at left3 with moveinleft
        show tiger20bored at left with moveinleft
        "Chelsie comes back with my phone, that looks exactly the same, that is a bit scary to think about, I could have a tracker on me at all times and not even know about it."
        hide wolf20bored
        show wolf20sadsmile at right
        d "Tate, I think you should accept a phone as well at some point, it's going to be useful."
        ttt simple"..."
        hide chelsie
        show chelsiesimple at left3
        hide wolf20sadsmile
        show wolf20simple at right
        hide merina20sadsmile
        show merina20simple

        "The cat cringes and recoils, not at the thought of owning a phone, but at the dead name being used."
        "I decide to intervene for the first time, now that all of our friends are in one place."
        y simple"Dallan, Merina, Aiden, everyone, please don't call him Tate anymore, that is not the name that defines him."
        "Everybody looks at me either curious or surprised, but my cat friend is the only one blushing."
        hide wolf20simple
        show wolf20sadsmile at right
        d "Just what happened in that adventure of yours?"
        y sadsmile"A mixture of emotions were churned and decisions were made."
        a "What should we call you then?"
        ttt sad "I...I'm not sure yet."
        y "We don't have time to explain every detail."
        hide wolf20sadsmile
        show wolf20 at right
        d "Well, little buddy, when you do decide, let us know!"
        hide tiger20bored
        show tiger20 at left
        a "As long as it's not {i}'Tartarus'{/i}."
        ttt sadsmile "It won't be, I learned my lesson."
        hide merina20simple
        show merina20sadsmile
        m "Why didn't you say anything sooner?"
        m "We could've helped."
        hide chelsiesimple
        show chelsiesadsmile at left3
        ch "We thought your name tagging was just for fun."
        ttt sad"Well...it was at the time, I guess."
        ttt "I just didn't think anyone would take me seriously."
        d "We will from now on, it's safe to say that much."
        hide chelsiesadsmile
        show chelsie at left3


        hide merina20sadsmile
        show merina20ex
        hide tiger20
        show tiger20bored at left
        d "Isn't that right guys?"
        m "Absolutely."
        ch "Count on me."
        a "Sure."

        ttt sadsmile "Thanks..."
        hide merina20ex
        show merina20

        m "Be on your way now, you don't want to waste the little daylight you have left."

        y sadsmile"Thank you so much for the food, and for your worries, and for your kindness."

        d "If we don't see each other before tomorrow morning, then I'll say it now, good luck on the test!"
        d "And other endeavors you might get yourself in."
        "He winks at me."
        a "Yeah, good luck, you little twerps."
        a "Although I'm sure you'll be fine if today's battles were any indication."
        m "May luck be on your side."
        show wolf20 at right2 with ease
        ch "Wishing you the best!"
        show ollie2smile at left2 with moveinleft
        o "I've got my fingers crossed for all of us."
        show roseec at right5 with moveinright
        r "Fortune be with you!"
        show coalec at left5 with moveinleft
        co "Stay safe and winning!"

        "This is enough to make a grown man cry, but I suck it up and resist!"
        "Seeing our friends come together like this after what we went through today."
        "I can't believe we were close to never seeing their smiles again."

        "We thank them again, looking back at the gathering of people we're leaving behind."

        scene campus1sunset with llongdissolve
        stop music fadeout 3.0
        play music "audio/wind.ogg" fadein 3.0 volume 0.2


        "The crisp air hits my lungs as soon as we step back outside."
        "These two cats are holding hands, swinging them back and forth playfully, because why should we be embarrassed about something so trivial after everything we've been through?"
        y sadsmile"I hope we don't regret leaving them there, we might be missing out on some fun."



        ttt smug "I made a point that I hate being lonely in the past few days."
        ttt "But that doesn't always mean the more the merrier."
        ttt "I'd much rather watch the sunset with someone like you, than a whole room of people I simply like."

        y "If I am more than {i}'someone you simply like'{/i} what does that make me?"
        ttt smug"Hey now, the turns have not reversed, you're not supposed to tease me."
        play music "audio/evening.ogg" fadein 3.0 volume 0.5
        scene tatesunset with longdissolve
        scene CGc37

        "Daisy petals fly past us, carried by the wind along with their faint perfume as we walk towards the highest point of the hill."

        "We find the steepest slope around to sit down on, watching the sun go down slowly, almost disappearing over the horizon."
        "We take out some sandwiches from the basket Merina prepared and eat in silence for a while."
        ttt sadsmile "Thank you, for defending my name earlier, or the absence of a name."
        y "That's what friends are for."
        tt"Weeell, no, friends are there to laugh at you, you are much nicer to me than a friend."

        "Speaking of friends, Scribbles, how did it make you feel, that I almost died?"
        un "Obviously that would've been...less than ideal."
        un "I don't want to lose my host."
        un "One of the only people who can take me."
        "I can smell excuses."
        "You like me, don't you?"
        un "You're ok, for a mortal."
        un "Wouldn't say {i}'like'{/i}, just tolerate."
        "That's progress, still."
        y sadsmile"It's a pity...the tribe turned out a bit insane."
        ttt "You kind of miss them too then, huh?"
        y "Is it weird if we do?"
        ttt "Nah, they deserved all our kindness up to the moment of religious kidnapping and murder."
        ttt "Hopefully they can leave peacefully now that their crazy Chief is gone."

        y "You were making progress with Ruth, he really liked you."
        ttt smug "Not as much as he liked your tail."
        y smug"Can you blame him?"
        ttt "Not even a little bit."
        y sadsmile"You said he was one of the guards holding you back... do you hold anything against him now?"

        ttt "The only actual evil is dead and gone."
        ttt "Reduced to a crystal."
        ttt "So no, I still like Ruth, he's a sweetheart."
        y smug"How much do you think he'd be worth?"
        ttt simple"Dude!"
        y sadsmile"What? I know that's your step dad, but I'm curious."
        ttt "Me too, actually."
        ttt smug"He was pretty old, so probably a fair amount."
        ttt "But it's illegal to sell Wild Fur crystals anyway, so it doesn't matter."
        y "What do you think will happen to their tribe now?"
        ttt "Ragnar will take over, most likely."
        y simple"Do you think he's a good fit?"
        ttt "I mean, he knows the difference between a wyvern and a dragon...at least there's that."
        y "He does?"
        y "Why didn't he do anything to stop his father then?"
        ttt bored"I assume because he was his father's anchor, his magic was always in the Chief's hands, so it's hard to do anything against someone with magic while you're powerless."
        y simple "That's true."
        ttt "But Ragnar is smart and cautious."
        ttt "He lived among our kind so he understands us better than his dad."
        ttt "He'll make a good enough leader."
        ttt smug"Maybe I could even visit sometime."
        y bored"Not without Dallan, Aiden, Merina and many more bodyguards with you."
        ttt smug"Heh, of course."

        y simple"Wait, if Ragnar knows that Seraph is a wyvern, then what will happen to him?"
        ttt simple"Are you worried for him?"
        y "I mean...even if he's a wild animal, he's still a living being."
        ttt sad"I'm assuming they must've killed him already..."
        ttt "There is no other logical solution to that."
        y worried"Oh no...I'm sorry."
        ttt sad"Don't be."
        ttt "I got irrationally attatched to a killer machine, all because I thought I have nobody that cares about me..."
        ttt sadsmile"But that is not true, is it?"
        y sadsmile"Not even close."
        y smug"And if I hear you say that ever again, I'll smack you."
        ttt smug"{i}*Gasp*{/i} You're so kinky [name]."
        if Tate_points >=10 and sex2 >=1:
            jump kisscat
        else:
            jump neveryoumind
        label neveryoumind:


        ttt simple"..."
        ttt simple"Hey, [name]?"
        ttt"May I ask you something?"
        y s"Go ahead."
        ttt "Back at the Nightfallen camp, was what Eureka and Ragnar said true?"
        ttt sad"That you...did things in there?"
        ttt simple"I mean, obviously I'll believe what you say over them, they are dirty little liars and manipulators, working for a tyrant, I don't doubt that, but I want to hear it from you."
        ttt sad "Are you...still a virgin?"
        if sex2 >=1:
            menu:
                "Am I...?"
                "No. (Truth)":
                    "He always had a nudge for finding the truth, no matter if it's false words or false personalities, he somehow knows."
                    "It's futile to hide it from him."
                    y "No...not anymore, I'm sorry."
                    ttt simple "..."
                    ttt sadsmile "I appreciate the honesty, I honestly thought you'd at least try to lie."
                    ttt "But you know you can't lie to me, don't you?"
                    y sad"I know...and you have the right to be upset."
                    ttt sad"It started as a joke, but I really thought we'll walk on this slutty hunter career hand in hand."
                    ttt simple"Well, still, I'm not going to blame you."
                    ttt "I'm not mad, just disappointed."
                    y "..."
                    ttt "..."
                    ttt "How was it?"
                    y simple"What?"
                    ttt "The sex."
                    ttt blush"How was it?"
                    ttt "If you did it, might as well have the courtesy to tell me all about it."

                    jump nokisscat


                "Yes. (lie)":
                        "I love him."
                        "I didn't say it yet, since my heart is caught in my throat every time I even think about it but I do."
                        "I know fucked up with my decision earlier, but it's too late to go back, I might as well cover it up."
                        y sadsmile"Yeah, I am, didn't I make a promise that you'll be in the room when that happens?"
                        y "Unless you meant that as a joke, because I sure didn't."
                        "I slide my hand on top of his, which was resting on the evening's sun-kissed grass."
                        "But he slides it away."
                        tt "You don't have to lie, you know?"
                        y "I..."
                        tt "I appreciate what you're trying to do."
                        tt "I'm sure you didn't have me in mind when you decided to have fun with the insanely hot Nightfallen that are also interested in you."
                        tt "I'm not sure if that hurts more or less, honestly."
                        y "I'm sorry..."
                        y "You-"
                        tt "I know, I know I said I'll believe you, but the truth is, no matter what those two told me, I can tell what you did..."
                        tt "Call it a hunch, an instinct, whatever, but I know."
                        y "..."
                        tt "..."
                        tt "How was it?"
                        y "What?"
                        tt "The sex."
                        tt "How was it?"
                        tt "If you did it, might as well have the courtesy to tell me all about it."

                        jump nokisscat

        else:
            menu:
                "Am I...?"
                "No. (Lie)":
                    y sad "No...I'm sorry, I'm not..."
                    y "I wanted to confess earlier, but this guilt I'm feeling over betraying yo-"
                    play sound "audio/wack.ogg"

                    y hurt2 "Ouch!" with hpunch
                    ttt blush "Cut the lies, twink."
                    ttt "I know that's not true."
                    y surprised"No no! I'm serious!"
                    y smug"Your brother's dick was enormous, you should've seen how much it stretched me and then-"
                    ttt pf"Stooooooop!"
                    ttt "Don't talk about my brother's huge cock in front of me."
                    y simple"It's way worse when you say it."
                    y sadsmile"How come my lie didn't work?"
                    y "How would you know what we did in private?"
                    ttt s"Told you, I have good instincts when it comes to lies."
                    ttt smug"Plus, you're a bad liar."
                    y sadsmile"What makes me such a bad liar?"
                    ttt smug"Nerd."
                    y bored"Ok, cat."
                    ttt "..."
                    ttt simple"..."

                    jump kisscat
                "Yes. (Truth)":


                    y sadsmile"I know I spent a lot of alone time with Ragnar and Eureka, but you don't have to worry."
                    y "I refused any attempts of theirs to get in my pants."
                    y ec"I promise I'm still pure as fresh snow!"
                    ttt simple"..."
                    ttt smug"Nerd."
                    y surprised"Wha-"
                    y angry"I kept my promise for you!"
                    ttt s"Heh, yeah yeah, I know, I'm just teasing."
                    ttt sadsmile"I actually really appreciate you taking our promise seriously."
                    y sadsmile"I know how much betrayal affects you."
                    ttt "..."
                    jump kisscat







            label nokisscat:
                y surprised"You...want to know?"
                ttt smug "Every little detail."
                ttt "I want sizes, feelings, movements, everything."

                y sadsmile"Then I guess I'll tell you all about it."
                "The intimate but awkward moment did a full one eighty with that one question."
                "The feeling of betrayal in the air fades, replaced by curiosity, joyfulness, and if that bulge the cat is trying to hide is any indication, lust as well."
                ttt simple"He was THAT big?"
                ttt "There's NO way you took him."
                y smug"Believe it, balls deep."
                y simple"I think I still have his cum inside me as well."
                y "It hurts when I sit down too."
                ttt simple "That is..."
                ttt surprised "Awesome."
                ttt s"I hope my first time at least compares."
                ttt bored "Monty lost his virginity in a public bathroom, in a threesome with two complete strangers when he first came here."
                y bored"Ew."
                y "Yeah, you're way better than that."
                y sadsmile"Are you...really not upset?"
                y "I'm not as good as you at detecting lies."
                ttt sadsmile"Promise I'm not."
                ttt "Well, I might be a little hurt you broke your promise, but this is a Hunter's academy, Nightfallen intercourse is what we're all about."
                "This conversation clashes with my plans...those being to take our relationship further."
                "But second thoughts linger."
                "Time feels like it stopped."


                "As the sun sank beneath the horizon, casting its warm, golden hues across the rolling daisy filled hills, I stood at the hilltop crisscrossed next to my sweet cat friend."
                "My eyes locked on the breathtaking view spread out before me."
                "A gentle breeze caressed our fur, and a serene calmness settled deep within our bones. But amidst the tranquility, my heart beat with a restless unease."

                "Beside me, he now stood in silence, his presence a comforting weight."
                "We had spent the past few days exploring, wandering through the wilderness, and sharing quiet moments of laughter."
                "There is an undeniable connection between us, an intimacy that seemed to transcend words."
                "And now, on this hill as the sun bid us farewell, the air crackled with the unspoken possibility of..."
                "Of a kiss."
                "A seal and a promise for this new step in our lives."

                "I steal a sideways glance at him, his face basking in the warm glow of the setting sun."
                "The delicate curve of his lips and the depth in his eyes became even more captivating."
                "He's lost in his own thoughts, whether those thoughts are about me or not, whether they're positive or not..."
                "It was a suspended moment, an invitation hanging in the air, tempting us to step into a realm beyond friendship."
                "Yet, within the recesses of my mind, doubts begin to sprout."

                "Is it too soon? Were we reading the signs right? Were we prepared to cross that threshold, to redefine the boundaries of our relationship? Uncertainty twisted within me, blending with desire and apprehension."
                "No...it shouldn't be too soon, but the circumstances are delaying the moment."
                "Perhaps if I didn't treat him like a secondhand partner, his lips would be the ones I'm lost in, instead of thought."
                "Still..."

                "Taking a tentative step closer, our shoulders almost touching, I feel the charged air that swirls between us."
                "My hand trembles, longing to bridge the remaining gap. But as my fingers hovered, I hesitate, held back by the weight of unspoken fears."

                "The fear of losing him as a friend gripped me tightly."

                "His face turns to me with a  soft smile on, as if daring me to make the next move cautiously."
                "I grab his hand in mine, then turn back towards the setting sun and plant the side of my head on his shoulder."
                "This is it, this is what I'm choosing for now, a decision he is grateful for, leaning against me as well."

                "Together, we watch as the sun completed its descent, leaving behind a canvas of deep oranges and purples that paint the sky."
                "The silence between us carries a newfound complexity, an unspoken agreement."
                "Though our lips had never met, the lingering desire was etched in the spaces between our stolen glances."

                "He rests his head slowly on my shoulder, cementing the thought that kissing is out of the question."

                ttt sadsmile "You know that I like you very much, don't you?"
                y sadsmile"You know I like you even more, right?"

                ttt smug"I know you're the only one that respects me."
                ttt "That is proof enough."

                ttt simple"..."
                y simple"Do you think you would have stayed with them if they didn't...you know, try to murder me?"
                y "Even if I protested?"
                ttt simple"Would you have been against it?"
                y "Of course, but I don't think I would've told you so."
                y sadsmile"I'd just try to be happy for you."
                ttt smug"Of course you would, you ray of sunshine."
                y bored"Is that sarcasm?"
                ttt smug "For once, no."
                y sadsmile"Oh, well, thanks then."
                ttt "To be fair, I probably would've stayed for a while, then get bored and come back."
                ttt "I like nature, but I need a hot, steamy shower from time to time, and a comfy bed."
                y ec"I get that, plus, imagine how exhausting it would've been to constantly sleep with everyone."
                ttt simple "What do you mean?"
                y s"Well, they can recharge much much faster using our kind as partners, everyone would've wanted you to get rid of their lust daily."
                y "Day and night, everyday, with all sorts of different Wild Furs."
                ttt "..."
                ttt pf "I'll...be right back."
                y bored"If you set foot in that camp again I'm telling."
                ttt simple "Damn it."
                y "You couldn't do it anyway."
                ttt pf"Why do you think so?"
                ttt "I bet I could gather a lot of bodies, if I wasn't so scared of starting."
                y smug"Because you'd have have to satisfy women too."
                ttt pf"Oh...yeah, I don't know how to do that."
                y smug"And speaking of steamy showers and comfy beds..."
                ttt simple"It's getting pretty late, huh?"

                y simple"We have a test tomorrow too."
                ttt s"What are you going to do about it?"
                y "The test?"
                ttt "No, about the shower and bed?"
                y smug"Well, the boring answer is that you go to your dorm and I'll go to mine, then we meet in the morning."
                ttt smug "How {b}dare{/b} you give me the boring answer first?"
                y "In that case, how about I invite you to my bed."
                y "I want to sleep next to you and your comically cartoonish pajamas."
                ttt s"I can take that offer."
                ttt smug"Can't wait to use your headless shower."
                stop music fadeout 2.0
                y pf"It's not my fault they did me dirty like that!"





                jump sleepingcats


                #(chibi of us sleeping in bed.)



                label kisscat:

                $ catkiss +=1

                ttt simple "I only recently realized you haven't been addressing me by my old name, like...at all."
                y simple"Isn't that what you wanted?"
                ttt sadsmile "No-I mean yeah, absolutely, I was just a little taken aback by the commitment."
                y smug"Better believe it, because I haven't said it in my mind either."
                ttt surprised "Wow, that's a strong will right there."
                ttt simple"I hate when things pop in my mind without my consent."
                y smug"Somebody with so much mind power, the master manipulator? Hard to believe."
                ttt smug "My mind is too wild to keep thoughts caged."

                "Both of us steal glances at each other when we think we won't be noticed."
                y s"The sky is beautiful."
                ttt simple "It makes me anxious."
                y simple"Why? Because it's as red as blood?"
                ttt "No, because it marks the end of the day...which means it's time to pass out for a while, away from each other."
                y confused"Away? Who said anything about away?"
                ttt "Huh?"
                "I hug him with both arms, as hard as I can."

                "His ears flick rapidly and eyes widen."
                y smug"I'm not letting you get away from me."
                ttt sadsmile "Ever?"
                y ec "Never."
                ttt smug"Heh."
                ttt "I should be the one to say that, as the hug expert."
                ttt sadsmile"But it turns out I have a harder time saying things that I mean wholeheartedly."
                ttt blush"Teasing is easier."
                y blush"Is that why you're blushing so heavily?"
                ttt "You're blushing too!"
                y "That's a given, I'm a shy guy by nature."
                ttt smug "You're not good at showing that, with all this touching."
                y "Stop being so soft, and I won't touch you."
                ttt sadsmile "..."
                ttt"[name]?"
                y "Yeah?"
                ttt simple "If I ever got in trouble, or you needed my help, you'd have to call out my name."
                y simple"Theoretically."
                ttt "..."
                ttt sadsmile "Names are given by special people, to special people, for special reasons."
                ttt "That's my philosophy."

                ttt "I'd say saving my life is a good enough reason why you should have this honor."

                y surprised"What are you saying?"
                ttt "I'm saying that I want you to give me a name."
                ttt "Preferably something Aiden can't tease me about."

                y worried"Name you?"
                y "B-but, I'm really bad with names."
                y "Are you sure?"
                ttt smug "Hey, I'm sure it can't be worse than what I came up with until now."
                ttt sadsmile"So yes, I'm sure."

                y "Do I have to do it right now? On the spot?"
                ttt smug"Yep."
                ttt "I want one now, give it to me now or never."
                "Alright...here I go."
                "What name would be fitting for this eccentric, friendly cat."
                "His name was 'Tate' before, which means cheerful."
                "He hated it because he thought it was too surface level, and because it was not chosen by somebody he loves, but by the community."
                label catname:
                "I need a unique name that represents him, sounds good and he'd love."
                $ catname = renpy.input("His name will be...", length=15)
                $ catname = catname.strip()

                if catname =="Tartarus":
                    y ec "[catname]."
                    ttt simple "..."
                    ttt bored "Why?"
                    y sadsmile"It grew on me."
                    ttt "The name that everyone made fun of me for?"
                    ttt "No thanks, please think harder."
                    y simple"Oh...ok, I'll try again."
                    jump catname
                elif catname =="tartarus":
                    y ec "[catname]."
                    ttt simple "..."
                    ttt bored "Why?"
                    y sadsmile"It grew on me."
                    ttt "The name that everyone made fun of me for?"
                    ttt "No thanks, please think harder."
                    y simple"Oh...ok, I'll try again."
                    jump catname
                elif catname =="Tate":
                    y ec "[catname]."

                    ttt bored "No thanks, please think harder."
                    y simple"Oh...ok, I'll try again."
                    jump catname
                elif catname =="tate":
                    y ec "[catname]."

                    ttt bored "No thanks, please think harder."
                    y simple"Oh...ok, I'll try again."
                    jump catname
                elif catname =="":
                    ttt bored "You can't just...not choose anything."
                    ttt "Come on! Think!"
                    y awkward"S-sorry, I'll try again."
                    jump catname
                else:

                    y ec "[catname]!"
                    ttt "..."
                    y "What do you think?"
                    ttt sadsmile "It's definitely...unique."
                    y simple "You don't like it."
                    ttt bored"I don't..."
                    y "Alright, no worries, I'll-"
                    ttt "Like, no offense, but I really really don't like it."
                    y "Got it, jus-"
                    ttt pf"Truly the worst name you could've picked, it is bordeline offensive, did you even think about it before-"
                    y angry "I GET IT!"
                    y pf "I told you I'm bad at names."
                    ttt sadsmile"No, it's okay, I'm just a little on edge since this is a big decision I put on your shoulder, just...try again."
                label catname2:
                    $ catname2 = renpy.input("His name will be...", length=15)
                    $ catname2 = catname2.strip()
                if  catname2 =="":
                        ttt bored "You can't just...not choose anything."
                        ttt "Come on! Think!"
                        y awkward"S-sorry, I'll try again."
                        jump catname2
                else:

                    y s"[catname2]."
                    "He makes a disgusted face."
                    y bored"..."
                    ttt sadsmile"One more try?"

                    "Let's find another one, I guess..."
                    "Ughh, but there aren't any names that both fit him AND sound really good!"
                    "Why couldn't you just be named Billy or something...That way a new name would've been easy."
                    un bored"{size=20}Psst.{/size}"
                    "Hey, Scribbles."
                    un "Want some advice?"
                    "Do you have a name suggestion?"
                    un simple"Not really, I have a theory."
                    "Uhm, sure? Let's hear it, but make it fast."
                    un "I don't think he hates his name as much as he says he does."
                    un "He simply hates the origins of it."

                    "So you're saying that I...don't have to change it after all?"
                    un bored"Interpret that however you want, I just spoke my mind."
                    un "Names are very sacred to us demons as well, so I understand what it means to feel like your name doesn't fit."
                    "That might be why he's so reluctant to accept a new name..."
                    "Tate..."
                    "Foster?"
                    "This might be the stupidest name that I can choose yet, but it's worth a try."
                    ttt smug"Sooooo?" with llongdissolve
                    y ec "Tate Foster."
                    ttt simple "..."
                    ttt simple"What?"
                    y s"Tate Foster, I think it suits you."

                    ttt bored "What are you doing?"
                    ttt "Are you making fun of me?"
                    y sadsmile"No, I'm as serious as I can be."
                    y "Let me explain."
                    ttt pf "Please do. In detail."
                    y "We only met each other three days ago."
                    y "The whole time we've spent together, that's the only name I've known you by...other than the...bad ones."
                    y "Your name is perfect the way it is, and perhaps you'll believe it from the mouth of somebody you love? If nobody else."
                    y "You are my cheerful cat friend, and I don't want you to feel like you have change, or that I don't like the version of you that I met on the first day, because I do."
                    ttt sad"What about my-"
                    y "As for your last name, maybe you read too much into it, or not enough."
                    y "{i}'Foster'{/i}...doesn't that also mean {i}'woodsman'{/i}?"
                    y sadsmile"Do you really think that they had the literal meaning of the word in mind when they gave it to you?"
                    y "As far as I've seen, everybody around here kind of...likes you, a lot."
                    y "And there's nobody that likes nature more than you, so I'd say they hit the spot."
                    y "Who wouldn't want to be named after the thing they love most?"
                    y ec"Tate Foster, a cheerful woodscat."
                    ttt simple "..."
                    ttt pf "{size=20}So a hippy?{/size}"
                    y bored"Your new name is Bennedict Cumberbatch, final answer, let's go home now."
                    ttt sadsmile "NO NO NO! I'm joking!"
                    ttt "Sorry."
                    ttt sadsmile "I just find it hard to be serious in emotional moments."
                    ttt sadsmilecry "I'm kind of..."
                    y sadsmile "Are you crying?"
                    ttt "W-what? No...no way a nerd like you could make me-{i}*sniff*{/i} cry."
                    ttt "But if you wanted to hug me again I wouldn't say no."
                    "I do just that, until his few tears get soaked into his fur and disappear."
                    "I didn't hear his feedback yet, but tears are a good hint it's probably going to be positive."
                    y sadsmile "So?"
                    ttt sadsmile"Honestly?"
                    ttt "I was skeptical at first."
                    ttt sad"Hearing my name come out of your mouth...not once did I feel weird about it."
                    ttt "You kind of made me realize that I'm not as alone as I thought I was."
                    ttt sadsmile"There are a lot of people that I care about, and I now know they care about me too."
                    ttt "Having a name that they chose collectively is proving to be less and less of a bother."
                    ttt "Right now, it's a bit embarrassing to say, but you're the most important person in my life, so having your blessing on this means I can finally accept it."
                    y surprised"Does that mean?"
                    tttt ec "Yep, I'll be keeping my names."
                    tttt smug"To be fair, I'm not sure how I'd feel if you had any other names other than [name] [name2], as weird as those are."
                    y simple"What's so weird about them?"
                    tttt s"I wonder how the others will react, since we did say I'm changing it."
                    y s"I'm sure they'll be happy with your decision, after all, you're the only one that disliked your names in the first place."
                    tttt "Heh, you're right."
                    tttt "I'm so happy I caught you in my hole."
                    tttt "Almost as if God sent me an angel to solve all my identity problems."
                    y smug"I had to fix you before grabbing your tail."
                    tttt blush"Is that a flirting attempt?"
                    y "So what if it is?"
                    tttt smug"From mister virgin himself?"
                    y "You're a virgin too."
                    tttt "But I'm way better at seduction."
                    tttt "I told you before that I can bed anyone anytime."
                    tttt "My lust game is on another level."


                    y smug"Alright...then kiss me."
                    tttt blush2 "What?"
                    scene tatekiss with longdissolve
                    scene CGc38


                    y smug"Prove it, kiss me right now, on the lips."
                    tttt "Y-you can't just say that!"
                    y sadsmile"Why not? Don't you like me?"
                    "I slide closer to him, almost touching faces, and he looks away."
                    y smug "If you say you can get anyone you want, try to get me."
                    y "See, one other thing I noticed about you these days, is that your teasing has its limits."
                    tttt blush2"I...it's not that I don't want to..."
                    y sadsmile"You've never kissed anyone before?"
                    "He shakes his head."
                    y ec "No worries, me neither!"
                    tttt blush"Your confidence is growing at an alarming rate..."
                    y smug "Do you not like it?"
                    tttt "I don't like trading roles in this relationship."
                    y "Aww, but I had such big plans to-"
                    scene tatekiss2 with dissolve
                    stop music
                    play sound "audio/buzz.ogg"
                    play music "audio/tulip.ogg" fadein 2.0 volume 0.3
                    "{i}*Buzz*{/i}" with hpunch
                    "{i}*Buzz*{/i}"
                    y simple "Huh?"
                    "My phone is ringing."
                    tttt blush"{i}Phew{/i}"

                    "Another unknown number."

                    "{i}*Click*{/i}"
                    y "Hello?"
                    play sound "audio/wack2.ogg"

                    ch "{size=60}{i}KISS ALREADY!{/i}{/size}" with hpunch

                    tttt simple"Chelsie?!"

                    "The phone wasn't even on speaker, yet it sure sounded like it."

                    d "{i}Chelsie! I told you NOT to call them!{/i}"
                    ch "{i}But look at them! Neither is making the first move!{/i}"
                    a "{i}I'm sure [name] would've done something if we waited a little longer.{/i}"
                    o "{i}They seemed to have a tense moment just then.{/i}"
                    y angry "{i}Hold on, how many of you are there?{/i}"
                    tttt bored "And how do you see us?"
                    m "{i}Chelsie brought more telescopes for us.{/i}"
                    "Indeed, atop the academy, multipe silhouettes can be seen, like ants on a hill."
                    m "{i}Haima is here too, and Monty is finally out of the hospital.{/i}"
                    a "{i}What a miracle...{/i}"
                    monty "{i}Hello cat and new stranger!{/i}"
                    ha "{i}I was promised a show.{/i}"
                    y surprised"Is the whole academy watching?"
                    d "{i}Rose and Coal had to go meet someone, but the rest of your friends are here!{/i}"
                    y "A-all...the rest?"
                    ch "{i}Yeah!{/i}"
                    ch "{i}And we're not seeing enough action!{/i}"
                    y awkward "A-about that."
                    stop music fadeout 2.0
                    "{i}*Click*{/i}"
                    "Suddenly, Tate grabs the phone and hangs up, throwing it to the side."

                    y "What are you-"
                    y surprised"!"
                    play music "audio/hope.ogg" fadein 2.0 volume 0.3
                    scene tatekiss3 with longdissolve
                    scene CGc39
                    "He grabs my tie, and plants his lips on mine."
                    "Fast, with determination and confidence."
                    "It was a swift exchange of warmth and affection, a brief yet meaningful connection."
                    "Time seemed to pause for that split second, as my heart raced with excitement."
                    "Though the kiss was brief, its impact lingered, leaving behind a sweetness I can not describe in the air and a promise of more to come."
                    "That is, if we weren't the shyest, most sexually charged people at the academy."
                    "I barely got to process the moment, my eyes opened the whole time, when he slowly pulls away with a smile."
                    scene tatekiss4 with llongdissolve
                    "Even if our tongues remained tame for these tantalizing moments, I can still taste him well."
                    "My mind is still in paradise when he calls my name."
                    tttt blush "[name]?"
                    y blush "Wow..."
                    tttt "I take it I did good?"
                    y "Yes, yes, a thousand times yes."
                    y "But...why now?"

                    tttt "I noticed your withdrawal when Dallan mentioned people are watching."
                    tttt "Your confidence kind of drained away in an instant."
                    tttt "So I decided that I either do it now...or we never do it."
                    y sadsmile "I'm glad you did it."
                    y "You're right, I wasn't so sure about an audience at first, but after this...I think it's worth it."
                    tttt sadsmile"You taste good."
                    y smug"I don't compare to you."
                    tttt "I hope the others enjoyed the show."
                    scene tatekiss2 with dissolve
                    stop music
                    play sound "audio/buzz.ogg"
                    play music "audio/tulip.ogg" fadein 2.0 volume 0.3

                    "{i}*Buzz*{/i}"
                    y simple "Speaking of."

                    "{i}*Click*{/i}"
                    y s "Heeello?"
                    play sound "audio/wack2.ogg"
                    ch "{i}YOU CALL THAT A KISS?!{/i}" with hpunch
                    y simple "What?"
                    play sound "audio/wack2.ogg"
                    eve "{i}{size=65}CHELSIE! STOP CALLING THEM!{/size}{/i}"
                    ch "{i}Oh come on, I didn't bring these telescopes here for nothing.{/i}"
                    ch "{i}I can't be the only disappointed one.{/i}"
                    m "{i}You do have a point...{/i}"
                    d "{i}Merina!{/i}"
                    a "{i}She's kind of right.{/i}"
                    d "{i}*gasp*{/i}"
                    d "{i}Actually...yeah.{/i}"
                    stop music fadeout 3.0
                    "Tate takes my phone once again, but doesn't hang up."
                    tttt bored "Guys, please stop, I know that's how the lot of you approach things, but [name]-"
                    "Before he can continue, it is my turn to take the phone away and throw it to the side."
                    y smug "Eh, we both almost died today, I can be bold for once."
                    tttt simple "What are you-"
                    play music "audio/hope.ogg" fadein 2.0 volume 0.3
                    scene tatekiss5 with longdissolve
                    scene CGc40

                    "With a swift move, I reverse the previous roles and close the distance between us."
                    "Instead of a quick, vicious smooch, comes a tender mouth embrace."
                    "I ignore the shocked expression he has, the same way he ignored mine before."
                    "Our first kiss was electric, this one: paralyzing."
                    "I continue our new experience by pushing my tongue deeper inside, and soon, the surprised cat does the same."
                    "With all eyes closed, nothing but sensations guide us further."
                    "Although far more intimate, long and sloppy, this would not satisfy an audience."
                    "And frankly, it isn't enough for me either."

                    "I push my head harder towards him, squishing our noses together, until he loses balance and I topple him over."
                    scene tatekiss6 with llongdissolve
                    scene CGc41
                    "No more shocked faces, no more surprises, Tate fully embraces the moment, wrapping his legs around me, as I hold his hands tight above his head."
                    "Only when his head is fully against the grass do I stop trying to overwhelm him."
                    "The faint sloppy, wet lips are the only sounds that invade my ears, along with the evening wind and...cheering?"
                    d "{i}Look at them go!{/i}"
                    ch "{i}That's what I was talking about! Woohooo!{/i}"
                    m "{i}It feels like only yesterday we were shunning him away from sex classes...{/i}"

                    y simple"Oops, I forgot to hang up when I threw it away."
                    y "Let me just-"
                    tttt smug "Don't you dare stop."
                    scene tatekiss7 with longdissolve
                    scene CGc42
                    "The hungry, needy cat grabs my head and restarts our makeout session."
                    "More intense than ever before, it feels like he's trying to taste me from every angle, and each bite is better than the last."
                    "I can't complain, this is what I thought he'd be like, before finding out he's as inexperienced as I am."
                    "As my head is busy being attacked by this scary predator, my hands are finding their own places to explore."
                    ch "{i}Aaaaaahh, look! Look he's doing it!{/i}"
                    d "{i}Oh my lord, is he...{/i}"
                    a "{i}He's really sticking his whole hand in there.{/i}"
                    m "{i}It is important to stretch those muscles before you start, good thinking [name].{/i}"
                    ch "{i}How many fingers do you think-{/i}"

                    y blushmad "I'm JUST touching him! Stop fantasizing over there!"

                    "We continue our tongue battle for what feels like hours, trying to ignore our friends' scarce, lewd comments."
                    "Every fun moment has its end, and unfortunately, as the one on top, it's my duty to be the first to break the kiss, once and for all."
                    scene tatekiss8 with llongdissolve
                    scene CGc43
                    "With heavy breaths, we open our eyes and look at each other."
                    "A trail of saliva between us fighting the forces of gravity and barely losing."
                    "Those sparkles in his irises, that slight crooked, toothy smile, the fluffy cheeks covering the bottom of his eyes making said smile more sincere, how could I not see...that he's always been looking at me that way."

                    "Who will recover enough air in their lungs first to say the fated words?"

                    y sadsmile "Tate...I-I love you."
                    tttt sadsmile "I lo- love.. you too."
                    "Perhaps both of them."

                    "The other line is now impossible to ignore, as fangirls are screaming with excitement."
                    "I take a second, now that Tate finally lets me, to get my phone and hang up."
                    y simple"No more interruptions."
                    tttt "Why? Did you have some more things in mind?"
                    y smug "There are so many things I want to do to you in my mind."
                    y "There's nothing that can stop me from getting my hands on you now."
                    tttt smug "Then what's stopping you?"
                    tttt "Fuck me right here, right now."
                    stop music
                    y "No."
                    tttt simple"What?"
                    tttt sadsmile"Why NooOoOoOt?"
                    play music "audio/hope.ogg" volume 0.3
                    y sadsmile"Tate, all our friends are watching."
                    y "And it's getting pretty late, we have a test tomorrow, which honestly? Makes me nervous."
                    tttt "Eh, I was joking anyway."
                    tttt smug"Even though a field of daisies at sunset is not the worst place for your first time."
                    y "Maybe when less eyes are on us."
                    tttt s"So, your room or mine?"
                    y s"Mine."
                    y smug"I might not have a shower head, but at least my bed isn't half full of stuffed animals."


                    tttt smug"So two negative points..."


                    y smug"We're going to need all the space we can get on that bed."
                    tttt blush"Are you...are you saying we're gonna do it?"
                    stop music fadeout 2.0
                    scene tatesunset with longdissolve
                    play music "audio/evening.ogg" fadein 2.0 volume 0.3
                    y "We'll see what happens."
                    y "In the meantime, let's get a move on."
                    y "We'll need to take the longer route, just so we don't meet any of our friends on the way."
                    t "Yeah...that would be awkward."
                    t "I don't feel like talking about this with them yet."
                    y "There is one thing you should talk to them about."
                    t "What's that?"
                    y "Your name?"
                    t "Oh right!"
                    t "Can I borrow your phone?"
                    stop music fadeout 3.0

                    scene campus1night with llongdissolve
                    play music "audio/nightsounds.ogg" volume 0.6
                    "The sun has dipped low over the horizon by the time we get back to town, engulfing our world in darkness."
                    "But as I said on the first day we met, my sun is always walking beside me, taking the form of a cheerful cat."
                    "We walk holding hands across the streets of Lakonia, as the news of his name travels from phone to phone."
                    "As someone that doesn't own a phone, he sure likes talking with one against his ear."
                    "He gives the news and announces his name proudly, and thankfully, everybody is very happy for him."
                    "I was not the only one who thought he already had a perfectly good name, Dallan almost started crying and Merina definitely sobbed once or twice."

                    label sleepingcats:


                    scene dormroomnight with longdissolve
                    "We arrive back at the dorm."
                    "The room is dark and cool."
                    scene dormroomnight with dissolve
                    play music "audio/nightsounds.ogg" fadein 3.0 volume 0.8
                    "The lights still don't work, but it's not like we need them much."
                    "As perverted as we both are, we silently agree that it is not the time to shower together."
                    "It's for the best, since we will definitely not be able to keep our hands from each other's naked bodies, and we can't afford to waste precious sleep time."
                    "He goes in first, then I follow after."
                    "His fur is glossy and soft looking, the daisy perfume easily noticeble when I walked past."
                    "The radio is on when I get out, connected to the weather channel."
                    play sound "audio/rain.ogg" volume 0.3
                    "{i}The weather tonight will be rainy, but we will be welcomed by a cloudless, sunny day, tomorrow morning.{/i}"
                    "Aiden texts me again while I'm drying my fur, making plans for us all to meet for breakfast, before embarking on the test journey, whatever that will be."
                    "Apparently we are all supposed to be present at 9AM in the town square."
                    "Weird place to start a test."
                    play music "audio/dream.ogg" fadein 3.0 volume 0.3
                    scene tatesleepblur with longdissolve
                    "To my surprise, Tate does not wear the pejamas I was expecting."
                    t "I figured if we'll be...cuddling on the same bed, it's going to be too warm for those."
                    "All I do is smile and nod in agreement, while walking towards the bed, inviting Tate to join me."

                    "The worries of the world disappear as the cat wraps his arms around me under the blanket."
                    t "Hey, just to make sure, we're really going to sleep, right?"
                    t "Like...you'll not expect me to grind on you or anything?"
                    t "Because I'm tired...really tired."
                    y nakedsmug"Heh, no worries, I said those things in the heat of the moment."
                    y nakedsimple"Wait...you on me?"
                    t "Obviously, I have to be the one on top, I'm wearing the pants in this relationship."
                    y nakedpf"I'm taller than you."
                    t "I'm stronger than you."
                    y nakedbored"{i}*sigh*{/i}"
                    y "Can we not talk about this kind of stuff when we're trying to sleep?"
                    t "Why? I'm making you hard already?"
                    y nakedsimple"Yes."
                    t "Oh. Okay then, I'll save my super effective flirt lines for another day."
                    t "You know..."
                    t "It's a shame they're wasting an entire room."
                    y nakedsimple"Who?"
                    t "The academy, they gave me an entire room for myself, even if I'll stay here the whole time, with you."
                    y nakedsmug"At least your stuffed animals will have room to breathe."
                    t "If they get kidnapped in the middle of the night, I'll blame you."
                    y "Hey, you're free to go sleep with them if you're so worried."
                    "He hugs me tighter and closes his eyes."
                    t "{i}*Snoooore*{/i}"
                    y "Sleep tight, little troublemaker."
                    t "{size=20}Good night.{/size}"
                    scene tatesleep with llongdissolve
                    scene CGc44
                    "The moons are shining through the rain filled clouds, heavy drops hit the window in the otherwise complete silence."
                    "Silence, save for the cat's light, gentle snores."
                    "He sure falls asleep fast."
                    "It is my turn to do the same, but unlike him, whose worries disappeared after our adventure, mine are just starting."
                    "I'm not as talented as him, not as familiar with Nigthfallen, or nature, not as good with people or magic."
                    "For him, and all the amazing people around me, tomorrow's test is nothing...but for me? Could mean the end of my time here."
                    "At this point, graduating isn't as important as being close to my beloved cat."
                    "I'll do anything to stay close to him, and warm his nights from the winter's winds..."
                    "At last, the worries turn to determination, and together with the cat's purrs on my chest, I calm my nerves enough to slip away in the dark."
                    stop music fadeout 2.0


                    scene black with longdissolve




                un "..." with longdissolve
                play sound "audio/button.ogg"
                un "Hey."
                play sound "audio/button.ogg"
                un simple"Are you asleep?"
                play sound "audio/button.ogg"
                un "Hey, [name]."
                play sound "audio/button.ogg"
                "..."
                play sound "audio/button.ogg"
                un bored"I'll hope that's a yes."
                play sound "audio/button.ogg"
                un ang"If you're pretending, I'm going to kill you."
                play sound "audio/button.ogg"
                un squint"Because you don't matter to me one bit, I'd murder you with no hesitation, got it?"
                play sound "audio/button.ogg"
                un bored"..."
                play sound "audio/button.ogg"
                un "Ok, you're asleep."
                play sound "audio/button.ogg"

                un simple"Still, let me get further inside your mind."
                play sound "audio/button.ogg"
                un curious"Uhmm, maybe a little further."
                play sound "audio/button.ogg"
                un suspicious"Juuust a little more."
                play sound "audio/button.ogg"
                un simple"Alright, here it goes."
                play sound "audio/button.ogg"
                play music "audio/wisp.ogg" fadein 2.0 volume 0.3
                un pride"{i}*Inhale*{/i}"
                play sound "audio/wack2.ogg"
                un cry"{size=70}BWWAAAAAAAARGH!{/size}"
                un "{i}*sniff*{/i} Guh-huh-huh...{i}*sniff sniff*{/i}"
                un "I really...{i}*sniff*{/i} thought you were d-done for good back there."
                un "I-I {i}*sniff*{/i} I don't want to {i}*snuff*{/i} be alone again."
                un "{i}*sniff*{/i}"
                un "Alright, calm down, you let it all out, now go back to your spiteful state."
                un "Your best state."
                un sad"Let's get something to keep my mind off this trauma."
                un suspicious"Hmmm."
                un simple"Oh, right, if he's asleep, shouldn't he be dreaming?"
                un "I still don't know if he saw the previous dreams, or if they're just for me, but I have to admit..."
                un "They were pretty entertaining."
                un "Especially after I found out they were technically real."
                un "So please continue dreaming."
                un "I'd hate to be left on a cliffhanger."
                stop music fadeout 2.0

                un "It's rare that somebody continues the dream they left off from two nights in a row."


                un sidee"Helloooo?"
                play music "audio/blizzard.ogg" volume 0.2

                un "When do you start, dream?"
                un "I wanna know what happened to the kid!"
                scene snowdreambg with llongdissolve
                un simple"Oh, there we go!"
                scene snow5 with llongdissolve
                scene CGc51
                un pride"{i}*cough cough*{/i}"
                un "The mysterious, large eared figure from before, catches the dying child, and with the little strength and body heat he has left, carries him to town."
                un bored"Nobody knows what happened to him after."
                un "It is a question that we will not know the answer to until the next dream."
                stop music fadeout 2.0


                kid "I think you know very well what happened next."
                play music "audio/firstday.ogg" fadein 2.0 volume 0.3

                un simple"Huh?"
                scene babytate with longdissolve
                scene CGc52

                un simple"Oh, hi."
                un "Are you talking to me?"
                "The little kid nods."
                un "Interesting."
                un bored"Perhaps you're right, but I'd rather find out from the source, not make up my own ending."
                un sad"What you know can sometimes prove to be deceiving, you know?"

                kid "The little cat was saved that night, and given a kind and generous family."
                un bored"Ooor you could just tell me."
                kid "He grew up to be blessed with magic, and loved by all, yet, misunderstood."
                kid "He always thought the world was against him, when in reality, he was just a shelfish dum-dum."
                un suspicious"Hey, language!"
                kid "Heehee."
                kid "He is now happy again, and I'm happy too, that is all that matters."
                kid "He started off with nobody, and was given the world."
                un simple"And that kid is you?"
                kid "I don't know, I don't remember."
                kid "It's what mister Sebil always told me."
                kid "I have to go, my new playmate is coming over."
                kid "He's a tiger like me! Rawr! I bet we'll be best friends!"
                un bored"You're not a...never mind, you go, tiger."
                stop music fadeout 2.0
                scene black with llongdissolve

                "The kid's image starts to fade, leaving behind the familiar darkness."
                "Except that this time, instead of winter cold, everything around is warm and...soft."




                un sidee"I did not expect to interact with his dreams."
                un "This was interesting."
                un "..."
                scene black
                if catkiss>=1:
                    play music "audio/nightsounds.ogg" volume 0.6
                    "{i}That same night...{/i}" with longdissolve
                    scene tentnight with llongdissolve

                    play sound "audio/celtic1.ogg" volume 0.3
                    show eureka at left
                    show ragnar simple at right
                    with dissolve
                    ra "How is he?"
                    ra "Will he be alright?"
                    eu "The scouts said they saw them both on a hill... and they're also quite sure, that they are now more than just friends."
                    eu "In other words, they're in perfect health."
                    show ragnar sadsmile at right
                    ra "That's good to hear..."
                    show ragnar sad at right
                    show eureka sadsmile at left
                    eu "Can you believe we actually did it at last?"
                    eu "The Chief is no more."
                    eu "Finally, no more meaningless sacrifices, no more {i}'hunters hunting'{/i}... no more lost tribemates."
                    ra "..."
                    eu "What's wrong? I thought you'd be the happiest of them all."
                    eu "You dreamed of being Chief for so long."
                    ra "Yeah...but-"
                    eu "Ah, I get it, he was your father to the end, even if his mind wasn't fully there, I still remember my-"
                    ra "N-no no, I'm not emotional over him all of a sudden, not a chance."
                    ra "The whole time I was away from the tribe, you and our friends were the only ones I was thinking about."
                    ra "That is, whenever I wasn't plotting that old man's downfall."
                    ra "That new magic of his came in clutch, it was shocking to say the least, when he beat me in a duel by removing my own little magic I had, all those years ago."
                    ra "Then I just ran away like a cub... not knowing what to do next."
                    ra "Now..."
                    eu "It's [name], isn't it?"
                    eu "He's been on your mind."
                    ra "..."
                    eu "But the plan worked, there's nothing to be sad about, your brother saved him like you said he would."
                    eu "From the beginning, since we planted the wyvern egg for him to find, to the kidnapping to the convincing, everything worked out fine!"

                    eu "Because of you, our great leader."
                    ra "He escaped... barely."
                    eu "That's because [name] was a late addition to the plan."
                    ra "I was supposeed to be there and help them at the ceremony."
                    ra "Instead, I closed my eyes and covered my ears, pretending like nothing was happening."
                    ra "Now my brother must hate me... us... hate us all."
                    ra "It was a perfect plan until I almost blew it."
                    eu "But you didn't."
                    ra "Do you think he'd want to ever see my wretched face again?"
                    eu "I'm sure he'll forgive us one day."
                    eu "We're still alive, aren't we?"
                    eu "No hunters came for us, no scout reported any suspicious activity."
                    eu "It seems like beside a little bad blood between brothers... we won the hight end of the stick."
                    show eureka ec at left
                    eu "So cheer up, Chief."
                    eu "We have a celebration to prepare."
                    eu "A {b}real{/b} celebration."
                    ra "..."
                    show ragnar sadsmile at right
                    ra "You're right."
                    ra "As long as our tribemates accepted me and forgave my past, that is all that matters for now."
                    show ragnar at right
                    ra "I'll worry about everything else some other time."
                    ra "I'll have time for that, especially now that hunting and fishing are our biggest priority, instead of surviving."
                    eu "That's the spirit."
                    show eureka sadsmile at left
                    eu "Although...a small decision still awaits you before the troubles can go away."
                    show ragnar simple at right
                    ra "And what would that- oh"
                    ra "Right."
                    ra "They didn't take the wyvern back, as I was hoping."
                    eu "They knew it isn't a dragon pretty early on."
                    show ragnar at right
                    ra "As expected of my brother and his partner."
                    ra "I suppose the most fair thing to do is let his own kind decide his fate."
                    ra "Tell the lizard to take him far into the forest tomorrow morning."
                    ra "There he can do whatever he wants with it."
                    ra "We can't, unfortunately, just keep a wyvern among us, the most dangerous of the Savage Furs."
                    eu "Do you think he'll come back?"
                    ra "The lizard?"

                    ra "Why wouldn't he?"
                    ra "His life was already far better than the average Savage Fur when my father was in charge, now it will be paradise."
                    eu "Why is that?"
                    show ragnar smug at right
                    show eureka blush2 at left
                    ra "Oh please, I know both you and Ruth have a soft spot for him."
                    eu "Wha- Well I- I don't- {size=20}wouldn't put it like that{/size}."
                    show ragnar at right
                    ra "Ha, it's quite alright, I know pity is a strong drug for kindhearted people."
                    ra "And you two are the kindest of them all."
                    show eureka sadsmile at left
                    eu "..."
                    eu "I'm glad you're here, Chief."
                    scene black with llongdissolve
                    ra "It's good to breath free at last." with dissolve





                    jump goodending
                else:
                    jump neutralending
                #(alarm clock)
