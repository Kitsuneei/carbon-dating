# Charactes defined here
define He = Character("Helium", color="ffad33", what_prefix='"', what_suffix='"')
define O = Character("Oxygen", color="ff471a", what_prefix='"', what_suffix='"')
define N = Character("Nitrogen", color="668cff", what_prefix='"', what_suffix='"')
define Cl = Character("Chlorine", color="ffff33", what_prefix='"', what_suffix='"')
define C = Character("Carbon", color="ffff66")
define M = Character("???", color="ffffff", what_prefix='"', what_suffix='"')
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
define current_path = "oxygen"

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
    scene bg classroon with dissolve
    show helium neutral at right
    with enter

    show chlorine neutral at slightleft with moveinleft

    Nar "You and Chlorine make it to the Honors class just in time."
    show chlorine happy at center with ease
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

    Nar "The whole of the class looks to you. Some faces smile, others glare, and others simply don’t care. {w} They give you applause led by the Professor."
    
    hide helium with leave


    Nar "As the class calms a few faces look at you a little longer than the rest."

    show chlorine neutral at center with enter

    show oxygen neutral at left behind chlorine with enter

    show nitrogen neutral at right behind chlorine with enter
    
    Nar "There is Chlorine who is devilishly smirking at you along with a boy in red and a girl in blue."

    hide chlorine
    hide nitrogen
    hide oxygen
    with dissolve

    Nar "Class seems to drag on as Professor Helium seems to adore long lectures. But as the day flies by the class comes to a close with a final important note."

    show helium happy at center with enter
    He "Class time is about over but there is one more thing I want to remind you all of before our next class Friday."
    He "The Molecular Dance is coming up this Friday night and it's required that all Honors students attend as role models for the rest of the students."
    show helium neutral with fadeWithText
    He "I know I've told you this all before but this is still important for our newest student to know."

    show helium sad with fadeWithText
    He "Oh and remember. {w} It is not required but being a bonded pair is strongly suggested."

    show helium happy
    He "So make sure you bring your plus one with you."

    show chlorine neutral at left with moveinleft
    pause 0.5
    show chlorine happy with fadeWithText
    pause 0.1

    Nar "You catch Chlorine staring at you with a smile raising his eyebrows in a mocking manner."

    pause 0.5
    hide chlorine happy with moveoutleft

    show helium neutral with fadeWithText
    He "That's all the time we have.{w} I'll see you all Friday morning for our second class time."

    Nar "The professor gathers her things and leaves the classroom. A few other students follow her out."

    hide helium with moveoutright
    pause 0.5

    Nar "As you gather your things Chlorine stops you."

    show chlorine neutral at center with moveinleft
    pause 0.5
    Cl "Act natural, but you have two of my least favorable exs heading this way. I'm running, but you cover me."

    show chlorine happy with dissolve
    pause 0.5
    show chlorine at slightleft with ease
    hide chlorine with moveoutright
    pause 0.5

    Nar "Chlorine leaves abruptly only giving you enough time to turn and greet the two other students approaching you. It's the boy and girl from earlier."

    pause 0.25
    show oxygen happy at slighterright with moveinright
    show nitrogen neutral at slighterleft with moveinleft
    pause 0.25

    N "Hi welcome to Catalyst University. I’m Nitrogen."

    O "Yeah, it's nice to meet you. You can call me Oxygen."

    O "Oh by the way, sorry for that embarrassment that the Prof put you through at the start of class."
    O "It was Chlorine who did that, wasn't it? {w}He's always been missing a few electrons."

    show nitrogen sad with fadeWithText
    N "He's not missing anything Oxygen. He's just a troublemaker."

    show oxygen neutral with fadeWithText
    O "I'm just joking. Don't take it so literally."

    show nitrogen neutral with fadeWithText
    N "Whatever, I've got to head out." 

    pause 0.25
    show nitrogen at center
    show oxygen at right
    with ease
    pause 0.25
    show nitrogen happy
    pause 0.25

    N "But it was really nice meeting you [C.name]. I'd like to get to know more about you."
    menu:
        "It was nice meeting you too. Let's hang out sometime.":
            show nitrogen happy with fadeWithText
            N "Absolutely. See ya around."
            $ nitrogen_love += 5
        "See ya.":
            pause 1.0
            show nitrogen sad with fadeWithText
            N "Yup, see ya."
            $ nitrogen_love -= 5

    pause 0.25
    hide nitrogen with moveoutright
    pause 0.25
    show oxygen at center with ease
    pause 0.5

    Nar "Nitrogen exits the classroom leaving you alone with oxygen."

    show oxygen happy with fadeWithText
    O "So hey can I ask you something? I promise it's nothing serious."

    menu:
        "Sure, go ahead":
            O "Are you planning on actually going to the dance?"
            menu:
                "Yeah I guess, it's required.":
                    show oxygen happy with fadeWithText
                    O "That's fair. I was just curious if it's actually your kind of thing. {w}I know the opinions of all the others so I was just curious about yours." 
                "It's not really my thing.":
                    show oxygen neutral
                    O "I can understand where you are coming from but it's sort of important you go. {w}A student at this university without any strong bonds gets left behind."
                    O "Plus you're in the honors class. So think about it."
        "I've got to go, maybe later":
            $ oxygen_love -= 5
            show oxygen sad with fadeWithText
            O "Oh yeah, sure later. It's nothing anyways.{w} Just make sure don't forget to find someone for the dance. Consider this a friendly reminder."
        "It's okay if its serious. You're pretty cool.":
            $ oxygen_love += 5
            show oxygen happy with fadeWithText #fades to neutral at “Make sure”
            O "Wow you're really nice. That's cool."
            show oxygen neutral with fadeWithText
            O "Well, here's the deal. Make sure you don't come alone to the molecular dance. Want to know why?"
            menu: 
                "Sure.":
                    show oxygen neutral with fadeWithText
                    O "Everyone who has ever been in the honors class shows up in a bonded pair. It's tradition."
                    O "It's so important that if you don't have someone with you you're gonna be removed from the honors class and even worse basically socially shunned."
                    O "So for real, make sure you bring someone with you.{w} It's really important."    
                "Uh okay. This is kind of weird.":
                    show oxygen neutral with fadeWithText
                    O "Weird? No not really. If you come alone you are basically saying goodbye to the honors class and your social life here. So for real, don't come alone."

    show oxygen happy with fadeWithText
    O "Well I got to go. Maybe I'll see you around."

    hide oxygen with moveoutright

    Nar "Oxygen leaves the classroom leaving you alone with thoughts."

    Nar "You go through the rest of your day of classes. {w}It's a long day and the workload at this university isn't easy."
    Nar "But you manage to finish everything before finally laying down for some rest in your shared dorm room."

    jump dorm2

label dorm2:
    scene bg dorm with dissolve
    pause 0.5
    show chlorine neutral at left with enter
    Nar "As you crash down onto your bed you see out of the corner of your eye, Chlorine looking at you from his bed."

    menu:
        "What's up?":
            pause 0.1
        "Ignore him.":
            pause 0.1
        "Stop that.":
            pause 0.1
    show chlorine at center with ease
    pause 0.5
    show chlorine happy with fadeWithText

    Cl "So… {w=0.5}those two were definitely checking you out."
    menu:
        "What are you talking about?!":
            pause 0.1
        "Huhh?":
            pause 0.1
        "No, they weren't.":
            pause 0.1

    show chlorine neutral with fadeWithText
    Cl "Don't play stupid. Oxygen and Nitrogen so want to get with you. It's really clear."

    Cl "So which do you think you have better chemistry with? Tell me now or I won't let you sleep."
    
    menu:
        "Uh Oxygen maybe.":
            show chlorine happy with fadeWithText
            Cl "He's nice, but just wait till you get to know him for real. There is a reason I dumped him."
            $current_path = "oxygen"
        "Maybe Nitrogen, she's cool.":
            show chlorine happy with fadeWithText
            Cl "Cool, but she's really closed off. So make sure you be nice to her. She didn't stick with me too long." 
            $current_path = "nitrogen"
        "Shut up! I just got here.":
            show chlorine sad with fadeWithText
            Cl "Okay, now I'm being serious. If my roommate fails to get bring someone to the dance I'm gonna be socially outcasted by proxy so for real if you had to choose who would you choose?"
            menu:
                "Fine, Oxygen I guess":
                    show chlorine happy with fadeWithText
                    Cl "He's nice, but just wait till you get to know him for real. There is a reason I dumped him."
                    $current_path = "oxygen"
                "I think Nitrogen":
                    show chlorine happy with fadeWithText
                    Cl "Cool, but she's really closed off. So make sure you be nice to her. She didn't stick with me too long." 
                    $current_path = "nitrogen"

    show chlorine neutral with fadeWithText
    Cl "Well I'm gonna get some rest now. You can start planning out your arrival to the molecular dance."

    hide chlorine with leave

    Nar "You slowly drift off into sleep as your mind is racing with the absolute craziness of today."
    Nar "What is this school's deal? What have you gotten into? {w} Are some of the questions filling your mind?"
    Nar "But out of them all, you can't help but wonder what will be your chemical romance."

label tuesday_start:
    # Day change here
    scene bg hallway with Dissolve(2.0)
    
    if current_path == "nitrogen":
        jump tuesday_nitrogen
    else:
        jump tuesday_oxygen

label tuesday_oxygen:
    Nar "As you go about your day you pass through the common area of campus.{w} The crowds of students heading to their classes rush by you."
    Nar "Someone bumps into you and you drop your books.{w} As you bend down to pick them up someone stops in the crowd to help you."
    
    show oxygen happy at center with enter

    O "Oh hey, [C.name]. Let me help you with those."

    Nar "Oxygen bends down and helps you pick up your things.{w} As gather all your books into your bag once more you catch Oxygen smiling at you."
    O "So someone told me you were maybe into me."
    menu:
        "Uh wait, it's not what you think.":
            show oxygen Sad with fadeWithText
            O "So you don't like me?"
            menu:
                "Wait that’s not what I mean.":
                    pause 0.1
                "Well yes but not the way Chlorine may have said.":
                    pause 0.1
            show oxygen happy with fadeWithText
            O "I'm just joking around. I know Chlorine can say the most bizarre things. {w}I don't take anything he says to be the truth."
        "Chlorine is such an isotope." :
            show oxygen neutral with fadeWithText
            O "Don't worry about him. He says a lot of stuff.{w} I don't take anything he says as the truth."
    show oxygen happy with fadeWithText
    O "But hey would you maybe want to meet up at the Basketball game tomorrow? {w}I have a good spot high up I usually sit. We can hang out."
    menu:
        "Sure, I loved to.": # + oxygen opinion
            $ oxygen_love += 5
            show oxygen happy with fadeWithText
            O "Awesome! I'll see you then. Tomorrow at 6 pm."

        "I'm actually busy tomorrow so maybe later this week": # - oxygen opinion
            $ oxygen_love -= 5
            show oxygen neutral with fadeWithText
            O "Yeah that's fine. I can swing by your place tomorrow maybe to work something else out."

    show oxygen happy with fadeWithText
    O "Well I have to head to my next class now so I'll see you later."

    pause 0.5
    hide oxygen with moveoutbottom
    pause 0.5

    Nar "Oxygen runs off into one of the campus buildings.{w} He's always in a hurry it seems."
    Nar "You go about the rest of your day finishing your classes and assignments. {w}Not forgetting just how Chlorine talked to Oxygen behind your back." 

    jump tuesday_dorm

label tuesday_nitrogen:
    Nar "Your second day of classes was going smoothly until you accidentally went to the wrong class and are now running to the correct room"
    Nar "As you cross through a crowded hall you accidentally bump into another student. Both of your books go flying."
    M "Ouch!"
    menu:
        "Oh, I’m so sorry!":
            Nar "The other student you ran into rubs her head and looks up at you.{w} As your eyes meet you realize this is Nitrogen from your honors class." 
            Nar "She appears more embarrassed than she is in pain."
        "Ouch! That must have hurt.":
            Nar "The other student looks up to you and glares at you."
            Nar" Her face looks frustrated and as she looks like she's about to say something insulting a wave of realization hits her and you both. {w} This is Nitrogen from your honors class."

    pause 0.5
    show nitrogen sad with moveinbottom
    pause 0.5

    N "Hey I'm sorry about that. I didn't see you and I guess we were both moving pretty fast." 

    Nar "Nitrogen helps you gather your books and as you both tuck everything away she looks back to you." 

    show nitrogen neutral with fadeWithText

    N "So, where are you heading?"

    menu:
        "Oh just to my next class.":
            show nitrogen neutral 
            N "I better not keep you then. But hey would you want to hang out at some point? {w}The campus gardens are pretty open around 6 pm tomorrow."
            menu:
                "Sure, I saw them on my tour of the campus. I'll meet you there tomorrow..":# + Nitrogen opinion
                    pause 0.1
                "Sounds like a plan. See you then.": # + Nitrogen opinion
                    pause 0.1
            $ nitrogen_love += 5
            show nitrogen happy with fadeWithText
            N "Perfect. Well, don't be late."
            N "I don't really care if you are but it's important that I know you aren't just flaking on me. See you then." 

            Nar "Nitrogen heads off down the halls. You are left alone for a moment as you watch her head off."
            Nar "But as quickly as that moment happens just as quickly you remember you are late for class. {w}You dash slightly below the speed of light." 

        "I'm actually already late for my next class. I have to go.": # - nitrogen opinion 
            $ nitrogen_love -= 5
            show nitrogen sad with fadeWithText
            N "Oh of course! I'll see you later then. Good luck."

    hide nitrogen with leave
    Nar "You run off down the hall not willing to be late to your next class."
    Nar "But as you do you can't help but think about Nitrogen for a moment. {w}Maybe you should have stayed and talked to her."

    jump tuesday_dorm


label tuesday_dorm:
    scene bg dorm with Dissolve(1.0)
    Nar "The rest of your day goes by quickly. By the time you arrive at your dorm room to get some rest, you realize that Chlorine isn't home."
    Nar "You think to yourself, that he's probably out with someone."

    Nar "As you lay down and begin to fall asleep, relaxing from the stress of all the work ahead of you. {w}You remember that you still need to find an official date for the Molecular Dance."



label ending:
    return

    
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


