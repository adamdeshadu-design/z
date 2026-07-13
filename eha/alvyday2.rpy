
label alvyday2:
    if persistent.alvy:
        menu:
            "Looks like you already completed day 2 of Alvy's route as well, jump to day 3?"
            "Yes. (The Latest Update)":
                jump alvyday3
            "No. (Continue with Day 2)":
                pass
    else:
        pass
stop music
scene hotelroom3 with dissolve
y nakedsurprised"The bed is… what?"
play sound "audio/falling.ogg"
scene hotelroom0 with hpunch
q "Sleep quickly vanishes from your eyes when the situation clears in your mind."
scene hotelroom0 with dissolve:
    blur 10
play music "audio/naruto.ogg"
q "Throwing away the barely hanging blanket from your feet, you jump and look around."
q "A light migraine stops you, followed closely by a calf cramp."
y nakedhurt2 "Ow, ow, ow! God, Fucking. Damn it."
stop music fadeout 2.0
y "Why now?"
un bored"It seems you slept too deeply and tightly, your body is in a bit of a shock, as well as your mind."
play music "audio/catjazz.ogg"
un simple"You really care that much about him, huh?"
y nakedsimple"I… I don’t know."
y nakedsad"Am I overreacting?"
un "That depends, what are you thinking so negatively about?"
y "You know what…"
un bored"I do, but it helps to say it out loud. You’ll think more clearly of a solution that way."
y "… I think-"
y "Alvy might’ve realized I’m part of the people he wants to avoid, a weirdo, and simply left."
un "Is that something plausible to you now?"
y nakedsimple"Saying it out loud-"
y nakedss"Heh, no, I do believe he would at least take the courtesy to say goodbye in person."
un curious"Great! So the panic is for noth- uhmm, why is your heart rate accelerating…?"
stop music
play music "audio/naruto.ogg"
y nakedscared4"That just means HE MUST’VE GOTTEN KIDNAPPED!"
un bored"Oh no."
y "YOU SAW THE DREAM, DIDN’T YOU?!"
q "You hastily put on your pants and shirt."
un squint"Yeah but that doesn’t-"
q "Your tie is crooked- I mean-"
un bored"Your tie is crooked… {i}*sigh*{/i} This narrator thing is hard when I also have to calm down a lunatic."
y angry"I AM PERFECTLY REASONABLE AS ALWAYS!"
y "HIS CRAZY PSYCHO FAMILY MUST’VE DONE SOMETHING!"

y "I HAVE MORE THAN ENOUGH CLUES THAT LEADS ME TO BELIEVE THAT ALVY-{w=1.0}{nw}"
stop music
play sound "audio/doorsmash.ogg"


show alvy sur zorder 1
show breakfast zorder 2
with hpunch
play sound "audio/scratch2.ogg"
q "You open the door to a surprised and scared dog, who almost spills the contents of his tray when you bump into him."
y worried"ALVY!"
play music "audio/steadybeat.ogg"
al "Y-yes, that’s me, good morning."
show alvy simple
al "Where are you going in such a hurry?"
y "After you! I thought…"
y sadsmile"Agh, never mind, it was silly."
show alvy sad
al "Did you think I ditched you by any chance?"
y sad"Well, when I woke up with nobody around and your belongings missing… what was I supposed to think?"
al "I’m sorry, I should’ve left a note, but I was afraid the buffet was going to close."
y simple"The buffet?"
show alvy sadsmile
al "Yes, for breakfast."
q "As you calm down more and more you notice the large tray of breakfast items he’s carrying."
al "I read yesterday in that pamphlet that they only serve it until 8 AM, so I wanted to grab some things for us before then."
show alvy shy
al "You were sleeping so soundly that I… just didn’t want to wake you."
al "We’ll need the energy for the auditions. I’m not sure how difficult they will be."


y sadsmile"That is very nice of you. I am actually starving, now that I think about it."
show alvy ec at left
show breakfast at left
with ease
pause 1.0
show alvy ec at right
show breakfast at right
with ease

q "The dog wags his tail and moves around excitedly with the tray of food, back and forth, looking from one night stand to the other then back to you."
show alvy sad at center
show breakfast at center
with ease

al "Uhmm, where should I-"
y s"Just put it on the floor."
show alvy shy
al "Right… the floor."
y "The food won’t touch the ground man, it’s fine."
y "Have you never eaten anything that’s not on a table?"
al "Breakfast in bed was a thing for me. Other than that-"
show alvy sadsmile
al "It’s fine! You’re right, the floor is just fine."

y "Besides, don’t you like new experiences?"
q "You sit down criss-crossed and invite the dog with a patting gesture."
hide breakfast with moveoutbottom
q "He places the tray down carefully and gets closer to you, on his knees."
show alvy smile
al "I made sure to get plenty of protein, some carbs, fruits and vegetables and something to wash it all down with."
al "Oh, and some dessert."
al "I never had dessert for breakfast, but I heard people like it."
show alvy shy
y pf"Have you never had pancakes or waffles drenched in syrup?"
q "You ask while creating a makeshift sandwich from the eggs, bacon, toast, and vegetables."
al "Not for breakfast, that would be a brunch meal at least."
y sadsmile"Not even some French toast with powdered sugar and fruit?"
al "The French toast I had was always savory."
show alvy ec
al "But there’s nothing to stop me now, I suppose."
hide alvy ec with moveoutbottom

q "The two beasts ravage the meal tray for the next couple of minutes in silence. The need for sustenance is greater than the need to communicate, and your friend is definitely not a full mouth talker kind of guy."
q "The food is just above average; the eggs are cooked well, seasoned with some salt and garnished with green onion, the bacon had crispy and chewy pieces, the bread was somewhat fresh, but the juice was definitely watered down."
show alvy eat with moveinbottom
y bored"I give it a 6/10."
al "Really? I’d say 7."
y "That’s just because of the croissant, isn’t it?"
al "It is extremely well made."
y "I doubt they made it in-house."
al "Hey, it’s in my mouth, that’s what matters. You can only dream of getting them this buttery in any other hotel."
y s"Hah, I won’t argue with that."
y simple"… uhm."
y "Speaking of dreams…"

show alvy sad


Y "What have you… seen in my dream last night? If I may ask?"
q "His ears drop slightly, and after swallowing his bite responds:"
al "Nothing unfortunately, sorry."

al "The dream aspect of the hotel didn’t work last night apparently, so they said."
show alvy simple
al "Something about a blocked air vent that didn’t let the fumes get in."
al "We only smelled the perfume and nothing more."
show alvy smile
al "I forgot to mention it before, but good news! I got some of my money back because of it!"
y surprised"Then how-"
show alvy sadsmile
al "Shame, I was really looking forward to seeing what those weird dreams of yours are like."
y simple"Yeah… a shame."
show alvy blush
al "I was… even more excited for you to see mine."
y confused"Why’s that?"
al "I had some questions."
show alvy sad
al "I never mentioned them to anyone in fear they’ll think there’s something wrong with me, but I doubt you’d judge me."
y smug"Because I’m weird?"
al "Because you’re a great guy."
y blush"Oh… thanks, you’re right, I wouldn’t judge."
show alvy simple
al "It’s a small chance, but did you have any dreams perhaps? Despite everything?"
al "Even without the gas?"
q "He looks at you with hopeful eyes leaning forward."
y simple"Just my… usual, dark one, nothing too special."
show alvy sad2
q "Disappointment is a strong word, but the dog definitely felt the reality set in."
al "Yeah, I knew it."
y "If I may ask, what were you hoping for me to see?"
al "It’s… complicated. That’s the whole reason I wanted you to experience it. I don’t have an explanation myself."
al "It’s not some kind of supernatural phenomenon or anything, the words and the reasons are kind of stuck in my throat."
q "A wave of guilt washes over you. You know damn well you did have a dream, a short, yet informational dream about your friend, but is it wise to tell him?"
q "Especially when he didn’t have the chance to see yours. For now, you decide to try and piece together the puzzle some more before revealing the full picture."
show alvy simple
y s"If you’re up for it, we could try it again sometime."

al "Share dreams?"
y ec"Yeah! Who says this has to be our only opportunity?"
show alvy blush
al "I’d… like that."

q "You finish the rest of the food in silence, commenting on the taste to break the awkwardness from time to time."
scene black with dissolve
q "With a satisfying sigh, you pat your belly and gawkily sit up to clean your hands in the bathroom’s sink."
scene hotelroom0 with dissolve
y simple"What should we do with the tray?"
al "I believe it counts as room service, someone will probably come to get it if we just leave it on the nightstand."
q"He checks out his backpack and rearranges things inside it carefully."
y bored"You could’ve left your backpack here while getting food, you know?"
q "He stops, expressionless for a moment before continuing his rummaging."
q "It was a trick statement coming from you, a bid to see his reaction."
q "He lets out a soft smile, the curve of his lips almost unnoticeable."
al "I know."
q "And that’s where he leaves it."
q "That short response still makes your heart accelerate for some reason."
show alvy with moveinbottom
show twogems

q "From his backpack he retrieves two small gems without a glow. Almost looking like shards of a broken beer bottle, unimpressive."

al "Do you want help with your luggage?"
y surprised"Oh, almost forgot about those."
un eyeroll"Again…?"
y sadsmile"They are pretty heavy, but I would feel bad making you carry anything."
show alvy sadsmile
al "We can just place them inside these gems."
y surprised"Is that what those are? Object summoning gems?"
al "Yes, they’re very small, but I believe two bags should fit."
al "Here, you can have them."
hide twogems with moveoutbottom
q "He takes your hand and casually places them in your palm."
y worried"J-just like that? But I thought gems-"
al "They don’t have Nightfallen inside them. I don’t care for regular gems all that much."
show alvy ec
al "You can put your things in them and we can go."
al "Before they come kick us out that is. We should free the room before 10 AM."
y awkward"Uhmm, yeah, sure… I’ll just… put my luggage in these."
q "You try to visualize the largest bag and imagine it entering the gem, and with some grunts of pain and hand motions later-"
show alvy simple
al "Do you not know how?"
y sad"{i}*sigh*{/i} No, what gave it away?"
al "You’re supposed to touch the object with the gem, for starters."
q "You do it all again, but this time follow the simple instruction he just gave you… and-"
show glow with dissolve
pause 1.0
hide glow with dissolve
y simple"It worked."
q "Your voice trailed behind with a severe lack of excitement, and the dog sensed that much."
show alvy awk
al "I-it’s alright! You don’t need to know every detail and secret of summoning so early! It took me a long time to find things out by myself!"
y simple"How long?"
al "A… a couple of weeks?"
y simple"Ah."
show alvy simple
al "Ok, days…"
y bored"ah."
show alvy shy
al "Miiight have been hours or minutes-"
y sleepy"ah."
show alvy awk
al "BUT I WAS DESPERATE!"
al "And had two amazing teachers."
al "I have no idea how to survive in the real world, you aren’t very experienced at summoning, so we’ll help each other out! Right?"
show alvy sadsmile
al "That’s what this whole… relationship is all about."
y simple"Yeah…"
y ec"Yeah, of course, that’s a good compromise."
y smug"We should go check out before we stall with yet another topic of conversation."
hide alvy sadsmile with moveoutright
scene hotelhall with dissolve
show dormdoor with dissolve
show alvy smug with moveinright
al "Good point, I was just about to ask about your Political Analysis of Arcanvale’s and Lordana’s international relations."
y "Yup, we should hurry before I scare you away with my political views, come on."
show alvy ec
al "Are you not even going to comment on Icatha’s immigration problem?"
y bored"Just shoot me in the face."
show alvy smug
stop music fadeout 2.0
al "I am a bit intrigued now."
y smug"Later perhaps I’d be up for debate, over a can of soda and a headache pill."
al "Alright, keep your secrets, but for now-"
show alvy ec
play music "audio/montage3.ogg" volume 0.6
al "Race you downstairs then!{w=1.0}{nw}"
                    
hide alvy ec with moveoutleft


y awkward"H-hey now, That’s not fair, I have to lock the-"
q "He’s already zooming down the stairs."
hide dormdoor
play sound "audio/doorhit.mp3"
y angry"OH YOU SON OF A- "
scene hotelhall with hpunch
q "After a second of struggling with the key card, the door locks and you take off after the cheery dog, determined not to lose to the only person in this town that seems slightly less athletic than you."
scene hotelstairs with hpunch:
    blur 15

q "You charge to catch up, almost tripping on the carpeted floor before jumping over the railing. You contemplated using an enchantment, but it wouldn’t be fair."
y pf"Even if it should be with his illegal head start."
show alvy sur with moveinright
stop music fadeout 3.0
q "You’re met with a surprise when you have to press hard on the brakes, lest you crash into your friend running back up the stairs towards you, with a worried expression."
play music "audio/fivesteprhythm.ogg" volume 0.4
y surprised"Hey, where are you going?"
y bored"Did you finally realize you ran off too early-"
show alvy sur at left with move
play music "audio/wind.ogg" volume 0.4
al "No, back! Back! Go back up!"
y worried"W-why, what’s going on?"
show alvy sur at center with move
al "{size=*0.6}They’re here.{/size}"
y simple"They?"
q "The dog is almost whispering, signaling for you to do the same."
al "{size=*0.6}The other recommended students! They’re talking to the receptionist.{/size}"
y "{size=*0.6}Let me see.{/size}"
al "{size=*0.6}Careful, don’t be too obvious.{/size}"
hide alvy sur with dissolve
scene black with llongdissolve
show dormdoor zorder 2
show hotelcr zorder 1
with llongdissolve
q "You walk to the bottom of the stairs and peek beyond the corner."
y simple"{size=*0.6}Indeed, that’s Coal and Rose.{/size}"
q "The large rabbit lady is doing the talking, showing the other person something on her phone, while the panther is enjoying some of the free snacks from the desks with his eyes closed."
scene hotelstairs with dissolve:
    blur 15
show alvy simple
y simple"{size=*0.6}Shouldn’t we at least say hi?{/size}"
show alvy sad
al "{size=*0.6}N-no… I don’t want to.{/size}"
y confused"{size=*0.6}Well that’s rude.{/size}"
y "{size=*0.6}I met them already and they’re nice.{/size}"

al "{size=*0.6}Tell me, why do you think they’re here?{/size}"
y s"{size=*0.6}We could ask them.{/size}"
show alvy plead
al "{size=*0.6}No, it’s because they know we’re also here, please, [name], I can’t deal with these kinds of situations.{/size}"
al "{size=*0.6}Please, let’s just go, and be alone again...{/size}"

menu:
    "Stay with Alvy and avoid them.":
        $ alvy_points+=1
        jump nocoalrose
    "Go meet them alone, then meet the dog in the back.":
        y sadsmile"{size=*0.6}Alright, look.{/size}"
        y "{size=*0.6}I’ll go there myself and greet them and see what they’re doing here.{/size}"
        al "{size=*0.6}But I-{/size}"
        y smug"{size=*0.6}And I won’t even mention anything about you, ‘I haven’t seen you since yesterday and have no idea where you are’.{/size}"
        y s"{size=*0.6}Then I’ll meet you in the back, deal?{/size}"
        show alvy simple
        al "…"
        show alvy sad
        al "{size=*0.6}Fine{/size}."
        al "{size=*0.6}Please don’t be long.{/size}"
        y ec"{size=*0.6}Be there in five.{/size}"
        stop music fadeout 2.0
        hide alvy sad with moveoutleft
        q "You give your friend a ten second start to go back, then make your entrance."
        scene hotelcr with dissolve
        scene CGal7
        play music "audio/purplecat.ogg"
        y s"Hey Rose! Coal!"
        r "Oh! Hi [name], what a surprise."
        co "Hey man, is the other recommended student here too by any chance?"
        y smug"Nah, I’m here alone."
        y sadsmile"Uhm, why would you assume he’s here?"
        y awkward"Seems kinda random, haha."
        co "It would be more random if you were here by yourself, this is a dream and love hotel, after all."
        r "And perhaps the same way Coal and I stuck together since yesterday, maybe you two did the same."
        y pf"That… makes a lot of sense, but no, I still haven’t seen him."
        y "I’m not some kind of weird guy who does random, non-logical things for fun."
        y "I obviously came here with…"


        menu:
            "Who did I {i}‘come’{/i} here with…?"
            "Aiden":
                y sadsmile"You know, yesterday I met Aiden and-"
                r "Oh, no need to say more."
                co "On the contrary, please say as much as possible."
                co "He’s quite the charmer, isn’t he?"
                co "I almost got persuaded as well, if it weren’t for all the other people we need to meet."
                r "I had to basically drag you out of his claws yesterday evening."
                co "I’m sure he was just playing, we met him later as well and he didn’t seem interested in the slightest anymore."
                r "Probably because he found another target already."
                q "She says squinting at you playfully."
                y simple"Didn’t know he was such a player."
                y "Anyway, I’m never meeting with him again, so…"
                co"Aww, did he break your heart? I promise I’m not jealous if anything-"
                y awkward"No! No, no, it’s, uhmm, it’s complicated, he’s complicated, I don’t have time for complications."
                jump byecoalrose
            "Dallan":
                y smug"Yeah I was with a certain wolf that caught my eye yesterday. Oh man those muscles"
                r "I got some of those!"
                q "She flexes her arms playfully."
                y sal"Indeed…"
                co "{size=*0.5}You’re salivating.{/size}"
                y awkward"Sorry!"
                r "That was flattering actually."
                r"And about Dallan, he’s not present with you right now?"
                co "He doesn’t seem the type to leave early from a night of passion."
                y awkward"Y-yeah he had to leave this time cause uhm…work stuff."
                r "I really needed to talk to him."
                r "Can’t believe you got him all to yourself for so long so quickly."
                r "If only I was {i}un petite chat{/i} as well, could charm him into a round of training."
                y simple"I don’t speak French."
                jump byecoalrose
            "Tate":
    
                y ec"Actually, I was here with Tate!"
                r "Oh, he did seem interested in you, got freaky so soon, ey?"
                y pf"Actually he just showed me photos of his stuffed animals and trauma dumped on me, then fell asleep."
                r "That…uhm,  I can’t verify if that’s in character, Coal?"
                co "Was the cat on our radar too?"

                r "Eh, doesn’t matter, he’s not with you now?"
                y simple"he uh… just disappeared, teleported."
                co "I did hear he likes to do that, I know that much."
                jump byecoalrose
            "Therium":
                y s"Oh I uh, hung out with Therium here last night, he had to get going, y'know, vice leader stuff"
                r "He did seem very interested in you."
                co "Surprising, since he doesn’t seem to give a damn about us."
                co "Doesn’t he want more recommended students in his shard?"
                r "He probably knows our magic isn’t that great."
                r "Is it true by the way, what they say, [name]?"
                y confused"What?"
                r "You know, a horse’s size~"
                y pf"{i}Uhmmmmmmmmmmmmmmmmmmmmmmmmmm-{/i} sure."
                co "Heh, nice."

                jump byecoalrose
            "The Headmaster":
                y ec"I was… actually here to meet Headmaster Argus! I forgot my luggage at the Academy and he brought it to me. He also needed to talk about stuff, and you know, it was very late and we decided to get a room."
                y s"That seems plausible, right?"
                r "I swear I heard that plot in a drama show when I was visiting my sister-"
                co "They don’t call him the {i}Head Master{/i} for nothing."
                y bored"Wipe that smirk off your face, it wasn’t funny."
                r "Yes… wipe it like… [name] wiped lion cum from his fur?"
                r "How was that?"
                co "Good one, you’re learning."
                q "The idiots high five each other, and now you have to live with the knowledge that they believe the headmaster fucked your face the other night."
                y bored"..."
                "Scribbles, kill them."
                un bored"I would, usually, but even I can tell you’re not being serious."
                jump byecoalrose
            "Alone":
                y ec"Yeah, I was here with me, myself and I, they’re the best people I know, you should meet them sometime."
                r "I know you’re joking, but that still sounded so very sad."
                co "We could spend time with you, [name], if you’re that lonely."
                y surprised"NO!"
                y awkward"I mean- it’s very nice of you, but I’m not a reject or anything… I was just curious about this place and didn’t want to make it weird by bringing a friend, you know?"
                y sadsmile"They have these dream fumes that do… things."
                co "Oh, I heard about that! Rose, we should share dreams sometime."
                r "Y’all can’t handle my dreams."
                y simple"..."
                y "Damn."
                co "...dark stuff."
                jump byecoalrose

label byecoalrose:
y s"Doesn’t matter, I’m just here to leave my key, if you don’t mind, then I’ll be on my way."
de "Thank you very much, and would your partner want his loyalty points."
q"You give the receptionist a nasty look through squinted eyes, like she didn’t just hear you struggling to maintain a lie."
st "{size=*0.5}It’s strict policy to ask… sorry.{/size}"
co"So you DO have someone here at least, we know that much guaranteed."
r "On your first night here? That might be a record."
y simple"Aren’t you here for the same thing?"
co "We were here to meet a friend mostly."
co "Out of town people usually stay at hotels, you know?"
r "Students not so much."
y smug"So true bestie."
y "Anyway, I gotta go… Would love to talk, but I gotta prepare for the auditions, and stuff."
co "Of course!"
r "Mind if we tag along?"
co "I also need some audition practice, even if mine will be different from yours."
q "Another obstacle, quick, you must think of something."
y pf"Ffffff… noooo, no."
co "No?"
y "Nooo…"
r "Just straight up? No… no extra excuses?"
un sidee"Huh, a choice isn’t necessary I suppose."
q "You squint your eyes and walk backwards towards the exit door, not breaking eye contact and whispering continuous no’s until the automatic doors close and they’re out of view."
scene black with dissolve
stop music fadeout 2.0
q "Safe to say they were a bit stunned, but not offended, just confused."
play sound "audio/button2.ogg"
r "{size=*0.5}What’s a bestie…?{/size}" 
play sound "audio/button2.ogg"
co "{i}*shrug*{/i}"
scene alley with dissolve
q "You did it! You defused the situation with your weirdness!"
play music "audio/onenine.ogg"
y s"Now to find my other weirdo friend."
y bored"The things I do for him…"

q "Behind the hotel, in the alleyway full of familiar garbage cans, silence reigned."
q "No dog in sight or any other fur."
y sadsmile"Uhm, Alvy? Are you hiding in a dumpster by any chance?"
y simple"I know you wanted to hide but this seems a bit extre-"
al "I’m here.{w=0.5}{nw}" 
play sound "audio/surprise.ogg"

y scream"AGH!" with hpunch
show alvy simple
q "He suddenly appears from behind."
"Yes I fucking know that now, thanks."
y worried"God, how did you do that?"
y "Can you teleport or something?"
show alvy shy
al "I told you I don’t know any spells."
al "My friend is keeping me hidden whenever I need."
y pf"Right… you mentioned that."
show alvy sad
al "How did it go?"
y ec"Great! Found out what they were there for, dream sharing, and they have no idea you were here too."
y simple"I think I might’ve freaked them out a little as well…"
al "Good, that means they’ll leave us alone."

jump byecoalrose2


label nocoalrose:
stop music fadeout 2.0
y simple"Do we really need to sneak around this early in the morning…? Can’t we just-"
show alvy sad
play music "audio/wisp.ogg"
q "You sense the disappointment oozing from the dog’s body"
y  smug"But y'know what’s even worse? Socializing~"
show alvy ec
q "if there was a record for fastest turn of emotions from being dejected to happy puppy love, this dog’s got it"

al "Thank you."
y ec"The things I do for friends."
scene hotelhall with dissolve

q "As you stealthily make your way upstairs, you lock your eyes with a random marten walking down, who is preparing to greet you. You place a finger in front of your mouth before bolting upstairs."
q "That’s a neat way to make someone question everything around them for a while."

q "Nobody spots you making your way back to your hotel room aside from that nice young man. So everyone else was spared an awkward interaction. Once inside, you pace around the room and think about your next move"
scene hotelroom0 with dissolve
y simple"Sooo. The fire escapes?"
y simple"There should be one on every floor, unless it doesn’t follow the OSHA standards… which would be concerning."
y "And what do I do with the key?"
show alvy simple with moveinleft
al "Just leave it on the bed. The cleaning people will find it."
show alvy simple at left with ease
y "As long as we’re not banned for life, it’s not such a bad place."
play sound "audio/window.ogg"

show alvy ang at left 
al "Grrrr."
q "The dog seems upset after opening the window."
al "Fire escapes or not, shouldn’t there be a way to get out from every room in case of a fire? Where are the stairs?"
y simple"They probably have runes set to take care of any rogue fires appearing. It’s cheaper than stairs… considering those only save people not the property."
show alvy ang at center with move
show alvy sigh
al "I suppose we have no other choice then."
stop music fadeout 2.0
y pf"About socializing or jumping through the window?"
un ang"I think you know the answer to that one and I’m saying TALK SOME SENSE INTO HIM, DON’T FUCKING JUMP!"
y awkward"Uhmm, m-maybe, let’s think of something else, the backdoor is still an opt-"
play sound "audio/carpet.ogg"
q "A pair of steps can be heard down the hall, before a knock at the door."

show alvy ring with dissolve
y "Welp, might as well-"
play sound "audio/buildup.mp3"
q "In the meantime, the dog clutches the ring at his side with a determined look, then-"
al "Hold steady."
play music "audio/blizzard.ogg"
scene black with dissolve
play sound "audio/tension1.mp3"

show alvynightfallen with dissolve
y scream"AH!"
stop music fadeout 2.0
"..."
q "The world around you seems to warp weirdly as a large black figure grabs your arm forcefully."
scene black with hpunch
pause 0.5
scene alley with hpunch
play sound "audio/wind.ogg"
q "That is… as much as I can describe, before the room turns into the back alley of the hotel."
show alvy sur with moveinleft
q "The canine is shaking you, trying to get your attention. He seems really frightened and worried about what he just did, even though you’re more than fine."
y worried"We’re outside…"
al "Are you alright?!"
y surprised"That was…"
show alvy sad2 
al "I know, I know! I’m sorry, I shouldn’t summon inside the barrier, I promise I’m not trying to get us in trouble on purpose, but I panicked and, and-"
stop sound
play music "audio/catjazz.ogg"
y ec"Don’t be! I don’t blame you."
show alvy sur
y sadsmile"It was just… kind of incredible."
show alvy blush
q "The dog looks bewildered for a moment, before slightly blushing as he realized he was being complimented."
y "Yeah you shouldn’t do it, but… you did save us from… a social interaction."
y "I’m shivering just thinking about it."
al "You’re not mad?"
y s"No police around, so I think I’m good."
y pf"Still though… let’s not do that again, I’d rather like to avoid any more jail time for the rest of the semester"
show alvy sadsmile
al "You’re right, you’re right."
al "You really didn’t mind… the transportation method?"
y "Honestly? Better than teleporting."
y bored"I avoid those devices like the plague, too much light even with an eye cover."
y sadsmile"This was… unique."
y ec"I’d like to know more at some point."
al "Totally! But for now, let’s get away from here… from them."



label byecoalrose2:
show alvy shy

y bored"Yeah, thank goodness we got away from those absolute lunatics that were probably just going to say hi to you and introduce themselves."
show alvy ang
al "I’m sorry, ok?!"
show alvy sad
al "Are you making a mean joke or are you actually upset with me?"
al "I can’t really tell."
show alvy blush
y ec"Oh I would never be mad at you, you’re too sweet and pure."
al "Thanks? I guess?"
show alvy shy
y simple"But if you’re so determined to keep hiding, what are your plans now?"

al "I still have some money left, we could get another-"
show alvy simple
y bored"Nope. No more hotels, I’m already sick of them."
y "No idea how you survived months with them."
y simple"Are the dorms really such a bad option? I already miss mine and I haven’t even seen it yet."
y "Do you happen to have friends or relatives living here?"
show alvy conf
q "His ears perk up at the suggestion."
al "I do… in a way?"
y s"Really?!"
show alvy simple
y "That’s great! You can stay there then."
y smug"Problem solved, wasn’t that quick?"

al "Well-"
y bored"It’s not that easy, is it?"

al "Not even a little bit."

y simple"What is it now? Are they also some kind of overprotective snobs? No offense."
al "No, they don’t actually live there, is the problem."
y confused"Huh?"
al "Just come with me."
hide alvy simple with moveoutright
stop music fadeout 2.0

q "He grabs your hand and runs down the street without further explanation."
scene outside2 with dissolve
play sound "audio/footsteps.ogg" volume 0.2
play music "audio/forestsound.ogg"
y simple"You seem confident, do you know where that place is just like that?"
al "I’ve been contemplating this option a lot in the past couple of weeks, so I’ve visited a couple of times."
y s"Excited to see this super secret place then."
y "Is it far?"
al "Not too far."
al "If you remember the map, it’s just up ahead then down the street."


scene outside3 with dissolve

q "After a not so exciting trip through commercial streets, you arrive at the main residential area."
q "Less buildings obscure your view and more lush trees welcome you in."
q "You go past a grand metal gate, with a thick brick wall surrounding the estate, clearly someone rich lives there."

stop sound fadeout 2.0
y s"That must be it, right?"
al "Not quite."
stop music fadeout 2.0
q "He guides you just past that house, or mansion, to a secluded place at the edge of the academy, overlooking the main gate and the forest."
scene porch with longdissolve
play music "audio/steadybeat.ogg" fadein 3.0
q "A small, rusty gate and old, barely hanging fence protect an otherwise nice looking house."
al "This is it, we’re here."
y s"Sooo, who owns it?"
al "Nobody, it’s... mine, technically."
Y surprised"You have property in Lakonia?"
y pf"Wow. That is… not that surprising."
al "It belonged to my aunt before she became more involved with her career and Nightfallen activism."
al "Now it’s just rotting away."
al "She left it to me in her Will, she made sure to tell me that every time she visited."
al "She really wanted me to become a hunter..."
y simple"Why were you debating coming here? It seems perfect for your needs."
al "Multiple reasons."
al "Although my aunt still visits every couple of years, the place must be extremely filthy… I’m afraid to even step inside. Secondly, living alone is a bit of a scary concept, even if I don’t like other people."
al "Not to mention that if my family finds out my aunt has property in Lakonia, this would be the first place they’d search for me."
y "So they don’t know… about you."
show alvy bored with moveinleft
al "{i}*sigh*{/i}, come inside."
hide alvy bored with moveoutright

stop music  fadeout 2.0

scene black with llongdissolve
play sound "audio/creak.mp3"
q "The walk to the front door is met with creaks of wooden planks beneath your feet, and the door itself wasn’t any quieter."
q "The dog used a key he already had in his backpack, yet another precious thing he held in there and protected with his life all this time."
scene alvyhouse0 with longdissolve
play music "audio/dream.ogg" volume 0.6 fadein 3.0
q "The living room you’re greeted in is spacious and well illuminated, even if dust particles fly around and through the sun’s rays like a rave party."
q "You both take a second to step inside, look around and breathe in the aged, dusted aroma, if you can even call it that."
show alvy shy with moveinleft

al "It’s nicer than I expected."
y simple"What did you expect?"
al "Vandalism, broken windows, no furniture, maybe even some broken walls and ceilings."
y smug"Oh come on, the police have to resort to sex parties and watching TV dramas to get away from the boredom of a crime free town."
y "There is nobody interested in breaking into a home."
show alvy simple
al "Anything is possible, how can you just trust complete strangers?"
y s"You trust them and they trust you, that’s how it works."

y "Still, might not be a ruined home, but-"
q "You use your white finger to slide along the shoe cabinet in front of the door."
q "The white becomes grayish black from mere inches of sliding."
show alvy smile
al "Yup. Needs some things to become livable."
y s"Depending on your standards, it’s satisfactory right now."
show alvy sad
al "Poor plants, nobody was around to water them for some time."
y "Look at that, was your aunt an artist?"
show alvy simple
al "She enjoyed painting, I assume she made most of the pictures she has on the walls."
al "And writing, she would write me stories about Nightfallen and poems about the outside world."
y surprised"Oh. My. God."
show alvy sur
al "What?"
y sadsmile"Is that you as a kid?!"
show alvy blushsur
al "W-what? Where?!"
y "On the wall! You look so cute in that tiny suit and sprayed hair."
show alvy blush

al "It wasn’t really my style…"
y smug"I can see that, mister Layered Streetwear."
show alvy blushangry
al "Shut up… and stop looking at that."
y ec"But I really like it, everything about you is very balanced and visually pleasing."
show alvy blush
al "That’s an oddly satisfying compliment."
y s"It’s also nice of her to have this, I can tell she really likes you."
al "Yeah..."
al "Uhm, let’s check out the bedroom, see what the bed situation is."
hide alvy blush with moveoutleft
y "Right behind you! Should be on the second floor, since the only other room here looks to be the kitchen."
scene black with dissolve
q "The stairs are withholding the test of time better than you would’ve expected, with barely any sounds coming from under your feet while ascending."
q "The second floor is simple, a longer hallway that separates two bedrooms and a bathroom at the end."
scene alvybedroom0 with dissolve
q "You follow the dog into the first room, one with no door on its hinges."
y confused"Where did this one go?"
al "Perhaps thieves?"
y "It looks ripped off by force, but it doesn’t make sense for a person to break in to steal a door."
al "The inside isn’t looking any better…"
q "Unlike what you’ve seen until now, this is one of the rooms you’d both agree falls into the ‘unlivable’ category."
q "Aside from the dust, wooden planks are missing here and there, the bed has a mattress ripped to shreds and even broken shards on the floor from a once seemingly beautiful crystal vase."
y smug"Well. Who’s calling dibs on this one?"
q "The dog looks a bit worried and disappointed, but doesn’t express any opinions."
al "I hope the other one is luckier."
scene black with dissolve

q "The second room is… great, perfect even, one might say. A sigh of relief escapes the dog’s muzzle."
scene alvybedroom with dissolve
y ec"Would you look at that!"
show alvy shy with moveinleft
al "Aside from the dust, this is promising."
y "No smells, no broken furniture or decorations and the bed…"
al "The mattress was preserved pretty well by this simple cover."

y smug"So, my good socially awkward friend, are you ready to get cleaning and move in?"
q "You ask while rolling up your sleeves and doing a flexing motion with your nonexistent muscles."
"Hey…"
show alvy ec
q "Your friend thinks for a couple of moments longer, looks around some more and with each passing second his smile grows wider."
stop music fadeout 2.0
al "Yes! I think I am!"

scene black with llongdissolve
play music "audio/jazz20.ogg"
q "You let out a laugh, and sprint to open every remaining door in hopes of finding cleaning supplies."
scene alvyhouse0 with dissolve
show alvy smile with moveinleft
al "If nobody bothered to take out the furniture there should be stuff to clean with around here too."
al "What do we even need?"
y s"Lots of things: brooms, rags, soap, bleach, sponges, mops, buckets- doubt we’ll find a vacuum- but for starters I’d be happy with just… Aha!"
q "Opening a closet you find the first important tool."
show duster with moveinbottom
y determined"Dusters."
y "Getting the dust off high places is a priority."
hide duster with moveoutbottom
q "You shake and puff one of them up and hand another to the dog with a playful flourish."

y "‘Alright, partner! Let's turn this dust haven into something livable."
q "You sweep a dramatic arc across the shelf you took the tools from, sending up a cloud that makes you both cough."
y dust"{i}*cough*{/i} Yeah, should probably start slow."
al "What should I do?"
y determined"First off, the living room!"
y "Go take off the window covers and let some sunshine in, maybe even open them for some fresh air."
show alvy ec
y s"I saw a step ladder in the closet, I’ll bring it there, then we’ll clean on top of shelves and wooden beams."
hide alvy ec with moveoutleft

q "The dog’s smile widens as he runs off."
q "Soon, with purpose in mind and instruments in hand, these two fumbling twinks start the actual work."
al "Actually… I think I’ll take my jacket off. It’s kind of unique, I don't want to dirty it."
y s"Good idea, would love to do the same with my uniform… but I honestly don’t have anything I don’t mind ruining with me."
un suspicious"That feels like some kind of excuse to not change clothes… I wonder why that would be, hmmm."
show alvyclean3 with moveinleft
q "Going from furniture to furniture and ornament to ornament with the dusters, the dog slows down to take in the state of a creaky bookshelf, running his hand over the layers of dust."
q "He seems lost in thought."
al "I can’t even see the wood. She hasn’t been here in a long while.’"
y simple"Judging by those dead plants… I have to agree."
al "I wonder why…"
q "Feeling helpless at your unknowing silence, you decide to make light of it all."
y sadsmile"Hey, maybe she fell in love with cars and wanted to live somewhere they’re not banned."
q "He somewhat agrees with a shrug, though he clearly keeps a brave face."
y smug"Or…"
y smug"Maybe she considers this place yours already, and didn’t want to intrude."
al "That… that doesn’t sound too far fetched."
y pf"And since nobody’s around at least that means no one can judge our, uh, unique cleaning style."
q "You give a mock sweep, accidentally knocking a large spiderweb loose that falls on your face and sticks to your fur."

q "A repressed laugh can be heard, as you make a face at the dangling strands."
al "I suppose if anyone says the place is still filthy we can just respond with ‘you should’ve seen it before we started’."

q "With a roll of your eyes, you both continue earnestly. The dog attacks the dusty shelves, carefully pulling off old books and odd trinkets, while you start on the floor, sweeping years worth of debris into a manageable pile, including whatever he throws down."
q "You can’t help but steal a glance at the young dog’s movements."
q "You’re not sure how familiar he is with cleaning a house, but given that he’s such a fast learner he imitates your techniques quite well."
q "With a sort of elegant flair to him, as if afraid to dirty his fur or ruin his claws, but the determined expression tells well enough that he’s more than willing to."

q "It doesn’t take long for the air to be filled with the scent of freshly scrubbed wood and… whatever was still stuck in the carpets. Probably paint, let’s go with that, you try not to think too much about that."

q "Humming under his breath, he wipes down windows so grime-covered you’d forgotten they were actually clear."
al "I did think that taking off those window covers didn’t make much of a difference, but it was because of the dirt… now it’s much better."
q "He says with a pleased grin."

q "You stop to stretch for a moment, watching him go about with his newfound enthusiasm."
y ec"And the air is finally getting replaced, it feels better to breathe."
y smug"And look at you! Didn’t even know how to hang clothes and now you’re doing a better job than me at cleaning."
al "Not sure about that, but it’s easy to work on something you care about."
al "Sacrifices for the things you love."
y "Hope you have the energy for the final part."
al "The final part of… cleaning this room?"
y "Yup."
q "You confirm, throwing him a moist rag, freshly squeezed into the soapy bucket."
y ec"Couldn’t find any mops, so we’ll have to do it the old fashioned way."
y determined"Follow my lead!"
q "You press the rag on the floor near a wall and scrub intensely for a couple of feet, then position yourself with your feet against the wall and your hands on the rag."
q "With one heavy boost, you run forward, cleaning the floor in a sprinting motion. From one side of the room to the other in mere seconds."
q "The dog quickly does the same from the other side, and tries to keep up as much as possible."
y hurt3"How is it?"
al "It’s fun, but also the most draining thing I’ve ever done physically."
y "The good part is that it’s over fast!"
q "Bend down, sprint, rinse, squeeze, repeat. From side to side and room to room, the sweat drops remain proof of your hard work just behind the rags."
stop music fadeout 2.0
q "Bit by bit, the house starts to feel less like an ancient relic and more like a place with potential. By the time you’re both scrubbing the last few surfaces, you’re certainly worn out but laughing freely."
play music "audio/purplecat.ogg" fadein 3.0
scene alvyhouse0 with longdissolve
scene alvyhouse with pushleft

y lust"‘I’m not saying we’re pros or anything-"
q "You say borderline panting to death."
y smug"-but I think we could start a business.’"
al "Not even I, with my sheltered hands, am delusional enough to think we can do this on the regular."
al "But I’d be lying if I said I didn’t feel accomplished right now."
y s"It is indeed a warm feeling inside."

q "You both collapse on the cleanest patch of floor you can find, breathing in the faint smell of old wood and fresh polish, staring up at the ceiling with a sense of accomplishment and the beginning of a new, sweet home."
show alvy 2 tired with moveinleft
al "Warm on the inside… and the outside."
y smug"What was that? Couldn’t hear you over your dog panting."
al "You’re a cat and also panting, that’s almost worrying."
y bored"Then how about you go buy us some drinks?"
show alvy 2 simple
al "But we’re not done yet, the hardest part is still up…"
q "You both glare towards the bathroom’s direction."
y ec"I’ll start without you, but even so, we could also use some more scrubs."
show alvy 2 sadsmile
al "Alright, I’ll go, don’t overwork yourself."
y awkward"I can barely promise I’ll work at all."
y s"And get some energy drinks while you’re there too, please."
hide alvy 2 sadsmile with moveoutleft

q "With one last nod and chuckle he walks away and out the door."
scene black with llongdissolve
stop music fadeout 2.0
y s"Let's see what we're working with."

scene alvybath0 with llongdissolve
y simple"That’s not a pretty sight."
play music "audio/oddish00.ogg" fadein 2.0 volume 0.5
un simple"Could be worse."
un sidee"Sooo, the dog is gone for a while."

un "Strange, you didn’t seem to lie… but neither did you tell the truth? What’s that all about?"
y smug"Well, that’s because the bathroom will be clean when he gets back, but I won’t be the one cleaning it."
un simple"..."
un bored"I’m going to forcefully circumcise you now."
y scream"W-WHAT I MEANT TO SAY!- {i}Pwetty pwease{/i} just help me, I’m but a wittle baby!"
un suspicious"You do realize you’re already in my debt, right? You said so."
un "How far are you willing to go into the shark’s mouth before the teeth start being scary?"
y determined"I’d put my paws through fire for a friend."
un bored"...Seriously?"
y sadsmile"I know I might appear selfish sometimes, with all my worldly desires-"
un "Cock."
y pf"Among other things-"
y sad"But I do have an aching feeling in my chest whenever I disappoint someone I care about."
y "And I do care about Alvy, I’d suffer for his sake."
un sidee"There is one thing I could…"
un sad"Although it’s futile to even say because it’s more than just a favor, and I know it’s not happening, just some wishful thinking."
y sadsmile"Don’t you think it’s worth a try?"
y pf"I doubt you want me to, like, eat my own arm or something. I know you well enough for that at least, I hope."
un "I simply want you to give up."
y confused"Cleaning?"
un sidee"Yes? Well, no, give up on the dog in general, just… be by yourself, focus on your supposed career and our deal."
y worried"That… that is quite a big ask."
y sad"You were right, I’m sorry, that’s just not something I can do."
un sad"Yeah, I expected that."
y "I don’t want to go back to the loser I was… alone."
un simple"In that case I do have a favor to ask in exchange for my services."
y simple"What is it?"
un "Just don’t be mad at me for keeping secrets in the future, alright?"
y smug"Hah, well played sir, well played."
y "That is something I hate to agree to but it is a very fair request, so I agree."
un tease"Great! In that case, brace yourself, this is going to take much more magic out of you than cleaning a body."


un simple"Also, you need to narrate this part, I have to concentrate."
y ec"On it boss!"
scene alvybath0 with llongdissolve:
    blur 20
    
"As those words leave my mouth, dirt patches and still water disappear before my eyes like they were never there."
"Every part of the bathroom my eyes touch turns clear the next moment. Like seeing a magician’s trick without a smoke screen, makes me question my reality, especially when broken pieces of furniture repair themselves here and there."
scene alvybath with longdissolve
y s"Strange, it wasn’t as much magic as I thought, I feel fine!"
y ec"You are so awesome! The greatest Demon that’s ever lived!"

un bored"3."
y confused"What? There are three?"
un "2."
y simple"I’m not sure what-"
un "1."
play sound "audio/heart.mp3"

y shoked2"{size=*1.2}{b}Agh!{/b}{/size}" with hpunch
show lust2 with longdissolve
q "A sharp pain envelops you, like a full body cramp. From your ear muscles to your toes, everything aches, before fatigue settles in."

y tired"What. is. This…?"
un simple"Told you, cleaning your body is already kind of magic taxing, cleaning a whole room was bound to drain you, especially since I had to repair cracks in the bathtub."
y "And you couldn’t have warned me?!"
un "I did warn you."
y "Warn me harder next time."
un sidee"I was kind of curious to see the effect too, thought you might’ve improved enough to withstand it."
y "How can I improve in a single day…?"
un bored"Anything is possible."
un sidee"Anything {i}has{/i} to be possible…"
y hurt2"Ughh, I feel like dying."
un bored"No, you feel like sleeping, you’re just tired, and have cramps, suck it up."
y "Is this what women’s periods feel like?"
un "This isn’t even half as bad."
y "How would you know?"
un pride"I’m a feminist."
y "I’ll just lay down on the freshly cleaned and… polished?- bathroom floor. Hope I don’t die."
un bored"The dog is going to bring you a magic energy drink and you’ll be on your feet in a matter of minutes, you drama queen."
y pf"You’re so mean to me…"
un ang"I LITERALLY LO-{w=0.6}{nw}"


un blush "{i}-Like{/i}. I like, kind of like you, for a mortal that is, you’re ok."

y bored"I suppose I’ll take that as truth."
y sadsmile"It’s kind of nice knowing you actually mean that, not being able to lie and all."
hide lust2 with llongdissolve
q "Your pain and fatigue is slowly being lifted, piece by piece."
y ec"Hey, I already feel better, that was fast, might not even need that drink!"
y simple"Why is this? I believe it happened before as well."

un sidee"I’m not… quite sure yet."
stop music fadeout 2.0

y s"A win is a win. I can prepare a nice resting spot for when Alvy gets back in the meantime."
scene alvyhouse with pushright
play music "audio/steadybeat2.ogg"
q "In one of the storage spaces you picked the brooms from, you find two perfectly good folding chairs."
q "What did his solitary aunt need two of them for? Perhaps she had friends visiting? Who are you to butt into her life anyway?"
scene porch with longdissolve
show porch3 with llongdissolve
q "You pick them up and bring them outside. With a little dusting they’re ready to be sat in, and just in time for your friend to arrive."
show alvy 2 ec with moveinleft

al "Hey, I got the goods."

y s"Sweet! Did you get the air freshener and candles?"
show alvy 2 sadsmile
al "Right here. Is the bathroom really that bad?"
y simple"Bathrooms are always disgusting, no matter whose it is. And this one has been neglected for months, or years."
al "I’m sorry for making you start without me… What should I help with? I could take the actual bath and toilet if you-"
show alvy 2 simple
y ec"No no, it’s ok, I’m already done."
al "The… the whole thing?"
al "Oh no, you’re one of those sloppy cleaners when you’re alone, aren’t you?"
y bored"The only thing sloppy after my cleaning is a co- {i}*cough cough*{/i} I mean-"
y awkward"No, I just decided to use some magic for this one."
show alvy 2 sadsmile


al "Right, your speciality cleaning magic, I forgot."
y pf"I wouldn’t say it’s my speciality… but yeah."
y smug"Speaking of, I could really use a magic energy drink right about now."
show alvy 2 ec
al "Of course! Here you go!"
al "I see you already prepared seats as well."
y s"We deserve to relax a little bit."
hide alvy 2 ec with llongdissolve
show porch2 with llongdissolve
q "The seat feels incredibly comfy after a long day of cleaning. As you sit on the porch, you can’t help but take in the view, watching people go about their day and imagining what they’ve been up to."
q "The light shines gently on both your faces, just enough to warm you but not bright enough to obscure your vision. You can see the dog's fur practically glowing, you wish you could just reach out and embrace him as you’re so close to each other."
q "You’ve taken some of the dog’s habits and deep down know that after everything you’ve been through, he doesn’t see you as an outside entity anymore."
q "Multiple times he tries to say something, gently opening his mouth, but stops himself, for lack of the right words or embarrassment."




al "I..."
al "I think this goes without saying, but you deserve to hear it-"
al "Thanks for the help. I never thought I’d be able to clean a house, especially by myself. Not that I did that much today, but it’s more than I expected still."
y s"It was fun, I certainly don’t regret lending you a bit of help."
y "It’s not like I have anything better to do."
al "Hey, do you think the fridge in the kitchen works fine?"
y "We cleaned it pretty well and I heard it buzzing some time ago, I’d say you can store some things in it. Although maybe keep them In containers for some time."
al "That’s alright, I just need to put these in there-"
q "He rummages through his backpack and picks out a small gem, from which he summons something."
y surprised"Two whole packs of soda? Wow."
y ec"Hey! You got the lemon one! Sweet!"
y smug"And sour, hehe."
al "I remember you said you liked it, I tried it once and can’t say I’m a fan, but to each their own I suppose."
y confused"Why did you buy… uhm, one, two… four, six- twenty four cans for then? I can’t possibly take them all with me."
y "Doubt I have a fridge in my dorm, and warm soda… eh."
al "Oh."
al "I thought you…"
al "I thought you’d want to stay here… with me."
y worried"But I… have a dorm, it’s not like I’m worried of anyone finding me, heh."
al "ah. Of course, I see…"
q "His expression sours more than the soda in your hands."
y awkward"U-unless you want me to stay with you! I don’t want to intrude, that's all."
al "Yes! P-please. If you may."
al "The house is too big just for me, and you helped clean it, it must be better than a dorm room, right?"
y sadsmile"Yeah, alright then, I’ll just stay with you."
q "From behind the chair, his tail wags frantically, and his feet tangle and sway over the edge like a little kid, trying to open his soda can excitedly."
q "You look forward to the garden and beyond the fence to the quiet streets. The scenery before you seems to shift, becoming your new future."
"Can’t say I expected any of this."
un simple"Me neither."
"Why, because I don’t have a face that attracts love?"
un sidee"No… it’s just… I’m really glad you got this far. I’m happy for you."
"Huh."
"I must be dreaming. Even the demon inside my head is wishing me the best."
un simple"Don’t say that. You’re awake and everything is fine."
"Thanks Scribs, it means a-"
un bored"Except that your auditions are in like an hour."
y shoked2"AGHK!" with hpunch
al "What’s wrong?"

y awkward"I- uhm, I remembered we have our auditions soon."
al "I know, we still have time. The arena is quite far but it should take us less than half an hour to get there."
y simple"It’s not just about time-"
al "Oooh, right. You’re not very experienced in summoning."
y "Do you know what we’ll have to do there?"
al "All I know is that most first years are not able to summon a Nightfallen until the first semester’s exams, so I was never too worried."
al "You just need to make your gem do… anything."
y simple"Do you think I need to own my own Nightfallen gem at the very least?"
al "I don’t see how else you’d be able to show off what you can do."
q "You both put on your thinking caps trying to find a solution."
q "Your mind keeps drifting to a certain demon-"
un "This would truly be a dream if you managed to even summon my arm."
q "In the meantime, the dog gets a somewhat worried expression, while clutching his backpack and breathing more intensely."
q "His expression softens as his eyes meet yours, and he begins a confident search."
al "I will lend you one."
y surprised"What?!"
y "A-are you sure? I know they’re very important to you and I-"
al "I’m not making this decision lightly, so yes, I’m sure."
al "It’s kind of my fault for taking your mind off of auditions in the first place."
al "Besides, there is a good chance that you won’t resonate with my gems…"
y simple"What does that mean?"
al "You know, to summon a Nightfallen at its peak requires a personal connection with its summoner."
al "Which is either obtained over time through trust or it simply bonds with you immediately if you’re compatible."
y confused"I know about that, but I thought you can still summon any Nightfallen as long as you know what’s inside the gem. The bond just makes it work better."
al "That’s for… lifeless gems. My Nightfallen are alive. If they don’t want to, they will not come out no matter what."
y "Doesn’t your friend get a little pass from them?"

al "Here."
q "He places a couple of small, decorated bags carefully in front of you, each possibly containing a gemstone."
al "These three here, Fang, Claw and Talon- they’re wild Nightfallen."
al "Do you know what that means?"
y simple"Uhm, they’re basically just regular beasts, don’t produce much energy and are very hard to tame."
y "I’m surprised you have them."
al "Exactly, they’re difficult to tame, which means they’re also very stubborn."
al "You can still try to move your hand over them, see if it does anything."
q "You do as instructed, but the gems remain unlit and silent."
y sad"Damn…"
al "Sorry…"
al "I also have two Cryptids, they’re more likely to cooperate, try it."
q "You move your hand again, this time, one of the bags seemed to jolt back a tad, but no glow to be seen."
q "However, the dog did hide his golden ring inside the pocket, a small detail you caught with the corner of your eye."
q "You swear it gleamed at you before it got shoved away."
y simple"...No luck here either."
al "…"
al "It seems I wasn’t as helpful as I wanted to be."
y sadsmile"It’s not your fault your Nightfallen don’t love me from the start."

al "Still, what will you do then?"
y simple"Can I perhaps buy one?"
al "With these kinds of prices? I don’t think you’ve been in the market enough."

y "In that case…"
y "Hmm…"
un simple"You could borrow one."
"They don’t resonate with me, I can’t use his Nightfallen."
un bored"Not his, borrow one from the Academy."
un "There should be a person that lends gems to students for these kinds of events."
"WHAT?!"
"And you’re telling me NOW?"
un curious"I thought you might find a solution on your own, I’m not your dad, you know?"
"How do you know that?"
un bored"Because I didn’t fuck your mother yet."
"NOT THAT! How do you know I can borrow gems for the audition?"
un sidee"I’ve… been around."
un "And it just feels logical, you know?"
"Are you completely sure that is the case?"
un tease"A hundred and ten percent."
y "I think I might have a solution."
al "Oh?"
y s"First years aren’t expected to be able to summon, so perhaps we’re not expected to have gems of our own either, seems logical, right?"
al "Yeah, but what will you do for the auditions then?"
y ec"There must be a person lending gems to first years for these kinds of situations. I’ll just get one there!"
al "That seems like a long shot."
y s"I don’t know, I’m pretty confident in my speculation."
al "I can see that from your smile and laid back attitude."
al "I wish I could be like that."
y smug"Hah, you don’t wanna be a loser."
al "Take that back! You’re not even close to it."
al "You’re the most awesome guy I know."
y laugh"That’s not a long list."

al "Even when it becomes longer you’ll still be at the top."
y sadsmile"Is that a promise?"
al "It’s just the truth."
al "A-anyway…"

al "Should we perhaps go a little earlier? To the arena that is."
stop music fadeout 2.0

y s"Yeah, I think that would be best."
scene black with llongdissolve
scene outside3 with dissolve
play sound "audio/crowdd.ogg"
q "You walk shoulder to shoulder through the busy streets. People are now up and about, going on with their day and many even go in the same direction as you, the auditions are somewhat of a big deal even for non-students."
q "Debating, debating… should you hold his hand? Or is touching fingertips as you brush each other’s tails and clothes enough?"
q "With thoughts like these, those nearly thirty minutes of walking went past like seconds."
scene outside2 with dissolve
show alvy simple with moveinleft
play music "audio/crowd.ogg" volume 0.2
al "So… we’re here. That’s the place."
y s"Yup! So many people have gathered already. Let’s go!"
al "Uhmm."
q "Your friend does not share your excitement, or your legs’ movement."
y simple"Something wrong?"
show alvy sad
al "It’s just- That’s A LOT of people."
q "You approach him with a smile while rolling your eyes. The palms of your hands fall on his shoulders with some force."
show alvy sur with hpunch
y smug"Do not fret, my fair maiden. I will protect you from any nasty stalkers and social encounters."
show alvy smug
al "Promise?"
q "He asks with a condescending, amused tone."
y "On my life."
show alvy sadsmile
al "Can we at least not stand in the crowd?"
y s"We’ll find the quietest spot just for you."
y smug"Now move your ass in here!"
scene black with dissolve
q "Your wish from earlier came true, as you grab his hand in yours and make your way inside."
scene arena2 with dissolve
show alvy simple at right with moveinright
y s"Thankfully the crowd is not even where we need to be right now."
y pf"Where would a gem lending person be…?"
show alvy simple at center with ease
al "Maybe it’s the place where most first year summoners are heading?"
y "Yes, but where could that be?"
hide alvy simple with moveoutleft
q "He grabs your arms and turns you around towards a group of young looking people, all with pouches and summoner brooches, walking down the stairs against the incoming crowd."
y awkward"Ah. Yes. That would be a good indication. Let’s follow them then!"
scene black with dissolve
q "The descent continues for multiple floors. The air becomes colder and more humid, not the most welcoming place you’ve been to so far."
play music "audio/crowd.ogg" volume 0.5
scene underarena with dissolve
q "Soon, the stairs open up into a large basement, with a tavern feel to it and rows of gemstones on full display."
q "Many summoners surround the place in groups, laughing, drinking, eating and most importantly; checking out their gems."
show alvy simple with moveinright
al "I’m not sure why, but I feel like you were right, this is the place."
y smug"What gave it away?"
al "Where do we even begin?"
show alvy shy
q "Your presence here seems to attract passive attention. Some people clearly remember your faces from the first gathering. A certain someone isn’t very comfortable with that."
al "I think I’ll be sick."
show alvy sur
show alvy sur at right2 with move
lu "Sick? On my watch? No sirs."
play sound "audio/oddish00.ogg" fadein 2.0
show luis at left2 with moveinleft
lu "Anything I can help with?"
stop sound fadeout 2.0
q "From behind the counter a tall… handsome… very well built man approa-"
q "Uhm, sexy, gorgeous, hard as rocks… lots of adjectives...he’s approach-"
q "Ok, there’s more- Godly, sculpted, dreamy, dadd-"
un ang"CAN YOU FUCKING STOP?!"
un "I GET IT, HE’S A SHIRTLESS HOT MAN, GIVE ME SOMETHING ELSE TO WORK WITH, DAMN!"
show luis simple at left2
show alvy simpleleft at right2
lu "Are... you ok? Wait, which one’s the sick one? I’m confused now."
al "Sorry, neither of us are, I was just exaggerating… as for my friend-"
q "After your drool falls to the ground you finally decide to close your mouth and shake yourself off."
y sal"You’re so fine- I mean- {b}I’M{/b} fine! Thanks for the concern."
y blush"W-who are you? If I may ask… {size=*0.3}you out{/size}?"
show luis at left2
lu "That would be my question usually."
show luis smug at left2
lu "I am, how you first years like to say, {i}‘the gem lending guy’{/i}."
show alvy sad at right2
lu "I take care of the gems here and lend them to students whenever necessary."
lu "Classes? Battles? Missions? I can provide it."
show alvy sweat at right2
y s"Nice, so you’re exactly who we’ve been looking for."
show luis simple at left2
lu "Anything for cuties like you, say, what, uhmm, what are you-"
lu "Are you sure he’s ok? He looks worse and worse."
q "You turn towards your dog friend who indeed seems a bit… green."
al "Alright, maybe I didn’t exaggerate as much as I thought, the crowd is… a bit much for me."
y sadsmile"Do you perhaps have a more quiet place around? Maybe a bathroom even?"
lu "I do have a bathroom but I wouldn’t want to make you stay there."
show luis at left2
show luis at left with ease
lu "Come on, you can stay in my office, and we can discuss your business here as well."
hide luis with moveoutleft
lu "Karina! You’re up to the counter!"
hide alvy sweat with moveoutleft
ka "Yes sir!"
q "From a chair, a small squirl… squarel… scurell?"
un squint"How the fuck do you…"
q "Squarell…sure- in a nice, fluffy dress and large hat, who places her comic book down and hurries to help the people at the counter. She can barely reach, but it doesn’t seem a problem for her, the enthusiasm on those cheeks is through the roof anyway."
stop music fadeout 3.0
scene luisoffice with pushleft
q "Following the shirtless man into his office, your mind is divided between worry for your friend, and the swaying lion-like tail above this man’s pants."
show luis at left2 with moveinleft
play music "audio/onenine.ogg" fadein 2.0
lu "Here we are."
show alvy sweat at right2 with moveinright
lu "You can look at whatever you want, just don’t touch."
y blush"Does that include you? Haha, {size=*0.5}I’m gonna kill myself.{/size}"
show alvy simpleleft at right2
al "Wow. There are a lot of gems here."
al "Are they all yours?"
lu "Only some, most of them are from the Academy."
lu "I let anyone borrow mine as well if they resonate with them, I’ll just keep an extra eye on them in that case."
lu "Are you feeling any better already?"
hide alvy simpleleft with moveoutright
q "His aloof expression says it all, walking away slowly and inspecting every gem in particular."
lu "I think he’s in heaven."
y simple"More like purgatory."
lu "You sure? Look at him."
y "He’s not a big fan of… dead gems. I think he’s just very curious."
lu "Ah. Yeah, my friend is like that as well."
y s"Your friend must love Nightfallen just as much then."
lu "Loving is an understatement."
lu "I remember when he tried to steal a bunch to release them. Poor fool."
lu "Lucky I stood up for him."
lu "Well, that, and he was good pals with the headmaster."
y s"Hah, yeah, that’s a bit much, but I feel like Alvy could do the same… if he wasn’t so shy."
show alvy smile at right2 with moveinright
al "Hey, mind if I-"
show luis smug at left2
q "He points towards a large drawer that clearly hides many more gems in it."


lu "Eh, knock yourself out."

show alvy simpleleft at right with ease
show luis simple at left2
al "Oh… sorry then."
y sadsmile"No, Alvy, he means you can go ahead."

show alvy ec at right2 with ease
al "OH! Thanks!"
hide alvy ec with moveoutleft
y "He’s new to modern speech."

show luis smile at center with ease
lu "He just keeps resembling my friend more and more."
y "Are you sure it’s ok to leave all of those summoners alone in there? You won’t get in trouble, will you?"
lu "Nah, Karina loves taking care of students, even if she messes up sometimes… most of the time."
lu "Plus, you’re both recommended, aren’t you? Management would like me to give you some… extra attention."
y simple"We’re that special, huh?"
y smug"I’d say you gave us enough attention with that view."
show luis smug
lu "View? Ah, you mean these?"
show luis smug with llongdissolve:
    zoom 1.6
    yalign(0.6)

q "He gets a bit closer in front of you and flexes his muscles, making his pecs move and his one good arm grow bigger and harder."
y blush"Y-yeah, that-"
lu "This one’s the strongest."
q "He ends the little show by flexing his metal prosthetic."
lu "Little wyvern accident, don’t need to ask."
y blush"’Little’? I think it looks really cool anyway, you’re really cool."
show luis ec with dissolve
lu "Thank you!"
lu "Your regular biological body is great too."

menu:
    "Should I have some fun?"
    "Continue to flirt for a bit.":
        $ luis_points +=1
        Y smug"Really? What parts do you like exactly?"
        show luis smile
        lu "Uhm, personally I’m a fan of… smaller, thinner waists. Yours seems about right."
        y "I do have one of those."
        q "You raise your shirt up and expose part of your pristine white, soft belly."
        y hurt3"I’d say it’s pretty easy to grab and hold."
        show luis blush with dissolve
        lu "We should put that to the test sometime."
        y smug"If I didn’t know you any better I would say you’re trying to flirt on the job."
        lu "And I would say you’re trying to seduce a staff member."
        y hurt3"Shame on me then."
        jump tothepoint

    "Get to the point.":
        jump tothepoint
    





label tothepoint:
show luis smile with dissolve:
    zoom(1.0)

lu "As much stalling as I’m trying to do before going to work, I have to ask-"
lu "What can I help you with today?"
y s"Nothing too complicated, I just need a gem for today’s auditions, that’s it."
show luis
lu "Easy enough."
lu "What level would you say you’re at in terms of summoning?"
show luis simple
y sadsmile"Uhmm, my friend would probably be advanced… I’ll take something for beginners."
lu "Really? As a recommended student? My friend summoned a demon during his auditions."
y bored"I’d rather you flex those muscles some more, not your friend."
show luis smug
lu "I’m just teasing, kind of."
y pf"I was scouted for my magic, I’m not very experienced in summoning."
show luis smile
lu "Alright, alright. Let me get a beginner's set."
hide luis smile with moveoutleft
q "This time, even the dog that’s been in his own world comes closer to watch."
show alvy simple at right2 with moveinright
show luis at left2 with moveinleft
lu "Here you go."
show gembox with moveinbottom
lu "You should be able to resonate with at least one of these."
q "He brings out a long box that contains a couple of very rough gemstones."
q "Cracked, deformed, what you’d expect from the lowest tier of shards."
al "And these are also dead?"
lu "Yeah, we’re not really allowed to lend the alive ones."
al "But you do have some."
lu "Yeah, suppose so."
q "In the meantime, you concentrate and hover your hand over the presented gems."
show alvy ring with dissolve
q "From the choices only one, the blue moon-crest shaped one starts to glow, and even vibrate."
q "A second surprise comes along as the dog’s ring glows as well, but just like last time, he hides it in his pocket."
lu "Seems like we have a winner."
hide gembox with moveoutbottom
lu "Strange, I never saw this one glow before, not even for-"
show luisofficeglow 
show alvy sur at right2 
show luis simple at left2
with dissolve
al "There’s another glow over there, look."
hide luis simple with moveoutleft
q "The three of you turn around to a corner drawer that looks like it hasn’t been opened in years, from which the ram retrieves another blue glowing shard."
hide luisofficeglow with dissolve
show luis simple at left2 with moveinleft
q "Smaller than the one in the box, but much brighter."
show luis sur at left2
lu "Huh, would you look at- Ah, Hey!"
show gem2 with dissolve
q "As soon as he touches it, it flies away from his hand and reunites with its missing brethren."
play sound "audio/magic.ogg"

show gem3 with llongdissolve
hide gem2 with dissolve
q "The two pieces come together forming a new shape, and the glow stabilizes to a faint, pulsing cool tone."
lu "I have… never seen that either."
show alvy conf at right2
al "What did you just do?"
y surprised"I didn’t do anything… or nothing I had control over."
"Scribbles?"
un simple"Not my doing either."
show alvy simple at right2
hide gem3 with dissolve
show luis smile at left2
lu "I suppose you two were not recommended for nothing."
lu "One summons demons at auditions, another one fuses gems, what can {b}you{/b} do?"
show alvy shy at right2
lu "Come on, all cards on the table, you got my full attention."
lu "You can resurrect Nightfallen, can’t you? That’s why you keep asking if they’re dead or alive?"
show alvy sur at right2
al "No! No, I swear. There’s nothing unique about me."
lu "I don’t buy it."
y pf"Me neither"
show alvy ang at right2
al "[name]!"
show alvy sad at right2
al "I have my own Nightfallen which is pretty rare for someone my age, I admit, but other than that-"
lu "What kind of Nightfallen are you compatible with?"
show alvy simple at right2
al "Huh? Uhm, I’m not sure, never tested it."
lu "It’s a room full of gems, no better time and place."
show alvy shy at right2
q "He seems a bit excited to try as well, but also scared."
show alvy summon2 at right2 with dissolve
play sound "audio/horror.ogg"
q "He concentrates nonetheless, having two pairs of eyes burning into him."
play sound "audio/whoosh.ogg"
scene luisoffice2 with longdissolve
lu "Aaaand the whole room is glowing, great."
q "Indeed, the whole room except for the little broken gem you just mended."
y surprised"Whoah!"
al "Whoah…"
show alvy simple at right2 with moveinright
al "What does that mean?"
show luis ec at left2 with moveinleft
lu "It means you can basically summon any of these gems if you wanted."
lu "And probably any gem you come across, judging by this."
show luis at left2
lu "Congrats."
show alvy blush at right2
al "Hm. Neat."
scene luisoffice with dissolve
show alvy blush at right2
show luis ec at left2
y ec"See?! You’re more talented than you give yourself credit for."
show alvy smug at right2
al "Look who’s talking."
lu "Do you want to borrow any gem knowing this?"
al "I’m good, thanks, I prefer my own."
lu "You don’t own a live demon, do you? Just checking."
show alvy simple at right2
al "Nope. Not even close to that level, and that I know for sure."
lu "And about you, are you choosing that blue one?"
y pf"Yup! Not like I have much of a choice, being the only one that likes me."
show luis simple at left2

lu "So that one is D71… but I have no idea what the smaller one was… Eh, doesn’t matter, they’re a single gem now anyway, I’ll register it as such."
al "When do the auditions start?"
show luis sweat at left2
y s"Like twenty minutes I think, but the sorcerers go first, so we won’t be late."
show luis sweat at center with ease
lu "A-are you leaving? You sure you don’t wanna check out more stuff?"
y "We got what we came here for, and there are no other choices for me so-"
show alvy sadsmile at right2
al "{i}*cough cough*{/i}"
y simple"Huh?"
al "I’d love to check out more gems… especially after what you did."
al "We can’t just leave after such a tease."
show luis ec
lu "He’s right, you should investigate, with my help."
y pf"Hmmm…"
al "Pleaaase?"
y smug"{i}*sigh*{/i} Alright."
y "You get lost in the gem world while I spend time with this stud, just out of earshot."
show luis blush
show alvy ec at right2
al "Nice!"
hide alvy ec with moveoutright
lu "Great?"
hide luis blush with moveoutleft

pause 1.0
if luis_points >=1:
    
    show lust with longdissolve
    play sound "audio/heart.mp3"
    "Aw shit, here we go again…"
    q "An introduction to this feeling is not needed anymore, but you know what you must do."
    "Funnily enough, this does not even change my current plans."
    q "You shove your fingers inside the ram’s pants, grabbing him by the belt and dragging him into the corner."
    show luis blush with moveinleft:
        zoom 1.8
        yalign(0.6)
        xalign(0.4)
    lu "Ok… that did things for me."
    lu "Is it wise to start something like that with your friend here?"
    jump afterluispoints
else:
    show luis smug with moveinleft
    q "You grab the ram by the wrist and drag him a bit further away, in a respectful yet authoritarian manner."
    lu "I sense questions incoming."
    jump afterluispoints

label afterluispoints:
y confused"You don’t seem to want us to leave, why?"
show luis think

lu "Is it hard to believe I simply like you?"
y "Come on, it may be true, but there’s something else as well."
hide lust with dissolve
show luis bored with dissolve:
    zoom 1.0
lu "Alright, fine."
lu "It’s boring and stressful out there, ok?"
show luis ang
lu "I love this job, but they’re becoming more and more strict with the paperwork and the rules, and every gem I lend I have to be afraid of some kind of possible punishment if I don’t get it back in time."
lu "Like that’s somehow my problem."
show luis bored
lu "Not to mention first year summoners aren’t very interesting or fun."
lu "Aside from you two, of course. You’re probably more interesting than most seniors, in fact."
show luis smile
lu "Not to mention very cute."
q "You try not to blush but fail miserably."
lu "Also kind of dumb."
show luis sweat
lu "Not you! Them. The other first years."
show luis bored
lu "Agh, I’m getting a migraine just thinking about it."
y simple"Is it always like this?"
lu "No, not even close, this is just a busy day."


if luis_points >=1:
    lu "I don’t even have time to relieve some stress, it would help a lot."
    y smug"I can help with that."
    show luis simple
    lu "You do know what I’m referring to, right?"
    y "Get off some steam? Blow one out? I don’t know what other figures of speech to use."
    y hurt3"I’m a good stress toy, so I’ve been told."
    show luis smug
    lu "Heh, yeah?"
    show luis smile
    lu "I… appreciate the offer."
    show luis simple
    lu "Trust me, I’d accept in a heartbeat."
    lu "I’m not seeing any opportunity to do it at the moment, even if it would make my day go by faster. I literally don’t have any time for that on my hands."
    show luis bored
    lu "Especially because she expires soon…"
    y simple"She?"
    lu "Three… Two… One-"
    play sound "audio/crash.ogg" volume 0.4
    pause 2.0
    play sound "audio/veryloud.ogg" volume 0.2
    q "Loud crashing noises can be heard from just beside the door, and the people’s murmurs intensify each second."
    ka "{size=*0.6}S-sorry sir! I’ll find your gem from this pile in just… oh boy. Is next weekend alright?{/size}"
    lu "{i}*sigh*{/i} I can’t leave her at the counter for more than ten minutes and thirty seven seconds {i}on the dot{/i}, otherwise chaos ensues."
    y bored"So you’re saying you don’t have time to fuck me because you need to be at the counter?"
    show luis simple
    lu "That’s… yeah, basically it, perhaps when I’m off-"
    y "I'm also busy the rest of the day."
    lu "That's a shame, then-"
    show luis sur
    y smug"Then see you below the counter."
    lu "What?"
    y determined"Quick, yes or no? Blowjob from me in the next two minutes?"
    show luis sur at left5 with move
    q "The ram is left bewildered as you push him towards the door and open it, and get ready to close it behind him at the same time."
    hide luis sur with moveoutleft
    lu "Yes!{w=0.5}{nw}" 
    
    q "Is the last thing you hear before the door gets shut completely."
    q "The people outside, including his sque- mammal friend are certainly happy to see him, so you won’t find him back for any clarifications."
    un simple"Are you actually doing what this mind of yours is imagining?"
    un sidee"Loving the idea, don’t get me wrong, but there are a lot of people outside, you know?"
    "I’ll be behind the counter, nobody will see."
    un curious"How do you plan on getting there without being seen?"
    "I don’t know, how do you plan on getting me there?"
    un bored"Damn you."
    "Hey, you wanna suck a dick or boil in this Lust Rush?"
    un ang"Grrrr… alright."
    un eyeroll"I can make you… transparent."
    un "Anything else would take too much of your magic, but that should work well enough."
    "Fine by me!"
    q "The short woman, Karina, enters the door at that moment, looking around with an unsure expression on."
    ka "Hello? Luis told me to supervise the one named Alvy?"
    y ec"Yup, he’s just over there, he loves people, go say hi."
    ka "O-ok."
    y determined"Scribbles power activate!"
    jump LuisSex
else:
    y smug"And are you trying to say two first years are making any improvements to your state of being?"
    show luis smug
    lu "Heh, yeah, as absurd as you think it sounds. You're both very neat, in different ways."
    lu "Under other circumstances I would've loved to know you better. Maybe even invite you to dinner sometime, especially you, alone."
    y sadsmile"That's very nice of you, I couldn't refuse if it happened."
    show luis sur
    lu "Really? I'd be glad to hear it, but that would be cheating I believe, considering the things I have in mind for you."
    y blush"I-I'm not... wait, cheating? As in... me and Alvy? T-together?"
    show luis smug
    lu "You did not finish a sentence yet there."
    y sadsmile"What I meant is... we're not together, me and him."
    show luis smile
    lu "But you want to be."
    y "I... Yeah... suppose so."
    lu "Too bad for me then, no shots will be thrown today."
    show luis ec
    lu "But I do think you should go have a nice afternoon enjoying those auditions with him, trust me."
    y smug"Fine, fine, I get a hint when I hear one."
    show luis smile
    y "I can't promise we'll have a great time watching the summoners though."
    lu "Nothing is too boring if you're with the right people."
    scene black with longdissolve
    y ec"Hey, Alvy! Let's go, we'll be late!"

    jump AfterLuisSex


label LuisSex:
hide lust with dissolve
label alvycg10:
$ persistent.unlocked_alvycg10 = True
stop music fadeout 2.0

q "Scribbles, aka: me, casts a transparency spell on you as soon as you open the door."
scene black with dissolve
q "Light bends and shifts around your body. Not quite invisible, but unless someone looks directly at you with intense focus, you should be good to go."
play sound "audio/unzip.ogg"
scene luissex with longdissolve:
    blur 25
play music "audio/tejano.ogg"
q "You quickly slither under the table next to him, like a snake, a snake hungry for cock."
q "The ram is busy catering to the few students still undecided on their gems, or ones that simply have questions."

q "He watches with warm amusement as you crawl under the table, his tail swishing behind him." 
q "He spreads his legs wider, giving you better access to his growing erection."
y smug"{size=*0.6}Let’s see what we’re working with{/size}."
q "He is more than willing to cooperate as you unzip his pants and try to drag them down to the floor."

lu "{size=*0.6}Hurry up, this is exciting but I still have enough shame to not want to be caught with my pants down, literally.{/size}"
y simple"{size=*0.6}Are you going to get in trouble otherwise?{/size}"
lu "{size=*0.6}At the sex school? Be for rea-{/size} {b}HI!{/b} Welcome, how may I help you?"

q "Looks like he’ll be busy from now on, but so will your mouth."
scene luissex with longdissolve

q "You reach out and rub his growing erection with hunger in your eyes."
q "Some precum already starts to ooze out in no time."
q "Your quick, hot, heavy breaths make his cock shiver in anticipation."
y bleed"I can’t decide if I want to continue the foreplay or begin the show."
q "One hand is unbuckling your own belt and the other continues to stroke the hefty meat."
q "With your whore expertise you deduce it has to be around nine inches long, girthy and veiny, with a considerable amount of cum shooting from those heavy balls right down your throat in no time."

q "The ram continues his business like usual. Nobody suspects their conversation partner could be naked from the waist down, with a hungry kitten stuck to his crotch."


q "As soon as your tongue ghosts over his sensitive flesh, Luis’s hips twitch forward involuntarily. His regular hand trying its hardest not to grab your hair and push you forward."


q "He rocks his hips, rubbing his cock against your lips, smearing them with his essence."
q "With all the lust accumulated you simply can’t stall any longer."
scene luissex2 with llongdissolve
q "Your mouth opens wide and there goes the man’s rod. Swallowed whole in one go."
lu "Y-yup, these are t-the ones I recommend."
lu "Damn it, you thirsty kitty…"
lu "Yeah, no, I mean I got some more in these drawers."
q "You hold it in, with your nose pressed deep in his pubes. A satisfying smirk would be plastered on your face at the fact that no hints of gagging can be heard, if your jaw allowed for any more movement, that is."
y boba"{i}Sluuurp, mhmm, shlop, shlop-{/i}"
q "Soon, some obscene sounds of slurping and suckling reach the ram’s ears, making his cock throb with need, but also worry."
q "If he can hear it, others might as well, and he knows it."

lu "{size=*0.6}Sorry, man, I’ll have to shut you up the only way I can think of.{/size}"

q "His powerful leg wraps around you like a vine, pulling you in closer and keeping you locked in."
q "Your movement is limited but not stopped. Still, that is enough for the sloppy smacking sounds to quiet down just enough."


lu "A succubus? Y-yeah, got some right here."
lu "{i}*huff*{/i} Careful, these things will suck the life out of you, haha… literally."

q "You sure are sucking some years from his life, with your head bobbing, hungry tongue slobbering over your prey."

q "You have to give credit where it’s due, even receiving the head of his life; he’s still as professional as ever, guiding the inexperienced students and looking out for their needs, with barely any shiver or stutter to his voice and body."
q "You haven’t touched yourself up until now, and you don’t have to-"
q "The sweet, strong scent of his shaft and balls and the pressure it builds up in your throat, combined with the lust that’s yet to be satiated get you closer and closer to orgasm."
q "’A desperate eager slut, ready to cum from a single dick in his mouth’, your thoughts, not the narrator’s."
q "Your tongue covers your teeth and glides up and down, feeling every pulsing vein and ridge on that monster in its way, until it touches the fur at the base and the cycle begins anew."
q "Without a warning or a sign from the happily conversing ram, the juicy, wet shaft starts throbbing violently, the balls flex eagerly and his legs tighten around you, as if his cock in your mouth wasn’t enough to cut the air out."
scene luissex3 with llongdissolve
play sound "audio/cum.mp3"
q "Hot, thick ropes of cum shoot straight into your stomach, with no chance of escaping. You close your eyes tightly and wait, pump after pump for what feels like ages."
q "In the meantime, your own climax starts as well. How can you even begin to comprehend having the semen of another man so deep inside you, and not shoot your own shots?"
q "Slowly, the ram lets go, the leg lock softening along with his cock, allowing you to guide it out."
q "What kind of service would it be if you left the poor man in this state?"
q "Of course you put your tongue to work one last time, as a sign of gratitude, and clean any mess remaining."
q "Most of his seed was pumped down your throat, but some drops and traces still remain, and this kitty won’t let any go to waste."
q "At last, you help him with his underwear and pants, as well as the buckle."
q "A pat on his thigh and an under-the-table fist bump marks the end of your little experience, with the Lust Rush long gone now."
q "You do wish you could thank him for the good time, but the quick glance with a smirk and wink he gives you will have to suffice, he’s a busy man, but a less stressed one now."
scene luissex with longdissolve:
    blur 20

un simple"I assume you want another spell-"
y smug"Eh, keep the magic."

q "Y-you get out from under the table, zipping your pants back up."
scene underarena with llongdissolve
stop music fadeout 2.0
if from_gallery:
   
    $ from_gallery = False
    jump return_to_gallery
else:
    pass
q "Confused murmurs can be heard around the room as you look around nonchalantly and unbothered, whistling a happy tune."
show luis blush with dissolve
play sound "audio/crowd.ogg" volume 0.3
q "Luis seems amused by your move, and even a man like him knows how to blush."

lu "[name], how do I convince you to marry me?"
y ec"Be a five-five shy dog with mommy issues."
lu "Hah, of course."
scene black with longdissolve

q "You pat him on the shoulder and he caresses your hand one last time, before continuing to serve the still confused audience."
q "A knock on his office door will be enough to let your friend know it’s time to go as well."
jump AfterLuisSex


label AfterLuisSex:

scene arena2 with llongdissolve
play music "audio/cjazz.ogg" fadein 2.0
play sound "audio/crowd.ogg" volume 0.2
q "Saying goodbye to the weirdly sexy ram, you make your way back up the stairs, until the dog starts to trail behind."
show alvy sad with moveinleft
y simple"Something the matter?"
al "It’s the sorcerers doing their auditions now, correct?"
y "They’ll start in a minute if they haven’t already, yeah, why?"
al "Do we have to be there?"
al "Isn’t it just better to stay in an office filled with gems… just the two of us, until our turn comes?"
y sadsmile "Oh come oooon! It’s going to be fun!"
y "There are people I’m very interested in watching show off."
al "But people are surely going to approach us, since we’re recommended students and all."
y pf"Hmmmm."
show alvy simple
y "I do have an idea."
q "You rummage through your backpack looking for a specific item."

show must zorder 2 with moveinbottom
y ec"Here you go!"
al "…"
show alvy bored zorder 1
al "Really?"
y must"You wanna trade with me or something?"
al "IIIIIII’m good."
al "But this will not be fooling anyone."
y "Better than nothing!"
y "Now let’s go! I don’t wanna miss Tate’s and Coal’s auditions."
al "I’m going to regret so many things, so very soon."
hide alvy bored
hide must 
with moveoutright

q "Your little disguises prove to actually work-"
q "In some ways."
q "Yes, they are turning heads, everyone wants to take a look at you, but they don’t seem to realize who you are."
q "That, or they’re too scared to approach."
stop sound
stop music fadeout 2.0
scene arena with dissolve
play music "audio/fight.ogg" volume 0.6
q "In any case, while you find two secluded seats to watch the auditions, your cat friend’s turn comes to be called into the arena."
y must"WOOHOOO! GO TATE!"
al "Are you really that close?"
y "I spoke to him like four times, we’re basically best friends."
al "Why do I feel like he would agree."
al "Do you know what he’ll do?"
y "He can teleport as far as I know, not sure about anything else."
show dummy with dissolve
al "How will that help him against that thing?"
y "He could… uhm, I’m not sure."
scene catarenaa with dissolve
play sound "audio/lightning.ogg"
q "The cat looks around at the crowd, as if making sure all eyes are on him, before conjuring a ball of magic in his hand."
y must"Oh, he’s doing something."
al "Electricity perhaps?"
q "After a moment, he shoots the ball towards the target dummy, and it vanishes completely."

scene arena with dissolve
stop music fadeout 2.0
q "The arena falls silent."
al "He didn’t just obliterate that… Did he?"
y must"I don’t think- LOOK THERE!"
q "A small shadow grows larger and larger in the same spot where the dummy was."
play sound "audio/explossion.ogg" volume 0.6
show dummy with moveintop
hide dummy with vpunch
q "With a loud crash and a massive dust cloud later- the machine is nowhere near functional, crumbled into pieces."
play sound "audio/cheering.ogg"
al "He shot a teleportation spell and let gravity do the work, interesting."
y must"I didn’t know teleportation could work like that."
un bored"If I have to talk about his teleportation one more time I’m gonna vomit."
"Why? We didn’t talk about it at all, ever, did we?"
un sidee"Uhmm, I’m just not a fan of mobility spells."
"That seems like a weird ick to have. They’re extremely useful spells!"
un ang"Shut up and let me have my own opinions, alright?!"
play music "audio/fight.ogg"
d "WHAT A GREAT DISPLAY OF OFFENSIVE TRANSPORTATION MAGIC!"
d "NEXT UP WE HAVE ANOTHER PROMISING FIRST YEAR, COAL, LET’S WELCOME HIM INTO THE ARENA!"
d "NEW DUMMY REQUIRED AS WELL PLEASE!"

y must"Coal, huh?"
y "I wonder what he does."
#scene badasscoal with longdissolve

q "The panther walks in with a confident expression and steady hips, on which rests a peculiar device, the one he’s been carrying and guarding the whole time, almost as obsessively as your dog friend and his backpack."
#scene badasscoal2 with hpunch
q "As soon as the match starts, he powers up his device, and in moments, a beam of energy shoots out from it, creating a large hole right in the center of the dummy."
q "The machinery managed to shoot some projectiles towards the panther before its demise, which were successfully blocked by a barrier created from the same device."
scene arena2 with dissolve
stop music fadeout 2.0

y must"That was even faster than Tate’s match, wow."
show alvy zorder 1
show must zorder 2
with moveinleft
play music "audio/cjazz.ogg"
al "He didn’t even use magic, did he?"
y must"That looked like magic."
al "But it came from his device."
y "He sure took care of that dummy better than most sorcerers, so does it matter?"
al "Suppose not, but it’s interesting to say the least."
show alvy sadsmile zorder 1
y "See? Didn’t I say you’re gonna have fun?"
al "Yeah… people are far more fun than they seem."
al "The whole world has so many surprises, good surprises."
q "He looks at you with a… sort of loving gaze, is what you’d describe it, although it’s hard to tell under the mustache. It is starting to confuse you."
scene black with dissolve
q "The sorcerer’s auditions go by relatively quickly, each person doing what they need to do in just a minute or two."
q "Since the Shard is not getting that many new members this year, soon it’s the Summoner’s turn."
scene arena2 

show alvy zorder 1
show must zorder 2
with dissolve
y must"Already?"
al "That just means we can go away faster."
y "I wonder how the list will go."
al "Not alphabetically, if the sorcerers were any indication."

d "THE FIRST PHASE OF TODAY’S AUDITIONS HAS ENDED! NOW FOR OUR DEAR SUMMONERS-"
q "Groans and moans echo throughout the arena, and even some disrespectful boos."
d "DON’T WORRY EVERYONE, I’M SURE THIS YEAR’S FIRST YEARS WILL CREATE SOME VERY INTERESTING GLOWING GEMS AND… AND SMOKE CLOUDS!"
q "His reassurance doesn’t seem to work, and it seems some summoners even take it as a mockery towards them, judging by the ugly stares."
q "Luckily, he’s unaware of them."
"I don’t know, there are enough people looking that he most likely saw at least some of them… poor Dallan."
un sidee"Uhm, yeah, you’re right, surely."
show alvy sadsmile
al "He’s a great host aside from being a bit oblivious at times."
y must"Aiden isn’t helping much either."
y "He’s been staring at his phone this whole time instead of commentating."
al "Maybe he’s shy since the Headmaster is literally behind him."
y "Aiden? Shy? I don’t know him that well, but I know that’s not the case."
y "Maybe he got a match on a dating app."
show alvy simple
al "Dating app? Is that a thing?"
y must"Yeah… I don’t know if I’m in a well enough state to explain what it is."
al "I can figure it out on my own based on the name, believe it or not."
al "But I doubt he needs an app to date someone, he’s very handsome."
y "You like him? {i}*gasp*{/i} You have a crush on him?!"
show alvy blushangry
al "Not a crush! I can recognize his good looks, you know? Just like I can tell you’re cute without… I-I mean, I can have opinions! That’s all."
show alvy blush
y "You sure can, your opinions are very respectable too."
stop music fadeout 2.0
play sound "audio/wind.ogg" volume 0.2
q "The thought that someone thinks you’re cute raises your mood and confidence, so much so that you ascend to a world of your own, a world of your own creation, with flying dog boys begging for your attention."
show alvy sur
q "In a world deep enough that you don’t even hear your name being called multiple times by now."
show alvy ang
al "[NAME]!"
y "Ah! W-what was that? Sorry, I was thinking of stuff."
show alvy sur
al "YOU’RE UP!"
play sound "audio/scratch2.ogg"
y shoked2"What?"
q "You look down at your pants, but thankfully nothing noticeable is showing."
al "The arena! You’re first!"
d "[NAME] [NAME2]?"
show alvy simple
y worried"FUCK!"
play music "audio/fight.ogg"
q "You jump out of your seat and run through the crowd with cartoonishly clumsy movements, and jump into the arena."
scene arena with dissolve
y hurt2"Great first impression."
y "And why the hell am I the first one?"
y angry"This is like… the opposite of plot armor."

un ang"Shut up and do your task."
y s"Right… and that is summoning my new little buddy."
y awkward"The one I haven’t ever tried to summon before."
y "Why do I like to make things hard on myself?"
un bored"Cause it reminds you of dick and you’re a slut."
y ec"You are so right."
q "The wolf has mentioned your title as recommended student while you were inside your daydream, so the crowd is waiting with bated breath to see what this ‘prodigy’ will do."
un tease"Don’t disappoint your fans."
y pf"I’m already stressed enough."
un simple"I’m serious, focus, you can do this."
un "Just think of the summon materializing."
y worried"I don’t even know what it looks like…"
un "Not even the most skilled Summoner in the world would either! You just mended that gem, who knows what resides in it, but it synced with you, so everything will be fine!"
y s"Oh, you’re… right in so many ways, thanks for the support, I can do it."

scene codysummons20 with longdissolve
q "The gem from earlier sits in the palm of your hand in its dull form."
y worried"Please please please be a cool, flashy Nightfallen."
q "Although you have no idea what resides in it, you’re tightly connected to the Nightfallen inside, so it shouldn’t be a problem to successfully summon it."
q "With a deep breath and seconds of concentration… it begins to move, then glow, and then-"
play music "audio/raye.ogg" fadein 1.0 volume 0.8
show codysummonss3 with longdissolve
q "With a large smoke cloud trailing behind, a creature appears."
q "It is… you can’t quite make out what it is."
q "The weirdly adorable Nightfallen is about your height, trying to stand on two legs at first then falling back to fours."
q "It looks at you with glee in its eyes... with its... large, sparkling eyes."
y sadsmile"Hey there, buddy."
y "You’re not a mimic… or a slime."
y "Not anything for beginners at least."
y "What are you?"
q "It chirps in response, as if it understood you but has no means of communicating yet."
q "The people watching are left in awe as well. Mostly because they didn’t expect someone to actually summon anything at the auditions."
show nightfallen 
hide codysummonss3
q "The curiosity turns to deep fondness when the creature flops on its back asking for belly rubs."
y smug"You’re enjoying this attention, aren’t you?"
y "It would be a crime to refuse you… so I suppose I’m petting my first ever Nightfallen."
q "You kneel down next to it and bury your hand in its soft, silky fur. Your action is followed by shouts of encouragement and approval from the crowd."
q "The Nightfallen has absolutely failed in damaging the provided dummy it was supposed to attack, but it captured the hearts of all those present, and some would say that is much more important."
q "After a minute of scritching and scratching and caressing, the Nightfallen is satisfied, and turns back into smoke, but not before giving you a polite bow, as a parting gift."
scene arena with longdissolve
stop music fadeout 3.0
y ec"That was… the best thing I’ve ever seen."
play sound "audio/cheering.ogg"
q "People around you would agree, considering the standing ovation your walk back to your seat has been met with."
scene arena2 with llongdissolve
y "How did I do?"
show alvy ec zorder 1
show must zorder 2
with moveinleft
play music "audio/cjazz.ogg"
q "Talking isn’t needed here, the dog’s wildly wagging tail says a thousand words, and the tight hug he dares give you says a million."
y blush"Oh!- oh. I take it you liked the display?"
al "It was amazing!"
show alvy conf
al "Was that a Wildfur? No, that would be illegal, I know that much. Perhaps a Cryptid? It looked like both, unless… {i}*gasp*{/i} was it a demon? It couldn’t be, right? Maybe a fairy of some sort, what if we tried-"
y smug"Calm down, it got you that fired up, huh?"
show alvy sadsmile
al "Sorry, yeah, I love finding out things about Nightfallen. Making up for all the time I spent learning the piano instead of reading Nightfallen books."
al "We’ll have so many things to talk about later!"
y "We have the whole year ahead of us, five of them, in fact."
show alvy ec
al "I can’t wait!"
y s"For now let’s sit and-"
d "NEXT UP!"
al "It seems like it’s my turn already, wish me luck!"
hide must with moveoutbottom
y "You don’t need luck, but still, leave them breathless!"

hide alvy ec with moveoutright
y "I’m wondering just how good he is. Will he summon all of his Nightfallen, I wonder?"
stop music
d "AND BEGIN!"
scene black







"Meanwhile." with longdissolve
y simple"..."
y surprised"What the-"
y "Where am I?"
y worried"Scribbles?"
y "Scrib Scrib? You there?"
y "Alvy?!"
play music "audio/triste.ogg"

xx "Shouldn’t you be spectating the auditions?"
y simple"Who-"
scene horseball with longdissolve
th "My butterflies are enough."
th "But shouldn’t YOU do the same?"
xx "Nah, it’s not my time just yet, I’ll just hang out with you some more, my good friend."
th "We’re not friends. And don’t you have better things to do?"
th "Argus is keeping an eye on him, why don’t you?"

xx "Father wants my eyes to be on you just a little more."

th "Not even hiding it anymore, huh? Just say to my face how much you don’t trust me."

xx "We believe in your opinions, but after you fucked him for a whole night it’s a bit harder to trust that you won’t be biased."
th "It didn’t actually happen."
xx "But it could’ve happened."
xx "Imagine having a perfectly good cake in front of you and it being taken away just like that."
th "You are an enabler."
xx "I’m just seeking fun wherever I can."
xx "Their bond grows stronger, much, much stronger already, and it’s only been about four days."



th "Don’t remind me…"
xx "Oops, forgot your jealousy is hard to hide."


xx "Look at the bright side."
xx "You, plan A, failed, but so did plan B! Now plan C looks more promising than ever!"
xx "Isn’t that great?!"

th "That’s what YOU wanted. I never wanted to get to plan B in the first place…"

th "Why…"
th "Why doesn’t he like me?"
th "I’m so much better than that stupid leopard."

xx "I don’t know, ask him."
xx "They’re both listening."
show horseball2
stop music
th "What?"
play sound "audio/button2.ogg"
xx "And watching. So fix your hair."
play sound "audio/button2.ogg"
th "I- I- my lord, you-"
play sound "audio/button2.ogg"
scene black
play sound "audio/button2.ogg"
xx "Oops, we’re out of time, the other twink is coming back."
play sound "audio/tension1.mp3"
y asleep"…"
al "Hey! Hey [name]!"
scene arena2 
show alvy
play music "audio/cjazz.ogg"
y shoked2"What… where-"
y surprised"Alvy?"
al "Were you sleeping?"
y hurt2"I think so?"
show alvy sad2
al "So you didn’t see me in there…?"
y worried"Not on purpose though! I promise!"
show alvy simple
y "I passed out, literally, and had this weird dream about Therium and this plague doctor masked freak."
show alvy sur
al "Seriously? He looked like that…? Are you feeling alright now?"
y "Yes, I’m just a bit tired, so you actually believe me?"
show alvy sadsmile
al "Of course!"
al "You wouldn’t lie to me, would you?"
y "Never! I promise. Unless it’s a joke, but that’s not the case right now."

show alvy simple

al "Has nobody tried to wake you?"
y simple"Why would they? It’s the summoners’ auditions."
q "Looking around you both notice multiple people deep in a slumber, no doubt created from boredom."
show alvy bored
al "They’re already bored when the two recommended students went first?"
y "Maybe they fell asleep earlier."
y must"In any case, shall we go? I doubt any more surprises will come around."
show must with moveinbottom
al "With pleasure- oh, almost forgot my mustache."
scene black with dissolve
stop music fadeout 2.0
q "While making your way towards the main gate, two large bodies and a medium one block your way unintentionally by teleporting right in front, startling the dog."
show arena2 with dissolve
play music "audio/wisp.ogg"
show wolf20sadsmile at right with moveinright
d "There really is no need to waste your magic like that, we can just walk, Tate."
show cat20sadsmile with moveinleft
t "But I wanted to catch [name] before he leaves and tell him how awesome they were!"
y must"{i}*cough cough*{/i}"
hide wolf20sadsmile
show wolf20surprised at right
show cat20simple 
q "They turn around as if it comes with a surprise that someone wants to use the main gate they’re blocking."

hide cat20simple
show cat20
show wolf20 at right
hide wolf20surprised
t "Oh hello there strangers!"
show tiger20bored at left with moveinleft
d "Are you leaving already? The summoners still have a while to go."
q "You deepen your voice before responding, just for the sake of amusement."
y must"Yes, that is part of the problem actually, we have other things to do."
y "Surely you can relate."
d "We are unfortunately escorting our friend to detention."
d "He got in a bit of hot water lately."
t "You don’t have to tell complete strangers that!"
show tiger20suspiciouss at left
a "What… fucking strangers…?"
q "You look up at Aiden and shrug with an awkward smile."
hide tiger20suspiciouss
alv alvym"Detention? At an academy?"
a "He is literally the only one that ever got detention, it’s not a thing for normal people."
d "It is basically his timeout. There aren’t many punishment rules since… well, we’re all adults here with responsibilities and don’t need that kind of thing."
show cat20bored
a "But this cat is a special case…"
t "Your ability to hurt your friends with words baffles me, Aiden."

a "By the way [name], well done on the auditions, both of you."
hide cat20bored
t "What?! You know [name]? Can you ask him what he thought of my performance as well when you meet him?"
a "I’m sure he doesn’t… let’s go."
t "Awwww."
t "Cool mustaches by the way."
show wolf20ec at right

d "We should all hang out one of these days."
d "I want to know more about our recommended students!"
hide wolf20ec
show wolf20awkward at right
d "Oops! I mean, the nice strangers we just met..."
hide cat20
hide cat20sadsmile
show cat21scared

T "Uhm, me and Aiden are actually busy tomorrow."
hide wolf20awkward
show wolf20surprised at right

D "What? Again? What are you two doing that you can’t tell me?"

A "If we told you you’d freak out."
show wolf20suspicious at right

D "Why? If you two are hooking up you can tell-"
hide cat21scared
hide cat20
show cat21mad
show tiger20angry at left
aandt "{size=*1.6}NO!{/size}" with hpunch
aandt "We’re not!"
hide cat21mad
show cat20simple
hide tiger20bored
hide tiger20angry
show tiger20simple at left
T "You’re just very… rule obsessed."
hide wolf20suspicious
D "Gasp!"
D "You’re off to break rules?"

A "Uhm… no, we’re hooking up, you were right the first time, come on Tate, let’s go, for real now."
hide cat20simple
hide tiger20simple
with moveoutleft

D "W-wait!"
hide wolf20
hide wolf20surprised
show wolf20awkward at right
show wolf20awkward at center with move

D "Sorry [name], I mean, stranger, it seems like I have to keep an eye on my friends tomorrow."
D "And now as well."
D "And forever."
D "You can’t even trust them with an egg, I swear."
hide wolf20awkward with moveoutleft
D "GUYS! I CAN BE TRUSTED WITH YOUR DEGENERATE REBEL PHILOSOPHIES, I SWEAR!"

y must"A feeling of Deja Vu rushes over me."
show rose at left with moveinleft
show coal at right with moveinright
q "Before you can step out of the gate, yet another block in the road appears, two of them."

r "Hello again [name]!"
co "What’s with the mustache?"
y must"Oh, hi, we were just-"
y "What the-"

q "Your partner is no longer with you."
y "I was just… trying a new style."
co "Might have to reconsider."
y bored"Probably."
r "Again just you. I could’ve sworn we’re getting the whole gang together this time!"
y simple"The whole gang?"

r "All of the recommended students."

r "We are yet to meet Alvy, but it seems you befriended him already."
r "Good for you."

co "You have a very friendly demeanor about you, so I’m not surprised."
r "Maybe some other time."
r "We seriously need to go to dinner sometime."
co "Or spar in the arena for a bit."

y awkward"I-I’m good, thanks, on the second thing."
y smug"But food does speak my language."
y "Although I doubt we’ll be able to schedule something before the test."
y "Oooh that little dog, so slippery he is, haha."

r "Howl when you do find him. We’d like at least a hello before the test starts."
y "Will do!"
co "Come on, we’ll be late to the meeting."
hide coal with moveoutright
r "He is such an impatient man…"
r "See ya around [name]!"
hide rose with moveoutleft
y "Bye!"
stop music
# mustache shenanigans over
y "…"
play music "audio/cjazz.ogg"
y "You can come out now."
q "The next moment, the dog reappears near you as if he never left, but this time the mustache is gone, and yours should be gone too probably, the panther was right."

al "Sorry… I panicked…"
y must"Even with our super high tech disguises?"
al "Especially with those. If I am to meet them for the first time I at least want to appear normal."
y smug"We’ve talked about this, normal is boooooring!"

al "It’s so not!"
al "Now let’s go have a completely normal time relaxing in the afternoon, you’ll see just how ‘boring’ it is."

y "Well that doesn’t count, with you around not even standing around feels boring."

al "Then come watch me drink three soda cans in two minutes under the house’s shade."
y s"That is something I do need to see."

y "We should order takeout too."
y simple"Talking to them about food plans made me hungry."
scene black with dissolve
stop music fadeout 2.0
q "As an experienced and professional narrator, this would be a good point for me to create a choice, the choice of whether or not you’ll finally hold his hand in yours without the pressure of time pushing you to do so."
scene chibitown0 with dissolve
play music "audio/chibiprologue.ogg"
show chibialvy4 with dissolve
q "But it isn’t necessary, as there is no correct choice other than full stop yes, nor do you get a say in it regardless, as the shy dog’s hand slides into yours first."
q "The way back is destined to be long and quiet. After some time of enjoying each other’s company, studying each other’s steady footsteps, sway of tail and hips, you get a little idea."
q "Just to spice things up a little, you take out a pair of earphones from your backpack, having to break the warm hand holding for an agonizing ten seconds to do so."
q "You offer him one bud which he accepts without a second thought."
al "What are we listening to?"
y s"Was going to ask you the same thing."
y "What are you into?"
al "Cuddles are nice."
y pf"I’m not familiar with that ban- never mind you were making a joke, haha."
al "Wow, someone’s sharp."
al "I usually like to walk through town with some Hollowcity playing."
y ec"I love that artist, I have all their albums saved!"
q "The happiness on his face can’t quite be described. It’s that face a puppy makes when its owner comes home from a long workday, the face a child makes when the ice cream truck stops just for them, the face snow leopards make when their crush is happy… yes, you two are pretty much twins."

q "You vibe to different songs, artists and bands, skipping and dancing all the way home. What strangers in the streets? What prying eyes judging you? All you know is that you’re having fun."
scene black with llongdissolve
scene porch 
show porch2 
with longdissolve
stop music fadeout 2.0
q "The chairs are in the exact same place you left them in, waiting for your arrival."
play sound "audio/forestsound.ogg"
y hurt3"Ahh, you’ve never felt so comfortable, mister chair."
al "Why was today so draining? We barely did any actual work."

y s"Socializing is an extreme sport."
al "Touche."

al "Oh, I forgot the sodas."
y "I’ll bring them!"
scene alvyhouse with pushright

q "You grab as many cans as you can carry, slam the fridge door with your hip and hurry back."
scene porch
show porch2
with pushleft
play music "audio/dreamy.ogg"
Y pf"Perhaps it would’ve been more convenient to just grab some food from somewhere on our way here, instead of ordering."
al "I feel like we’ll have more control with a whole catalog of restaurants in front of us, won’t we?"
y s"You’re probably right."
y "What do you wanna eat?"
al "Hmmm."
al "I’m craving some fruit sandwiches right about now, a bunch of them."
y confused"Fruit sandwiches? If we find any places that sell them."
al "We could make them if anything."
un bored"Please don’t, this story is long enough as is…"
y bored"I don’t have the energy."
y s"What else do you want?"
al "That’s it."
y "You can’t just eat fruit sandwiches… that’s not a meal."
al "Yes it is! It’s carbs with dairy and fruit… it’s no different than a pasta dish."
y bored"Pasta will at least have tomatoes for veggies, if nothing else."
al "Tomatoes are fruit."
y angry"That... NO! What?! What are you doing to my brain? Stop! It’s not a fruit and It’s not a meal!"
y bored"I mean technically…{i}*sigh*{/i}"
y pf"I’m ordering a pizza as well anyway."
stop music fadeout 2.0
al "I’m okay with that, as long as I get my sandwiches."

scene black with longdissolve

play sound "audio/soda.ogg"
pause 1.0
play sound "audio/soda2.ogg"
$ renpy.pause(10.0)
scene porch 
show porch2 
with longdissolve
al "Told you- {i}*burp*{/i}- I can do it."
stop sound
play music "audio/steadybeat2.ogg"
y smug"I had my doubts, I can’t lie, but that was a good technique."

al "You know, for a place taken over by nature it looks nice."
al "The outside of the house, the garden, even the pathway from the gate to the porch was almost left untouched."
y ec"Mother nature must’ve known you’re coming and tidied up a bit."
al "Could I ask you not to mention that word please? Sorry, but it’s stressful just to hear it."
y pf"I said a lot of words in that sentence."
al "...'Mother'."
y simple"Oh, sorry, she did look very intimidati-"
y awkward"I mean- {i}seem{/i} that way, from what you told me."
y "But I understand."
al "Thanks."
y "Spontaneous topic change!"
y ec"How about-"
al "You said my aunt’s name in your sleep."
y simple"-…"
al "I reckon that’s spontaneous enough."
y "It… sure was."
y sad"I-"
al "I don’t blame you, and I’m not upset at you, I promise."
al "I just want to know for sure what you’ve seen, please."
y "Just you, younger you, and your aunt, surrounded by Nightfallen, with your… parent, watching."
y simple"Seemed like a memory to me."
al "Might’ve been."
y "I’m ready to listen, to anything, just so you know."
al "I want to tell you… so many things. But I’m afraid."
q "The dog’s hands are shaking, barely holding the cold can with little force."
y sadsmile"If it involves secrets you can trust me."
al "I do trust you, but I literally can’t."
q "His large, pleading eyes lock onto yours, silently begging for help… but you can’t help when you don’t know where to start."
y simple"Is there a literal spell on you preventing you from talking, or some kind of trauma?"
al "The latter? I think? Although the first one could be true. It’s not like I’m experienced in magic, but I doubt it."
y sad"I wish I could help…"

al "My dreams have been empty for about a week or so as well, which is the more alarming part."
y sadsmile"You mentioned you dreamed about demons before, correct?"
al "One. Just one particular demon, if that’s what it was."
y "Aren’t you glad they’re gone anyway?"
q "He seems to be stuck between shaking his head and shrugging, undecided on what to think."
al "They weren’t bad, per se. In fact, I wouldn’t be here without them."
y simple"Why’s that? What did they do?"
al "How do you think I got my Nightfallen gems, [name]?"
q "It feels like the dog gathered all his strength just to say that sentence."
q "At that moment a slight realization hit, or perhaps more like a new truck of questions you need to throw his way."
q "It’s true, a sheltered kid from a family of non-hunters that hates Nightfallen? What experience does he have with Nightfallen?  Why is he here? How is he here? And where do you come into play in his journey?"
q "You can’t help but chuckle."
y sad"I suppose I stuck so close to the surface level story that I forgot to search you deeper."
y "But that’s why you’re so nervous about it all, the answers are not that simple, huh?"
q "He nods slowly, looking at the gentle blue butterfly landing on his half empty soda can."
y sadsmile"That’s alright! Don’t fret. You sparked a big fire of curiosity in me, and I won’t stop until I find every last bit of detail from your personal life. I’ll open you up like a book, and I’ll let you know I’ve read a hundred and twenty four books this summer alone."
y smug"You could say I’m an expert."
q "He looks happy and relieved."
al "Please do."
un simple"Looks like what he truly yearns for is someone to give a shit about him, nothing more and nothing less."
"But he physically can’t bring himself to open up…"
un bored"I think you know what the solution to that is."
y "Dreams are also my area of expertise."
y "I will drill you so hard and deep-"
al "O-oh?"
y pf"Wait… no."
y blush"Uhmm, spontaneous topic change?"
al "If you insist."
al "{size=*0.5}But I don’t mind that last part.{/size}"
y pf"{size=*0.25}Noted?{/size}"
al "W-what about your life?"
al "I wouldn’t want to assume, but surely you don’t have things that bad happening, right? Outside of the divorce, that is."
al "I didn’t get to dream about you, so sharing seems fair."
q "He’s waiting for the juicy information about a city boy’s life, the highs and the lows, while wagging his tail frantically and beaming with excitement."
y awkward"Uhmm, hmm."
un tease"Come ooon, you don’t want to disappoint him."
un sidee"And maybe you’ll unlock some of these closed off memories for me to peak in as well..."
y "I’m not lying when I say that… I don’t remember much."
un ang"You little shit."
al "How much is ‘much’?"
y simple"I remember my therapist. Although not exactly what we talked about… ever."
y bored"Kind of a waste of money in that regard."
y sad"I remember I had to move schools and leave my friends a couple of times, that must’ve sucked."
al "But you don’t remember them?"
y simple"N-no? Not particularly. It’s not like we were BEST friends or anything."
y "You don’t think I’m a bad person for that, do you?"
al "No, but I do think there’s more to that than you think."
y bored"Please, don’t turn into a therapist as well."
al "I’m just saying."

y "Good thing I remember my most traumatic event at least, God made sure of that one, if nothing else."
stop music
b "What did God look like?"
play sound "audio/sitcom.ogg" fadein 1.0
show bean 2 with movee
play sound "audio/button2.ogg"
al "…"
play sound "audio/button2.ogg"
y simple"…"
play sound "audio/button2.ogg"
un simple"…"
play sound "audio/button2.ogg"
b "I bet she has no fur."
play sound "audio/button2.ogg"
b "Shedding is not very godly."
play sound "audio/button2.ogg"
y "Who the fuck are you?"
play music "audio/catjazz.ogg"
b "Hi, I’m Bean, says right here."

al "Are you our delivery boy?"
show bean 2ec
b "Oh yeah, almost forgot. Your life stories were much more interesting than listening to my aunt complain about her topical antibiotic ointment cream being too cold for the tenth time, so I got lost in the sauce here."
y pf"How long have you been here for again?"
show bean 2conf
b "Uhhmm, you ordered this twenty eight minutes ago, it took me about eight to get here and two more to get my pants unstuck from your broken gate’s metal thingy, so I don’t know, like forty minutes?"
Y worried"Is my pizza cold?"
show bean 2
b "Yeah, cold pizza is the best, isn’t it?"
y bored"Only if they’re leftovers and you have a hangover… I’d like it hot and ready."
show bean 2ec
b "That’s what she said."
al "Do you have my sandwiches?"
show bean 2 
b "Good news about those. Since you’re the only weirdos ordering these, no offense-"
y "That’s fair."
b "They gave you a couple of extra ones, but they also specified I have to put them on the house, so I’ll just throw them real qui-"
show bean 2sur
al "Do that and I break your arms.{w=1.0}{nw}"

y angry"Alvy!"
b "Yooo. That’s brutal, man."
al "S-sorry… I’m serious about my sandwiches…"
show bean 2conf
b "Should I put them there gently then, ooor-"
y bored"No, Bean. ‘On the house’ just means for free."
b "Oh alright. And by {i}‘free’{/i} you don’t mean you want sexual favors in exchange, right?"
y blush2"What? No!"
al "Why’d you think that?"
b "I got this job because of a lost bet with my brother, and in only a couple of days I got invited to like… seven sex parties, and a couple of regular requests for like blowjobs and stuff."
y pf"While on the job?"
al "For money?"
show bean 2
b "I don’t know about money, but they did offer tips. I’m pretty set in life, so I don’t need tips. Had to decline all of them."
b "I have to say, this whole experience did raise my self esteem by a lot. Gay men find me extremely attractive."
y pf"You do have certain… qualities."
al "Yeah… although I can’t explain it."
show bean 2smug
b "Thanks, you two are hella cute as well. I’d probably accept an invitation from you two if anyone, but like, not in a gay way or anything."

y bored"I think the food is the only part of you that should enter us…"

b "I understand, a committed marriage is great, but if you ever need to spice it up-"
al "We’re not…"
y blush"M-married…"
show bean 2conf
b "I am so confused right now."
y awkward"Just good ol’ pals, besties, living under a roof… haha."
b "Man, historians would love to write about you."
b "Can my bros just live with me, and sleep in my bed, and bite my lower lip in affection without it meaning anything?"
y simple"Uhm, yes?"

b "That is so cool… I need to make some phone ca- wait, do Nightfallen have phones?"
al "What?"
show bean 2
b "Can I get your numbers though?"
y bored"I don’t think so, thanks for the food, goodbye."
show bean 2conf
b "Do you believe in afterlife?{w=0.5}{nw}"

y angry"GOODBYE!"
show bean 2
b "Fine, I missed two deliveries already, don’t want another strike."
b "Give me four stars."
al "Not five?"
show bean 2conf
b "THEY already like me too much, I want my stats to be less than perfect to combat THEIR affection towards me."
hide bean 2conf with moveoutleft
stop music fadeout 2.0
un curious"Why are those capitalized?"
play music "audio/steadybeat2.ogg"
y bored"Finally, he’s gone."
al "He’s funny."
y confused"Seriously? Every seemingly normal person around is a weirdo in your eyes except for mister high on life?"
al "He had a kind aura around him."
y smug"Or are you just grateful he brought the food?"
q "The dog thinks while taking a massive bite of his cream sandwich, half a mandarin bursting with juices from within."
al "{i}I woknow, ould e{/i}."
y pf"And we’re not having this discussion again, you ARE taking a slice of pizza."
y "You can’t live with dessert alone."
al "You sound just like my maid. Except fast food or sugar weren’t ever on the table."
al "Huh. We’re circling back to me it seems. I don’t like these powers of yours."
y s"Trust me, I’m not a good manipulator."
al "That’s what a good manipulator would say."
stop music fadeout 2.0
y smug"Maybe I’ll crack you open without you realizing."
play music "audio/catjazz.ogg"
ch "Hope I’m not interrupting your cracking."
show chelsie with moveinleft
y surprised"Chelsie!"
ch "Hello boomers!"
ch "This place looks great for parties! Although you two don’t seem like the type to throw any, or go to any."
y bored"Did you come here just to judge us?"
al "And how do we never see anyone coming…?"
show chelsieec

ch "Oh no, certainly not, finding you is just a little surprise."
ch "There is a hole in the wall just on the other side of this yard."
ch "It was always empty so we just used it as a sneaky getaway."
hide chelsieec
show chelsiesmug



ch "I’m sure you’re very curious why I need to sneak out right now and can’t take the main gate-"
y simple"Not really."
al "Can’t say we do."
ch "Aiden asked me for a favor, a super secret Nightfallen mission, business, escapade, adventure."
ch "Tate and Dallan would usually do this kind of stuff with him, but they need to stay in ‘detention’."
ch "Pff, I know, what a low effort lie, I know an excuse when I see one."
y simple"I’m pretty sure that’s true, Tate got detention very early on."
ch "Naaaah. He just wants me, it’s alright [name], you don’t need to be jealous just cause usually you’re his type."
y blush2"Am I?"
hide chelsiesmug
ch "Besides, looks like you’re already taken."
q "She winks at the dog, multiple times in a very obvious manner."
al "I will not entertain that with more responses."
show chelsiesmug
ch "So don’t be greedy, leave some men for the rest of us!"

y simple"I don’t even know how we got to this accusation."
y "Do what you must, I guess."
hide chelsiesmug
show chelsiepf
ch "Phew. Thanks."
ch "Again, this is SUPER secret. I only told a few dozen people, so you make sure nobody is on my trail, alright?"
ch "Especially Merina."
ch "She’s his ex."

al "So much unwanted drama."

show chelsieec
ch "Ha! Of course there is! People need to put in the work to get to me, I’m not that easy."
hide chelsieec
ch "Especially because I have this situationship with Rose at the moment."
y confused"You do?"
hide chelsiepf
show chelsie
ch "She doesn’t know yet."
ch "That’s another secret for you two."
al "At this rate we’ll find the secrets of the universe, life and everything."
ch "I’m surprised you don’t know yet, your house address is literally the answer, hah!"
al "Huh."
show chelsiepf
ch "Suspicious…"
ch "I’ll go before something weird happens."
hide chelsiepf
show chelsieec
ch "Toodaloo!"
hide chelsie
hide chelsieec with moveoutright
stop music 

y ec"Byee!"

y s"What did you think of her?"
play music "audio/steadybeat2.ogg"

al "A bit strange."
y confused"Really. Stranger than Bean?"
al "A little bit."
al "She seems like the type to do bad things on accident."

y pf"Can’t confirm nor deny that, but it would make sense."
y s"Are there any sandwiches with grapes in there?"
al "There’s one with kiwi and grapes."
y "Close enough."
q "The cold bread cools your palms as you unwrap the translucent plastic."
q "You never quite understood this desert, an inferior cake, you’d call it."
q "This time, your opinion might change for the better. The bread is soft and slightly moist from the sweet syrup. The fruit just tart enough to cut through the sweetness."
al "Hey, so… just curious-"
y simple"Yes, they’re very good, but they still don’t substitute meals."
al "Not that!"
al "Do you have a pair for tomorrow’s battles?"
y surprised"Oh. Uhmm, no. I’ve been with you for most of my time here."
al "Do you think we have to fight?"
y simple"I don’t think so. School hasn’t even started, hell, we aren’t even officially admitted yet, until the test is done."
al "That’s a relief."
y "You don’t want to fight?"
al "No way, why would I?"
y "To… show off I guess, but now I realize you definitely don’t care about that."
al "I’ll do it with you if you really want to, I’m not against the idea."
y s"That’s okay, I’m not very experienced anyway. It will be a world of pain and nothing else."

ha "Am I interrupting something here?"
show haimaa with moveinleft

al "How? How? How do we never see them coming?"
y sadsmile"N-no, other than our lunch."
show haimabored
y "Uhm, Haima, right?"
ha "Ughh, great, you know who I am, what do you want?"
y "Nothing much really, was just going to ask what you’re doing here, same question you were probably about to ask."
hide haimabored
ha "Oh."
ha "Right, you’re recommended students, aren’t you? I think I remember your faces."
q "They say rubbing their temples in annoyance that they didn’t realize sooner."

ha "Didn’t know it’s your place."
al "Are you also here for the {i}‘secret’{/i} exit?"

ha "Yeah… I’m probably the person using it the most."
ha "Hope you don’t mind that I trimmed the grass and bushes around."
y surprised"So that’s why the garden looks more kept than the interior."
ha "I’m just trying to get away from the academy for a while without anyone tailing me."
ha "Too many people want stuff from me and I can’t deal with that right now."

al "I know the feeling…"
al "Not that I’m so important, but sometimes I need peace and quiet too."
ha "Since you’re recommended you must’ve been bothered by my colleagues more than enough."
al "I’ve been in this town for a while, so yeah… quite a lot."
y simple"Why? What do you have to win with us?"
ha "Eh. A bunch of money for us leaders and vice leaders, and benefits for the Shard as a whole."
ha "It’s a good deal, but I don’t have the energy to pester you about it."
ha "Plus, all of you come here with a Shard already in mind, and basically no way for us to change those plans, so why bother?"
q "They seem calmer while talking to you, although still apathetic, at a glance."
q "The intriguing, dark, cursed arm covered in bandages lays at their side lightly shaking, as they hold on to the scrunched up sleeve with the one good arm."
al "Want to sit down for a while?"
show haimasurprised
q "They seem very surprised. You think it’s a bit odd the shy dog that doesn’t like company muttered those words unprompted, but even so, your reaction wasn’t as heavy as theirs."
q "He tries to weigh their fruit preferences with squinted eyes for a moment, before settling on one and handing it to them with an inviting gesture."
q "You join in quickly and throw the pillow from your chair on the porch."

al "You might want to stay here for a minute at least, one of your colleagues just passed through here."
hide haimasurprised
ha "Was it… Merina?"
y bored"Chelsie."
ha "Hmgh… Alright, I could take a little snack break."
hide haimaa with llongdissolve
show porch4 with longdissolve


q "They sit down awkwardly, unwrapping the plastic slowly with one hand."
q "You let the dog do the talking for once. He seems curious about someone who is as interested in talking to new people as he is, which is not at all."
q "But that somehow cancels it out."

ha "So you two live together here or something?"
al "It’s my aunt’s house, or was…"
al "We just finished cleaning most of it."
ha "A whole house to yourself sounds better than a dorm room, even if it’s the size of a penthouse."
al "I don’t think I could survive in a dorm."
al "Do students have… roommates?"
ha "Only those that want to. Most of them are single rooms."
al "At least you have that."
ha "Hah. Just because I’m alone in a room doesn’t mean there aren’t eyes on me twenty-four seven."
al "W-why? Is someone watching us?"
ha "Not you. Just me."
ha "I’m under curse watch."
ha "They have to make sure I don’t go crazy and destroy the town."
y surprised"You can do that?"
ha "Yeah, and that’s the only reason I accept being treated like this. I admit, it’s a bit terrifying to even think about."
ha "You don’t seem as alarmed as you should be."
al "I don’t believe you’d hurt someone intentionally."
ha "Heh, why not? Do I not look the part?"
al "You’re not weird enough in my eyes."
y s"Oooh, that’s a big compliment."
q "Once again they look at the dog with wide eyes before regaining posture and changing the subject."
ha "Thanks… so, anyway-"
ha "Going into my little place in the forest through this hole in the wall is the time I’m truly alone."
ha "Passing through the barrier makes me untraceable for a little while."

al "I’m never truly alone either. Well, now I don’t really want to be, since [name] got here."
y blush"Awww."
al "Aside from students wanting me in their shard, there are also my overbearing parents."
ha "I’m dealing with a Harpy Hare myself, how do you manage them?"
al "By… running away?"
ha "Huh."
ha "Metal."
q "They reach out with their regular hand to fist bump the dog."
q "Your worries come out for just a moment. You sigh in relief that you taught him how to fist bump, or there would be another microphone incident."

ha "Thanks for the treat. I reckon Chelsie must be far enough away to not bother me."
ha "And thanks for… not having any problems for me to solve, I guess. You’re neat."
al "Thanks for sharing your story, and for taking care of my garden."
y ec"See ya around."
ha "Good luck on tomorrow’s battles."
hide porch4 with llongdissolve

q "Although you still can’t quite make out what creature they are, one detail is clear- they can’t stop their tail from wagging as they walk away faster and faster in embarrassment."

q "You watch the dog wave goodbye fondly, even after the leader’s figure is no more."
y s"You were very talkative there. I’m proud of you."
al "They reminded me of myself too much."
y "A lot of people share things in common with you if you try to get to know them."

al "Really? What do you think I share with our vice leader?"
y smug"Therium? Come on, you both love Nightfallen more than anyone."
al "How would you know?"
q "You said that statement confidently, but now that you think about it… how DO you know? Do you even know? No… it’s just a hunch, it’s gotta be."
y simple"I mean, it would make sense, he’s the Summoner’s vice leader, and since there’s no leader yet, he’s gotta be at the top, right?"
al "I guess… What do you think we have in common?"
y s"We’re both introverts."
al "You? You look like you could wrap anyone around your finger. You must be messing with me."
y smug"I’m not! Here’s a second thing we have in common, we both came to the academy virgins! Ha, There!"
y blush"As much as I wish guys would kneel at my feet I’m not that confident."
q "The dog looks away uncomfortably as you talk."
y awkward"Sorry… too lewd?"
al "What? N-no, not that…"
al "I believe you now, really."
al "It’s just… I’m not really a virgin."
y shoked2"OH!"
y surprised"You… you did the- but your parents! Do they know?"
al "Yeah, it was their idea after all. There’s no way I’d ever get someone on our property without them knowing."
y simple"…"
y "Wait."
y confused"Didn’t you say you never met anyone outside of your family, except for-"
y surprised"...your music teacher…"
al "Well…"
y bored"That’s it, I’m murdering your grooming teacher."
q "You express holding an imaginary shotgun."
al "IT’S NOT THAT EITHER!"
al "It wasn’t him. I loved him, as a friend, but I guess I lied a little to you before."
y surprised"Impossible!"
al "There is someone else I met with, someone my parents approved of."
y simple"But did YOU approve of?"

al "…"
al "It’s not like I had a catalog of people to choose from."
al "B-but it was consensual at the time, if that’s what you’re worried about!"
q "He exclaims panicked as you cock the nonexistent firearm."
al "I just grew to regret it more and more as the real world unveiled around me."
al "I’m also regretting it… because of you."
q "You take a sip of soda slowly, trying to understand what you did wrong, but then it hits you-"
y hurt2"{i}*Cough Cough* *Cough*{/i}"
"And I choke like an idiot."
q "And he chokes like an idiot."

stop music fadeout 2.0

y awkward"I-I see…"

q "The worries for his well being go down, but the butterflies in your stomach go wild."

q "And not just the metaphorical ones…"
play sound "audio/sinister.mp3"
show butterfly3 zorder 2 with dissolve
pause 1.5
show horse zorder 1
hide butterfly3

play sound "audio/wack.ogg"
Y shoked2"AH!"
y sadsmile"Therium! H-hello."
play music "audio/horse.ogg"
q "For the first time, your friend actually sensed the new arrival coming, and his mood didn’t quite improve."

th "Hello, [name], you."
th "Hope I didn’t arrive at a bad time."
th "Is everything alright?"

q "A feeling of dread sets in your heart, just moments after it almost exploded from excitement… and the horse knows it."
y "Y-yeah, of course, I mean, you’re not necessarily here at a bad time, you’re not interrupting anything, that is, what’s up?"
al "How did you know where to find us…?"
q "There’s someone asking the real questions."
q "But he lets out a soft smirk, without leaving your eyes and shows his phone’s screen."
th "Chelsie sent your location in the group chat."


al "Great, I suppose everyone else knows where we are now too…"

y pf"God damn it Chelsie."
th "That was perfect for me, since I realized neither of you got your lunch and dinner cards."
th "Which isn’t the end of the world, there’s time for that, but then there are your dorm keys as well…"
y surprised"Oh right, I completely forgot about my dorm."
th "I see you’re probably not even going to need these, but it’s better to have them anyway."
y ec"Of course, the tenants we’ll lease the dorms to will surely need them, haha."
th "That is highly illegal."
y awkward"I-I know, just a joke, sorry."
th "You might want to focus on continuing to grow, that is your purpose here after all, isn’t it?"
th "Not useless romance, or partying, to name a few things."
y ec"Of course! That’s what we’re here for, at an academy, to learn, got it."
al "The school year hasn’t even started yet."
th "If you’re driven only by grades you’re better off {b}dead{/b} and {b}replaced{/b}!"
q "The horse’s loss of composure takes both of you by surprise."
th "I mean, the academy is not responsible for what happens to you, you heard the headmaster."
show horse ec
th "In any case, congratulations on the auditions. It does look like you’re at the very least growing, even if not by a lot."
show horse
th "Being the only students that summoned anything is certainly worthy of the recommended student title."
th "I’m happy for you, and THEY are pleased too."
y simple"Thanks? Uhmm, who are ‘they’ exactly?"

show horse ec
th "Sorry, shouldn’t have said that, slip of tongue."
th "Suppose I’m just so happy about our new member doing great."
show horse
th "Member{b}s{/b}."
q "His gritted teeth say otherwise, that wasn’t a slip out of happiness..."

th "I’ll leave you to it then."
th "Try not to go too wild, living together like this."
stop music
play sound "audio/horror.ogg"
th "It’s not just your body after all...{w=1.5}{nw}"

show butterfly3
hide horse
pause 1.0
hide butterfly3

y "I-"

q "And just like that, he disappears as quickly as he appeared."
q "As for your friend-"
y bored"I know what you’ll say, weird man, agai-"
play sound "audio/run2.mp3"
scene black with dissolve
q "He gets up and quickly runs back behind the house, holding his hand to the mouth."
y surprised"Hey! You alright?!"

scene porch
show porch2
with llongdissolve
al "Y-yeah, I’m okay. But I think I’ll stop my lunch here…"
y simple"I sure hope so, after four sandwiches."
play music "audio/steadybeat2.ogg"

y sadsmile"Did Therium make you nervous because he’s a figure of authority?"
al "Sure, among other things."

y simple"So many people showing up uninvited."
y "Does this bother you?"
al "Honestly?"
al "I thought it would… but with you here, not really."
al "Well, until our last visitor..."
al "But now that I have confirmation you’ll stay- I’m trying my best to ignore my displeasures."
al "At least I’m not scared about the thought of everyone knowing my location anymore."
y pf"I have to talk with Chelsie about respecting people’s privacy…"
al "I doubt you’ll be the first one to do so."
y "Yeah, some things are untrainable."
al "Like a storm..."
al "Still, I’d rather go somewhere else, if that’s okay with you."
y s"I’d love to."
y "We could go watch a movie."
al "Umm…"
y "Or the arcade! I love those retro ticket games."
al "Don’t you need to pay for those?"
y "With quarters, it’s basically nothing."
al "I don’t want to rely on you to pay for me."
y confused"You… don’t have some quarters?"
al "I’m all out."
y simple"Straight up bankrupt?!"
al "Yes… turns out the real world is much more expensive than I envisioned."
al "A single grand didn’t last long."
al "But that’s alright! I have the food card and my house is free, so it’s alright."
y worried"It’s not alright. A house comes with bills."
y "You’re gonna have to buy crystals for power unless you don’t need light or electricity for whatever reason."
y simple"Not to mention heating and water. Houses here come with internet bills too, unlike dorms."
y "If you don’t pay you might need to move to your dorm."
al "I… had no idea."
y "I could help with that since I’m staying here too, but besides that, having some pocket money to spend is essential for someone your age."
al "You’re saying these things, but do you have some kind of solution?"
y "I do have one, not sure how much you’ll like it."
al "I’ll do almost anything."
y smug"You neeeeed-"
y ec"A Summer Job!"
al "…"
al "It’s Autumn."
y bored"Alright, an Autumn part time job then, whatever."
al "I’ve never had a job before. I don’t even know how you’re supposed to get one."
y sad"{i}*sigh*{/i} I’m probably stressing you out for no reason right now."
y simple"We need to focus on not getting expelled first and foremost. Money problem can be solved after the test."
y s"For now, why don’t we go for a walk in the park or something?"
al "Sure, it will be a great time to think about the new problems you just shoved in my brain."
y "I’ll make it up to you with an ice cream treat."
al "Fantastic compromise!"
al "Let’s go then."
y worried"Wait… more cream for you… I might’ve made a mistake."
al "Too late to back down now, you’ll disappoint me otherwise."
stop music fadeout 2.0
scene black with llongdissolve
y smug"Just hold my hand and start walking, you happy ray of sunshine."
play music "audio/chibiprologue.ogg"
scene chibiforest with dissolve
show chibialvy4 with dissolve
q "Of course this dog is happy when he gets to indulge in activities which otherwise would be taboo in his household, with a person who would bring disgrace upon his family’s name."
"Hey! I’m not that bad!"
un simple"Course not, but a snobbish rich noble family wouldn’t appreciate your middle class ass on their thousand dollar chairs."
un sidee"That’s alright, they don’t matter, it’s just you and me- and the dog… that matter."
"Thank you… that means something."
un "Don’t worry about it."
un "...Anyway."

q "The two of you stroll down a winding path shaded by old trees just a sharp turn away from the house. Hands intertwined as you walk side by side, swaying away in whimsical delight."

q "The sun is bright and in full view, casting warm light that seeps through the leaves, creating a soft, dappled glow along your path."

q "Your steps fall into a quiet, easy rhythm, and you share small smiles, glancing at each other with shy affection."
q "Neither of you are quite sure where that promised sweet treat can be found, but you’re satisfied with the sweetness of the dog’s childish excitement."

q "At a little pond, you both pause, watching ducks glide lazily across the water as a gentle breeze ripples the surface."

q "You give the dog's hand a gentle squeeze and nod toward a pair of birds drifting close together, as if they’re in their own quiet dance."

q "You laugh softly, seeing a bit of yourself and him in the simple harmony of those birds."

q "For a moment, he looks at you and brushes his thumb gently over your knuckles, a small gesture filled with warmth."
stop music fadeout 2.0
scene outside3 with dissolve
q "The path opens back up to the urban town. You let out a soft sigh as the reassuring clamor of people hits your ears."
play music "audio/wisp.ogg"
q "You certainly loved the little quiet time you just had together, but it was starting to get too intimate for the current relationship status."

al "Pretty sure we’re away from any residential areas. All of these are shops, restaurants and establishments."
y smug"Yeah yeah, I get your hint, surely one of them sells ice cream."
al "Please, if I truly thought you forgot about our deal, I would just remind you straight up. You look like a man of your word."

y simple"Now where do we-"
q "The dog’s ears spring up suddenly."
al "Do you hear something?"
scene outside2 with pushright
y surprised"Huh?"
show maidboy with moveinbottom
st "P-please, you have to, {i}*sniff sniff*{/i} my life is on the l-line, I beg you, I’ll do any-"
st "Hello?"
st "Moris are you there?!"

q "To your twentieth surprise of the day, your partner drags you along towards the moans, without much thinking."
alv alvy"Hi, is everything alright?"
show maidboy sad with dissolve

st "H-hi, well, I wish I could say yes but I have a huge problem…"

un sidee"A feeling of dread envelopes me… for some reason."

st "Rush hour is coming closer at the Cafe I work at and my boss needs me, but I CAN’T GO!"
show maidboy mad
st "My only colleague who can take my shift has {i}‘Pneumonia’{/i}, like that’s a real thing…"
y simple"Uhmm, sure."
st "And I have tickets for the big Magic Duels, all the way in the city."
st "They cost an arm and a leg… I can’t just NOT GO!"
st "But if I don’t go right now I’ll miss it, since the teleporters close early today, specifically because of the game."

y "Can’t you just call in sick?"
show maidboy sad

st "I already made the mistake of asking my boss if I can take off... You know? Like a lame {b}honest{/b} person, so now he knows..."

y ec"Well, we tried, see ya."
q "Your arm gets grabbed with great force."

alv alvy"Will you pay us?"
show maidboy simple

st "Huh?"
y shoked2"Huh?"

alv alvy"If we take your place, will we be paid?"

y surprised"What the-"
show maidboy ec

st "YES! Yes absolutely, double my shift’s worth, a-and you can keep all the tips, that’s where the big kicker is anyway."
st "Will you really do that for me?"

y pf"{size=*0.6}Dude! We don’t have experience in whatever this guy’s job is!{/size}"
alv alvy"Hmm, good point."
alv "What is your job and how do we do it?"
show maidboy s
st "Extremely easy, actually!"
st "You are going to be waiters, except it’s even easier than that, especially for someone like you two. Petite, curvy and good looking,"

alv alvyec"See?"
y pf"What do you mean by that?"
un squint"Something’s fishy around here..."

st "You’ll just have to bring out food and drinks – and if you spill some don’t even worry, some people like that."
y simple"Ok?"
stop music
st "Then just look cute and wear these special maid uniform-"
play sound "audio/wack2.ogg"
un ang "HOOOOOOOOOOOOOOOOOOOLD!" with hpunch
un "I KNEW IT! I KNEW I SHOULD’VE NUKED THIS TOWN WHEN I HAD THE CHANCE, THIS FUCKING FAG-"
scene black with dissolve
pause 2.0
play sound "audio/pop.ogg"
show maidscribbles
pause 3.5

un bored"…" with longdissolve
un "Well. This happened."
play music "audio/triste.ogg"
un "I feel humiliated, and used."
un "I was an object of desire in a foreign body."
un "I know what you’re thinking, dear reader…"
un cry"{i}'Your host and his totally platonic friend in maid costumes satisfying customers for money? Thank you for sparing us the horror.'{/i}"
un pride"You’re welcome, my memory might be stained, but yours will remain pure."
un simple"Still, I understand the curiosity eats away at raw flesh nonetheless, like a trainwreck, so beautifully tragic, you just have to know."
un "Here is the resume:"
un suspicious"They were greeted by an evil boss with a devilish grin, half their size, but if I am any indicator, size doesn’t matter… in being despicably evil, that is."

un sidee"They wore their uniforms with too little shame, and started pleasuring their customers, with food and drink, sweet words, lies and obscene gestures."
un pride"I would never lift up my host’s skirt to take a look at his new panties, let that be on the record."

un simple"The story does have some twists. The man drooling the most over these two new hires turned out to be a certain shapeshifting tiger."
un squint"That pervert..."
un sidee"[name] seemed to be flattered by the way he acted throughout his shift… that little whor- no. He’s a victim. Just like me."
un simple"The tiger is an avid frequenter of the establishment, he was just in the right spot and the right time, so at least he’s not a stalker."
un bored"At least they got their money’s worth. The shift money, even doubled, wasn’t amazing, but the tips… let’s just say the dog didn’t work his ass off for nothing… literally."
un simple"Will you ever experience what I experienced? See what I saw? I sure hope not."
un sidee"But there is always the chance…"
un "Sometimes, things happen more than once..."
un bored"I hope they got home by the time I finish monologuing."
un "I’m going to let him off the hook for making me wear this in his mind as well, just because I pity him."
un sad"Them both…"
stop music fadeout 2.0
un bored"Scrib Scrib- out."
hide maidscribbles with llongdissolve

scene porch with longdissolve

al "Look at all this cash…"

play music "audio/purplecat.ogg"

y bored"Stop waving them around, you’re just asking to be robbed."
show alvy smug with moveinleft
al "I have friends to help me if that were the case."
y "Summoning is illegal, you’ll go to jail again."
show alvy ang
al "I meant you! Are you not gonna help me?"
y pf"I wouldn’t have to if you put the money away…"
show alvy sadsmile
al "Alright…"
al "What did you think?"
y simple"About the whole experience?"
y smug"I should be asking you!"
y "That was basically my element, I was obviously thriving."
show alvy smug
al "So you WERE bending over on purpose! I knew it."
y blushmad"W-well you spilled your water on that man twice!"
show alvy blush



al "It was an accident! I never carried that much with one hand. I swear I didn’t know he had a humiliation kink."
y simple"Goodness."
show alvy simple
al "What was your friend’s name again? The tiger guy?"
y "Aiden?"
al "Yeah, he took a lot of pictures up your skirt."
y awkward"Oh, a-and you’re telling me just now? That’s sooo embarrassing, shame on him-"
show alvy bored
al "Are you done?"
y pf"Ok I let him."
y s"But-"
y "It was for the sake of money."
show alvy conf
al "Then why did you give me your share?"

show alvy blush
y blush"Because I lo- like, I like you, and I don’t need it as much as you do."
al "…"
al "That’s nice of you."
al "I wouldn’t accept, under normal circumstances-"
y smug"But I spooked you with worries?"
show alvy shy
al "Kinda…"



y s"But seriously now."
y "You did enjoy it, didn’t you?"
show alvy sadsmile
al "I felt cute, and wanted, it was nice."
al "Don’t think I’d do it again, unless my wallet was under once more."
y sadsmile"For someone so shy, wasn’t it… a little embarrassing at times?"
show alvy shy
al "It definitely was. But I feel like it’s more embarrassing for the people that enter the Cafe specifically for us."
y laugh"That’s true."
show alvy smile
al "And it gave me kind of a… a rush."
al "An adrenaline rush, the whole day."
al "It was also nice of the Big Boss to make that pie for us."
y confused"Stop calling him that."
show alvy ec
al "But what if he hears us? Better safe than sorry."
y s"Hah, it wouldn’t surprise me."
scene black with dissolve
y "No wonder that guy was so scared of missing a day."
scene alvyhouse with llongdissolve

show alvy sigh with dissolve
al "But now I. Am. Exhausted."
y determined"Hey! That’s my line!"
show alvy conf



al "Aren’t you more muscular than me? You should have more energy."
un bored"Wow. That is not a sentence I thought I’d ever hear."
y pf"I wasn’t physically or mentally prepared to take on a real job, so it sure had a toll on me."



y sadsmile"Do you mind if I draw a bath first?"
y "My fur needs a long time to dry without a fur drier. The house was probably built before those were even a thing."
show alvy sadsmile



al "Go ahead, we cleaned the bed, but I still need to actually make it."
al "I’ll try to be fast."

stop music fadeout 2.0

y ec"Don’t worry about it, take your time."

hide alvy sadsmile with moveoutleft
scene black with dissolve
play music "audio/randaldo.ogg" fadein 2.0
scene alvybath with longdissolve
q "You walk in opposite directions for now. After choosing some clean clothes, which look the exact same as your current clothes, you find the bathroom you so quickly and nicely cleaned earlier, all by yourself."

y smug"Yes Scribbles, thank you again for your help."
un pride"{size=*0.5}yu wecm...{/size}{w=1.0}{nw}"


q "Unfortunately the oh so helpful demon wasn’t able to fix the door with the amount of magic it was given, so you’ll have to make do."
y s"Eh, it’s fine. This isn’t a public bathroom, nor are we high school kids to pull pranks on each other."
un curious"Surely he won’t take a peek through the hole."
y surprised"Alvy would never, neither would I, in fact."
un tease"Ha, bullshit. You’re the type to get in someone else’s shower and masturbate less than a meter away."
y angry"What? No! I would never."
un simple"Maybe some alcohol would influence that thought."
y bored"I’m not a drinker."
un curious"Not even if the most attractive guy in town offered you a glass?"
y "Maybe, but still, I can control myself… unless it’s a lust rush."
un eyeroll"If you say so."
y simple"I wonder if Alvy bought-"
y ec"Yup! We’re having a bubble bath tonight!"
un bored"The sun isn’t even set."
y pf"Shush, I’m supposed to relax after a stressful day, not argue."
q "The hot water quickly fills the bathtub and the bubble making solution rapidly works its wonders."
label alvycg9:
scene alvybath
$ persistent.unlocked_alvycg9 = True
show alvybath1 with longdissolve
play sound "audio/doorsound.mp3"
q "You check once again that the door is fully closed, before starting to undress."
show alvybath20
play sound "audio/sheets.ogg"
show alvybath2
hide alvybath1
with llongdissolve
q "One by one, each article of clothing is placed on the hook nearby."
q "You take your sweet time with every movement, delighted by the thought of warm water enveloping you, with the setting sun in your eyes and surrounded by green, lively plants."

q "You caress your soft, long fur, checking for rogue lumps, but the only lumps you settle on are made of fat. Yes, you are very satisfied with your body, checking every angle like a peacock ready for mating."

show alvybath3
hide alvybath2
with llongdissolve
q "But even narcissism has its limits, and you finally step into the water."

q "Oop, never mind, you’re just testing the water and realize it’s too hot…"
un bored"Pussy."
y nakedbored"You feel the temperature too! Do you want to get boiled alive?"

q "You pour in some more cold water and do a second test."
show alvybath4
hide alvybath3
with llongdissolve
q "At last, your relaxation can begin."

q "You sink slowly into the warm bath, the water lapping around you like a gentle embrace, softening every tense muscle as you settle in."

q "The light scent of lavender drifts up from the bubbles, mingling with the faint warmth of steam that curls softly in the air."

q "Your fur floats lazily around you, warmed and softened by the bath, and as you close your eyes, you feel the water cradle you, supporting you in perfect stillness."
q "You stretch out, feeling the weight of the day melt away, each gentle ripple against your skin easing you further into tranquility."
q "For a while, you simply lie there, enjoying the silence, the warmth, the calm—drifting into a world where nothing exists except this peaceful, comforting moment."
q "Breathing deeply, you let go of every worry, every stray thought, allowing yourself to be completely at peace, wrapped in the soft cocoon of the water."
q "A happy tune escapes your muzzle, as you can’t help but break in song along with the birds outside."
un simple"Your voice isn’t even that bad actually, might want to try and train it in the future."
y naked"The overabundance of compliments from you lately is a real treat, Scribbles. Not to sound ungrateful, but what gives?"
un simple"..."
un sidee"I’m just telling the truth, I guess."
un "Trying not to lie just to avoid accidentally saying something nice is not always worth the effort."
y nakedss"I’m glad the truth is so positive then. I know there are many bad things about me as well."
un simple"..."
un blush"It’s your turn…"
y nakedsimple"What?"
un sidee"Say something nice about me."

y "Oh, uhmm."


y naked"Your powers are very useful, you’re a great mage."
un bored"So… you like the things I do for you, not me."



y nakedsurprised"No! No, wait, that’s not all, of course."



y nakedsimple"I…"
menu:
    "I also think…"
    "I like your voice.":
        pass
    "You’re a great narrator.":
        pass
    "You’re very tolerant.":
        pass
    "You’re wiser than I gave you credit for.":
        pass
    "You’re fun to talk to.":
        pass
    "You’re my first friend in a long while.":
        pass
    "You made my nights better ever since you invaded my dreams.":
        pass



un blush"Is all of that true…?"
y nakedsimple"Huh? I didn’t even get to say anything."
un sidee"You don’t need to, I saw your choices."
un "It’s a bit hard to believe you think like that after knowing me for so little time, but I do want to trust your mind."



y nakedpf"You’re cheating."



un bored"It would be cheating if more than half your mind wasn’t blocked for no good reason."
un simple"I don’t actually know anything important about you, you know…?"
y nakedsmug"You’re going to be here for a long while, until my weak ass gets the power to summon you, so we got time."
un sidee"Yeah… loads of time."
y "For now, I feel like taking a nap in this warm water, would that be such a crime?"
un bored"If you wanna risk drowning."
y nakedbored"I won't-{w=1.0}{nw}"
stop music
show alvybath5 with dissolve
play sound "audio/doorsound.mp3"


q "A peculiar sound at the door disrupts your conversation."



y nakedsimple"What the-"
window hide
play sound "audio/doorclose2.ogg"
hide alvybath4
show alvybath6
hide alvybath5 
with llongdissolve
pause 3.0
play sound "audio/sheets.ogg"
show alvybath7
hide alvybath6 
with llongdissolve
pause 3.5
play sound "audio/bath.ogg"
show alvybath8
hide alvybath7 
with llongdissolve
pause 3.0
play sound "audio/hum.mp3"
show alvybath9
hide alvybath8 
with llongdissolve
pause 3.0
show alvybath10
hide alvybath9
with llongdissolve
pause 2.0


window show
Y nakedblush"Uhmmmmm…"
y "Hi?"

if from_gallery:
    window hide
    # Reset the flag so it doesn't affect the normal gameplay flow
    $ from_gallery = False
    jump return_to_gallery
else:
    pass

al "Hello?"
al "What?"
al "Alright, I know there are hooks for the robe right there, but I don’t always have to be proper just because I’m from a noble family, you know?"



y nakedblush2"Thaaaat is not even close to an issue."
al "Then what is it? You look like you’ve seen a ghost."



Y "…"
y "Nothing."
y "Definitely nothing."



al "Oh. Of course. I have to apologize."
al "I know it was a bit rude and selfish of me yesterday to bathe by myself in the hotel room, even after you requested to join, but I was a bit emotional at the time."
al "No hard feelings?"
y nakedblush2"That’s fine, I don’t mind."



al "I feel like you do mind."
al "Was it such a big deal for you? I can apologize in other ways too if that’s not-"



y nakedblush"No… no, it’s not like that."
y nakedblush2"The opposite, in fact."
y "Do you… usually bathe with someone else, or what’s happening?"



al "Obviously, who is going to wash your back and mine?"
al "Scrubbing is also overall easier to do on someone else’s body."
al "And it’s not a bad time for… for some light conversation… either-"
al "{i}*sigh*{/i}."

play music "audio/randaldo.ogg" fadein 3.0

al "I just did something incredibly weird again, didn’t I?"
hide alvybath10
show alvybath11 
with llongdissolve



y nakedss"How can we be alive without doing the most awkward things imaginable every so often."



al "How wrong was my perception of this?"



y nakedblush3"Well, for starters, nobody bathes with someone else, unless they’re five years old, or-"
y "-lovers, I guess."
y "It’s really not too difficult to do everything yourself."



al "Should I perhaps just-"
y "No, it’s too late, you might as well stay."
y nakedss"Besides, knowing that you thought this was completely normal eased a lot of my initial shock."



al "Wait, so what did you think I was doing, if you don’t think it’s normal?"



y nakedsmug"Uhmmm, let’s talk politics."
al "I’d rather die."

y naked"Fair enough."



al "Is it really more embarrassing than maid dresses though?"
y nakedpf"Maybe by a liiiittle bit."



al "But you really enjoyed wearing it."



y nakedblush"Not as true as you think it is… I uhh, I mostly enjoyed {i}you{/i} wearing it..."



al "Oh."
al "You looked good too, all things considered."
y nakedss"Thanks."
al "Although I do prefer the regular you. A bit more."
y "That’s reassuring."
q "To your surprise… with all these lewd thoughts and embarrassment inside your head…"
q "No Lust Rushes to be seen or felt."
"And only one came by today as well, I call that a win!"
Un suspicious"Curious."
q "The lack of legroom forces you to be comfortable touching each other’s bodies with your legs, unless you don’t want to intertwine them."
q "Thankfully, by the time the bubbles start to disappear and the clear water reveals what’s underneath, you’re already used to the dog’s naked presence, so nothing really changes."
q "The relaxation properties of the water gradually diminish, alongwith the temperature, so it might be time for some actual cleaning."
q "You take a sponge and some fur shampoo to start."
y nakedsmug"Come ‘ere."



al "B-but you said-"
y "Someone’s gotta wash your back, right?"

q "You wink at him with a smirk, maybe a bit straight forward, but he turns around and gets closer to you, not before betraying a hint of blushing."
q "The fur on his body, just like his paws: silky smooth, soft, untangled. He takes good care of it."
q "The muscles underneath lack definition, but these aren’t the arms of a fighter, not the back of a swimmer, nor the legs of a runner."
q "He’s a musician, a scholar, a lover."
q "Fragile and tender, but confident, that’s Alvy, that’s your friend… or perhaps-"
q "Your mind goes blank for a moment, then another, and another, like being intoxicated. The gentle hand of a dog being the only thing you feel in return, pressing against your skin and deep inside your thick fur coat."
q "When all is done, only then do you return to reality."



al "What do you say?"
y nakedsurprised"W-what was that?"
al "The water is getting cold, should we get out?"
y nakedss"Yeah, yeah sure."
stop music fadeout 2.0
scene black with dissolve
play sound "audio/bath.ogg"
q "This time, instead of staring like a statue, you look away politely as he gets up and puts the robe back on."
play sound "audio/sheets.ogg"
al "I’ll be changing in the bedroom, since your clothes seem to be here already."
y nakedss"Good idea."
q "Your initial quick bath seems to have morphed into a full spa day, turning the last visible sunlight into darkness."





scene alvyhousenight with longdissolve
show alvy 2 simple with dissolve
play music "audio/steadybeat2.ogg"
al "Do you think we’ll get in trouble if I summon inside the house?"
y s"I mean, there’s nobody to see them, so it should be fine."
y confused"Why would you want that?"
show alvy 2 sadsmile
al "Some of them don’t exactly love being inside their gems all the time."
y ec"Then don’t let me stop you."
al "But is it fine with you?"
y smug"Depends what you want to do with them."
al "Nothing necessarily, just have them hang around."
y s"Then yeah! I love little guys running around. Or… big guys. Yours are pretty big."
al "Thank you. They’ll be grateful to stretch their legs a little."
y sadsmile"My fur is almost dry, I’ll wait just a little bit before going to sleep."
y ec"Goodnight in any case! I’ll be downstairs if anything-"
show alvy 2 simple
al "What? Downstairs? There’s no bedroom down there."
y simple"Duh, the only other bed has a broken mattress, but the couch is soft enough and I stole this pillow from one of your drawers!"

show alvy 2 sad
al "A-are you sure the sofa is clean enough?"
al "I spent more time deep cleaning the bed."
al "M-maybe you should... just stay with me. In here."



al "I don’t want to be alone."
q "The answer you’re about to give will forever and ever be positive, but even so, you want to consider the implications for a moment."

scene black with longdissolve
y "Alright. I’ll stay."



q "Two young men, sharing a bed, with the moonlight showering over them through the window above their heads."
q "Unlike the other night, you both decide it might be best to wear something a bit more than simply underwear."
q "Lust Rushes might not appear, but regular boners are still on the table."
scene alvysleep with longdissolve


al "[name]?"
y simple"What is it?"
al "I’m not sure what kind of dream you’re about to have… but I’m sorry, in advance."
y sadsmile"It can’t be that bad."
al "Sorry for not being strong enough to be upfront, that is."
y "I don’t expect you to, I’m totally fine letting you be the main character for a while."
y ec"The secretive, mysterious new guy that I drag along on adventures just because I feel like it."
al "I can’t wait for more random adventures then. {i}*Yaaawn*{/i} I hope you’ll take me on many more."
scene black with longdissolve
q "Those are the last soft words spoken between the two of you, before sleep conquers your minds."
q "It’s only natural after a day filled with so much nonsense."
stop music fadeout 2.0


"Meanwhile…" with dissolve
scene horseball with llongdissolve
play music "audio/unspoken.ogg"

xx "So he really DOES rub one off in his shower, that’s hilarious."
xx "Does he also let his father deflower him in this one?"
th "Not here, he wants to be faithful for once."
xx "Interesting choice."
xx "Did you know that one is blind?"
th "Yes, I’m not a fucking idiot like him."
xx "I would’ve been fooled, personally."
th "Why am I not surprised?"
xx "When is his dream ending? I want to meet them already."
scene black with longdissolve
th "Soon. He only just got in."


stop music
"Back to you…" with dissolve





play music "audio/blizzard.ogg"
y asleep"…"
y simple"…"
y worried"Am… am I-"
y sadsmile"Oh thank goodness, it’s a dream. I don’t want to leave my bed so soon."
y pf"Now what am I doing here? Which part of my brain is this?"
y "Dark, dark, and more dark… wait, weren’t there more cracks of light in the darkness before?"

y simple"Scribbles?! Are you here?!"
Y bored"I’m kind of in a hurry to another dream!"
stop music
unn "Then get out of here already..." with llongdissolve
scene scribblesdream20 with llongdissolve:
    xpos -1600
    

y s"Hey, there you are!"
play music "audio/sinister.mp3"
y smug"Hiding behind the throne, are we?"
y simple"The throne that…"
y "Something’s not right…"
stop music fadeout 2.0
play sound "audio/horror.ogg"
play music "audio/horse2.ogg" fadein 4.0
scene scribblesdream20:
    xpos -1600
    ease 12 xpos 0

y simple"I..."

"My demon friend, cloacked in shadow and blood, sits on the ground defeated..."

y worried"Scribbles!"
y "What happened to you?"

unn "[name], you weren’t meant to be here, please just… leave."
y "You look unwell, that is even ignoring the bloody mess."
y "I don’t know how concerned I should be."
unn "I’m just patching up."
unn "Nothing to worry about here, nothing to see."
unn "Think of the blood as a metaphor of some sort."
unn "Demons can’t bleed, after all."
y sadsmile"You still look and sound very tired, are you sure you don’t need some company? Some help?"
unn "No… no you can’t help."
unn "But hey, I’m almost done, so we can go ahead and… go somewhere else."
unn "The best way you can help is leave me alone."
unn "Just a couple more pieces and I’ll be done."
y sad"But why…?"
y "Why are you so against the light?"
y worried"You complained so much about the darkness and loneliness in here."
unn "I have my reasons."
y angry"You can’t just-"
unn "Remember your promise? You can’t be upset at my secrets."
unn "The less questions the better."

y worried"But how can I just walk away from this?"



y "Alvy is my friend, but so are you now, I want to butt in as much as possible if it means I’ll help."
y simple"It… cracked more, right there, in the corner-"
unn "…"
y "Do you see that Srib-"
unn "YES I’M SEEING IT!"
unn "This isn’t going to work… I’ll need another plan."
unn "But for now…"
stop music
unn "Hey."
unn "Wake up!"
scene black 
play sound "audio/wack2.ogg"
unn "WAKE THE FUCK UP!" with hpunch
scene alvysleep with hpunch
"!"
play music "audio/wind.ogg"
"Seriously? You’re waking me up just to not let me help?"
un ang"You’re only making things worse! It’s better I keep you here."



"I need sleep you doofus! You can’t just keep me awake."



un simple"I’m not doing it just because of that."
un "I have a special mission for you here, in the real world."



"What does that even imply?"
"Will it stop your bleeding?"
un ang"Shut up about that, I told you I’m fine."
un sidee"But that interaction did make me long for something…"
un "I need you to go somewhere."
"In the middle of the night? What time is it?"
"One AM…"
"If you’re saying this has nothing to do with helping you then my answer is-"
"Hell to the no."



un sad"Please, it’s important to me nonetheless."



"Promise that it’s not just a trick to not let me in the dream, because I also promise I’m leaving you alone when I go back to sleep."
"I’m going to respect your boundaries even if it worries me."
un "I promise, and thanks…"



un simple"I simply have a way to make you stronger, and I want to share it with you."



"Seriously? That sounds… awesome!"
"Hope I don’t have to do anything illegal."



un sidee"Not necessarily."
un "You see, you found me in a magical chamber. My old ancient treasures are being kept in a similar place."
un "There is a special medallion I want you to have."



"How come this is the first I’m hearing of it?"



un sad"I thought it would be best to leave it out of your life… it’s supposed to help you with your energy manipulation technique, but since you’re a summoner now, it’s not going to be as useful."
un "And you decided not to fight in tomorrow’s battles, so that’s one less reason to get it yet again… but-"
un simple"It is special to me. And I can’t bear to have it buried in that place any longer. I want you to have it."






"That’s all I needed to hear. I dress myself quietly to not wake Alvy and walk out of the room."
scene alvyhousenight with dissolve
play music "audio/firstday.ogg" 

un curious"Are you telling me that or are you narrating?"



y "It was narration, as a way to let you know I’m going on your little nightly adventure."



un tease"Fantastic!"
un "You know where to go."
y confused"No? I certainly don’t, how would I?"
un sidee"Oh, right..."
un tease"In that case, I’ll simply guide you! Onwards my vessel!"


y "Are we having a problem here, little guy?"
un simple"Huh?"
show lilguy with moveinbottom
un bored"Oh."
un "I see."
q "In front of you stands a little creature with a skull mask on its face."
q "You remember seeing it in the dog’s previous dream."
q "It’s weirdly cute, especially as it tilts its head curiously at you."
un "Just shoo it away, we don’t have time."



y sadsmile "Heyy, little guy. Are you not going to sleep?"

hide lilguy with moveoutleft



q "The Nightfallen looks at you, up and down, and then at the door, after which happily struts up the stairs."



y simple"Where do you think he’s going?"



un ang"I think he’s a little snitch, that bastard."
un "Run out the door now or never."

show alvy simple with moveinbottom
al "Where are you going?"
y scream"AH!"
y awkward"A-Alvy, good, uhmm, night- evening! How did you get here so fast?"
y pf"And all dressed as well…?"



al "I asked my question first."
y worried"{i}*sigh*{/i} There’s just somewhere I have to be, but I’m coming back, I promise."
al "Hmmm."
y sadsmile"I wouldn’t ditch you just like that."
show alvy ec
al "I know. I want to come with you anyway."
show alvy shy
al "Unless there is something you really don’t want me involved in?"
y sadsmile"You can come. I would have to explain myself if you ever see the medallion anyway."
show alvy conf
al "Medallion?"
y "Long story, come on."

scene nighttown with dissolve
q "Although you didn’t bother to ask the demon’s opinion on the matter, he continues to guide the two of you towards a secluded part of the academy’s campus."
q "The dog tries to hide his excitement as much as he can, but you can tell a borderline rebellious night stroll like this plays into his fantasies."
show butterflies with dissolve
q "On the way you see blue butterflies dancing in the moonlight, flying alongside you."
al "I’ve never seen butterflies at night, only moths, but what do I know about the real world."
y simple"No, you’d be right, they’re usually not out at night, especially not ones as big and beautiful as these."
y "Maybe it’s one of those things you never notice, like your neighbors bringing in the groceries."
y "Hopefully they’re not caught by a bat or something."
scene theriumkiss0 with dissolve
show alvy simple with dissolve
al "Sooo, we’re in a random, empty, dark place. Is this our final destination?"
stop music fadeout 2.0

"Scribbles? Where to now?"
"…"
play music "audio/wind.ogg"
"Scrib?"
al "[name]?"
y simple"Y-yeah, I mean, give me a sec."
al "What are you looking for exactly?"
al "Should I prepare a summon to protect us perhaps?"



y "We’re not in any danger, I just kind of forgot-"
stop music

show alvy sur 
show alvy sur at right with move
play sound "audio/heart.mp3"
xx "It’s nice to finally meet you, young prodigies."



"A shiver runs down my spine as I hear a low, soft voice behind us, almost like a whisper cutting through the air."


show cloak with movee
"Slowly, we both turn around, and there they are- tall, cloaked in shadows. The hollow, dark eyes of the mask seem to gaze right through m- no, not me, Alvy... unreadable and haunting."



"The long, dark cloak drapes over their form, making them seem more shadow than person, as if woven from the darkness itself."
play music "audio/triste.ogg"


"They stand silently, observing, or perhaps waiting for something, and in that quiet moment, it feels as though the whole world stands still. Every instinct in me says to run, yet something in their presence holds me in place, compelling me to stay."

show alvy sad at right
show alvy sad at right2 with ease
al "It’s… it’s you."



xx "Long time to see, Alphonse."



y worried"You know this thing?"



al "This is the dem-"
show alvy sad2 at right2
show alvy sad2 at right with move
al "The person that helped me get to where I am today."
al "Also the one that used to appear in my dreams… not anymore though."



xx "Aww, I’m sorry darling, did you miss me?"
xx "I am a bit busy with a world ending threat kinda, sorta."
xx "Not to mention the new people that changed all of our plans."
y worried"W-why are you looking at me?"
al "That’s alright, I knew you wouldn’t be there forever."
"So Alvy actually liked the alleged demon inside his dreams… just like me."
"Should I have been more truthful with him?"
"Sure wish I had a second opinion inside my head right about now."



xx "And [name] [name2], we finally meet."
xx "I can’t wait to know more about you."
xx "But there’s more than enough time in another configuration."
xx "Such an entertaining character you are."
y simple"Thanks?"
xx "I can’t believe the other two wanted to dispose of you."
y pf"Say what?"

xx "I believe you were looking for this."
y "I’m gonna take your word for it because I’m not even sure."
"A cold, furless hand drops the short chain of the medallion into my palm."
xx "I know, he’s shy around me, don’t worry too much."

y surprised"You-"
xx "Shhh, no need for drama."
xx "And Alphonse, good job, you avoided them nicely, just like I instructed."

al "Does she know anything?"
xx "Not as far as I can tell."
xx "Just don’t wander off too far."



al "I know."
show alvy sad at right


al "Will I ever see you again?"



xx "Hah, you can’t get rid of me that easily, I might not be whispering in your ear anymore, but I’ll always be around, trust me."



xx "You, young man, are getting so close to the truth, and maybe something greater, please, continue to dig further. THEY are very pleased."
y simple"That’s what Therium said earlier…"



xx "Good luck getting through tomorrow, I have a feeling it will be a busy day."



y "We’re not going to fight, uhmm, if that’s what you’re referring to."
xx "Oh, I know."



"I swear I felt a wink behind the mask."



xx "I think I’ve said more than enough, it’s time I go…"


stop music
xx "…"
xx "WHAT’S THAT BEHIND YOU?!" with hpunch
play sound "audio/scratch2.ogg"
scene black 
y scream"WHAT?!" with hpunch
scene theriumkiss0
show alvy simple at right


y bored"Damn it…"
al "How did you fall for that?"



y "If it were a clown saying that, I would’ve laughed, when it’s a strange demon like creature in the middle of the night, I take it seriously."

al "That’s reasonable."
scene black with llongdissolve

play music "audio/nightsounds.ogg"

scene alvysleep with dissolve
y simple"I didn’t know you were on good terms with it."

al "Yeah… that’s why I wanted some advice from professionals."
al "I love Nightfallen, and don’t really have limits in that regard."
al "I was wondering if it was foolish to trust someone like that."



y sadsmile"Honestly? I can’t be the one to judge."
y "I’m battling my own mental demons."



y "Your aunt leaves you a house as heritage, a strange demon helps you escape your crazy parents and trains you to use your summoning abilities."
y smug"I’d say all the stars aligned for you to be here."



al "I’m just lucky like that."
al "Especially the part where I found you."



y sadsmile"I haven’t done much to help."



al "You gave me the confidence I need to succeed, among other, more personal things."
y smug"What other personal things?"



al "Don’t make me say it, I’m sleep deprived and easy to manipulate."



y "I’m sleep deprived and forgetful, we’re on even terms."



y sleepy"In fact, you have like… ten seconds before my brain shuts down… I’m exhausted."



al "I guess…"
al "You just made me realize what real ---- feels like…"

stop music fadeout 2.0

y asleep"That’s {size=*0.9}awesome{/size} {size=*0.8}Saylor{/size} {size=*0.7}Twift,{/size} {size=*0.6}can I{/size} {size=*0.5}have an{/size} {size=*0.4}autograph{/size} {size=*0.4}pease...{/size}{i}*snoooore*{/i}"
scene black with longdissolve
al "Heh, I should follow you into the void as well, sleep well."
"{i}In the dream world:{/i}" with longdissolve
play sound "audio/blizzard.ogg"
"Scribbles was nowhere to be seen on the walk home either."
"Whatever he’s up to, I’m not going to find out now either, since it seems this dream is already morphing just like last night."
label alvydream3:
$ persistent.unlocked_alvydream3 = True
                
play music "audio/goodbye.ogg" fadein 2.0

scene alvydream3 at Zoom((1920, 1080), (0, 0, 3940, 2160), (2020, 540, 1920, 1080),0.0) with extralongdissolve
"..."







aal "Prodigy?... PRODIGY?"
aal"I don’t care how {i}‘talented’{/i} you think he is, or how much money this career makes, he’s going to stay far away from these obsessed, perverted savages."
aun "Please listen to me. You can’t keep him caged like this forever."
aun "He has so much potential, far greater than even mine."


aal "Well that’s not something to boast about."

aal "And it’s not forever, only until he’s old enough to marry, Richard will be a worthy husband for him."
aun "More like a worthy investment…"
aal "ENOUGH!"
aal "One more word out of you and you can say goodbye to these, ‘special commissions’."
aal "I’m doing you a favor even allowing you to get close to him."
aal "Any hunter could do the same thing and keep their mouths shut for a little extra pay."
aun "If you would let me stay longer I could even find the reason why they’re attacking so much."
aal "Don’t try to manipulate me you {i}witch{/i}."
aal "Have you taken care of the rodent yet?"
aun "The Cryptid Nightfallen? Yes, and it’s a harmless and rare one, if only you could-"
aal "Synthia, I don’t care, how many times do I have to tell you?"
aal "You’re here to clean the trash, no more, no less, don’t tell me about what you find in the bags."
aun "Of course…"
aal "Now GO!"

teacher "Is she always this loud?" with longdissolve
scene alvydream3 at Zoom((1920, 1080), (2020, 540, 1920, 1080), (0, 0, 3940, 2160), 22.0) with ease

teacher "I can barely hear your notes."
teacher "C-sharp, by the way, not D."
al "Only when my aunt is here…"
al "I think she’s doing it right outside my room on purpose."
teacher "That’s just rubbish, want me to give her an earful?"
al "NO! No… she’s just going to fire you."
teacher "And you don’t want that?"
al "Of course not, you’re- my only friend."
teacher "What about the gem I gave you?"
al "I’m still trying to get used to their presence."
al "I’m not sure I’ll be ‘friends’ with one anytime soon."
teacher "Is that where you keep them? Under the floorboard?"
al "Is it such an obvious place?"
teacher "No, nobody would find them, especially your mother, I can simply sense them."
al "I wish you were my magic teacher instead."
teacher "You can’t let her treat you like that, you know?"
al "She… she’s my mom."
al "What am I supposed to do?"
teacher "You’re a smart boy, already an adult too. There are many things you can do."
teacher "My plans are still on the table too."
teacher "I’m guessing your backpack is ready at any point."
al "I’m… keeping those options as a last resort."
teacher "If you say so."
teacher "I just hope you don’t live to regret that."
teacher "Emergency."
al "What?"
stop music
teacher "EMERGENCY!"
if from_gallery:
    # Reset the flag so it doesn't affect the normal gameplay flow
    $ from_gallery = False
    jump return_to_gallery
else:
    pass
scene black
play music "audio/phone.mp3"
"{i}Emergency Call! Emergency Call! Emergency Call!{/i}"
y sleepy"What the-"
scene alvysleep with dissolve
y sleepy"In the middle of the night?"

y "Someone better be dying."
stop music
play sound "audio/button3.ogg"
"{i}*Click*{/i}"
y "Hello?"
play sound "audio/wack2.ogg"
d "{size=*1.5}[NAME], I’M DYING!{/size}" with hpunch

play music "audio/steadybeat2.ogg"
y worried"D-DALLAN, IS THAT YOU?!"

al "What’s happening…?"
d "Hey [name], sorry for the sudden jumpscare, the stress is slowly killing me but not just yet, I just needed to be sure you’re there and awake."
y bored"Mission accomplished I guess, thanks a lot."
d "Sorry, yes, it’s me, Dallan. I got your number from Therium, I am SO sorry for intruding on your free time."
Y pf"It’s 4 AM…"
d "Yes! You are very aware of your surroundings! That is very good for your task!"
y simple"What task?"
d "You’re with Alvy Arufar right now, correct?"
y angry"How?! How?! How does everyone know that???"
d "Great!"
d "You see, I have run into a bit of mess. Well, alright, not me per se, but I have to help my friends with some issues."
d "It’s a bit of a secret, multiple secrets really, so I know this is a big favor and burden on you, as first years, but there’s really nobody better for the job."
y bored"I love you Dallan, but can you please get to the point?"
d "Of course! So, uhmm-"
stop music
play sound "audio/button2.ogg"
d "Would you two be willing to present the battles tomorrow in my stead?"
play sound "audio/button2.ogg"
yal wtf"Eh...?"
scene black with longdissolve
$ persistent.alvy = True

jump alvyday3

