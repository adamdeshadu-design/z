label Tatess:
    if Secret_points <= 0:
        $ Secret_points +=1
        play music"audio/casual.ogg"
        "I'll check up on Tate, he seems upset."
        "I approach him slowly from behind, as he's lost in thought."
        y simple"Hey, is everything alright?"
        show cat20simple at right2 with dissolve
        t"Huh?"
        t"Oh, yeah, everything is fine, except that Merina here-"
        show merina20simple at left2 with dissolve
        "He points at the fox girl, to whom I give a nod of acknowledgement, being the first time we interact."
        "She dips her head politely."
        hide cat20simple
        show cat21bored at right2
        t"Doesn't want to get rid of my detention because I'm missing a couple of people on my list!"
        y simple"The one you tried to scam me into signing?"
        hide cat21bored
        show cat20awkward at right2
        t"Haha, you should learn to let go of the past."
        t"Forget and forgive right?"
        y bored"Suuuure."
        hide cat20awkward
        show cat20sad at right2
        hide merina20simple
        show merina20sad at left2
        m"Sorry Tate, but I can't bend the rules, not even a little."
        m"The new Headmaster was really set on expelling you completely for your {i}'shenanigans'{/i}."
        m"You're lucky you're still here."
        m"Honestly, I'm not sure how that even happened, but I'm glad a detention is all you're going to get."
        show cat20angry at right2
        t"I was supposed to not be punished at all if I completed this..."
        t"That's the last time I do any favors for tha-"
        hide cat20angry
        show cat20simple at right2
        t"Nevermind..."
        hide cat20simple
        show cat20tired at right2
        t"Maan..."
        t"This is just depressing."
        t"I might as well die right now."
        hide cat20sad
        show cat20tired at left with move
        show merina20sad at center with move
        "He starts pacing around the room as me and Merina talk."



        y worried"Is there nothing you can do?"

        hide cat20tired
        show cat20tired2 at left
        show cat20tired2 at right with move
        m"I'm afraid that the new Headmaster is a little hard on the rules, especially because it's his first year in that role."





        m"As I said..."
        hide cat20tired2
        show cat20tired at right
        show cat20tired at left with move
        hide merina20sad
        show merina20simple
        m"He's getting off way easier than expected."
        m"The Headmaster really wanted Tate to skip a year, he's very talented and gifted, but lacks maturity."
        hide cat20tired
        show cat20tired2 at left
        show cat20tired2 at right with move
        m"As you can see."
        "Tate's walking around us cursing the Headmaster under his breath, waving his hands in the air."
        t "I just need one day, ONE day, today and perhaps tomorrow as well...but NOOOOOOO! That damn...weirdly sexy lion just has to butt in."
        hide cat20tired2
        show cat20tired at right
        show cat20tired at left with move
        y simple"I see."
        y"Wait, how did he already get a punishment if this is the first day?"
        y"Isn't he a first year like me?"
        hide cat20tired
        show cat20tired2 at left
        show cat20tired2 at right with move
        hide merina20simple
        show merina20sadsmile
        m"Oh, he is, but, well-"
        m"I don't think it's my business to tell his story."
        y"Understandable, I'll find out eventually from the source, but for now-"
        y"Hey, Tate."
        hide cat20tired2
        show cat20tired at right
        show cat20tired at left with move
        t"hmm?"



        Y s"Maybe I could help."
        Y "How many signatures do you need again?"
        t "Only ten..."
        y "Alright, that's not so bad, we can find ten people by the end of the day."
        show cat20tired at right with move
        hide cat20tired
        show cat20surprised at right


        t "Really?!"
        t "Would you do that for me?"
        hide merina20sadsmile
        show merina20simpledown
        m "But there aren't that many students on the campus, since they're probably checking their dorms..."
        m"And they have to at least show SOME sign of magic to be allowed in."
        m "Besides, who knows how patient the Headmaster would-"
        hide cat20tired
        hide cat20surprised
        show cat21bored at right

        t "Hey hey hey, if I didn't know you any better, Merina, I'd say you don't want me to complete this list."
        hide merina20simpledown
        show merina20sad
        m "Of course I want that to happen, seeing you unhappy is the last thing I wish to witness, and we can always use more members."
        hide cat21bored
        show cat20angry at right
        t "Great! Then what's the big deal?!"
        stop music
        hide cat20angry
        show cat20surprised at right with hpunch
        h "The big deal is that you have one more hour to complete that list."

        show merina20sad at left with move
        hide merina20sad
        show merina20simple at left
        show headmaster20angry with moveinleft
        play music "audio/hm1.ogg" fadein 2.0


        "The whole room seems to get darker upon the new large, intimidating lion figure stepping into the room and our conversation, respectively."

        m "Mister Argus!"
        hide cat20surprised
        show cat21scared at right
        t "H-headmaster? H-hii~"
        t "How's it hanging?"
        t "Did you get a new haircut? Your mane looks lovely today."

        hide headmaster20angry
        show headmaster20smile1

        h "Why yes I did, it's a special day, after all, thank you for noticing."
        t "No problem, happy to serve, always at your dispos-"
        hide headmaster20smile1
        show headmaster20smile22
        h "With all that being said..."
        h "I'm assuming we'll see each other in detention tomorrow?"
        m "I thought Dallan was responsible for detentions until the teachers start the year."
        show headmaster20simple2
        h "Don't be absurd, the leader of the defender's Shard?"
        h "Why waste the time with a misbehaving first year? It's not like I can't sign some documents and keep an eye on him at the same time."
        "Tate looks like he's about to fall over from anxiety, his knees shaking."
        m "Yeah, but-"
        show headmaster20foxy
        h "Besides, I have a feeling we will get along pretty well, isn't that right, Tate?"
        t "I...uhm, well."
        show headmaster20angry
        y simple"But he won't have detention!"
        "The Headmaster's now annoyed, sharp eyes turn to me at lightning speed, but soften almost immediately."
        hide headmaster20angry
        show headmaster20smile1
        hide merina20simple
        show merina20sur at left
        "Merina and Tate also look surprised, as if everyone forgot I was there because of the tense atmosphere, and only take notice when my words hit the floor."
        hide merina20sur

        show merina20calm at left
        m "Ah, I apologize, where are our manners?"
        m "This is-"
        h "[name]..."
        h "Yes, yes I know, I do my own homework when it comes to my students, especially when they're so... special."
        h "Pleased to meet you."
        y awkward"Uhm, the pleasure's all mine?"
        hide merina20calm
        show merina20simple at left
        h "I'm sure it is."
        h "Suppose I was right to keep my eye on you from the start."
        y simple"What do you mean, sir?"
        h "Seeing how you're the only first year that attended the leader's public meeting."
        show headmaster20side
        h "Or rather, the only one who willingly did so, I should say."
        "He side-eyes Tate, making him look away."
        y "Oh, that.. I guess, but I wouldn't say-"
        hide headmaster20side
        hide headmaster20smile1
        show headmaster20pissed
        h "And what was that reproach you gave a second ago? If you don't mind me asking, I don't think I quite understood."
        un tease"Oop, you annoyed him, haha."
        un bored"Get ready for an ass whooping."
        y "H-he won't have detention if he completes his list, right?"
        y "That was the agreement."
        y "The one with the-"
        h "I know the one."
        h "You'd be correct."
        hide cat21scared
        show cat21sad at right
        t "[name], you really don't-"
        show merina20simple at right2 with move
        "Merina stops him."
        m "Let him talk."
        y "You just said he still has an hour to complete it, right?"
        hide headmaster20side
        show headmaster20angry
        h "Let me stop you right there, mister [name], I see what you're getting at."
        un "Wow, he anticipated the follow up to your rhetorical question? I think he's some kind of genius."
        h "So I'll ask this."
        h "He needs to collect how many signatures again?"
        "Merina nudges Tate."
        t "T-ten, sir."
        show merina20simple at left with move
        h "Ten signatures in an hour."
        h "Out of thirty-five."
        y surprised"We can do it, we just-"
        hide headmaster20angry
        show headmaster20angry2
        h "DO NOT." with hpunch
        h "Interrupt."
        "{i}*Gulp*{/i}"
        h "Do you know how many students I passed on my way over here, all the way from my office, which is on the other side of the building?"
        un bored"Negative four...?"
        un "Or some bullshit like that?"
        h "Two."
        h "Two students, a lost bunny with no sense of direction and a map in hand, held upside down, as well as a dog with a missing arm, that asked me {i}'how's it hanging, chief?'{/i}."
        h "Needless to say, not the most satisfying candidates."
        h "And do you know how many students sign up on average every year for the Sorcery Shard?"
        y simple"Ermm, a thous-"
        h "TWO HUNDRED EIGHT!"
        h "There is no way in Hell, he gathers up thirty-five signatures in one day."
        h "Especially now, as evening approaches."
        h "If he did, it would be some kind of record, even with help."
        hide headmaster20angry2
        show headmaster20angry
        h "You might as well give up."
        "Tate looks more and more depressed as the {i}'explanation'{/i} goes on, Merina barely holding her tongue at the Headmaster's savage explanation."

        y angry"So you just wanted him to fail then?"
        t "[name], please."
        y "Why not just give him detention in the first place then?"
        y "Why bother with an impossible task?"
        hide headmaster20angry
        show headmaster20angry2
        h "It is a lesson!"
        h "I'm not expecting you to understand as a first year, just obey."
        y "Well, I might not, but I do know one thing, he has ten more signatures to gather up, and that's what he'll do."
        "The room remains quiet, even the people that were talking nearby are now listening to our exchange."
        hide headmaster20angry2
        show headmaster20angry
        h "..."
        h "It seems like you don't like to listen to reason."
        h "Know that some things can't be solved with the power of love and friendship."
        h "That kind of logic will get you in a lot of trouble in the future."

        y smug"That kind of logic landed me a scholarship here, didn't it?"
        hide headmaster20angry
        show headmaster20amused
        h "..."
        h "Heh, you know what?"
        hide cat21sad
        show cat21simple at right
        h "I like you."
        h "Foolish as you might be."
        "Breaths of relief can be heard all around, but the loudest come from Tate and Merina."
        "A fainting mouse is caught in Dallan's arms."
        y surprised"Huh?"
        hide headmaster20amused
        show headmaster20smile1
        h "Standing up for your friends and partners is an important quality for a hunter."
        h "So, I'll give you TWO hours."
        h "I still believe it impossible, but maybe you can just find ten unfortunate souls to torment around here."
        t "R-really?"
        m "Thank you, mister Argus."
        y "Yes, thank you very much!"
        hide headmaster20smile1
        show headmaster20angry
        h "But..."
        "Oh no..."
        un "Here comes the sex punishment."
        h "If you still fail, you are both coming to detention with me."
        un bored"Eh, close enough."

        h "Let me make myself clear, I'm only doing this because the Sorcery Shard could most definitely use the extra members, as far as the records show."
        h "I'm also going to remind you that the signatures are only valid until the auditions results come in."
        h "If any of the people that signed turn out not to be proficient enough in magic, the signature won't count, and you'll both still get detention."
        hide headmaster20angry
        show headmaster20foxy
        h "Alongside some {i}'special'{/i} punishment."
        h "Do we have a deal?"
        "He extends his big, meaty hand to me and smirks."
        t "Yes, say yes, pleasepleaseplease."
        m "You don't have to do this, [name], it really does sound impossible, even with the extra time."
        "Merina is the voice of reason here, two hours or two days, does it even matter if we can't find people proficient enough? But the cat's new excited face replacing his sad expression really cements my decision."
        "How can I say {i}'no'{/i} to the hope in his eyes?"
        "So I extend my hand as well, feeling his strong grip which I desperately try to match."
        y s"Deal."
        hide headmaster20smile22
        hide headmaster20simple2
        hide headmaster20pissed
        hide headmaster20foxy
        show headmaster20smile1
        "He nods slowly, pupils unmoving."
        h "Then I shall leave you to it."
        show headmaster20smile1 at right with move
        show cat21simple at center with move

        h "And Tate?"
        stop music fadeout 3.0
        t "Yes, sir?"

        h "I hope you're grateful for your new friend."
        h "He did just save your pelt..."
        hide cat21simple
        show cat20ec
        t "The gratefulest!"
        hide headmaster20smile1 with moveoutright
        "The Headmaster walks away with a smile, this situation is obviously a win-win for him."
        "I can't believe I argued with the Headmaster on the first day... and won?"
        "Kind of."
        play music "audio/catjazz.ogg" fadein 2.0
        un "An ant doesn't win against an anteater just because the anteater wasn't hungry that day."
        "I would much rather hear that kind of wisdom on a positive note."
        un "And I much rather have a vessel that joins the Shard that will help me get a real body as soon as possible, but we can't have everything."
        "Who said I'm not joining the Summoner Shard?"
        un ang"Oh, shut your ass up, I can feel your dick throbbing with excitement thinking about that damn cat, I know your plans."
        "...Perhaps you really do."
        scene meetingroom
        show cat20
        show merina20 at left
        show merina20 at left2 with move


        m "Wow..."
        m "I didn't expect that, but it's not like I've known the Headmaster for long, so I can't be the one talking."
        t "THANK YOU THANK YOU THANK YOU [NAME]!!!" with hpunch
        "I was expecting to be toppled over by him, but this time he adopted a more respectful approach, taking both my hands in his and shaking them vigorously."
        t "You saved me!"
        y "Hold on, it's not over yet, we didn't complete the list."
        hide cat20
        show cat20simple
        t "Shoot, it felt like such a win in my book that I forgot about the real fight about to begin."
        t "You need to teach me how to talk down to men who can fit my entire head in their mouths."
        t "Literally."
        hide merina20
        show merina20sadsmile at left2
        m "I'm sorry, I do want to point out that the Headmaster can expel anyone whenever he wants, even leaders, so you should tread carefully as a first year."
        hide cat20simple

        show cat20determined
        t "Ha!"

        t "You think he gives a damn about that old man's rules?!"
        y simple"A-actually, I do, and I didn't know that."
        hide cat20determined
        show cat20simple
        t "oh."
        y "I take it that I should avoid his bad side...?"

        m "Like the plague."

        y "Noted."

        t "You're not pulling out because you're scared, right?"
        y "Course not, I'm a man of my word."
        hide cat20simple
        show cat21smug

        "Tate looks me up and down, raising an eyebrow."

        t "{i}'Man'{/i} might be an overstatement."


        y bored"I might change my mind soon..."

        t "Then let's go before that happens."
        show cat21smug at right with move

        "He grabs me tighter and hurries towards the door, but before he can drag me along, Merina's excited voice stops him."
        hide merina20sadsmile

        show merina20ex at left2






        m "Ah, Ollie! Over here!"
        hide cat21smug
        show cat21simple at right
        m "Wait just a second you two!"
        show merina20ex at left with move
        show ollie at left5 with moveinleft
        "A small, skittish mouse hurries over as Merina calls him, briefly touching me and Tate with his gaze before locking his eyes to the ground again."
        show ollie at center with ease
        hide merina20ex
        show merina20sadsmile at left
        m "Are you okay?"
        m "You fainted again."
        hide ollie
        show olliescared
        o "Y-yeah, I have to get used to the difference in size between the old and new Headmasters."
        o "He's a bit intimidating."
        m "I'm sorry it gives you such a hard time."
        m "[name], this is Oliver, my vice."
        "He adjusts his glasses."
        o "H-hi."
        y s"Nice to meet you, I am-"
        hide cat21simple
        show cat21bored at right
        t "{i}*Aghem*{/i}"
        t "Can we do introductions AFTER I complete this list and confirm I don't have detention?"

        menu:
            "Can the list not wait for the sake of politeness?"
            "You're right, no time to waste!":
                $ Tate_points+=1
                y awkward "You're right, sorry Oliver, I'd love to know you better but we have less than two hours to do this whole thing..."
                o "I understand...the Headmaster can be very scary."
                y ec "We should sit down for a cup of tea or something someti-"
                y surprised "O-ok, I'm being dragged away, bye."
                jump nointro
            "Let's not be rude.":
                $ Ollie_points +=1
                $ Merina_points +=1

                y s"Come on, I won you an extra hour, we can spare five minutes for introductions."
                hide olliescared
                show olliego
                o "A-actually I'd rather you go."
                hide merina20sadsmile
                show merina20sur at left
                m "Ollie!"
                o "Not disrespectfully, just... personally."
                hide merina20sur
                show merina20simple at left
                o "It seems pretty important, I wouldn't want to waste your time."
                hide olliego
                show ollieshame
                t "You seem pretty good at it already."
                "The mouse looks away in shame."
                y angry"Tate!"
                y "Be nice."
                "The little guy is trembling as much as Tate did in front of the Headmaster, but I doubt I'm intimidating enough to be the cause of that."
                m "Excuse him, he's anxious around strangers."
                m "And anyone that isn't me or Dallan..."
                m "We're working to solve that."
                m "For... three years now."
                hide ollieshame
                show olliesmile

                y s"Hey, same goes for me, but I control it, to some extent."
                o "O-oh, wow, you must be a powerful mage to do that."
                t "Well, he is a recommended student"
                y "As I was saying, my name is [name]."

                o "Oh yeah, I remember your name now, f-from the gathering."
                o "W-what spell do you use for that, to control your emotions I mean?"
                un "Avada kedavra."
                y "It's called {i}'making an effort for the sake of social status'{/i}."
                o "That's a long name, I've never heard of that one before."
                "He takes out a journal and starts scribbling in it."

                y "I can teach it to you sometime, maybe with some coffee?"
                "He wrinkles his nose."
                y "Or would you prefer tea?"

                o "Tea sounds wonderful."
                hide cat21bored with moveoutright
                hide olliesmile with moveoutright
                hide merina20sadsmile

                hide merina20simple
                show merina20bored at left
                show merina20bored at center with move

                m "Hey now."
                "She comes closer and whispers."

                m "You're not flirting with my vice by any chance, right?"

                menu:
                    "Was that flirting?"
                    "I am.":
                        hide olliescared
                        y "I might just be, what about it?"
                        m "In that case..."


                        show merina20sadsmile
                        hide merina20bored
                        m "Good."

                        y "Good?"

                        m "He needs to get out of his shell more, maybe another, more confident 'man' can teach him."

                        y "I felt those quotes on my soul."
                        m "Just saying, you're not too intimidating, nor too energetic, you seem nice enough, maybe you could help him."
                        jump ollietalk

                    "I'm just trying to be nice.":

                        y "No no, I promise, I'm just trying to be nice here."

                        hide merina20bored
                        show merina20sadsmile

                        m "Pity."

                        y "Pity?"

                        m "Ollie needs to learn to get out of his shell more, I thought a {i}'man'{/i} like you could help."

                        y "I could feel those quotes on my soul..."
                        m "In any case, maybe you could still help, by playing {i}'mister nice man'{/i}."
                        y "I'll see what I can do..."

                        jump ollietalk

                        label ollietalk:


                            show merina20sadsmile
                            show merina20sadsmile at left with move
                            hide merina20sadsmile
                            show merina20 at left
                            show cat21bored at right with moveinright
                            show olliesmile with moveinright

                            y "So, what's with all the homework you got there, Oliver?"
                            o "It's just work, you know, finances, schedules, reports, all the fun stuff."

                            y simple"Fun, suuure."

                            hide cat21bored
                            show cat21mad at right

                            y s"I like your glasses."

                            o "Oh, t-thank you, Merina chose them for me."
                            hide merina20
                            show merina20ex at left

                            m "A round pair of glasses for a round pair of ears."
                            show merina20ex at left3 with move
                            show ollielaugh
                            "She pokes at his ears, making him chuckle."

                            o "S-stop that."

                            y s"You two seem like good friends."
                            hide ollielaugh
                            show merina20ex at left with move
                            m "Naturally, we've known each other for a long time."
                            m "Our mothers were, and still are, in a close business relationship."
                            m "His mom has a chain of potion shops all over the country."
                            hide merina20ex
                            show merina20 at left
                            y "Could it be {i}'The Crackling Cauldron'{/i} by any chance?"
                            o "Yes, high quality, home brewed potions, seems you've heard of it."
                            y "I sure have, my family buys healing potions there, since there's a shop right across the street from our house."
                            m "My mother is basically the face of their brand."
                            y "So... the {i}Fire Witch{/i}?"
                            m "You've heard of both our families then."
                            y "Obviously I know of one of the best potion brands and one of the best Hunters out there!"
                            hide merina20
                            show merina20blush1 at left
                            show ollieblush1
                            y "Now I could even say it's an honor to meet you!"
                            "They're both blushing while Tate rolls his eyes."
                            m "The pleasure's mine."
                            o "Y-yeah, what she said."
                            hide merina20blush1
                            show merina20sadsmile at left
                            hide ollieblush1
                            show olliesmile
                            "All this time, Tate's been watching us with murder in his eyes, looking at his imaginary wrist watch every so often."

                            t "This is all nice and all, but can we pleaaaase get a move on?"

                            y simple"Yeah, we should probably-"

                            m "Alright, fair point, just one moment, let me introduce you to the others, and before you start groaning, Tate, I promise, it will only take a minute, we're speedrunning this."
                            hide merina20sadsmile
                            show merina20 at left
                            t "We'll see about that."
                            m "Come this way."
                            hide merina20 with moveoutleft
                            hide olliesmile with moveoutleft
                            hide cat21mad with moveoutright


                            show chelsie with moveinleft

                            "First, she guides me towards an eccentric raccoon girl named Chelsie, that talked a little too fast for my brain."
                            "What I could gather from her fast tongue, was that she is an inventor, the Defender's vice leader and Dallan's best friend."
                            ch "Only 48.99, special price for a cutie like you, what do you say?"
                            show merina20bored at left4 with moveinleft

                            "And apparently I look like I could use the {i}'Shmongucular'{/i} she's selling, though Merina got her away from me before she could explain where exactly you have to insert that thing."
                            hide chelsie with moveoutright
                            hide merina20bored with moveoutright

                            t "At least she didn't let Chelsie keep you here for half an hour like she usually does with first years."

                            show haimaa with moveinleft

                            "Then came a small... Wolf? Fox? Badger?..."
                            "Person... named Haima, with a cursed arm and chilling gaze that were enough to let me know I should not mess with them."
                            ha "Stupid fucking tiger, ditching his duties again."
                            ha "Just wait until I put my hand on you."
                            "They seem a little preoccupied."
                            "They're the complete opposite of Chelsie, they don't get along with their vice and don't like to talk much."
                            hide haimaa with moveoutright
                            show merina20sadsmile at left with moveinleft
                            show olliesmile with moveinleft
                            show cat21bored at right with moveinright
                            m "And... those two should be it, I believe, you met everyone else, right?"
                            y "Yes, I think, except for the Summoner's leader."
                            m "Right, well, the good news is that we haven't either."
                            y simple"How so? Did they not arrive yet?"
                            show ollie
                            hide merina20sadsmile
                            show merina20simple at left
                            hide cat21bored
                            show cat21mad2 at right
                            m "They did... but we're assuming they must be shy, it's their first year both at the academy and as a leader."
                            o "Which is very unusual."

                            m "We'll let you know if we find any information on that."
                            y awkward"You don't need to go through the trouble to-"

                            hide merina20simple
                            show merina20ex at left
                            hide ollie
                            show olliesmile
                            hide cat21mad2
                            show cat21mad at right with hpunch

                            "A determined tug on my shirt is letting me know it's time to go."
                            "For real this time."

                            y "The list, alright, I'm going."
                            m "See you later, [name]."
                            m "And good luck to you two."
                            o "G-goodbye."


                            scene black with dissolve
                            t "Finally, I thought you'd never stop talking."
                            y bored"We talked for about four minutes."
                            t "That's four too many!"
                            jump nointro

                            label nointro:
                                stop music fadeout 3.0
                                scene hallway with dissolve
                                "Tate takes a broom resting by the door as we rush out."

                                show cat20ec with moveinleft

                                t "Hop on."

                                y confused"Huh?"
                                hide cat20ec with dissolve
                                show catfly with dissolve

                                "He places the broom between his legs and to my surprise, it levitates as he takes his feet off the ground."
                                y "Wow!"

                                y bored"Who am I kidding, this isn't so surprising actually, considering where I am."
                                y s"Alright, I'm into it."
                                play music "audio/wisp.ogg" fadein 4.0



                                scene chibitate with longdissolve
                                scene CGch7

                                "I take the hand he offers me and make myself comfortable."

                                t "How do you feel?"

                                y simple"Like I have a hard piece of wood pressed against my ass and balls."
                                t "So you're familiar with the feeling."

                                y bored"What's that supposed to mean?"

                                t "Hold on tight!"

                                "Thankfully, we start moving at a steady pace, double the speed of walking, but not quite running."
                                "I look down at the moving cracks between each tile on the floor."

                                y surprised"This is awesome..."
                                t "Huehuehue, just one of my many talents."
                                y s"So you can teleport and fly."
                                y "What else?"

                                t "Uhmmm..."
                                t "Hey, want me to play the tour guide for you?"
                                t "I have a great guide impression, watch."
                                y bored"So just the two talents..."

                                t "Ladies, gentlemen and twinks!"
                                y angry"Hey, I'm a gentleman!"
                                t "I didn't mention which one I thought you were yet."
                                un bored"Self reported..."
                                t "If you look to your left, you'll see doors, and to your right, windows."
                                y smug"Any more information about these doors and windows, oh mister guide?"
                                t "Certainly, anything for paying customers!"
                                y simple"I'm not paying."
                                t "Getting to gaze upon your lustrous fur is payment enough."
                                "That was pretty smooth, I'll give him that."
                                t "The respective door on the left we're approaching in about fifteen feet was modeled in 1994,
                                by a local sculptor with Narnian origins, the main body is made of maple."
                                t"Hardwood harvested from the center of the tree, also known as heartwood, it is a deeper shade of brown with a slight reddish hue, while the frame was brilliantly thought out to be made with oak, for increased sturdiness."

                                "All of that was said with a somewhat monotone, snobbish voice."
                                y simple"Wow, you sure know a lot about that specific door."
                                y "Was any of that true?"
                                t "Yep."

                                t "I know a lot about a lot of things around here, unfortunately, most of it is useless, just like what I just said."
                                t "These were my bedtime stories as a kid..."
                                t "I suppose I should be thankful I had bedtime stories at all."
                                t "At the time I actually enjoyed them."
                                t "Although, instead of architectural history, I would have loved to know more information about how to skin a lion..."



                                y awkward"Not a fan of the new Headmaster, huh?"
                                y simple"Maybe I should've asked this earlier, but what are you getting punished for anyway?"

                                t "Stupid reasons, completely unfair, I was set up!"

                                y "And what would that unfair reason be?"

                                t "Alright, so get this, I was minding my own business, getting ready to go on a little forest expedition."
                                t "For reasons I don't feel like disclosing."
                                t "When all of a sudden, the Headmaster comes by, out of nowhere, and tells me to guard a stupid door I've never seen before."

                                y "A door?"

                                t "Yeah, it was weird, since I know this place better than anyone, but I've never seen that door."

                                un squint"Hmmm..."

                                y awkward"Uhm, what did the door look like?"

                                t "It wasn't anything special, just a door, I wasn't allowed in, I was just told that I had to stay there until someone else came by and told me to leave."
                                t "To not let anyone in and to report if anyone passed by, but everyone was at the gathering, so it was dead quiet..."

                                y simple"And you left before that person came along?"

                                t "Yes, I had to!"
                                t "I promise I had a good reason."

                                y "When did this happen, exactly?"

                                t "A couple of minutes before you fell in my hole."
                                t "My magic alarm went off."

                                t "So I had to abandon both my post and my super important personal reasons for you."
                                t "So in a way, this is all your fault, and I'm the one helping you out of trouble!"
                                y bored"Really?"
                                t "{i}*sigh*{/i}"
                                t "I know, sounds too stupid to even joke about that."

                                un bored"Ok, I'm pretty sure he was guarding my door."
                                "That's my theory too."
                                "So the Headmaster knew about the door..."
                                un curious"I wonder who was supposed to come along to relieve the cat from guarding."

                                t "Now you see how it was unfair?"

                                y simple"..."
                                y "Yes?"

                                t "You don't..."
                                y bored"I don't."

                                t "Aghh!"
                                t "The point was that I had no business guarding a dumb door at that time!"
                                t "It was just unfortunate timing, anyone could've been put in that position if they were around."
                                t "Instead, they had to make the one person who's too busy to guard a door do the job."
                                y simple"What were you busy with?"
                                t "That's... a secret."

                                t "Anyway, when I came back, the Headmaster was furious and the door wasn't there anymore."
                                t "I mean, how was I supposed to know someone was going to steal the whole room away?!"
                                t "To be fair, if he told me to guard it so the door wouldn't go anywhere, I would've left my post even faster."
                                t "And probably called the psychic ward..."



                                menu:
                                    "Was it his fault for getting in this mess?"

                                    "You're innocent.":
                                        $ Tate_points+=1

                                        Y s"You're right, you shouldn't have been punished for something that's barely your fault."
                                        y "Students were supposed to be gathered in the auditorium at that time anyway, so technically, the Headmaster broke the rules too by keeping you there."

                                        t "Yeah!"
                                        t "That made HIM late for the gathering too!"
                                        t "I'm glad you understand."
                                        jump tatetalkk

                                    "The punishment fits the crime.":

                                        Y simple"The Headmaster gave you an order, I know it might sound unfair, but once he said it, you should've done as told."
                                        t "You sound like Dallan right now..."
                                        t "Let's all commit sudoku on the Headmaster's order, because he is God!"
                                        y bored"You mean seppuku?"
                                        t "Same thing."
                                        jump tatetalkk


                                        label tatetalkk:
                                            y s"..."
                                            t "...."
                                            y simple"......"
                                            t "Hey... how long have we been wandering through the hallways?"
                                            y "About twenty minutes..."
                                            t "And how many people have we seen so far?"
                                            y "..."
                                            y bored"Zero."

                                            t "Bend me over and fuck me sideways..."

                                            y blush"What?"
                                            y "Right now?"

                                            t "Figure of speech."

                                            y simple"oh."
                                            y pf"What does it mean?"
                                            t "It means {i}'I can't believe this crap'!{/i}"




                                            t "Maybe he was right... maybe this is just futile..."
                                            "My mind goes back to the Headmaster's handsome, smug face."
                                            "For some reason, it was making me a little mad."
                                            y determined"Oh no, he's not right."


                                            y "Let's quicken the pace."
                                            y "We're finding someone, no, everyone, and filling up that list!"
                                            "This is the perfect time to use one of my support abilities."

                                            "Speed boost."

                                            "Will it work on a broom?"
                                            "Let's find out!"

                                            scene chibitatefast with dissolve

                                            t "Woah, what's happening?"
                                            t "I'm putting the same amount of magic into flying but we're going twice as fast!"
                                            t "This would be so cool if I wasn't able to do that on my own!"


                                            un bored"Love interest impressed semi-successfully."
                                            "Don't just stand there making sarcastic comments, do something to help!"
                                            un curious"What do you want me to do?"
                                            "I don't know, search the area and find traces of organic life then guide me to them?"
                                            "Just a thought."
                                            un eyeroll"Ughh, fiiiiine, I'll help you get your pussy out of detention."
                                            un "You're lucky I'm good at spells like that, {size=20}and that is a pretty smart suggestion...{/size}"
                                            un "Here, X-Ray vision to see all forms of life."

                                            "Eww, that's a lot of rats in the walls."
                                            un bored"Those are insects, actually."
                                            y scream"EWWWWWW!" with hpunch

                                            t "Huh, what's wrong?"

                                            y awkward"I-I mean, Yeeeey!"
                                            y "This is really fun! Hey! Why don't we check that classroom at the end of the hall?"
                                            y "I have a good feeling about that room in particular."
                                            stop music fadeout 3.0

                                            t "Ok?"

                                            t "And people say I'm the weird one..."
                                            scene hallway20 with longdissolve

                                            "I step off the broom and get to the door, realizing only now that I'm back on my feet that I'm tired..."
                                            "Fatigued even."
                                            "My legs are shaking and I just can't catch my breath."
                                            "Why the hell did this happen?"
                                            un "You enchanted a magical object with a speed boost that's meant for people, dipshit."
                                            un "You also made me cast a somewhat power hungry spell."
                                            un "I was going to say something, but I thought maybe you have some special abilities under your sleeves."
                                            "Damn it..."

                                            scene classroom2 with llongdissolve
                                            play music "audio/bread.ogg" fadein 3.0
                                            "I drag myself to the door and we enter the classroom I so randomly picked out."
                                            show cat21simple at right with moveinright

                                            "Inside are five people playing a tabletop game around a large table."
                                            "They are all petrified in place by our sudden appearance."


                                            show dogsur zorder 2 with moveinleft
                                            "A small dog with round glasses and high-waisted pants."
                                            show bun at left4 zorder 1 with moveinleft
                                            "A ginger rabbit with a bowl cut."
                                            show fenecsur at left2 with moveinleft
                                            "A chubby fennec in suspenders."
                                            show goatsur at left with moveinleft

                                            "A tall but sheepish looking goat."
                                            show carsur at left5 with moveinleft
                                            "And last but probably also least: a very awkward caracal."

                                            "Even with the lack of energy, the adrenaline still made me open up the door a little too fast and too hard, startling everyone in the room, including Tate."
                                            t "..."
                                            y tired"{i}*Heavy breathing*{/i}"

                                            st1 "..."
                                            st2 "..."
                                            st4 "Hi?"
                                            t "Hey."
                                            y tired"h-ha...{i}*huff*{/i}"
                                            st5 "..."
                                            un "Seven people in a room now awkwardly stare at each other."
                                            un "Everyone waiting for the initiator to explain why the two new arrivals are here."
                                            un "...That's you, you're the initiator."
                                            un ang"SO HURRY UP!"
                                            st3 "Youuu... wanna play {b}Nuts & Nightfallen{/b} with us?"


                                            t "What is this place?"
                                            t "Are you like a club or something?"
                                            st2 "huh?"
                                            hide dogsur zorder 2
                                            show dog zorder 2
                                            hide bun at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenecsur at left2
                                            show fenec at left2
                                            hide goatsur at left
                                            show goat at left
                                            hide carsur at left5
                                            show car at left5





                                            st2 "Oh, yeah, well, not really, we gather once a week and play N&N together."
                                            st5 "It's usually on Sunday, but that test will ruin our plans, so we're doing it early."
                                            t "What's 'Nuts & Nightfallen'?"
                                            st4 "It's kinda like a high fantasy, action packed dating sim."
                                            t "Sim?"
                                            st5 "Simulator, it's an imagination game."
                                            t "You're {i}'pretending'{/i} to go on dates?"
                                            st1 "Super cool dates!"
                                            st2 "I'll be married to a dragon this session if everything goes well!"
                                            hide cat21simple
                                            show cat21bored at right
                                            t "Wow..."
                                            st4 "Isn't it cool?"
                                            y "{i}*huff huff*{/i}"

                                            ben "I'm Benjie, by the way."
                                            "Says the little dog."
                                            goo "M' name's Goolie!"
                                            "Exclaims the fennec excitedly."
                                            ap "Apollo...hi."
                                            "Za goat tells us."
                                            cal "Uhmm, Cal...I-I'm Cal."

                                            "The feline spoke."

                                            go "I'm Godwin the Third."
                                            "The rabbit says with a slight sickly rasp in his voice and sniffling his nose."
                                            hide cat21bored
                                            show cat21simple at right
                                            t "Cool name, do you not shorten it to anything?"
                                            go "No."
                                            t "Awesome."
                                            t "Who named you?"
                                            go "It's like, an homage to my great-grandfather that died in the war, or something."
                                            go "I don't know, I never really cared for family drama."
                                            t "Sick...I should take notes..."
                                            t "You're all already friends on the first day?"
                                            ap "We're High School friends."
                                            ap "We all wanted to and managed to get into the academy, thankfully."
                                            cal "Well...not Zibby."
                                            ben "Yeah...RIP Zibby..."
                                            t "I'm sorry for your loss."
                                            ben "Oh no, he's not dead, he's just not into the whole sex concept of the job."
                                            go "He wants to be a heart surgeon."

                                            t "Ah, that type of guy."
                                            go "His parents are kind of disappointed in him too."


                                            goo "We've created a secret society among ourselves."
                                            goo "We mostly just hang out and play games."


                                            ben "We call ourselves the E.F.D."
                                            t "E. F. D?"
                                            ben "Ears For Days!"

                                            "They all do a synchronized head shake to show off their big, floppy ears."

                                            t "That's actually kinda cute."

                                            goo "Thank you!"

                                            t "So... you're a bunch of weird nerds playing horny games?"
                                            ap "Uhm, we prefer the word geeks."

                                            un squint"Not the loser pronouns..."




                                            go "We're looking for more members at the moment."
                                            ben "Care to join?"


                                            t "I always wanted to try N&N ever since I found out about it two minutes ago, but I don't have any nerd friends, so I don't know..."
                                            goo "We have snacks."
                                            hide cat21simple
                                            show cat21smile at right
                                            y tired"{i}*huff huff*{/i}"

                                            t "Well why didn't you say so? What kind?"

                                            cal "Fips."
                                            hide cat21smile
                                            show cat21simple at right
                                            t "What the hell are those?"
                                            t "Let me try."

                                            ap "Fish flavored Chips."
                                            hide cat21simple
                                            show cat20angry at right

                                            t "Ew, what the fuck?"

                                            t "Who... what...why... that's atrocious!"
                                            goo "I like them..."
                                            hide cat20angry
                                            show cat21bored at right
                                            t "Whatever, tasteless nerds or not, you are first years, so I highly suggest you stop messing around and go explore the campus a little."
                                            t "You can play games later."
                                            hide dog zorder 2
                                            show dogsur zorder 2
                                            hide bun at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenec at left2
                                            show fenecsur at left2
                                            hide goat at left
                                            show goatsur at left
                                            hide car at left5
                                            show carsur at left5

                                            un"This cat being the voice of reason?"
                                            un"Incredible."

                                            cal "B-but we can't leave now!"
                                            go "Lord Bergamuhz just got resurrected!"
                                            ap "If we don't stop him now, he will destroy the world!"
                                            ben "If we don't defeat him I can't have a dragon husband!"
                                            hide cat21bored
                                            show cat21simple at right

                                            t "That does sound pretty serious..."
                                            t "Well, we don't want to stand between you and the end of the world..."
                                            t "Or laying with a dragon."

                                            y tired"W-wait..."
                                            y "{i}*huff*{/i}, sign... sign."

                                            t "What?"
                                            t "Sign?"

                                            y "L-list, give them the list."

                                            t "What li-"
                                            t "Ooooh, strudels, I already forgot!"
                                            stop music
                                            hide cat21simple with moveoutright

                                            "Damn you and your high energy body."
                                            play music "audio/funk.ogg" fadein 2.0 volume 0.4

                                            show cat20glasses at right with moveinright

                                            "The cat puts on a pair of sunglasses found on the strangers' table and all of a sudden, the whole atmosphere changes."



                                            t "Aghem."

                                            t "Listen here nerds!"

                                            ap "Geeks."

                                            t "We'll get to {i}'losers'{/i} if you say that again!"
                                            t "First off."


                                            t "I'd say it's nice to meet you all, but I don't want to get attached, since you're not going to last long this way."
                                            "They seem concerned, I mean, he did just tell them they'll die soon, so..."
                                            t "I'll have to be honest."
                                            t "I've been sent by the higher ups to deliver you the bad news."
                                            ap "The higher ups?"
                                            go "The seniors?"
                                            t "Sure, them."
                                            cal "Well what is it?!"
                                            goo "Do you think it's Monty?"
                                            ben "I already gave him my lunch money."
                                            cal "Me too..."
                                            go "I think I forgot..."
                                            ap "Damn it dude, we're gonna get water ballooned for this..."
                                            goo "Sorry."

                                            t "Shut up and listen up!"

                                            t "Here's the thing."
                                            t "You all look scrawny, pathetic and overall beaten up by life itself."

                                            goo "Hey!"

                                            ben "No no, he's right."

                                            goo "oh..."
                                            hide dogsur zorder 2
                                            show dogsad zorder 2
                                            hide bun at left4 zorder 1
                                            show bunsad at left4 zorder 1
                                            hide fenecsur at left2
                                            show fenecsad at left2
                                            hide goatsur at left
                                            show goatsad at left
                                            hide carsur at left5
                                            show carsad at left5

                                            t "You have no fashion sense, consume the worst snack brands and you STINK of masturbation lotion!"
                                            t "And not the good kind..."
                                            t "On top of that, you are wasting a perfectly good day, one of the most exciting day of your lives mind you!"
                                            T "You are all a bunch of disappointments, that are fated to die alone!"
                                            y simple "Where is this going?"
                                            stop music fadeout 2.0

                                            un "I think he just wants to insult them."


                                            "They stand in silence for a second, looking stunned at the cat and his harsh words."
                                            hide dogsad zorder 2
                                            show dogcry zorder 2
                                            hide bunsad at left4 zorder 1
                                            show buncry at left4 zorder 1
                                            hide fenecsad at left2
                                            show feneccry at left2
                                            hide goatsad at left
                                            show goatcry at left
                                            hide carsad at left5
                                            show carcry at left5




                                            "But instead of cries of protests, the guys in front of us shed actual tears."
                                            "I'm more surprised by their coordinated emotions than the actual outburst."
                                            "Not to mention thankful that the funky rock was cut by the sudden silence."

                                            play sound "audio/wack2.ogg"

                                            cal "HOW DOES HE KNOW?!" with hpunch
                                            play sound "audio/wack2.ogg"

                                            goo "THAT SUMS UP MY WHOLE LIFE!"
                                            play sound "audio/wack2.ogg"
                                            go "I JUST WANT A GIRLFRIEND!"
                                            play sound "audio/wack2.ogg"
                                            cal "DAMN YOU MONTY AND YOUR PERFECT SEX LIFE!"
                                            play sound "audio/wack2.ogg"
                                            ben "WHAT CAN WE DO, MISTER PURPLE CAT?!"
                                            play sound "audio/wack2.ogg"

                                            goo "I DON'T WANNA DIE ALONE!"

                                            t "Do not fret, I was once just like you!"
                                            hide dogcry zorder 2
                                            show dogsad zorder 2
                                            hide buncry at left4 zorder 1
                                            show bunsad at left4 zorder 1
                                            hide feneccry at left2
                                            show fenecsad at left2
                                            hide goatcry at left
                                            show goatsad at left
                                            hide carcry at left5
                                            show carsad at left5

                                            go "Really?!"
                                            goo "But you look so cool!"
                                            goo "With those extravagant clothes and sunglasses."
                                            hide cat20glasses
                                            show cat20glassesmad at right
                                            play music "audio/bread.ogg" fadein 3.0

                                            t "HEY!" with hpunch
                                            t "Do I look like a liar to you?!"
                                            hide dogsad zorder 2
                                            show dogside zorder 2
                                            hide bunsad at left4 zorder 1
                                            show bunside at left4 zorder 1
                                            hide fenecsad at left2
                                            show fenecside at left2
                                            hide goatsad at left
                                            show goatside at left
                                            hide carsad at left5
                                            show carside at left5

                                            "They exchange unsure glances through their previous tears of realization."

                                            cal "no...?"
                                            hide cat20glassesmad
                                            show cat20glasses at right

                                            t "Exactly, so listen close."
                                            hide dogside zorder 2
                                            show dog zorder 2
                                            hide bunside at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenecside at left2
                                            show fenec at left2
                                            hide goatside at left
                                            show goat at left
                                            hide carside at left5
                                            show car at left5

                                            "The five guys lean in and listen carefully to the cat, who's spouting empty but attention catching words from start to finish...."

                                            t "Everything can change!"
                                            t "And I'm here to do just that."

                                            t "Now tell me, how many of you are first years, precisely?"
                                            hide dog zorder 2
                                            show doghand zorder 2
                                            hide bun at left4 zorder 1
                                            show bunhand at left4 zorder 1
                                            hide fenec at left2
                                            show fenechand at left2
                                            hide goat at left
                                            show goathand at left
                                            hide car at left5
                                            show carhand at left5

                                            "All of them, except the caracal, raise their hands."
                                            "He looks around like he had committed a crime as he notices the other's raised hands."
                                            hide cat20glasses
                                            show cat20bored at right

                                            t "The boss lowers his sunglasses."

                                            y bored"Are you talking to yourself now?"

                                            hide doghand zorder 2
                                            show dogsur zorder 2
                                            hide bunhand at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenechand at left2
                                            show fenecsur at left2
                                            hide goathand at left
                                            show goatsur at left

                                            t "He approaches the unsuspecting feline."


                                            show dogsur at left2 zorder 2 with move

                                            show bun at left2 zorder 1 with move

                                            show fenecsur at left5 with move

                                            show goatsur at left5 with move
                                            show cat20bored at center zorder 1 with ease



                                            show carhand at left4 zorder 2 with move

                                            "The others take a couple of steps back, leaving the poor caracal just inches away from the crazy cat."
                                            t "With his... knitted sweater and nervous pose."
                                            t "He still sees himself as a mighty predator, doesn't he?"

                                            cal "N-no s-sir."

                                            t "Then tell me, what year are you supposed to be in?"


                                            show carblush1 at left4 zorder 2

                                            cal "I-I... uhm, second year?"
                                            cal "And part of the Defender's Shard..."
                                            hide carblush1 zorder 2
                                            t "HA!"

                                            t "I see..."
                                            "Tate holds the poor boy's chin and inspects his head on all sides, letting go a second after, unimpressed."
                                            show cat20bored at right zorder 1 with ease

                                            t "I'll come back to you..."
                                            show carhand at left5 zorder 2 with move

                                            t "Now, how many of you possess magical abilities?"

                                            show dogsur at center zorder 2 with move

                                            show bun at left4 zorder 1   with move

                                            show fenecsur at left2   with move

                                            show goatsur at left with move

                                            hide dogsur zorder 2
                                            show doghand zorder 2
                                            hide bun at left4 zorder 1
                                            show bunhand at left4 zorder 1
                                            hide fenecsur at left2
                                            show fenechand at left2
                                            hide goatsur at left
                                            show goathand at left
                                            hide carsur at left5
                                            hide carhand
                                            show carhand2 at left5

                                            "All of them raise their hands, and the caracal relaxes for the moment."

                                            t "Good."

                                            t "And how many of you are members of the Sorcery Shard as of today?"

                                            hide doghand zorder 2
                                            show dogsad zorder 2
                                            hide bunhand at left4 zorder 1
                                            show bunsad at left4 zorder 1
                                            hide fenechand at left2
                                            show fenecsad at left2
                                            hide goathand at left
                                            show goatsad at left
                                            hide carhand2
                                            show carsad at left5

                                            "Nobody raises anything."

                                            hide dogsad zorder 2
                                            show dogsur zorder 2
                                            hide bunsad at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenecsad at left2
                                            show fenecsur at left2
                                            hide goatsad at left
                                            show goatsur at left
                                            hide carsad at left5
                                            show carsur at left5

                                            hide cat20bored
                                            show cat20glassesmad at right with hpunch

                                            "Tate slams the table with his hands, leaning in and scaring everyone again."

                                            t "HERE IS YOUR FIRST MISTAKE!"
                                            t "You're all wasting their efforts and abilities."

                                            hide dogsur zorder 2
                                            show dogsad zorder 2
                                            hide bun at left4 zorder 1
                                            show bunsad at left4 zorder 1
                                            hide fenecsur at left2
                                            show fenecsad at left2
                                            hide goatsur at left
                                            show goatsad at left
                                            hide carsur at left5
                                            show carsad at left5

                                            ap "T-their?"
                                            t "YOUR PARENTS'!"
                                            t "SOCIETY'S!"
                                            t "MONTY'S!"
                                            goo "NOT MONTY!"
                                            hide cat20glasses
                                            show cat20glassesmad at right

                                            t "How can you ever look any of them in the eyes while defaming their legacy?"
                                            t "You're playing a fantasy game, about being superhero adventurers, but you do not realize..."
                                            t "YOU CAN BE THAT IN REAL LIFE!"
                                            t "Don't you want to achieve that goal?"
                                            t "Don't you wanna fuck a dragon in real life?"
                                            ben "HELL YEAH!"
                                            t "And possibly get normal partners along the way as well?"
                                            "They slowly nod."



                                            t "And how are you going to stop being losers if you don't learn to touch grass and use your best weapons against Nightfallen?"
                                            t "Magic!"
                                            hide dogsur zorder 2
                                            show dogcry zorder 2
                                            hide bun at left4 zorder 1
                                            show buncry at left4 zorder 1
                                            hide fenecsur at left2
                                            show feneccry at left2
                                            hide goatsur at left
                                            show goatcry at left
                                            hide carsur at left5
                                            show carcry at left5

                                            "So far, he managed to make three of them cry twice and one of them vibrate with the prospect of courting a dragon."
                                            un "I thought these were considered 'adults' in your kind."
                                            "They... are."
                                            un "Fascinating."

                                            goo "{i}*sob*{/i} I want-{i}*sob*{/i} I want to join the Sorcery Shard..."

                                            t "You... you want to join?"
                                            "Most of them nod vigorously."
                                            hide cat20glasses
                                            show cat20glassesmad at right
                                            t "There we go, CHANGING OUR MINDS, HUH?!"
                                            t "A LITTLE LATE FOR THAT!"
                                            "What is he doing?"
                                            ben "L-late?"
                                            hide cat20glassesmad
                                            show cat20glasses at right
                                            t "I don't even know what to say, the demand is pretty high, you have to be really lucky to get in at this point..."
                                            cal "But... it's only been a day and-"
                                            t "THAT'S TOO LATE!"
                                            t "People got in line months ago!"
                                            ben "Please mister cat! I need to get in!"
                                            go "I can't afford to bring shame on my family's name!"
                                            goo "I want to have super cool magical adventures in real life!"

                                            ap "I want to impress cute girls with my magic!"
                                            ben "I want to impress cute {b}guys{/b} with my magic!"
                                            hide dogcry zorder 2
                                            show dogsad zorder 2
                                            hide buncry at left4 zorder 1
                                            show bunsad at left4 zorder 1
                                            hide feneccry at left2
                                            show fenecsad at left2
                                            hide goatcry at left
                                            show goatsad at left
                                            hide carcry at left5
                                            show carsad at left5

                                            hide cat20glasses
                                            show cat21bored at right



                                            t "{i}*sigh*{/i}, fine, I'll see what I can do."

                                            t "Here, sign your name on this list and I might be able to convince the leader of the Sorcery Shard to let you in."
                                            t "Although it's not a promise."
                                            t "And you'll owe me after this."

                                            hide dogsad zorder 2
                                            show dogsmile zorder 2
                                            hide bunsad at left4 zorder 1
                                            show bunsmile at left4 zorder 1
                                            hide fenecsad at left2
                                            show fenecsmile at left2
                                            hide goatsad at left
                                            show goatsmile at left
                                            hide carsad at left5
                                            show carhand at left5

                                            goo "THANK YOU!"
                                            show fenecsmile at right2 with move
                                            ap "WE ARE SO GRATEFUL!"
                                            show fenecsmile at left2 with move
                                            show goatsmile at right2 with move

                                            ben "WE'RE IN YOUR DEBT!"
                                            show goatsmile at left with move
                                            show dogsmile at right2 with move
                                            go "LONG LIVE OUR PURPLE KING!"
                                            show dogsmile at center with move
                                            show bunsmile at right2 with move

                                            "The four first years sign our list."
                                            show bunsmile at left4 with move
                                            "I'm just standing there, flabbergasted..."
                                            un "I'm surprised as well."
                                            un "He's REALLY good at manipulating, which I thought was MY area of expertise."
                                            un "Even if those five seem dumber than freshly birthed cubs."
                                            un "Aren't 'nerds' supposed to be highly intelligent?"
                                            "Smart, not wise."
                                            un bored"Ah, that explains the whole 'you' situation..."
                                            "What's that supposed to mean?"
                                            un "You know."
                                            "..."

                                            un "Maybe hanging around this cat won't be as bad as I thought."
                                            hide cat21bored
                                            show cat21mad2 at right
                                            y awkward"W-well, glad we got all of that sorted out, I guess we'll see you all at the auditions."
                                            y "Come on, Tate, let's go and-"
                                            t "Hold on."
                                            hide dogsmile zorder 2
                                            show dogsur zorder 2
                                            hide bunsmile at left4 zorder 1
                                            show bun at left4 zorder 1
                                            hide fenecsmile at left2
                                            show fenecsur at left2
                                            hide goatsmile at left
                                            show goatsur at left


                                            "Tate stares at the caracal with squinted eyes."
                                            "At least I'm assuming that's what they'd look under the glasses."

                                            hide dogsur with moveoutleft

                                            hide bun with moveoutleft

                                            hide fenecsur with moveoutleft

                                            hide goatsur with moveoutleft

                                            t "You."
                                            show cat21mad2 at center with move

                                            "The others, once again leave space for the two of them."
                                            cal "M-me?"

                                            t "Why aren't you signing?"





                                            cal "I-I'm in my second year."
                                            hide cat21mad2
                                            show cat21simple
                                            t "Did I stutter?"
                                            t "Did... did anyone hear me stuttering?"
                                            t "Do I have a stuttering problem, by any chance?"
                                            t "A-a-are m-my wo-words get-getting t-tangled b-be-before they c-come out?"
                                            hide cat21simple
                                            show cat21mad2
                                            "The other four shake their heads frantically."

                                            t "Come closer."

                                            show carhand at left with move
                                            cal "..."

                                            t "Closer."
                                            show carhand at left2 with move

                                            t "When was the last time you had sex, son?"
                                            "Son...?"
                                            cal "I..."
                                            show cat21mad2 at right2 with ease


                                            t "When was the last time you grabbed a piece of ass and really just buried your face in that thing and went-"
                                            hide cat21mad2
                                            show cat21brr at right2
                                            t"{i}BRRRRRRR{/i}!"
                                            cal "Uhmmm..."
                                            hide cat21brr
                                            show cat21bored at right2
                                            hide carhand
                                            show carblush1 at left2

                                            cal "{size=20}I-I'm kind of a vn....{/size}"
                                            t "What was that?"
                                            cal "I'm sorta of a vgin...."
                                            hide cat21bored
                                            show cat21mad2 at right2
                                            t "I CAN'T HEAR YOU!"
                                            hide carblush1
                                            show carblush2 at left2
                                            cal "I'M A VIRGIN!"

                                            t "..."
                                            t "I see."
                                            hide carblush2
                                            show carblush3 at left2
                                            t "Come here."
                                            show cat21mad2 at right with move
                                            show carblush3 at center with move

                                            "He guides the guy with a hand on his back, the difference in height is hilarious compared to the power dynamic."
                                            "Tate brings him two feet in front of me."
                                            t "Look at this guy, do you think he's hot?"
                                            y "Huh?"

                                            cal "Y-yeah?"

                                            t "Would you fuck him?"

                                            y blush2"What the hell?"
                                            cal "Yes."

                                            un bored"Wow, no hesitation."
                                            un "Good for you I guess."

                                            t "Give him a kiss then, right here, right now."
                                            hide carblush3
                                            show carblush2

                                            "The caracal looks back at his fellow ner-"
                                            "I mean geeks, that are all giving him the thumbs up."
                                            "Is nobody gonna ask my opinion???"
                                            "He takes a deep breath, then-"
                                            hide carblush2 with dissolve
                                            show carkiss with dissolve

                                            "Leans forward with his eyes closed and lips at the ready."

                                            un scared"Dodge!"
                                            show carsur
                                            hide carkiss with hpunch
                                            play sound "audio/falling.ogg"




                                            "I practically jump backwards, hitting the floor."
                                            hide carkiss
                                            show carsur with hpunch

                                            y blushmad"What the ACTUAL fuck?!"

                                            "I thought they were joking!"

                                            t "YOU SEE THAT?!"

                                            t "See how disgusting you are?"
                                            t "He would've accepted the kiss, and maybe even gone on a date with you after, IF you had accomplishments inside the Sorcery Shard!"
                                            t "Instead of wasting your time in whatever other, inferior Shard you chose."
                                            hide carsur
                                            show carblush3

                                            cal "I-is that true?"
                                            "He stares at me with wide eyes."

                                            menu:
                                                "Uhmmmm...."
                                                "Yes.":
                                                    jump yeskiss
                                                "Nope.":
                                                    jump nokiss
                                                "I would date you anywhere, anytime, hot stuff~":
                                                    jump hotkiss

                                            label yeskiss:


                                            y simple"Ermm, yes?"
                                            scene classroom2
                                            show cat21bored at right
                                            show carsmile


                                            cal "Hell yeah..."
                                            jump afternerdkiss
                                            label nokiss:
                                            y bored"No way..."
                                            scene classroom2
                                            show cat21bored at right

                                            show carsad
                                            "He seems disappointed."
                                            t "Of course he says that now!"
                                            t "You are so pathetic that he doesn't believe in your abilities at all!"
                                            t "You gotta show him you can do it!"
                                            hide carsad
                                            show carsmile
                                            cal "Y-yeah, yeah, you're right!"
                                            cal "I'll impress him!"
                                            cal "I'll impress everyone!"
                                            cal "I'll get all the ass!"
                                            "Tate gives me a side eye for almost ruining his manipulation attempt."
                                            jump afternerdkiss
                                            label hotkiss:
                                            scene classroom2
                                            show cat21bored at right
                                            show carblush3

                                            y smug"Hell yeah, hot stuff~"
                                            y "I only jumped out of surprise."
                                            y "In fact, how about we get out of here right now and make out somewhere private."
                                            y "And maybe I can even give you a taste of something else as well."
                                            "The feline blushes heavily before Tate intervenes."
                                            hide cat21bored
                                            show cat21mad2 at right

                                            t "Hahaha."
                                            hide cat21mad2
                                            show cat21mad at right
                                            t "HA!"
                                            t "See how he's mocking you?"
                                            t "He's making fun of you!"
                                            hide carblush3
                                            show carsad
                                            cal "Oh...of course."
                                            hide cat21mad
                                            show cat21smug at right
                                            t "But you can show him you're good enough to be made out with."
                                            t "And maybe more."
                                            t "You just have to sign."
                                            hide carsad
                                            show carsmile
                                            "The cat's words are making these guy's ears work like a roller-coaster the whole time, going up, down, making loops of excitement."
                                            "At his final statement, they remain raised high, twitching lightly."
                                            jump afternerdkiss




                                            label afternerdkiss:
                                            scene classroom2
                                            show cat21smug at right
                                            show carsmile
                                            show carsmile at right2 with move

                                            "He walks towards Tate, holding the list and signs."
                                            show carsmile at center with move
                                            cal "I'm going to quit the Defender's Shard right now!"

                                            t "Yeah, that's the spirit!"
                                            "The other nerds cheer as well."
                                            t "Good job!"

                                            t "Don't forget to come back for this beast when you've defeated a thousand Nightfallen with your magic!"
                                            show cat21smug at right with hpunch
                                            "He slaps my back a few times."
                                            y simple"ow."
                                            "Tate collects the list with five more signatures now on it."

                                            show cat21fire at right with dissolve
                                            hide cat21smug
                                            t "Pleasure doing business with you boys, and don't forget, the secret to having bitches is cool magic."
                                            "He shoots out some mini fireworks from his fingertips, at which they applaud."
                                            show dogsur at left with moveinleft
                                            ben "Wait!"
                                            ben "You never told us your name!"

                                            t "My name...?"
                                            t "Heh."
                                            hide cat21fire with moveoutright
                                            stop music fadeout 2.0
                                            t "Just call me Master."

                                            scene hallway20 with longdissolve
                                            show cat20ec with moveinleft
                                            play music "audio/happy2.ogg"


                                            "Finally, we get to leave the room, with half the list filled and five nerds left in awe."

                                            show list2 with dissolve

                                            y simple"Wow."
                                            t "I know, I'm awesome, aren't I?"
                                            hide list2 with dissolve

                                            y bored "I can't believe you whored me out like that."
                                            hide cat20ec
                                            show cat20smug

                                            t "Ah, that...well, you can't bake a cake without breaking a few eggs, or something like that."
                                            t "But come on, you were impressed, admit it."

                                            y pf"Ok, ok, it was pretty cool seeing you manipulate the insecurities of a group of young adults, I admit."

                                            y simple"Now I'm surprised you didn't finish that list sooner."

                                            t "We can call this teamwork, after all, I wouldn't have known there are people just chilling in a random classroom if it weren't for you."
                                            hide cat20smug
                                            show cat20simple
                                            t "Seriously, on the first day?"
                                            t "I'll never understand nerds."
                                            y "Me neither."
                                            un "Aren't you a nerd too?"
                                            un "I can see some memories of you being {i}preeeetty{/i} excited about a poetry grade."
                                            un simple"Oh, and here is you crying over a 97 percent on an Algebra test just two years ago!"
                                            "Stop going through my brain..."
                                            "I was... a cool nerd?"
                                            un bored"Yeah, sure."
                                            t "How'd you do it?"

                                            y "Hm?"

                                            t "Knowing where they were, how'd you know?"

                                            y "I have good hearing."
                                            y "Or instincts?"


                                            t "Hmmm... Alright, I'll buy that excuse for now."
                                            t "Even if it's total bs."
                                            t "But I'll require a more detailed explanation in the future."
                                            hide cat20simple
                                            show cat20smile

                                            t "Do you have any more ultra instincts up your sleeve to find people?"

                                            "I look around, just as a somewhat familiar black panther comes around the corner."

                                            y s"I don't think we'll need any."
                                            hide cat20smile
                                            show cat20smileright
                                            y "Look."

                                            y "It doesn't seem like he spotted us yet."
                                            t "Isn't that one of the recommended students, what's his face?"
                                            t "I think it was Kale?"
                                            y confused"What? No."
                                            y "That was so wrong it's not even funny."
                                            y "It's Coal."

                                            t "Ooooh, I really really want to get him!"
                                            t "Merina would be so happy!"

                                            y simple"Then let's make a plan before we approach him."


                                            t "He looks a little lost..."
                                            hide cat20smileright
                                            show cat20smug
                                            "Tate grins widely."
                                            t "Do we dare?"

                                            y "Dare what?"

                                            t "Scam him."

                                            y worried"No! Tate, no!"

                                            t "Why nooot?"

                                            t "He for SURE has a ton of magic, and he looks nice enough to be an easy target, kind of like you, AND if we get him, Merina would be super impressed with me."

                                            menu:

                                                "Should we scam him for an easy signature or risk losing him?"

                                                "No way...":
                                                    jump noscam

                                                "Fine...":

                                                    jump scam


                                            label scam:

                                            play music "audio/catjazz.ogg" fadein 4.0

                                            y bored"Fine, let's not risk it, we do need that signature."

                                            t "Yeah!"
                                            hide cat20smug with moveoutright
                                            t "And if anything goes south, we can play it off as a joke."

                                            scene hallway20 with dissolve
                                            "We walk towards the lost panther wearing a worried face."
                                            show coalnoworry at left2 with moveinleft
                                            y "Hi there."
                                            show cat20smile at right2 with moveinright
                                            t "Hey!"

                                            co "Oh, hello."
                                            show coalnosimple at left2
                                            hide coalnoworry
                                            y "Do you need any help? You seem lost."
                                            co "No thank you, I'm fine, I was just waiting for someone, but they're a little late."
                                            t "Are you perhaps a first year?"
                                            hide coalnosimple
                                            show coalno at left2
                                            co "I am, how'd you know?"
                                            co "Am I that obvious?"

                                            t "I don't see a badge on you and first years are usually the ones that look the most confused."

                                            co "Makes sense."
                                            t "Have you joined the Shard yet?"
                                            hide coalno
                                            show coalnosimple at left2

                                            co "{i}'The'{/i} Shard?"
                                            co "Don't you mean {i}'a'{/i} Shard?"

                                            y "No, you see, as a first year, you HAVE to join the Sorcery Shard."
                                            hide cat20smile
                                            show cat20smug at right2
                                            t "Yep, it's a rule."
                                            y "You can switch out later."

                                            co "I didn't know that."
                                            t "Don't worry, this guy is a recommended student and even he didn't know."
                                            hide coalnosimple
                                            show coalno at left2
                                            co "Hey, I'm a recommended student as well!"
                                            y smug"You don't say!"

                                            un "Abort, abort!"
                                            "What's wrong?"
                                            un "This guy has no magic, I sense NOTHING coming from him."
                                            "Shit..."
                                            "I should bring this up then."

                                            y s"There is just one little thing we need to know before you can join."
                                            y "Do you perhaps have any cool magic to show us?"

                                            co "Unfortunately, I have no magic."

                                            hide cat20smug
                                            show cat21bored at right2

                                            t "Rats..."
                                            t "Waste of time."
                                            un "Hold up, I sense a strong aura, but it's coming from behind him."
                                            un "Perhaps he's hiding a very small magical person in his back pocket."
                                            "I start circling him slowly, and sure enough, behind him, perhaps not a person, but against the wall sits a prism shaped device."
                                            un "That's it! That thing looks powerful."
                                            un "I bet it's super magical."
                                            "Yet another conversation topic."
                                            y "Hey what's that?"
                                            hide cat21bored
                                            show cat20simple at right2
                                            show coal at left2 with dissolve
                                            hide coalno


                                            y "It looks pretty magical to me."
                                            co "Oh, that? It's my-"
                                            hide cat20simple
                                            show cat20 at right2
                                            t "Ooh, let me see!"
                                            show cat20 at left4 with move
                                            hide coal
                                            show coalnoworry at left2
                                            show cat20 at right2 with move
                                            "The cat takes it out of Coal's hands with great force, which scares him a lot, for good reason."

                                            co "B-be careful with it, please."
                                            co "In fact, why don't you just give it back to-"
                                            hide cat20
                                            show cat20simple at right2

                                            show coalnoworry at center with ease
                                            t "Oops..."

                                            "{i}Autodestruction sequence initialized...2... minutes remaining.{/i}"
                                            un "Oh, you little fool."
                                            hide coalnoworry
                                            show coalnosimple at center
                                            show coalnosimple at right2 with move
                                            hide coalnosimple
                                            show coalsimple at right2
                                            show coalsimple at left2 with move
                                            "Coal snatches it out of his hands and starts to disassemble it on the ground."
                                            hide cat20simple
                                            show cat21scared at right2
                                            show cat21scared at right with ease

                                            t "I think I'll telepo-"
                                            "I grasp his shoulder and hold him in place."
                                            y pf"Don't even think about it, we're seeing the end of it."

                                            "We watch Coal with held breaths as he unscrews some bolts and presses some buttons."
                                            "Thankfully, he manages to shut his device off after a few agonizing moments."

                                            "{i}Reset initialized.{/i}"


                                            "{i}Time remaining, 28 hours, 21 minutes.{/i}"

                                            co "Great..."
                                            hide cat21scared
                                            show cat21simple at right2


                                            y worried"I am SO sorry, Coal!"
                                            y "We shouldn't have touched your thing."
                                            show coalsadsmile at left2
                                            hide coalsimple

                                            y simple"That sounded wrong."
                                            y worried"We didn't know it was so sensitive!"
                                            y pf"No, still wrong..."
                                            y sad"We're very sorry!"
                                            "I'm shaking right now, who knows how much that thing costs."
                                            y "L-let me pay yo-"
                                            "I open my wallet to find a lone credit card and some change, at the sight of which I panic."
                                            y scared4"Ah!"
                                            hide cat21simple
                                            show cat20simple at right2
                                            y scared3"Tate, money, NOW!"
                                            "The cat struggles to reach some inner pockets on his attire hastily as well."
                                            t "I-I have, uhm."
                                            t "Do you take graham crackers for repairs?"
                                            co "Guys, chill out."
                                            co "It's not a big deal, you didn't break anything."
                                            co "But if you were to damage it, there is no price for repairs, because there's only one of these babies in the world."
                                            y s"Phew."
                                            y "Another day, another priceless artifact spared."




                                            "I hit Tate with my elbow as I notice his apathetic expression."
                                            hide cat20simple
                                            show cat20confused at right2
                                            t "Ouch."
                                            t "Yeah, I'm sorry, although I'm still interested in whatever that was."
                                            t "Is it a bomb?"
                                            y surprised"{i}*Gasp*!{/i}"
                                            y "Is it?"

                                            co "{i}*sigh*{/i}"
                                            co "No, it's not."
                                            co "It's... a thing."
                                            "Very descriptive."
                                            co "And it's fine, it's my fault anyway."

                                            y confused"How is it ever your fault in this situation?"
                                            hide cat20confused
                                            show cat21bored at right2
                                            t "Shhh, he said it's his fault."
                                            hide cat21bored
                                            show cat21simple at right2
                                            hide coalsadsmile
                                            show coal at left2

                                            co "I was warned about an {i}'eccentric purple cat'{/i} and his shenanigans."
                                            co "More so I was told to run the opposite direction if I ever spot him."

                                            t "You heard about me?"
                                            hide coal
                                            show coalsadsmile at left2

                                            co "Honestly, I thought he'd be some kind of sex predator, not a tech menace."
                                            co "And I made the mistake of standing my ground."
                                            hide cat21simple
                                            show cat21spark at right2

                                            t "[name], he heard about me."
                                            y "Not in a good way..."
                                            y "Sooo, your device is going to be alright?"
                                            co "Yeah, I just need to wait for it to reset."
                                            co "Kind of sucks that I won't be able to use magic for a while."
                                            hide cat21spark
                                            show cat20ec at right2
                                            t "So it IS a magic device!"
                                            hide coalsadsmile
                                            show coal at left2

                                            co "Yes, in fact, it's one of the main reasons I got into the academy."
                                            co "I told you before that I don't have magic of my own, but with this little guy, I can cast a large variety of spells."

                                            y "That's so cool!"
                                            y "What Shard were you thinking of joining?"

                                            hide coal
                                            show coalec at left2

                                            "He looks at our wide eyed faces and chuckles."
                                            hide cat20ec
                                            show cat20surprised at right2
                                            co "Heh, give me that list."

                                            t "Seriously?!"




                                            hide cat20surprised
                                            show cat20ec at right2
                                            t "Appreciate it, you're saving my skin."
                                            show list3 with dissolve
                                            t "Awesome!"
                                            y ec"Thank you so much!"
                                            hide list3 with dissolve
                                            hide coalec
                                            show coalsmug at left2

                                            co "Why are you thanking me?"
                                            co "Isn't this {i}'mandatory'{/i}."
                                            hide cat20ec
                                            show cat21mad2 at right2

                                            y pf"Errm, yes, yes it is."

                                            "Tate hits me lightly with his elbow back."
                                            hide coalsmug
                                            show coalec at left2

                                            co "Heh, it's ok, I know you were trying to {i}'scam'{/i} me, I was warned about this too."
                                            co "But I wanted to sign up for the Sorcery Shard anyway, so it's your lucky day."
                                            hide cat21mad2
                                            show cat21blush at right2

                                            "Both me and Tate are blushing from embarrassment, while Coal laughs."

                                            co "Don't feel bad, if you want, you can make it up to me later, I'll find you whenever the time comes."
                                            t "Welp, I'm never scamming anyone again."
                                            co "Glad to hear it, good luck on your search, I'll go search for my friend elsewhere."
                                            t "Before you go, what name did the person use when he warned you about me?"
                                            hide coalec
                                            show coalsimple at left2
                                            co "Uhmm, I think it was... Tate?"
                                            hide cat21blush
                                            show cat21bored at right2
                                            t "Damn it..."

                                            co "Is that not your name?"
                                            t "It is... kinda."
                                            co "Kinda?"
                                            t "It's a whole thing."
                                            hide cat21bored
                                            show cat20ec at right2
                                            t "Cya later."
                                            hide coalsimple
                                            show coal at left2
                                            y ec"Bye, hope you find your friend, and sorry again!"

                                            co "Good luck to you as well, in whatever trouble you decide to get in next."
                                            hide coal with moveoutleft

                                            scene hallway20
                                            show cat20simple at right2
                                            show cat20simple at center with ease


                                            t "Told you it was a bad idea to try to scam him..."
                                            y pf"You-"
                                            y bored"{i}*sigh*{/i}, never mind."

                                            $ scam+=1
                                            jump aftercoal

                                            label noscam:
                                            play music "audio/catjazz.ogg" fadein 4.0
                                            hide cat20smug
                                            show cat20bored
                                            y simple"No."
                                            y "We really shouldn't."
                                            y s"Plus, he might just agree to join without having to scam him."

                                            t "Ughh, fine, but if he refuses, it's your fault."
                                            hide cat20bored with moveoutright
                                            y "Fair enough."

                                            scene hallway20 with dissolve

                                            show coalnoworry at left2 with moveinleft


                                            "We walk towards the lost panther wearing a worried face."

                                            y "Hi there."
                                            show cat20smile at right2 with moveinright
                                            t "Hey!"

                                            co "Oh, hello."
                                            y ec"Do you need any help? You seem lost."
                                            co "No, no thank you, I'm fine, I was just waiting for someone, although they're sure taking their time to show up..."
                                            t "Are you perhaps a first year?"
                                            hide coalnoworry
                                            show coalno at left2
                                            co "I am, how'd you know?"
                                            co "Am I that obvious?"

                                            t "I don't see a badge, and first years are usually the ones that look the most confused."

                                            co "Read like a book."
                                            co "Erm, I'm Coal, by the way."
                                            y "Right, where are our manners, I am-"
                                            co "[name]."
                                            co "Yeah, I heard about you, at today's announcements."
                                            y "I'm flattered you remembered."
                                            co "And you are... Tate, right?"
                                            hide cat20smile
                                            show cat21bored at right2
                                            show coalnosimple at left2
                                            hide coalno
                                            t "Damn it, why do my other names not stick to people?"
                                            co "Is that... not your name?"
                                            t "It is, but it's like, a whole thing, you wouldn't understand."
                                            co "Oh."
                                            t "At least you've heard of me, that's a big win."

                                            co "Honestly, I was told about an eccentric purple cat in a crop top, and was warned to run away in the opposite direction as soon as I saw them."
                                            hide cat21bored
                                            show cat21spark at right2
                                            t "He heard about me."
                                            hide coalnosimple
                                            show coalno at left2
                                            co "At first I thought you'd be some kind of sex predator, haha."
                                            t "He really heard..."
                                            y pf"Bad things about you..."
                                            hide cat21spark
                                            show cat21smile at right2
                                            t "All publicity is good publicity, my dear [name]."
                                            y bored"Factually untrue."
                                            y "Anyway."
                                            y "I'll get straight to the point."

                                            y s"Have you joined a Shard yet?"

                                            co "Not yet, but I've made a decision already, just need to go to the leader to sign."
                                            hide cat21smile
                                            show cat20vibrate at right2
                                            t "May I ask what Shard that is?"
                                            "Tate is visibly nervous and shaking."
                                            co "Why, the best one there is, obviously."

                                            t "And that iiis...?"
                                            hide cat20vibrate
                                            show cat21simple at right2
                                            co "The Defender's Shard."
                                            "The cat's tail drops and mine comes lower as well."
                                            y simple"I see..."
                                            hide cat21simple
                                            show cat21smile at right2
                                            t "Well, no time to linger and sulk, let's go find more people!"
                                            "His mood got better in an instant, although I could still feel sadness behind his words."
                                            hide coalno
                                            show coalnosimple at left2
                                            y awkward"A-alright, sorry Coal, we're on a strict schedule and we have to go, but it was nice meeting you."
                                            co "Hold on, that's it?"
                                            hide cat21smile
                                            show cat21simple at right2
                                            t "What do you mean?"
                                            co "I thought the infamous {i}'Purple Demon'{/i}, as an anonymous encounter mentioned, would at least TRY to scam me into signing into the Sorcery Shard."
                                            hide cat21simple
                                            show cat21spark at right2
                                            t "Wow, that's a cool name, maybe I should adopt it."
                                            t "And hey, you heard about my list too?"
                                            t "Just what DON'T you know?"
                                            hide coalnosimple
                                            show coalno at left2
                                            co "Sorry, I was just curious if you'd do it, but I guess a certain someone had a positive impact on you already."
                                            "He looks at me with a smug expression."
                                            y simple"Are you saying you lied about-"
                                            co "Joining the defenders?"
                                            co "Yep, I actually wanted to join the sorcerers from the start."
                                            hide cat21spark
                                            show cat20ec at right2
                                            "Tate's mood improves again, but this time it feels genuine."

                                            y simple"Hold on, do... do you have any magic, we forgot to ask."

                                            co "Nope, none whatsoever."
                                            hide cat20ec
                                            show cat21simple at right2
                                            "Another tail drop from the cat follows suit."
                                            hide coalno with moveoutleft




                                            co "I do however, have this."
                                            show coal at left2 with moveinleft

                                            "He gestures to the device resting by the wall, which he picks up and places at his side."
                                            co "It can create magic with the use of energy."
                                            hide cat21simple

                                            show cat20surprised at right2

                                            t "Cool!"

                                            y surprised"Any kind of magic?"

                                            co "Mostly offensive, but it can do some situational things too."
                                            co "So yes, I will be able to pass the assessment if that's what you were worried about."
                                            y awkward"No offense."
                                            hide cat20surprised
                                            show cat20ec at right2
                                            t "None taken, now sign PLEASE!"

                                            "He basically shoves the clipboard in Coal's face."
                                            "He signs, unbothered by Tate's enthusiasm."
                                            co "There."



                                            co "What about you two, what brings you in this Shard?"

                                            hide cat20ec
                                            show cat20smug at right2


                                            t "I can fly and teleport."
                                            co "Nice! Sounds handy."

                                            y pf"My magic is... situational."

                                            co "I see."

                                            co "Here."

                                            show list3 with dissolve

                                            t "Awesome, thanks again!"
                                            hide list3 with dissolve
                                            co "My pleasure, good luck on your search, I'll go search around for my friend."
                                            hide coal with moveoutleft
                                            y ec"Bye, hope you find your friend, and sorry again!"

                                            scene hallway20
                                            show cat20simple at right2
                                            show cat20simple at center with ease


                                            t "Can't believe not scamming him worked..."
                                            y "Sometimes, not being an asshole pays off."

                                            t "It would appear so."










                                            jump aftercoal

                                            label aftercoal:

                                            play music "audio/happy2.ogg" volume 0.3

                                            scene hallway20
                                            show cat20ec



                                            t "With that, we have six!"

                                            t "If my math is right, that makes it more than half!"
                                            t "How much time do we have left?"

                                            y simple"Let's see...hmm, oh."
                                            hide cat20ec
                                            show cat21simple
                                            y simple"Twenty minutes."


                                            t "TWENTY?"

                                            t "What do we do?"

                                            y bored"We could offer up our bodies in exchange for signatures?"
                                            hide cat21simple
                                            show cat20ec
                                            t "Great idea!"

                                            y simple"W-wait, no, I was joking."
                                            hide cat20ec
                                            show cat21scared

                                            t "Right, so was I... definitely joking."

                                            un "I spotted three more people, two to your left and another one straight ahead."
                                            "Thanks, Scribbles, you're super helpful!"
                                            un eyeroll"The things I do for my subjects."
                                            hide cat21scared
                                            show cat20smile
                                            y s"I think we should split up."
                                            y "You take this left hallway and I'll go straight ahead, meet me back here in fifteen minutes."

                                            t "Good idea, we can cover up more ground this way."
                                            t "Who takes the list?"
                                            y "Just keep it, I'll get the names of whoever I find and I'll sign them myself."
                                            t "Roger that."
                                            hide cat20smile with moveoutright

                                            "I turn around, preparing to sprint, but the soft voice of the cat stops me."
                                            show cat21sadsmile at right with moveinright

                                            t "Hey, [name]..."
                                            t "Thanks again, for doing this..."
                                            t "I really need to complete this list, more than you know."

                                            y ec"I'm happy to help, I promise I'll get you those signatures no matter what."


                                            "He smiles, but behind the curved lips are a pair of eyes lost in thought."

                                            "More than I know?"
                                            "I know well enough the taste of detention, even if I've only gotten it once in my life."
                                            un "Maybe here they're being tortured in detention, you know, like younglings are supposed to be treated in the first place."
                                            stop music fadeout 2.0
                                            hide cat21sadsmile with moveoutright

                                            "After another moment of silence, we both sprint in our designated directions."
                                            scene hall with dissolve
                                            play music "audio/jazz4.ogg" fadein 3.0 volume 0.5
                                            un "How come you didn't choose the path with the two people."
                                            y simple"I'm not confident enough in my persuasive abilities, and Tate seems to know how to get what he wants from people."
                                            un tease"Can he get a dick from you as well?"
                                            y smug"He can have my heart."
                                            un eyeroll"Bleh, romance, disgusting."
                                            un "I'm only interested in carnal pleasure."
                                            y s"You'll have to get used to it from now on."
                                            un bored"That is to say, you think you can actually get in his bed?"
                                            un curious"Actually, scratch that, why would you WANT to get in his bed?"
                                            y smug"He's hot?"
                                            un eyeroll"I suppose that's {i}kind{/i} of true, for someone that thinks with their dick, at least."

                                            un simple"Hey, careful, here he comes."

                                            play sound "audio/thud.ogg"

                                            scene black

                                            "I round the corner and plant my face directly into someone's chest."

                                            st "ow..."
                                            y awkward"Sorry, sorry, I should've been more careful!"
                                            scene hall with dissolve
                                            un ang"I told you to be careful, you fucking troglodyte."
                                            un bored"Why do I ever bother?"



                                            show connor with dissolve


                                            st "It's no problem, it happens when you're hurrying, I suspect you're a first year as well?"
                                            hide connor
                                            show connorsur
                                            y scared4"YES!" with hpunch
                                            "That was a little loud."
                                            "I already managed to startle him, goodbye first impressions."
                                            hide connorsur
                                            show connor

                                            y awkward"Sorry, I'm just looking for first years that haven't joined a Shard yet, are you one by any chance?"

                                            st "I am, what's up?"

                                            y s"Awesome! Name's [name], yours?"

                                            con "Connor."

                                            un bored"Douchebag."

                                            y "Are you perhaps interested in joining the Sorcery Shard?"

                                            con "Not really, I was thinking of becoming a slayer."
                                            y simple"Oh... do you not have any magic?"

                                            con "I do, but I'm just more interested in working alone in the future."

                                            y worried"But, but..."
                                            con "Would that be all?"
                                            con "Can I go?"
                                            con "Unless you want to sue for damages, you look like you hit a brick wall, not a person."
                                            "I stand up straighter, arrange my crooked tie, and try to keep my emotions under control."


                                            y "Wait, what can I do to convince you?"
                                            y "This is really important to my friend."

                                            con "I don't know your friend, so not to be rude, but I don't really care."
                                            show connor at right2 with ease
                                            con "Now if you'll excuse me-"


                                            y "Hold on..."
                                            show connor at center with ease
                                            "Damn it, I don't know how to convince him, what would Tate do?"
                                            y "I'll..."
                                            y determined"I'll suck you off... right here, right now, if you join the Sorcery Shard."
                                            un "That's definitely not what he'd do..."
                                            un "Slut."
                                            hide connor
                                            show connorsur

                                            con "Oh shit, for reals?"

                                            y "Yes!"
                                            hide connorsur
                                            show connor

                                            con "You and every other guy in this place..."

                                            y pf"Say what?"

                                            con "In fact, I'm pretty sure a lot of guys would pay ME to let them have a go at my cock, I'm not going to make such an important decision for five minutes of heaven."

                                            un tease"He really slapped you with reality."
                                            show connor at right with ease

                                            con "So if you don't mind I'll just-"

                                            y worried"WAIT!"
                                            hide connor
                                            show connormad at right

                                            con "Ughh, what now?"

                                            y worried"Please, I'll do anything."
                                            show connormad at center with move

                                            y "A-and, you don't even have to be a member for life, you can just switch shards if you hate it so much in sorcery."
                                            y "Doesn't that sound like a decent deal?"

                                            con "You're not wrong... {i}'anything'{/i} you say?"

                                            y determined"Anything."
                                            hide connormad
                                            show connor

                                            con "You're... one of those special guys aren't you?"
                                            con "A {i}'recommended student'{/i}, I believe you're called."

                                            y s"Yes, I am."

                                            con "..."
                                            con "What are your powers?"
                                            y "I can manipulate energy, and I have some supportive abilities on the side."
                                            con "Shit, that's pretty good."
                                            "He thinks for a second."
                                            con "Fine, listen up."

                                            y "I'm all ears."



                                            con "I have the power to copy other's magic, but the problem is that I need their consent, and it lasts for two weeks."

                                            con "If you let me copy yours, for as long as I'm in the Sorcery Shard, every two weeks, I'll sign your list."
                                            con "Although I doubt I'll be staying in that shard after the test."

                                            y simple"Is this going to affect me in any way?"

                                            con "Only for a minute, you'll feel a bit tired."

                                            "Do you think it's safe, Scribbles?"
                                            un bored"Sure, copying abilities usually doesn't bring harm to either parties, especially if you consent."
                                            un "And copied magic is usually much, much weaker than the original magic, so you're getting the high end of the deal."

                                            y determined"I accept."

                                            un squint"You're in luck, this was easier than I thought."

                                            con "And I'll take a blowjob too."

                                            y shoked2"What?"

                                            un bored"Aaand I spoke too soon."

                                            con "You offered to do it before, it shouldn't be a big deal, right?"
                                            y worried"But you said-"
                                            hide connor
                                            show connormad
                                            con "Do you see {b}anyone{/b} around?"
                                            con "Nobody else to do it with."
                                            "The hallways are awfully empty and silent."
                                            hide connormad
                                            show connor
                                            con "And it just so happens I'm in the mood for one, and you're here."
                                            con "Also, you're not half bad looking."

                                            menu:
                                                "Do I do it?"
                                                "Accept.":
                                                    $ blowjob +=1
                                                    "Might as well, it would make for good practice."
                                                    un "{i}*cough*{/i} Whore."
                                                    un "Again."
                                                    y awkward"Alright, let's do it."
                                                    show connor at left with ease
                                                    stop music fadeout 2.0
                                                    con "Cool, then get in."
                                                    "He holds the door of an empty classroom."
                                                    y simple"Although, can we keep it under ten minutes?"
                                                    con "Then you better suck fast."
                                                    scene black with longdissolve
                                                    play music "audio/jazz2.ogg" volume 0.4
                                                    "Once I'm inside he blocks the door with a chair."
                                                    con "I don't want surprise visitors."
                                                    y "Good thinking."
                                                    "He guides me towards the back pushing me from behind."
                                                    "He rests his back against a wall and pushes my shoulders down, making me kneel in front of him."
                                                    "I didn't expect to be manhandled like this today, but here we are."
                                                    scene shepbj11 with longdissolve

                                                    Y bored"You don't like wasting time, do you?"
                                                    con"Not when I can have a mouth around my cock in that amount of time."
                                                    "He unbuttons his pants and starts sliding them down, underwear and all."
                                                    scene shepbj1 with dissolve
                                                    scene CGcc1
                                                    "I could notice a large bulge growing as soon as we entered the room, but I am still surprised as his hard cock springs up and hits my chin."
                                                    "It doesn't seem like he is going to do much effort himself, his bored eyes look down at me with a hint of anticipation and annoyance."
                                                    "I don't bother unzipping my own pants, as I'm not necessarily doing this for pleasure."
                                                    "Although I'd be lying if I said I'm not craving having this in my mouth."
                                                    "I start by licking his shaft from base to tip, trying to cover as much surface with my tongue as I can."
                                                    "His cock twitches at the sensation, and a moan or sigh of relief escapes his muzzle."
                                                    "I massage the tip with my fingertips before grabbing the base and fixing it straight towards me."
                                                    "I take a second to get a whiff in, because that's what they sometimes do in movies, right?"
                                                    "I've never done this before, if that wasn't obvious."
                                                    scene shepbj2 with dissolve
                                                    scene CGcc2
                                                    "But that doesn't seem to be a problem for this guy, since as soon as his cock reaches the back of my throat he melts."
                                                    con "Fuuuck... this is pretty good."
                                                    con "Didn't think you'll take it all."
                                                    "I look up at him with a smug glint in my eyes as I start to slowly slide it out until my lips are the only ones holding onto the top of his head, releasing it with a pop."
                                                    "With another lick from the base up, I bring it back in and quicken my pace, making sure my snout hits his belly before moving my head back and repeating."
                                                    con "That's it... don't stop."
                                                    "It turns out the awkward sessions I had in my bedroom with my toys, practicing blowjobs, were not in vain, let's hope the pillow kissing will come in handy as well at some point."
                                                    "His hips move a bit forward as his back slumps lower against the wall, a sign of relaxation and great enjoyment."
                                                    "His teeth are clenched, same goes for his fists."
                                                    "I would assume that means he's close, but it doesn't seem like he wants to say anything about it."
                                                    "I spend another minute hunched over the slab of warm meat that now goes in and out like butter."
                                                    "I've got used to the girth at this point, and the saliva lubing it became enough to drip onto the floor, like a melting popsicle on a summer day, mixed with the precum that can be differentiated by its saltiness."
                                                    scene shepbj3 with dissolve
                                                    scene CGcc3
                                                    "Before I know it, the cock in my mouth starts throbbing, followed seconds later by a thick stream of hot cum, filling my mouth and spilling down both my throat and outside my mouth, gushing through the small gaps between my lips and his shaft."
                                                    menu:
                                                        "The little free space left in my mouth that wasn't occupied by dick is now full of seed."

                                                        "Swallow.":
                                                            "The warm liquid flows deeper into me, and I don't stop it."
                                                            scene shepbj33 with dissolve
                                                            "I slide his cock out, my mouth still tight around it, collecting the dripping cum that was left on it before swallowing everything with a quick tilt of my head, leaving my mouth empty."
                                                            "He seems content by my action."
                                                            con "Good job, this was better than expected."
                                                            con "And we didn't even make a mess."
                                                            "I lick my lips and wipe away any cum left that I can't reach, using a baby wipe from my backpack."
                                                            "I would be lying if I said I didn't enjoy this, even if I'm technically being paid for it... wait, am I-"
                                                            un "A whore?"
                                                            un "Yes."
                                                            "Fuck!"
                                                            "Well, can't do anything about it now..."
                                                            scene black with dissolve
                                                            "He places his now softened member back in his pants and buttons them back up as I get up and we walk out of the room."
                                                            jump signing





                                                        "Spit it out.":
                                                            scene shepbj33 with dissolve
                                                            "Before he's even done squirting everything out I hastily pull his cock out of my mouth, coughing back as much of his seed as I can, making a small puddle on the ground."
                                                            "A warning would've been nice!"
                                                            con "Great..."
                                                            "Through teary eyes I see him make a hand gesture, the next second the puddle flies out the window."
                                                            y hurt2"{i}*Cough*{/i} W-what was that about?"
                                                            un "The cum bender!"
                                                            con "I can control liquids, got the ability from another first year earlier."
                                                            y simple"Let's hope nobody was walking by this window outside."
                                                            scene black with dissolve
                                                            "I get back up and we walk out of the room."

                                                            jump signing



                                                "Nope nope nope nope nope.":
                                                    scene hall
                                                    show connor

                                                    y awkward"No no no no no..."
                                                    hide connor
                                                    show connormad
                                                    con "No?"
                                                    y "No."

                                                    y "That comment from earlier? Haha, I was just joking."
                                                    hide connormad
                                                    show connor
                                                    con "Is that so?"
                                                    con "Alright then."
                                                    show connor at right with ease
                                                    con "Bye."

                                                    y "Wait wait wait!"
                                                    y "Please!"
                                                    y "Is my magic not good enough?"
                                                    con "You teased me already, so no, I need more."
                                                    con "If you have nothing extra to offer then I'm not interested."
                                                    "Damn it, why does this guy have to ask for such a reasonable and fair exchange?"
                                                    "Can't he just accept a flying kiss or something?"
                                                    un "You're not that hot."



                                                    y determined"How about I throw some cash instead?"
                                                    show connor at center with move

                                                    con "Such a big deal for ya, huh?"
                                                    con "I'm even more intrigued about how you feel inside now."
                                                    con "Buuut I could actually use the cash."
                                                    con "Give me enough to buy twenty blueberry blasts from the vending machine."
                                                    y simple"Very specific, but okay, here ya go."
                                                    "I open my wallet, panicking at first since it's mostly empty, but then I remember my overly cautious mother, who likes to shove money into various non conventional places, so if my wallet is stolen, the thief would be TRICKED!"
                                                    "It's just a burden to me most of the time."
                                                    "I eventually find a small stack of money in a deep pocket in my backpack."

                                                    con "Cool, this should do."
                                                    jump signing

                                            label signing:
                                                play music "audio/jazz4.ogg" fadein 3.0
                                                scene hall
                                                show connor
                                                con"Let's get on with it then."

                                                con "Give me your hand."

                                                y blushmad"I'm not gonna marry you as well, the fuck?"

                                                con "It's for the magic exchange..."

                                                y simple"oh."

                                                con "..."
                                                con "You're not the brightest, are you?"
                                                y pf"There's no need to be THIS rude."

                                                hide connor with dissolve
                                                show connorclose with dissolve




                                                "He rolls his eyes as he pulls my hand closer."
                                                un squint"Why the fuck would you think that's what he means?"
                                                "Give me a break, I'm full of emotions..."

                                                "I keep my arm extended, embarrassed as he unbuttons my cuff and rolls my sleeve up, holding it with both hands."
                                                con "When you feel a tingling sensation, simply don't resist it, and let some magic flow to your arm."
                                                "I do as I'm told, and it only takes him a couple of seconds to complete the ordeal, leaving me slightly fatigued."
                                                hide connorclose with dissolve
                                                show connor with dissolve

                                                con "This should be enough, might come in useful during the test."
                                                con "So, where do I sign?"
                                                y simple"My friend has the list, just write your name in my phone and I'll sign it for you."
                                                con "Cool."

                                                con"Pleasure doing business with you."

                                                con "Now can I go?"

                                                y awkward"Yes, sorry for taking your time, and thanks for the signature."
                                                hide connor with moveoutright

                                                if blowjob >=1:
                                                    "I watch him walk away, the taste of his cum lingering in my mouth."
                                                    y pf"This better be worth it."
                                                    jump afterconnorsex
                                                else:

                                                    "I watch him walk away, with my allowance for two months in hand."
                                                    y pf"This better be worth it."
                                                    jump afterconnorsex

                                                label afterconnorsex:

                                                scene hall






                                                "But in any case."
                                                "Thank goodness we managed to do it."
                                                un simple"YOU did it."
                                                un squint"I'm not even sure I want a part in this."
                                                "Suit yourself."
                                                "I'll be the hero of the day by myself."
                                                "All glory to me."

                                                "Where to now?"
                                                un bored"Back."

                                                "Back where?"
                                                un "Back where the cat told you to meet him."
                                                un "You have like seven minutes left."
                                                stop music fadeout 2.0
                                                play sound "audio/run.ogg"
                                                "Shit."


                                                scene black with dissolve
                                                "Let's hope he managed to convince those two to sign."


                                                scene hallway20 with dissolve
                                                show cat20 with moveinleft
                                                stop sound
                                                play music "audio/littlehappy.ogg"

                                                t "Hey!"
                                                t "Pleaaaase tell me you had some luck on your part."
                                                y "I managed to get one more person to sign."
                                                y "Did you get those two?"
                                                hide cat20
                                                show cat21simple
                                                t "Two?"
                                                t "How'd you know there were two?"
                                                y awkward"Yet another convenient guess."
                                                hide cat21simple
                                                show cat20ec
                                                t "Suspicious, but yes!"
                                                t "I did!"
                                                t "And all I had to do is flirt with them for a minute."
                                                hide cat20ec
                                                show cat20smug
                                                t "Men are so stupid."

                                                "That guy wouldn't accept a blowjob and those two signed after some flirting...?"
                                                un bored"Chill out, Snow White, you're not the fairest of them all."
                                                un "You'll need more than looks to convince."
                                                hide cat20smug
                                                show cat20smile

                                                t "We have to hurry back."
                                                t "Take my hand, I'll teleport us back."
                                                y pf"Hmm."
                                                y "Five...one...one...two..."
                                                y surprised"Wait, we only have nine signatures!"
                                                hide cat20smile
                                                show cat21sadsmile
                                                t "It's fine, I made my peace with it already, we were close, but the Headmaster was right."
                                                y simple"But..."
                                                hide cat21sadsmile
                                                show cat20smile
                                                t "Shall we go? Hang on tight."
                                                scene teleport

                                                "He takes my hand with a last warning and we teleport away."
                                                stop music fadeout 2.0
                                                "This is the first time I experience something like this, and my landing was not very graceful, but I managed to remain on my feet."
                                                scene meetingroom with dissolve
                                                play music "audio/hm1.ogg" fadein 2.0
                                                "We arrive a minute early, right as the Headmaster rounds the corner and enters the room together with a worried Merina, who quickly brightens up when she sees Tate with the list in hand."
                                                show cat21smile at right with moveinright
                                                show merina20 at left with moveinleft
                                                show headmaster20smile1 with moveinleft



                                                h "Ah, you are just in time, let's hear the news."
                                                h "And if that smile is genuine, then I'm bracing myself to faint already."
                                                "Indeed the cat had a smile on, but once again, the eyes gave him away, his pupils were shaking as a thin layer of liquid made them refract in the light."
                                                t "Well.. here it goes, long story short, we didn't get to-"
                                                y ec"Disappoint you on the first day!"
                                                play sound "audio/scratch.ogg." volume 0.3
                                                stop music
                                                hide cat21smile
                                                show cat21simple at right
                                                hide merina20
                                                show merina20simple at left
                                                hide headmaster20smile1
                                                show headmaster20surprised
                                                t "I'm sorry?"
                                                "At that moment, the decision was clear."
                                                "I have been lying to myself for some time that any other choice could be made at this point, so I take the paper and sign my own name on it."
                                                show list4 with dissolve
                                                play music "audio/hm1.ogg" fadein 2.0
                                                "The three people are taken aback by my decision."
                                                "The Headmaster accepts the list hesitantly, looking at me through squinted eyes once he reads it."
                                                h "Name Name two...?"


                                                y simple"hm?"
                                                hide list4 with dissolve
                                                hide headmaster20surprised
                                                show headmaster20angry
                                                y pf"Oh, I forgot that's not how that works..."
                                                hide merina20simple
                                                show merina20sadsmile at left
                                                m "I'll fix it for him..."
                                                m "What is your last name again, [name]?"
                                                $ name2 = renpy.input("My last name is...", length=15)
                                                $ name2 = name2.strip()
                                                $ NAME2 = name2.upper()
                                                if name2 =="":
                                                    $ name2="White"
                                                    $ NAME2 ="WHITE"
                                                y s"[name2]."


                                                m "[name] [name2], understood...and are you sure?"

                                                h "A last second decision?"
                                                h "It's not what I expected from you."
                                                y ec"It is not last second, I've been thinking about this for months."
                                                y s"I admit I have had my doubts for a little while now, but Tate's dedication really inspired me and solidified my decision."

                                                t "I did that?"
                                                "The Headmaster looks impressed and annoyed at the same time while holding the new list."
                                                "His expression turns to confusion again."
                                                h "There are only nine in here, counting yours."

                                                t "I knew I should've paid more attention in math..."
                                                y simple"Huh?"

                                                h "It would seem like even your chivalry couldn't-"

                                                y "Oh, wait, sorry, just a second."
                                                show list5 with dissolve
                                                "I take the list back and write the name of the guy from before, Connor Murphy."
                                                un curious"You really forgot to sign him?"
                                                "Don't blame me, I was under a lot of stress!"
                                                hide list5 with dissolve

                                                y s"Here."
                                                scene meetingroom
                                                show merina20 at left
                                                show cat21smile at right
                                                show headmaster20



                                                "Everyone other than the Headmaster breathe out, relieved."

                                                "He reads every single name on the list one by one, twice, to see if there are any mistakes, but he just can't find any."
                                                "I wouldn't be surprised if he memorized every name in this academy already."
                                                hide headmaster20
                                                show headmaster20amused


                                                h "This looks legit, for now."
                                                h "I do, however want to remind you-"
                                                y bored"The signatures won't be valid if they don't pass the auditions, got it."
                                                m "Speaking of, where should we hold the auditions this year?"
                                                m "There are a lot of empty training rooms right now."
                                                m "The biggest one, in the East wing could-"
                                                hide headmaster20amused
                                                show headmaster20smile1

                                                h "No, not a training room, we'll use the arena."
                                                hide merina20
                                                show merina20simple at left
                                                m "Won't the arena be busy tomorrow?"
                                                m "We're holding practice sessions the whole day."

                                                h "Yes, and I think that would be a perfect opportunity for the new students to audition, no?"
                                                h "Just give them a bit more of a challenge than the others."
                                                h "I decided to spectate the event as well."
                                                h "I know teachers usually don't get involved, but since it's my first year I want to see with my own eyes what everybody is capable of."
                                                hide cat21smile
                                                show cat20angry at right


                                                t "Hey, the practice is supposed to be our free time and...and-"
                                                show headmaster20side
                                                hide headmaster20smile1
                                                "A chilling stare shoots at Tate."
                                                hide cat20angry
                                                show cat21scared at right

                                                t "And... I think that's a great idea!"
                                                m "Understood, I'll make the new plans for tomorrow then."
                                                hide headmaster20side
                                                show headmaster20simple2

                                                h "Good."
                                                h "I suppose I don't have anything else to complain about."

                                                y bored"Aren't you forgetting something?"
                                                hide headmaster20simple2
                                                show headmaster20bored
                                                h "Hmm?"
                                                h "What would that be?"
                                                y "Me and Tate just did the impossible, at least what YOU thought to be so."
                                                y simple"Don't we get anything, at least an apology?"
                                                y pf"You were {b}wrong{/b}."


                                                "Once again, everyone holds their breath, waiting for the lion's response."
                                                t "Please don't aggravate the lion dude..."
                                                h "{b}IF{/b} these signatures are proven to be valid, then you have my sincerest congratulations."
                                                h "And perhaps a credit bonus can be discussed in the future."
                                                h "Are you satisfied now, mister [name2]?"
                                                y ec"I'm all good now, sir."

                                                h "Then if nobody has any more interruptions, I'll take my leave, good day."
                                                hide headmaster20bored with moveoutright
                                                scene meetingroom
                                                show cat21spark at right
                                                show merina20sadsmile at left
                                                show cat21spark at right2 with move
                                                show merina20sadsmile at left2 with move
                                                stop music fadeout 3.0


                                                "Watching the Headmaster leave, one single worry remains on my mind, and that is Coal."
                                                "I hope he can pull his weight, magicless as he is."
                                                "He is a recommended student, but if he's anything like me..."
                                                play music "audio/forgetmenot.ogg"


                                                "Actually, it seems like another problem arises, as a teary cat jumps in my arms."
                                                hide cat21spark with hpunch

                                                t "You did it!"
                                                t "You madman!"
                                                t "You're such a badass!"

                                                t "Wow, I can not believe someone that can't recognize a trap in the middle of the day would get me out of trouble."
                                                m "Even I fail to do that sometimes..."
                                                show cat21smile at right2 with moveinright

                                                m "I'll leave you two to it now, I need to find Ollie and discuss these audition plans."
                                                m "Honestly, the Headmaster needs to tone it down with the changes around here."
                                                t "You should propose that to your new lion friend the next time you see him, [name]."
                                                y pf"He's not my friend."
                                                hide cat21smile
                                                show cat20smug at right2

                                                t "What?"
                                                t "Already jumped to lovers?"

                                                y bored"Ugh, you're a headache."
                                                t "I've been told so many times."

                                                m "Something tells me you two will get along just fine, have fun!"
                                                y ec"See you later, Merina."
                                                hide merina20sadsmile with moveoutright

                                                "She leaves, swinging her tail lightly, and my eyes can't help but follow her until she's out of sight, as even my legs take a step towards the direction she disappeared to."

                                                show cat20smug at center with move

                                                t "Hey, hey, eyes here buddy."
                                                un "Busted."
                                                y surprised"Huh?"
                                                t "Did you get smitten or something?"
                                                t "What, am I not sweet enough for your eyes?"
                                                "He turns around and swings his tail and hips the way Merina did, but approaches me while doing it, instead of walking away."
                                                y awkward"N-no that's not it, you're cute, I mean, cute too."
                                                y "I-I mean, Merina-who??"



                                                t "Ah, the sweet smell of insecurity."
                                                t "Don't worry, you can't escape my grasp anyway."
                                                y "What does that mean?"
                                                t "Oh you know..."
                                                y "I... don't."
                                                hide cat20smug
                                                show cat20smugclose
                                                t "Then let me show you~"
                                                show tigerhand with moveinleft

                                                y confused"Huh?"

                                                t "Aaand it looks like we have company already."
                                                t "It's been nice not being tailed for two hours, at least."


                                                hide tigerhand zorder 2 with moveoutleft
                                                hide cat20smugclose with dissolve
                                                show cat20smile zorder 1 with dissolve
                                                scene meetingroom
                                                show cat20smile
                                                show wolf20 at right with moveinright
                                                show tiger20bored at left with moveinleft






                                                "A wild tiger and wolf appear just as Tate's sharp ears predicted."
                                                "Two for the price of one."
                                                "Aiden's hand stopping whatever Tate was about to do..."





                                                "Dallan comes in with the energy of a lost puppy reunited with its owner, his tail wagging aggressively."
                                                "While Aiden is as cool as ever, just a little angry at the cat's lack of personal space awareness."
                                                "Those two do make a nice Yin and Yang."


                                                d "Hey there, [name]."
                                                a "Still here?"
                                                a "Do you want another speech from mister boredom over here?"
                                                hide wolf20
                                                show wolf20sadsmile at right
                                                d "I wasn't that boring!"
                                                d "W-was I?"

                                                t "I don't know, I was asleep."
                                                hide wolf20sadsmile
                                                show wolf20simple at right
                                                d "oh."

                                                y "I was just helping Tate complete his list to get out of detention."
                                                a "Ha, good luck with that, the Headmaster likes giving impossible tasks just to see you struggle and punish you in the end."
                                                a "He's a prick."
                                                hide wolf20simple
                                                show wolf20angry3 at right
                                                d "Language!"
                                                a "Sorry."
                                                "Aiden looks me dead in the eye, shaking his head."

                                                y "Actually, we completed the list."
                                                hide wolf20angry3
                                                show wolf20ec at right
                                                hide cat20smile
                                                show cat20ec
                                                t "I'm officially a free cat!"

                                                d "Nice job!"
                                                d "I knew you could do it, even if you had some help."
                                                hide tiger20bored
                                                show tiger20iritated at left
                                                hide cat20ec
                                                show cat21bored

                                                a "No you didn't, you were complaining you'll have to spend time watching him in detention for the next three days."
                                                hide wolf20ec
                                                show wolf20awkward at right
                                                d "I was just preparing for the worst case scenario..."
                                                hide cat21bored
                                                show cat21mad2
                                                t "{i}'Worst'{/i}?"
                                                t "Gee, thanks guys, suuuuch great friends you are."
                                                a "I'm not your friend."
                                                t "Now if you'll excuse me, I'll take my ACTUAL friend, and spend some quality time with him."
                                                t "The one that actually CARES about my well being."

                                                t "How does that make you feel, Aiden? Being left behind by your friend?"

                                                a "I literally prayed for your death many times in the past."
                                                d "He's joking."
                                                a "I'm not."

                                                d "Haha, he's such a jokester, this guy!"
                                                d "He's not usually like this, [name], I promise."


                                                a "Instead of spending time with this leech, you can do something that is not a complete waste of time and come with me and Dallan."
                                                hide cat21mad2
                                                show cat21bored

                                                t "And do what? Crochet?"


                                                a "Get familiar with the school, something that you would technically be best at, but you're too childish to do."

                                                t "Sorry, can't hear you over the sound of boredom."

                                                a "That... doesn't even make sense."
                                                t "Your face doesn't make sense."
                                                hide tiger20iritated
                                                show tiger20angry2 at left

                                                a "Grrr..."
                                                a "Calm Aiden, a single punch from you would kill him."

                                                t "He's talking to himself now, cool."
                                                t "See, [name]?"
                                                t "Nuts."
                                                t "And not the good kind."

                                                hide tiger20angry2
                                                show tiger20bored at left
                                                hide wolf20awkward
                                                show wolf20 at right

                                                d "Aaanyway, what do you think, [name]?"
                                                d "We're serious about the offer."
                                                d "It's your time, you choose how you want to spend it."







                                                menu:
                                                    "Do I want to go with Tate or stay in this room to see what other interesting things might happen?"

                                                    "Go with the cat.":
                                                        $ adventure +=1
                                                        jump tateadventure

                                                    "Stay here.":
                                                        $ Tate_points +=-1
                                                        $ betray +=1
                                                        y awkward"Sorry Tate, I had some other plans in mind after helping you."
                                                        y pf"Besides, I don't really feel like going outside of the barrier on the first day of school."
                                                        hide cat21bored
                                                        show cat20drama
                                                        t "Oh no!"
                                                        t"Another killjoy..."
                                                        t "Betrayed by the one once considered friend!"
                                                        "He brings the back of his hand to his forehead sighing dramatically."
                                                        hide cat20drama
                                                        show cat21bored
                                                        t "But seriously, you did all that just to leave me?"
                                                        t "Deja Vu is hitting pretty hard right now."
                                                        y simple"How so?"
                                                        t "Never mind, just have fun with your {i}'friends'{/i}."
                                                        t"I'll go alone, since this can't wait for you to change your mind."

                                                        t"Guys, please make sure he doesn't break a claw while I'm gone."
                                                        hide wolf20

                                                        show wolf20ec at right

                                                        d "Will do!"
                                                        a "He's being sarcastic."
                                                        hide wolf20ec
                                                        show wolf20simple at right
                                                        d "ah."


                                                        y sadsmile"Sorry, I promise to make it up to you."

                                                        t "I guess helping me with an impossible task is as good of a redemption arc as you'll get as a friend."
                                                        t "So you're forgiven, for now."
                                                        t "But I treasure loyalty, remember it."
                                                        play sound "audio/teleport.ogg"
                                                        show cat20teleport
                                                        hide cat21bored
                                                        hide cat20teleport with dissolve


                                                        "He teleports away without another word."

                                                        un "Sheesh, he didn't take that too well."
                                                        "What a grateful cat..."
                                                        hide wolf20simple
                                                        show wolf20 at right



                                                        d "Great, I'm glad you decided to stay safe, logical thinking!"
                                                        d "Now, why don't we start with the library?"
                                                        hide tiger20bored
                                                        show tiger20simpledown at left

                                                        d "It's pretty close by and-"
                                                        show tiger20simpledown at left2 with move

                                                        a "Hold on, Chelsie is texting me."
                                                        hide wolf20
                                                        show wolf20simple at right
                                                        a "Your members are organizing a witch hunt."
                                                        hide wolf20simple
                                                        show wolf20frust at right
                                                        show wolf20frust at right2 with move


                                                        d "Damn it, I leave them alone for ten minutes and they're already committing atrocities."
                                                        hide wolf20frust
                                                        show wolf20sadsmile at right2
                                                        d "Looks like we have to ditch you too, [name]."
                                                        y bored"Seriously?"
                                                        y "Just like that?"
                                                        hide tiger20simpledown
                                                        show tiger20bored at left2

                                                        a "Let that be a lesson, never ditch your friends."

                                                        y angry"But you're the ones who suggested it!"
                                                        y simple"Can't I come with, at least?"
                                                        y worried"I love stopping people from murdering each other!"

                                                        a "Oh no no no."

                                                        a "This is a delicate situation."
                                                        a "They'll eat you alive."

                                                        d "Yes, you'd probably be safer with a hoard of Nightfallen around, most likely."

                                                        d "We'll make it up to you, we promise."

                                                        a "I'm sure you have other friends to spend your time with."
                                                        hide tiger20bored with moveoutright
                                                        hide wolf20sadsmile with moveoutright


                                                        y angry"This is my first day!"

                                                        "He and Dallan power walk away, starting to run as soon as they get to the hallway, passing Merina that was just entering."
                                                        d "M'Lady~"
                                                        m "M'Lord~"

                                                        a "Sorry, we're busy, witch hunt."
                                                        m "I understand, carry on."

                                                        show merina20 with moveinright

                                                        "My social savior is here!"

                                                        m "Hey [name], you're still here, I see."
                                                        y simple"Is that a problem?"

                                                        y bored"Everyone seems to be pointing it out."
                                                        y "And then making sure it IS a problem..."

                                                        m "I wouldn't say {i}'problem'{/i}, it's just a little unusual."
                                                        y "And why's that?"
                                                        hide merina20
                                                        show merina20sadside with dissolve
                                                        "She says nothing, instead, looks around with an unsure, slightly worried expression."
                                                        "Complete silence follows, as we are the only ones in the room."
                                                        y pf"I get it now."
                                                        hide merina20sadside
                                                        show merina20simple
                                                        m "Tate didn't ditch you, did he?"
                                                        m "He has this toxic trait where he kind of takes advantage of people's kindness."
                                                        m "But not in a heartless way, he's just a little selfish, but.. not in a bad way."
                                                        m "He just doesn't understand empathy very well... but not..."
                                                        hide merina20simple
                                                        show merina20sadsmile
                                                        m "I should probably stop talking about his qualities."
                                                        y pf"You should."
                                                        y simple"And no, he didn't ditch me, in fact, I'm the one that refused his {i}'adventure'{/i} invitation."
                                                        hide merina20sadsmile
                                                        show merina20simple
                                                        m "Huh, that's once again, something odd."
                                                        m "He usually spends his time in the forest alone."
                                                        m "Will hiss at anyone that even suggests trailing him."
                                                        m "Would even set magic traps behind to make sure he's alone."
                                                        m "The fact that he wanted you to come with..."

                                                        y "So... you're saying I shouldn't take his invitations for granted?"
                                                        m "That would be preferable."

                                                        y "I noticed you care a lot for him, going so far as to almost fight the Headmaster in his stead."
                                                        hide merina20simple
                                                        show merina20smug
                                                        m "Says the guy who literally fought him verbally for Tate's sake."
                                                        m "Was close to throwing hands too."
                                                        y "Guess I did... didn't I?"
                                                        hide merina20smug
                                                        show merina20sadsmile

                                                        m "Tate is like a little brother to me."
                                                        m "I've known him for a long time, and helped him understand his magic better."
                                                        m "I might not be a teleportation expert, but I know enough about magic to score a leader's position."
                                                        m "I'm embarrassed to say, but he looks up to me as well, so I'm trying to be a role model as much as I can."
                                                        y s"I'd say you're doing a great job so far."
                                                        hide merina20sadsmile
                                                        show merina20sad
                                                        m "Am I?"
                                                        m "Then why isn't he following my lead and keep a healthy diet, study for six hours a day, everyday, do paperwork for six more hours and practice-"
                                                        hide merina20sad
                                                        show merina20bored

                                                        m "Yeah, I'm hearing myself too."
                                                        Y simple"Yup, not even I would like that, and I loved homework in high school."
                                                        y "Tate seems to be the kind to seek peril and excitement more than school work."
                                                        hide merina20bored
                                                        show merina20
                                                        m "You'd be right, I doubt I can be of much help, as a lover of the arts."
                                                        y smug"Arts you say?"
                                                        m "That's a story for another time."

                                                        y s"In that case, back to the cat in the room, or... in the forest."

                                                        y "Are you two childhood friends?"

                                                        m "Not really..."
                                                        m "We only met when I first came to the academy."

                                                        y simple"Isn't this his first year, like me?"
                                                        y "How-"

                                                        m "Ah, I understand the confusion, let me be more clear, Tate's been living on academy grounds for years."
                                                        m "This is his home."

                                                        y pf"You mean he lives in the city surrounding the academy?"

                                                        m "Again, close, but not really."
                                                        m "You see, Mister Sebil, our previous Headmaster, found Tate when he was a kid, at the time, and took him in."
                                                        m "Of course, Mister Sebil and his wife had a lovely house, but considering he was the Headmaster and she was a teacher here, and they never had kids of their own, Tate didn't like being left home alone."
                                                        y simple"He... is an orphan then?"
                                                        hide merina20
                                                        show merina20sadsmile

                                                        m "Precisely, so almost his whole life's been revolving around this building, and the students in it."
                                                        y "This does not seem the best place for a kid to run around."

                                                        m "Agreed, he got in so much trouble for trying to sneak into the classrooms when we had Nightfallen energy extraction lessons, which is highly not safe for work."
                                                        m "That's where I, Aiden, Dallan and Chelsie came in."
                                                        m "We made sure those classes were {i}'Tate proofed'{/i}."
                                                        m "Anti teleportation barriers, icy floors, detection devices, one-way windows and more."
                                                        m "Ollie wanted to help, but he's a little easy to bully around, especially by Tate."

                                                        y "Sounds like a headache."
                                                        m "It was, but I don't regret it, it brought excitement to my school years."
                                                        m "Excitement that wasn't revolving around sex."
                                                        m "And God knows I needed that to get through the busy days."

                                                        y "Mister Sebil retired, didn't he?"
                                                        hide merina20sadsmile
                                                        show merina20sad
                                                        m "..."
                                                        m "He did..."
                                                        m "That's why we're tiptoeing around Tate a little more than usual."
                                                        m "He didn't take his retirement lightly."
                                                        m "Especially since he did it the year Tate was supposed to become an actual student."
                                                        hide merina20sad
                                                        show merina20
                                                        m "But enough of the sad backstories."



                                                        m "Have you seen Oliver by any chance?"
                                                        y "Didn't he leave with you?"

                                                        m "Yeah, but he gets distracted a lot."
                                                        m "I'm here because I forgot my staff, we're all a little empty headed from time to time."
                                                        un bored"Oh trust me, he knows that feeling, this place is a ghost town of thoughts."
                                                        m "I can't really look or wait for him, he'll most likely come back here sooner or later, when he does, can you do me a favor and look after him?"
                                                        m "Just follow him around, make sure he doesn't get into trouble."

                                                        y bored"Sure, I have nothing else to do anyway."
                                                        y simple"Does he get into trouble a lot?"

                                                        m "No, Ollie is a sweetheart, but a demon could walk beside him sometimes and he wouldn't notice."
                                                        m "And he sometimes seems to forget he is a vice leader, and some people are not nice enough to not take advantage of his nervous nature."
                                                        y "That does sound sad."
                                                        m "It's cute when he gets in {i}'the zone'{/i} as I call it, but it's bothersome when he misses meetings."

                                                        y s"I'll watch him like a hawk then."
                                                        y "Do you need me to pass any message to him?"
                                                        m "No, thank you, there's nothing too urgent, just occupy his time and mind, that would be enough."

                                                        y ec"Will do!"

                                                        m "I appreciate it."
                                                        m "I need to go now, leave it for the Headmaster to change plans around for no reason..."

                                                        m "I'll see you later."

                                                        y "It's my pleasure, and thank you for letting me know... everything about Tate."
                                                        "She gives a slow nod."
                                                        show merina20 at right with ease
                                                        m "Ah, another matter, keep in mind, Ollie is not much of a talker, especially around strangers or people he doesn't like, but you seem smart, you probably got that already from meeting him earlier."
                                                        hide merina20 with moveoutright

                                                        "She dips her head again and gives a polite smile before walking out the door."

                                                        jump ollietime



                                                        label tateadventure:

                                                        scene meetingroom
                                                        show cat20ec
                                                        show wolf20simple at right
                                                        show tiger20bored at left

                                                        y ec"Another adventure already?"
                                                        y "Sign me in!"

                                                        t "Woohoo!"

                                                        d "Are you sure, [name]?"

                                                        d "That seems a little dangerous for a first year, after all you'll be leaving the barrier, if Tate's previous adventures are any indication."
                                                        a "Yes, I think it's best that we come with."
                                                        hide cat20ec
                                                        show cat20angry
                                                        hide tiger20bored
                                                        show tiger20surprised at left
                                                        hide wolf20simple
                                                        show wolf20surprised at right

                                                        "Tate lets out a warning hiss, that is actually pretty scary."
                                                        "You're only ever afraid of a cat when the serious claws come out, and this is that kind of moment."
                                                        "Both guys are taken aback, even more than I am."

                                                        t "I think you forget I'm no longer a little baby you have to follow around everywhere."
                                                        t "Me and [name] can handle ourselves."
                                                        y smug"How dangerous can it be?"
                                                        hide tiger20surprised
                                                        show tiger20bored at left
                                                        hide wolf20surprised
                                                        show wolf20simple at right

                                                        d "Well..."
                                                        d "If we take out the few {i}'existence erasing'{/i} Nightfallen that were still roaming the forest..."

                                                        y simple"The existence- what now?"
                                                        play sound "audio/buzz.ogg"
                                                        "{i}*Bzzz*{/i}" with hpunch
                                                        a "Hold on..."

                                                        hide tiger20bored
                                                        show tiger20surprised at left
                                                        hide wolf20simple
                                                        show wolf20surprised at right

                                                        a "Shit, Dallan, Chelsie texted, we got a code {b}W{/b}."
                                                        hide cat20angry
                                                        show cat20simple
                                                        d "{i}*gasp*{/i} A witch hunt? Already?"
                                                        hide wolf20surprised
                                                        hide tiger20surprised
                                                        show tiger20iritated at left
                                                        show wolf20angry3 at right
                                                        a "Those damn defenders..."
                                                        d "I leave them alone for ten minutes and they commit atrocities..."
                                                        a "Alright, you two do whatever you want, but don't come back crying when you get caught by a pack of Nightfallen."
                                                        d "And be back before dinner time."
                                                        hide cat20simple
                                                        show cat21bored

                                                        t "Thanks for the warnings, dads..."

                                                        y simple"Wait, what was that about the exist-"

                                                        t "Let's go before they take out the ruler to make sure we're appropriately far away from each other."
                                                        hide wolf20angry3
                                                        show wolf20ec at right

                                                        d "Can't wait to hang out later!"

                                                        scene black with dissolve
                                                        stop music fadeout 3.0

                                                        "Not wanting any more distractions to stop the curious me from following him, the cat pushes me towards the door while covering my eyes."
                                                        "This way, I can't see any new people to intoduce myself to."
                                                        "Thankfully, this is the first floor, so no stairs to be wary of."
                                                        "We walk outside of the building, now standing on the main street, stretching all the way to the main gate."
                                                        "My questions from before remain unanswered."
                                                        "Existence- what...?"

                                                        scene outside2 with dissolve
                                                        play music "audio/happy3.ogg"

                                                        y s"So, where are we going?"

                                                        "I turn around to face the cat that now is trailing behind, even if he was the one most excited for this {i}'adventure'{/i}-"
                                                        "But he's gone."

                                                        y confused"What the-"

                                                        un tease"Ha ha, he ditched you already."
                                                        un "Probably looked at your fat ass for too long and changed his mind."
                                                        un "There are limits to how submissive and breedable someone can look before it's just too much."

                                                        "I'm not sure if I should be offended or not..."
                                                        play sound "audio/teleport.ogg"

                                                        show cat20teleport
                                                        show cat21smile1 with dissolve
                                                        hide cat20teleport with dissolve
                                                        "He reappeared!"

                                                        t "Sorry, I needed to check on something."
                                                        t "Shall we?"

                                                        y pf"That's ok, my heart totally didn't almost die from disappointment."
                                                        y s"As I was saying before you teleported away, where are we going?"

                                                        t "There's this abandoned place in the forest I like to hang out around, let's go there."

                                                        y "Sounds interesting."
                                                        un bored"More like creepy."
                                                        un "I'd ask for more information about this {i}'abandoned place'{/i}, but what do I know?"
                                                        un "I'm just an ancient, wise demon."
                                                        hide cat21smile1
                                                        show cat20smug

                                                        t "I see you're looking towards the main gate, and no."

                                                        y simple"No?"

                                                        t "No, I haven't used the main gate in years, so you won't either, why waste time walking when you can fly?"
                                                        hide cat20smug with dissolve
                                                        show catfly with dissolve

                                                        "He hops on his broom again, and signals to me to get on as well."
                                                        "I do as he wants, although very nervously."


                                                        scene black with longdissolve
                                                        stop music fadeout 3.0

                                                        "Very...very nervously, in fact, I might say this is a bit terrifying."
                                                        y worried"Oh God..."

                                                        scene chibitate2 with longdissolve
                                                        scene CGch8
                                                        play music "audio/wisp.ogg" fadein 3.0

                                                        t "What's the matter?"
                                                        t "We already flew together earlier."

                                                        y worried"Y-yeah, but like, four feet off the ground... not all the way over the academy's walls."

                                                        t "You'll be alright, even if you do fall, which won't happen, I can teleport AND make you float."
                                                        t "So there is almost zero percent chance for you to get injured."

                                                        y "That's reasonable."
                                                        t "And, you can hold onto me for extra security."

                                                        "I do exactly that, both for my safety and for a chance to touch his body."
                                                        "It was a little weirder than I thought, I already forgot his belly is completely exposed, so the heat and softness of his fur were a bit of a surprise."
                                                        "I instinctively stab my claws in his skin as we get off the ground, he winces but doesn't complain."
                                                        "He probably realizes I'm scared, even if, as he said, I basically can't hit the ground, ever, even if I fall"
                                                        "His hypothetical promise of safety is enough to calm my nerves, slowly, as we ascend."

                                                        scene chibitate22 with dissolve

                                                        "My negative emotions dial down together with my fear of heights, replaced by excitement, happiness and a bit of adrenaline pulsing through my veins."
                                                        "My claws also retract, leaving only my fingertips pressed against his belly."
                                                        "He visibly relaxes as well, thankful for the pain relief, and starts to purr softly and calmly."

                                                        y sadsmile"Sorry for the claws."

                                                        t "Meh, not my first rodeo."

                                                        y "This... this is actually really nice."

                                                        t "It's a great way to cool down on a warm day."
                                                        "He's going at a slow pace for me, although I know for a fact he would step hard on the gas if it were only him on this broom."
                                                        t "Hey, look over there."
                                                        "He points to my left, where the academy's rooftops rise on the hill, a park serving as its main campus, melting into the open streets full of residential houses and smaller buildings of the town."
                                                        "The sun, still up in the sky, is barely obscured by the top of the grand building."
                                                        "The shadow play is impressive."

                                                        y surprised"That's beautiful."
                                                        t "Perfect for flying, since the sun doesn't get all up in your face."

                                                        y s"Can you fly like this on any broom, or is this one special?"
                                                        t "I can use almost any object, even a chair, as long as I pump enough magic into it."
                                                        t "But I like brooms because they look cool in the air."
                                                        t "{i}Is that a plane, a bird, a witch?{/i}"
                                                        t "{i}No!{/i}"
                                                        t "{i}It's {b}Phantom!{/b}{/i}"
                                                        y confused"{i}Phantom{/i}?"
                                                        y "Is that a new nickname?"
                                                        t "Yeah, you know, I fly, and teleport, and my magic has this blue hue to it."
                                                        y bored"Please drop it."
                                                        t "Is it that bad?"
                                                        y "Almost as bad as {i}'Tartarus'{/i}."
                                                        t "Maan, I thought I had it this time , back to brainstorming then."

                                                        y simple"Speaking of teleporting."
                                                        y "Uhm, not to imply I'm not enjoying the ride, but wouldn't teleporting there be faster?"
                                                        t "I can only teleport a couple of times a day, and I already did about four times, plus taking someone with me takes a lot of magic."

                                                        y smug"I can get used to this."
                                                        y simple"I'm still not great with heights though."

                                                        t "We're almost there."
                                                        t "The secret is to clutch the broom with your thighs, not butt."
                                                        t "This way it's more comfortable, and you work out those thigh muscles."
                                                        y smug"Big thighs save lives, after all."
                                                        t "Waaay too many people would agree with you."

                                                        "We enjoy the slow ride in silence, I've never been on a plane, helicopter, air balloon or anything like that, so Tate lets me focus on the view."
                                                        "After some time, I start studying the peculiar cat's movements instead."
                                                        "He watches every bird that goes by with the corner of his eye."
                                                        "He keeps his ears extra sturdy, as if trying not to let the wind take his hoodie off, even if he never had it on in the first place."

                                                        "His head naturally seems to be attracted by different spots in the forest underneath us, like the lake, a flower rich hill that looks very warm and cozy, would love to lay in there someday, and the train tracks he mentioned earlier."
                                                        "It's only been a couple of hours since we first met in the forest, but I already have mixed thoughts about how to describe his personality. Up here, he looks peaceful and calm, but still curious."
                                                        "While on the ground, I find it hard to not pull him by the ears at times."
                                                        "Needless to say, I'm looking forward to spending time with him, and getting to know him better."


                                                        t "Ladies and gentlemen, if you look right below you to your left, you'll notice our final destination for the day."
                                                        t "Keep your seat belts fastened and your phones off, so we can land this thing without crashing."

                                                        y simple"We can crash?"

                                                        t "Sir! What are you doing in the captain's cabin?!"
                                                        y "You mean pilot?"
                                                        t "Oh, now you're teaching me about my own profession?"
                                                        y bored"Sorry, geez, I'll get back to my seat."
                                                        t "Thank you."
                                                        t "And for your information, no, we can't crash, I'm a master at flying, watch."
                                                        T "Although, hold tight."

                                                        "I learned not to take words like that for granted, so I hold on for dear life, with both my thighs and claws."
                                                        "And good thing I did, since Tate decided to do a loop in the air, just above the treetops."
                                                        y surprised"Woah!"
                                                        un cry"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH!" with hpunch
                                                        "My own surprise was cut short by Scribble's absolute terror filled scream."
                                                        un "AND VERY REASONABLY SO!"
                                                        un "TELL HIM NOT TO DO THAT AGAIN!"

                                                        y ec"Hey, that was fun, let's go again!"
                                                        t "I knew I liked you for a reason."
                                                        un "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!" with hpunch
                                                        stop music fadeout 2.0

                                                        scene black with dissolve

                                                        "We do two more loops before Tate finishes our descent."
                                                        "I had nothing to eat since morning, so I'm not afraid of getting sick."



                                                        "My feet touch the ground, and I take my first actual look around, seeing that we landed in a clearing in the middle of the forest."

                                                        scene forest2 with longdissolve
                                                        show catfly with dissolve
                                                        play music "audio/happy3.ogg"

                                                        t "What did you think?"
                                                        y smug"You sure know your way around a big piece of hard wood."
                                                        t "Ha! Wood really is my specialty."
                                                        "He sits sideways on the broom, floating in front of me."

                                                        "Scribbles, you ok?"

                                                        un cry"N-no, I think I'm sick."

                                                        "How? I'm completely fine."
                                                        un "I don't fucking know!"
                                                        un "Ughh, I'll get you back for this."

                                                        "I feel a bit bad for doing him dirty like that, but at least my 'pilot' had fun."

                                                        t "So, here we are."
                                                        t "I landed a bit farther away from our actual destination so I can give you some general directions."

                                                        y confused"General directions?"

                                                        t "If you take the path right behind me, you'll get to the main road, which you can take to get back to the academy, if you go forward, you'll get to an abandoned train wagon, it's waterproof."

                                                        y simple"Cool?"

                                                        y "Uhm, why do I need to know that?"

                                                        t "Just in case I mess up the coordinates when I come back."

                                                        y "Come back?"

                                                        t "It will take just a second."
                                                        play sound "audio/teleport.ogg"

                                                        show cat20teleport
                                                        hide catfly
                                                        hide cat20teleport with dissolve

                                                        y angry"Hey!"

                                                        un tease"Haaa!"
                                                        un "He left you for dead."
                                                        un "What a dumbass, following a stranger to the middle of the forest."
                                                        un "This is it, this is my revenge."
                                                        "You didn't do anything to contribute to this!"

                                                        un "Call it fate, darling."

                                                        "Shut up... I still have my phone for emergencies, but he said he'll be back."
                                                        "Although... what do I do till then?"
                                                        "What does one do alone in the woods waiting for a friend that might or might not come back for them?"

                                                        menu:

                                                            "Hmm... I could..."

                                                            "Take a look around.":
                                                                $ Tate_points +=1
                                                                y simple"I don't want to leave, obviously, he said he'll be back in a minute."
                                                                y "But I don't want to just sit here doing nothing."
                                                                un simple"Then let's take a look around."
                                                                un "I remember the scents of the forest, and memories are starting to flow."

                                                                "I choose a random direction, one that doesn't lead to the main road or the train tracks and walk that way, getting some branches out of my face."
                                                                play sound "audio/chirp.ogg" volume 0.3
                                                                "I am only a couple of steps away from the clearing, but something steals my attention."

                                                                y "Scribbles, did you hear that?"
                                                                un "Sounds like cries, very pitiful cries for help."

                                                                "Just ahead, at the bottom of a tall tree, stood a small, featherless chick."
                                                                "Pitiful indeed, as Scribbles mentioned, but not unworthy of kindness."

                                                                y worried"It must've fallen from its nest, I think I heard some more cries from above."
                                                                un curious"Are you gonna climb the tree?"
                                                                y bored"No, I'm gonna toss it back up like a tennis ball."
                                                                un simple"For real?"
                                                                y pf"No... obviously I'm climbing up."
                                                                un "Do you think it's ok to touch it?"
                                                                y simple"It's either that, or it dies on the ground, so I'll take my chances."

                                                                y sadsmile"It's ok little baby, I got you."

                                                                "I take a paper bag from my backpack, put the chick inside, place the bag between my teeth and get to climbing."
                                                                scene forest4 with dissolve
                                                                "I forgot I'm not that great at climbing, and the tree had no low branches, so it was extra hard."

                                                                un bored"A feline that can't climb trees?"
                                                                "We're not all expert climbers..."
                                                                "With a bit of struggle and a broken claw later, I get to my destination, and gently place the baby in its nest, along its two siblings."
                                                                un "Are you satisfied with your Samaritan deed?"
                                                                y ec"Yep."

                                                                un "Let's see you get down now."

                                                                y "..."
                                                                y "....."
                                                                un "..."
                                                                y bored"Fuck."
                                                                un bored"Yeah."
                                                                y simple"Can you help?"
                                                                un "I could cut down the branch you're on."
                                                                y bored"Then forget it."
                                                                t "{size=20}[name]?!{/size}"
                                                                t "{size=20}Heloooo?!{/size}"
                                                                y determined"Ha, never punished, suck it, Scribbles!"
                                                                y worried"OVER HERE!"
                                                                "A worried cat appears from between the rustling bushes."
                                                                "His eyes change to confused amusement when he sees me clutching a tree branch with all my limbs."
                                                                t "Now how did you get all the way there?"
                                                                y "I was saving a baby bird that fell from its nest..."
                                                                t "Awww, that's so sweet."
                                                                t "Let me help you."
                                                                scene black with dissolve
                                                                "He flies up above my head, I grab the end of his broom and he begins to slowly descend."
                                                                scene forest2 with dissolve
                                                                show cat20simple with moveinright
                                                                t "Was it alright?"
                                                                y s"Yeah, it was just a little scared."
                                                                hide cat20simple
                                                                show cat21sadsmile
                                                                "Tate looks relieved, and satisfied as well."
                                                                t "I was a little worried you went back home or something when I didn't see you here, didn't think your heart suddenly grew feet and ran to a bird's rescue."

                                                                y confused"Do I give off heartless vibes?"

                                                                hide cat21sadsmile
                                                                show cat21smile

                                                                t "Nah, far from it."
                                                                t "You might just be the second most wholesome person I've met, beside Dallan, nobody can be kinder than him."
                                                                t "He'd give you a kidney if you ask him nicely."
                                                                t "I tried and it almost worked, if I didn't tell him I don't actually want it."
                                                                y simple"That's... worrying."
                                                                t "Aaanyway, you didn't happen to bump into any nasty Nightfallen around here, right?"
                                                                y surprised"No, don't think I- Wait."
                                                                y angry"I forgot, this forest is filled with those guys, and you just left me alone like that?"
                                                                hide cat21smile
                                                                show cat21smug
                                                                t "Relax Cinderella, I was only gone for a minute or two, plus, I haven't seen any Nightfallen in this part of the forest for a while now."
                                                                y pf"Your reasons don't make me feel better."
                                                                t "Let's get a move on before the sun starts to set."

                                                                jump traintrack



                                                            "Take a seat and wait for Tate to come back.":
                                                                scene forest2
                                                                y simple"I guess I'll just wait for him, how long can that take?"
                                                                un "Famous last words."
                                                                "I take out my phone, happy that I have signal, even if it's faint."
                                                                "I was hoping for some fun notifications to interact with, but there was nothing other than a game update."
                                                                y "I should delete that game..."
                                                                un simple"How does this work?"
                                                                y "What?"
                                                                un "This device you're holding, how does it work?"
                                                                un squint"It's called a {i}'phone'{/i} as far as I remember."

                                                                y "Yeah, well..."
                                                                y "I'm not sure how it works."
                                                                y "I just know it uses satellite signals to connect to the internet and stuff."
                                                                un simple"I don't know half the words you just used."
                                                                y bored"I can't explain it any better, we can just call it fun magic."
                                                                un curious"How do you not know how a device your own kind made functions?"
                                                                y "I didn't make this, I just bought it, it's much more intricate than whatever YOUR kind had."
                                                                un bored"Doubt it."
                                                                un "Your kind is inferior in every way."
                                                                play sound "audio/teleport.ogg"
                                                                show cat20teleport with dissolve
                                                                show cat20ec with dissolve
                                                                hide cat20teleport with dissolve
                                                                "Our argument is cut short by a flash of blue light."
                                                                "Which surprisingly, didn't scare me as much as I thought it would."
                                                                t "Hey!"
                                                                y ec"Hey!"
                                                                t "I did it!"
                                                                y "You did it!"
                                                                y s"Uhm, what did you do?"
                                                                t "I came back exactly where I left off."
                                                                hide cat20ec
                                                                show cat21smile
                                                                t "I'm glad you're still here."
                                                                t "I was kind of worried you might've started to head home."
                                                                t "Or wander off to never be seen again."
                                                                y "That would be pretty stupid of me."
                                                                t "I don't know how smart you are exactly, I mean, you did get scammed into signing into the Sorcery Shard."
                                                                y pf"I was just naive, not stupid, and I didn't thanks to Dallan."
                                                                y simple"Unless... the whole signature gathering was just a ploy to make me sign..."
                                                                hide cat21smile
                                                                show cat21smug
                                                                y surprised"{i}*gasp*{/i} Was it?"
                                                                y "No...there's no...no way...right?"
                                                                t "I'll never tell."
                                                                y worried"God..."
                                                                t "A genius villain or fate, whatever interfered in your life clearly wanted you around me."
                                                                t "With that being said, you didn't meet any Nightfallen either, hopefully?"
                                                                y simple"Don't think so."
                                                                y angry"Hold up, I forgot, there are Nightfallen around!"
                                                                y "And you just left me here alone?!"
                                                                t "Oh stop fussing, I wasn't gone long enough for any of them to take your clothes off AND cum inside you."
                                                                y bored"Geez, very considerate of you."
                                                                t "Let's just go, before the sun goes down."
                                                                jump traintrack



                                                            "Take the main road back to the academy.":
                                                                $ betray +=1
                                                                scene forest2
                                                                y sad"I guess there's a reason he told me how to get back..."
                                                                un bored"Yeeep..."
                                                                y simple"Well, time to go..."
                                                                un "Yeeep..."

                                                                y "Are we far from the academy?"

                                                                un "I'd say about a mile, maybe a bit less."

                                                                y "It's not that bad, I should be back in twenty minutes or less."
                                                                scene forest3 with dissolve

                                                                "I start advancing through the bushes and low tree branches until I find the road the cat mentioned, and begin my walk back to the academy."

                                                                y sad"I don't even know how to feel..."
                                                                y "I feel worse now than when my date stood me up two years ago."


                                                                un tease"Look at the bright side!"

                                                                y simple"..."
                                                                y "And what would that be?"

                                                                un bored"Welp, if you can't find one, then I for sure can't."
                                                                un "Sucks to suck."
                                                                y bored"{i}*tsk*{/i}"
                                                                "I walk for another minute in silence, trying not to sulk too much, after all, I still have Dallan, Aiden and perhaps Merina and Ollie to hang out with."
                                                                "Maybe those guys won't leave me in the middle of the woods alone."
                                                                "Maybe that is the bright side."

                                                                un curious"Hey, do you hear that?"

                                                                y simple"Hmm?"
                                                                "Frantic rustle of leaves can be heard getting louder and louder."
                                                                "Then a crash."

                                                                show cat20dead with vpunch

                                                                t "Ouch..."

                                                                y surprised"Tate!"
                                                                y "You came!"
                                                                y simple"Are you alright?"

                                                                t "Yeah I'm fine."
                                                                t "I told myself I wouldn't do such abrupt landings anymore."

                                                                y worried"You don't seem too good, maybe-"

                                                                hide cat20dead
                                                                show cat21mad2

                                                                t "No! Don't change the subject."

                                                                y simple"What was the original subject?"

                                                                t "I told you to stay there, and I'd be back in a minute, and you actually decided to walk back?"
                                                                t "Just like that?"
                                                                t "Why did you agree to come with me in the first place?"
                                                                t "And to think I actually got the coordinates JUST right this time..."

                                                                y angry"Hey, don't put this one on me, you left me in a completely wild and unfamiliar territory and dipped!"
                                                                y "I didn't know if you'd be back or not, so I decided to not look like a fool and head back."

                                                                t "TWO minutes was all I needed."
                                                                t "Have a bit of faith in me, damn it."
                                                                t "At least start heading off after five."
                                                                hide cat21mad2
                                                                show cat21bored

                                                                t "But fine, I suppose I could've been more clear."
                                                                t "I just thought you'd be smarter..."

                                                                y bored"What was that?"

                                                                t "Let's agree to disagree."
                                                                hide cat21bored
                                                                show cat20angry

                                                                y "Agreed."
                                                                show cat20angry at right with move

                                                                t "Now are you coming or not?"

                                                                y angry"I'd love to..."

                                                                t "Then hop on the broom!"
                                                                hide cat20angry with moveoutright

                                                                t "We're going a little faster this time, since you wasted some precious time."

                                                                y sad"Sorry..."

                                                                t "Yeah yeah..."

                                                                t "...You scared me, you know?"

                                                                y simple"Why?"

                                                                t "As you said, this is a new territory AND it crawls with Nightfallen."

                                                                y "I completely forgot about that part..."

                                                                t "Luckily there aren't many around in this part of the forest these days."
                                                                t "Still, I'd hate myself if I let anything happened to you."
                                                                t "I knoooow, you're a 'special little guy', a recommended student, but still..."
                                                                scene black with dissolve

                                                                "We fly back to our original spot in silence the rest of the way."
                                                                "It really was stupid of me to walk away like that."
                                                                "What was I thinking?"
                                                                "I sure hope this wasn't like a...life altering decision or anything."


                                                                jump traintrack


                                                                label traintrack:

                                                                scene forestt with dissolve

                                                                "We walk side by side out of the clearing, our tails brushing against each other almost as much as our pelts and clothes touch the thick bushes all around."

                                                                "Somehow I didn't notice until now, but apparently, when he teleported back from his totally secret spot, he made a quick stop by the cafeteria."
                                                                "He hands me some kind of cheese filled pastry he brought in a small kitchen cloth, which I gladly accept, since I didn't eat anything since morning."
                                                                y s"This reminds me."

                                                                "I reach into my backpack and fish out two ham sandwiches my mom prepared for my lunch, and hand one to Tate."
                                                                "We munch ravenously on the gluten rich meal while walking further, a happy tune escaping Tate's throat at times."
                                                                t "Did your mom cut this ham straight off an Angel's thigh, because it's heavenly!"
                                                                y "She likes to marinate individual slices since she doesn't think the store does a good enough job with the seasoning."
                                                                t "Brilliant."
                                                                "The small plastic wrap from the sandwiches gets picked up by the wind as I was trying to throw it back in the backpack, getting stuck in a bush."
                                                                "Tate quickly sprints towards it, grabs it, as well as an old candy wrap that was lying on the grass floor nearby, and comes back."
                                                                "It's safe to say he doesn't appreciate litter."
                                                                "We share a water bottle as well, and once we're done, I decide to press for information."
                                                                y simple"Hey, Tate?"
                                                                t "Sup?"
                                                                y "Why did you leave all of a sudden earlier anyway?"
                                                                stop music fadeout 3.0

                                                                t "Here we are, my favorite spot!"
                                                                scene tatetrain3 with longdissolve
                                                                t "Or one of them at least."
                                                                play music "audio/pianorelax.ogg" fadein 3.0

                                                                y confused"The train tracks?"
                                                                y "Ok?... but why did you leave m-"
                                                                "He puts his finger up against my lips, hard enough that I can feel the pressure on my teeth."
                                                                t "Shhhh."
                                                                t "Tell me, dear [name]."
                                                                t "Do you live with your mother, still?"
                                                                y simple"Is it that obvious?"
                                                                t "Fatherless as well?"
                                                                y "Accurate again."
                                                                t "How many sexual partners did your mother have in the past year?"
                                                                y blushmad"What the fuck?"
                                                                y "How should I know?"
                                                                y "A-and more importantly, why would I ever tell you that?"
                                                                t "See?"
                                                                t "There are things you don't want to tell me for personal reasons, and I won't make you."
                                                                y bored"Ah."
                                                                y "I understand now..."
                                                                y simple"But I think it's unfair to compare that to why you left me alone in the forest for a while."

                                                                y pf"I mean, how would you like it if I asked about your dad's riding rounds with your mom?"
                                                                show cat21smug with dissolve
                                                                t "Wouldn't bother me."
                                                                "His smirk is kind of bothering me."
                                                                y "Alright then, how many?"
                                                                t "Zero."
                                                                y simple"..."
                                                                y bored"They're separated as well, got it."
                                                                y pf"Well, in that case, how many dates did either of them go to in the last two years?"
                                                                t "Zero."
                                                                "His smugness is still there."
                                                                y angry"H-how many times did any of them kiss you on those fluffy cheeks of yours?"
                                                                t "Zero."
                                                                y simple"Damn, strict parents."
                                                                y "Birthdays?"
                                                                t "Zero."
                                                                y worried"Hugs?"
                                                                t "Zero."
                                                                y simple"Wow, your parents must really hate y-"
                                                                un squint"Holy shit, he doesn't have parents, you fucking dumbass!"
                                                                y "Oooooh..."
                                                                y "You're an orphan..."
                                                                t "Finally."
                                                                y "I'm so-"
                                                                hide cat21smug
                                                                show cat21bored
                                                                t "Oh but hold your pity, it's been a loooong while now, it doesn't affect me."
                                                                t "I've decided a long time ago I won't sulk, depressed, disconsolate, sorrowful, dejected or miserable all day."
                                                                t "I hate sad people."
                                                                hide cat21bored
                                                                show cat20smile
                                                                t "There's always something to smile about, like these!"
                                                                hide cat20ec with moveoutleft
                                                                scene tatetrain with longdissolve
                                                                scene CGc2
                                                                "He hops on one of the shining, red, steel beams and tries to hold his balance with his arms."
                                                                "His tail is moving uncontrollably, coiling and swinging making him lose the balance his limbs try so hard to keep."
                                                                "So I give him a helping hand which he happily accepts."
                                                                t "Or this."
                                                                "He squeezes my hand a little tighter, making me blush."

                                                                y blush"I was wondering throughout the day why you know so much about the academy."
                                                                y "And a lot of people know you well despite being a first year like me."
                                                                y "I'm guessing you've been living here for at least a couple of years now."

                                                                t "Wow, it's your turn with our shared brain cell, it seems."
                                                                t "You're right."
                                                                t "The academy building was my playground for as long as I can remember."

                                                                y simple"The building itself?"

                                                                y "It doesn't seem like the best place for a child to be around."
                                                                y "Aren't there sex classes and what not, constantly being taught here?"

                                                                t "There are, but don't worry your little head."
                                                                t "Those meanies made sure I didn't participate, look inside, hear about it or spontaneously teleport inside any classrooms."
                                                                t "The windows were one sided, Aiden placed anti teleportation fields around classrooms, Dallan would lock the doors, and if I did come close, Merina and Chelsie would just push me down the hallway on icy floors."
                                                                t "Kudos to them for taking such precautions, but sixteen-year-old me was REALLY pissed off."


                                                                y "I'm surprised the old Headmaster didn't do anything about it."
                                                                t "Hey hey hey, he was the BEST gosh darn Headmaster this place has ever had, unlike that coward excuse of a lion."
                                                                y "He got under your skin that much, huh?"
                                                                t "You could say that."
                                                                y "Were you the only kid that decided to hang around the academy?"
                                                                t "Kids aren't allowed even close to the main building."
                                                                y "So why you?"
                                                                t "I was... an exception."
                                                                t "The Headmaster, the previous one, mister Sebil, is technically my father, adoptive, obviously."
                                                                t "They never had children, and I never liked staying alone at home or with the babysitter, so I hung around the academy."
                                                                t "I got to meet Dallan, Chelsie, Merina and everyone else."
                                                                t "And with Aiden I have a more special relationship."

                                                                y confused"More special?"
                                                                t "He's adopted too, but we're complete polar opposites."
                                                                t "He likes to think he hates me, but I know the truth."
                                                                t "We were both adopted when we were six, and his dads forced him to get along with me once they found out about me."
                                                                t "Obviously he's older."

                                                                t "That's all I'll say about him."
                                                                t "If you want more information, you should probably ask him sometime."

                                                                "For now, I'm a bit more interested in the guy that's holding my hand, and chuckling every time our eyes meet."

                                                                "The railroad has no end in sight as we keep walking downhill."
                                                                "Beautiful blue butterflies flutter around now and again, as the sun's rays lose more degrees in angle by the minute, and their now golden fiery touch graze our intertwined hands."
                                                                "The rays are probably touching more than that, but I don't care about anything else, as there's nothing more important at the moment, than knowing I contribute to giving this cat a genuine smile on his face."
                                                                "His tail has been quiet and relaxed for some time now, used gracefully for balance, so my hand becomes useless in his, but as long as he doesn't ask for his hand back, why would I give up on it?"

                                                                y simple"Can I ask you something?"
                                                                t "As long as it's not about my hypothetical parents' love life."
                                                                y s"Heh, it's not."
                                                                y "How come this is your favorite place around?"
                                                                y "Not to say the view is not beautiful or worthwhile, but why this part of the forest?"

                                                                t "For starters, the train that passes once a month or so is scary enough that it keeps Nightfallen away."
                                                                t "That means I can camp in peace!"

                                                                t "Do you like camping, [name]?"

                                                                y smug"Why wouldn't I like to sleep in unpredictable weather, get sucked dry by insects and not have any technology around for my basic needs?"

                                                                t "Pff, okay, city boy."
                                                                t "You're missing out."

                                                                y s"Do you camp often?"

                                                                t "Almost everyday."
                                                                y surprised"Really?"
                                                                y simple"Do you not... have a-"


                                                                t "You are really pessimistic, you know that?"
                                                                t "I do have a home, and SHOCKING! I share it with my adoptive parents."
                                                                t "But I prefer the wild."
                                                                t "I'm gonna have to take you to my super cool tent some time."

                                                                y ec"I'd be lying if I said I don't want to see it."

                                                                "The rails split in two at one point, and I follow the one Tate chooses."

                                                                "Not much further along, we find a derailed locomotive and a wagon, old, rust starting to eat it away, and plants surround it."
                                                                "Surprisingly, one of the lights is still somehow functional."
                                                                y simple"That must be disturbing to the few trains that pass through here."
                                                                t "Having to watch the corpse of one of their kind just chilling here?"
                                                                y "Yep."
                                                                stop music fadeout 3.0
                                                                scene junkyard with longdissolve
                                                                "Behind some more greenery, a small junkyard catches my eye, which is apparently our final destination."
                                                                play music "audio/happy20.ogg" volume 0.3

                                                                show cat20smile with moveinleft


                                                                t "So, what's your whole deal?"

                                                                y simple"What do you mean?"

                                                                t "Your powers and stuff."
                                                                t "You must be pretty powerful if you were recommended."

                                                                y "Oh, that."
                                                                y "I can manipulate energy to some extent."
                                                                hide cat20smile
                                                                show cat20

                                                                t "That is SO cool!"
                                                                t "Energy manipulation? I've heard stories about you guys!"

                                                                y simple"Stories?"
                                                                hide cat20
                                                                show cat20smile

                                                                t "Yeah, fairytales mostly, since there weren't many people with that kind of magic in some time."
                                                                t "One of the few topics outside of academy history I've been told stories about."
                                                                t "Like this one prince, who brought his kingdom a huuuge energy crystal by slaying a dragon."
                                                                t "He used his magic to weaken the beast, then further to spread the crystal's energy to everyone, bringing people light."
                                                                t "Are you also a magical prince with the power to slay dragons?"
                                                                y "I doubt I'm THAT powerful."
                                                                t "Demons?"
                                                                un bored"Don't you dare answer that one."
                                                                "I shrug."
                                                                hide cat20smile
                                                                show cat20simple

                                                                t "A savage Nightfallen?"
                                                                y awkward"M-maybe?"
                                                                t "A... slime?"
                                                                y "...yes..."
                                                                hide cat20simple
                                                                show cat21bored
                                                                t "You don't seem too sure."

                                                                hide cat21bored
                                                                show cat20smile

                                                                t "Well, no matter, as long as you have some magic, maybe you can help me out with my little training?"
                                                                y awkward"What kind of training? I'll help with any training!"
                                                                "Anything to stop being questioned..."

                                                                t "I'm trying to use my magic to teleport things around without touching them."
                                                                y s"That seems pretty useful."
                                                                y "What do you want me to do?"

                                                                t "First off, if I collapse from exhaustion I'll need you to carry me on your back aaaall the way back."
                                                                y bored"Not gonna happen."
                                                                hide cat20smile
                                                                show cat20smug
                                                                t "Heh, I know, noodle arms, I'm joking."
                                                                hide cat20smug
                                                                show cat20smugclose
                                                                "He comes closer and starts poking my hands, biceps, armpits and ending with the belly."
                                                                "The most vulnerable part... foul play."

                                                                y ec"haha, stop it, stop, T-Tate p-please."
                                                                y angry"I SAID STOP!"
                                                                hide cat20smugclose
                                                                show cat20smile
                                                                t "Damn, you're really soft."
                                                                y simple"Thanks?"
                                                                t "But seriously, the thing is, I already have the ability to teleport things at a distance if I hit them with a spell."
                                                                hide cat20smile
                                                                show cat21smug
                                                                t "Like this."
                                                                show stick1 at left with moveinleft
                                                                "He throws a stick up in the air and points his finger at it."
                                                                show stick2 at left with dissolve
                                                                hide stick1
                                                                t "Bang."
                                                                "A small ball of light, the size of a marble hits the stick and it disappears-"
                                                                hide stick2 with dissolve
                                                                show stick2 at right with dissolve
                                                                show stick1 at right
                                                                hide stick2 with dissolve
                                                                "Reappearing a couple of feet away."

                                                                y surprised"Woah! That is a super creative usage of your power."
                                                                hide stick1 with moveoutright
                                                                t "Glad you can see my overwhelming talent."
                                                                hide cat21smug
                                                                show cat20
                                                                t "But I want to do it purely with my MIND!"
                                                                t "I'm not sure what to do exactly to achieve that, and seeing how you're a recommended student-"
                                                                "Not this bs again..."
                                                                t "I thought you could give me some tips."
                                                                hide cat20
                                                                show cat20determined
                                                                t "That is your role today."
                                                                t "Be my tip guy."
                                                                y awkward"Uhmmm."
                                                                t "Come ooon, give it to me."

                                                                un tease"You heard the guy, give him your tip."
                                                                "I don't know any, how could I?"
                                                                "Please tell me you can help me."
                                                                un curious"You don't know ANY tips?"
                                                                un "Your whole thing revolves around mind magic."
                                                                un ang"The only reason you weren't influenced by MY mind control spell, is because of your supposedly superior mind magic!"
                                                                "I didn't ask for an argument, just tell me if you can help or not, I don't want to disappoint him!"
                                                                un bored"{i}*sigh*{/i}"
                                                                un "I'm not well versed in transportation spells, but one of the first steps in casting spells with your mind is strong emotions."
                                                                un "At least for beginners."
                                                                un "It would also help to see how much he ACTUALLY knows first."

                                                                y s"Alright, but before that, can you show me how far you've gotten with your efforts until now?"
                                                                t "Certainly, watch this!"
                                                                stop music fadeout 2.0
                                                                show leaves1 at left2 with moveinleft

                                                                play sound "audio/button.ogg"

                                                                "He picks up some leaves from the ground, takes a deep breath, then throws them in the air."

                                                                show cat20leaf1 with dissolve
                                                                hide cat20determined
                                                                play sound "audio/button.ogg"

                                                                "As the small, slightly withered leaves descend slowly, he places his fingers on his temples, and directs his bulging eyes towards the falling leaves."

                                                                hide leaves1 with dissolve
                                                                show leaves2 at left2 with dissolve
                                                                hide cat20leaf1
                                                                show cat20leaf2
                                                                play sound "audio/button.ogg"
                                                                "We both follow them with our gaze..."

                                                                hide leaves2 with dissolve
                                                                show leaves3 at left2 with dissolve
                                                                hide cat20leaf2
                                                                show cat20leaf3
                                                                play sound "audio/button.ogg"
                                                                t "..."
                                                                hide leaves3 with dissolve
                                                                show leaves4 at left2 with dissolve
                                                                play sound "audio/button.ogg"
                                                                y simple"..."
                                                                hide leaves4 with dissolve
                                                                play sound "audio/button.ogg"
                                                                t "....."


                                                                y bored"So nothing?"
                                                                play sound "audio/button.ogg"

                                                                hide cat20leaf3
                                                                show cat20tired
                                                                t "Nothing."
                                                                play sound "audio/button.ogg"
                                                                hide cat20tired
                                                                show cat20
                                                                t "So far!"
                                                                play music "audio/happy20.ogg" fadein 3.0 volume 0.4
                                                                t "But that's why I need your help."

                                                                y simple"Do you even know if mind casting is possible for teleportation?"
                                                                t "Yes, mister Sebil tried to teach me sometime ago, but he gave up fast saying I still need a couple of years of training..."
                                                                t "'Maybe when you're a senior'."
                                                                t "Yeah, sure, like I'm going to wait that long."
                                                                hide cat20
                                                                show cat20determined
                                                                t "Now give me some wisdom, recommended boy!"

                                                                y s"Alright, here is the first share of wisdom."
                                                                y "Strong emotions are a good catalyst for mind spells."
                                                                hide cat20determined
                                                                show cat20smile

                                                                t "So, I should think of something that evokes strong emotions, huh?"

                                                                y "That's basically it."

                                                                t "Hmm, let me try."
                                                                hide cat20smile

                                                                show cat20leaf2
                                                                show leaves2 at left with dissolve

                                                                "He does the same thing with the leaves, and the exact same gestures."
                                                                hide leaves2 with dissolve
                                                                hide cat20leaf2
                                                                show cat20laugh
                                                                "Except that this time, when the leaves fall, he erupts into laughter."

                                                                y simple"What's so funny?"
                                                                y "What were you thinking about?"
                                                                t "AHahaha, s-sorry, hAha."
                                                                t "I was just imagining you naked."


                                                                y blush2"What's so funny about that?"
                                                                hide cat20laugh
                                                                show cat21smug
                                                                t "Oh, you know..."

                                                                y blushmad"Stop saying I know stuff, I literally don't!"
                                                                t "Aww, you're blushing, you're so cute."
                                                                y "..."
                                                                y bored"You're lucky compliments work well on me."

                                                                hide cat21smug
                                                                show cat21simple

                                                                t "Your tip didn't work, by the way."
                                                                y angry"Well you're not supposed to think of something funny!"
                                                                y simple"I was referring more to anger, sadness, depression, stuff like that."

                                                                t "Hmmm..."
                                                                t "I don't really have things to be unhappy about."
                                                                hide cat21simple
                                                                show cat20smug1
                                                                t "Especially now, since you're here."

                                                                "I continue to stay red faced while he winks at me."

                                                                "Do you have any other means to help, perhaps?"

                                                                "Scribbles?"
                                                                un bored"Emotional attachment might help, if he tries to teleport something small, with personal value, he might be able to do it."

                                                                y simple"Do you have any small, light object that you care about?"
                                                                hide cat20smug1
                                                                show cat20smile
                                                                t "A lot of things, why?"

                                                                y"Use one of them instead of the leaves, objects with emotional value might be easier to touch with your mind alone."

                                                                t "That makes sense."
                                                                hide cat20smile
                                                                show cat21simple
                                                                t "Well, let's see..."

                                                                "He searches through his pockets, which hold more things than I expected."
                                                                t "I have Merina's hair pin, she gave it to me in my long hair phase."
                                                                y simple"I'd love to see a photo of that."
                                                                t "Aiden's mini dagger's sheath he {i}'lost'{/i} last year."
                                                                y "Hope he doesn't find out you have it."
                                                                t "Dallan's recommendation letter for me."
                                                                y "You just carry that one around?"
                                                                t "Sometimes, because why not?"
                                                                hide cat21simple
                                                                show cat21smile zorder 1
                                                                t "Oh, and this."
                                                                show daisy1 zorder 2 with dissolve
                                                                "He takes out one last item, from an inside pocket in his cropped jacket, a plastic daisy, uncannily perfect, which is exactly what gives away the fact that it's fake."
                                                                t "This was... a gift."
                                                                t "I'll try it with this."
                                                                hide cat21smile
                                                                show cat21sadsmile zorder 1
                                                                show daisy1 zorder 2

                                                                "He ponders throwing it in the air like the leaves, but stops."

                                                                t "Can you..."
                                                                t "Hold this, for a moment."
                                                                hide daisy1 with dissolve

                                                                y simple"Alright."

                                                                hide cat21sadsmile
                                                                show cat21close

                                                                "Once again, he takes a deep breath, this time holding it in for longer, with his eyes closed and a serious expression on."
                                                                "He concentrates on the daisy in my palms, and it begins to glow a faint light blue shade, rising less than an inch in the air."
                                                                show daisy2 with dissolve
                                                                show daisy1 with dissolve
                                                                hide daisy2 with dissolve
                                                                "Before disappearing completely, and reappearing in his hands, that are now cupped close to his chest."
                                                                hide cat21close
                                                                show cat21simple

                                                                y ec"You did it!"

                                                                "It takes a moment for him to realize, but once his eyes lock with the daisy again, he grins."
                                                                hide daisy1 with dissolve
                                                                hide cat21simple
                                                                show cat20ec

                                                                t "I did it!"

                                                                y ec"High five!"
                                                                show cat20ec with hpunch

                                                                "We do a double hand smack as we giggle to the victory."
                                                                t "Mind magic Mind magic Mind magic!"
                                                                y ec"Mind magic Mind magic Mind magic!"
                                                                hide cat20ec
                                                                show cat21smile

                                                                t "It's probably going to be useless for now, but I'm glad I at least know I can do it."
                                                                t "Might come in clutch at some point."
                                                                hide cat21smile
                                                                show cat21smile1
                                                                t "Thanks for the tips!"
                                                                t "I knew you'd know what to do."

                                                                y s"You're welcome, and hey, it might be useless now, but give it some practice, and maybe you'll be able to teleport other people with your mind!"

                                                                hide cat21smile1
                                                                show cat21smug

                                                                t "Are you sure you'd want that?"
                                                                t "Then my power would be limitless."

                                                                y smug"As long as it makes you happy."

                                                                hide cat21smug with dissolve

                                                                "We sit down on the grass, by the train tracks, as Tate continues to practice teleporting the daisy, the pin, the letter and the dagger sheath from one of my hands to the other, since he's not allowed to touch any of them if we want this to work."
                                                                "Every time he does, a laugh crosses his face, a frown or even a tear."
                                                                "I suppose Scribbles' emotion tip worked way better than anticipated."
                                                                "Although I do wonder what he thinks about every time."

                                                                "Minutes pass as we play around and talk about each other's powers."
                                                                "Unfortunately my phone charging ability was not as impressive to him as it would've been for almost anyone else, since he doesn't have a phone, and never did."
                                                                "Then, his face starts to sour, unexpectedly."

                                                                show cat21sad with dissolve
                                                                "A bored, melancholic gaze in his eyes."









                                                                t "..."


                                                                t "Sorry I dragged you all the way over here."

                                                                y confused"Huh?"
                                                                y "Why?"
                                                                y "Where is this coming from?"

                                                                t "I don't know..."
                                                                t "Dallan and Aiden were right, I should've played the tour guide more today, since I know so much about the academy from stories and experience, instead of dragging you in the middle of nowhere."
                                                                t "To do whatever we're doing right now."
                                                                t "It's the least I could do after you helped me so much."

                                                                "This really took me by surprise."
                                                                "I didn't expect this sincerity coming from him."
                                                                "He seems genuinely sorry, even if he really shouldn't be."

                                                                un bored"You are very easy to fool, manipulate and gaslight."
                                                                un eyeroll"By anyone but me, apparently."
                                                                un bored"Just you wait until I get my extremely hot body back."

                                                                y sadsmile"I don't think you should've changed anything."
                                                                y "I had fun today, and I learned stuff."

                                                                hide cat21sad
                                                                show cat21simple

                                                                t "You did?"
                                                                t "Like what?"

                                                                y smug"I know what a Narnian carpenter did in 1994."

                                                                hide cat21simple
                                                                show cat21smile

                                                                t "Heh, at least I'm not the only one cursed with that useless information now."

                                                                y"I know where I can go if I want to enjoy nature without the worry of Nightfallen creeping in every corner."
                                                                y "Doubt many people beside you know about that."
                                                                hide cat21smile
                                                                show cat21smile1

                                                                t "That's true..."

                                                                t "And I suppose that the test the Headmaster wants us to complete must include some forest ventures, if I know him well enough."

                                                                y ec"So then it's good that I get familiar with it!"

                                                                y smug"Plus, who said I care about all these technicalities."
                                                                y "I much rather work on unlocking new amazing abilities, like you did today."
                                                                y ec"Or soar the skies on a broom."

                                                                hide cat21smile1
                                                                show cat21sadsmile


                                                                t "Can I trust that you're not just saying this?"
                                                                t "Do you mean it?"
                                                                t "I won't be mad if you don't."
                                                                t "I much prefer honesty and loyalty over white lies, even if they might hurt sometimes."

                                                                menu:
                                                                    "Do I actually rather have fun and fool around instead of learning about the academy, or am I just trying to make him feel better?"

                                                                    "I absolutely mean it. (Truth)":
                                                                        y ec"I swear I mean everything."
                                                                        y smug"I really hope I didn't cement myself as a boring nerd in your eyes, because I expect you to take me on more adventures in the future."
                                                                        show cat20ec with dissolve
                                                                        hide cat21sadsmile with dissolve

                                                                        "If the sun were to disappear right now from the horizon, I wouldn't know, since it has just risen on Tate's face."
                                                                        un squint"That's so cheeeeesy, bleh."
                                                                        t "Oh trust me, I have things planned out already, just the two of us!"
                                                                        y surprised"Already?"
                                                                        hide cat20ec
                                                                        show cat21smile1
                                                                        y "We met today."
                                                                        t "You get to know a person best in the first, like, what? Three? Seven minutes?"
                                                                        t "I have enough information gathered about you to make somewhat correct assumptions."
                                                                        y smug"Is that so?"
                                                                        y "I suppose you're making some sense there."
                                                                        y "And I can't fight against nature."
                                                                        hide cat21smile1
                                                                        show cat21blep
                                                                        y s"Being friendly is just in your blood."
                                                                        "He looks at me with eyes closed and tongue out."
                                                                        "Stop being so goddamn cute..."
                                                                        "Spontaneous topic change time."
                                                                        jump afterlie




                                                                    "There might be a lie or two in what I said. (Truth)":

                                                                        y awkward"Alright, I might've exaggerated how much fun I actually had, just a tiiiny little bit."
                                                                        hide cat21sadsmile
                                                                        show cat21smug
                                                                        t "A-hah."
                                                                        t "I had a little nudge."
                                                                        t "I appreciate the honesty, even if it's a bit disappointing."
                                                                        t "It just means I have to try harder."

                                                                        y confused"A {i}'nudge'{/i} you say?"
                                                                        y "Why?"
                                                                        t "You're a little... unadventurous."
                                                                        y bored"You think I'm boring?"
                                                                        y angry"I'm not boring!"
                                                                        y "I can be lots of fun!"




                                                                        t "It's not that I don't believe you, it's just that you didn't give me reasons to trust you on that."

                                                                        un bored"Pretty wise words from such a foolish cat."

                                                                        y bored"Let's just change the topic."
                                                                        jump afterlie




                                                                label afterlie:

                                                                scene junkyard
                                                                show cat20smile


                                                                y simple"If I may ask, why did you need to get out of detention so desperately?"
                                                                y "It didn't seem like that's your first visit there."
                                                                hide cat20smile
                                                                show cat20simple

                                                                t "..."
                                                                t "You're right, I'm quite familiar with punishments, but this time, I had reasons to not want to be stuck there for hours."
                                                                y "Such as?"

                                                                t "It's the same reason I teleported away earlier."
                                                                y "Ah, I get it, then I won't press further."
                                                                y "I'm assuming I won't get an answer anyway."
                                                                hide cat20simple
                                                                show cat21sadsmile

                                                                t "Thanks..."
                                                                t "That reminds me, do you mind if I leave you alone for just a second again?"

                                                                y "If you must, I won't stop you."
                                                                y bored"But if a more adventurous Nightfallen decides to come near the iron-monster's tracks, then my death will be on you."
                                                                hide cat21sadsmile
                                                                show cat20smug
                                                                t "You're hot enough to attract their dicks, not their claws."
                                                                y "That is sooo reassuring."
                                                                t "Be back in a sec."

                                                                t "Thank you again, [name]."
                                                                play sound "audio/teleport.ogg"

                                                                show cat20teleport
                                                                hide cat20smug with dissolve
                                                                hide cat20teleport with dissolve

                                                                un simple"Cool, you have another free minute."

                                                                un "If not a Nightfallen, hopefully no wild animal will come give your face a taste while we're at it either."

                                                                y smug"I only let cute cats taste this face."

                                                                un suspicious"Stop, literally stop."

                                                                un "I wanted to teach you a very useful spell in the meantime, but you're too distracted by your cat addiction to-."

                                                                y surprised"No no no, wait!"
                                                                y "I'm sorry, I want to learn new spells!"
                                                                y "If there are spells I can learn in under a minute then bring them on! That would be awesome!"
                                                                y s"In fact, you should've said something about that earlier!"
                                                                y "Way earlier."

                                                                un bored"I don't feel like sharing all my ancient knowledge with you just yet, so I'm doing this for two reasons."
                                                                un "One, this spell is easy to get anywhere."
                                                                un "With or without me, you might find it sooner or later."
                                                                un "And two, it might be crucial for your survival."
                                                                y simple"That's ominous, what spell is that?"
                                                                un "Teleportation Canceling."

                                                                y "How is that {i}'crucial'{/i}?"
                                                                un "That cat is one hundred percent going to murder you, he's giving off serial killer vibes."
                                                                y bored"That's because you don't know what a 'friend' is."
                                                                un ang"Are you calling me a loser?!"
                                                                y "I'm calling you uninformed."
                                                                y simple"Tate is a little weird and full of energy, but definitely harmless."
                                                                y "Anyway, even if I don't think it's that important, I'd still want to learn it, I want as much magic as possible."
                                                                y s"What do I have to do?"

                                                                un bored"Fine, just disregard my warnings and use me for your own benefit."
                                                                un "I'm used to it."
                                                                y smug"Yeah yeah {i}{b}grandpa{/b}{/i}, can we get on with it?"

                                                                un "{i}*sigh*{/i}."



                                                                un "First off, find a big stick, a branch, if you may."

                                                                y simple"Alright, let's see."

                                                                "Surprisingly, there aren't many fallen branches around, most likely a result of the lack of wildlife and Nightfallen around the train tracks."

                                                                y "Where do I-"

                                                                un "Just break one off from a tree, it ain't that deep..."

                                                                y bored"Sure, let me just violate a tree real quick."

                                                                show branch1 with dissolve

                                                                "I find a low hanging branch, with the least amount of leaves on it, one that is starting to wither, and break it off."

                                                                y s"Here, now what?"

                                                                un "If you'd allow me, I'd like to use magic to shape it a bit."

                                                                y "Permission granted."
                                                                hide branch1 with dissolve
                                                                show branch2 with dissolve

                                                                "I feel a tiny bit of magic being drained from me, as the bark starts to crack and fall, leaving the naked wood underneath, then even that gets smoothed out."
                                                                "The final product feels almost polished."

                                                                y s"Cool, what now?"

                                                                un simple"Now you take this new and improved branch..."

                                                                un ang"And go fuck yourself with it."
                                                                un "Nobody calls me a grandpa you absolute doorknob."


                                                                y angry"Damn it Scribbles!"

                                                                y "I said I'm sorry!"

                                                                un "No you didn't!"
                                                                un "I would've accepted an apology, but you didn't bother to formulate one!"


                                                                y worried"Then I'm sorry! Ok?"
                                                                y "I got a bit excited about a new spell."

                                                                y simple"You're not a grandpa, you're a sexy, youthful man."
                                                                un sidee"Now call me a dilf."
                                                                y simple"What?"
                                                                y confused"Do you know what that is?"
                                                                un sidee"Your mind mentions this word a lot, so I'm familiar."

                                                                y bored"Are you even a dad?"

                                                                un suspicious"No, but I like the idea and how it sounds, so do it or else no spell for you."
                                                                y "..."
                                                                y pf"You're... a dilf."

                                                                un pride"Why thank you very much for noticing."
                                                                un "Oof, is it hot in here or is that just me?"
                                                                play music "audio/happy20.ogg" fadein 2.0 volume 0.3

                                                                y bored"Can we pleaaase resume our business?"

                                                                un bored"Alright, fine, here is the real deal."
                                                                hide branch2 with moveoutright
                                                                "I throw away the smooth branch that I only now realize looks a lot like a dildo."
                                                                "Maybe a bear or something can have fun with it..."

                                                                un "You probably remember the spell is done through a snap of fingers."
                                                                un "In order for the snap to take effect, you need to, one:"
                                                                un "Have the person who's magic you cancel in your vision."
                                                                un "And two, you need a secondary soul to play the role of catalyst."
                                                                un "And that secondary person will lose all their magic for the duration."
                                                                un "Otherwise, if you use this spell on your own, you will cancel both the teleportation, and your own magic altogether."
                                                                y "In other words, I can't learn this, who am I gonna use as a catalyst?"
                                                                un "It's me, genius."
                                                                y simple"Oh."
                                                                un "I'm technically another soul inside your body."
                                                                un "You can't be seen using my magic anyway, so if you ever need to cancel teleportation, it wouldn't matter whether or not I can use spells."


                                                                y "Can just anyone learn this then, as long as they have a person as a catalyst?"
                                                                y "That would make Tate's whole thing kind of... useless."

                                                                un "No, not just anyone."
                                                                un "You need a person you trust with your life, and since we share the same body, technically I have no choice but to trust you with my life."
                                                                un "Although it is easy to learn, only those with light, energy or trickery focused abilities can use it."
                                                                un "Like that tiger friend of yours."
                                                                un "Plus, if someone ten times bigger and stronger than the cat cancels his magic without a second soul, it wouldn't matter, since they could just crush the cat with pure strength."
                                                                un "All that matters is to not let your opponent escape."

                                                                y "I see."
                                                                y "I wonder who Aiden's secondary person is..."



                                                                un "So then, are you ready to learn?"

                                                                y "I'm not sure..."

                                                                un simple"W-what?"
                                                                un squint"The fuck do you mean you're {i}'not sure'{/i}?"
                                                                un "Why did I bother explaining everything to you then?"

                                                                y simple"The problem is that I don't know how Tate would react if he knew I suddenly learned a specific spell just to counter him."
                                                                un suspicious"How, in the actual fuck, is he supposed to know you learned the spell in this exact moment, and not like, five years ago?"

                                                                y worried"I don't know, it just feels weird."

                                                                un "Fine, in that case, give me your final answer right now, if it's a no, you'll have to find the final steps on your own someday."
                                                                un "Because I'm already humiliating myself enough to take this audacity from you, I'm not opening my schedule for whenever you change your mind."

                                                                menu:
                                                                    "Should I learn a teleportation canceling spell?"
                                                                    "Could be handy.":
                                                                        $ Tate_points +=1
                                                                        $ spell+=1
                                                                        y s"You're right, it could come to be useful in the future."
                                                                        y "And he wouldn't know I learned it today."
                                                                        un eyeroll"Thank you for not being braindead."
                                                                        jump learnspell



                                                                    "I'd rather not have that knowledge.":
                                                                        y worried"No, Scribbles I couldn't, becau-"
                                                                        un pride"Nope, shut the fuck up, I don't need your weak ass reasoning behind this."
                                                                        un "I get it, you're stupid, let's move on with our lives and never speak of this again."
                                                                        y "But I-"
                                                                        un suspicious"SHH!"
                                                                        y simple"..."
                                                                        "I stand there in silen-"
                                                                        un squint"I SAID SH-"
                                                                        un simple"Oh, you're just monologuing, sorry, carry on."
                                                                        "..."
                                                                        "As I was saying, I stand there in silence for another minute, pondering my decision."
                                                                        jump afterlearnspell

                                                                label learnspell:
                                                                y s"So how do I activate it?"

                                                                un simple"First off, repeat these words: Inrita fatum, transibit cum illis."
                                                                y simple"Cum?"
                                                                un bored"Not that kind of cum, you slut."
                                                                un "Say that while snapping your fingers."
                                                                un "Usually the activation process goes a bit differently, but that's because you have to touch the catalyst's body to do so and we... well... we can't touch."
                                                                "I do as he says, barely remembering the strange words."
                                                                "As soon as I snap, my fingers glow brightly for a moment, before turning back to normal."
                                                                un "Done, it's activated."

                                                                un "Whenever you want to use it, just think of me and your other target switching places."

                                                                y "It's a whole lot of trouble just to cancel some mobility spells."
                                                                un "Well, canceling ANY spell is hard work, usually, unless your affinity is specifically spell canceling."
                                                                y "Interesting."
                                                                un "One more thing."
                                                                un "Keep in mind this spell can also cancel someone else's cancellation, it's like a common switch."
                                                                un "Not sure if this will ever be useful, but remember it."
                                                                y "Will do."


                                                                jump afterlearnspell
                                                                label afterlearnspell:
                                                                play sound "audio/teleport.ogg"

                                                                show cat20teleport with dissolve

                                                                show cat20
                                                                hide cat20teleport with dissolve

                                                                "PTSD hits me like a truck as Tate suddenly appears inches from my face, with a smile on."
                                                                "A BIG smile on."
                                                                "Wherever he went, it left him satisfied."

                                                                y scream"Ah!"
                                                                y worried"Can you stop doing that?"
                                                                t "Why?"
                                                                t "You're cute when you're scared."
                                                                y simple"What are you so excited about?"
                                                                t "Secret, for now."

                                                                t "But I do want to share it with you soon."

                                                                y pf"You're such a tease."
                                                                y "In more ways than one."
                                                                hide cat20
                                                                show cat20smug1

                                                                t "I know, but that's what you love about me, right?"

                                                                y bored"You can say that."


                                                                t "The sun is starting to set, come on, we don't want to miss it!"

                                                                y simple"Miss it?"
                                                                hide cat20smug1 with dissolve
                                                                show catfly with dissolve

                                                                t "Hop on!"
                                                                "He gets on his broom and gestures for me to join him."
                                                                stop music fadeout 3.0
                                                                scene black with dissolve
                                                                "I almost forgot we flew all the way here, so it makes sense to do the same on the way back."
                                                                "The ascension along the forest's tree line made me, once again, a little jumpy."
                                                                "Which meant more claws in poor Tate's stomach."

                                                                scene chibitate23 with longdissolve

                                                                play music "audio/wisp.ogg"

                                                                "As soon as my eyes got brave enough to peek, I was stunned by the sky's colors."
                                                                "We enjoyed a silent ride for a while, as my eyes jumped from cloud to cloud."
                                                                y smug"I doubt I'll ever get tired of this."
                                                                t "It's a good way to discover new places I can teleport to."

                                                                y s"Ah, so my suspicions were right, you {b}do{/b} have to know a place before teleporting to it."
                                                                t "Obviously, otherwise, I'd be in your mom's bedro-"
                                                                "{i}*smack*{/i}" with hpunch
                                                                t "Ouch."
                                                                y bored"Keep my mom's name out of your damn mouth, you silly goober."
                                                                t "Your mom's name is {i}'mom'{/i}?"
                                                                y bored"You know what I meant."
                                                                t "Huehueheu, don't read too much into my jokes."
                                                                t "Speaking of names, what do you think of Ray?"
                                                                y simple"Ray?"
                                                                y "Short for {i}'Raymond'{/i}, I presume?"
                                                                y "It's pretty nice."
                                                                t "More like {i}'Rey de la Sombras'...{/i}"
                                                                y confused"Huh?"
                                                                y "Doesn't that mean, {i}'Shadow King'{/i}?"
                                                                t "Damn it, of course you speak Spanish..."
                                                                y simple"Wait, Tate, is this about your nickname game?"
                                                                t "Wouldn't call it a game... but sure."
                                                                t "So what about it?"
                                                                y bored"It's silly."
                                                                t "You just said it's nice!"
                                                                y pf"Not the full nickname."
                                                                y "It just feels a bit over the top."
                                                                y "Like {i}'Tartarus'{/i}, or {i}'Shadow Prince'{/i} or {i}'Phantom'{/i}..."
                                                                t "Purple Demon?"
                                                                y "No..."
                                                                t "Damn it..."

                                                                y simple"I do have to agree with what Aiden said before, seems a bit disrespectful, or at least weird to be looking for a cool new nickname."
                                                                y "Even if it's for a hunter's career."
                                                                y "Your name is fine as it is."

                                                                t "Yeah, just a cool nickname..."
                                                                t "I suppose you might be right."

                                                                "Tate ends our conversation there, and we continue the rest of the way in silence."
                                                                "Thankfully, it wasn't awkward, since the view was taking our attention away anyway."
                                                                t "Can never get enough of those reds, oranges and yellows."
                                                                t "Some of my favorite colors."

                                                                y s"Not purple?"

                                                                t "Nah, it's just the motif I'm rocking, because let's be honest, I'm slaying it."
                                                                t "Not as much as those piercing pink eyes of yours~"

                                                                y smug"Smooth, but too cheesy."
                                                                y "I prefer sweet over savory."
                                                                t "I HAVE to be cheesy."
                                                                t "Why else did I swoop you off your feet with my broom for?"

                                                                y blush"Stoooop..."
                                                                t "Don't cover your ears, you're gonna fall!"

                                                                y pf"You said it's impossible for me to fall!"

                                                                t "It's impossible to get hurt, but if you break my heart first with your denial, then I won't be able to save you!"
                                                                Y screamblush"Aaaaghh!"

                                                                "He continues to make puns, make cheesy remarks and overall make me smile while blushing all the way back."
                                                                "It was a bit hard not to jump off sometimes, but as much as my ears were scratched by his words, my brain is waiting impatiently to hear what else he comes up with."
                                                                scene black with dissolve
                                                                stop music fadeout 3.0
                                                                "At last, he lands the broom near the academy's front garden, where we left off."
                                                                scene rooftop with dissolve
                                                                play music "audio/pianorelax.ogg" fadein 3.0
                                                                "We were just in time to catch two tired figures emerging from the front door of the building."
                                                                "Beaten up might be a better way to describe them, now that they're closer."

                                                                show wolf20dead at right with moveinright
                                                                show tiger20dead at left with moveinleft
                                                                show cat20simple with moveinright



                                                                d "Hey you two."
                                                                d "Hope you didn't get in trouble without us around, haha."

                                                                y simple"Not as much as you did."
                                                                y "What happened?"

                                                                hide cat20simple
                                                                show cat21smug

                                                                t "Let me guess, Aiden's ex's finally decided to team up?"
                                                                t "Not even the defender's leader can stop a crowd that big."

                                                                a "You're lucky my fists are tired, munchkin."
                                                                t "No thanks, not into fisting."

                                                                y surprised"You have that many failed relationships, Aiden?"
                                                                "He looks at me surprised, turning embarrassed."
                                                                a "N-not {i}'failed'{/i}."
                                                                a "We just had... different interests in mind at the time."
                                                                t "His interests were a dickin' while theirs were lovin'."
                                                                a "That's... not entirely false..."
                                                                a "But very broad."
                                                                a "And overly simplified."
                                                                a "I promise I'm not that shallow."
                                                                d "Well, not ex's, but we did have to stop my members from throwing a new summoner student out the window because he accidentally entered our headquarters..."
                                                                a "Then got in a fight with my slayers, but retreated since they had weapons ready."
                                                                hide cat21smug
                                                                show cat21simple

                                                                y simple"Oh wow."
                                                                t "Where was Haima while this was happening?"
                                                                d "Leading the slayers..."
                                                                t "oh."

                                                                a "We finally managed to calm the waters, after me and Dallan did a fake arm wrestling to see {i}'which Shard is better'{/i}, and we {i}'tied'{/i}."

                                                                d "Haima was a bit furious about that."
                                                                d "Are you going to be able to manage them?"
                                                                a "They'll be fine, there's always Monty to take their anger on."
                                                                t "Monty's resilient."

                                                                show wolf20sadsmile at right with dissolve
                                                                hide wolf20dead with dissolve

                                                                d "But enough about our day, what about you, [name]?"
                                                                d "What did you think of your first day here?"
                                                                hide tiger20dead with dissolve
                                                                show tiger20bored at left with dissolve

                                                                a "You should probably go take some shots at the nurse's office after spending so much time in close proximity to this cat."
                                                                hide cat21simple
                                                                show cat20smug
                                                                t "Don't listen to him, [name], he's jealous."
                                                                y simple"Jealous of what exactly?"
                                                                hide tiger20bored
                                                                show tiger20surprised at left
                                                                t "Well obviously it's me because we-"
                                                                a "H-heeyy, why don't you respond to Dallan's question while we head to the cafeteria, I think we are all starving, right?"

                                                                d "You can say that twice."
                                                                hide wolf20sadsmile
                                                                show wolf20simple at right
                                                                d "Actually, don't, it will make me starve more."

                                                                t "I can certainly use more than bread in my system right about now."
                                                                scene black with dissolve
                                                                jump groupdinner

                                                                label groupdinner:
                                                                play music "audio/lunch.ogg" fadein 3.0 volume 0.5

                                                                "We make our way to the cafeteria, the three guys take turns leading the way, since I'm the only one that doesn't know where it is."
                                                                "Tate tells Dallan about our forest walk, but he sure as hell likes to exaggerate things."
                                                                scene cafsun with dissolve
                                                                show cat20 with moveinright
                                                                show tiger20bored at left with moveinleft
                                                                show wolf20 at right with moveinright
                                                                t "Then, I make three hoops in the air, while standing up."
                                                                t "[name] stands there, absolutely and utterly safe, while I jump off and call the broom back to me, catching it in mid air and getting back on."
                                                                a "Then everybody clapped..."
                                                                hide cat20
                                                                show cat20ec
                                                                t "Exactly!"
                                                                d "Seems like you had a lot of fun."
                                                                hide cat20ec
                                                                show cat21smug
                                                                t "And [name] gave me some tips on how to teleport things with my mind."
                                                                a "Is that actually true?"
                                                                y awkward"Yeah, pretty much."
                                                                "Tate continues with these stories while I nod along."
                                                                "Aiden, unlike Dallan, obviously doesn't buy most of them, but they're harmless, and we both let it slide."
                                                                "It's pretty late, which means there are fortunately enough empty seats for us four."
                                                                "We are all hungry, so we get multiple trays full of different food for the table."
                                                                "Mine in particular, had half a rotissserie chicken, some mashed potatoes and a large, green salad."
                                                                "Tate got two burgers with a ton of fries."
                                                                "Aiden is a steak kind of guy, with fancy grilled veggies on the side, and Dallan's tray is basically filled with all of our meals combined."
                                                                "That man can eat..."
                                                                "I'm not rushing to be anywhere, and it's a nice, golden, cool evening, so I decide to take it easy on the food and make some conversation with these guys."
                                                                "Or at least the ones I interacted with before in a meaningful way."
                                                                "After all, can't ask someone a personal question if you didn't win any {b}friendship points{/b} for them before, right? Haha."
                                                                un curious"Why'd you say it like that?"
                                                                hide wolf20
                                                                show wolf20eat at right

                                                                menu questionss:
                                                                    "I'll talk to..."
                                                                    "Aiden.":
                                                                        if Aiden_points >=1:
                                                                            scene cafsun
                                                                            show cat20
                                                                            show tiger20bored at left
                                                                            show wolf20 at right
                                                                            y s"Hey Aiden, may I ask you something?"
                                                                            A "Go ahead."
                                                                            y "Earlier today you ran off as soon as the meeting ended."
                                                                            y "Do you mind if I ask why?"
                                                                            a "Yes."
                                                                            y simple"oh."
                                                                            t "Don't waste your breath [name], he's a time wizard."
                                                                            y surprised"Really?"
                                                                            hide tiger20bored
                                                                            show tiger20iritated at left
                                                                            a "I told you a THOUSAND times, I am NOT a time wizard!"
                                                                            t "Hmmm, I don't remember it being a thousand, are you sure it's not a different me from another timeline, you slutty time wizard?"
                                                                            a "Grrr...yes, I'm sure."
                                                                            t "Then why do you always disappear for no reason?"
                                                                            d "And have so much free time while completing all your work..."
                                                                            a "Not you too..."
                                                                            d "I'm JUST saying, I have no other explanations so even that starts to sound plausible."
                                                                            y simple"Haima was pretty pissed, as if it happens a lot."
                                                                            a "Drop the subject, or I'm getting up right now."
                                                                            hide cat21smug
                                                                            show cat20simple
                                                                            d "..."
                                                                            t "..."
                                                                            y "..."
                                                                            y "Sorry... didn't mean to pressure you."
                                                                            hide tiger20iritated
                                                                            show tiger20bored at left
                                                                            a "It's alright, I understand, but now that YOU understood as well, we can stop thinking about it."
                                                                            a "I'm not a time wizard, and my motives don't concern you."
                                                                            a "End of story."
                                                                            "Questions still dangle above my head, but I don't want to play with the bomb that is his temper, so let's see what else is on the menu."
                                                                            jump questionss
                                                                        else:
                                                                            "I don't think I'm good enough friends with him to deserve answers to my personal questions..."
                                                                            "Maybe if I chose his brochure back then, or something."
                                                                            "I should try somebody else."
                                                                            jump questionss
                                                                    "Tate.":
                                                                        if Tate_points >=1:
                                                                            scene cafsun
                                                                            show cat20
                                                                            show tiger20bored at left
                                                                            show wolf20 at right
                                                                            y s"Hey, Tate?"
                                                                            t "That's me."
                                                                            y simple"So... you're a first year, that means you'll be joining the Sorcery Shard {b}after{/b} the auditions, right?"
                                                                            t "Yep."
                                                                            y pf"So why do you have a badge?"
                                                                            hide cat20
                                                                            hide cat21smug
                                                                            show cat21simple
                                                                            hide wolf20eat
                                                                            show wolf20bored at right
                                                                            hide tiger20bored
                                                                            show tiger20iritated at left
                                                                            "The two guys next to him give him a sour look."
                                                                            d "Yeah, tell him why."
                                                                            a "I'm sure it will be a completely innocent reason."
                                                                            hide cat21simple
                                                                            show cat21scared
                                                                            t "I, uhmm."
                                                                            t "I stole it."
                                                                            y pf"Why?"
                                                                            t "I wanted it."
                                                                            y simple"You don't usually have stolen goods displayed on your chest like that."
                                                                            d "Well we got it back from him, multiple times."
                                                                            a "But he always sneaks one out anyway."
                                                                            hide cat21scared
                                                                            show cat21smile
                                                                            t "So they finally decided to give up."
                                                                            t "Smartest decision they ever made."
                                                                            t "I've had it since I was thirteen."
                                                                            hide wolf20bored
                                                                            show wolf20frust at right
                                                                            "Dallan cringes at the severe rule breaking confession."
                                                                            t "The previous leader of the Sorcery Shard thought it was cute that I wanted to be in their Shard so badly, so he didn't try to stop me."
                                                                            t "And Merina gave up after my second scavenge."
                                                                            y smug"So you're a long lasting, serial troublemaker."
                                                                            hide cat21smile
                                                                            show cat21smug
                                                                            t "Pleasure to meet you."
                                                                            "I should change the subject before Dallan manifests the first angry vein in his life."
                                                                            hide wolf20frust
                                                                            show wolf20eat at right
                                                                            hide tiger20iritated
                                                                            show tiger20bored at left
                                                                            jump questionss
                                                                        else:
                                                                            "I don't think I'm good enough friends with him to deserve answers to my questions..."
                                                                            "Maybe if I chose his brochure back then, or called him cute once, or something."
                                                                            "I should try somebody else."
                                                                            jump questionss
                                                                    "Dallan.":
                                                                        if Dallan_points >=1:
                                                                            scene cafsun
                                                                            show cat20
                                                                            show tiger20bored at left
                                                                            show wolf20 at right
                                                                            y s"Hey Dallan, mind a question?"
                                                                            d "Never, shoot ahead!"
                                                                            y "How's life like here as a leader?"
                                                                            y "I heard it's hard work."
                                                                            hide wolf20eat
                                                                            show wolf20sadsmile at right

                                                                            d "It is, especially for me."
                                                                            y s"I bet, you have a lot of members to take care of."
                                                                            d "That, and because of my limitations."
                                                                            y "I've seen how people gather around you, so it must be hard getting away from people being so popular, I get you."
                                                                            d "Yeah, that, among other limitations..."
                                                                            d "But the payoff is great!"
                                                                            t "Yeah, lucky... he's rich while still being a student..."
                                                                            d "I wouldn't say rich... just enough so I don't have to rely on my family while I'm here."
                                                                            a "Money and extra credit is one thing, but having eyes follow you around and heads turning everywhere you go must be exhausting."
                                                                            t "Aiden is not talking from experience, I just thought I'd clear that up for ya."
                                                                            a "If only there weren't so many witnesses..."
                                                                            "Even now, just sitting here and enjoying our meal, there are a bunch of students looking our way from time to time, mostly at Dallan."
                                                                            y simple"Does that bother you, Dallan?"
                                                                            d "I don't see the prying eyes."
                                                                            y "Must've taken a while to get that used to it."
                                                                            d "Fairly easy actually."
                                                                            hide wolf20sadsmile
                                                                            show wolf20eat at right
                                                                            "The first non-humble thing he said so far."
                                                                            "He has a hard time talking since his mouth is stuffed most of the time, so I'll just talk with someone else."
                                                                            jump questionss
                                                                        else:
                                                                            "I don't think I'm good enough friends with him to deserve answers to my questions..."
                                                                            "Maybe if I chose his brochure back then, or something."
                                                                            "I should try somebody else."
                                                                            jump questionss
                                                                    "That's about it.":
                                                                        jump afterquestionss

                                                                        label afterquestionss:
                                                                        scene cafsun
                                                                        show cat20simple
                                                                        show tiger20bored at left


                                                                        show wolf20simple at right

                                                                        "Now that he's no longer hungry, Dallan happily gives us some more juicy details about what happened today."
                                                                        d"So get this, a summoner entered the defender's headquarters by accident."
                                                                        a" Obviously they had to overreact, as always."
                                                                        d "But the guy wasn't just SOME guy, he was another recommended student, like you."
                                                                        d "Everyone was a little disappointed he didn't become a defender, but we already got one of those, so maybe it's for the best."
                                                                        a "Yeah, it is {b}definitely{/b} for the best."
                                                                        hide cat20simple
                                                                        show cat21smug
                                                                        t "You're just salty that no recommended students chose your shard."
                                                                        hide tiger20bored
                                                                        show tiger20iritated at left
                                                                        a "And how many have you got, pipsqueak?"
                                                                        t "One."
                                                                        t "That Coal guy."
                                                                        hide tiger20iritated
                                                                        show tiger20bored at left
                                                                        a "I see... so there is still time..."
                                                                        "He glances at me for a moment, before returning to his leftovers."
                                                                        "Tate kept me a secret, probably doesn't want to stir problems, letting others know his Shard got two recommended students."
                                                                        un "Or he forgot you're technically a big deal."
                                                                        "That's another possibility, yes..."
                                                                        hide wolf20simple
                                                                        show wolf20 at right
                                                                        d "Speaking of first years, I heard tomorrow you two will have a little special assignment to do."
                                                                        y simple"Special?"
                                                                        t "The Sorcery auditions."
                                                                        y pf"Oh, right, I forgot about that."
                                                                        d "I'm sure you'll do great."
                                                                        d "I've known Tate for a long time, so I don't doubt he'll have no problems in there."
                                                                        a "And recommended students are impossible to fail."
                                                                        d "That's usually how it goes, yes."
                                                                        y awkward"Can't waaait..."
                                                                        un bored"You don't seem too excited."
                                                                        "Whaaat?"
                                                                        "Nooo..."
                                                                        "I'm super excited."
                                                                        un "Sure, because that wasn't awkward sarcasm in your voice and I'm totally not sensing panic when you hear the words {i}'auditions'{/i}."
                                                                        hide tiger20bored
                                                                        show tiger20blushside at left
                                                                        a "Hey, so, uhm, [name]."
                                                                        a "Tomorrow, I was thinking maybe you'd want, you know, before practice starts, or your auditions."
                                                                        hide cat21smug
                                                                        show cat21mad2
                                                                        hide wolf20
                                                                        show wolf20simple at right
                                                                        t "The angry cat stands up from his seat."
                                                                        hide tiger20blushside
                                                                        show tiger20simple at left
                                                                        show cat21mad2 at left3 with move
                                                                        show tiger20simple at left5 with move
                                                                        a "What?"
                                                                        a "Why are you narrating yourself?"

                                                                        t "And asks the dumb, annoying tiger."
                                                                        t "Are you trying to steal my partner?"
                                                                        a "P-partner?"
                                                                        "He looks at me a little shocked and confused."
                                                                        "Completely forgetting the {i}'dumb and annoying'{/i} comment, lucky for Tate."
                                                                        hide cat21mad2
                                                                        show cat21bored at left3
                                                                        t "Hunting partner."
                                                                        a "oh."
                                                                        hide tiger20simple
                                                                        show tiger20bored at left5
                                                                        show tiger20bored at left with move
                                                                        a "So what if I am?"
                                                                        a "I'm just trying to occupy his time with actual important stuff."
                                                                        t "Your dick ain't that important."
                                                                        show cat21bored at center with move
                                                                        hide tiger20bored
                                                                        show tiger20angryright at left
                                                                        d "oof."

                                                                        t "For your information, me and [name] have VERY important things to do tomorrow morning."
                                                                        a "Such as?"
                                                                        t "None of your business."
                                                                        t "Now, peasant."
                                                                        t "And Dallan."
                                                                        d "Hi."
                                                                        t "Clean this table up."
                                                                        t "I'm taking this spotted specimen with me, and we'll do unspeakable things to each other somewhere else."
                                                                        hide tiger20angryright
                                                                        show tiger20surprised at left
                                                                        "W-what is he talking about?"
                                                                        hide cat21bored with moveoutright
                                                                        "Tate picks me up by one arm and drags me along."
                                                                        "Aiden is, once again, stunned by his words, while Dallan just a tad oblivious."
                                                                        hide wolf20simple
                                                                        show wolf20ec at right
                                                                        d "Alright, don't get into {b}too{/b} much trouble."
                                                                        hide tiger20surprised
                                                                        show tiger20angry at left
                                                                        a "HOLD ON NOW!"
                                                                        a "I AIN'T CLEANING YOUR FUCKING MESS!"
                                                                        a "COME BACK HERE!"
                                                                        stop music fadeout 3.0
                                                                        scene black with dissolve
                                                                        a "AND WHAT DO YOU MEAN BY {i}'THINGS'{/i}?!"
                                                                        a "HEY!"
                                                                        "We are now too far away for Aiden to start chasing."
                                                                        "I look back over my shoulder apologetically as I continue to be dragged along."
                                                                        "I manage to catch Aiden's face softening as our eyes meet."
                                                                        "Then he and Dallan pick up our trays and head for the kitchen."



                                                                        t "Don't be sorry for him."
                                                                        t "We had to assert dominance."
                                                                        y simple"Still, wasn't it a little mean?"
                                                                        y "The way we left like that?"
                                                                        t "I had to get you out before they asked about your powers."
                                                                        t "The conversation seemed to be going in that direction."
                                                                        t "You trust me, don't you?"
                                                                        y "Yeah."
                                                                        "With every ounce of my being, although that might be foolish to do."
                                                                        scene nightpark with longdissolve
                                                                        play music "audio/guitar.ogg" fadein 3.0



                                                                        if refuse >=1:
                                                                            show cat20smile with moveinright
                                                                            t "Hey, [name]."
                                                                            t "Do you think Merina's done with her weird date thing?"
                                                                            y simple"It's not a {i}'weird date thing'{/i}, it's just dinner."
                                                                            y "I'd say it's possible, we finished so why wouldn't they?"
                                                                            hide cat20smile
                                                                            show cat20bored

                                                                            t "Are they at that restaurant by the coast?"
                                                                            y "I believe so."

                                                                            t "Bleh, the fish place."
                                                                            jump tateasksmerina


                                                                        else:
                                                                            show cat20smile with moveinright
                                                                            t "Since today is Tuesday, Merina must have dinner with Oliver at that disgusting fish restaurant by the coast."
                                                                            t "So I'll sacrifice my dignity and step foot in that place for our sake."
                                                                            y simple"It seems a bit rude to interrupt them like that."

                                                                            t "They must be about done anyway, how long can someone possibly have dinner for?"
                                                                            jump tateasksmerina

                                                                        label tateasksmerina:
                                                                        scene nightpark
                                                                        show cat20smile
                                                                        t "Stay here, I'm going to ask them about our rooms and get our keys."
                                                                        t "Be back in a minute."
                                                                        y confused"If you're going to teleport, can't you just take me with you?"

                                                                        t "I already used my teleportation a lot today, if I take you with me, I'd be drained."
                                                                        y simple"Understandable, then I'll wait for you."
                                                                        y "Hopefully I won't end up sleeping on this bench."
                                                                        play sound "audio/teleport.ogg"
                                                                        show cat20teleport
                                                                        hide cat20smile with dissolve
                                                                        hide cat20teleport with dissolve

                                                                        "He gives me a final salute before the blue light makes him vanish."
                                                                        "Still can not believe I forgot to ask about my room..."
                                                                        "Good thing Tate is almost as airheaded as me."
                                                                        "I now realize how much distance we've covered by running from the cafeteria, enough to the middle of this secluded park."
                                                                        "It doesn't seem like a random location either, there is a single, illuminated bench by the sidewalk, surrounded by the occasional wild daisy through the grassy floor and flower filled bushes."
                                                                        y s"This is quite nice, actually."
                                                                        y smug"I wouldn't even mind sleeping here tonight."

                                                                        un pride"Well, I'm not sleeping in anything other than a soft bed."
                                                                        un "It's the least you can do for me."
                                                                        y confused"{i}'The least I can do for you'{/i}?"
                                                                        y "Am I in your debt or something and didn't know?"
                                                                        un surprised"Wha-"
                                                                        un cry"But how could you ever deny me a basic need such as soft sheets?"
                                                                        un "I've been imprisoned for centuries!"
                                                                        un "Do you have no heart?"
                                                                        y bored"You are so dramatic."
                                                                        y "Besides, I was joking, I don't want to sleep with bugs swarming around."
                                                                        un relaxed"Phew~"

                                                                        "I take a seat on the bench and wait."
                                                                        "The night sky is brighter than expected, with no clouds in sight, it makes it easy for the stars and the moons to demonstrate their full potential."
                                                                        un simple"Are you afraid of the dark?"
                                                                        y pf"That would be such a creepy thing to say if you didn't have that squeaky little baby voice."
                                                                        un ang"I told you already... IT'S JUST HOW YOUR MIND IMAGINES IT!"
                                                                        un "IT'S NOT MY FAULT!"

                                                                        un bored"Damn, I can't have a normal conversation with you, can I?"
                                                                        y smug"Did we ever?"

                                                                        un "I'll be in the back of your mind for a while."
                                                                        un "Good luck being alone with your thoughts."
                                                                        un "Your...stupid, meaningless thoughts."

                                                                        "Scribbles is right, my mind can create some scary things on its own, and some stupid ones too."

                                                                        "Thankfully, I won't have to overthink too much, as a bright light appears in front of me again."
                                                                        play sound "audio/teleport.ogg"
                                                                        show cat20teleport with dissolve
                                                                        show cat20smug
                                                                        hide cat20teleport with dissolve

                                                                        t "I'm back!"
                                                                        hide cat20smug with dissolve
                                                                        show cat21bow with dissolve
                                                                        t "The cat says, bowing profoundly to the spotted feline in front of him, whom has been awaiting his return with a held breath."
                                                                        y "Thou art a most wondrous poet and gleek'r, I knoweth yond, but what news doth thee bringeth from lady Merina?"
                                                                        y"Wouldst thou beest so kind as to shareth thy inf'rmation with me, oh lief Tate."
                                                                        hide cat21bow with dissolve
                                                                        show cat21simple with dissolve


                                                                        t "Huh."
                                                                        t "And here I thought those guys from earlier were nerds."
                                                                        t "I also hate the fact that I understood you..."

                                                                        hide cat21simple
                                                                        show cat20smile

                                                                        y simple"Was Merina busy?"
                                                                        y "I really hope we didn't mess up their night."
                                                                        t "She was a little tipsy, flirting with the waiter, but I doubt I {i}ruined{/i} anything."

                                                                        hide cat20smile
                                                                        show cat20ec


                                                                        t "Here's the tea."
                                                                        t "First off, we were placed in the same building!"

                                                                        y ec"That's awesome!"
                                                                        hide cat20ec
                                                                        show cat21smile

                                                                        t "Unfortunately, we are on different floors and wings, we'll still be pretty far away from each other."
                                                                        t "Now, I know what you're thinking."
                                                                        t "But Merina specified we won't get to change our rooms if either of our neighbors mysteriously disappear."

                                                                        y simple"I wasn't thinking that."
                                                                        hide cat21smile
                                                                        show cat21smile

                                                                        t "Shh, it's ok, I'm not judging you."
                                                                        t "I was thinking about it as well."

                                                                        hide cat21smile
                                                                        show cat21smile1

                                                                        t "Here's your lunch and dinner card."
                                                                        t "With this, we won't have to pay for meals, except breakfast, for some reason."

                                                                        y "Shoot, we didn't pay for dinner tonight... did we?"

                                                                        t "Don't worry about it, Aiden acts like a bitch sometimes, but he often pays for my meals."
                                                                        t "And Dallan does it without hesitation."

                                                                        y "Is it ok to take advantage of them like that?"

                                                                        hide cat21smile1
                                                                        show cat20angry

                                                                        t "Hey, they're rich!"
                                                                        t "Do you even know how much these leaders and vice leaders are being paid?"

                                                                        y "Uhm, I assume a lot?"

                                                                        t "A LOT!"

                                                                        hide cat20angry
                                                                        show cat21smug


                                                                        t "So no, I decided not to feel bad about it."

                                                                        un simple"I agree with him."
                                                                        un bored"Eat the rich, or make them buy you something to eat."
                                                                        t "Aaand here is your key card, room 72."
                                                                        t "Mine is 123."
                                                                        y s"Sweet, shall we go check them out?"

                                                                        t "Of course, but aren't you missing anything?"

                                                                        y confused"Missing?"
                                                                        t "Perhaps something personal and important people usually bring on trips?"
                                                                        y simple"I don't think-"
                                                                        y surprised"Wait."
                                                                        y "Damn it!"
                                                                        y worried"My luggage is still inside the academy."
                                                                        y "I gotta go get it."
                                                                        t "Don't bother, the meeting room where you left it is closed."
                                                                        hide cat21smug
                                                                        show cat21bow
                                                                        t "But worry not, oh thou fair maiden!"
                                                                        t "I shall bringeth it to thee!"
                                                                        hide cat21bow
                                                                        show cat21smug
                                                                        t "Ey? How'd I do? Did I sound all old and fancy?"
                                                                        y smug"It was pretty good, although you'd want to replace 'shall' with 'shalt' for the best effect."

                                                                        t "Sorry, I can't actually pretend to care anymore."
                                                                        t "I'll just teleport into the meeting room and get your bags sometime later."

                                                                        hide cat21smug with dissolve
                                                                        show catfly with dissolve

                                                                        t "Now let's get a move on."

                                                                        t "Hop back on!"

                                                                        y ec"{i}'Hop'{/i} is slowly becoming my favorite word, I will not say no to another broom ride."
                                                                        scene chibitate25 with longdissolve

                                                                        "We soar up just enough to pass the rooftops of some nearby houses from the residential area, once past, the dorm buildings were easy to spot."
                                                                        "All of them were relatively close to one another, divided by either very tall trees or the occasional narrow street."
                                                                        stop music fadeout 3.0

                                                                        t "Let's see, bricks...number three...vines...number- ah, there it is."
                                                                        "We land in front of a six story building, made of diamond patterned bricks, with a reddish hue."
                                                                        "A wall of greenery partially covering two of its sides, with various plants and vines also trying to make their way up the front wall."
                                                                        "That's all I managed to observe, alongside the big number three on the front door, before Tate flings it open and drags me inside."
                                                                        play music "audio/firstday.ogg" fadein 4.0
                                                                        scene dorm with longdissolve
                                                                        "The interior is very well furnished considering it's a common room, where anyone comes and goes as they please."
                                                                        "There were bookshelves filled with- you guessed it, magical items."
                                                                        "Oh, and some books too, here and there."
                                                                        "Tall pillars hold the spiral staircase I'm being rushed to climb, and numerous paintings decorate the walls besides the crystal powered lamps."
                                                                        scene dormhall with dissolve

                                                                        "As we get to the third floor, Tate finally slows down, but he still buzzes with excitement."
                                                                        show cat20smile with moveinleft
                                                                        "We stop in front of a door."
                                                                        "72."
                                                                        t "Here we are, this one is yours."
                                                                        t "Lets see how lucky you got."

                                                                        y simple"Aren't all dorm rooms the same?"
                                                                        "I fish out the card Tate gave me, and try to figure out how to use it."
                                                                        hide cat20smile
                                                                        show cat20simple
                                                                        t "Not even close, you should see Dallan's dorm, or Aiden's!"
                                                                        t "Those guys have a mansion inside a building."
                                                                        t "Merina's is legit just a penthouse."
                                                                        t "Kind of comes with the position."
                                                                        y smug"Then as unimportant first years with no achievements, we should be thankful we at least don't have roommates, huh?"
                                                                        hide cat20simple
                                                                        show cat21smug
                                                                        t "I wouldn't mind having a particular someone as a roommate."
                                                                        "My mind is a little too focused on how the hell this keycard works to respond to Tate's bold statement."
                                                                        t "It's new, you gotta peel off the protective seal."
                                                                        "Yep, he's right, a thin layer of plastic comes off after a short inspection."
                                                                        y bored"A regular key would've been less trouble."
                                                                        t "I'm pretty sure magic easily beats a regular key mechanism."
                                                                        y "You might be right."
                                                                        y "Wouldn't want unexpected guests in the middle of the night."
                                                                        scene dormroomnight with dissolve
                                                                        "I push open the door and try to find a light switch, just to find there is no lightbulb."
                                                                        y pf"wow..."

                                                                        show cat20smile with moveinleft
                                                                        "Tate ducks under my arm to get a good look inside."

                                                                        t "Not baaad, oh, and look, there's a door there, maybe there are more rooms, you're a {i}'special little guy'{/i} after all!"
                                                                        hide cat20smile with moveoutright
                                                                        "He invites himself in, spinning around while walking towards the other door, trying to see everything he can."
                                                                        "The room resembled my old bedroom, except that it was slightly bigger, with a nicer window but smaller bed."
                                                                        scene shower with dissolve
                                                                        "I follow the curious cat as he opens the second door."
                                                                        show cat21bored with moveinright

                                                                        "Annoyance can be seen on his face, as a plain bathroom comes into view, but this is fantastic news for me."
                                                                        "I have no need for more space than the one bedroom, and my own bathroom is a big win."
                                                                        "The lights work fine, but it looks like the shower is missing its shower head..."
                                                                        "I'm gonna need to bring up these missing objects to someone in charge."
                                                                        "But hey, at least I don't have to pay to stay here."
                                                                        hide cat21bored
                                                                        show cat20simple

                                                                        "Tate's ears suddenly perk up."

                                                                        t "I gotta go."

                                                                        y s"Hmm, what was that?"
                                                                        hide cat20simple
                                                                        show cat21scared

                                                                        t "Sorry, I can't stay anymore, nice dorm room, you're gonna have to come see mine sometime, but I seriously need to go, see you in the morning, sleep tight!"
                                                                        play sound "audio/teleport.ogg"

                                                                        show cat20teleport with dissolve
                                                                        hide cat21scared
                                                                        hide cat20teleport with dissolve

                                                                        "Before I can protest, he's gone."

                                                                        un sidee"Wow, this bathroom really bummed him out."
                                                                        y bored"Yeah, pretty sure that's not the reason."
                                                                        scene dormroomnight with dissolve
                                                                        y simple"He's just a weird one."
                                                                        y simple"There are a lot of {i}'maybes'{/i} and {i}'what ifs'{/i} to be thrown around when it comes to Tate, so I shouldn't bother."
                                                                        y "He said he'll tell me everything soon, and I trust him."
                                                                        jump tomyroom
                                                                        label tomyroom:
                                                                        y sleepy"{i}*Yaaawn*{/i}"
                                                                        y "I'm super tired."
                                                                        y "Today was waaaay too socially tiring."

                                                                        un curious"Aren't you going to shower?"

                                                                        y "I would, but all the spare clothes are in my luggage."
                                                                        y "Actually, it's pretty warm in here, I'll just sleep naked, and hopefully Tate comes back with my stuff in the morning."
                                                                        y "It would've been pretty nice if he had a phone so I can text him about it..."
                                                                        "I take off my tie and unbutton my shirt, feeling the fur on my chest along the way."
                                                                        "Rough, coarse, dusty."
                                                                        y "Eh, who am I kidding? I feel all dirty and sticky."
                                                                        play sound "Audio/shower2.ogg" volume 0.2
                                                                        scene shower with dissolve
                                                                        "I decide not to be a filthy little guy today, and hop in the shower, headless as it is."
                                                                        "At least the water is hot, even if it feels like being hosed down."
                                                                        "Bathroom appliances are included too, even if they're not my favorite brands."


                                                                        if dinner>=1:
                                                                            menu:
                                                                                "As tired as I am, here, under the hot water, I can't help but think about..."
                                                                                "Oliver.":
                                                                                    $ Ollie_points +=1
                                                                                    "Ollie..."
                                                                                    "That mouse sure lives in my head rent free as of today."
                                                                                    "Something about him makes me go wild."

                                                                                    "That might be an overstatement, but still, while around him, I feel my instincts come out, making me want to chase him, grope him, pin him down or bend him over."
                                                                                    "That petite figure, so easy to pick up."
                                                                                    "And surprisingly, I get the same feelings thinking about the roles being reversed."
                                                                                    "All in all, I suppose it boils down to having the hots for him."
                                                                                    un bored"A seveeeeere case of the hots, I dare say."
                                                                                    un "But I can't blame you."
                                                                                    un "The shy types were always fun to break in, back in my days."
                                                                                    jump showercum

                                                                                "Merina.":
                                                                                    "Merina..."
                                                                                    $ Merina_points +=1
                                                                                    "I know it's very ironic to say this, but her foxy persona, the way she moves so casually yet seductively is enough to make anyone drool over her."
                                                                                    "A perfect contrast of sexiness and beauty, and despite all that, her confidence gives off hints of innocence."
                                                                                    "As intimidatingly inferior she makes me feel with her mere presence, I would risk it all for a night with her."
                                                                                    "My fingers through her silky hair, or her fingers in mine, doesn't matter, as long as I get to be inside her, at the end of the day."
                                                                                    un bored"She would absolutely be the one pegging you, and you'd love it."
                                                                                    un "Whore."
                                                                                    jump showercum

                                                                                "Tate.":
                                                                                    $ Tate_points +=1
                                                                                    "Even if I chose to not go on that adventure with him, he keeps popping in my mind."
                                                                                    "Athletic, lithe body, with the belly always exposed, pants worn a little lower than he's supposed to, he knows what he's doing."
                                                                                    "And it's working better than he imagines."
                                                                                    "My imagination goes a little wild, images of him flashing on and off."
                                                                                    "He's bouncing up and down while I relax on my back, his hands intertwined with mine."
                                                                                    "Then he's holding my face, making me look him in the eyes as he's thrusting with a smirk."
                                                                                    "Now he's clenching the bed sheets as my whole weight stands on top of him."
                                                                                    un "The whole thirteen pounds of skin and bone..."
                                                                                    un "Actually, he's kind of muscular for someone of his size, I'll give him that."


                                                                                    "It might be wrong to think this way about him, since we literally met today, but don't you ever see someone so fine just casually walking down the street, that you can't help but fantasize about them for weeks on end?"
                                                                                    jump showercum


                                                                        else:

                                                                            $ Tate_points +=1
                                                                            "As tired as I am, here, under the hot water, I can't help but think about Tate..."
                                                                            "My new feline friend that loves to tease, because he probably has a hunch about how that body of his makes me feel..."
                                                                            "Athletic, lithe body, with the belly always exposed, he knows what he's doing."
                                                                            "And it's working better than he thinks."
                                                                            "My imagination goes a little wild, explicit images of him and I flashing on and off."
                                                                            "At first, he's bouncing up and down while I relax on my back, his hands intertwined with mine."
                                                                            "Then he's holding my chin up, making me look him in the eyes as he's thrusting with a smirk."
                                                                            "Now he's clenching the bed sheets, eyes rolled back as my whole weight stands on top of him."
                                                                            un bored"{size=20}The whole thirteen pounds of skin and bone...{/size}"
                                                                            "I hope these things can come at least close to reality, In the future."
                                                                            "No matter how long that might take."
                                                                            jump showercum

                                                                            label showercum:
                                                                            stop music fadeout 3.0
                                                                            stop sound fadeout 1.0
                                                                            scene black with dissolve
                                                                            "Needless to say, this erection of mine did not last long with the vivid images popping in."
                                                                            "With a sigh of satisfaction, I step out of the shower."
                                                                            "Down the drain goes the only evidence of the lewd thoughts I had."
                                                                            scene dormroomnight with dissolve
                                                                            play music "audio/nightsounds.ogg" volume 0.3

                                                                            "I drag my legs to the bed after a quick drying, and flop on it, ready to dream."
                                                                            un curious"Just like that?"
                                                                            un "Legs spread, ass out, no covers?"
                                                                            "{i}*Muffled noises*{/i}"
                                                                            un eyeroll"Suit yourself."
                                                                            un bored"Maybe I'll experience my first cold in...ever."
                                                                            un "It could be fun."
                                                                            scene black with longdissolve
                                                                            stop music fadeout 2.0



                                                                            "."
                                                                            "..."
                                                                            "....."
                                                                            scene snowdreambg with longdissolve
                                                                            play music "audio/blizzard.ogg"
                                                                            un simple"Huh, what is this?"
                                                                            un "I don't think I've seen this part of your brain before."

                                                                            un "Hey."
                                                                            un "Hey, mortal."

                                                                            un bored"Hmm."
                                                                            un "I suppose he's still asleep."
                                                                            un simple"Oh! Could this be?"
                                                                            un "He's dreaming."
                                                                            un "Ooh, what's that?"
                                                                            un surprised"What's that other thing?"
                                                                            un suspicious"Is that a person?"


                                                                            un simple"This is pretty interesting."
                                                                            un "."

                                                                            un bored"..."
                                                                            un "~...~"
                                                                            un bored "{i}*hummm~*{/i}"
                                                                            un "..."
                                                                            un "{i}*lip smack* *lip smack*{/i}"
                                                                            un sidee "hm..."
                                                                            un "Snow..."
                                                                            un "....."
                                                                            un "The silence is a bit suffocating, not gonna lie."

                                                                            un bored"All of these new images would usually be narrated by you, but since your mind is constructing this dream, it's a little busy at the moment."
                                                                            un "I might as well try to do it in your place, maybe it's fun."
                                                                            un "Why else would you do it all day long?"
                                                                            un "The secret is to say every word with the confidence of a God, even if you have no idea what is happening."

                                                                            scene snow1 with longdissolve

                                                                            un pride"{i}*cough cough*{/i}"
                                                                            un simple"We find ourselves in the middle of a winter night, the town's road being covered by about a foot worth of snow, the wind is blowing hard enough to mimic a snowstorm by lifting the outermost layer of snowflakes, carrying it around with intense, irregular movements."
                                                                            un "I'm assuming this scenery is here because you decided to go to sleep without a blanket like a fucking moron, and now you're cold as hell."
                                                                            scene snow2 with dissolve
                                                                            scene CGc49
                                                                            un "A shot of a foot, dramatically stepping in the snow, is presented in this frame."
                                                                            un "The foot belongs to a small, cloaked figure, which struggles to move through the thick, white blanket, ready to pass out at any moment."
                                                                            un "The wind is strong enough to not only take the cloak away flying at the first opportunity, but their whole body with it, toying with them like a puppet."
                                                                            un "A sad, dramatic scenery."

                                                                            un "Then-"
                                                                            scene black with dissolve
                                                                            stop music
                                                                            un suspicious"huh?"
                                                                            un simple"What's happening?"
                                                                            un squint"What? That's it?"
                                                                            un "What kind of fucking dream was that?"
                                                                            un ang"That made no sense!"
                                                                            un "Who dreams only the beginning of a story?"
                                                                            play music "audio/knocking.ogg" volume 0.2

                                                                            un bored"I'm disappointed, to say the least."
                                                                            un curious"And what's with this knocking?!"
                                                                            scene dormroomnighttate2 with llongdissolve
                                                                            show blink with dissolve


                                                                            "I wake up to the sound of knocking in the middle of the night."
                                                                            un simple"Oh, you're up."

                                                                            "I slowly open my eyes and regain my senses."
                                                                            "A cold feeling surges through me."
                                                                            "The chilled sheets don't help much, pressed against my stomach, face, thighs and... dick?"
                                                                            play music "audio/knocking.ogg" volume 0.6
                                                                            "Right, I'm naked."
                                                                            "The knocking becomes faster and louder, signaling impatience."
                                                                            y nakedasleep"Who in the hell...?"
                                                                            y "It's coming from the window?"
                                                                            y "Aren't I on the third floor?"
                                                                            play music "audio/nightsounds.ogg" volume 0.5

                                                                            scene dormroomnighttate with dissolve

                                                                            "The sleep rubs away, replaced by confusion and curiosity."
                                                                            "A figure stands... no, floats outside my window."
                                                                            y nakedblush"{i}*Gasp*{/i}, Tate!"
                                                                            y "Wait."
                                                                            "His eyes are fixed on my uncovered butt, sprawled on the bed."
                                                                            "Thankfully the parts that really matter are covered by my tail, still, that doesn't stop me from panicking, reaching for the blanket, instantly becoming a cocoon of shame."


                                                                            t "{size=30}I'M TELEPORTING INSIDE!{/size}"
                                                                            play music "audio/sweetwind.ogg" fadein 3.0 volume 0.1
                                                                            scene dormroomnight with dissolve
                                                                            play sound "audio/teleport.ogg"
                                                                            show cat20teleport with dissolve
                                                                            show cat20smug
                                                                            hide cat20teleport with dissolve
                                                                            "The next second the purple cat is at the foot of my bed, smiling widely."
                                                                            "I'm not sure if I should be happy to see him, mad he woke me up, or outright terrified by his presence here, so I stay quiet, staring with a judging expression."

                                                                            t "I brought your luggage."

                                                                            y nakedblush2"Thanks?"
                                                                            y "Could...could that not have waited until morning?"
                                                                            y "What time is it?"

                                                                            t "It's {i}'get out of bed and come with me right now'{/i} o'clock."
                                                                            "I would argue, or at least ask more questions, but I doubt I'll end up going back to sleep in any case."
                                                                            y nakedbored"Damn it..."
                                                                            y "Fine, let me get dressed."
                                                                            t "Hurry up."
                                                                            y "..."
                                                                            y "Well?"
                                                                            t "Well?"
                                                                            y nakedangry"Turn around!"
                                                                            y "Or go in the other room."
                                                                            t "I already saw everything there is to see from the window, you don't have to be shy."

                                                                            y "I am not changing in front of you!"
                                                                            hide cat20smug
                                                                            show cat21bored

                                                                            t "Ughhhh, can't watch a good show nowadays without being shunned."
                                                                            hide cat21bored with moveoutright
                                                                            "He walks into the bathroom and closes the door."
                                                                            "I pick out some clothes from my luggage and get started."
                                                                            "I have multiple pairs of the same jeans, shirt and tie, because why would I change perfection?"
                                                                            "Except that this time, I put on some nicer underwear, just in case..."

                                                                            un bored"I admit that you have surprisingly high chances of getting laid."
                                                                            "You think so?"

                                                                            un eyeroll"Absolutely, most of these people are hornier than {b}me{/b}!"
                                                                            un "And I'm a {b}lust{/b} demon!"
                                                                            t "Are you done yet?"
                                                                            t "You have like four things to put on, it can't be that complicated, unless...{i}*gasp*{/i}!"
                                                                            t "Are you hinting you need my help to get dressed?"
                                                                            t "Well, if you insist!"
                                                                            show cat20smug with moveinright
                                                                            "He bursts through the door, face dropping when he sees me pinning the last shirt button."
                                                                            hide cat20smug
                                                                            show cat21bored

                                                                            y smug"A little late."
                                                                            t "Too bad."
                                                                            t "At least now we can go."
                                                                            hide cat21bored with dissolve
                                                                            show catfly with dissolve
                                                                            t "Get on, we don't have time!"

                                                                            "Goodbye sweet bed, my new, weird and hot friend needs me."

                                                                            jump flytoegg
