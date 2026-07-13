label Demonss:
    if Secret5_points <=0:
        $ Secret5_points +=1

        "I walk out the door, uninterested in the others."
        scene hall with longdissolve
        play music"audio/pianosoft.ogg"
        un"What are you hoping to achieve here?"
        y simple"I'm not sure, but I have a feeling I'm not meant for any of them."
        un"meant?"
        un tease"What?"
        un"Did you think you'll marry one of them or what?"
        "..."
        un bored"{i}*sigh*{/i}"
        un"You know."
        un"Usually I would tease you more."
        un"Or just stay silent and let you fuck up everything you do."
        un"But I just have to say this."
        un"If you don't go back in there and {i}'choose'{/i} one of them."
        un"So to speak."
        un"You might regret it."
        y simple"..."
        y worried"You're right."
        y"What am I thinking?!"
        un"Maybe it would not have been such a bad idea."
        un"If this path was finished."
        y"What do you mean?"
        un"You can't progress any further even if you didn't listen to me!"
        un"I suggest you choose one of the guysfrom the trio."
        un "They all seem pretty interested in you."

        menu:
            "Fucking hell...":
                scene meetingroom with dissolve
                jump mainchoice
            "You are so smart Scribbles, thank you for the wise advice.":
                un tease"You're welcome!"
                scene meetingroom with dissolve
                jump mainchoice
    else:
            if Secret6_points <=0:
                $ Secret6_points +=1

                un"Come on dude."
                un"I just told you this path is not ready yet."
                y bored"How do I know you're telling the truth?"
                un ang"Uhm, HELLO?!"
                un"Demons can't lie dumbass!"
                un"You said it yourself."
                un"Now go back there, and show that tiger, wolf or cat some love."
                scene meetingroom with dissolve
                jump mainchoice
            else:


                un"Really?"
                play sound "audio/button.ogg"
                un ang"This is NOT funny."
                play sound "audio/button.ogg"
                un"You're wasting both our time!"
                play sound "audio/button.ogg"

                un"Trust me, I'd love to take this path as well."


                play sound "audio/button.ogg"
                un"BUT."

                play sound "audio/button.ogg"
                un"WE."



                play sound "audio/button.ogg"
                un"CAN'T."

                play sound "audio/button.ogg"
                un"RIGHT."
                play sound "audio/button.ogg"
                un"NOW."
                play sound "audio/button.ogg"
                un"Understood?"
                play sound "audio/button.ogg"
                un simple"Just come back later man"
                play sound "audio/button.ogg"
                un"And."
                play sound "audio/button.ogg"
                un"To be honest..."
                play sound "audio/button.ogg"
                un sidee"I really hope you do"
                play sound "audio/button.ogg"
                un"Come back later..."
                play sound "audio/button.ogg"
                un"Just between me and you."
                play sound "audio/button.ogg"
                un simple"But for now, that tiger, the wolf and especially the cat need you more."
                play sound "audio/button.ogg"


                menu:
                    "OK.":
                        play sound "audio/button.ogg"
                        un simple"Good."
                        play sound "audio/button.ogg"
                        jump mainchoice

                    "I understand.":
                        play sound "audio/button.ogg"
                        un simple"Thank you."
                        play sound "audio/button.ogg"
                        scene meetingroom with dissolve
                        jump mainchoice
