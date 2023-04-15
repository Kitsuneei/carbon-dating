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
transform wiggle(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

# Game variables defined here
define nitrogen_love = 0
define oxygen_love = 0
define current_path = "oxygen"
define date_accept = False
define path_final = "Alone"

# The game starts here.
label start:
    play music "music/dorm.mp3" fadeout 1.0
    window hide Dissolve(boxSpeed)
    scene bg monday with dissolve
    pause 2.0
    scene bg dorm with dissolve
    
    Nar "You've finally arrived. After several weeks of waiting you've received your acceptance letter and have made it to Catalyst University, the most prestigious college in the whole country."
    Nar "Now all you have to do is finish unloading your bags."
    Nar "After locating your dorm you enter the room to find that it's been completely taken over by your roommate. But they are nowhere in sight. You look at your documentation and see that for their name your roommate has opted to go by their last name, Chlorine."
    Nar "It appears that Chlorine has covered the room with posters and collectibles."
    Nar "There are posters for the most popular recent bands like \"Vanilla Isotope\" and \"BORON Tennessine (BTs)\"."
    Nar "There is a shelf with a dozen collectibles from the best shows today like \"Solution or Solvent\" and \"Periodic Love\"."
    Nar "As you get distracted by the dozens of interesting things in this room you hear the dorm room door creak open behind you."
    Nar "A man wearing shades of green walks in through the door, smiling and waving to someone as he steps through the threshold." 
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
            Cl "I'll tell you a story later about this one kid Boron."
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
    play music "music/classroom.mp3" fadeout 1.0
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

    Nar "The whole of the class looks to you. Some faces smile, others glare, and others simply don't care. {w} They give you applause led by the Professor."
    
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
    He "Class time is about over but there is one more thing I want to remind you all of before our next class Thursday."
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
    He "That's all the time we have.{w} I'll see you all Thursday morning for our second class time."

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

    N "Hi welcome to Catalyst University. I'm Nitrogen."

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
        "See ya then.":
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
                    O "Plus you're in the Honors class. So think about it."
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
                    O "Everyone who has ever been in the Honors class shows up in a bonded pair. It's tradition."
                    O "It's so important that if you don't have someone with you you're gonna be removed from the Honors class and even worse basically socially shunned."
                    O "So for real, make sure you bring someone with you.{w} It's really important."    
                "Uh okay. This is kind of weird.":
                    show oxygen neutral with fadeWithText
                    O "Weird? No not really. If you come alone you are basically saying goodbye to the Honors class and your social life here. So for real, don't come alone."

    show oxygen happy with fadeWithText
    O "Well I got to go. Maybe I'll see you around."

    hide oxygen with moveoutright

    Nar "Oxygen leaves the classroom leaving you alone with thoughts."

    Nar "You go through the rest of your day of classes. {w}It's a long day and the workload at this university isn't easy."
    Nar "But you manage to finish everything before finally laying down for some rest in your shared dorm room."

    jump dorm2

label dorm2:
    play music "music/dorm.mp3" fadeout 1.0
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
    Nar "What is this school's deal? What have you gotten into? {w} These are some of the questions filling your mind."
    Nar "But out of them all, you can't help but wonder what will be your chemical romance."

label tuesday_start:
    # Day change here
    play music "music/hallway.mp3" fadeout 1.0
    scene bg tuesday with dissolve
    pause 2.0
    scene bg hallway with dissolve
    
    if current_path == "nitrogen":
        jump tuesday_nitrogen
    else:
        jump tuesday_oxygen

label tuesday_oxygen:
    Nar "As you go about your day you pass through the common area of campus.{w} The crowds of students heading to their classes rush by you."
    Nar "Someone bumps into you and you drop your books.{w} As you bend down to pick them up someone stops in the crowd to help you."
    
    show oxygen happy at center with enter

    O "Oh hey, [C.name]. Let me help you with those."

    Nar "Oxygen bends down and helps you pick up your things.{w} After gathering all your books into your bag once more, you catch Oxygen smiling at you."
    O "So someone told me you were maybe into me."
    menu:
        "Uh wait, it's not what you think.":
            show oxygen sad with fadeWithText
            O "So you don't like me?"
            menu:
                "Wait that's not what I mean.":
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
            $ date_accept = True
            O "Awesome! I'll see you then. Tomorrow at 6 pm."

        "I'm actually busy tomorrow so maybe later this week": # - oxygen opinion
            $ oxygen_love -= 5
            show oxygen neutral with fadeWithText
            $ date_accept = False
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
    play music "music/hallway.mp3" fadeout 1.0
    Nar "Your second day of classes was going smoothly until you accidentally went to the wrong class and are now running to the correct room"
    Nar "As you cross through a crowded hall you accidentally bump into another student. Both of your books go flying."
    M "Ouch!"
    menu:
        "Oh, I'm so sorry!":
            Nar "The other student you ran into rubs her head and looks up at you.{w} As your eyes meet you realize this is Nitrogen from your Honors class." 
            Nar "She appears more embarrassed than she is in pain."
        "Ouch! That must have hurt.":
            Nar "The other student looks up to you and glares at you."
            Nar" Her face looks frustrated and as she looks like she's about to say something insulting a wave of realization hits her and you both. {w} This is Nitrogen from your Honors class."

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
            $ date_accept = True
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
            $ date_accept = False
            N "Oh of course! I'll see you later then. Good luck."

    hide nitrogen with leave
    Nar "You run off down the hall not willing to be late to your next class."
    Nar "But as you do you can't help but think about Nitrogen for a moment. {w}Maybe you should have stayed and talked to her."

    jump tuesday_dorm


label tuesday_dorm:
    play music "music/dorm.mp3" fadeout 1.0
    scene bg dorm with Dissolve(1.0)
    Nar "The rest of your day goes by quickly. By the time you arrive at your dorm room to get some rest, you realize that Chlorine isn't home."
    Nar "You think to yourself, that he's probably out with someone."

    Nar "As you lay down and begin to fall asleep, relaxing from the stress of all the work ahead of you. {w}You remember that you still need to find an official date for the Molecular Dance."

    if date_accept == True:
        if (current_path == "oxygen"):
            jump wednesday_oxygen
        else:
            jump wednesday_nitrogen
    else:
        jump wednesday_skip

label wednesday_oxygen:
    play music "music/oxygen date.mp3" fadeout 1.0
    scene bg wednesday with dissolve
    pause 2.0
    scene bg bleachers with Dissolve(1.0)

    Nar "As you arrive at the Basketball court you see there is a game between your school's team and a visiting school."
    Nar "There are dozens of people watching the game in the bleachers.{w} As you scan the crowd you catch the eyes of Oxygen starting back at you."
    Nar "Oxygen waves you over and you head up the bleachers to meet him. {w}The spot he brought you to is high up and in the back where it's nearly like you two are alone."

    show oxygen happy with fadeWithText

    O "I'm glad you came. I was sort of worried I may have scared you off with my invitation. I know I can be too much sometimes."
    menu:
        "You're fine, it's actually kind of cute.":# + oxygen opinion
            $ oxygen_love += 5
            show oxygen happy with fadeWithText
            O "Dang, I was right before you really are nice."

        "Only sometimes, but I'm glad I'm here.":# - oxygen opinion
            $ oxygen_love -= 5
            show oxygen neutral with fadeWithText
            O "I'm glad you are too."

    Nar "He turns away from you and focuses on the game. {w}You two sit there for a moment simply enjoying each other's company."
    Nar "At one point the crowd cheers and Oxygen stands up to cheer with them."
    show oxygen happy at slightleft with ease
    show oxygen happy at slightright with ease
    show oxygen happy at center with ease
    menu:
        "Cheer with the crowd.":
            Nar "You stand up and cheer with the crowd. Oxygen notices and seems to approve. He sits back down with the rest of the crowd."
        "Don't cheer.":
            Nar "You watch as the crowd erupts with praise.{w} You look to Oxygen and he seems to take note of you not cheering."
            Nar "He doesn't appear displeased but more concerned instead."

    Nar "Oxygen leans over to you."

    show oxygen neutral with fadeWithText
    O "Are you having fun?"
    menu:
        "Absolutely, I'm really glad I came.":# + oxygen opinion
            show oxygen happy with fadeWithText
            $ oxygen_love += 5
            O "I'm glad you did because honestly when you walked into class I knew we would bond well." 

        "Well, It's not really my thing.":# - oxygen opinion
            $ oxygen_love -= 5
            show oxygen sad with fadeWithText
            O "Sorry, I guess I just assumed. Well, it's almost over anyways."
            Nar "Oxygen turns away from you and looks back at the game. You can tell he's a bit upset."
        
    Nar "As the game continues and starts to head to its last few minutes you notice that oxygen catches the eyes of an element in the crowd."
    Nar "He waves down to the other element. You think she's Gold but you can't be sure. You just know Gold is the most popular student on campus."

    show oxygen neutral with fadeWithText
    O "Excuse me for a moment. Business calls."

    pause 0.5
    show oxygen at slightright with ease
    hide oxygen with moveoutleft
    pause 0.5

    Nar "You see Oxygen heads down the bleachers and meets with Gold for a moment."
    Nar "They talk for a minute but it seems like Gold is in a hurry. She opens one of her hands and there is a small bundle of cash."

    Nar "Oxygen grabs the cash and then reaches into a side pocket of his coat and pulls out a small container of something colorless."

    Nar "Gold takes the substance and looks it over. She seems displeased. She talks with Oxygen and for a moment they seem to argue."
    Nar "But the tension quickly fades and she walks away. Oxygen heads back up to your seats."

    pause 0.5
    show oxygen neutral at center with moveinleft
    pause 0.5

    Nar "As he sits down you catch a glimpse of the bundle of money he slips into his pocket."

    menu:
        "What's the money for?":
            show oxygen neutral with fadeWithText
            O "Oh just a side job I have. A way to get some extra cash. Don't worry about it."

        "You don't say anything.":
            Nar "Oxygen sits down settling his things. He looks over to you with a smile and then his focus returns back to the game."

    Nar "About thirty minutes passed and the game wraps up. It seems that your school won and the crowd gives a great round of applause to the players."
    Nar "You and Oxygen both head for the exit."

    Nar "Before you head to your dorm Oxygen stops you for a moment."

    show oxygen happy with fadeWithText
    O "Hey I just wanted to let you know that I really enjoyed tonight."
    O "It was fun, sorry that business got in the way. I appreciate that you didn't flake on me."
    menu:
        "Hey it's okay.":
            show oxygen neutral with fadeWithText
            O "Good, well I guess I'll see you tomorrow."

        "It wouldn't be right for me just to leave.":
            show oxygen neutral with fadeWithText
            O "Yeah I guess you're right. I'll see you tomorrow."
    
    O "Oh, by the way, this is kind of cheesy but it's something I got to say."
    O "I'm attracted to you to the point where I could make a fifth fundamental force. {w}You're really something special [C.name]."

    show oxygen happy with fadeWithText
    O "Sorry that was way too cheesy."
    menu: 
        "Nah it was fine.":
            pause 0.1
        "Yes, but sweet.":
            pause 0.1

    O "I appreciate the support. I'll see you soon."

    Nar "Oxygen heads off to his dorms. You can't help but think about what he just said. {w}Was it too cheesy or was it sweet?"
    Nar "Also, you aren't sure what happened between him in Gold but you can't think of it now. {w}It's time you headed back to your dorm."
    jump thursday_begin


label wednesday_nitrogen:
    play music "music/dorm.mp3" fadeout 1.0
    scene bg wednesday with dissolve
    pause 2.0
    scene bg classroon with dissolve

    Nar "You spend all of your Wednesday classes in a daze as you anticipate your meeting with Nitrogen this evening."
    Nar "There were more than a few instances where you had to snap yourself back to reality during class, and realized that you had missed a large chunk of the lecture."

    Nar "Finally your last class is wrapped up and you exit the building to cross the school grounds at a speed walk so as not to be late."
    Nar "Nitrogen seems like the kind of person that would hit you upside the head for being late."

    play music "music/garden.mp3" fadeout 1.0
    scene bg greenhouse with Dissolve(1)
    Nar "You approach the greenhouse and see the vague shape of someone distorted through the greenhouse glass, but with an unmistakable blue hue."
    menu:
        "Sneak up behind her":# - nitrogen opinion
            $ nitrogen_love -= 5
            Nar "You enter the greenhouse quietly and tiptoe up behind the familiar figure of Nitrogen."
            Nar "As you sneak right up behind her, you grab her shoulder and..."
            C "Boo!"

            show nitrogen sad with moveinbottom
            N "Eek!"

            show nitrogen at slightleft with ease
            show nitrogen at slightright with ease
            show nitrogen at center with ease

            Nar "Nitrogen spins around, fists raised and ready, with a look of terror on her face."
            Nar "The pot that she was holding shatters on the ground, before she realizes that it's you. {w}She lets out a breath and lowers her hands with a sigh."
            N "Oh, it's you, [C.name]."

            Nar "She looks down at the shattered pot, looking really bummed. She quickly shakes it off and looks back up to you."
        "Make your presence known":# + nitrogen opinion
            $ nitrogen_love += 5
            Nar "You make some noise as you enter so as not to startle her, and she turns to smile at you with a pot in her hands."

            show nitrogen happy with fadeWithText
            N "Over here, [C.name]!"

            Nar "She waves you over and you approach curiously, eyeing the pot in her hands."
            Nar "She sets it on the shelf and spritzes it with a spray bottle."
    show nitrogen neutral with fadeWithText
    Nar "Nitrogen hands you a spray bottle and begins misting some of the other plants."

    show nitrogen happy with fadeWithText
    N "I'm glad you came on time, this is the best time of day to be in the greenhouse."
    N "It's not too hot because the sun is starting to set, and most people have gone to the dining hall for dinner."

    show nitrogen neutral with fadeWithText
    N "So..{w=0.5} um..{w=0.5} [C.name], do you have any hobbies?"

    menu:
        "Uh… I'm currently expanding my horizons. Any suggestions?": #+ nitrogen opinion
            $ nitrogen_love += 5
            show nitrogen happy with fadeWithText
            Nar "Nitrogen smiles, but quickly hides it and attempts to look indifferent."

            show nitrogen neutral with fadeWithText
            N "Well… I could use some help with making sure these orchids stay humid, so you could start with putting that spray bottle to use. {w}Maybe you'll enjoy gardening."

            show nitrogen happy with fadeWithText
            Nar "Nitrogen shrugs as if she's indifferent, but when you start misting the orchids enthusiastically, she looks excited to share her hobby with someone."
            Nar "Suddenly, she turns to you in a snappy movement, seeming flustered about something."

            N "Are you copper because I can CU in a relationship with me?"

            Nar "There's a long pause filled with silence. Nitrogen blushes furiously and turns back to the orchids."
            Nar "She begins talking again before you have the chance to respond."


        "Not really, it's kind of just all studying for me.":# - nitrogen opinion   
            show nitrogen sad with fadeWithText
            N "Oh, well… I think it's good to have hobbies. You should really try to find something that you enjoy that isn't school related."
            Nar "She turns her back and goes back to misting some orchids, trying to appear indifferent."

    show nitrogen neutral with fadeWithText
    N "Anyway, um, I have a lot of homework that I should get to. But… {w=0.2} I'm looking forward to seeing you in class tomorrow."

    Nar "She sets down the spray bottle and turns away sheepishly, heading for the exit."
    menu:
        "Watch her leave":
            pause 0.1
        "Yeah, see you!":
            pause 0.1
    Nar "As Nitrogen disappears out of the greenhouse, you set down your own spray bottle and gather your things to leave."
    Nar "As you walk back to your dorm room, your head swims with thoughts about Nitrogen."
    Nar "You wonder if she's the one that you want to ask to the Molecular Dance, and what she would say if you asked her."
    jump thursday_begin

label wednesday_skip:
    play music "music/dorm.mp3" fadeout 1.0
    scene bg wednesday with Dissolve(2.0)
    Nar "Wednesday is uneventful. You go through your classes without issue and finish all your assignments on time."
    Nar "You're all set for Thursday mornings class."
    jump thursday_begin

label thursday_begin:
    play music "music/classroom.mp3" fadeout 1.0
    scene bg thursday with Dissolve(0.5)
    pause 2.0
    scene bg classroon with Dissolve(1.0)
    Nar "As you arrive in class this morning you see everyone finding their seats."
    Nar "You see Chlorine waving you over from where he sat earlier in the week."

    pause 0.25
    show chlorine neutral with enter

    Nar "As you head over he pulls you down into your seat and begins to whisper to you." 

    show chlorine sad with fadeWithText
    Cl "So I heard you blew it. I can't believe I thought you could get a date of your own. I should have kept my Ion you." 
    menu:
        "How did you know?!":
            show chlorine happy with fadeWithText
            Cl "Oh I didn't know but I know now. I noticed how your week was going and you just confirmed my theory."

            show chlorine neutral with fadeWithText
            Cl "But don't worry I'm still in your corner. You just need to repair things."
            Cl "At the end of class when they approach you, make sure you work things out."
            Cl "You need a date for the dance. Don't be a stray atom."

        "What are you talking about? It went well.":
            show chlorine happy with fadeWithText
            Cl "I know, I was just testing you."

            show chlorine neutral with fadeWithText
            Cl "Based on the times you came back to the dorm I had my theories. I'm happy for you."
            Cl "It's hard enough to make new friends on this campus. Not to mention getting a date in time for a dance at the end of the week."

            Cl "They'll probably approach you today after class so make sure you know what to say."
            Cl "You better say yes. You need a date, don't forget."

    hide chlorine with dissolve
    pause 0.25
    show helium neutral at center with enter
    pause 0.25
    

    Nar "Class starts and as usual Professor Helium drags things out for as long as she can."

    if nitrogen_love >= 10:
        pause 0.25
        show helium neutral at right with ease
        pause 0.25
        show nitrogen happy at center with moveinbottom
        pause 0.25

        Nar "At one point in the class you catch Nitrogen staring at you. {w}Your eyes meet and she smiles at you."

        pause 0.25
        hide nitrogen with moveoutbottom
        pause 0.25
        show helium at center with ease
        pause 0.25

    if oxygen_love >= 10:
        pause 0.25
        show helium neutral at right with ease
        pause 0.25
        show oxygen happy at center with moveinbottom
        pause 0.25
        Nar "Near the end of the class you turn to stretch in your seat and catch Oxygen looking at you."
        Nar "He's clearly lost in thought but as your eyes meet he snaps out of it. He smiles at you."

        pause 0.25
        hide oxygen with moveoutbottom
        pause 0.25
        show helium at center with ease
        pause 0.25
    Nar "Professor Helium finishes her lecture. As she does she turns to face the class and becomes more relaxed."

    show helium happy with fadeWithText
    He "So class how is everyone doing? I'm assuming everyone has their dates for tomorrow night."

    Nar "You see as nearly everyone in class nods. It appears they have already found many of their bonds."

    if oxygen_love >= 15:
        pause 0.25
        show helium neutral at right with ease
        pause 0.25
        show oxygen happy at center with moveinbottom
        pause 0.25
        Nar "You catch Oxygen staring at you from the corner of your eye."
        pause 0.25
        hide oxygen with moveoutbottom
        pause 0.25
        pause 0.25

    if nitrogen_love >= 15:
        pause 0.25
        show helium neutral at right with moveinbottom
        pause 0.25
        show nitrogen happy at center with enter
        pause 0.25
        Nar "You see Nitrogen glance at you for a moment." 
        pause 0.25
        hide nitrogen with moveoutbottom
        pause 0.25
        pause 0.25

    pause 0.25
    pause 0.5
    show chlorine neutral at left with enter
    pause 0.25

    show chlorine happy with fadeWithText
    Cl "Oh yeah I definitely got my date Prof. You can trust me."

    show helium happy with fadeWithText
    He "Oh really mister Chlorine? Who's the lucky one?"

    Cl "Oh just a sodium kind of guy. We really pair well."

    He "Good for you. Well, I wish the best of luck to the rest of my students too."
    He "Remember you are all role models for the rest of the university. {w}Catalyst Honors Class Students are meant to stand above the rest."

    hide chlorine with leave
    pause 0.25
    show helium at center with ease
    pause 0.25
    hide helium with moveoutright
    pause 0.25

    Nar "Professor Helium finishes her lesson and heads out of the class with a few other students."
    Nar "As you are lost in thought of what you are going to do about the dance you snap out of it by overhearing an argument between Nitrogen and Oxygen."

    show nitrogen sad at slighterleft with moveinleft
    show oxygen neutral at slighterright with moveinright
    N "Was that Ozone I saw?"

    O "It doesn't concern you."

    N "I know what I saw Gold holding with her last night. Don't think I forgot about your past mistakes."

    show oxygen sad with fadeWithText
    O "Look Nitrogen get out of my business, you don't even care about Ozone. This doesn't concern you"

    show nitrogen sad
    N "Ozone is a drug Oxygen, and I wouldn't care if you didn't keep stealing from the garden for your ingredients."

    Nar "Oxygen rolls his eyes while Nitrogen sighs and rubs her brow. They both turn to look at you, apparently just realizing you heard everything."

    show oxygen neutral
    show nitrogen neutral
    with dissolve

    show oxygen at right
    show nitrogen at left
    with ease

    show chlorine happy at center with enter

    Cl "Well you two really know how to make your business everyone else's problem."

    N "Chlorine you're such an Acid."

    O "She's right."

    Cl "Ah whatever, at least I have a date that's so-dium fine."

    Nar "There's a pause in the conversation allowing you to voice your opinion."
    menu:
        "I think Nitrogen is right about this.":# + Nitrogen opinion
            $ nitrogen_love += 5
        "Oxygen is right it’s none of our business.":# + oxygen opinion
            $ oxygen_love += 5
        "Honestly Chlorine you are kind of an Acid.":# +Nitrogen opinion + Oxygen opinion
            $ oxygen_love += 5
            $ nitrogen_love += 5

    Nar "Nitrogen and Oxygen both hear you out and softly nod. Chlorine, on the other hand, begins to leave."

    show chlorine neutral with fadeWithText
    Cl "Well this was an interesting interaction but I think [C.name] had something to say. I'm out of here. See ya."

    Nar "Chlorine makes his exit with a smile and a wave. He grabs his bag and heads out of the class."

    hide chlorine with moveoutright

    show oxygen at slighterright
    show nitrogen at slighterleft
    with ease

    Nar "Nitrogen and Oxygen both shake off the interaction and turn to you." 

    menu:
        "Approach Nitrogen about the Dance." if nitrogen_love >= 20:
            Nar "You approach Nitrogen. She smiles at you."

            hide oxygen with dissolve
            show nitrogen at center with ease
            N "What's up?"
            C "Would you want to go to the dance with me?"

            show nitrogen happy with fadeWithText
            N "I thought you'd chicken out. Of course."
            Nar "Nitrogen leans in and gives you a hug. You can feel the chemistry. While she does so she whispers in your ear."

            show nitrogen neutral with fadeWithText
            N "If you did chicken out I would have never forgiven you."

            show nitrogen happy with fadeWithText
            N "I'm joking of course. I'll see you tomorrow [C.name]."

            hide nitrogen with moveoutright

            Nar "Nitrogen gives you a wink and heads out. She seems to shine with happiness. Eventually, you leave the classroom too."

            $ path_final = "Nitrogen"

        "Approach Oxygen about the Dance." if oxygen_love >= 20:

            Nar "You approach Oxygen. He relaxes his posture and smiles."

            hide nitrogen with dissolve
            show oxygen at center with ease
            O "So, what do you need?"
            C "Would you want to go to the dance with me?"
            show oxygen happy with fadeWithText
            O "Absolutely. I was a bit worried about yesterday after the way I left things but I'm so happy you still asked."

            Nar "Oxygen leans in and hugs you tightly. He even lifts you up a bit and then sets you down. You can feel the chemistry." 

            show oxygen neutral with fadeWithText
            O "You've really made me so happy I met you [C.name]. I'll see you tomorrow."

            Nar "Oxygen grabs his things and then leaves the classroom with a smile on his face. You eventually leave the room yourself."

            $ path_final = "Oxygen"

        "Hey guys sorry about overhearing everything. But I have to go.":
            Nar "You head for the door. It seems like the pair wants to stop you but instead, they let you go."
            $ path_final = "Alone"

    Nar "You leave the class building and go about your day. The thoughts of what is and what could have been cloud your mind."
    Nar "But as you finish the rest of your classes for the day you eventually head off to your Dorm room."

    play music "music/dorm.mp3" fadeout 1.0

    scene bg dorm with dissolve
    Nar "As you get ready to get some rest for tomorrow Chlorine enters the dorm room shutting the door behind him."

    show chlorine neutral at center with moveinleft

    Cl "No matter what you chose to do I think you chose right. Even if the rest of the school body thinks differently."

    if path_final == "Oxygen":
        Cl "Yeah maybe you can work things out with him. I trust your judgment. I just can stand too much of him."
    elif path_final == "Nitrogen":
        Cl "She's good for you. She wasn't for me, but for you, I think you'll both soar high."
    else:
        Cl "There's always next year my lonely particle."

    Nar "Chlorine falls into his bed and quickly falls asleep. Leaving you alone once more."
    Nar "As you too lay in bed you think about just how tomorrow will go. Hopefully, it won't be a bad reaction."
    jump friday_begin

label friday_begin:
    play music "music/dance.mp3" fadeout 1.0
    scene bg fiday with dissolve
    pause 2.0
    scene bg dance with dissolve

    show helium happy with enter
    He "Welcome everyone to the Molecular Dance! I see you all have your bonds. Make sure to enjoy yourselves and have a wonderful night!" 

    Nar "The crowds gather and the music booms. The student body thunders to life. Everyone seems to be having a great time."
    hide helium with leave

    if path_final == "Oxygen":
        jump oxygen_end
    if path_final == "Nitrogen":
        jump nitrogen_end
    else:
        jump ending

label oxygen_end:
    Nar "You see him cut through the crowd as he approaches you."

    show oxygen happy with moveinleft

    Nar "Oxygen looks really happy and even a little nervous. When he reaches you he puts his arms around you and leans in."

    O "This is my perfect night. You and I will make an intoxicating pair."

    scene co ending with Dissolve(1.0)
    pause(5.0)
    return 


label nitrogen_end:
    Nar "You catch a glimpse of her as she walks towards you."

    show nitrogen happy with moveinleft
    Nar "Nitrogen stands before you and picks up your hands from your waist."

    N "I'm glad we're doing this. Our love will be dangerous."

    scene cyanide ending with Dissolve(1.0)
    pause(5.0)
    return


label ending:
    Nar "Except for you. As you stand alone, with the crowd dancing around you. You catch a glimpse of Oxygen and Nitrogen dancing together."
    Nar "You are the single particle alone in space."

    C "Welp, I should have gone to community college."

    scene lonely ending with Dissolve(1.0)
    pause(5.0)

    return