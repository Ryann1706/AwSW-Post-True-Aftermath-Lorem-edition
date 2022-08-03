
label ryann_lorem_post_true:

$ renpy.pause (2.0)
scene black with dissolveslow
$ renpy.pause (2.0)
scene np3 with dissolveslow
$ renpy.pause (1.0)

m "The last few hours felt like a dream, or a memory of a dream I had many times before. Izumi was dead, Reza was captured, and both worlds were safe - for now. No doubt it would all make sense in the morning but now I just wanted to get home and get some rest. Lorem and I walked back to town from the portal, together."
show lorem think with dissolve
$ renpy.pause (0.5)
Lo "So, what’s going to happen now?"
c "I don't know. It seems like I've got everything right this time so I won't have to do it all over again. If I have to, I will. But a part of me just wants to continue on and see what happens."
Lo normal "I hope you don’t have to do all this again."
Lo think "After you explained all the stuff you went through with time travel, Reza, and the comet, I think you’ve been through enough already."
$ renpy.pause (2.0)
show lorem sad with dissolve
$ renpy.pause (1.0)
m "Lorem suddenly adopted a somber expression, like they realized the actual impact of what they just said."
Lo "That comet is really going to hit, and it's going be bad, huh?"
menu:
    "Yeah.":
        c "Yeah. I learned about it in school. When it hits, it will send enough debris into the air it’ll block out the sun and freeze the planet in a winter that lasts a decade. It will destroy the ecosystem, and everything heavier than a kilogram will die within a year."

    "I’m not sure.":
        c "I’m not sure exactly what’ll happen, but yes, it will be bad."

c "But it’s not something you need to worry about."
c "The limiting factor for the portal is mass, so smaller dragons, like you and Ipsum, will get priority for being moved to the human world."
$ renpy.pause (1.5)
Lo normal "Would anyone else get priority?"

menu:
    "Adine":
        $ ryann_lorem_true_character_mention = "Adine"
        c "Adine would. Being a flyer would be very beneficial, and she has lots of experience with, and is very good at interacting with people."

    "Anna":
        $ ryann_lorem_true_character_mention = "Anna"
        c "Anna would.  She’s a scientist, and very intelligent. She would be an invaluable asset to humanity in helping us recover, and advance even further."

    "Bryce":
        $ ryann_lorem_true_character_mention = "Bryce"
        c "Bryce would. The human world isn’t in the best state, and having an authority figure, especially one as experienced as him would be a huge asset in helping humanity recover."

    "Remy": 
        $ ryann_lorem_true_character_mention = "Remy"
        c "Remy would. He’s very knowledgeable, and with what he has at his disposal, he would be a great asset to humanity’s recovery."

c "But it really doesn’t matter who would or wouldn't get priority. I’m sure we can devise a plan to safely get everyone into the human world."
Lo think "Right. We’re going to be living in the human world from now on…"
$ renpy.pause (2.0)
c "You seemed so excited about that idea before."
Lo relieved "I was, but the thought alone, and it actually about to happen is very different."
c "Is there something specific you’re worried about?"
Lo "Yeah. It’s just…"
show lorem think with dissolve
$ renpy.pause (2.0)
Lo "How would humanity react to someone being a hermaphrodite?"

menu: 
    "You have nothing to worry about. You’d be accepted.":
        $ ryann_lorem_true_humanity_reaction = "accepted"
        $ ryann_lorem_true_mood += 1
        c "You have nothing to worry about. You'd be accepted. Humanity is very open and accepting when it comes to things like that."
        $ renpy.pause (1.0)
        Lo normal "I’m… really glad to hear that."

    "It’s hard to tell how people would react.":
        $ ryann_lorem_true_humanity_reaction = "unsure"
        c "It's hard to tell how people would react. Everyone would have their own views about it."
        Lo sad "…"
        c "Keep in mind that it doesn’t mean everyone will react negatively. Some people will be indifferent, some will accept you, and some might not. Everyone’s different."
        Lo think "Well, I guess that's better than how our society would view it."

    "You should hope it's not too harsh.":
        $ ryann_lorem_true_humanity_reaction = "harsh"
        $ ryann_lorem_true_mood -= 1
        c "I can’t speak for everyone, but you should hope it isn’t too harsh."
        show lorem sad with dissolve
        $ renpy.pause (2.0)
        Lo "I really hope it’s not. I hope you’re wrong, and that more people are accepting like you."


$ renpy.pause (1.5)
c "So, what are you going to do now?"
Lo think "What do you mean?"
c "Well, moving to the human world will be a big change. What are you going to do once you’re there?"
Lo "Well, I'll still work on my game, but other than that, I’m not sure…"
$ renpy.pause (1.5)
Lo happy "Oh! Maybe I could learn about and grow some plants unique to the human world!"
Lo think "I could learn about some more human myths, and see how true our myths about humans are…"
Lo happy "And I could check out human video games too!"
$ renpy.pause (1.0)
Lo relieved "Oh, right. Because of the solar flare, any video games must have been destroyed, huh?"
c "Well, not everything electronic was destroyed by the flare. The PDAs, and some other stuff survived, so some games might have survived too, right?"
Lo happy "Oh yeah!"
c "Well, if I find any games, I’ll let you know."
Lo normal "I could try and look out for some too."
c "It seems like you’re all set on things to do now."
Lo "Heh, I guess I am."
$ renpy.pause (2.5)

m "Lorem and I walked in silence for a while, the only sound we could hear was our footsteps. My shoes trudged along the path, and their small claw clinked against pebbles they hit as they walked."
scene np4 
show lorem normal
with dissolveslow
$ renpy.pause (1.0)
show lorem think with dissolve
$ renpy.pause (3.5)
c "Lorem, you’ve suddenly gotten really quiet. Are you okay?"
Lo "Yeah. It’s just something else I was thinking about."
c "What is it?"
Lo "Well, you mentioned [ryann_lorem_true_character_mention] earlier, and it got me wondering about something."
$ renpy.pause (1.5)
Lo sad "Why did you spend time with me? You could have spent time with anyone else. So, why out of everyone, did you choose me?"

label ryann_lorem_post_true_menu:
menu:
    "Because you’re an absolute cutie." if not ryann_lorem_true_lorem_cute:
        $ ryann_lorem_true_lorem_cute = True
        $ ryann_lorem_true_romance += 1
        c "I spent time with you because I think you’re an absolute cutie."
        Lo shy "O-Oh… Um…"
        $ renpy.pause (1.5)
        Lo relieved "B-Be serious, [player_name]."
        show lorem shy with dissolve
        jump ryann_lorem_post_true_menu

    "I am serious." if ryann_lorem_true_lorem_cute:
        $ ryann_lorem_true_mood -= 1
        c "I {i}am{/i} being serious. That is the reason."
        Lo relieved "[player_name]."
        c "What? Do you not believe me?"
        m "Lorem let out a long sigh."

    "Do I need a reason?":
        c "Do I need a reason to spend time with you, other than I wanted to?"
        Lo normal "I guess not."

    "Because I like you.":
        $ ryann_lorem_true_mood += 1
        c "I spent time with you because I like you, and I like spending time with you. It’s that simple."
        Lo normal "Well, I’m really glad to hear that. I like spending time with you too."

$ renpy.pause (1.5)
scene np5e with dissolveslow
$ renpy.pause (0.5)
m "I hadn't realized it, but we had arrived at my doorstep. I wondered if I should invite them in. I wanted to, but so far they hadn't given me any indication they felt the same way. Luckily they broke the tension."
show lorem normal flip with dissolve
$ renpy.pause (0.5)
Lo think flip "It's getting pretty late. I should head back to my apartment before it gets too dark, and Ipsum starts to worry about me."
menu: 
    "See you later, then.":
        c "Alright. I’ll see you later, then."
        Lo normal flip "See ya."
        $ renpy.pause (0.5)
        show lorem normal with dissolve
        hide lorem with easeoutleft
        $ renpy.pause (0.5)
        play sound "fx/flap1.ogg"
        $ renpy.pause (3.5)

    "Do you want to come in?":
        $ ryann_lorem_true_mood += 1
        c "Actually, do you want to come in?"
        Lo think flip "Hmm. I’m not sure. Like I said, Ipsum might worry if I don’t come back without saying anything."
        c "Well, you just call Ipsum from my phone and tell him you'll be here."
        $ renpy.pause (2.0)
        Lo normal flip "Alright."

play sound "fx/door/handle.wav"
$ renpy.pause(1.0)
scene black with fade
stop music fadeout 3.0
$ renpy.pause (4.0)

jump ryann_lorem_aftermath
