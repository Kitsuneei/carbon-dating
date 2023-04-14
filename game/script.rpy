# Charactes defined here
define He = Character("Helium", color="ffad33", what_prefix='"', what_suffix='"')
define O = Character("Oxygen", color="ff471a", what_prefix='"', what_suffix='"')
define N = Character("Nitrogen", color="668cff", what_prefix='"', what_suffix='"')
define Cl = Character("Chlorine", color="ffff33", what_prefix='"', what_suffix='"')
define C = Character("Carbon", color="ffff66")
define Nar = Character(what_italic=True)

# Transition defined here
define fadeWithText = { "master" : Dissolve(0.5) }
define moveSpeed = 0.5
define leave = Dissolve(moveSpeed)
define enter = Dissolve(moveSpeed)
define boxSpeed = 0.25

# Transform defined here
transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0
transform slighterleft:
    xalign 0.15
    yalign 1.0
transform slighterright:
    xalign 0.85
    yalign 1.0

# Game variables defined here
define nitrogen_love = 0
define oxygen_love = 0

# The game starts here.
label start:
    window hide Dissolve(boxSpeed)
    scene bg dorm
    Nar "You've finally arrived. After several weeks of waiting you've received your acceptance letter and have finally arrived at Catalyst University, the most prestigious college in the whole country. Now all you have to do is finish unloading your bags."
    Nar "After locating your dorm you enter the room to find that it's been completely taken over by your roommate. But they are nowhere in sight. You look at your documentation and see that for their name your roommate has opted to go by their last name, Chlorine."
    Nar "It appears that Chlorine has covered the room with posters and collectibles."
    Nar "There are posters for the most popular recent bands like \"Bad Reaction\" and \"MATTER\". There is a shelf with a dozen collectibles from the best shows today like \"Solution or Solvent\" and \"Periodic Love\"."
    Nar "As you get distracted by the dozens of interesting things in this room you hear the dorm room door creak open behind you. A man wearing shades of green walks in through the door, smiling and waving to someone as he steps through the threshold." 
    Nar "As he turns to you and shuts the door he stops smiling and looks puzzled."

    show chlorine sad at center
    with moveinright

    Cl "I don't remember handing out my key to some random on the street. You aren't one of my ex's lovers coming to teach me a lesson are you?"

    menu:
        "I'm your roommate":
            show chlorine neutral with fadeWithText
            Cl "Oh… well my bad. So you're that transfer student, Carbon right? Well, I guess nice to meet you. I go by my family name here, Chlorine. That's what everyone else does too."
        "Ex's lover?":
            show chlorine happy with fadeWithText
            Cl "Ha, I'm just joking."
            show chlorine neutral with fadeWithText
            Cl "It's obvious you aren't with one of my exs. You're my new roommate… Carbon right? Transfer students from the backcountry or whatever." 
            Cl "I'm assuming you all go by your family names where you are from like we do here."

    show chlorine neutral with fadeWithText

    Cl "So just to clarify, do you go by something else or is Carbon okay?"

    menu:
        "Actually I'd rather you call me by my first name":
            show chlorine sad with fadeWithText
            Cl "Well, what do you go by? Hopefully nothing stupid."
            python:
                name = renpy.input("What's your name?")
                C.name = name.strip() or "Carbon"
            show chlorine neutral with fadeWithText
            Cl "Well, it's nice to meet you [C.name]. At least your name isn't as bad as some of the family names here."
            Cl "I'll tell you are story late about this one kid Boron."
        "You can just call me Carbon":
            python:
                C.name = "Carbon"
            show chlorine happy with fadeWithText
            Cl "Good, fitting in is the first step to not getting repulsed here."

    show chlorine neutral with fadeWithText
    Cl "I'll help you get unpacked. If you just throw your stuff all over the place you'll mess up my vibe."
    Cl "I have people over all the time and I don't want them to be thrown off."
    Cl "Oh also we have our class meeting for the Honors Program in like an hour so let's hurry."

    hide chlorine with moveoutright

    Nar "With Chlorine's help you rush through unloading your luggage."
    Nar "He shows you all the necessities of living in the Second Year Dormitory and tells you a pretty funny story about the kid named Boron. But before you know it you both have to rush to your class." 
    jump classroomA

label classroomA:
    scene bg classroon
    show helium neutral at right
    with enter

    show chlorine neutral at center with moveinleft

    Nar "You and Chlorine make it to the Honors class just in time."
    show chlorine happy at slightright with ease
    Nar "As you slip in and take your seat in the middle of the room you see that Chlorine broke off from you and is now whispering something to the professor."

    show helium happy with fadeWithText
    Nar "The professor listening to Chlorine's whispers turns her eyes to you. She stares at you through her gleaming glasses and smiles."
    show chlorine neutral at slightleft with ease
    Nar "Chlorine finishes talking to her and sits next to you."

    Nar "As Chlorine smirks he turns towards you and gives you a thumbs up. Just then the professor steps away from her lecture podium and moves to the center of the class's view."
    hide chlorine with leave
    show helium at center with ease
    pause 0.5
    show helium neutral with fadeWithText
    pause 0.25

    He "Good Morning everyone. It's a pleasure to see everyone's faces in class today, but I see a new face in the room too."
    He "Now normally a professor wouldn't deem it necessary to welcome a new student to a lecture class but this is the Honors class after all."
    show helium happy with fadeWithText
    He "Everyone please welcome [C.name] to our class. They will be joining us for the rest of the semester.{w} It's not every day that a new student slips into the Honors class at the last minute."

    
label old:
    Nar "Press any key to continue to test."    

    show nitrogen happy at slightleft
    show oxygen happy at slightright
    with enter

    N "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vehicula sapien nisi, maximus dictum est porta fringilla. Curabitur eget urna eu elit lacinia pharetra lobortis. " with Dissolve(boxSpeed)

    show nitrogen sad at slightleft with fadeWithText

    N "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non pharetra nulla, mattis dapibus nisi. "
    
    show nitrogen sad at center
    show oxygen at slighterright
    with ease

    pause 0.5

    show nitrogen neutral with Dissolve(0.4)

    pause 1.0

    nar "Urna eu elit lacinia pharetra lobortis. ...."

    O "Nope."

    hide oxygen with moveoutright

    N "Aight, I'm out!"

    hide nitrogen with leave

    pause 0.5

    scene bg room
    $ oxygen_love = 0

    return

label testing:
    "testing"

    
    python:
        name = renpy.input("What's your name?")

        C.name = name.strip() or "Carbon"    

    C "hello, [c.name]"

    $ nitrogen_love += 10

    C "[nitrogen_love]"

    menu:
        "TestingA":
            "A"
        "TestingB":
            "B"

    #play music "music name here" fadeout 1
    #play sound "sound name here"

    show oxygen happy
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    show oxygen happy at slightleft

    # These display lines of dialogue.

    N "You've created a new Ren'Py game."

    O "Once you add a story, pictures, and music, you can release it to the world!"

    "Testing something here."
    "Does this work?"

    "Wow, It's really really dark in here."

    "Lucy" "Better watch out. Testing"
 

    # This ends the game.


