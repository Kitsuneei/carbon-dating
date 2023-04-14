# Charactes defined here
define h = Character("Helium", color="ffcccc")
define o = Character("Oxygen", color="ccccff", what_prefix='"', what_suffix='"')
define n = Character("Nitrogen", color="ccccff", what_prefix='"', what_suffix='"')
define c = Character("Test", color="ffffcf")
define nar = Character(what_italic=True)

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

    scene bg room
    window hide Dissolve(boxSpeed)

    nar "Press any key to continue to test."    

    show nitrogen happy at slightleft
    show oxygen happy at slightright
    with enter

    n "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vehicula sapien nisi, maximus dictum est porta fringilla. Curabitur eget urna eu elit lacinia pharetra lobortis. " with Dissolve(boxSpeed)

    show nitrogen sad at slightleft with fadeWithText

    n "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non pharetra nulla, mattis dapibus nisi. "
    
    show nitrogen sad at center
    show oxygen at slighterright
    with ease

    pause 0.5

    show nitrogen neutral with Dissolve(0.4)

    pause 1.0

    nar "Urna eu elit lacinia pharetra lobortis. ...."

    o "Nope."

    hide oxygen with moveoutright

    n "Aight, I'm out!"

    hide nitrogen with leave

    pause 0.5

    scene bg room
    $ oxygen_love = 0

    return

label testing:
    "testing"

    
    python:
        name = renpy.input("What's your name?")

        c.name = name.strip() or "Carbon"    

    c "hello, [c.name]"

    $ nitrogen_love += 10

    c "[nitrogen_love]"

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

    n "You've created a new Ren'Py game."

    o "Once you add a story, pictures, and music, you can release it to the world!"

    "Testing something here."
    "Does this work?"

    "Wow, It's really really dark in here."

    "Lucy" "Better watch out. Testing"
 

    # This ends the game.


