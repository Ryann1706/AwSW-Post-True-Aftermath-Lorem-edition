
label ryann_lorem_aftermath:

if annastatus != "good":
    $ annastatus = "neutral"

if remystatus != "good":
    $ remystatus = "neutral"

if brycestatus != "good":
    $ brycestatus = "neutral"

if adinestatus != "good":
    $ adinestatus = "neutral"

$ renpy.pause (3.0)
nvl clear
window show
play music "mx/flashback.ogg"

n "There was a large ceremony held to honor me and all the dragons who helped me stop Reza and save both humanity and dragonkind. As time went on, and the dragons adapted to their new lives in our world, things were starting to look up. All the friends that I had made along this journey were living great lives."
n "Adine was offered a sponsorship for her Aerobatics career, while Remy became a school teacher of Dragonic History and Literature. The two of them ended up together and adopted Amely and Vara."
n "Anna was cured of her cancer, pardoned for her crimes, and now serves as the leading scientist in examining the similarities between humans and dragons."
n "Bryce, Sebastian, Maverick, and all the other officers were offered jobs as part of the City Guard. And with dragons guarding the streets, crime rate in the city dropped tremendously."
n "As for me and Lorem…"


stop music fadeout (2.0)
nvl clear
window hide
$ renpy.pause (4.0)
scene ryann_lorem_new_apartment
show ipsum think at center
with dissolveslow
play music "mx/snowflake.ogg" fadein 2.0

$ renpy.pause (1.0)
play sound "fx/unwrap.ogg"
$ renpy.pause (5.0)
c "Well, it's not perfect, but I’d say it's good enough."
Ip "I suppose it will have to do."
Ip sad "I apologize for making this much more inconvenient than it had to be. I doubt I could have done this in time without your help."
c "Have you considered keeping your claws short like Lorem does? Maybe you wouldn’t shred half of the wrapping paper that way."
Ip think "Maybe I should."
$ renpy.pause (2.0)
c "Anyway, how are you and Lorem settling into your new apartment?"
Ip normal "Well, it’s hard not to miss our old one, but this one is more than sufficient."
Ip "Not to mention, it’s actually situated for multiple people, unlike before. So we each have much more room and privacy."
c "Does that mean no more Lorem being woken up by explosions?"
Ip happy "Oh, absolutely not. They wish, though."
c "How come you two are still living together anyway? I’m sure you could get separate apartments if you asked."
Ip think "We did consider it, but it is much more cost-effective living together. Plus, it means fewer chores for each of us to do."
c "That’s fair enough, I suppose."
$ renpy.pause (2.0)
c "Sorry that I already forgot, but what was it that Lorem had to go out to do?"
Ip normal "They had to fill out some paperwork."
c "And how much longer will it be before they get back?"
Ip think "Assuming my timing is correct, they should be here any second now."
$ renpy.pause (1.5)
show ipsum normal with dissolve
show ipsum at right with ease
play sound "fx/door/handle.wav"
$ renpy.pause (1.0)
show lorem normal flip at Position(xpos=0.2) with easeinleft
$ renpy.pause (0.3)
play sound "fx/door/door_close.ogg"
$ renpy.pause (1.0)
Ip happy "Surprise!"
c "Surprise!"
Lo happy flip "W-Woah! What’s all this for?"
Ip "We wanted to congratulate you for all the progress you made on your game."
c "So, we got you a gift."
Lo emotional flip "Awww… You two didn’t need to do that…"
Ip normal "Well, if you think we didn’t need to, then I can just take back the gift."
Lo normal flip "Nope. It’s too late to take back now."
c "Are you going to open it, then?"
Lo "Yeah, of course! I’m really curious to see what it is now."
$ renpy.pause (0.5)
play sound "fx/unwrap.ogg"
$ renpy.pause (0.5)
show lorem happy flip with dissolve
$ renpy.pause (3.0)
show lorem relieved flip with dissolve
Lo "Oh."
Ip happy "What do you think?"
Lo "You got me an Ixomen Sphere…"
c "It was Ipsum’s idea."
Lo think flip "I figured as much."
Ip normal "I thought you loved Ixomen Spheres?"
Lo relieved flip "Seriously, though. You could have gotten anything, but you chose this?"
$ renpy.pause (1.0)
show lorem think flip with dissolve
$ renpy.pause (1.0)
Lo relieved flip "Wait. This better not be your old one, and you've gotten a newer one to replace it, Ipsum…"
Ip "Lorem, I’m not {i}that{/i} bad."
Lo think flip "Well, thanks, I guess."
menu:
    "You deserve it for all the work you put in.":
        $ ryann_lorem_true_mood += 1
        c "Lorem, you deserve something nice like this for all the hard work and effort you've put in."
        Ip "Yes. I can tell it isn’t exactly what you wanted, but you do deserve something for all you’ve accomplished."
        $ renpy.pause (1.5)
        Lo relieved flip "No. You two are right."
        Lo normal flip "I know I don’t sound too enthusiastic, but I really do appreciate it. Plus, I did find it kinda funny."
        Lo "So, [player_name], Ipsum, thank you very much for the gift."

    "You should be grateful you got anything.":
        $ ryann_lorem_true_mood -= 1
        c "Hey! You should be grateful we got you anything."
        Ip sad "[player_name], you don’t have to be so abrasive. If Lorem doesn’t like the gift, we just have to accept that."
        $ renpy.pause (1.5)
        Lo relieved flip "No, Ipsum, [player_name] is right. I should be more thankful."
        Lo think flip "You two went out of your way to get me this. So, thank you for the gift."

    "I hope you enjoy it.":
        c "I can tell you’re not a huge fan of it, but I hope you enjoy it."
        Ip "Yes. I’m sorry you’re not too thrilled, but I do hope you enjoy it too."
        $ renpy.pause (1.5)
        Lo think flip "Actually, I should rephrase what I said."
        Lo normal flip "I know I don’t seem too excited about the gift, but I do appreciate it, and I can see the funny side of it too. So, thank you for getting me this."

Lo think flip "Anyway, I’m sure I’ll be able to find some kind of use for it."
Ip happy "It’s actually one of the most recent and advanced iterations."
c "Yeah. Plus, they really are more useful than you’d think."
Lo normal flip "I’ll take both of your words for it then."
$ renpy.pause (2.0)

Ip normal "So, Lorem, did everything go smoothly with getting that paperwork done?"
Lo happy flip "Yeah! It went great!"
c "What exactly did you have to sort out?"
Lo think flip "Well, I don’t want to bore you with all the official business stuff, so I’ll summarize."
Lo normal flip "It was mostly accounting and finance stuff from all the supporters and sponsors that are funding my game."
Lo "After that whole ceremony thing when we caught Reza, my game suddenly got a whole lot of attention, and lots of people who liked it decided to support me."
Lo happy flip "It even got me attention from an owner of an office block, who let me rent a space at a really discounted price!"
c "That's great to hear. Are you going to be moving in there soon?"
Lo think flip "We already did, actually. A bit over a week ago now, I think."
c "We?"
Lo normal flip "Well, yeah. You didn’t think I’d keep working by myself, did you?"
Lo "I only have one other person working with me right now, but I’m hoping to get a few more in the future."
c "Are you sure you can afford all that?"
Lo "I can. I’m still working doing deliveries to help take care of the essentials, but it’s much more part-time now. On top of the money from supporters and sponsors, I’ll have enough."
$ renpy.pause (1.0)
show lorem think flip with dissolve
$ renpy.pause (1.5)
Lo happy flip "You know, I have to go to the office in a bit to drop off some of that paperwork. So, I could give both of you a tour of the place while I’m there!"
Ip sad "I’m sorry to disappoint you, but I already had plans for later…"
Lo think flip "Well, I can just show you at another time then."
Lo normal flip "What about you, [player_name]?"
show ipsum normal with dissolve

menu:
    "As long as you don’t mind.":
        c "Well, as long as you wouldn’t mind, I’d like a tour of the place."
        Lo "Of course, I don’t mind. I’d love to show you around."

    "I don’t have anything better to do.":
        $ ryann_lorem_true_mood -= 1
        c "Well, I don’t have anything better to do, so I guess I might as well."
        Lo relieved flip "[player_name], come on. I promise you’ll enjoy it."
    
    "I’d love a tour.":
        $ ryann_lorem_true_mood += 1
        c "Sure. I’d love a tour."
        Lo happy flip "And I’d love to give you one!"

Lo normal flip "We can head over there now."
c "Let’s get going, then."
Ip happy "Don’t wreak too much havoc without me."
Lo relieved flip "I’m having second thoughts about bringing you now."
Ip normal "I was joking, Lorem. {w}Mostly, at least."
Lo "Right…"
c "Well, see ya later, Ipsum."
show lorem normal flip with dissolve
$ renpy.pause (0.5)



scene black with dissolveslow
stop music fadeout 2.0
play sound "fx/steps/clean.wav"
$ renpy.pause (3.0)
play sound "fx/door/handle.wav"
$ renpy.pause (1.0)
scene ryann_lorem_office3 with dissolveslow
play music "mx/dash.ogg" fadein 3.0
$ renpy.pause (0.5)
show lorem normal at Position(xpos=0.8) with easeinright
$ renpy.pause (0.5)
play sound "fx/door/door_close.ogg"
show lorem normal with dissolve
show lorem at center with ease
$ renpy.pause (0.5)
Lo happy "And here we are!"
c "Wow. What an office."
Lo think "We’re not in the office yet. This is just the reception."
c "Oh."
c "Wow. What a reception, then."
Lo normal "I know it’s not much now, but we’re still just starting up, and it’ll only improve with time."
$ renpy.pause (1.5)
Lo relieved "You know, I’m a bit bummed that Ipsum couldn’t come along with us. I would have really enjoyed showing him some of the stuff here too."
c "I think it might have been for the best that he didn’t come along. Who knows what kind of tricks or pranks he would have pulled when you weren't looking?"
show lorem normal with dissolve
m "Lorem let out a soft chuckle."
Lo "You have a point there."
Lo think "Anyway, let me show you the actual office space now."
$ renpy.pause (0.5)

scene ryann_lorem_office with dissolve
$ renpy.pause (0.5)
show lorem think flip at Position(xpos=0.35) with easeinleft
$ renpy.pause (0.5)
show lorem normal flip with dissolve
$ renpy.pause (0.5)
Lo "And here’s where most of the work will get done."
Lo think flip "Most of the computers aren’t actually in use right now, but I’m hoping they will be once we get more people on our team."
menu: 

    "You could get lots of work done for your game here.":
        c "It looks like you could get lots of work done for your game here."
        Lo happy flip "That’s the idea!"
        Lo think flip "Working with others will be so much easier than doing pretty much everything myself."

    "This is a really impressive setup you have.":
        $ ryann_lorem_true_mood += 1
        c "Wow. This is a really impressive setup you have here."
        Lo happy flip "I’m glad you think that!"
        Lo think flip "I know it’s not the {i}best{/i}, and there are definitely better options, but it gets the job done well enough until we can get something better, which is enough for me."
        Lo normal flip "Well, at least for now."

    "It seems to be a bit overkill.":
        $ ryann_lorem_true_mood -= 1
        c "It seems to be a bit overkill, considering it’s only two of you working here right now."
        Lo relieved flip "Well, like I just said, I’m playing on hiring more people. It won’t always be just the two of us."

Lo normal flip "Anyway, yeah. This is the main office space. There’s a small meeting room off to the side, a staffroom, and, you know, other stuff like that."
Lo normal flip "Thankfully, this place came mostly furnished already, so I didn’t have to deal with ordering stuff in and assembling furniture."
c "Is there anything else, furniture-wise, you need?"
Lo think flip "Well, nothing we need immediately. Just mostly stuff like water coolers, fans, printers, filing cabinets, and maybe some pictures and decorations too…"
Lo normal flip "Stuff that’ll make things more convenient, comfortable, and organized, really."
Lo "We already have everything we need to actually work though, if that’s what you were wondering."
$ renpy.pause (0.5)
show lorem think flip with dissolve 
$ renpy.pause (1.5)
Lo "Hmm… So what should I show you next?"
$ renpy.pause (1.0)
"???" "Afternoon, Lorem."

show lorem normal flip with dissolve
show lorem at Position(xpos=0.2) with ease
$ renpy.pause (0.5)
show andreas normal at right with easeinright
$ renpy.pause (0.5)
"???" "Huh. I didn't expect to see anyone else. Mind explaining what's happening here?"
Lo "I’m just giving [player_name] a tour."
"???" "Alright. Well, it’s nice to actually meet you in person, [player_name]."
c "You know who I am?"
"???" "I mean, yeah. It’s kind of hard not to know about you after everything you’ve done."
Lo "Anyway, [player_name], this is Andreas. He’s the person I mentioned I’m working with."
c "Alright. Well, it’s a pleasure to meet you, Andreas."
And "As I said, it’s nice to meet you too."
Lo "Honestly, I consider myself so lucky to get to work with Andreas. He’s an absolute blessing."
c "How so?"
Lo happy flip "Well, not only is he a programmer, but he also has experience with video editing, effects, and making music!"
Lo think flip "We’re at the point where we’re making a trailer to show off what’s been done so far, and I thought I’d have to commission someone else to help do it."
Lo normal flip "But like I said, Andreas is a blessing."
And "Does this mean I get to be employee of the month?"
Lo relieved flip "You’re the only employee."
And "…"
And "So is that a yes, or…?"
show lorem normal flip with dissolve
m "Lorem gave an annoyed, yet amused eye-roll in response."
$ renpy.pause (1.5)

c "So, Andreas, would you mind telling me about yourself?"
And "Sure."
And "Well, I’m a huge music and video game fan. And, I’ve actually had an interest in Lorem’s game for a decent bit before working together."
And "And like Lorem said, I’m a programmer, and I do some video editing and music stuff too, which was all mostly freelance work I did. So everything just kinda fit for us to work together."
Lo happy flip "And I couldn’t be more grateful for that!"
c "Well, you definitely seem like an interesting person, Andreas."
And "You know, I could give you my number, and we could talk more later if you want."
c "Sure."
And "Alright, well, one second."
show lorem normal flip with dissolve
m "Andreas quickly went over to a desk and scribbled down a phone number on a piece of paper."
play sound "fx/paper2.ogg"
And "Here you are."
$ renpy.pause (1.5)

And "Anyway, is it alright if I go out for a lunch break now?"
Lo "Yeah, of course."
Lo think flip "Where are you going?"
And "I heard of some fancy restaurant a few minutes from here, so I’m gonna check it out."
Lo "You’re going to a fancy restaurant for your lunch?"
And "Yeah. But I’ll probably get something like chips, some pizza, or something like that. Maybe listen to some music too."
c "You’ve never been to a fancy restaurant before, have you?"
And "Hey. If I want to go to a fancy restaurant by myself, order junk food, listen to some music, and ruin the mood for some fancy, rich couple on a date, that’s what I’m gonna do."
c "Well, have fun, I guess."
And "I’ll see you later, then."
Lo normal flip "See ya."
$ renpy.pause (0.5)
hide andreas with easeoutleft
$ renpy.pause (0.5)
show lorem at Position(xpos=0.35) with ease
$ renpy.pause (0.5)
c "Well, he was interesting."
Lo "He definitely is."
c "What was with that hoodie he was wearing? Is it some kind of uniform?"
Lo think flip "Oh, no. I wouldn’t make anyone wear a uniform. It’s something he just chooses to wear."
c "Is it because humans wear clothes, and everyone is in the human world now, so he wants to try and fit in?"
Lo "He mentioned he's had it for a while now, so I don’t think so."
c "Why is he wearing it, then?"
Lo "I’m not really sure. You’d have to ask him yourself."
$ renpy.pause (2.0)

Lo normal flip "Anyway, there’s something I wanted to tell you something about him."
Lo "But first, I’m assuming you saw his heterochromia?"
menu:

    "It’s pretty weird.":
        $ ryann_lorem_true_mood -= 2
        $ ryann_lorem_true_romance -= 1
        c "Yeah, I saw it. It’s pretty weird."
        Lo sad flip "[player_name], please. Don’t view people based on the things they hatched with."
        Lo relieved flip "It’s not Andreas' fault that he hatched that way, and he can’t control that. So just don’t judge him for it, please."
        c "…"
        c "Right. I’m sorry."
        show lorem think flip with dissolve 
        $ renpy.pause (2.0)

    "Is that why you hired him?":
        c "Yeah. Is that why you hired him?"
        Lo think flip "Well, yes and no."
        c "That’s not really an answer, Lorem."
        Lo "It’s indirectly the reason."
        c "What’s the story, then?"
        Lo normal flip "That’s the reason I brought it up."
        jump ryann_lorem_aftermath_andreas_merge

    "I didn’t even notice.":
        $ ryann_lorem_true_mood += 1
        c "No. I didn’t even notice."
        Lo think flip "Really?"
        Lo normal flip "Well, basically, his eyes are different colours because of a mutation when he hatched."

Lo normal flip "The reason I brought it up was that I wanted to tell you the story of how he was hired."
label ryann_lorem_aftermath_andreas_merge:
Lo "Before I started hiring people, I did some research on how to properly build a team for this kind of stuff, and communication and trust came up a lot."
Lo "So, after sorting through the first batch of applications, I held a group interview."
Lo think flip "Remember when I told you I was a hermaphrodite, and I said I wanted you to know on my terms, rather than someone else's?"
Lo relieved flip "Well, that’s what I did. I told them all I was a hermaphrodite, and anyone who had a problem could feel free to leave."
$ renpy.pause (2.0)
Lo normal flip "Andreas was the only one who stayed."
c "That must have been pretty tough for you to do."
Lo "It really was, but I'm glad I did it."
$ renpy.pause (2.0)
Lo shy flip "Uh, sorry for rambling. Let’s get back on with the tour."
show lorem think flip with dissolve
$ renpy.pause (1.5)
Lo "I guess I can show you my office next."
c "You have your own office?"
Lo normal flip "Yeah. It’s just part of the layout, so it’d be a waste not to use it."
Lo "So, let me show you what it looks like."
$ renpy.pause (1.5)

scene ryann_lorem_office2 with dissolve
$ renpy.pause (0.5)
show lorem normal at Position(xpos=0.65) with easeinright
$ renpy.pause (0.5)
Lo happy "And here’s my office!"
c "Woah."
Lo normal "I know, right?"
menu:

    "You’ve got quite the view from here.":
        c "Well, you’ve definitely got quite the view from in here."
        Lo "It really is beautiful, isn’t it?"
        Lo "I especially like it when the sunlight gets to shine through all the trees. It really helps when it comes to focusing."

    "This is a really cool office.":
        $ ryann_lorem_true_mood += 1
        c "Yeah. This is a really cool office you have here."
        Lo happy "Thank you!"
        Lo normal "Like I said, this place was already furnished, so I haven’t even gotten a chance to personalize it yet."
        c "I bet it'll look even cooler then."

    "It's unfair your office is so much nicer.":
        $ ryann_lorem_true_mood -= 1
        c "It’s kinda unfair how much of a better office space you have compared to what everyone else will get."
        Lo relieved "Like I said, this is what it was like when I first got here. I didn’t choose to make it so fancy-looking."

Lo think "Anyway, give me a second."
$ renpy.pause (0.5)
show lorem at Position(xpos=0.2) with ease
$ renpy.pause (0.5)
play sound "fx/paper.wav"
m "Lorem walked over to a filing cabinet and opened it, putting in the paperwork they did earlier."
show lorem think flip with dissolve
show lorem at Position(xpos=0.35) with ease 
show lorem happy flip with dissolve
Lo "Alright. Now that’s dealt with!"
c "So, what will you be doing here?"
Lo normal flip "Not much different from the others, really."
Lo think flip "Though I’ll have to handle managing stuff now, and finance and PR stuff for the time being too."
Lo relieved flip "And because of what I’m doing, I can’t even utilize most of the stuff that’s already in here. I only use the desk, and stuff like my laptop and a few other small things I brought here."
c "Lorem, you should be careful that you’re not pushing yourself too hard."
Lo normal flip "Oh, you don’t need to worry about me. I expected things to be rocky at the start while I’m still adjusting to this anyway."
Lo "It’s been a huge change, but I can handle it."
$ renpy.pause (1.5)
c "Anyway, would you mind if I asked you something about the progress of your game?"
Lo "Sure. Go ahead."
c "Well, you mentioned you and Andreas were working on a trailer for it, but how much actual work is done on it?"
Lo think flip "Well, for the trailer itself, it’s about half finished. And for the game…"
$ renpy.pause (2.5)
Lo "It’s hard to give an accurate time estimate, but assuming we get some more people working with us, we should have a demo finished in… roughly three to four months."
menu: 
    "I’m interested to see how the extra resources you have will change your game.":
        c "I’m interested to see how all these extra resources from your supporters will change the scope of your game."
        Lo normal flip "That’s exactly why it’s so hard to give a good guess on how long it’ll be before we have something ready."
        Lo think flip "Before, it was just me working on it while still working a full-time job. But now, I’ll, hopefully soon, be working with a team of people."

    "I thought you’d have more done.":
        $ ryann_lorem_true_mood -= 1
        c "I thought you’d have done more with all this extra help you’re getting."
        Lo relieved flip "[player_name], keep in mind that right now it’s still just me and Andreas, and he’s only been here a bit over a week."
        Lo think flip "Also, all this extra help is going to be changing the scope of the game, and I’m having to do a lot more managing and other stuff now too."

    "It’s going to be great with all this extra help.":
        $ ryann_lorem_true_mood += 1
        c "Well, regardless of how much of it is done now, it’s going to be great with all this extra help you have."
        Lo normal flip "Thank you. It really does mean a lot to me to hear that you believe in me."

$ renpy.pause (1.5)
show lorem think flip with dissolve
$ renpy.pause (2.5)
Lo "Well, I’m not really sure what else there is to show you…"
Lo normal flip "I’d take a guess and say you won't find things like being shown a bathroom, storage area, and janitor closet exciting."
c "You’d be right with that guess."
Lo think flip "There’s not really anything else to show you then."

if ryann_lorem_true_mood < 0:
    jump ryann_lorem_true_bad_ending

Lo normal flip "So, I guess this is the end of the tour."
c "Well, thank you then. I really enjoyed it."
$ renpy.pause (1.0)
show lorem think flip with dissolve
$ renpy.pause (2.0)
Lo "I feel like this isn’t enough, though."
c "What do you mean?"
Lo "Well, I know there isn’t much to this office, and I don’t want this to feel underwhelming or disappointing for you."
c "Well, you don’t have to worry about that, because I really did like the tour."
$ renpy.pause (2.5)
Lo normal flip "Alright, I believe you."
Lo think flip "Still, I want to do something more for you."
Lo "It’s just…"
$ renpy.pause (1.5)
Lo emotional flip "You’ve done so much for me, and I want to try to repay it somehow."
c "What do you mean?"
Lo "I mean, you accepted me for being a hermaphrodite, you’re the reason I have this office, and financial support for my game."
Lo normal flip "You’ve even saved my life. Not just my life, but you pretty much saved both of our species from extinction too."
c "You’re making it sound like I did that last thing single-handedly."
Lo "You don’t have to be so humble. If it weren't for you and everything you went through, nothing would have happened in the first place. So you technically {i}are{/i} the reason both of our species were saved."
$ renpy.pause (1.5)
Lo shy flip "I… I’m messing up what I wanted to say."
Lo emotional flip "What I mean is, truly, thank you for everything you’ve done for me."
menu:
    "You mean a lot to me.":
        $ ryann_lorem_true_romance += 1
        c "Lorem, you mean a lot to me. I’m happy just knowing you’re happy. You don’t need to thank me."
        Lo shy flip "O-Oh, well, um… I’m glad that you’re happy too, then."
        Lo think flip  "Uh, so, back to what I was saying."
    
    "Friends are always there for each other.":
        $ ryann_lorem_true_mood += 1
        c "Friends are always there for each other. You don’t need to thank me for that."
        Lo think flip "Right, though our friendship seems to be a bit one-sided, then."

    "Don’t get too mushy.":
        $ ryann_lorem_true_mood -= 1
        c "Alright, Lorem. Don’t get too mushy on me now."
        Lo think flip "Right, sorry."
        $ renpy.pause (2.0)

Lo "I know I can’t do much, but like I said, I want to try to do something for you."
c "Well, what did you have in mind?"
Lo "I can’t really think of anything off the top of my head…"
$ renpy.pause (2.0)
Lo "We could go out somewhere together? Maybe that restaurant Andreas mentioned?"
c "Sure."
Lo normal flip "I have a bit of work to do here, so will tomorrow work for you?"
c "It will."
Lo "Alright. I’ll call you later with the details."
c "I’ll see you tomorrow then."
$ renpy.pause (1.0)


scene black with dissolveslow
stop music fadeout 2.0
$ renpy.pause (2.5)
m "After finishing their work for the day, Lorem let me know the time and place of our meeting."
m "And the following day, we met at the restaurant."
$ renpy.pause (2.0)
play music "mx/hydrangea.ogg" fadein 4.0
$ renpy.pause (2.0)
scene ryann_restaurant with dissolveslow
$ renpy.pause (1.0)
m "Besides critical needs like hospitals, luxury was another thing that the dragons' generators revived. And as Andreas had described, the restaurant was indeed very fancy."
$ renpy.pause (0.5)
show lorem normal flip at Position(xpos=0.35) with dissolve
$ renpy.pause (0.5)
Lo think flip "Wow. When Andreas said fancy, I didn’t think he meant {i}this{/i} fancy."
c "If you think it’ll be too expensive for you, we can go somewhere else."
Lo normal flip "Oh, no. That’s not what I meant."
Lo think flip "It’s just not what I expected."
Lo "Anyway, let’s find somewhere to sit."
$ renpy.pause (1.5)
Lo "Maybe over-{w=0.7}{nw}"
"???" "Hey! [player_name], Lorem!"
show lorem normal flip with dissolve
show lorem at Position(xpos=0.8) with ease
show lorem normal with dissolve
$ renpy.pause (0.2)
show remy normal flip at Position(xpos=0.05) 
show adine giggle b flip at Position(xpos=0.25) behind remy
with easeinleft
$ renpy.pause (0.5)
c "Hey Remy. Hey Adine. It’s great to see you two again."
Ad normal b flip "Yeah, it’s been a while since we last spoke, huh?"
c "Well, things have been really hectic the past few weeks."
Ry "You could say that again."
c "So, what are you two doing here?"
Ry smile flip "We’re here together for a lunch date."
Lo think "Lunch date? So you two are…?"
Ad giggle b flip "Yep, we are!"
show adine normal b flip with dissolve
Ry normal flip "It’s definitely not what I expected to happen, but I couldn’t be happier that things turned out this way."
Ry shy flip "I never thought it was possible, but Adine filled the void in my heart that Amelia left."
$ renpy.pause (0.2)
show remy at Position(xpos=0.16) with ease
play sound "fx/kiss.wav"
show adine giggle b flip with dissolve
$ renpy.pause (0.5)
Ad "Remy! Not in front of [player_name] and Lorem!"
show remy at Position(xpos=0.05) with ease
show remy normal flip with dissolve
show adine normal b flip with dissolve
Lo normal "Well, you two certainly seem like a perfect fit for each other."
$ renpy.pause (1.5)
Ry "Anyway, what are you two doing here?"
Ad giggle b flip "Oohhh~ Are you two on a date too?"
Lo shy "N-No… We… "
$ renpy.pause (1.0)
Lo "U-Um… [player_name]...?"
menu: 

    "Lorem is too cute to resist.":
        $ ryann_lorem_true_romance += 1
        c "What can I say? Lorem is too cute to resist."
        Lo "[player_name]!"
        Ad "Lorem, calm down. We’re just pulling your tail."
        show adine normal b flip with dissolve 
        c "Yeah. It’s just a bit of playful teasing."
        Lo think "R-Right."

    "We’re just friends going out for food.":
        $ ryann_lorem_true_mood += 1
        c "We’re just friends going out for food. That’s it."
        Ad "Oh? {i}Friends{/i} going out to a fancy restaurant {i}alone together{/i}? Sounds fishy if you ask me."
        Ry smile flip "Yes. It makes me a tad skeptical, too."
        Lo "N-No, we’re not… We just…"
        Ad "Lorem, calm down. It’s just a bit of playful teasing. We don’t actually think that."
        show adine normal b flip
        show remy normal flip
        with dissolve
        Lo think "R-Right."

    "I don’t like Lorem in that way.":
        $ ryann_lorem_true_romance -= 1
        c "No, we’re not on a date. I don’t even like Lorem in that way."
        Lo normal "Yeah. We’re just friends."
        Ad normal b flip "Alright. If that's the story you two want to stick with, then go ahead."

c "Wait. If you two are here, then who’s looking after Amely and Vara?"
Ry "Anna is."
c "Anna is?"
Ry "Yes. She feels bad for what she did to Amely, so she’s trying to make up for it by spending time with her."
Ad disappoint b flip "I kinda guilt-tripped her about that, huh?"
Ry "Of course not. I think once she gave it some thought she realized you were right."
Ry smile flip "Plus, it's pretty convenient having a free hatchling-sitter if we need it."
Ad giggle b flip "I can’t argue with that."
show adine normal b flip
show remy normal flip
with dissolve
$ renpy.pause (1.5)
Lo think "By the way, Remy, if you have any spare ties, would you mind if I borrowed one? I have a meeting coming up, and I want to try and look more presentable."
Ry "What do you need it for?"
Lo normal "I have some interviews later in the week."
Ad think b flip "For that game thing you’re working on?"
Lo "Yep. I’m looking for more people to hire."
Ry smile flip "I’m glad to hear that you’re making progress on it."
Ry normal flip "Anyway, I do happen to have some spares. Let me know when you need one then."
Lo "Thanks. Will do."
show adine normal b flip with dissolve
$ renpy.pause (1.0)
Ry "Anyway, we should get going. Hopefully we’ll see you two later at some point."
Lo "Alright. Goodbye then."
c "Yeah. See ya."
$ renpy.pause (0.5)
hide adine
hide remy
with easeoutright
$ renpy.pause (0.2)

Lo think "Well, I guess we should find somewhere to sit too, then."
$ renpy.pause (1.0)
show lorem at center with ease
play sound "fx/chair.wav"
$ renpy.pause (1.0)
show lorem normal flip with dissolve 
$ renpy.pause (0.5)
show lorem at Position(xpos=0.35) with ease
show zhong serv b at right with easeinright
$ renpy.pause (0.5)
if zhongunplayed == False:
    Zh normal b "Good afternoon, [player_name]."
    c "Hello, Zhong. How have you been lately?"
    Zh smile b "Just wonderful. This certainly wasn't the holiday trip I had in mind, but my son sure seems to be enjoying it."
    Zh serv b "And, good afternoon to you as well, Lorem."

else:
    Zh "Well, it seems we have some celebrity guests."
    Lo think flip "Maybe one celebrity guest."
    Zh normal b "From what I recall, you were also present at that ceremony, Lorem."
    Zh "And you’ve become noticeably more well-known because of it."
    Zh serv b "Anyway, good afternoon to both of you."

Lo normal flip "Good afternoon to you too, Zhong."
c "I’m glad to see you’ve gotten a job in a nice place like this."
Zh smile b "And I’m definitely grateful for it."
Zh serv b "Anyway, have you two decided on anything?"
Lo think flip "Well, we just sat down, so we haven’t gotten a chance to."
Zh "Well, take as much time as you need to."
m "I took a look at the lunch options on the menu."
menu:
    "Chips (Fries)":
        $ ryann_lorem_true_food_choice = "chips"
        c "I’ll have some chips."

    "Salad":
        $ ryann_lorem_true_food_choice = "salad"
        c "I’ll have a salad."
        Lo normal flip "I’ll take a guess and say you want that on its own, and not on pizza?"
        c "How did you know?"

    "Omelette":
        $ ryann_lorem_true_food_choice = "omelette"
        c "I’ll have an omelette."

    "Pizza baguette":
        $ ryann_lorem_true_food_choice = "pizza baguette"
        c "I’ll have a pizza baguette."
        Lo think flip "A pizza baguette? What’s that?"
        c "I’m assuming you know what a baguette is?"
        Lo normal flip "Yeah."
        c "So, cut it in half along the length, then put sauce, cheese, and toppings on it, then cook it, and that’s a pizza baguette."
        Lo think flip "Huh. That does sound pretty interesting…"
        c "Interesting enough to try it?"
        Lo "Let’s see the other options first."

show lorem think flip with dissolve 
$ renpy.pause (1.5)
if ryann_lorem_true_food_choice == "salad":
    Lo normal flip "I’ll have a salad too."
else:
    Lo normal flip "I’ll have a salad."

Zh "And for a drink?"
menu:
    "Water":
        $ ryann_lorem_true_drink_choice = "water"
        c "Just water."

    "Juice":
        $ ryann_lorem_true_drink_choice = "juice" 
        c "I'll have some juice."

    "Soda":
        $ ryann_lorem_true_drink_choice = "soda"
        c "I'll have some soda."

    "Tea":
        $ ryann_lorem_true_drink_choice = "tea"
        c "I'll have some tea."
        
    "Coffee":
        $ ryann_lorem_true_drink_choice = "coffee"
        c "I'll have some coffee."

if ryann_lorem_true_drink_choice == "juice":
    Lo "I’ll have juice too, but with ice."
    if ryann_lorem_true_food_choice == "salad":
        $ ryann_lorem_true_mood += 1
        c "I’m starting to think you’re copying me."
        Lo think flip "I don’t mean to. I guess we just have similar tastes."

else:
    Lo "And I’ll have some juice, with ice."

Zh "Okay. I’ll be back with your orders soon."
Lo normal flip "Thank you."
$ renpy.pause (0.5)
show zhong serv b flip with dissolve 
hide zhong with easeoutright
$ renpy.pause (0.2)
show lorem at center with ease
show lorem normal with dissolve
$ renpy.pause (0.5)

Lo think "It’s a bit odd how they have so many snack foods considering how fancy this place is."
c "Well, it’s one of a few non-essential facilities that were spared the resources to open, so it’s no surprise that they’d aim to have a large target audience."
Lo "True."
c "Also, what was up with you asking Remy for a tie for an interview?"
Lo normal "Well, the way I set up the group interviews I mentioned yesterday was per species. Specifically, dragons and humans."
Lo think "I thought it would be easier this way, in case there were any kind of questions or explanations that specifically humans needed."
Lo "And even though we’re all in the human world now, there are still dragons that have a big interest in or are easily excited around humans, and I didn’t want anyone to feel overwhelmed, uncomfortable, or anything bad like that."
c "Are there really dragons that are still excited about humans?"
Lo normal "Well, yeah. Not everyone has gotten to interact with one of you like I have, and some still really look up to, and adore, humans."
c "So they’d act like you did when you first met me?"
Lo "Heh. I guess you got me there."
Lo think "Anyway, I thought because humans wear clothes a lot, I’d seem more professional, and it would be a more comfortable environment if I did something similar."
c "Did enough humans apply that it was actually worthwhile to have a separate interview?"
Lo normal "Oh, yeah. There was a lot."
Lo think "I wasn’t just looking for programmers, designers, and other business-related stuff. I was also looking for models to make sure the human models in the game were as accurate as possible."
c "Oh, Lorem, I didn’t know you were looking for humans to model for you."
Lo shy "Not in that way, [player_name]..."
c "And I thought what we had was special…"
Lo normal "Well, I'm sorry to be the one to tell you, [player_name], but it seems like your modeling days are over."
$ renpy.pause (1.0)
show lorem think with dissolve
$ renpy.pause (1.0)
Lo "On a more serious note, I hope you’re not offended about that."
c "Oh, of course not. You obviously can’t get an accurate model for your game from just one sample."
Lo normal "I’m glad to hear it’s not a problem then."
$ renpy.pause (1.5)
c "Actually, wait a second. You said before that the game will be about mythical creatures, with humans being one of them. But don’t you think with both species living together now, it could kinda invalidate us being included?"
Lo think "You do have a point there, but the target demographic for the game is still mainly dragons, and humans will only be one of multiple species, so I’m sure it’ll be fine."
c "Well, if you say so."
$ renpy.pause (2.0)

show lorem normal flip with dissolve
$ renpy.pause (0.5)
show zhong serv b at Position(xpos=0.95) with easeinright
$ renpy.pause (0.2)
play sound "fx/glasses.wav"
Zh "Here are your orders."
Lo "Thank you."
c "Thanks, Zhong."
Zh "Let me know if you need anything else."
$ renpy.pause (0.5)
show zhong serv b flip with dissolve 
hide zhong with easeoutright
$ renpy.pause (0.2)
show lorem normal with dissolve
$ renpy.pause (0.5)
m "Both of us tried our food simultaneously."
$ renpy.pause (1.0)
Lo happy "Wow! This is really good!"
c "I’d have to agree with you there."
show lorem normal with dissolve
$ renpy.pause (2.5)
show lorem think with dissolve
$ renpy.pause (1.5)
show lorem relieved with dissolve
$ renpy.pause (0.5)
c "What’s wrong, Lorem?"
Lo think "Well, I wanted us to go out so we could have a good time together, but just going out to eat like this is kind of boring…"
c "…"
c "I might have an idea to fix that."
m "I signalled Zhong to come over to our table."
$ renpy.pause (0.5)
show lorem normal flip with dissolve
show zhong serv b at Position(xpos=0.95) with easeinright
Zh "Is there anything I can help with, [player_name]?"
c "Yes. I was wondering, do you have anything here to entertain your guests? Any games or other distractions?"
Zh normal b "I doubt we do, but I'll check just in case."
show lorem think flip with dissolve
show zhong normal b flip with dissolve
hide zhong with easeoutright
$ renpy.pause (3.0)
show zhong normal b at Position(xpos=0.95) with easeinright
Zh "You’re in luck. There was a deck of playing cards in our lost and found box."
c "That’s convenient."
Zh serv b "You will have to return them though."
c "Of course."
Zh "Feel free to let me know if you need anything else."
show zhong serv b flip with dissolve 
hide zhong with easeoutright
$ renpy.pause (0.2)
show lorem normal with dissolve

Lo "So, what are we going to play now that we have some cards?"
c "Hmm…"
$ renpy.pause (1.5)
c "Truth or Dare."
Lo think "I’ve never heard of that game before. How do you play it?"
c "Well, the core rules of the game are very simple. They’re so simple that most of the time, people add some kind of twist, or have extra rules, so I’ll just explain the version that we’ll be playing."
c "Both of us will draw a card, and the highest card wins. The winner then gets to choose if they want the loser to do a truth, or a dare."
c "If you choose truth, then the winner gets to ask the loser a question, and they have to answer it, no matter what it is."
c "If you choose dare, then the winner gets to dare the loser to do something, and again, they have to do it, no matter what it is."
Lo "What kind of things do you ask the other person to do?"
c "It can be anything you want. Something funny, embarrassing, something the other person wouldn’t usually say or do, or something you want them to do."
Lo normal "Alright. I think I get it."
c "Let’s get started then."
$ renpy.pause (1.0)

stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round1 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round1
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (2.0)

c "(10 of clubs…)"
Lo think "What did you get?"
m "I placed my card on the table for them to see."
Lo relieved "I got an eight…"
c "So I win."
Lo normal "Yes, you do."
c "I’ll give you an example of what a dare can be. And I’ll be nice and go easy on you to start with."
menu:
    "Chug the rest of your drink.":
        c "I dare you, to chug the rest of your drink."
        Lo think "Oh. That doesn't seem so hard."
        c "I did say I’d go easy on you."
        Lo "Here we go then."
        $ renpy.pause (0.5)
        play sound "fx/gulp2.wav"
        $ renpy.pause (6.0)
        play sound "fx/glassdown.wav"
        Lo normal "Ahh."

    "Eat a mouthful of food without using your hands.":
        c "I dare you, to eat a mouthful of your food, without using your hands."
        Lo relieved "Oh. This will be fun and not at all messy."
        c "You have to do it. That's the rules."
        Lo think "Alright. Here goes nothing…"
        $ renpy.pause (1.5)
        m "Lorem lowered their face down into their bowl; So close their face was almost touching their food."
        m "Following a few moments of apprehension, Lorem attempted to eat some of the salad."
        $ renpy.pause (1.5)
        m "Then, after a decent period of Lorem messily struggling to eat, they eventually sat back up."
        $ renpy.pause (1.0)
        Lo "You know, that actually wasn’t as hard as I thought it would be."
        Lo normal "I’m just glad I didn’t put any kind of dressing on my salad."
        $ renpy.pause (1.5)

    "Keep an ice cube in your mouth until it melts.":
        c "I dare you, to keep an ice cube in your mouth until it melts."
        Lo relieved "Seriously?"
        c "Yep."
        Lo think "Alright…"
        $ renpy.pause (1.5)
        Lo happy "Ha! The ice cubes have already mostly melted from sitting in my drink."
        c "That doesn’t mean you get out of having to do it."
        Lo think "I know, but it at least won’t be as bad now."
        m "Lorem plucked an ice cube from their drink and proceeded to put it in their mouth."
        show lorem sad with dissolve
        m "Almost immediately, their face was overcome with a wave of discomfort."
        $ renpy.pause (2.5)
        m "For about half a minute, Lorem continued to sit very much in discomfort with the ice cube slowly melting in their mouth."
        $ renpy.pause (2.0)
        show lorem think with dissolve
        $ renpy.pause (2.0)
        Lo "Okay, I might have overreacted a bit. It wasn’t that bad."

Lo normal "You were right about going easy on me."
c "Don’t get used to it."
$ renpy.pause (1.5)

Lo think "So we draw again?"
c "Yep."
$ renpy.pause (0.5)
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round2 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round2
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (1.0)

$ ryann_lorem_true_minigame_random1 = renpy.random.randint(1, 5)
c "(3 of diamonds. Lovely…)"
Lo normal "I got a nine."
c "Well, you win this time."
Lo "Right. So I can dare you to do anything?"
Lo think "Hmm…"
$ renpy.pause (2.0)

if ryann_lorem_true_minigame_random1 < 4:
    # Prank call
    Lo normal "You said I can make you do something embarrassing, right?"
    c "Yes, as long as it’s within reason. And I don’t like where this is going."
    Lo think "Did you bring your phone with you?"
    c "…"
    c "Yes. And again, I don’t like where this is going."
    Lo normal "I want you to make a prank call."
    c "Alright. Who should I call?"
    Lo think "Pick someone randomly."
    c "Okay."
    m "I opened my contacts, looked away, and picked one at random."
    $ renpy.pause (2.5)
    Lo normal "Who is it?"

    if ryann_lorem_true_minigame_random1 == 1:
        c "Oh."
        Lo happy "Come on! Tell me!"
        c "It’s Remy."
        Lo normal "Oh, this will definitely be embarrassing."

    elif ryann_lorem_true_minigame_random1 == 2:
        c "I think you’ll enjoy this."
        Lo happy "Tell me!"
        c "It’s Andreas."
        Lo normal "Oh, I {i}will{/i} enjoy this!"

    else:
        c "Oh no…"
        Lo happy "Oh, now I really want to know who it is!"
        c "It’s Anna."
        Lo normal "Good luck with that."

    c "So, what should I say?"
    show lorem think with dissolve
    $ renpy.pause (2.5)
    Lo normal "I’ll go easy on you too, and I’ll let you say nothing."
    c "You want me to just stay silent?"
    Lo normal "Yep."
    c "Alright then."
    play sound "fx/phonering.ogg"
    $ renpy.pause (3.5)
    stop sound 
    $ renpy.pause (1.0)
    
    if ryann_lorem_true_minigame_random1 == 1: # Remy
        m "I tried my best not to look at Remy and Adine, but I could still see them out of my peripheral vision."
        m "I had only then noticed a small bag next to Remy, which he started to look through, presumably to find his phone."
        $ renpy.pause (2.0)
        m "He eventually did find it, and after struggling to interact with it for a bit, he answered it."
        Ry "Hello, [player_name]?"
        $ renpy.pause (3.0)
        Ry "[player_name], are you there?"
        $ renpy.pause (3.0)
        m "Remy then lowered the phone to speak with Adine."
        Ad "{size=-10}Is that [player_name]?{/size}"
        Ry "{size=-10}I presume so. It’s from their phone.{/size}"
        show lorem happy with dissolve
        m "I tried desperately to focus on eating and avoid looking even in their general direction."
        m "But I could still see Adine look over at us with a puzzled look."
        Ad "{size=-10}But they aren’t using their phone?{/size}"
        Ry "{size=-10}Maybe they called accidentally then?{/size}"
        Ad"{size=-10}Maybe.{/size}"
        m "Remy then hung up the call."
        $ renpy.pause (1.5)
        c "I hope you enjoyed that."
        Lo happy "I did. The looks on your face were priceless!"
        $ renpy.pause (1.5)
        m "A few seconds later I got a text."
        Ry "([player_name], I got a call from you a few moments ago, but I think it was accidentally sent from your phone. If it wasn’t, call me back at some point later.)"
        Lo think "Who is that?"
        c "Remy. He thought it was an accidental call, and to call him back if it wasn’t."
        c "I feel bad that he went through the effort to get his phone and text me back, but it was all for nothing."
        Lo normal "Then why didn’t you say anything?"
        c "…"
        c "Let’s just move on to the next round."

    elif ryann_lorem_true_minigame_random1 == 2: # Andreas
        And "Hey. This is [player_name]’s number, right?"
        $ renpy.pause (3.0)
        And "Hello? Anyone there?"
        $ renpy.pause (3.0)
        And "Hey, are you messing with me or something?"
        $ renpy.pause (3.0)
        m "Abruptly, Andreas hung up."
        Lo think "I guess he figured it out pretty quick."
        c "I guess he did."
        m "Then I suddenly got a text."
        And "(Just got a silent call from you. Either your phone is broken, or it was a prank. If it wasn’t, let me know.)"
        Lo normal "Is that Andreas?"
        c "Yeah. But I’m pretty sure he knew it was a prank."
        c "Well, I hope that prank call was what you hoped for."
        Lo "It was entertaining enough."
        c "Anyway, let’s move on to the next round."

    else: # Anna
        An "Hey, [player_name]. What is it?"
        $ renpy.pause (3.0)
        An "[player_name], are you there?"
        $ renpy.pause (3.0)
        An "I’m busy right now. I’m looking after Amely and Vara. What do you want?"
        $ renpy.pause (3.0)
        An "[player_name], I don’t exactly have the time to wait until you feel like talking."
        $ renpy.pause (4.0)
        An "{size=-10}That cheeky bastard just prank-called me…{/size}"
        m "Then she hung up."
        m "And as soon as she did, I heard Lorem start chuckling."
        c "Well, I hope you enjoyed that."
        Lo happy "I did!"
        c "Let’s move on to the next round."
        show lorem normal with dissolve

elif ryann_lorem_true_minigame_random1 == 4:
    Lo normal "You said I can make you do something funny, right?"
    c "As long as it’s within reason."
    Lo think "What about puns?"
    c "Yep. That’s fair enough."
    Lo normal "Alright. You’re next three sentences have to have a pun in them, then."
    c "…"
    Lo happy "And they have to be food or restaurant-related."
    c "(Right. Because this needed to be made harder…)"
    show lorem normal with dissolve
    $ renpy.pause (2.5)
    c "You {i}butter{/i} appreciate the effort I’m putting into these puns, because they take {i}thyme{/i} to get right."
    c "I value our {i}friend-chip{/i}, but you’re a real {i}pizza-work{/i} for making me do this."
    c "I’m {i}bready{/i} to be done with this now."
    Lo happy "I have to say, I’m {i}berry{/i} impressed!"
    c "…"
    Lo normal "What?"
    c "I hope that you enjoyed that."
    Lo happy "Oh, I did!"
    c "Let’s just move on to the next round."

else:
    Lo normal "You said I can make you do anything I want you to do?"
    c "As long as it’s with reason."
    Lo happy "I know exactly what I want you to do, then."
    Lo normal "Order and pay for dessert for us."
    c "…"
    Lo "You {i}did{/i} say I can make you do anything."
    c "I did…"
    Lo "So?"
    c "Alright, I will."
    Lo think "I wonder what I should choose…"
    c "Hey! I’m the one paying, so I get to choose."
    Lo normal "Alright. That’s fair enough."
    Lo think "What are you picking?"
    c "Cake?"
    Lo normal "Sure."
    m "I signaled Zhong to come to our table."
    $ renpy.pause (0.5)
    show lorem normal flip with dissolve
    show zhong serv b at Position(xpos=0.95) with easeinright
    Zh "Yes?"
    c "Can we have two orders of cake, please?"
    Zh "The only kind we have today is chocolate. Is that okay?"
    c "Yeah."
    Zh "Just a moment then."
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    $ renpy.pause (3.0)
    show zhong serv b at Position(xpos=0.95) with easeinright
    Zh "Here you are."
    c "Thanks, Zhong."
    Lo "Thank you."
    Zh "You’re welcome."
    $ renpy.pause (0.5)
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    show lorem normal with dissolve
    $ renpy.pause (0.5)
    Lo happy "And thank you, [player_name], for the cake!"
    c "Yeah, yeah. Let’s just move on to the next round."

$ renpy.pause (1.0)
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round3 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round3
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (1.0)

c "(Queen of spades…)"
c "What did you get?"
Lo think "A six."
c "Then I win."
c "I’ll give you an example of a truth this time."
Lo "That’s when you ask me a question that I have to answer, right?"
c "Yep. So…"
menu:
    "What is your biggest fear?":
        c "What is your biggest fear?"
        Lo "My biggest fear?"
        $ renpy.pause (1.5)
        Lo sad "I mentioned it before, but it’s probably having to step into the limelight and let the world know I’m a hermaphrodite and that I have to do it eventually if I want to finish my game."
        Lo think "Like I said before, I told everyone who showed up for my interview, and that was unnerving enough, but it wasn’t as bad as my fears were telling me it would be."
        if ryann_lorem_true_humanity_reaction == "accepted":
            Lo "You said humanity would accept me, which has really given me hope, but it still is scary to think about."

        elif ryann_lorem_true_humanity_reaction == "unsure":
            Lo "You said it’s hard to tell how humanity would react, which is true, but I’m really hoping that humanity is different from how dragonkind would react."

        elif ryann_lorem_true_humanity_reaction == "harsh":
            Lo relieved  "You said humanity might react harshly, and that makes it even harder for me to do, but I’m still holding on to the hope that you’re wrong on that."

        $ renpy.pause (2.0)
        c "I probably shouldn’t have brought that up. I’m sorry."
        Lo normal "You don’t have to apologize. There’s no point trying to avoid it and not talk about it. It’s something inevitable I need to deal with."
        $ renpy.pause (1.5)
        c "Let’s move on to the next round."

    "Do you have a crush on anyone?":
        c "Do you have a crush on anyone?"
        Lo relieved "Really?"
        c "That’s how the game works. You have to answer."
        Lo think "Alright, fine."
        $ renpy.pause (2.0)
        if ryann_lorem_true_romance == 3:
            Lo normal blush "I… I might, but I’m not saying more than that."
            c "You might?"
            Lo think "Well, I’m pretty sure, but not 100 percent yet."

        elif ryann_lorem_true_romance < 0:
            Lo normal "I’m pretty sure I don’t. No one immediately comes to mind at least."

        else:
            Lo "I’m not too sure if I do yet. I guess I’ll just have to wait and see."
            c "You’ll have to wait and see?"
            Lo "Yeah. I’m not totally sure if they like me, so I’ll have to wait until they say anything, or hint at it, or something."

        c "Right."


    "Who would you choose between me and Ipsum?":
        c "If you had to choose between me and Ipsum, who would choose?"
        Lo "Choose how?"
        c "If we were both in a situation where we were about to die, and you could only save one of us, who would you choose?"
        Lo "That’s pretty hard…"
        Lo relieved "You’ve done so much for me and have been a great friend, but I’ve known Ipsum for years…"
        $ renpy.pause (3.0)
        c "I’m not sure how to feel about you taking so long to answer."
        Lo sad "It’s a hard question to answer!"
        $ renpy.pause (3.0)
        Lo think "I think I’d choose you, though."
        c "Are you just saying that because I’m the one in front of you right now?"
        show lorem normal with dissolve
        $ renpy.pause (3.0)
        Lo think "No."
        c "Right."

show lorem normal with dissolve
$ renpy.pause (1.0)
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round4 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round4
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (1.0)

$ ryann_lorem_true_minigame_random2 = renpy.random.randint(1, 3)
c "(5 of clubs…)"
Lo think "Hey, so, completely random and unrelated question, but is an ace the highest or lowest card for this game?"
c "Let’s say it’s the lowest."
Lo happy "Good thing I have the king of hearts then!"
c "You cheeky little…"
Lo normal "Hey! You can’t say anything. You only said ace was the lowest because you thought it was what I had. Don’t deny it."
c "Fine. You got me there."
Lo "So I win."
Lo think "The dares are fun, so I’ll pick that again."
$ renpy.pause (2.0)
if ryann_lorem_true_minigame_random2 == 1:
    Lo normal "I want you to eat a spoonful of salt."

elif ryann_lorem_true_minigame_random2 == 2:
    Lo normal "I want you to order a glass of water, then throw it in your face."

else:
    Lo normal "I want you to order something spicy and eat it."

c "Wow. Really picking it up a notch, huh?"
Lo "The only limit you said was “within reason”."
c "True. But you should be careful with raising the bar so much. "

if ryann_lorem_true_minigame_random2 == 1: # Salt
    m "Lorem reached to the edge of the table, grabbed a salt shaker, and handed it to me."
    Lo "Well? What are you waiting for?"
    c "Fine…"
    m "I unscrewed the salt shaker's lid and poured a shallow pool into a spoon that was on the table."
    m "I held it in front of me, apprehensive for what was about to come."
    Lo "Come on. Stop stalling."
    m "I mustered my willpower and shoved the spoon in my mouth."
    m "I immediately almost gagged as all the moisture was sucked out of my mouth."
    show lorem happy with dissolve 
    m "I couldn’t tell what face I made, but it was very entertaining based on Lorem's reaction."
    m "It was a struggle swallowing due to how dried up my mouth was, but I just barely managed to."
    m "I couldn’t help but let out a series of dry coughs and finish the remainder of my [ryann_lorem_true_drink_choice] to help with how dehydrated I now felt."
    c "I hate you for that."
    Lo normal "If it makes you feel any better, I found that very entertaining."
    c "It doesn’t."
    Lo "Oh well. I’m sorry to hear that."
    c "I’m going to get back at you for that."

elif ryann_lorem_true_minigame_random2 == 2: # Water
    if ryann_lorem_true_minigame_random1 == 5:
        Lo think "And poor Zhong, having to come over to our table so much."
        c "You’re the one picking dares that involve ordering something."
        Lo normal "Yeah. This’ll be the last one then."
        m "Once again, I signaled Zhong to come over."

    else:
        m "I signaled Zhong to come over to our table."

    show lorem normal flip with dissolve
    show zhong serv b at Position(xpos=0.95) with easeinright
    Zh "Yes, [player_name]?"
    if ryann_lorem_true_drink_choice == "water":
        c "Could I have another glass of water, but a small one, please?"
    else:
        c "Could I have a small glass of water, please?"
    Zh "Of course."
    $ renpy.pause (0.5)
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    $ renpy.pause (3.0)
    show lorem normal flip with dissolve
    show zhong serv b at Position(xpos=0.95) with easeinright
    $ renpy.pause (0.5)
    play sound "fx/glassdown.wav"
    Zh "Here you are."
    c "Thanks."
    Lo "Well?"
    m "I sighed and picked up the glass."
    show black with dissolve
    show lorem happy flip
    show zhong shy b
    m "I closed my eyes, and threw the cup in my face."
    $ renpy.pause (0.5)
    play sound "fx/splash.wav"
    $ renpy.pause (2.5)
    m "I picked up a napkin off the table, dried off my face, then opened my eyes."
    hide black with dissolveslow
    m "And it was only then noticed Zhong still at the table, giving me a concerned look."
    Zh "That’s the first time I’ve had someone do something like that sober."
    c "Lorem made me do it. It was for a dare."
    show lorem normal flip with dissolve
    Zh "Well, unlike others, you at least have a reason."
    c "Yeah, uh, sorry about that."
    Zh serv b "If you need any more napkins, let me know."
    $ renpy.pause (0.5)
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    $ renpy.pause (0.5)
    show lorem normal with dissolve
    Lo "That was fun."
    c "I’m glad you're enjoying this at least."
    
else: # Spicy
    if ryann_lorem_true_minigame_random1 == 5:
        Lo think "And poor Zhong, having to come over to our table so much."
        c "You’re the one picking dares that involve ordering something."
        Lo normal "Yeah. This’ll be the last one then."
        m "Once again, I signaled Zhong to come over."

    else:
        m "I signaled Zhong to come over to our table."

    show lorem normal flip with dissolve
    show zhong serv b at Position(xpos=0.95) with easeinright
    Zh "Yes, [player_name]?"
    Lo happy flip "How about some hot sauce?"
    c "Yeah. Could you bring us some hot sauce? And some water too?"
    Zh "Of course. One moment."
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    $ renpy.pause (3.0)
    show zhong serv b at Position(xpos=0.95) with easeinright
    Zh "Here you are."
    c "Thanks, Zhong."
    Zh "Let me know if you need anything else."
    show zhong serv b flip with dissolve 
    hide zhong with easeoutright
    show lorem normal with dissolve
    Lo "Well, drink up, [player_name]."
    c "I’m not drinking hot sauce!"
    Lo "Alright. Just a sip then."
    c "Okay…"
    m "I opened the lid of the hot sauce and brought it up to my mouth then took a quick, small swig of it."
    m "A few seconds after swallowing, I felt the heat coat my whole mouth, and even in my nose."
    m "It wasn’t unbearable, but still extremely irritating and slightly painful."
    m "I then chugged the glass of water, which helped, but didn’t stop the burning feeling."
    m "After a minute of struggling, the heat eventually subsided."
    $ renpy.pause (2.0)
    c "I hate you for that."
    Lo happy "That looked like it was {i}bad{/i}."
    c "It was. You better hope you don’t need to get up or move away from your food at any point."
    Lo normal "Yeah, I’m sure you’ll do that."
    c "Even if I don’t do that specifically, I’m going to get back at you for this."

$ renpy.pause (1.0)
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round5 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round5
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (1.0)

$ ryann_lorem_true_minigame_random3 = renpy.random.randint(1, 3)
c "(7 of diamonds…)"
Lo think "What did you get, [player_name]?"
c "The seven of diamonds."
Lo happy "Lucky for me, I got the jack of diamonds!"
c "Great."
Lo normal "Looks like I’m on a roll."
c "You got two in a row…"
Lo "And how many have you got in a row?"
c "…"
Lo think "I’ll think I’ll pick the truth one this time."
Lo happy "And I also think I’ll ask something really embarrassing!"
c "Or you could not do that."
Lo normal "You said I can make you do something embarrassing as long as it’s within reason, so that’s what I'll do."
c "You’re really using the whole “within reason” thing as an excuse for everything, huh?"
Lo "Well, they're your rules."
Lo think "So…"
$ renpy.pause (2.0)

if ryann_lorem_true_minigame_random3 == 1:
    Lo normal "Do you think humans or dragons are more attractive?"
elif ryann_lorem_true_minigame_random3 == 2:
    Lo normal "If you could go on a date with anyone you’ve met while in the dragon world, who would you choose?"
else:
    Lo normal "What trait do you find most attractive in someone?"

c "Oh my god, Lorem, really?"
Lo "Come on, [player_name]. Answer the question."
m "I let out a long sigh."
c "Alright, fine."
$ renpy.pause (1.0)

if ryann_lorem_true_minigame_random3 == 1:
    menu:
        "Humans":
            $ ryann_lorem_true_romance -= 1
            c "I think I find humans are more attractive."
            Lo think "Yeah, I probably should have expected that, huh?"
            c "Well, it makes sense that someone would find their own species more attractive. "
            c "Especially given that a few months ago, humans were the only sentient, intelligent species that we knew of."
            Lo normal "You make some fair points."

        "Dragons":
            $ ryann_lorem_true_romance += 1
            c "Being honest, I think I’d have to say I find dragons more attractive."
            Lo shy "O-Oh. Really?"
            c "Yeah. I don’t really know why, I just do."
            Lo think "Interesting."

        "Equal":
            c "I think I find humans and dragons equally attractive."
            Lo think "Really?"
            c "Yeah. I don’t think species matters, but other things like personality, are more important."
            Lo normal "Yeah, I think I’d have to agree with you on that one."

elif ryann_lorem_true_minigame_random3 == 2:
    menu:
        "You":
            $ ryann_lorem_true_romance += 1
            c "Being honest, I’d choose you."
            Lo shy "O-Oh, really?"
            Lo "W-Well, um…"
            $ renpy.pause (2.0)
            c "Seems like your plan to embarrass me backfired, huh?"
            c "Unless… You wanted me to choose you?"
            Lo "N-No! T-That’s not what I…"
            c "Hey, you were the one who asked the question. It’s not my fault you don’t like the answer."
            Lo relieved "Let’s just move on."

        "Adine":
            c "I think I choose Adine."
            Lo think "But, Adine and Remy said earlier that they're dating…"
            c "…"
            c "Right. I forgot about that."
            c "But I mean, if they weren’t together, I’d choose Adine."
            Lo "Okay. That makes more sense."

        "Anna":
            c "I think I’d choose Anna."
            Lo think "That’s an interesting choice. Why her?"
            c "I just have a sneaking suspicion that a date with her would be pretty fun and exciting."
            Lo "I’m assuming that’s got something to do with other timeline stuff?"
            c "Maybe."

        "Bryce":
            c "I think I’d choose Bryce."
            Lo think "Bryce, huh? Is there any reason why?"
            c "Well, who wouldn’t want to go out with the chief of police? {w}Well, ex-chief of police…"
            c "Plus, he’s a good-hearted person, and despite his flaws, he’s trying to improve himself."
            Lo normal "Well, as long as you’re happy, [player_name]."

        "Remy":
            c "I think I’d choose Remy."
            Lo think "But, Adine and Remy said earlier that they're dating…"
            c "…"
            c "Right. I forgot about that."
            c "But I mean, if they weren’t together, I’d choose Remy."
            Lo "Okay. That makes more sense."

        "Ipsum":
            $ ryann_lorem_true_romance -= 1
            $ ryann_lorem_true_mood -= 1
            c "You know, being honest, I’d choose Ipsum."
            Lo relieved "Seriously, [player_name]? Out of everyone, you had to choose my roommate?"
            c "What can I say? He’s a pretty charming and handsome guy."
            m "Lorem sighed."
            Lo "Let’s just move on."

else:
    menu:
        "Intelligence":
            c "I think I find intelligence most attractive."
            Lo think "Hmm. Yeah, that’s a reasonable enough thing, I suppose."

        "Looks":
            c "I think I find looks most attractive."
            Lo think "Looks? I mean, I can understand the importance of finding someone physically attractive, but, personally, I don’t think it’s the most important thing."
            c "Well, everyone has their own opinions and preferences."
            Lo "True, but still, there’s a lot more to people than looks alone."

        "Personality":
            c "I think I find someone’s personality the most attractive."
            Lo normal "Yeah. I completely agree with you on that."
            Lo think "I can understand why other people would say things like looks, or intelligence, but how well you can get along with someone is extremely important."
            Lo normal "I’m assuming when you say personality, you’re looking for something specific?"
            menu:
                "Something similar to your beautiful personality.":
                    $ ryann_lorem_true_romance += 1
                    c "I’m looking for something like your beautiful personality."
                    Lo shy "O-Oh. well, um…"
                    Lo think "T-Thank you? Was that a compliment?"
                    c "Let’s say it was."

                "You’ve already asked your one question.":
                    c "Lorem, you’ve asked your one question already."
                    Lo think "Oh, right. I forgot about that part."

        "Ambition":
            c "I think I find someone’s ambition most attractive."
            Lo think "Someone’s ambition? What do you mean?"
            c "I mean how ambitious someone is. How much drive or motivation they have to do what they want or need."
            Lo "Oh, I get it now."
            Lo normal "I’ve never heard someone mention that before as what they find most attractive, but now that you’ve explained it, I totally agree with you."
            Lo think "Still, just ambition is pretty vague. Is there something more specific you look for?"
            menu:
                "The ambition you have for your game is truly admirable.":
                    $ ryann_lorem_true_romance += 1
                    c "An example is the ambition you have for making your game. I find it truly admirable."
                    Lo shy "O-Oh. W-Well, thank you, for the compliment."

                "You’ve already asked your one question.":
                    c "Lorem, you’ve asked your one question already."
                    Lo think "Oh, right. I forgot about that part."

        "Wealth":
            $ ryann_lorem_true_romance -= 1
            $ ryann_lorem_true_mood -= 1
            c "I think how much wealth someone has, is what I find most attractive."
            Lo relieved "Seriously, [player_name]?"
            c "What?"
            Lo sad "Finding someone attractive based on their money is such a shallow thing to do…"
            $ renpy.pause (2.5)
            Lo relieved "Let’s just move on."


$ renpy.pause (1.0)
show lorem think with dissolve
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show ryann_lorem_eyes at Pan ((500, 0), (0, 0), 1.0)
show ryann_round6 at Pan ((-500, 0), (0, 0), 1.0)
with dissolvemed
$ renpy.pause (2.0)
hide ryann_lorem_eyes
hide ryann_round6
with dissolvemed
play music "mx/hydrangea.ogg" fadein 1.0
play sound "fx/card.wav"
$ renpy.pause (1.0)

c "(The 4 of spades… Lorem isn’t going to get three in a row, are they?)"
Lo relieved "Oh…"
c "What is it?"
Lo think "Remember that you said an ace was the lowest?"
c "I do."
Lo relieved "Well, take a guess what I got."
c "Serves you right for trying to trick me earlier."
Lo think "So, uh, what do you choose?"
c "So, I bet you thought you’d get away with the last two things you made me do consequence-free, right?"
Lo relieved "Oh no…"
c "I’ll choose a dare."
$ renpy.pause (2.0)
menu:
    "Improv a random conversation with Adine and Remy.":
        c "I dare you to go up to Adine and Remy unprovoked and improv a random conversation with them."
        Lo think "Uh, what do you mean?"
        c "Just go over to Adine and Remy’s table and start talking."
        if ryann_lorem_true_minigame_random1 == 1:
            Lo relieved "I can’t do that. We interrupted their date enough already with that prank call."
            c "It’s a dare, Lorem. You have to do it."

        m "Lorem sighed."
        Lo think "Okay. So, um, what should I talk to them about?"
        c "That’s for you to figure out when you get over there."
        Lo shy "But I have no clue what to say!"
        c "Exactly. Good luck."
        Lo relieved "Oh…"
        $ renpy.pause (0.5)
        show lorem relieved flip with dissolve
        $ renpy.pause (1.0)
        hide lorem with easeoutright
        $ renpy.pause (0.5)
        m "Lorem then slowly got out of their seat and sluggishly made their way over to Adine and Remy’s table."
        m "They were too far away for me to hear, but I could tell Lorem’s approach was very unprecedented."
        m "At first, things seemed to be going well. Most of what I assumed was just basic small talk and other conversation filler."
        if ryann_lorem_true_minigame_random1 == 1:
            m "Then I saw Remy gesture over to me. I was confused at first, but I soon remembered the prank call, and hoped Lorem would explain it away while they were over there."
        $ renpy.pause (2.0)
        m "After a bit more conversing, I saw Lorem begin to pause and stutter a lot. "
        m "And even though I was a fair distance away, I saw a faint pinkish glow appear on Lorem’s face."
        m "Soon after, Lorem quickly left them and came back over to our table."
        $ renpy.pause (0.5)
        show lorem embarrassed at center with easeinright
        $ renpy.pause (0.5)
        c "So, how’d it go?"
        Lo "Oh my gosh…"
        c "Not well?"
        $ renpy.pause (2.0)
        Lo shy "Okay so, it started fine. I asked how their date was going, how they were, and other small talk stuff like that."
        Lo embarrassed "But, then I asked if they were dating anyone, or if they were looking for a relationship. Even though they told us they were dating, less than an hour ago…"
        c "That doesn’t sound like a good situation."
        Lo shy "It really wasn’t…"
        Lo "But it gets worse."
        Lo "Then, I tried to change the subject…"
        $ renpy.pause (1.5)
        show lorem embarrassed with dissolve
        $ renpy.pause (1.5)
        Lo "By asking if they were planning on having kids."
        c "Oh no."
        Lo shy "Thankfully, they thought the whole thing was a joke."
        Lo embarrassed "But, still, I can’t help but feel so embarrassed…"

    "Say something out loud for everyone to hear.":
        c "I dare you, to say something out loud, for everyone in the restaurant to hear."
        Lo shy "Oh my gosh, really, [player_name]?"
        c "Hey. It’s a dare. You have to do it, Lorem."
        show lorem relieved with dissolve
        m "Lorem let out a long sigh."
        Lo shy "Fine. What do you want me to say?"
        c "Hmm…"
        $ renpy.pause (2.5)
        c "I know exactly what I want you to say."
        c "I want you to say: “I am the cutest little blue dragon to ever exist.”"
        Lo relieved "[player_name]."
        c "What? I’m only making you speak the truth."
        if ryann_lorem_true_minigame_random2 == 1:
            c "Plus, I bet you thought it was all fun and games when you made me eat salt. Now, I’m just getting back at you."
        elif ryann_lorem_true_minigame_random2 == 2:
            c "Plus, I bet you thought it was all fun and games when you made me throw water in my face. Now, I’m just getting back at you."
        else:
            c "Plus, I bet you thought it was all fun and games when you made me drink hot sauce. Now, I’m just getting back at you."

        Lo embarrassed "I can’t believe I’m doing this…"
        $ renpy.pause (2.0)
        show lorem shy with dissolve
        play sound "fx/chair.wav"
        m "Lorem then stood up from their seat, and then for a few moments, stood in silence."
        $ renpy.pause (2.5)
        Lo "I-{w=0.5}{nw}"
        $ renpy.pause (1.5)
        Lo "{size=+3}I am the cutest little blue dragon to ever exist!{/size}"
        show lorem embarrassed with dissolve
        show lorem at Position(ypos=1.1) with ease
        m "Lorem then immediately sat back down and tried their best to hide from the world by hunching nearly completely over and covering their face."
        Lo "Oh my gosh…"
        c "What’s wrong, Lorem?"
        Lo "I hate you for making me do that."
        Lo "I’m so embarrassed…"
        c "Lorem, I mean, if you don’t want to accept the truth…"
        show lorem shy with dissolve
        show lorem at Position(ypos=1.0) with ease
        Lo "S-Shush up! Just, stop talking about this."
        c "(Shush up? That’s how Lorem says “shut up”? That’s adorable.)"

    "Kiss me.":
        c "I dare you… to kiss me."
        Lo shy "W-What? Are… Are you being serious?"
        c "Lorem, don’t pretend to be oblivious. You know the rules by now."
        Lo relieved "O-Okay, fine."
        Lo think "So, you, uh, must mean, like, on the cheek, or something like that, right?"
        menu:
            "Hand":
                c "No, just on the hand."
                Lo "Oh. That’s not too bad then."
                c "I want to do something to get back at you. But I don’t want to embarrass you {i}too{/i} much."
                Lo "Let’s just do this then."
                play sound "fx/chair.wav"
                m "Lorem rose from their seat on the other side of the table and walked over to mine."
                show lorem shy with dissolve
                m "They sheepishly reached out with their small scaly hand and took mine in it, bringing it closer to their face."
                play sound "fx/kiss.wav"
                m "Lorem then placed a gentle kiss on my hand from their scaly lips, then quickly made off back to their seat."
                Lo relieved "I really hope no one saw that."
                c "You do know Remy and Adine watched the whole thing, right?"
                Lo shy "W-What?!"
                c "I just messing with you. They didn’t."
                Lo embarrassed "D-Don’t joke about that! I’m already embarrassed enough…"

            "Cheek":
                $ ryann_lorem_true_romance += 1
                c "Yep. Right on the cheek."
                Lo shy "Let’s just get this over with then."
                play sound "fx/chair.wav"
                m "Lorem, taking their time, then got up from their seat on the opposite side of the table and came over to my side."
                m "They stood next to me and apprehensively inched their face closer to mine."
                $ renpy.pause (2.0)
                play sound "fx/kiss.wav" 
                m "Suddenly, they planted a quick peck on my cheek, before scurrying back to their seat."
                Lo embarrassed "Oh my gosh…"
                c "What’s wrong, Lorem?"
                Lo shy "I can’t believe you made me do that…"
                Lo relieved "I really hope no one saw."
                c "You do know Remy and Adine watched the whole thing, right?"
                Lo shy "W-What?!"
                c "I just messing with you. They didn’t."
                Lo embarrassed "D-Don’t joke about that! I’m already embarrassed enough…"

            "Lips":
                $ ryann_lorem_true_romance += 2
                c "Nope. I want you to kiss me on the lips."
                Lo shy "[player_name]!"
                Lo "We’re in public! W-What if someone sees?"
                c "Hey. A dare is a dare, and that means you have to do it."
                Lo embarrassed "…"
                Lo shy "F-Fine…"
                Lo embarrassed "L-Let’s just get this over with…"
                play sound "fx/chair.wav"
                m "I stood up from my seat, as Lorem slowly got up from theirs as well."
                m "Lorem then slowly shuffled over and stood in front of me. And I proceeded to lower myself down slightly to match their height."
                $ renpy.pause (1.5)
                show lorem shy with dissolve 
                $ renpy.pause (1.0)
                play sound "fx/kiss.wav"
                m "After a good few seconds of stalling, Lorem quickly gave me a peck on the lips, then scurried back to their seat and began to hide their now very red face."
                c "What’s wrong, Lorem?"
                Lo embarrassed "Oh my gosh, I can’t believe you made me do that…"
                Lo shy "Seriously, what if someone saw that…?"
                c "Lorem, everyone else here is focused on themselves, or whoever they're with. No one saw us."
                Lo "S-Still, I just…"
                Lo embarrassed "It’s just so embarrassing…"


$ renpy.pause (3.0)
c "You know, I think this is a good point to finish the game."
Lo shy "Y-Yeah, I think so too."
c "I can take a guess at how you feel about it, but I found this to be pretty fun."
Lo think "W-Well, despite all the embarrassing stuff, I enjoyed it too."
Lo "I can tell from this small example that it can be a pretty fun game though. Maybe if there were more people, and we weren’t in public, it could be even better?"
c "Hmm, maybe."
$ renpy.pause (2.0)
Lo normal "Anyway, we're pretty much done here, so how about we call Zhong over?"
c "Sure."
$ renpy.pause (1.5)
show lorem normal flip with dissolve
show zhong serv b at Position(xpos=0.95) with easeinright
$ renpy.pause (0.5)
Zh "Do you need anything else?"
Lo "Yes. We’d like to get our bill."
Zh "Just a moment then."
show zhong serv b flip with dissolve 
hide zhong with easeoutright
$ renpy.pause (3.0)
show zhong serv b at Position(xpos=0.95) with easeinright
Zh "Here you are. Also, you can return the card when you’re ready."
c "Here are the cards."
Zh "Thank you."
c "So, are we going to split the bill?"
Lo "Oh, no. I’m paying for everything."
c "Are you sure? I don’t mind paying for my own food."
Lo "[player_name], I was the one who invited you out, so I should be the one paying. I don’t mind."
if ryann_lorem_true_minigame_random1 == 5:
    c "Alright, but are you paying for the cake too?"
    Lo think flip "Well, I did specify you're the one paying for it."
    c "So, you’re not paying for everything."
    Lo normal flip "That’s the one exception because it was a dare. Everything else is paid."

c "Well, if you say so."
show lorem think flip with dissolve 
$ renpy.pause (1.5)
Lo normal flip "Here’s the money for the bill. And you can keep the rest."
Zh "Thank you very much. Please come again."
$ renpy.pause (0.5)
show zhong serv b flip with dissolve 
hide zhong with easeoutright
show lorem normal with dissolve
$ renpy.pause (0.5)
Lo think "So, now that the bill is taken care of, what should we do now?"
c "We could just go for a walk."
Lo normal "Sure. But where to?"
c "I have an idea."
Lo "Well, lead the way then."
$ renpy.pause (0.5)

scene black with dissolveslow
stop music fadeout 2.0
$ renpy.pause (1.5)
m "I decided to take Lorem to a nearby lake, and after a short walk around its edge, we found a place to sit."
$ renpy.pause (1.5)


scene park2
show lorem think
with dissolveslow
play music "mx/starlight.ogg" fadein 1.5
$ renpy.pause (2.5)
Lo "Okay, so we agree on pizza, but what if, not counting cheese and sauce, you could also only choose one topping?"
c "Now that’s an even harder one. There are so many good options."
Lo normal "Well, there’s only one way to settle this."
c "How?"
Lo happy "So, we have a pizza party, order lots of pizzas, and each pizza has its own individual topping. Then we just figure out which option is the best from there!"
c "Maybe we should postpone this idea for the time being. You’ve already spent enough on food today."
show lorem normal with dissolve
$ renpy.pause (1.5)
c "I probably should have asked sooner, but how are you settling into the human world?"
Lo think "Well, I think it’s been pretty good here so far. I know I’ll still miss our world, but I have a feeling that it won’t be too bad staying here forever."
Lo happy "One thing I find amazing is how similar our species really are. Even just the small stuff, like food, hobbies, books, and furniture. It’s so cool, yet also so strange how near-identical human things are to ours!"
Lo normal "Even some of your myths are very alike to some of our own."
c "Speaking of our myths, did you ever get a chance to look at some of ours about dragons?"
Lo happy "I did, actually!"
Lo "As I expected, not all of them are accurate, but some are shockingly close! It’s almost like certain dragon species were based on some of those myths."
c "You know, you might not actually be too far off from the truth there."
Lo think "What do you mean?"
c "You know your creation myth about a human creating you? It’s actually completely true. And you got to meet that human."
Lo "Wait, really?!"
c "Yep. Izumi, the human who helped us stop Reza, is the reason dragons exist."
Lo happy "That’s… Amazing!!!"
Lo "I actually got to meet the human who created dragons! That’s so cool!"
c "I have a feeling you’re going to rub that in Ipsum’s face {i}a lot{/i}."
Lo "Oh, absolutely! He’ll never hear the end of it."
$ renpy.pause (1.0)
show lorem normal with dissolve
$ renpy.pause (2.0)
m "We sat in silence for a while, just watching over the still, shimmering lake, while a cool, refreshing breeze washed over us."
$ renpy.pause (2.0)

if ryann_lorem_true_mood < 6:
    # Neutral ending
    $ renpy.pause (1.5)
    m "After a bit longer, Lorem eventually broke the silence."
    Lo happy "You know, today was a lot more fun than I thought it would be."
    c "Yeah, I enjoyed it a lot too."
    Lo normal "I’m glad to hear that."
    Lo think "But I should probably be going now."
    Lo normal "I don’t want to fall too far behind on work, and leave Andreas working on his own for too long."
    c "It’s alright. I understand."
    Lo "We should hang out again soon. I’ll try to find some spare time that’s more just a few hours."
    c "Hey, Lorem, I get it, you’re really busy with your game now, and it’s hard for you to have as much free time now."
    Lo think "It really is, but still, I’ll try to find some time. Thanks for being so understanding."
    c "It’s no problem."
    Lo normal "Anyway, I’ll see you later!"
    c "See ya."
    $ renpy.pause (0.5)
    hide lorem with easeoutleft
    $ renpy.pause (1.0)
    m "And just like that, Lorem was gone. But I decided to stay and sit for a while longer, and enjoy the view."
    $ renpy.pause (1.5)
    scene black with dissolveslow
    $ renpy.pause (1.5)

else:
    # Good endings
    menu: 
        "Move closer to Lorem":
            $ ryann_lorem_true_romance += 1
            play sound "fx/undress.ogg"
            m "I moved closer to Lorem, sliding down the bench, so their tail was now brushing up on my leg."
            show lorem shy with dissolve 
            m "I saw a familiar blush out of my peripheral vision, but they didn’t move away or reject my advances."

        "Don’t get any ideas":
            pass

    $ renpy.pause (1.5)
    show lorem think with dissolve
    $ renpy.pause (1.5)
    Lo "Hey, [player_name]?"
    c "Yeah?"
    Lo "I know today wasn’t much in comparison to what I owe you, but I still hope you enjoyed it."
    c "You need to stop doing that."
    Lo "Doing what?"
    c "Feeling like you owe me something."
    Lo relieved "But I can’t help it. You’ve done so much for me, and both of our species. I feel-"
    m "I put my hands on Lorem’s shoulders and turned them to look at me."
    show lorem shy with dissolve
    c "Lorem. You don’t owe me anything."
    c "I didn’t save both of our species to get something out of it. I did it became it was the right thing to do."
    c "I didn’t spend time with you to get something out of it. I did it because I like you, and I care about you."
    c "Us being here together right now, and after everything we’ve been through is payment enough, okay?"
    $ renpy.pause (1.5)
    show lorem think with dissolve 
    $ renpy.pause (2.0)
    Lo normal "Okay, I hear you. You’re right."
    Lo relieved "I know I’ve said it to death at this point, but you’ve done so much for me, and I’m forever grateful for it."
    Lo normal "But, you're right. You didn’t do any of it to get something back."
    Lo "And I really care about you too."
    $ renpy.pause (1.0)
    play sound "fx/undress.ogg"
    m "I let go of Lorem’s shoulders and we both went back to staring at the lake."
    Lo think "But, yeah, now that you mention it, we really have been through a lot, huh?"
    c "Yeah, I guess we have…"
    $ renpy.pause (2.5)
    c "(We really have been through a lot…)"
    m "The words echoed throughout my head and led me to think of all the good times we’ve had over the past few weeks."
    m "But just as the good memories appeared, the bad ones reared their ugly head too."
    stop music fadeout 2.0
    $ renpy.pause (2.0)

    play sound "fx/heartbeat.ogg"
    scene storex 
    with flash
    $ renpy.pause (1.5)
    show lorem think at center with dissolve
    $ renpy.pause (0.5)
    Lo "(No. It’s not over here…)"
    $ renpy.pause (1.5)
    show lorem think flip with dissolve
    $ renpy.pause (1.0)
    Lo happy flip "(It must be underwater then!)"
    Lo think flip "(Well, here goes nothing.)"
    $ renpy.pause (0.5)
    play sound "fx/splash.wav"
    hide lorem with dissolve 
    $ renpy.pause (3.0)
    play sound "fx/underwatercrash.ogg"
    $ renpy.pause (2.0)
    play sound "fx/loremknocks.ogg"
    $ renpy.pause (5.0)
    stop sound

    play sound "fx/heartbeat.ogg"
    scene park2
    show lorem think 
    with flash
    $ renpy.pause (0.5)
    Lo "[player_name]? Are you okay?"
    $ renpy.pause (0.5)

    play sound "fx/heartbeat.ogg"

    show loremwounded with flash
    $ renpy.pause (3.0)
    scene black with dissolveslow
    $ renpy.pause (0.5)
    play sound "fx/rev.ogg"
    $ renpy.pause (0.5)
    play sound "fx/boxdive.ogg"
    $ renpy.pause (0.5)
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)
    play soundloop "fx/hiss.ogg" fadein 1.0
    $ renpy.pause (1.0)
    play sound "fx/run.ogg"
    $ renpy.pause (1.5)
    stop soundloop fadeout 1.0
    $ renpy.pause (2.0)
    play sound "fx/explosion.ogg"
    $ renpy.pause (6.0)
    
    play sound "fx/heartbeat.ogg"
    scene park2
    show lorem sad 
    with flash
    Lo "[player_name]! [player_name], what’s wrong?"
    m "I abruptly snapped out of my head and back into my surroundings."
    play music "mx/starlight.ogg" fadein 2.5
    m "I noticed Lorem looking extremely concerned clinging to my shirt, shaking me to snap me back to reality."
    Lo "[player_name], please. Tell me what’s wrong…"
    c "S-Sorry, Lorem. It’s just memories of the other timelines."
    c "I just wish I could just forget them all."
    m "I only then noticed a few tears that had been running down my face."
    $ renpy.pause (2.0)
    Lo think "What were you thinking about?"
    c "Other timelines where you died. Other timelines where I couldn’t save you…"
    Lo normal "Well, you managed to save me in this one."
    c "But that doesn’t mean I can just forget the times when I couldn’t!" with vpunch
    show lorem sad with dissolve
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    m "Lorem then suddenly wrapped their arms around me and pulled me into a comforting hug."
    Lo "[player_name], it’s okay now. You’re safe, I’m safe, everyone is safe."
    Lo normal "I know it must have been painful to go through all of that, but because you did, you were able to make everything right this time."
    $ renpy.pause (3.5)
    c "Thank you for that, Lorem."
    c "In the end, I guess it was worth it. Because now I can focus on the present, and look forward to the future."
    Lo "Hopefully a future I can be a part of."
    c "Of course you will be, Lorem."
    $ renpy.pause (2.5)
    m "After a while when I had calmed down, we broke apart from our hug and I settled for keeping hold of Lorem’s shoulders again."
    c "I doubt I could have made it this far without you."
    $ renpy.pause (1.5)
    if ryann_lorem_true_romance > 3:
        menu:
            "Kiss Lorem":
                $ renpy.pause (1.5)
                m "Lorem and I looked into each other's eyes. Their’s shining a beautiful amber in the daylight."
                m "I moved my hand from their shoulder, to their neck, as I slowly moved closer to them."
                show lorem shy with dissolve 
                m "Lorem seemed to understand what was happening, as they began to blush passionately, and they started to move closer too."
                show lorem sleep blush with dissolve
                m "We closed our eyes, still inching closer together, and I soon felt their scaly lips against mine."
                $ renpy.pause (2.0)
                show lorem normal blush with dissolve
                m "We parted shortly after and continued to stare into each other's eyes for a few moments."
                $ renpy.pause (1.5)
                Lo blush "I… I-I don’t know what to say…"
                c "I'm pretty sure we both know how the other feels though."
                Lo "T-That we both, um, {i}like{/i} each other…?"
                c "Yep."
                $ renpy.pause (3.0)
                Lo relieved "Honestly, I-I’ve liked you for a while now, but I was worried that you wouldn’t feel the same, because I’m a hermaphrodite…"
                c "Remember what I said when you told me? I don’t mind at all."
                show lorem normal blush with dissolve 
                $ renpy.pause (1.5)
                Lo relieved "It’s so relieving to hear you say that…"
                show lorem normal blush with dissolve 
                m "Now sure of our feelings, Lorem proceeded to cuddle into my side and wrap their small tail around my back, as I put my arm around their shoulder and pulled them closer."
                Lo think "So, where do we go from here?"
                c "I’m not too sure. But I know we’ll figure it out together."
                Lo normal blush "Yeah."
                $ renpy.pause (2.0)
                Lo think "You know, I kind of get how you feel. When I used to think about the future, I only thought of things that made me worried, anxious, or scared…"
                Lo normal "But knowing you’ll be part of it from now on, I feel a lot safer, and more secure."
                c "I’m glad that you’ll be a part of my future too, Lorem."
                $ renpy.pause (2.0)
                m "We sat in silence, cuddling for a while longer, just enjoying the view, and each other's warmth and company."
                $ renpy.pause (2.0)
                Lo think "This lake is really beautiful, huh?"
                c "Yeah, it really is."
                Lo shy "Well, it’s, uh, not as beautiful, as you…"
                c "Awwww."
                Lo "Um, s-sorry. I’m not very experienced with, uh, this kind of stuff…"
                play sound "fx/kiss.wav"
                m "I gave Lorem a small kiss on their forehead."
                c "Don’t worry about it. It was pretty cheesy, but it was so adorable as well."
                Lo blush "O-Oh, well, I’m glad you liked it…"
                m "Lorem then gave me a small lick on the cheek in return."
                c "You’re so cute."
                $ renpy.pause (2.0)

                m "I then withdrew my hand from Lorem’s shoulder, and instead moved under their wings and started to gently caress their side."
                show lorem sleep blush with dissolve
                play soundloop "fx/purr.ogg" fadein 1.5
                m "In response, Lorem moved, so they were now resting their head on my lap and started purring adorably."
                Lo "That feels amazing…"
                c "Just be careful with your horns, okay?"
                Lo "Yeah…"
                $ renpy.pause (3.0)
                Lo "If I fall asleep, wake me up, okay? You’re just so warm, and comfortable…"
                c "Alright. Maybe I will."
                $ renpy.pause (3.0)
                Lo "I love you, [player_name]..."
                c "I love you too, Lorem."
                $ renpy.pause (2.5)
                stop soundloop fadeout 5.0
                show lorem sleep with dissolveslow
                $ renpy.pause (3.5)
                m "And just like that, the purring slowly faded, then soon stopped. Lorem was fast asleep on my lap."
                m "Good thing I had no intentions of moving anytime soon."
                $ renpy.pause (2.5)
                scene black with dissolveslow


            "Look away":
                jump ryann_lorem_true_friendship_ending

    else:
        label ryann_lorem_true_friendship_ending:
        m "We once again went back to staring at the lake."
        $ renpy.pause (2.0)
        c "Anyway, sorry for all that. Overall, I really enjoyed today. Thanks for inviting me."
        Lo "It’s no problem. I really enjoyed today too."
        Lo happy "We should hang out like this again soon!"
        c "Would your work not get in the way?"
        Lo normal "Don’t worry, I always have time for you."
        Lo happy "That’s what friends are for, right?"
        c "Aww. That was so sweet."
        $ renpy.pause (2.0)
        Lo think "You know, I kind of get how you feel. When I used to think about the future, I only thought of things that made me worried, anxious, or scared…"
        Lo normal "But I’m glad to know that I’ll always have a friend that has my back no matter what."
        Lo "I really couldn’t have a better friend. Thank you, [player_name]."
        c "I couldn’t ask for a better friend either, Lorem."
        $ renpy.pause (2.5)
        scene black with dissolveslow

$ renpy.pause (1.0)
m "I finally did it, dragonkind is safe, humanity is on the road to recovery, and Lorem was starting to find more acceptance, and was getting closer and closer to finishing their game."
m "For the first time in what feels like an eternity, I was looking forward to the future."
stop music fadeout 2.0


jump ryann_lorem_true_credits



label ryann_lorem_true_bad_ending:

# Lo think flip "There’s not really anything else to show you then."
c "Really? That’s it?"
Lo "Well, yeah. It’s a pretty small office."
c "That’s pretty disappointing then."
c "I really expected there to be more to it than that."
Lo relieved flip "Well, I’m sorry you feel that way."
Lo think flip "If you wanted, we could go out and do something to try and make up for it."
c "Yeah. It’d be nice to do something actually enjoyable. What did you have in mind?"
Lo relieved flip "Well, I don’t really have an idea on the spot like that…"
stop music fadeout 4.0
c "Seriously? You couldn’t even think of something for us to do? Why did you even offer in the first place?"
$ renpy.pause (3.0)
play music "mx/fragments.ogg" fadein 1.5
Lo sad flip "[player_name], we need to talk."
c "About what?"
Lo "It’s just… Something about you has changed."
Lo "I don’t know what happened, but you’ve been acting completely differently."
Lo "You said you didn’t mind when I told you I was a hermaphrodite, but, honestly, I’m starting to think that’s not true."
c "What are you talking about?"
Lo relieved flip "You’ve been acting unnecessarily mean, dismissive, or just… off."
Lo sad flip "And I’ve been trying to make excuses for you. That all that time travel stuff was messing with you… Or you’ve been overstressed because of work, or other things…"
Lo relieved flip "But I can’t keep ignoring this and try to stay ignorant."
c "I really have no clue what you’re talking about."
Lo cry flip "Seriously? Y-You didn’t even realize what you were doing and saying to me this whole time?"
c "What? So I make a few comments and do a few things you don’t like and you start making a big deal over it like I’ve been bullying you?"
c "I mean, come on, Lorem. Learn to take a joke instead of overreacting."
$ renpy.pause (2.5)
show lorem angry flip with dissolve
Lo "This is exactly what I’m talking about!" with vpunch
Lo "I’m clearly hurt about something, yet you don’t care how I feel! You just say I’m overreacting and need to take a joke!"
Lo "I’m not just going to let you keep bullying and belittling me!"
Lo "And you don’t even realize what you've been actually saying!? You really are just as bad as all those other bigoted idiots!"
$ renpy.pause (1.5)
show lorem cry flip with dissolve
$ renpy.pause (2.0)
Lo "I thought I found someone else I could finally trust… Someone who wouldn’t judge for something I can’t control, but no. You’re just like everyone else…"
Lo "It’s the same as always. Someone I trusted. Someone I considered a friend."
stop music fadeout 3.5
$ renpy.pause (3.0)
Lo relieved flip "[player_name], I’m still grateful for everything you’ve done for me. You’re the reason I have this office, financial support for my game, and you’ve even saved my life. I won’t forget that."
Lo sad flip "But I won’t keep putting up with this."
$ renpy.pause (2.5)
Lo relieved flip "Please… Just leave…"
c "L-Lorem, I-{w=0.5}{nw}"
Lo cry flip "Stop. It doesn’t matter what you’re about to say. Just leave."
$ renpy.pause (1.5)
m "I left still in shock, shaken and unnerved from seeing Lorem actually angry."
$ renpy.pause (1.0)
scene ryann_lorem_office with dissolveslow
$ renpy.pause (2.0)
scene ryann_lorem_office3 with dissolveslow
$ renpy.pause (2.0)
scene town5 with dissolveslow
$ renpy.pause (2.0)
m "I went outside the office block and sat at the top of a staircase just outside and reflected on my recent actions."
m "I hated myself for what I did. What was wrong with me? How could I hurt Lorem like that after what they’ve been through?"
m "The wave of guilt washing over me made me nauseous."
m "And there was nothing I could do to make amends with Lorem. It was too late to go back…"
$ renpy.pause (3.5)
m "Or was it…?"
$ renpy.pause (1.5)
scene black with dissolveslow
$ renpy.pause (1.5)

jump ml_main_menu
