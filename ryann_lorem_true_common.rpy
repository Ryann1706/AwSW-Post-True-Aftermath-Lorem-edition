
init python:

    ryann_lorem_true_mood = 0
    ryann_lorem_true_romance = 0

    # Post-True variables
    ryann_lorem_true_character_mention = ""
    ryann_lorem_true_humanity_reaction = ""
    ryann_lorem_true_lorem_cute = False # Incorrect

    # Aftermath variables
    ryann_lorem_true_food_choice = ""
    ryann_lorem_true_drink_choice = ""

    ryann_lorem_true_minigame_random1 = 0
    ryann_lorem_true_minigame_random2 = 0
    ryann_lorem_true_minigame_random3 = 0


# Extra character sprites
image lorem angry = "cr/lorem_angry.png"
image lorem angry flip = im.Flip("cr/lorem_angry.png", horizontal=True)
image lorem cry = "cr/lorem_cry.png"
image lorem cry flip = im.Flip("cr/lorem_cry.png", horizontal=True)
image lorem embarrassed = "cr/lorem_embarrassed.png"
image lorem embarrassed flip = im.Flip("cr/lorem_embarrassed.png", horizontal=True)
image lorem emotional = "cr/lorem_emotional.png"
image lorem emotional flip = im.Flip("cr/lorem_emotional.png", horizontal=True)
image lorem blush = "cr/lorem_blush.png"
image lorem blush flip = im.Flip("cr/lorem_blush.png", horizontal=True)
image lorem normal blush = "cr/lorem_normal_blush.png"
image lorem normal blush flip = im.Flip("cr/lorem_normal_blush.png", horizontal=True)
image lorem sleep = "cr/lorem_sleep.png"
image lorem sleep flip = im.Flip("cr/lorem_sleep.png", horizontal=True)
image lorem sleep blush = "cr/lorem_sleep_blush.png"
image lorem sleep blush flip = im.Flip("cr/lorem_sleep_blush.png", horizontal=True)

define And = Character(_("Andreas"), color="#ecad37")
image andreas normal = "cr/andreas_normal.png"


# Extra backgrounds
image ryann_lorem_new_apartment = "bg/ryann_lorem_new_apartment.jpg"
image ryann_lorem_office ="bg/ryann_lorem_office.jpg"
image ryann_lorem_office2 = "bg/ryann_lorem_office2.jpg"
image ryann_lorem_office3 = "bg/ryann_lorem_office3.jpg"
image ryann_restaurant = "bg/ryann_restaurant.jpg"

# Extra minigame assets
image ryann_lorem_eyes = "cg/ryann_lorem_eyes.png"
image ryann_round1 = "cg/ryann_round1.png"
image ryann_round2 = "cg/ryann_round2.png"
image ryann_round3 = "cg/ryann_round3.png"
image ryann_round4 = "cg/ryann_round4.png"
image ryann_round5 = "cg/ryann_round5.png"
image ryann_round6 = "cg/ryann_round6.png"



# Credits
image ryann_lorem_true_credits = "cg/ryann_lorem_true_credits.png"

label ryann_lorem_true_credits:

$ renpy.pause (3.0)
$ _game_menu_screen = None
stop sound fadeout 2.0
scene black with dissolveslow
$ renpy.pause (1.0)
play sound "mx/partingsong.ogg"
$ renpy.pause (1.5)

show ryann_lorem_true_credits with dissolvemed
$ renpy.pause (8.0)
scene black with dissolve

show izumismile2 at Pan((0, 187), (-300, 0), 10.0)
show credits1 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits1 at right with dissolvemed
show chap5 behind credits1 at Pan ((-800, 354), (-700, 354), 10) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show credits2 at left
show map behind credits2 at Pan ((-260, 0), (0, 0), 10)
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits2 at right with dissolvemed
show cgamely behind credits2 at Pan ((-100, 150), (0, 310), 10) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cgclerk at Pan((400, 50), (400, 277), 10)
show credits3 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits3 at left with dissolvemed
show cgdamion behind credits3 at Pan ((400, 100), (400, 250), 10) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show credits4 at right
show cgemera behind credits4 at Pan((400, 150), (400, 302), 10.0)
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits4 at left with dissolvemed
show cgmeeting behind credits4 at Pan ((990, 308), (1240, 0), 10) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show meetingipsum at Pan ((-150, 50), (-100,324), 15)
show credits5 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits5 at right with dissolvemed
show meetingkevin behind credits5 at Pan ( (-100, 177), (-200, 0), 10.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
play movie "cg/chap3/sun2.ogv" loop
show credits6 at left
show movie behind credits6 at Position(xpos=0.75, xanchor='center')
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits6 at right with dissolvemed
stop movie
show meetingkatsu behind credits6 at Pan ((-150, 150), (80, 300), 10.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cgvara at Pan ((250, 326), (500, 150), 10.0)
show credits7 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits7 at left with dissolvemed
show cgseb behind credits7 at Pan((400, 302), (400, 50), 10.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show credits8 at right
show cgarrival behind credits8 at Pan((50, 200), (300, 100), 10.0)
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits8 at left with dissolvemed
show cganna behind credits8 at Pan((360, 302), (360, 0), 10.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cgbryce at Pan((-250, 0), (0, 0), 10.0)
show credits9 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits9 at right with dissolvemed
show meetinglorem behind credits9 at Pan((90, 100), (90, 350), 10.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show credits10 at left
show cgadine2 behind credits10 at Pan((-650, 302), (-650, 0), 10.0)
with dissolvemed
$ renpy.pause (8.0)
show black2 behind credits10 at right with dissolvemed
show cg1 behind credits10 at Pan((-550, 0), (-550, 0), 8.0) with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
scene logo with dissolvemed
$ renpy.pause (10.0)
scene black with dissolveslow
show creditsx with dissolveslow
$ renpy.pause (10.0)
scene black with dissolveslow
show creditsx2 with dissolveslow
$ renpy.pause (5.0)
scene black with dissolveslow
$ renpy.pause (4.0)

jump ml_main_menu
