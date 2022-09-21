#Register music channel
init python:
    renpy.music.register_channel("nature", "ambience", False)
    renpy.music.register_channel("hewan", "hewan", False)
    renpy.music.register_channel("hewan2", "hewan2", False)
    renpy.music.register_channel("hewan3", "hewan3", False)

label phase2:

    play music audio.IPD loop
    scene IPD WORKPLACE with fade

    "It's a bright and sunny day at the Interdimensional Police Department or IPD for short."
    "The sunlight is shining through the windows today."
    "A perfect day to go outside and lay down on a sandy beach with a friend or two but not for Rai Galilei."
    "He's one of the busy officers from IPD."

    "Today is like any of his work days, a lot of new paperworks awaits Rai in his office, which he happily accepts as it is."
    "Waking up and walking to his office like normal. Accompanied by the usual chit-chatter with colleagues."
    "Rai finally reached his office desk. It doesn't look like one at the moment as it is covered by mountains of paperwork. He lets out a big stretch. And it's time for him to do his work."

    "Before sitting down on his desk, he grabs a can of cola and cracks it open."
    "His number one favorite drink to accompany him through all the paperwork of the day."
    "He takes a sip as he sits down on his chair."

    show Rai Default

    Rai "Ah.. another day with my wife, Shigoto-san."
    Rai "Hmm, let's see what I have to do today."

    Rai "Man... It's just the beginning of the day yet someone has already put this much paper here."

    Rai "I can't work properly if my table is full of papers."

    Rai "I need to tidy it up a bit, I think I should put some of the papers in the drawer for the meantime."

    "While Rai was tidying up the papers that were on his desk, one of his Galilean coworkers came by his table."

    show Rai Default at left with easeinleft
    show Galilean_1 Default at right with easeinright

    Galilean_1 "Good morning! Sorry to disturb you so early in the morning."
    Rai "Oh! Good morning!"
    Rai "It's okay. Is there something that I could help you with?"
    Galilean_1 "Ah yes, I'm just here to remind you about the meeting that we will be holding in a bit."
    Galilean_1 "Please don't forget to bring the necessary files for it!"
    Rai "Thank you for the reminder. I'll get it ready."
    Galilean_1 "Okay then, I shall excuse myself now. Have a good day!"

    hide Rai Default with dissolve
    hide Galilean_1 Default with dissolve

    "As Rai gets back on his chair, he sees a post-it-note reminder on his PC screen to help fix the CCTV."
    "He can help fix the CCTV first, or attend the meeting first, or he can just ignore all of that and tidy up the files in his drawers."

    "Which one will he do?"
    menu:
        "Tidy File":
            jump phase2_scene1_intro

        "Fix CCTV":
            jump phase2_scene2_intro

        "Attend Meeting":
            jump phase2_scene3_intro

    label phase2_scene1_intro:
        stop music fadeout 2.0
        play music audio.IPD loop
        scene IPD WORKPLACE with fade

        "Rai picks up the papers on his desk and opens his drawer. "

        show Rai Surprised

        Rai "Wait, what...?"

        "It was surprisingly tidy."
        "There are only a few cases that will make Rai have the intention to tidy up his work drawer. The first one is if it was untidy."
        "And the second one is if there were several important papers that seemed to look stuck or tucked between a pile of folders in his work drawer."
        "If that was the case then he would have no choice but to look for it fearing that it would get buried."
        "What was miraculous and magical about it is that even though he was prone to be forgetful, it was as neat as if he had just recently tidied it."

        Rai "(When did I... tidy it up? Kinda forgot really.)"

        "What's going on today? Is the Rai Galilei starting to experience senility or fatigue from work so much that his mind is forced to forget the activities that he did yesterday or maybe even more recent than that?"
        "Who knows."
        "But for Rai this seems like a plus for him since it's already clean. He can just put the papers that's currently in his hands easily."

        show Rai Default
        Rai "(Maybe it's one of my coworkers. Oh well, time to get back to Shigoto-san.)"

        hide Rai Default with dissolve
        scene black with dissolve

    menu:
        "Fix CCTV":
            jump phase2_scene2_intro

        "Attend Meeting":
            jump phase2_scene3_intro

    label phase2_scene2_intro:
        stop music fadeout 2.0
        play music audio.IPD loop
        scene IPD WORKPLACE with fade

        show Rai Default

        "As Rai was about to go to the CCTV Room, when he heard a knock"
        play sound audio.knock

        show Galilean_2 Default at right with easeinright

        Galilean_2 "Uhh sir? Forgive me for the intrusion, but I'm here to give you this. It's from the CCTV Operator Guy. He says to give it to you."
        Rai "Oh, okay. Just put it on the table, thank you."
        Galilean_2 "Then, I'll excuse myself."

        hide Galilean_2 Default with dissolve

        "After they left, Rai read the paper."
        "'Need help in the CCTV Room -Artemisia'"

        Rai "My god, I thought it's a prank. Damn you Artemisia."

        "Rai laughs as he folds the paper neatly and walks towards the CCTV Room."

        play sound audio.footsteps
        scene black with fade

        stop music fadeout 2.0
        play music audio.cctv_room loop

        scene CCTV with fade

        show Artemisia Default
        Artemisia "Welcome sir, sorry to summon you with a piece of paper."

        show Rai Happy at right with easeinright
        Rai "Ah, you mean this?"

        "Rai shows the paper that has already been folded into a shuriken-shaped. He throws the shuriken across the room, making it fly and it returns neatly into his hand."

        Artemisia "Ohmagah, Milord... Ahem- I mean. Such a talent to neatly fold an origami and to make it fly like that."
        Rai "Oh don't flatter me, also this... origami thing you said? I learned it from the Youtube video you gave during my expedition in the Far East Dimension."

        show Rai Serious
        Rai "Anyway, what seems to be the problem regarding the CCTV?"
        Artemisia "Right. As I said from the message, there seems to be a problem with some of the CCTVs in certain spots. We've been dealing with some sort of signal lost sometimes"

        "Artemisia shows a monitor with IPD camera layout."

        show Rai Thinking
        Rai "Hmm, the spots are odd. Just around the jail corridors."
        Artemisia "What do you mean sir?"

        show Rai Serious
        Rai "CCTVs placements that are broken are too odd, as if it was done on purpose to create a blind spot. Maybe it's just me though."
        Artemisia "I see. How observant of you sir."

        show Rai Excited
        Rai "Aww hehe, I've been working here for so long that I feel like IPD is an extension of my body. So, where do I start?"
        Artemisia "Yes sir. So--"

        "Before Artemisia could finish their sentence, someone came running into the room."
        play sound audio.footsteps

        show Artemisia Default at left with easeinright
        show Rai Default at center with easeinright

        show Galilean_2 Default at right with easeinright
        Galilean_2 "Sorry for the intrusion sir, but there's an emergency meeting!"
        Artemisia "What happened?"
        Galilean_2 "We caught an inmate that tried to break out of  jail. We believe that someone outside of our premises tried to help him, but he wouldn't open his mouth."
        Rai "Sorry Artemisia. It's an emergency. I'll see you soon."
        Artemisia "Roger sir. Good luck."

        scene black with fade

        jump phase2_scene3_intro

    label phase2_scene3_intro:
        stop music fadeout 2.0
        play music audio.meeting_room loop
        scene Meeting Room with fade
        show Rai Serious

        Rai "Felix Lynx,huh?"

        "Rai said to himself as he flipped over to the next paper about the inmate."

        Rai "Crime Record: Illegal Dimension Hopper, 1st Degree Interdimensional Mass Murder."
        Rai "..Of fishes in other dimensions. Fitting for a cat."

        "As he examines and searches the database for the inmate, his background, family connection, relation to other criminals. Something immediately clicks."

        show Rai Surprised
        Rai "But really, why does he seem familiar... Ah right, this kusogaki."

        show Rai Annoyed
        Rai "He's the one that ate the fish that I just bought during my trip in the Quantal World. That glutton!"

        "Skimming the profile once more, he makes sure to not let this case miss again."

        Rai "So, not getting tired of getting caught again?"

        "Rai asked his colleagues to leave them alone and shut the door, making him and the Cat Guy have a proper talk."

        show Felix Default at right with easeinright
        Felix "Speak for yourself, yellow bratty. I won't spill much."
        Rai "Well I won't ask much. But again, trying to catch some fish"
        Felix "That again? HAHAHAHAHA, YELLOW SHORTIE, guess you drank too much cola. I will repeat and speak for it again. It is because I can."

        "Rai's emotion set bar almost snapped from the nickname he just got."

        Artemisia "Sir Rai, we need help. Something weird is happening."

        show Rai Surprised
        Rai "I'm in the middle of something. Show me through the monitor.."

        "The small TV at the corner of the room suddenly flashed with a bright light then a static video showed. Not long after that, it's back to normal and shows some bent CCTV cameras."

        show Felix Annoyed
        Felix "Damn, that looks bad."

        show Felix Serious
        Felix "Must be those two stupi–"

        show Rai Surprised
        Rai "..What did you just say?"

        show Felix Annoyed
        Felix "No. Nothing"

        show Rai Happy
        Rai "(Ah...)"
        Rai "(I see!)"
        Felix "What are you talking about man?! Get away from me!"

        show Rai Excited
        Rai "Well thanks to you, I know there is someone who is trying to mess up the surveillance just now. I don't need you anymore..."

        show Rai Default
        Rai "Contacting IPD, Team Galileian, Team Artemisia, escort this inmate back to his jail. I'm done with him. Retrieve the Inmates Collar from him and send me the data after jailing him. Moving to the CCTV room ASAP."
        Artemisia "Aye aye Sir."
        Rai "Now checking the cameras."

        "Rai sees the weirdly 'bent' CCTV camera. He runs towards the main room to consult the Galileian officer there."

        show Rai Surprised
        Rai "I got the report that our CCTV is weirdly shaped. Fast Report, ASAP."
        Galilean_2 "Yes sir. As you can see, our signal was disrupted just before the camera bent, and now it seems like it was crushed by something. While we're here, this is the record from the CCTV before it was 'bent'."

        "Rai checks the camera and notices the way the camera 'bent'."

        show Rai Surprised
        Rai "THERE!"

        show Rai Serious
        Rai "For some millisecond, there's a long, flexible and a very fast moving object that hit the cameras"
        Rai "Did someone managed to breach into IPD?!"
        Galilean_2 "Err, as far as i know, it's just the janitor that passed by those corridors"

        show Rai Serious
        Rai "Okay then, give me the copy to this stick drive. I might need it for the latest investigation."
        Galilean_2 "Okay sir"

        "As he passes him the stick drive, Rai is still wondering who the other culprit is."
        "After a minute passed."

        Galilean_2 "Here's the data that you need sir."

        "One finished in no time.  His communicator rings."

        Artemisia "Artemisia to Galilei."

        show Rai Serious
        Rai "Galilei here."
        Artemisia "We just extracted the data for the inmate you asked, where should we send it?"
        Rai "Oh, it's already extracted? Send it to the database."
        Artemisia "Understood sir. We will process the data then. Artemisia out."

        "Rai then walked toward his room to continue his search and to deduce the identity of the cat's accomplice."
        "Watching the latest sound recording of the jailbreak from Felix's collar, Rai learns the inmate's behavior."
        "He slowly crafts his theories and analyzes the hypothesis about how he managed to attempt a jailbreak."
        "During the middle of the video, Rai suddenly pauses the record and plays it backwards."

        show Rai Thinking
        Rai "Wait..."

        "The inmate seems to be mumbling something."
        "He continued to learn about the inmate for this case."

        Rai "Hmm.. For now this will be the only information that I have..."

        "He examines and tries to make out something from the mumbling."

        Rai "Farmland?"
        Rai "He said something like going to a place called Farmland?"

        show Rai Serious
        Rai "All is connected..."

        "A fiery ambition flickers in his eyes, a flame that never goes down as long as the criminals are roaming around."
        "Rai runs as fast as he can towards his office to pack his things and head towards Farmland Dimension."

        "Which criminal will he catch?"

    menu:
        "Criminal #1":
            jump route2

        "Criminal #2":
            jump route3

    label route2:
        label scene1:
            stop music fadeout 2.0
            play music audio.farm loop
            scene Farm with fade
            play nature audio.wind loop
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep

            show Rai Default
            "A place dominated by a combination of green and brown. Cool air blows all over the place. Sounds from nature—be it the sounds of the animals or the rustle of leaves—fill the ears."
            "A boy—or a man?—stands in the middle of a meadow."
            "He looks around carefully. Researching every corner he can reach calmly..."
            "Until someone comes near him. He greets the boy."

            play sound audio.footsteps_grass
            show Farmer Default at left with easeinleft
            Farmer "Hello, boy!"

            "The boy turns slowly. He smiles politely."

            show Rai Happy
            Rai "Hello, Sir!"
            Farmer "What are you doing here, young boy?"

            show Rai Surprised
            Rai "Uh-uh, for a job!"

            play sound audio.ting

            Farmer "Oh, you're the new kid who's going to work here, aren't you?"

            show Rai Default
            Rai "(But I am not kid tho...)"
            Farmer "Welcome! Thank you for coming all the way here."

            show Rai Happy
            Rai "No worries!"

            show Rai Default
            Rai "(It's for my mission, too.)"
            Farmer "Please prepare yourself and come to see me again."

            show Rai Happy
            Rai "Okay!"

            play sound audio.footsteps_grass
            hide Rai Default with dissolve

            "Rai turns around and leaves the farmer behind."
            "He looks at his surroundings, making sure of the situation according to the information he got in the base."
            "He recalls that report."

            Rai Serious "IPD is not a place that would commit such a mistake."
            Rai Serious "Looking peaceful as it is, there's still must be something."

            "Rai signs and shrugs his shoulders."
            "He knows that not much can be done with the lack of information."
            "That's why he's here, anyway. It won't walk on by itself."

            Rai Excited "Let's get ready!"

            "After Rai prepares himself, he returns to meet the farmer at the same location."

            play sound audio.footsteps_grass
            show FRai Default with dissolve

            Farmer "Are you ready, young man?"
            FRai "Ready anytime, Sir!"

        label phase2_scene1_1:
            Farmer "A fiery spirit, apparently."
            Farmer "Okay. There's some work you need to do."
            Farmer "What kind of work are you going to do, huh?"

        menu:
            "Something simple, maybe...?":
                jump scene1_1_a

            "Whatever is needed now, Sir.":
                jump scene1_1_b

        label scene1_1_a:
            Farmer "Simple, huh?"
            Farmer "You are the type who wants to do the easiest, huh? Even though you're still young, you still have a lot of energy, you know."

            "Rai just laughs awkwardly."

            jump phase2_scene1_2

        label scene1_1_b:
            Farmer "Hahaha!"
            Farmer "Such a determined person! Good to hear."

            show FRai Default
            FRai "Glad to be helped."

            jump phase2_scene1_2

        label phase2_scene1_2:
            Farmer "Great. Now we can move on to your first job."
            Farmer "Here, take this."

            show Map at truecenter with dissolve

            "The Farmer gives small old paper. It was a small map containing the places on the farm."
            "Rai flipped the paper."
            "On the other side, there is a list."

            Farmer "Go to the shed."

            "He pointed to the paper given to Rai."

            Farmer "You can check the list of jobs listed there."
            Farmer "Good luck!"
            hide Map with dissolve

            "He smiles."
            "Rai bows to The Farmer and leaves immediately."

            play sound audio.footsteps_grass
            hide FRai Default with dissolve
            hide Farmer Default with moveoutleft

            "Rai checks the paper again. He tries to remember all the jobs."

            FRai Thinking "(Shed, huh? There must be a lot of stuff in there.)"
            FRai Serious "(There must be a lot... {i}something.{/i})"

            "As this one policeman had already pointed out, there were indeed a lot of things in that place."
            "A huge amount."

        label scene2:
            stop music fadeout 2.0
            stop nature
            stop hewan
            stop hewan2
            stop hewan3
            play music audio.shed loop
            scene Shed with fade
            play sound audio.door_open

            show FRai Default at left with easeinleft
            "Rai finally arrives at the shed and looks around. Nothing much."
            "Too much going on here."

            show FRai Surprised
            FRai "Whoa—look at here."

            show FRai Nervous
            FRai "Very {i}neat.{/i} Ha ha."

            play sound audio.paper
            "Rai checks upon the jobs list. One of them is arranging the farming equipment."
            "Not a difficult job, actually. It just needs patience and energy."

            play sound audio.barang_klutuk_klutuk
            "Rai starts picking stuff up near his feet."
            "There's no point in thinking all the time doing nothing."

            show FRai Default
            FRai "(Just get over it)"
            FRai "Well, where should I store all this?"

            "Rai looks to his right."
            "He sees a wooden shelf glued to the wall."

            play sound audio.ting

            FRai "Maybe it's there, yes."

            play sound audio.footsteps
            show FRai Default at right with easeinright

            "Rai approached the shelf while carrying the items."
            "He put the things on the shelf."

            play sound audio.barang_ditaruh
            FRai "Let's see. This one over here, then this one over here..."

            "Rai began to arrange the items."
            "He pushes the items that were previously on the shelf to the edge of the shelf."

        label scene2_2:
            show FRai Excited
            "Rai pick up the scattered items."
            "He arranges the items by function in each place on the farm as he had seen the entire contents of the map."
            "Maybe that way, it can help farmers take things as needed."

            play sound audio.barang_ditaruh
            "After fully filling the shelf on the right, he moved to the shelf on the left."

            play sound audio.footsteps
            show FRai Default at left with easeinleft
            
            "He picks up another item that was on the floor and carries it over to the shelf. He arranges the same as the previous shelf."

            show FRai Default
            FRai "This thing here, and this thing there..."

            play sound audio.barang_kepentok
            "Again, something caught his attention."
            "Something hit the back of Rai's hand."
            "It was a small object shaped like a ring."
            "Rai takes it."

            show FRai Thinking
            FRai "Hmm? Is this one of the farm's belongings? I don't think so."

            "He wondered why on his first day such a strange thing had happened."
            "Yeah, it's actually normal considering he's also been on a mission and sometimes unusual things happened even to ordinary people."
            "Like... Casually eating sand for example."
            "Back to topic."
            "Rai checks the thing."

            show Ring with dissolve

            "It is a circle with a hole in the middle."
            "There are some sort of four patterns or lines on the edges."
            "It doesn't have volumes, so calling it a ring would be strange. It looks more like a coin with a hole in the middle of it."

            hide Ring with dissolve

            FRai "What part of this is required in the farm? Hmm...."

            "Rai thinks aloud and remembers things that are roughly on the farm."


            show FRai Annoyed
            FRai "There's no use. I can't remember."

        label scene2_3:
            "Rai looks at the object carefully."

            show FRai Thinking
            FRai "What should I do?"

        menu:
            "Check the shed.":
                jump scene2_3_a

            "Keep it.":
                jump scene2_4

        label scene2_3_a:
            show FRai Serious
            FRai "There might be something that fits this thing. I have to find it."

            "Rai searches in the shed."
            "He checks the items there one by one, with nothing left behind. Search it from left to right, bottom to top."

            show FRai Default at right with easeinright
            show FRai Default at left with easeinleft

            "He even goes up to the pile of wooden boxes there."
            with vpunch

            play sound audio.box_falling
            "And of course, falls {i}gracefully.{/i}"

            show FRai Nervous
            FRai "Aeugh...."

            show FRai Default
            FRai "At least I'm still alive..."

            "Rai is speechless. He knows it was his fault."

            show FRai Serious
            FRai "(I shouldn't be in a hurry. There's still time.)"

            "Rai gets up and brushes the dust off his clothes."

            show FRai Happy
            FRai "Whatever happens, happen!"

            jump scene2_4

        label scene2_4:
            show Ring with dissolve
            "Rai sees the object in his hand."

            show FRai Serious
            FRai "I'd better save this for now."

            "Rai keeps it in his pocket."
            hide Ring with dissolve
            "Rai piles back the scattered boxes that he had previously stepped on."

            show FRai Default
            FRai "Surely no one noticed. {b}Definitely.{/b}"

            "Rai looks around."
            "Everything looks better than before. Farm items are neatly arranged."

            FRai "One job done."

            show FRai Happy
            FRai "Now onto the next job!"

            "Rai rechecks the list of jobs he held. He marks the work as completed."
            "He looks at the sentence listed in the next assignment."

            show FRai Thinking
            FRai "Complete the inventory, huh?"
            FRai "I've already checked the items that I think need to be replaced anyway."

            "Rai writes a list of all the items to be purchased. He also rechecks all the items as needed."
            "After all is done, he stares at the list."

            show FRai Happy
            FRai "I think it's time to see the farmer."
            FRai "Even if I have money, it seems strange to go shopping without asking."

            "Rai pockets his notepad."

            show FRai Excited
            FRai "Okay, let's gooo!!"

        label scene2_5:
            stop music fadeout 2.0
            play music audio.farm loop
            scene Farm with fade
            play nature audio.wind loop
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep

            "Rai leaves the shed and goes to meet the farmer."

            show Farmer Default at right with dissolve

            "Not long after, he sees the farmer from a distance. The Farmer is in the middle of something."

            show FRai Default at left with easeinleft
            FRai "Hey, sir!"

            "The farmer stops his activity. He looks up and smiles."

            Farmer "Are you done?"

            "Rai approaches the farmer. He shows the paper that the farmer had given him earlier."

            show FRai Excited
            FRai "Already for the first part!"
            Farmer "Good work."

            "He patted Rai's shoulder."

            Farmer "Now which one do you want to do?"

            show FRai Happy
            FRai "I want to go shopping for equipment first. There are a few things to buy as there are items that don't look like they can be used anymore."
            Farmer "I see. Wait a sec..."

            "The farmer reaches for his trouser pocket. He takes some money out."

            Farmer "Here's the money."
            Farmer "Make sure to buy what you need. If it's not enough, just come back and buy some more, okay?"

            show FRai Excited
            FRai "Okaayy!"
            FRai "I'll be right back."
            Farmer "Be careful, okay. Bring it in a little bit."

            show FRai Happy
            FRai "Yes, sir!"

            play sound audio.footsteps_grass
            hide FRai Default with dissolve
            hide Farmer Default with dissolve

            "Rai waves to the farmer as he leaves. Rai puts the money and the shopping list into the bag."
            "Once he finishes organizing, he looks back at the map and heads straight for the village."

        label scene3:
            stop music fadeout 2.0
            stop hewan
            stop hewan2
            stop hewan3
            stop nature
            play music audio.village loop
            scene Village with fade
            play nature audio.people_chattering_loop loop

            show FRai Default
            "Finally Rai arrives at the village."
            "He sees the hustle and bustle of the village people who were busy passing here and there to get to their destination."
            "Rai tries to avoid the crowds by walking on the side of the road. He leans against the wall to find a gap in the busy street."

            show FRai Nervous
            FRai "(Maybe this isn't the right time.)"

            "Rai struggles through those people."
            "It's understandable that a place like this is indeed packed with crowds because it is close to the marketplace."
            "He makes it through the crowded place after some time."

            FRai "Finally... I'm out..."

            "Rai pants after struggling through all the obstacles that exist."
            "Okay, that's an exaggeration."
            "In short, he returns to his consciousness to go to his destination, the market."
            "As said before, this place is indeed full of people."

            "Rai bumbles with someone."
            with vpunch
            play sound audio.bump

            show Villager Default with easeinright
            show FRai Default at left with easeinleft

            Villager "Hey! Walk with your eyes open, Kid. Be careful."

            show FRai Surprised
            FRai "Uh oh- I'm sorry!"
            Villager "Oh? Are you a newcomer?"

            "Rai who previously looked down, meets the person's eyes."
            "Looks like she's a villager here."

            show FRai Nervous
            FRai "...right, I'm new here."
            Villager "Ah..."
            Villager "By the way, what is a young fellow like you doing here?"

            show FRai Default
            FRai "Oh, about that..."

            "Rai says that he needs to buy farm equipment. Therefore, he had to go to the market."

            Villager "Market, huh? You're going in the right direction."

            "Of course, he brings a map too. Though he won't say that."

            Villager "Usually the farmer will go to the market. Is he busy?"

            show FRai Happy
            FRai "I think so. So I want to help."
            Villager "Why?"

            show FRai Default
            FRai "I'm an intern there."
            Villager "Aaah~ That's why you did it huh. It's part of your job."

            "Rai nods in agreement."

            Villager "Then, since I'm going there too, how about we go together?"


            show FRai Happy
            FRai "Yeah, sure!"

            Seller "Hey!!"
            with vpunch

            show FRai Surprised
            FRai "Waaahhh!!"

            show Villager Default at right with easeinright
            show FRai Default at center with easeinright

            "Someone shouted right behind Rai."

            show FruitsVeggies Seller at left with dissolve

            Seller "Hahaha. Are you surprised?"
            Seller "I'm sorry."

            "The person who had just arrived was carrying some food in his hand. It looks like fruit and vegetables."

            Seller "Oh? You want to go to the market?"
            Villager "Yes, as usual."
            Seller "Then let's go together!"
            Villager "There's some groceries I want to buy from you too."
            Seller "You're lucky. I brought some fresh one."
            Villager "That's good."
            Seller "Yes, yes. Let's move!"
            Villager "Let's take this child along."
            Seller "Oh? New kid?"

            "For some reason, they seemed to forget Rai's existence for a moment."
            "Even though it's actually a good thing because it means Rai can blend in with the people well."

            show FRai Excited
            FRai "Hello, my name is Rai, I'm new here!"
            Seller "Welcome, Boy!"

            show FRai Happy
            FRai "Thank you."

            "They shake hands."

            Villager "Anyway, let's go to the market."

            "They walk together towards the market."
            "The villager and seller tell stories about the village and the people who live here. They also tell him about some places around it."

            stop music fadeout 2.0
            stop nature
            play music audio.market loop
            scene Market with fade

            "After walking quite a distance, they arrived at the place where the seller will be selling his stuff."

            show Villager Default at right with easeinleft
            show FRai Default at center with easeinleft
            show FruitsVeggies Seller at left with easeinleft

            Seller "Then I'll prepare first, okay?"

            show FRai Happy
            FRai "Let me help you!"

            "Like a good kid he is, Rai helps the salesman line up his wares."
            "He lined up each fruit and vegetable and grouped them."

            Seller "By the way, where's {i}the kid{/i}?"
            Villager "Come to think of it, that's true. Where's {i}the kid{/i}?"

            show FRai Thinking
            FRai "Other kid?"

            "Rai turns to them. He was interested."

            Villager "Yes, there is also a young kid besides you here."

            "For some reason, it felt too sudden to mention someone."
            "However, this could be a clue to his mission."

            Seller "She used to shop at my place. Did she move?"
            Villager "That's right. I haven't seen her in a long time."
            Villager "Usually she asks for items that have just arrived in the village."

        label scene3_1:
            "Looks like someone is missing in this village. Moreover, she's a kid."

        menu:
            "Isn't somebody going to look for her?":
                jump scene3_1_a

            "Hopefully she can be found.":
                jump scene3_1_b

        label scene3_1_a:
            Seller "I haven't seen anyone coming for her, I don't think she has any family or relatives here."
            Villager "Yeah, maybe that's why."

            jump scene3_2

        label scene3_1_b:
            Villager "That's right. I hope she will be found soon."

            jump scene3_2

        label scene3_2:
            Seller "We've actually been looking for her around the village."
            Seller "It might be possible though that she already met her family who are outside the village."
            Villager "Yes, who doesn't treasure such a lovely child like her."
            Seller "She looks very cheerful, doesn't she?"
            Villager "Though she's a little weird, haha."

            "Rai raises an eyebrow."

            show FRai Thinking
            FRai "What do you mean by 'weird'?"
            Seller "She... she tried.. a way too hard to blend in, you know."
            Seller "She doesn't look like most people, but she always insists that she's the same as everyone else even though no one mentioned that she's not."
            Villager "She doesn't have to do that though. We'll definitely respond to her like everyone else."
            Seller "Yeah, she's too much."
            Seller "But that makes her cute."

            "Personality, demeanor, appearance."
            "Rai tries to process all the information he got. As if trying to connect the dots, he tries to arrange them in his head."
            "Maybe he should write it down after he went home from the market."

            Seller "So, boy. What do you want to buy?"

            "Rai immediately takes out his shopping list."

            show FRai Happy
            FRai "Oh! I want to buy this and this. Then..."

            "Rai points and reads the list listed. He buys quite a lot."
            "After putting all the groceries in a plastic bag, Rai pays the seller some money."

            Seller "Thank you."
            Seller "Don't forget to stop by again."
            Villager "If there's anything you want to ask, just come over. We'll try to help too."

            Rai "I'm happy to ask."

            show FRai Excited
            FRai "Thank you for helping me."
            FRai "Also for giving me some information."

            "After saying goodbye, Rai heads to the next place."

            play sound audio.footsteps
            hide FRai Default with dissolve

            "He goes to a place where people were selling farm equipment. He walks deeper into the market."

        label scene4:
            scene Market with fade
            stop nature
            play nature audio.people_chattering_loop loop

            "The noise of the crowd can be heard everywhere. He looks left and right to make sure he didn't go past where he planned to go."
            "Until finally, he hears a voice that caught his attention."

            show Merchant Default at right with dissolve

            "It is the merchant."

            show FRai Default at center with easeinleft

            "Rai approaches the merchant. The person noticed him and immediately greets him."

            Merchant "Hello, boy."
            Merchant "Is there anything that you need?"

            show FRai Thinking
            FRai "Hello, uhmm.. {i}Sir{/i}...?"

            "Rai doubts about how to address this person. He guessed from this person's stature that he was a man. In addition, his voice is quite heavy."

            show FRai Nervous
            FRai "Uhm, I'm here looking for stuff."

            "Rai takes out his shopping list."

            show FRai Default
            FRai "This."
            Merchant "Can't you just read it straight away?"

            "Rai, who had wanted to give a list, immediately pulls it back."

            show FRai Nervous
            FRai "It's not like that. Maybe you'd like to check it out in person."
            Merchant "Say it."
            FRai "Uh oh..."

            "The man immediately waved his hand and sighed."

            Merchant "Don't be so nervous."
            Merchant "I just... want you to mention the items you're looking for while I'm looking for them."

            "Rai nods."

            show FRai Default
            FRai "I need a shovel and a hoe."

            "The merchant began to move to find the items."

            Merchant "Then?"

            "Merchant approaches Rai while carrying the previously requested item."
            "Rai looks at his shopping list again."

            FRai "A few nails and screws..."

            "The merchant goes back to look for the requested item."

            Merchant "What else?"

        label scene4_1:
            show FRai Default
            FRai "And...."

        menu:
            "I'm not sure you have one but...":
                jump scene4_2

            "This stuff.":
                jump scene4_1_a

        label scene4_1_a:

            Merchant "Didn't I told you to name the stuff right away?!"

            show FRai Surprised
            FRai "A..."

            "Rai was surprised by the merchant's response."

            Merchant "Go. I don't have time"

            show FRai Nervous
            FRai "W-wait. I need---"

            play sound audio.desk_slam
            Merchant "I SAID GO!"

            "Feeling unable to fight any further, Rai decides to go home with the items he already has in hand."
            "Before leaving, of course Rai left some money to pay for the goods."

            show FRai Sad
            FRai "...Thank you."

            "Rai returns to the farm."
            "He knew it might be too hasty to ask directly. But that doesn't mean he'll just give up."
            "Tomorrow he will return to the merchant. After all, the items he needed were lacking."
            "Well, we'll see tomorrow."

            jump scene4

        label scene4_2:
            Merchant "What? Say it."

            show FRai Nervous
            FRai "Aeugh... still I'm not sure...."

            "The merchant turns around and puts his hands on his hips."

            Merchant "I have it all. Whatever you're looking for."

            show FRai Surprised
            FRai "Hm? Anything?"

            "The merchant nods."

            show Ring with dissolve

            show FRai Happy
            FRai "Then do you have anything similar to a ring like this?"

            "Even though it was only a glance, the merchant looked surprised when he saw the object in Rai's hand."

            show FRai Serious
            FRai "(Aha. Gotcha.)"
            Merchant "I don't know."
            hide Ring with dissolve

            show FRai Sad
            FRai "But you said you have everything..."

            "The merchant looked restless."

            FRai "I was just wondering if you know what this thing is."

            show FRai Happy
            FRai "But if you don't know, then fine. That means you don't {i}own it all{/i}."

            "For some reason, the merchant's pride was scratched."

            Merchant "...Saw."

            show FRai Thinking
            FRai "Hm?"

            "The merchant brings the nails and screws that Rai had ordered earlier."

            Merchant "I saw it before."
            FRai "Only that?"

            "Rai observes the merchant's movements who responded silently."

            Merchant "Maybe it belongs to that {i}kid{/i}."
            FRai "(Again?)"
            FRai "Who exactly is this {i}kid{/i}?"

            "Rai had heard about this child several times today."
            "Even so, Rai doesn't fully have an idea about this child. It could be that this child is related to the mission because it sounds important to the people here."

            Merchant "Instead of 'who', maybe 'what' to be exact."

            show FRai Surprised
            FRai "What do you mean?"
            Merchant "I know you get what I meant."

            show FRai Nervous
            FRai "Ahaha..."

            "Rai shrugs his shoulders."

            show FRai Default
            FRai "Hmmm. What else can we dig here??"

            show FRai Thinking
            FRai "So can you explain about this kid?"
            Merchant "I can't really tell you."

            show FRai Annoyed
            FRai "Again?"
            Merchant "This time I mean it. She's just one of my customers."

            show FRai Thinking
            FRai "Customer?"
            Merchant "Yes."
            Merchant "She came to see me a few times."

            show FRai Default
            FRai "What for?"
            Merchant "What do you think she was doing?"

            show FRai Annoyed
            FRai "(This guy really....)"
            Merchant "If you want to find out what this kid is doing, I can't tell-- whether I know that or not."
            Merchant "Customer's privacy policy, you know?"

            "Rai understands this, although usually in missions there is no such thing as 'local policy'."

        label scene4_3:
            show Tempered Glass at truecenter with dissolve
            Merchant "But if you're still stubborn, maybe this can still help."

            "The merchant gives a clear rectangular object. The thickness is not too thick but not as thin as paper."

            show FRai Thinking
            FRai "What is she doing with that thing?"
            Merchant "She said she wanted to get this fixed but I don't know how."

            "Rai accepts it."
            "Upon closer inspection, there were indeed cracks and scratches on the surface."
            hide Tempered Glass with dissolve

            Merchant "I don't even know the material. So I was planning to give it back when she comes back."
            Merchant "But look? We can't even see a strand of her hair."

            show FRai Sad
            FRai "Oh, I see..."

            "Suddenly there is silence."

            show FRai Happy
            FRai "Then, I'll take this clear thing and buy the items on the list."
            Merchant "Just name the stuff."
            FRai "Okay~"

            "Rai fills his bag with the items he had bought. He also gets additional luggage in the form of a medium-sized box containing equipment."
            "After packing everything, Rai pays for them."
            "Rai says goodbye and leaves the place."
            play sound audio.footsteps
            hide FRai Default with dissolve

        label scene5:
            stop music fadeout 2.0
            stop sound
            stop nature
            play music audio.shed_night loop
            scene Dark Shed with fade
            show FRai Default at left

            play sound audio.barang_ditaruh
            "The time has shown night. The sky was dark. The sound of nocturnal animals outside the shed was heard."
            "With an oil lamp in his hand, Rai packed up the things he had bought."
            "He arranged the stuff in the remaining space of the wooden shelf."
            "There are lots of things and it takes time. Fortunately, Rai felt he had enough energy left to tidy things up."

            play sound audio.footsteps
            show FRai Default at right with easeinright
            FRai "Well, this one over here... this one over there..."

            show FRai Happy at center with easeinleft
            FRai "Done!"

            "Rai appreciated himself with applause."
            "After seeing that all the items looked like they wouldn't fall, Rai walked over to the mat that had been prepared in advance."
            "He plopped down on the mat."
            "Rai's tiredness and fatigue immediately grabbed him."
            "Rai lets out a long breath."

            show FRai Default
            FRai "(It's normal to be tired, especially on missions. Who wouldn't break a sweat after a long day of going here and there anyway?)"

            "Rai looks up at the ceiling."
            "For the first day, it was quite a long day."

            FRai "Let's see."

            "Rai recalled today's events."
            "He also glances at objects that were suspected to be evidence that had been collected."

            show FRai Serious
            FRai "(A ring-shaped object and a glass the size of a palm.)"

            "Rai looks away from the item."
            "He remembers the conversation he had with the villagers. They have been mentioning that one particular kid so many times."

            show FRai Thinking
            FRai "(Who exactly is this kid?)"
            FRai "(Was it that important for the child to be in the village?)"

            show FRai Serious
            FRai "(Could it be that she... has anything to do with this mission...?)"

            "Even if he wondered so, it was certain that Rai would suspect this child."
            "It was too obvious that she has a big influence in the village even though she wasn't that famous."

            show FRai Thinking
            FRai "Is it that hard to say the child's name? How come no one knows her name."
            FRai "(Or did she not introduce her name? From her personality, it doesn't seem like that.)"

            "Rai felt something was up."
            "He was still confused as to how everything had happened in the village but there was no sign of any big commotion or anything about the girl's disappearance."

        label scene5_1:
            show FRai Serious
            FRai "Or maybe... that kid..."

        menu:
            "Has she been kidnapped?":
                jump scene5_1_a

            "Is she hiding?":
                jump scene5_1_b

        label scene5_1_a:
            show FRai Thinking
            FRai "(If that's the case, was it because she provoked someone? I think she's also kinda naive.)"

            "Rai didn't mean to offend, but he thought about it considering she was denying the fact that she wasn't human."

            show FRai Sad
            FRai "I hope she's okay."

            jump scene5_2

        label scene5_1_b:
            show FRai Thinking
            FRai "(Why is she hiding? Was she threatened by anyone?)"

            "Rai remembered that the villagers said he was acting weird though it didn't bother most people. "

            show FRai Serious
            FRai "Or... there's something else that she should be hiding."

            jump scene5_2

        label scene5_2:
            "Whatever it is, Rai knows all of this is related, either directly or indirectly."

            show FRai Default
            FRai "(Well, I'll find out later anyway.)"

            show FRai Happy
            FRai "Time to rest!"

            play sound audio.bed_sheet
            "Without thinking, Rai adjusted position. He immediately slid into the dream world."

        label scene6:
            stop music fadeout 2.0
            play music audio.shed loop
            scene Shed with fade
            play hewan audio.birds_chirping

            "Morning has come. The sun had risen to the surface brightly."
            "Rai immediately wakes up and arranges his mat."
            "He changes his clothes and gets ready to meet the farmer."

            show FRai Excited with dissolve
            Rai "Okay, let's gooo!!!"

            play sound audio.door_open
            "After getting ready, Rai goes out of the shed to the farmer."

            stop music fadeout 2.0
            stop hewan
            play music audio.farm
            scene Farm with fade
            play sound audio.footsteps
            play nature audio.wind
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep

            show Farmer Default at right
            show FRai Happy at left with easeinleft
            FRai "Good morning, farmer!"
            Farmer "Oh! Morning too, young man."

            "Rai hands over the things the farmer asked for yesterday."
            "The Farmer thanked Rai. A wide smile appeared on his face."

            Farmer "You seem so excited."

            show FRai Default
            FRai "I'm ready to work."
            Farmer "Yeah, yeah. That's great."
            Farmer "Then, move on to the next job, okay?"

            show FRai Happy
            FRai "Ready!"
            Farmer "Do you still have the map from yesterday?"

            "Rai nods."

            Farmer "Now you have to irrigate the cornfield. Take the water in the river."
            Farmer "You know where the bucket is, right?"

            show FRai Default
            FRai "Yeah, I'll pick it up later."
            Farmer "Good. Cheer up."

            "Rai immediately rushes to the shed and takes the bucket. He also brings other things in case he needs them."
            "After preparing, Rai goes to the river."

        label scene7:
            stop music fadeout 2.0
            stop hewan
            stop nature
            stop hewan2
            stop hewan3
            play music audio.river_bgm loop
            scene River with fade
            play nature audio.river_loop loop

            show FRai Default
            "The air feels a lot more refreshing than at the farm. The sound of running water really creates such a calm atmosphere."
            "Rai walks down the rocky road carefully."
            "Rai collects the water with the bucket that he was carrying."

            Unknown "W-woah!!" with vpunch

            show FRai Default at right with easeinright
            "Someone's voice startled Rai."

            show Fisherman Default at left with dissolve

            "It turns out that someone was sitting by the river. He's holding the fishing rod."
            "Apparently, he was pulling a fish."
            "Because he looks troubled, Rai intends to help. The fisherman's face, which was looking happy, turned into confusion."

            Fisherman "Who...?"

            show FRai Default at center with easeinleft
            "Rai takes a closer look and it surprises the fisherman."

            show FRai Happy
            FRai "Sorry, sorry. I didn't mean to startle you."
            Fisherman "Ah yea...."

            show FRai Default
            FRai "By the way, what did you get?"

            "The fisherman hesitantly hands over the thing."

            show Antena Device with dissolve

            "It looks like a fishing hook."
            "But the ends are not bent but straight and not too sharp."

            Fisherman "...Why do strange things keep happening..."

            show FRai Thinking
            FRai "Eh? What did you say?"
            Fisherman "N-no! It's nothing."

            "Rai looks at the object carefully again."

            FRai "Is that a broken fishing hook?"
            Fisherman "I don't think so. The tip is too blunt for a hook."

            show FRai Default
            FRai "(It is true. Is this again related to the mission?)"

            show FRai Happy
            FRai "Sorry if this sounds rude since we just met but may I take that thing? It looks interesting!"
            Fisherman "Of course you can."
            Fisherman "Besides, it can't be used for fishing anyway."

            "Rai receives the hook-shaped object from the fisherman."
            hide Antena Device with dissolve

            show FRai Thinking
            FRai "...hm? How come this mission seems easy huh?"
            Fisherman "W-what?"

            show FRai Happy
            FRai "It's nothing."

            show FRai Thinking
            FRai "(It's getting more and more awkward.)"
            FRai "(Why is it that almost everywhere there must be something odd, like at least one?)"
            FRai "(And again, it's easy to find and get them.)"

            show FRai Default
            FRai "Oh yeah, are you catching fish? How many have you got?"
            Fisherman "Here..."

            "The fisherman shows a bucket filled with fish. The fish filled half the bucket."

            show FRai Happy
            FRai "How about I fish with you?"

            "The fisherman smiles."

            Fisherman "Glad to accept your offer."

            hide FRai Default with dissolve
            play sound audio.water_splashing
            "Rai throws himself into the river and starts catching fish that he saw."
            show FRai Default with dissolve
            "After Rai gave fish to the fisherman, he was given some fish by him."
            "Rai walks home with water and fish in his hand."
            hide FRai Default with moveoutright

        label scene8:
            stop music fadeout 2.0
            stop nature
            play music audio.cornfield loop
            scene Corn Field with fade
            "After Rai gave the fish to the farmer, he went to the cornfield."
            show FRai Default with easeinleft
            "After previously he saw a green-blue scene, now he sees a green-yellow landscape. Plants towering above Rai lined up."

            play sound audio.watering_plants
            "Rai who had brought water, starts watering the corn plants."

            show FRai Happy
            FRai "Water, water~ Keep watering!"

            "The vast place was already starting to get wet with water."
            "Rai sighs and sits on the edge of the field."

            show FRai Default
            FRai "Okay, next..."

            "Rai grabs a hoe and drags it to the empty part of the cornfield."

            show FRai Excited
            FRai "Time to dig!"

            play sound audio.nyangkul
            "Rai plowes the ground diligently."
            "Every now and then he wets the ground with water to make it easier to dig."

            show FRai Surprised
            FRai "Oh?"

            "Something is stuck on the hoe."

            show Rubber with dissolve

            show FRai Thinking
            FRai "This..."

            "Rai takes the thing."
            "The texture is like cloth. It stretches easily."

            play sound audio.barang_klutuk_klutuk
            "Rai puts down his hoe. He put it in his pocket."
            hide Rubber with dissolve

            show FRai Default
            FRai "I'll check it again later."

        label scene8_1:
            show CG3 with fade
            $ persistent.cg3_unlocked = True

            play hewan audio.gagak

            "Rai who was wiping his sweat heard the sound of a crow behind him."
            "The crow perched on the scarecrow."

            FRai Happy "Oh! Hello, sir crow!"
            Crow "Hello! Hello!"

            "Rai laughs happily at the crow's response."

            FRai Default "What are you doing here?"
            Crow "Food! Eat!"

            FRai Surprised "Oh! Looking for food huh?"

            "Rai takes some corn kernels in his pocket."

            FRai Excited "Do you want this~?"
            Crow "Caw!"

            "The crow flew over and pecked at the corn kernels."
            "After picking up some, he immediately flew back into the scarecrow."

            FRai Happy "Is that good, Sir Crow?"
            Crow "Delicious!"
            FRai Happy "Good!"

            "Rai wipes the sweat that ran down his cheeks."
            "The weather is quite hot too."

            FRai Thinking "By the way, does Sir Crow often come here?"
            Crow "Here! There!"
            FRai Default "Ooh. Go back and forth everywhere huh?"

            play sound audio.ting
            "Rai suddenly remembered something."
            FRai Thinking "Mister crow, do you know someone who is missing?"

            "The crow tilted its head, confused."
            FRai Nervous "Uhm, she's a girl. Looks like she used to visit the village. But suddenly she's out of sight."
            FRai Nervous "Do you know anything, sir crow?"
            Crow "The ears! Long!"
            FRai Thinking "(Long ears? Is she an elf too? Is she related to the seller?)"
            FRai Thinking "Is there anything else Mr Crow knows?"
            Crow "Noisy!"
            FRai Nervous "Uh oh, did you mean the girl or me?"
            Crow "You!"
            FRai Surprised "Eh?!"
            Crow "Not!"
            FRai Annoyed "...."
            FRai Happy "Thank you, Sir Crow. If you would lik---"

            play hewan audio.wings_flapping
            hide CG3 with fade

            # scene Corn Field
            "The crow, without waiting for Rai to finish speaking, had already left to fly."

            show FRai Annoyed
            FRai "Wow~ what a very polite crow."

            "Maybe the crow had other business. Let's just assume so."
            "Rai collects his farming tools."

            show FRai Excited
            FRai "It's finally over. Time to go back!"

            "After closing the water reservoir, Rai went to store the equipment in the shed."

        label scene9:
            stop music fadeout 2.0
            play music audio.shed loop
            scene Shed with fade
            show FRai Default at left
            "Arriving at the shed, Rai puts all of his equipmenst in their proper place. He puts large items near the boxes, while small items on the shelves."

            play sound audio.barang_ditaruh
            show FRai Default at right with easeinright
            show FRai Default at center with easeinleft

            show FRai Surprised
            FRai "Oh yeah, that thing earlier."

            show Rubber with dissolve
            "Rai takes a look at the thing that he just got."

            show FRai Thinking
            FRai "It's some kind of rubber, right? That's the one on the clothes."
            FRai "Does this have anything to do with it?"
            hide Rubber with dissolve

            "As Rai stacks up some hay, he notices something strange."

            show FRai Thinking
            Rai "What's this?"

            show Hair at truecenter with dissolve
            "Rai picked it up and examined it."

            FRai "Why is this hay blue?"
            FRai "Oh wait..Is this hair....?"

            "When Rai touched it, it didn't look like the texture of the hair. It feels slicker and stiffer."
            "It is similar to string but thinner."

            FRai "The fact that it's here when it wasn't there before, is it possible that..."
            hide Hair with dissolve

            show FRai Serious
            FRai "(Anyone else has barged in?)"

            "Rai knows that only him and the farmer were in and out of the shed. There are no other workers here."
            "The farmer has also handed over some of the work to Rai."

            show FRai Thinking
            FRai "If it really has something to do with that kid, does that mean she's nearby?"

            "Rai just assumed. But it could be true."

            show FRai Serious
            FRai "Perhaps it's time I report directly to base."

            "Rai plans to return to IPD. That way, maybe he will discover more about the evidence that he had gathered."

            show FRai Default
            FRai "I'll tell the farmer first."

            "Rai then continues on to the next job."

        label scene10:
            stop music fadeout 2.0
            play music audio.MIRA loop
            play nature audio.gemuruh_loop
            scene black with fade
            "At some place...."

            Unknown "Ha ha ha!"
            Unknown "HA HA HA!!"

            "They chuckle."

            Unknown "Are you coming, oh {i}my friend{/i}?"

            play sound audio.petir
            "They can't wait for Rai's arrival."

        label scene11:
            stop music fadeout 2.0
            stop sound
            stop nature
            play music audio.IPD loop
            scene IPD WORKPLACE with fade
            "Rai arrives at the IPD."
            "As usual, Rai reports to the boss as soon as he arrives. He met with his fellow Galileans to take care of the evidence that had been obtained."
            "After handing it over to his co-worker, Rai lets him check thoroughly."

            show Rai Serious with dissolve
            show Galilean_3 Default at left with dissolve
            Rai "What about the results?"
            Galilean_3 "As you might expect, it's all related. All the data is connected."
            Rai "Is it true that..."
            Galilean_3 "You're right."

            "His Galilean co-worker shows the results of their lab analysis."

            show Radar Machine at truecenter with dissolve

            "It looks like a cellphone that has a unique design. The shape is stiff but looks solid."

            show Rai Thinking
            Rai "How can a device like this exists in that dimension?"
            Galilean_3 "I don't know for sure either."
            Rai "Is there anything that can be done with this thing?"
            Rai "Could it be a transmitter or something?"
            Galilean_3 "We caught some signals from this device earlier."
            Galilean_3 "Not as accurate but enough to know the possible location."

            show Rai Serious
            Rai "Alright. Send the coordinates to me immediately."
            Galilean_3 "Yes, sir."

            "Rai receives the location code of the person they are looking for. Rai smirked for a moment."

            show Rai Default
            Rai "I got it. Thank you."

            hide Radar Machine with dissolve

            hide Galilean_3 Default with dissolve
            "After they separated, Rai immediately prepared to move to the intended location, back to Farmland. But this time not the farm, but to a hill near there."

            Rai "Get ready, whoever you are."

            "With an unreadable expression, Rai stepped out of the IPD."

        label scene12:
            stop music fadeout 2.0
            play music audio.hill loop
            scene Hill with fade
            play nature audio.wind loop

            "Rai starts to climb up the hill."
            "He had brought provisions to meet this person face to face."
            "His clothes were still the same as his identity as an apprentice at the farm because there was still the possibility that he might meet people he had known before."
            "Fortunately, the hiking trail looks perfect, it seems that the residents here are used to it."
            "...Or that's what Rai thought earlier."

            show FRai Nervous with dissolve
            FRai "Uhm, where should I go?"

            "Like the experience Rai had, he should return to the starting point of the climb. But when he looked back, the traces of the existing path had completely disappeared."

            show FRai Surprised
            FRai "How come...."

            "Luckily Rai was out in the open so he could see the whole surroundings."

            show FRai Thinking
            FRai "Let's see. If I came from over there, I should have gone to..."

            Adventurer "Oh, are you lost, Kiddo?"
            with vpunch

            show Adventurer Default at left with easeinleft

            "Of course Rai was surprised."

            Adventurer "Did that surprise you? I hope you're okay."

            show FRai Happy
            FRai "I am alright."

            "Rai was still stroking his chest. He was surprised of her presence."

            Adventurer "So is it true about my question earlier?"

            show FRai Surprised
            FRai "Oh! Yeah, I got lost, I guess."

            "The woman giggles."

            Adventurer "It's fine. I'm sure you'll find the way."

            "Rai relieves."

            Adventurer "Now, do you see that rock, kiddo?"

            "Rai looked in the direction the lady pointed."

        label scene12_1:
            Adventurer "Looking at the position of the moss, where do you think we are in?"

        menu:
                "East.":
                    jump scene12_1_a

                "West.":
                    jump scene12_1_b

        label scene12_1_a:
            Adventurer "Haha, nice try."

            "The adventurer ruffled Rai's hair."

            Adventurer "Everyone can make mistakes. That's okay."

            jump scene12_2

        label scene12_1_b:
            Adventurer "Good job, kiddo."

            "The adventurer gives a thumbs up."

            jump scene12_2

        label scene12_2:
            Adventurer "That is the west."
            Adventurer "Moss prefers to grow out of the sun."

            "Rai agrees."

            Adventurer "From what I can see, you're coming from the east, aren't you?"
            Adventurer "So you're going west, right?"

            show FRai Default
            FRai "Yes that's right."
            Adventurer "Then, just follow the direction of the moss. It can guide you."

            show FRai Excited
            FRai "Okay!"

            "They both smiled."

            show FRai Happy
            FRai "Then, I shall get going. I want to continue my journey."

            "The adventurer crossed her arms looking at Rai."

            Adventurer "Yes, be careful, okay."
            Adventurer "Recently there's been a strange sound coming from over there."

            show FRai Thinking
            FRai "Sound?"

            "Rai directly faced the adventure."

            Adventurer "Yeah. Since there weren't many people there, no one knew for sure nor checked the source of the sound."
            FRai "What does that sound like?"
            Adventurer "It sounded like a blacksmith at work or two shovels colliding."

            show FRai Default
            FRai "Oooh...."

            "Rai gets it."

            show FRai Happy
            FRai "Thanks for the info. I'll be careful!"
            Adventurer "Yeah, I believe in you. Hope we meet again."
            FRai "Yes!"

            "Rai waves, then continues his journey to the west side of the hill."

        label scene13:
            stop music fadeout 2.0
            stop nature
            play music audio.cave_bgm loop
            scene caveTunnel with fade
            play nature water_droplets_loop loop

            "After walking quite a distance, Rai reaches the cave."
            "According to information, the location is around here."
            "When Rai arrived, it was true that there were many caves on display. Luckily Rai knows the closest approximate location to the destination."
            "Rai walks through the cave. He saw the surroundings that were filled with stalagmites and stalactites all around."

            show FRai Thinking with dissolve
            FRai "Hmmm..."

            "Rai tries to repeat the information he had received so far."

            show FRai Serious
            FRai "(The device is related to the person IPD is looking for. But, does that cat kid has anything to do with it?)"
            FRai "(Are they related to the farmer?)"
            FRai "(What is their motive?)"
            FRai "(What are they trying to do?)"
            FRai "(If it's getting the IPD or my attention, they sure are getting it.)"

            "Many questions flooded Rai's mind. But that's normal in missions. Rai really had to keep thinking."

        label scene13_1:
            stop music fadeout 2.0
            stop nature
            play music audio.cave_bgm
            play nature audio.water_droplets_loop loop
            scene caveNyabang with fade
            show FRai Surprised
            FRai "Oh?"

            "There are two cave mouths in front of it."

            show FRai Thinking
            FRai "Which one should I go through?"

        menu:
                "Right":
                    jump scene13_1_a

                "Left":
                    jump scene13_2

        label scene13_1_a:
            scene caveNyabang with fade
            show FRai Default
            FRai "To the right, huh?"

            play sound audio.gedubrak
            "Without any warning, Rai falls into a deep hole." with vpunch
            "It seemed there were several minutes before Rai stopped and hit the ground. The banging sound is quite loud."

            show FRai Nervous
            FRai "Aeugh...."

            "Rai tries to get up and goes back to find out where he was."
            "Rai walks through the visible cave path."

            jump scene13_1

        label scene13_2:
            scene caveNyabang with fade
            "Rai walks to the mouth of the cave on the left. He makes sure that the path he had chosen did have traces of being passed by people, such as the footprints of boots."

            show FRai Default with dissolve
            FRai "It's seems like it's going to be a long way.."

            "The deeper Rai goes, the darker the cave is."
            "Although he didn't carry an oil lamp or other lighting, he could see in the dark. Strange indeed."

            #cave bercabang 2
            "And again, he faces two cave mouth options."
            "One has footprints from sports shoes. Others have large puddles of water."

            show FRai Thinking
            FRai "Which one is it?"

        menu:
                "Caves with footprints.":
                    jump scene13_2_a

                "Caves with puddles.":
                    jump scene13_3

        label scene13_2_a:
            scene caveNyabang with fade
            show FRai Default
            FRai "Must be this way. You can see from the traces left here."

            scene black with fade
            "When Rai stepped in, suddenly the surroundings were dark."

            show FRai Thinking
            FRai "(Ah, did I go the wrong way? Yet there are traces, very clear.)"

            "Rai was waiting for the surroundings to become clear."

            stop music fadeout 2.0
            stop nature
            play music audio.hill
            scene Hill with fade
            "After a while, it turned out that Rai was outside the cave with the surrounding green scenery."

            show FRai Default
            FRai "(Back here huh?)"

            "After looking left and right, Rai goes back to the cave entrance not far from where he is sitting."

            jump scene13_1

        label scene13_3:
            show FRai Excited
            FRai "(I'm not that easily fooled.)"

            "Rai walks into the mouth of the cave. He calmly entered without doing one hundred percent supervision. Of course he's in work mode."

            show FRai Thinking
            FRai "(The previous imprint was obvious but the imprint in the cave before that was the footprints of boots. It shouldn't be that different right?)"

            "Rai nods."

            show FRai Serious
            FRai "(This fellow is good at hiding traces too.)"

            "With that, Rai continues to walk through the cave."

        label scene14:
            stop music fadeout 2.0
            stop nature
            play music audio.MIRA loop
            scene caveFinal with fade
            "After going through a long hallway, Rai arrives at a huge place."
            "The place was also bright, as if it didn't feel like it was in a cave."
            "Rai goes around to see the place. He sees several tables with small devices on them."

            play sound audio.footsteps
            "Rai instantly in alert mode."

            Unknown "Oh? I have a guest?"

            show FRai Default at right with easeinright
            "Rai takes a closer look at who it was."

            Unknown "Welcome!"

            show Mira Default at left with dissolve

            "It turned out to be a girl in a dress."

            show Mira Excited
            The_Girl "You must be tired from walking all the way here? Come on! I'll serve you some tea."

            show FRai Annoyed
            FRai "...Who--"

            show Mira Serious
            The_Girl "Hey, are you listening? I'm asking you."

            "The tone when she spoke sounds different from before. It startled Rai a bit."

            show Mira Happy
            The_Girl "Ah, I'm sorry. My program--ah, I mean my body's condition is not completely good but it's still under maintenance anyway!"

            "Rai notices this girl's appearance. Obviously she wasn't human. Especially with the big antennae on her head."

            show FRai Annoyed
            FRai "(That's not a long ear, Mr. Crow.)"

            show Mira Excited
            The_Girl "Come on, come in! There's no need to be shy."

            "Rai approaches The Girl without any words."

            show Mira Happy
            The_Girl "Well, that's it. Come sit here."

            "The Girl pats the small chair across from her before returning to sit on the other side. Rai comes close but chooses not to sit down."

            The_Girl "Eeeh, just take a seat. I'm not going to get mad at you."

            show Mira Excited
            The_Girl "In fact, I'm glad to have friends to talk to over tea!"

            show FRai Thinking
            FRai "Won't be mad? Are you sure?"

            "The Girl nods. She took a sip of something from a cup."

            show Mira Default
            The_Girl "Sure. I haven't spoken to anyone in a long time."

            show FRai Serious
            FRai "Hah! You must be very busy."

            show Mira Surprised
            The_Girl "Hm? Not really. In fact  have nothing to do now."

            show FRai Thinking
            Rai "Question, what do you have in that cup?"
            with vpunch

            play sound audio.desk_slam
            "The Girl pounds the table."

            show Mira Angry
            The_Girl "I'm a human!!"

            show FRai Default
            FRai "But I didn't say you {i}aren't{/i} human?"

            show Mira Annoyed
            The_Girl "Ugh!"

            show Mira Angry
            The_Girl "Well whatever! It's tea, okay?"

            "The Girl continues to sip her tea while Rai keeps an eye on her."

            show FRai Thinking
            FRai "So.. Mind to tell me what all of those things are?"

            show Mira Default
            The_Girl "Why mind that? Didn't you tried so hard just to get here? Just enjoy the beautiful view, while i enjoy my tea."

            show FRai Surprised
            FRai "(She saw me struggling at the cave earlier huh---)"
            FRai "How did you know that?"

            show Mira Happy
            The_Girl "I have super powers!"

            show FRai Default
            FRai "You said you are a human.."

            show Mira Serious
            The_Girl "You think humans can't have any powers?"

            "Rai becomes silent."
            "Indeed he's also a human with something similar like superpowers, he couldn't deny that. But the power of people in general with the strength of IPD members is different."

            show Mira Default
            The_Girl "You're just like... the woman in the village. You should maintain your manners!"

            show Mira Serious
            The_Girl "I guess you should just go home if you don't like it here."

            show FRai Sad
            FRai "Why? Aren't you glad I'm here?"

            show FRai Excited
            FRai "I'm accompanying a girl who was alone in this secluded cave~"

            show Mira Annoyed
            The_Girl "Even though you casually barged in? In the middle of my tea party?"

            show FRai Default
            FRai "Hmm?"

            "The Girl stands up. In an instant the atmosphere turns tense."

            show Mira Serious
            The_Girl "I guess I have to give up being a {i}good girl.{/i}"

            "Rai remained with his confused smile while The Girl had a flat expression this time."

        label scene15:
            # scene caveFinal with fade

            show Mira Sad
            The_Girl "You don't want to do it the peaceful way, do you?"

            show FRai Serious
            FRai "Oh? So we're jumping to the point now?"
            FRai "Good. Been waiting for that"

            show FRai Happy
            FRai "Do people who's trying to break through IPD's defenses want to go the peaceful way?"

            "The Girl is annoyed. Then, she cleared her throat."

            show Mira Excited
            The_Girl "First of all. As a good girl, I will introduce myself."

            show Mira Happy
            MiRA "I'm MiRA. An ordinary human who chats with other humans."

            show FRai Happy
            FRai "Well..Thank you for introducing yourself."

            show FRai Serious
            FRai "Though.. The human part is a bit questionable."

            show Mira Angry
            MiRA "What do you mean?!"

            "MiRA was offended by Rai's words."

            show FRai Serious
            FRai "Take a look of yourself."

            show Mira Surprised2
            MiRA "Eh?!"

            show FRai Happy
            FRai "The point is, you better turn yourself in and come with us, okay? I'll be good if you just cooperate with me!"

            show Mira Annoyed
            MiRA "I am a human!"

            "She's not responding to Rai's words. Rai can not believe that this girl is still in denial."

            show FRai Excited
            FRai "Yes, yes. Of course."
            FRai "So, come with me, will you?"

            show CG4 with fade
            $ persistent.cg4_unlocked = True

            "When Rai is about to pull MiRA's hand, this girl's expression becomes serious."
            "Along with that, around her a hologram-like screen appears."

            MiRA Angry "I'm not leaving!"
            FRai Thinking "Can robots be unstable too?"
            FRai Thinking "Is there something wrong with the program?"
            MiRA Annoyed "I told you multiple times, I am a human!"
            FRai Default "(Yep.)"
            FRai Default "(This girl is a little bit cuckoo in the head.)"
            FRai Nervous "I'm sorry, but you know.. That appearance of yours..."
            MiRA Angry "I have two hands and two legs, isn't that enough?!"

            "Rai's expression calms down."

            MiRA Annoyed "You guys, kept saying that I'm not human."
            MiRA Angry "Even though I only look a little different from you guys!"
            FRai Nervous "(But it's not just a little...)"
            MiRA Angry "The people in the village are like that too! You are the same!"

            "MiRA shows something in her hand."

            MiRA Happy2 "You must know what I'm thinking, right?"
            FRai Serious "Perhaps..."
            MiRA Angry "No one listened to me!"
            MiRA Angry "No one believed me!"
            MiRA Excited "And so I will blow up the village!"

            "Rai's expression turns serious. Of course Rai can not let it happen. Intervention from a world that is not where it belongs is not allowed."

            FRai Serious "Okay listen. Calm down first---"
            MiRA Angry "Huh! You think I'll listen to you?!"
            FRai Annoyed "Ugh...."
            MiRA Angry "I'll get rid of everyone who talks about me behind my back, you're all bad people!"
            FRai Serious "Are you sure about your decision?"
            MiRA Sad2 "What is it that makes me unsure? You saw how they treated me, right?"

            "Rai zips his mouth."

        label scene15_1:
            stop sound
            stop nature
            MiRA Serious "It's useless for you to persuade me. I've been here longer than you, you know."
            MiRA Angry "They always bring up that I'm different. Do you know that?!"
            MiRA Annoyed "They don't believe what I'm saying... They always have that look on their face...."
            MiRA Angry "They keep... discriminating me!"

            "MiRA slightly bowed. Her voice is low, almost like a whisper."

            MiRA Sad3 "Do you know... how does that feel?"

        menu:
                "Let her be.":
                    jump scene15_1_a

                "Calm her down.":
                    jump scene15_2

        label scene15_1_a:
            #STILL IN CG

            MiRA Sad4 "Haha..."
            FRai Nervous "What?"
            MiRA Sad "See...?"
            FRai Default "Eh?"
            MiRA Angry "Even you are the same as them!"
            MiRA Angry "Why won't you just believe me?!!"
            FRai Surprised "WAIT!"
            with vpunch

            play sound audio.bomb_explode
            "MiRA presses the forbidden button. Red screens appear everywhere. Each screen displays different corners of the village. It could be seen from the screen that the village is in chaos due to explosions everywhere."
            play nature audio.bomb_nging_loop_fadein
            MiRA Excited "EAT THAT!"


            "MiRA laughs with satisfaction seeing the destruction in front of her eyes."
            "Rai widens his eyes. Rai tries to believe what happened."
            "The mission before his eyes, failed."

            FRai Annoyed "(I wish I could redo it again...)"

            show black with fade
            hide black with fade

            jump scene15_1

        label scene15_2:
            MiRA Sad "Though... even though...."
            MiRA Sad2 "I just want to be accepted.."
            FRai Sad "You know what will happen if you press the button right?"
            FRai Sad "Are you sure you want to do that?"
            MiRA Annoyed "Yes! O-of course!"
            MiRA Sad2 "I guess..."
            FRai Sad "By doing that... you know? You might regret it..."
            FRai Sad "All those people in the village, they've been looking for you, you know?"
            MiRA Surprised "...."
            MiRA Surprised2 "Huh?"
            FRai Serious "Despite the way they look at you, I do think they are still concerned about your wellbeing. They are wondering about your whereabouts."
            FRai Sad "The guy and the grocery seller I met last time even thought that you tried too much to blend in."
            FRai Sad "They even said that they are fine accepting you as a person even if you are not like them."
            FRai Serious "I don't think their speech nor manner implied any malicious intention. It's just a misunderstanding on your side."
            MiRA Annoyed "You're lying!!"
            FRai Serious "Why would I? Let me ask you this again. From what I've told you and from what you've seen from the villagers."
            FRai Serious "Do you think those actions were fueled by hatred? Malice?"
            FRai Serious "Does it even make sense for someone who is trying to discriminate against you to be concerned about you?"
            MiRA Annoyed "Ugh...."
            FRai Default "So, just hand over that dangerous thing and come with me, okay?"
            FRai Default "We'll get everything straight with a chat, shall we?"

            hide CG4 with fade

            # scene caveFinal
            show Mira Default at center with easeinleft
            "MiRA steps closer to Rai."
            "MiRA gives the trigger to Rai."

            show FRai Excited
            FRai "Good girl!"

            "Rai secures that thing."

            show FRai Happy
            FRai "Then let's go outside now. The sun must be shining bright outside!"

            "Rai led MiRA out of her residence."
            "Before leaving, Rai asked MiRA to turn off all existing tools."
            "They walk out of the cave in silence."

        label scene16:
            scene Hill with fade
            play nature audio.wind loop
            play sound audio.footsteps_grass

            "Rai and MiRA come out of the cave. They walked down the hill."
            "The wind blows filling the silence between them. It's time to head back to IPD, bringing along his newly found inmate, Rai contacts the IPD to open up a portal."

            show FRai Default at center with dissolve
            show Mira Default at right with dissolve
            FRai "Just a minute, MiRA."

            "MiRA nods."
            hide FRai Default with moveoutleft
            "Rai walks a little away from her."
            "MiRA looked up at the sky sadly."

            show Mira Sad
            MiRA "The sky..."
            MiRA "I-it's beautiful"
            MiRA "What have I been doing all this time?"

            "MiRA knew that all of this was wrong. She also knew that the people there weren't actually that mean to her."
            "Deep down, MiRA was actually grateful to be there. All of them were trying to get to know MiRA."
            "She herself made the barrier between her and others."
            "She should have been more open while she could. She was worrying too much"
            "Worrying that people won't accept her. When in fact, she was the one who didn't accept herself."

            play sound audio.footsteps_grass
            show FRai Default at center with easeinleft
            "Rai goes back to MiRA again."

            FRai "Let's go."

            "Rai and MiRA head back down the hill."
            "Rai walks in front of MiRA."
            "Rai doesn't handcuff MiRA because she wants to cooperate."

            show Mira Default
            MiRA "...Thank you..."

            show FRai Default
            FRai "Hmm?"

            "Rai glances at MiRA."

            FRai "Oh, it's nothing."

            show Mira Serious2
            MiRA "..."
            FRai "You know what.."
            FRai "I don't think it's that bad being a robot."

            show Mira Annoyed
            MiRA "A HUMA-"

            show Mira Default2
            MiRA "...An android."

            show FRai Happy
            FRai "An android, yes."
            FRai "In fact.. I do think you look cool!"

            show Mira Surprised2
            MiRA "Really?!"

            show Mira Happy2
            MiRA "Thank you!!"

            show Mira Default2
            MiRA "Hearing that made me really happy."
            MiRA "I guess that's what I've been wanting to hear."

            "Rai ended the journey by taking MiRA to IPD."
            "Rai missed something though."
            "There's something left on MiRA's table.."

            stop music
            stop nature

            $persistent.k2_caught = True

            show black with fade
            pause(2.0)

            show CG11 with fade
            $ persistent.cg11_unlocked = True
            pause(10.0)
            show black with fade
            pause(5.0)

            jump ending


    label route3:
        label R3scene1:
            stop music fadeout 2.0
            stop nature
            play music audio.farm loop
            scene Farm with fade
            play nature audio.wind loop
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep


            show Rai Default
            Rai "Alright, so here's the place huh..."

            "Rai is looking around, gazing through the fields, to familiarize himself with the scenery that will be with him for quite a long time."
            Rai "Ahh~ the breeze here feels nice, exactly like what I expected."
            Rai "Oh right, I should look for the farmer first huh? He must be expecting me by now."

            "Rai looks around, trying to find the farmer, just to find nothing such as that in sight."

            show Rai Thinking
            Rai "He's nowhere to be seen around... maybe he's inside the barn? I should go check."

            "Rai went towards the barn, but just as he tried to open the door, suddenly a big hand touched his shoulders."

            show Farmer Default at right with easeinright
            Farmer "Hey kid!"
            with vpunch

            show Rai Surprised
            Rai "A-ah... hello sir!"
            Rai "(Whoa, that surprised me.)"

            show Rai Annoyed
            Rai "(I'm not a kid though, hmph.)"
            Rai "(Oh well, for the sake of this mission, I'll let it slide this time.)"

            Farmer "Who are you? What are you doing? Are you trying to break into my farm?? Are you—"

            "The farmer suddenly stops."

            Farmer "Ah, my bad for jumping to conclusions, but you do kinda look suspicious kid, haha."

            show Rai Nervous
            Rai "A- actually, i'm looking for you just now sir."
            Farmer "Hmm? What kind of business did you have with this old man?"
            Farmer "Oh wait... are you perhaps the..."

            show Rai Happy
            Rai "Yeah! I'm the intern that's going to help you around here for a while sir! Nice to meet you!"
            Farmer "Likewise, kid!"

            "The farmer observed Rai for a bit."

            Farmer "Hmm... but you sure you could put up with the farmwork kid?"
            Farmer "Ah, but you're the one who came here on your own will..."
            Farmer "I'm sure you already thought this through."

            show Rai Annoyed
            Rai "Don't underestimate me just yet sir!"

            show Rai Excited
            Rai "Even though I look like this, physical labor is nothing for me!"
            Rai "You can count on me sir!"

            show Rai Nervous
            Rai "(*gulp* I might have exaggerated it a little bit...)"
            Rai "(Oh well, if that's what it took to earn his trust.)"

            Farmer "Hahaha, you're such a confident kid, I like that."
            Farmer "Alright, but you must be tired from your trip today right? I'll start the work tomorrow"
            Farmer "You should rest up for today, or if you want, you could go around the neighborhood to get yourself used to our environment, it's your call."

            show Rai Happy
            Rai "Thanks for your consideration sir! I might go with the latter suggestion, I also want to see what's around here."

            Farmer "Alright then, I'll leave you to yourself kid"
            Farmer "Have fun and see you tomorrow."

            show Rai Happy
            Rai "See you tomorrow sir, have a nice day!"

            play sound footsteps_grass
            hide Farmer Default with moveoutright

            show Rai Default
            Rai "(Alright, now that i'm free, maybe i should be getting started on the investigation)"

            show Rai Thinking
            Rai "(Hmm... where should i go though...)"

        menu:
            "Take a stroll on the forest nearby":
                jump R3scene1_1_a

            "Go to the village and see the market there":
                jump R3scene1_1_b

            "Go fishing on the river":
                jump R3scene1_1_a

        label R3scene1_1_a:
            show Rai Thinking
            Rai "Hmm.... But I'm already kinda tired today."

            show Rai Default
            Rai "Maybe I should go to the village and the market instead, i'm also curious about the people of this world."

            jump R3scene2

        label R3scene1_1_b:
            show Rai Default
            Rai "Yeah, I should probably check the village for now."
            Rai "This is also my chance to learn about the villagers."
            Rai "Maybe I would also find some clues."
            Rai "Alright let's go!"

            jump R3scene2

        label R3scene2:
            stop music fadeout 2.0
            stop hewan
            stop hewan2
            stop hewan3
            stop nature
            play music audio.village loop
            scene Village with fade
            play nature people_chattering_loop loop

            show Rai Surprised
            Rai "So this is the village huh..."

            show Rai Excited
            Rai "Whoa... what a lively village!"

            show Villager Default at left with easeinleft
            Villager "Haha! Sure it is."
            Villager "Is this your first time here? Never seen you around before."

            show Rai Surprised
            Rai "Ah hello there."

            show Rai Default
            Rai "That's right, I just came here today."
            Villager "What kind of business did you have around here?"
            Villager "It's been a while since a youngster like you showed up outta nowhere."

            show Rai Happy
            Rai "I'm helping out the Farmer around the farm for now"
            Rai "Maybe you could say it was an internship? Hehe."
            Villager "Ah, so that's how it is."
            Villager "Well, good luck on your job."
            Villager "Maybe you should check out the market after this."
            Villager "There's a lot of interesting stuff there for sure."
            Rai "Yes, that's what I planned to do after this."
            Rai "Thanks for the suggestion though."

            "Rai suddenly realized something."

            show Rai Thinking
            Rai "(Wait, did he say that it's been a while since someone like me showed up?)"
            Rai "(I wonder if they're the ones that I'm looking for?)"
            Rai "(Should I ask him for more information about them?)"

        menu:
            "Ask the villager about the other newcomer":
                jump R3scene2_1_a

            "Nope, time to get going":
                jump R3scene2_1_b

        label R3scene2_1_a:
            show Rai Surprised
            Rai "Ah, wait!"

            show Rai Default
            Rai "I recalled that you said it's been a while since someone like me showed up around here?"
            Rai "Does that mean there's someone relatively new around here like me?"
            Villager "Yeah, you wanna know about it?"
            Rai "Yes, please tell me about them."
            Villager "Alright, I guess it would be easier for you to get along with fellow newcomers huh?"
            Villager "I don't really know about her, but not long ago i heard that someone around your age, a young woman, started living with the butcher"
            Villager "I don't know, maybe she adopted her?"
            Villager "But it's kinda weird that someone like her decided to adopt someone as a daughter."

            show Rai Thinking
            Rai "Weird?"
            Villager "Uh... if i could put it into words... the Butcher is like someone that you don't want to mess around with"
            Villager "A straightforward, and sometimes aggressive person, maybe that's how i would describe her"
            Rai "I see..."
            Rai "Thank you for the information!"
            Rai "It's getting late, maybe i should get going"

            show Rai Happy
            Rai "See you later!"
            Villager "Hope you found that information helpful, good luck!"

            jump R3scene3

        label R3scene2_1_b:
            show Rai Default
            Rai "(Ah, nevermind)"
            Rai "(maybe i would find out about it sooner or later)"
            Rai "(Time to get going!)"
            Rai "Sorry for taking up your time"
            Rai "It's getting late, maybe i should get going"

            show Rai Happy
            Rai "See you later!"
            Villager "It's alright, happy to help."
            Villager "Good luck!"

            jump R3scene3

        label R3scene3:
            stop music fadeout 2.0
            stop nature
            play music audio.market
            scene Market with fade
            "After walking for a short while, Rai arrived at the market, but unlike his expectations..."

            #Sfx silent
            show Rai Surprised with dissolve
            Rai "Eh?..."

            show Rai Default
            Rai "(Looks like everyone is already preparing to pack up for today.)"
            Rai "(Maybe I came too late?)"
            Rai "(Oh well, I'll just come back to the farm and return here tomorrow.)"

            "Rai returned back into the farm, and spent the rest of the day resting up to prepare for his first day tomorrow."

        label R3scene4:
            stop music fadeout 2.0
            scene black with fade
            "The next day..."

            play hewan audio.chicken_morning

            Rai Surprised "Whoa!"
            with vpunch
            play sound audio.gedubrak

            play music audio.shed loop
            scene Shed with fade
            show Rai Annoyed
            Rai "O-oh... it's already morning huh..."

            show Rai Default
            Rai "I should be getting ready for today."
            hide Rai Default with dissolve
            show FRai Default with dissolve

            "After preparing himself for the long day, Rai went toward the field."
            "The Farmer, as expected, had already waited for him there."

            stop music fadeout 2.0
            play music audio.farm loop
            scene Farm with fade
            play nature audio.wind loop
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep

            show Farmer Default at right
            show FRai Default at left with easeinleft
            Farmer "Good morning kid, it's your first day working today, you're ready?"

            show FRai Excited
            FRai "Readier than ever sir!"
            FRai "Or you could say that i am, Rai-dy, heheh"
            Farmer "Ha, good one kid"
            Farmer "Alright, for your first day, you're free to choose what kind of work you wanna do"
            Farmer "Ok, what will it be for today?"

        menu:
            "Till the cornfields":
                jump R3scene4_1_a

            "Take care of the barn animals":
                jump R3scene4_1_a

            "Restock supplies at the market":
                jump R3scene4_1_b

        label R3scene4_1_a:
            Farmer "On second thought, maybe i should send you to restock some supplies instead"
            Farmer "It's also a good opportunity to get acquainted with the mart vendors, should be good for you"

            jump R3scene4_2

        label R3scene4_1_b:
            Farmer "Oh you want to help restocking at the market?"
            Farmer "Sure sure"
            Farmer "You must also be eager to know more about the neighborhood right?"
            Farmer "Alright, go on."

            jump R3scene4_2

        label R3scene4_2:
            Farmer "That reminded me, you already went to the village yesterday right? How was it?"

            show FRai Default
            FRai "The village is lively, the people are also nice"
            FRai "But too bad, i was too late when i came to the market yesterday, everyone's already wrapped up for that day."
            Farmer "I see I see... That's more reason to send you there today"
            Farmer "Alright, i need you to go to the butcher on the market"
            Farmer "Tell her to get the Farmer's usual stuffs"
            Farmer "She should know already"
            Farmer "Oh, and also tell her to put it on my tab."

            show FRai Thinking
            FRai "(The butcher huh...)"
            FRai "(This might be my chance to look for a lead.)"

            show FRai Happy
            FRai "Ok, got it!"
            FRai "I'll be off now, goodbye!"
            Farmer "Take care!"

            jump R3scene5

        label R3scene5:
            stop music fadeout 2.0
            stop nature
            stop hewan
            stop hewan2
            stop hewan3
            play music audio.market loop
            scene Market with fade
            play nature people_chattering_loop loop

            show FRai Default
            FRai "So this is how the market looks like on these hours huh"
            FRai "It's just as lively as the village, I mean, look at those crowds."

            show FRai Thinking
            FRai "Actually at first I wanted to look around first"
            FRai "But i think i should go straight to the butcher, what the villager said yesterday still bugging me."

            "Rai, decided to get rid of any desire to procrastinate inside him, went straight to the butcher, even though he originally wanted to look around for a while."

            show FRai Default
            FRai "Excuusee meee."

            show MeatButcher Default at right with easeinright
            Butcher "Yo kid, what did you need?"

            "The butcher turns around to see Rai."

            Butcher "Make it quick kid"
            Butcher "I don't have all day, you're not the only customer here"

            show FRai Nervous
            FRai "A-ah yes..."

            show FRai Nervous
            FRai "(Whoa, she's so intimidating)"
            FRai "(Get yourself together Rai Galilei)"

            show FRai Serious
            FRai "I was sent here by the Farmer, he said to get the usual."
            Butcher "Heh, don't be so serious kid"
            Butcher "Sorry for the earlier, I'll get your order up right now, please wait a little."

            show FRai Nervous
            FRai "O-okay?"

            "The Butcher went to fetch Rai's order. In the meanwhile"

            show CG5 with fade
            $ persistent.cg5_unlocked = True

            FRai Thinking "(Hmm... look at these juicy meats, they look delicious)"
            FRai "(I wonder if i should use some of the money the IPD provided me to buy some?)"
            FRai "(To throw myself a welcoming BBQ party perhaps?)"
            FRai Default "(Oh no I shouldn't)"
            FRai "(These are for emergencies only)"
            FRai "(I can't splurge it carelessly like that)"
            Butcher "Your order's here kid."

            hide CG5 with fade

            Butcher "That was quick heh?"
            Butcher "Glad i have someone to help out here now"

            show FRai Happy
            FRai "Thanks ma'am"
            FRai "Oh also, the farmer told me to put these on his tab"
            Butcher "Ye, i know that already"
            Butcher "But give this to him after you get back"

            "The Butcher handed Rai a piece of paper."

            show FRai Thinking
            FRai "What is this for?"

            Butcher "That's the thing i needed him to prepare tomorrow in place of today's payment"
            Butcher "I'll get my daughter to fetch it tomorrow at the farm."

            show FRai Default
            FRai "Ah, got it"
            FRai "I'll give it to him when i get back"
            Butcher "Oh before you go, may I ask something else?"
            FRai "Yes?"
            Butcher "Since you're also new here, I want to ask you to be my daughter's friend"
            Butcher "She came here not too long ago, and she's kinda shy"
            Butcher "Hope she can open up more with someone who's also new in the farmland."

            show FRai Surprised
            FRai "E-eh?? That was so sudden"
            Butcher "So you're rejecting my request?"

            show FRai Default
            FRai "No, not like that"
            FRai "Actually, I'm grateful for the chance"
            FRai "Maybe she could also give me pointers around the farmland, and something like that"
            Butcher "Heh, good"
            Butcher "BUT"
            Butcher "I only asked you to get along with her"
            Butcher "Don't even try to do anything to her."
            Butcher "Don't you dare put her in danger"
            Butcher "You didn't want to incur this Lioness' wrath, right?"


            show FRai Nervous
            FRai "Y-you didn't have to worry about that"
            Butcher "Good, we're done here for today"
            Butcher "Now go"

            show FRai Default
            FRai "Alright, i'll be going now"

            "After getting things done, Rai left the market, and went back to the farm."
            "Finishing off the rest of his duty that day"
            "The day goes on after that"
            "Until the next day comes..."

        label R3scene6:
            stop music fadeout 2.0
            stop nature
            scene black with fade

            "The next day..."

            play music audio.shed loop
            scene Shed with fade
            show FRai Default
            FRai "Phew, that was quite heavy"
            FRai "Man, the shed was really messy, I'm glad everything were back on where they belong"
            FRai "Oh right, someone was supposed to come here today huh?"
            FRai "I wonder when she'll come"

            stop music fadeout 2.0
            play sound audio.door_open
            play music audio.Elsyne loop
            Unknown "Excuse meee"

            show FRai Surprised
            FRai "Huh, who's that?"
            FRai "Comiiing."

            show Elsyne Surprised at left  with easeinleft
            The_Girl2 "Eeeek!" with vpunch
            The_Girl2 "W...who are you?"

            show Elsyne Scared
            The_Girl2 "A... A thief?"
            The_Girl2 "D... Did someone break in?"
            The_Girl2 "W... Where's the Farmer?"

            show Elsyne Default
            The_Girl2 "Ah, wait"

            "The girl realized something"

            show Elsyne Shy
            The_Girl2 "Y... You're the customer from yesterday right?"
            The_Girl2 "S... Sorry for the earlier"

            show FRai Default
            FRai "Wait wait, it's fine, really"
            FRai "Have you calmed down"

            The_Girl2 "Y.. Yes"
            FRai "Okay then"
            FRai "So, are you the one who's sent by the butcher to pick up her request?"
            The_Girl2 "Yup"
            Elsyne "I... I'm Elsyne, nice to meet you"

            show FRai Happy
            FRai "Same here!"
            FRai "My name's Rai, by the way"
            Elsyne "M... Mr Rai huh..."
            FRai "No no, just Rai is fine."
            Elsyne "Ah, okay."
            FRai "I'll go fetch the things for you, wait here for a sec ok."
            Elsyne "Mmhm."


            "Rai went to the back, and returned with a sack full of farm commodities."

            FRai "Phew, here you go."
            Elsyne "Uh-huh, thanks."
            Elsyne "I'm going now, bye."

            show FRai Surprised
            FRai "W-wait, you sure you can bring that back all by yourself?"
            FRai "Do you need me to accompany you?"
            Elsyne "I'm fine all by myself, no need to worry."
            Elsyne "And even though you were to accompany me, you're sure you know where to go?"

            show FRai Nervous
            FRai "Ah, haha..."
            Elsyne "S... Sorry, I didn't mean to offend you."
            Elsyne "A... Actually, mom asked me to show you around after this."
            Elsyne "You should go with me."
            FRai "All right then, let's go."
            Elsyne "Mmhm"

            show FRai Excited
            FRai "Okay!"
            FRai "We should probably go bring these things first right?"
            Elsyne "Mmm."
            Elsyne "Let's go back to the village first."

            scene Village with fade

            show Elsyne Default with easeinright
            show FRai Default at right with easeinright

            Elsyne "Here"
            FRai "Phew, arrived at last"
            FRai "It's not even that far, but these things are quite heavy"
            FRai "I'm already sweating"
            Elsyne "Told you"
            Elsyne "I would've been fine by myself"

            show FRai Happy
            FRai "Don't worry about that though!"
            FRai "As the Farmer's helper, i should be getting used to these kind of work"
            Elsyne "Mmmm,if you say so"
            Elsyne "Wait here"

            show FRai Surprised
            FRai "Eh?"

            hide Elsyne Default with dissolve
            "Elsyne went inside, and returned back with a cup of water in a flash"

            show Elsyne Default with dissolve
            Elsyne "Here, drink."

            show FRai Happy
            FRai "Thanks, I appreciate it"
            Elsyne "Mmhm"
            Elsyne "Ma told me to do that if someone's visiting"

            show FRai Thinking
            FRai "Ma? You mean the butcher?"
            FRai "I didn't expect she's someone to said something like that"
            Elsyne "Yes..."
            Elsyne "She might looks a little rough outside, but actually she's really kind"

            show FRai Default
            FRai "You're right"
            FRai "She got this really intimidating aura when we first met"
            FRai "But when she's talking about you, she somehow softened"
            Elsyne "Uh-huh"

            show FRai Thinking
            FRai "(So that's how it is huh)"
            FRai "(She's the someone who can douse the Butcher's raging flames)"
            FRai "(She must be that precious for her)"
            FRai "(That reminded me, should i ask her about her views toward the village and the villagers?"

        menu:
            "Yes, i want to know her opinion about the village":
                jump R3scene6_1_a

            "No, that's too personal, i shouldn't interfere":
                jump R3scene6_1_b

        label R3scene6_1_a:
            show FRai Thinking
            FRai "So, I've been meaning to ask you something, is it okay?"
            Elsyne "Hmm? Go on"
            FRai "You've been living here not long before i arrived right?"
            FRai "What did you think about this village and the villagers"
            Elsyne "Ah, that"
            Elsyne "They're... a bunch of nice people"
            Elsyne "When Ma first took me in, i didn't expect them to be so welcoming"

            show Elsyne Sad
            Elsyne "I was so scared back then..."
            Elsyne "The fear of being rejected, shunned, or..."
            Elsyne "Being feared"
            Elsyne "But... yeah..."
            Elsyne "I'm grateful of the kindness that they've shown towards me"
            Elsyne "Sometimes... i don't think i deserved this all these kindness"
            Elsyne "Someone like me..."

            show FRai Serious
            FRai "I'm sorry, but you're wrong there"
            Elsyne "Huh?"
            FRai "Everyone deserves kindness, no matter how little they are"
            FRai "Even though they're a criminal who took thousands of life, i don't think they should be robbed entirely of kindness"
            FRai "Though, you're nothing like that, so please be more confident of yourself"
            FRai "You're more than deserved for all of this"
            Elsyne "......"

            show Elsyne Smile
            Elsyne "A...alright, thanks for those encouraging words"
            Elsyne "I think... I should be more proud of myself from now on."

            show FRai Happy
            FRai "That's the spirit!"
            Elsyne "(What a weird guy...)"
            Elsyne "(He knows nothing...)"
            Elsyne "No, he shouldn't know anything about that"
            Elsyne "My true self...."

            jump R3scene6_2

        label R3scene6_1_b:
            show FRai Serious
            FRai "This is my chance to get more information from her"
            FRai "Should I really pass on this chance?"

        menu:
            "Yes, i want to know her opinion about the village":
                jump R3scene6_1_a

        label R3scene6_2:
            FRai "Oh anyway, where should we go next?"

            show Elsyne Default
            Elsyne "Depends, your call"

            show FRai Thinking
            FRai "Hmmm let's see..."
            FRai "I've been to the village and the market, so how about..."
            Elsyne "There's a forest and a river near the farm, have you been there?"
            FRai "Oh? Your personal recommendation?"
            FRai "No i haven't been there yet"
            FRai "But if you're the one who recommended it, it must be a nice place"
            Elsyne "Uh-huh, i often went there after work to wind down"
            Elsyne "You could either take a stroll in the breezy forest, or sit down and relax to the sound of the flowing river."
            Elsyne "It's such a lovely place, i'm sure you would like it"

            show FRai Excited
            Rai "Alright then, that sounds interesting"
            Rai "I'm fine with whichever we go first"
            Rai "We should be off now"
            Elsyne "Sure"
            Rai "Alright, what're we waiting for then? Let's gooo"

        label R3scene7:
        scene Forest with fade
        play hewan audio.birds_chirping

        show Elsyne Default with easeinleft
        show FRai Surprised at left with easeinleft
        FRai "Whoa, so this is the forest huh..."
        FRai "I didn't expect there's a forest this dense nearby"
        Elsyne "Yup"

        show FRai Happy
        FRai "Aaahhh, what a nice breeze"
        FRai "I understand why you liked this place"
        Elsyne "Uh-huh"

        show FRai Thinking
        FRai "So, what'd you usually do here?"
        FRai "Just aimlessly strolling around? Or there's something else?"
        Elsyne "Mostly just wandering around"
        Elsyne "But sometimes I also hunt here"

        show FRai Surprised
        FRai "What???"
        FRai "You? Hunting?"
        Elsyne "W...why so surprised"
        Elsyne "As the Butcher's daughter, i should know a thing or two about hunting"
        Elsyne "I'm not that frail, you know"

        show FRai Nervous
        FRai "A-ah, sorry"

        show TalkingTree Default at right with dissolve

        show FRai Surprised
        FRai "Huh, what's that giant tree over there?"
        FRai "Wait, is it ALIVE?"
        Elsyne "Plants are also a living thing you know"
        Elsyne "But yes, that's the guardian of this forest, the Talking Tree"
        Elsyne "Looks like he's taking a nap right now"

        play sound audio.snore

        Talking_Tree "Zzzz...."

        show FRai Default
        FRai "We shouldn't bother him then, let's move on"
        Elsyne "Uh-huh"

        show black with fade
        stop sound
        hide TalkingTree
        hide black with fade

        show FRai Thinking
        FRai "So... Can you tell me more about him?"
        FRai "Those kind of tree aren't something that you usually see everyday"
        FRai "Except if you lived on the farmland, i guess"
        Elsyne "Sure"
        Elsyne "Ma told me that at first, the tree was originally believed to be some kind of myths in the village"
        Elsyne "But later, it turned it to be a real thing"

        show FRai Excited
        FRai "Whoa, neat"
        Elsyne "Uh-huh"
        Elsyne "Oh, we've arrived"

        show FRai Default
        FRai "I can see the clearing over there"
        FRai "So we've arrived at the exit?"
        Elsyne "Not quite"
        Elsyne "You'll see soon enough"

    label R3scene8:
        stop hewan
        scene River with fade
        play nature river_loop loop

        show Elsyne Default with easeinright
        show FRai Surprised at right with easeinright

        FRai "Wow, it's the river!"
        Elsyne "Yup"
        Elsyne "This is our next destination"
        Elsyne "The river is a pretty popular spot among the villager"
        Elsyne "On the weekend you could see people fishing, picnicking, or even swimming here"

        show FRai Default
        FRai "I see..."
        FRai "And if i recall correctly, you liked to sit down and relax to the sound of the flowing river here right?"
        Elsyne "Yeah"
        FRai "I do agree with you"
        FRai "It's so calming around here"
        FRai "I think one of these days i'm gonna snuck outta the farm to take a nap for a while here..."

        show FRai Thinking
        FRai "Anyway, this river should lead somewhere right?"
        FRai "What is at the end of the river? A lake?"

        show Elsyne Smile
        Elsyne "*giggles* Glad you asked"
        Elsyne "It's more than just a lake"
        Elsyne "I was saving this for the last"
        Elsyne "We should hurry up then"
        Elsyne "Come, let's go!"
        FRai "(She suddenly became more cheerful when i mentioned about it)"
        FRai "(I wonder what's on there?)"

        show FRai Surprised
        FRai "Ah, coming!"

        "The two of them quickly went and followed the river. Elsyne's enthusiasm seems weird for Rai at first, but when they arrived at their final destination, everything cleared up."

        label R3scene9:
            stop nature
            scene waterfallDay with fade
            play nature waterfall_loop loop

            show Elsyne Smile with easeinright
            show FRai Surprised at right with easeinright

            Elsyne "Here we are!"
            FRai "So... when you said it was more than a lake..."
            FRai "It's actually a waterfall???"
            Elsyne "Yup"
            FRai "I don't even remember how many times i feel amazed by the Farmland today..."

            show FRai Excited
            FRai "The farmland never ceases to amaze me!"
            Elsyne "Glad you're having fun"

            show Elsyne Shy
            Elsyne "When Ma told me to bring you around, i was afraid that you'll feel bored with me"

            show Elsyne Smile
            Elsyne "But i'm glad that's not the case"

            show FRai Default
            FRai "Bored?"

            show FRai Excited
            FRai "On the contrary, this might be the most exciting day i've ever had since i first came to the Farmland"

            show Elsyne Smile
            Elsyne "I see..."
            Elsyne "You know..."
            Elsyne "This waterfall might be my favorite place among everything else on the Farmland"
            Elsyne "Especially at night"
            Elsyne "Either after working, or after going on a hunt, for me, nothing can beat the feel of the waterfall at nighttime"
            Elsyne "Maybe we should go together sometimes at night"
            FRai "Sounds great!"
            FRai "I'll be looking forward to it"
            Elsyne "Now that we've seen everything, let's go back"
            Elsyne "You must be tired for today right?"

            show FRai Default
            FRai "Yeah"
            Elsyne "I can't lie about that, it's been a while since I walked this far"
            FRai "But you shouldn't worry about me"

            show FRai Happy
            FRai "I'm fine and everything has been a blast today!"

            show FRai Thinking
            FRai "Ah right"
            FRai "But does that mean we should walk all the way back through the river and forest again"
            Elsyne "No"
            Elsyne "There's a shortcut actually"

            show FRai Surprised
            FRai "Wait, so we can actually go straight here from the farm without going through the forest and river?"
            Elsyne "Uh-huh"
            Elsyne "But since I'm giving you a tour today, it won't be fun that way."

            show FRai Default
            FRai "That makes sense"
            FRai "It's getting late now, let's get going."

            "Having ended their tour, the two of them went back to the farm, and parted ways there for today"

        label R3scene10:
            stop music fadeout 2.0
            stop nature
            play music audio.shed_night
            scene Dark Shed with fade

            "That night, Rai tried to recall today's events before finally going to sleep."

            show FRai Thinking with dissolve
            FRai "(Hmm... Perhaps I have gathered some valuable information about my suspect after today.)"
            FRai "(I do recall something weird.)"
            FRai "(Firstly, when i talked about 'a criminal who took thousands of lives', she went quiet for a while.)"
            FRai "(I don't know if she's still being absorbed in the somber atmosphere from before.)"
            FRai "(Or if she's hiding something.)"
            FRai "(And second, she hunts?)"
            FRai "(When we went to the forest earlier, i didn't found a trace about a hunt or something like that)"
            FRai "(Unless if the hunter was the kind that can incapacitate or dispose of their prey easily without leaving a trace, like using some kind poison, perhaps?)"
            FRai "(Furthermore, she should be working at the Butcher's from morning until a little past afternoon right? When did she find the time to hunt?)"
            FRai "(At dusk? Or maybe in the evening?)"
            FRai "(And I also recalled that she often visited the waterfall at nighttime, maybe that was also connected?)"
            FRai "(I know I shouldn't be that distrustful towards her, but i need to confirm this myself)"
            FRai "(Considering the type of person that she is, maybe a direct confrontation won't work')"
            FRai "(Maybe I should try to investigate the forest at night?)"
            FRai "(But that could be dangerous though)"
            FRai "(Alright, that's enough for today)"
            FRai "(I'm already feeling tired, and i need to wake up early tomorrow)"
            FRai "(Well, goodnight)"
            stop music fadeout 2.0
            "Meanwhile, on Elsyne's side"

            play music audio.Elsyne loop
            scene Village Night with fade
            show Elsyne Default
            Elsyne "(Today was so much fun...)"
            Elsyne "(It's been a while since i last interacted this much with a stranger ever since i came here)"
            Elsyne "(Rai... huh)"
            Elsyne "(I don't think we're just strangers anymore)"
            Elsyne "(A friend... maybe?)"

            show Elsyne Sad
            Elsyne "(Do I really deserve this kind of happiness?)"
            Elsyne "(Even after everything that he said earlier today?)"
            Elsyne "(Someone like me who...)"
            Elsyne "(No, I shouldn't think about that anymore.)"
            Elsyne "(I'm trying to live a new life here... even with this stained past.)"
            Elsyne "(And i also shouldn't let him know the truth)"
            Elsyne "(About me...)"
            Elsyne "(About who I really am...)"
            Elsyne "(And about what i really am)"
            Elsyne "(I should protect this secret...)"
            Elsyne "(From Ma... From Rai... or from anyone...)"
            Elsyne "(At any cost.)"

        label R3scene11:
            stop music fadeout 2.0
            play music audio.farm
            scene Farm with fade
            play nature audio.wind loop
            play hewan audio.chickens
            play hewan2 audio.cows
            play hewan3 audio.sheep

            show FRai Default
            FRai "Here we go"

            play sound audio.footsteps_grass
            show FRai Default at right with easeinleft
            show FRai Default at left with easeinright
            show FRai Default at center with easeinleft
            FRai "That's all for today"
            FRai "Ah that went faster than i expected"

            show FRai Happy
            FRai "Siiir, i'm done for today"

            show Farmer Default at left with dissolve
            Farmer "Oh? Good job boy"
            Farmer "Very well then, you're free for today"
            Farmer "Go rest up or something"

            FRai "(Heh, “Boy” huh?)"
            FRai "(So that means he didn't see me as a kid anymore?)"
            FRai "(Wow, what with the sudden changes of heart)"
            FRai "Thank you sir!"

            show FRai Thinking
            FRai "Ah, i've been meaning to ask you this sir"
            FRai "I'm planning to go out tonight, may I borrow the flashlight that's been stored in the shed?"
            Farmer"Hmm? Feel free to use it boy"
            Farmer "You've been a great help for me lately"
            Farmer "It would be hard for me to refuse, you know"
            Farmer "Oh, and may I ask where'll you go tonight?"
            Farmer "It's not like i forbid you to go anywhere"
            Farmer "But please, steer clear from the forest at night"

            show FRai Nervous
            FRai "Ah it's nothing much, i just want to look around"
            FRai "But i think i would need a lighting, just in case"

            show FRai Thinking
            FRai "(Huh? Did he just say something about the forest at night?)"

            show FRai Nervous
            FRai "A-ah, and also if you don't mind me asking sir."

            show FRai Thinking
            FRai "Why did you say to avoid the forest at night?"
            FRai "Did something happen there lately?"
            Farmer "Well, going to the forest at night generally is a bad idea boy"
            Farmer "But lately, something has been sighted there at night"
            Farmer "Someone reported they saw a figure with a lot of tentacles sprouting from their back"
            Farmer "Even if the eyewitness said that the creature doesn't seem to be dangerous because they didn't attacked the witness"
            Farmer "But it's better to be safe than sorry, you know"
            FRai "(A figure with a lot of tentacles huh...)"
            FRai "(That matched up with my report about the target)"

            show FRai Serious
            FRai "(I know I must be going in the right direction here"

            show FRai Happy
            FRai "Alright, thanks for the warning sir!"
            FRai "I'll be sure to remember that"
            Farmer "Take care boy"
            Farmer "And i think that's also all for today for me"
            Farmer "I'll be going now, goodbye"

            play sound audio.footsteps_grass
            hide Farmer Default with moveoutleft

            show FRai Serious
            FRai "Alright, I should start preparing right now"
            FRai "And maybe I'll go to the forest at around 9PM."

        label R3scene12:
            stop music fadeout 2.0
            stop nature
            stop hewan
            stop hewan2
            stop hewan3
            play music audio.forest_night
            scene Forest Night with fade
            play hewan audio.owl

            show FRai Serious
            FRai "Okay, here goes nothing"
            FRai "Luckily i still remembered my way around the forest, thanks to Elsyne"
            FRai "Let's just go for a quick patrol for now"

            show black with fade
            "After a while"
            hide black with fade

            show FRai Thinking
            FRai "(Hmm... so far there's nothing out of ordinary)"

            show FRai Nervous
            FRai "(Except for this chill though...)"
            FRai "(And this feeling of something watching you...)"
            FRai "(Maybe that was just my imagination"
            FRai "(I should just ignore that)"

            play sound audio.grass_rustling
            show FRai Surprised
            FRai "(What was that???)"
            FRai "(I swear there's something from that direction...)"
            FRai "(I should check it out)"

            show black with fade
            "Rai tried to sneak towards the direction that he believed that there's something over there"
            hide black with fade

            show FRai Default
            FRai "(This might be a good spot to hide)"
            FRai "(And fortunately, i have dimmed my flashlight)"
            Unknown "I'm sorry, little one"

            play sound audio.stab
            Unknown "(Hmm? I can feel that something... no, someone's nearby)"
            Unknown "(Urrghh... i can't pinpoint what they are)"
            Unknown "(I might have used too much of my energy today)"
            Unknown "WHO'S THERE???"

            show FRai Surprised
            FRai "(Grrk)"
            FRai "(It can speak?)"
            FRai "(No, that voice... is that?)"

            "The unknown figure approached Rai's hiding spot, but luckily, they didn't notice him..."
            "Or did they?"

            stop music fadeout 2.0
            show black with fade
            hide FRai Default
            hide black with fade


            play music audio.Elsyne

            show Elsyne Surprised2 with dissolve
            Elsyne "(There's nothing here...)"
            Elsyne "(But this feeling... it's kinda familiar...)"
            Elsyne "(...No it couldn't be???"
            Elsyne "(Him???)"
            Elsyne "Hnngh, i need to get away, fast"

            play sound audio.running
            hide Elsyne Default2 with moveoutright
            "The unknown figure suddenly fled with a blinding speed, but unfortunately, Rai already got an idea, about what is that figure"
            stop sound

            show FRai Surprised with dissolve
            FRai "(No...)"
            FRai "(My eyes didn't play a trick on me right???)"
            FRai "(That figure... and also that voice...)"
            FRai "(Is that...)"
            FRai "(Elsyne???)"

            show FRai Default
            FRai "(I should probably go back for now)"
            FRai "(Maybe tomorrow, i'm gonna confront her about it directly)"
            FRai "(For the sake of the mission...)"

            "Having his doubt somewhat confirmed, the officer decided to end his investigation and went back to the Farm."
            show black with fade

        label R3scene13:
            "After the last night's event, Rai decided to confront his suspect directly today"
            stop music fadeout 2.0
            stop hewan
            play music audio.market loop
            scene Market with fade
            show MeatButcher Default at right
            show FRai Default
            Butcher "Yo kid, so you've come again"
            Butcher "What do I need to get you this time?"
            Butcher "Any orders?"

            show FRai Nervous
            FRai "A-actually... I came here to talk to Elsyne"
            FRai "May I?"
            Butcher "You two really did become closer huh? Haha"
            Butcher "Alright then, I'll call her for you"
            Butcher "One sec"

            hide MeatButcher with moveoutright
            show FRai Default at left with easeinright
            show Elsyne Default at center with easeinright
            show MeatButcher Default at right with easeinright

            stop music fadeout 2.0
            play music audio.Elsyne
            Butcher "There she is, I'll leave you two on your own now"

            hide MeatButcher with moveoutright
            Elsyne "What?"

            show FRai Nervous
            FRai "I wanna ask about something..."
            FRai "Last night, did you-"

            show Elsyne Sad
            Elsyne "Enough"
            Elsyne "So that was really you huh?"

            FRai "Y-yes..."
            Elsyne "So be it then"
            Elsyne "Fine, I'll tell you everything later"
            Elsyne "Meet me at the waterfall tonight, and before then, get outta my face"
            FRai "H-huh, A...alright"
            Elsyne "Now go."
            Elsyne "Get out"

        label R3scene14:
            stop music fadeout 2.0
            play music audio.Elsyne
            scene waterfallNight with fade
            play nature waterfall_loop loop

            show Elsyne Default2 at left
            #From here on Elsyne gonna be on her Eldritch form, unless stated otherwise

            "As Rai went toward the meeting spot, he could see a shadowy figure waiting for him. The exact same figure that he saw on the forest last night"
            show FRai Nervous at right with dissolve
            Rai "I...I'm here"
            Elsyne "So you've come huh"

            show Elsyne Default2 at center with easeinleft
            "The figure came closer"

            show CG6 with fade
            $ persistent.cg6_unlocked = True

            Elsyne Smile2 "You've seen everything"
            Elsyne "This is who i really am"
            Elsyne "Let me guess, you were sent here to go after me, no?"
            FRai Serious "To tell you the truth... Yes"
            FRai "I'm officer Rai Galilei of the Interdimensional Police"
            FRai "I was sent here to detain, and bring you to the IPD"
            Elsyne "So that means you have prepared for the worst possible outcome huh?"
            FRai "What are you talking about"
            Elsyne "I.... I'm not going down without a fight"
            Elsyne "Did you expect for me to just get caught obediently?"
            FRai Sad "N...No"
            FRai "But if possible, i want you to give yourself in"
            FRai "I don't wish to hurt you"
            Elsyne "Hmph"
            Elsyne "(Me too, Rai)"
            Elsyne Sad2 "(Me too, Rai)"
            Elsyne "(I also didn't wish to hurt you)"
            Elsyne "But is there really another way?"
            Elsyne Angry "HERE I COME, PREPARE YOURSELF"
            FRai Serious "Tch, so we're doing this the hard way?"
            Rai "Fine then, you left me with no choice"

            "Rai loaded up his gun"

            hide CG6 with fade
            scene waterfallNightRed

            show Elsyne Angry
            show FRai Default at right
            play sound audio.kick
            Elsyne "RRAAAGH" with vpunch

            show FRai Surprised at left with easeinright
            "Elsyne extended her tentacles quickly at Rai, but the officer, with his great reflexes, dodged it in time"

            FRai "Whoa!"

            show FRai Serious
            FRai "(Those tentacles are blindingly fast)"
            FRai "(I should really avoid getting struck by those)"

            play sound audio.gun_loading
            FRai "(i'll be sure to avoid her vitals)"
            FRai "(Maybe I should aim for the tentacles?)"

            "Rai took aim at Elsyne"

            Elsyne "Hm?"
            Elsyne "Oh no you don't"
            Elsyne "Freeze!" with vpunch

            "The eyes on her tentacles suddenly glows up"
            "And after that, an odd psychic wave reverberated through the area"

            show FRai Annoyed
            FRai "(Urrk)"
            FRai "(What's... happening)"
            FRai "(I can't... move)"

            show Elsyne Smile2
            Elsyne "Feel it..."
            Elsyne "The terror that's crawling in your skin"
            FRai "(I can't... fail here)"
            FRai "(I must shake it off, no matter what)"

            "Even after immobilized by Elsyne's power, Rai continued to try to break free"
            "And eventually, he succeed"

            FRai "GAH" with hpunch

            scene waterfallNight
            show Elsyne Default2
            show FRai Serious at left
            FRai "Haah..."
            FRai "Finally... I broke free"

            "Once again, the officer took aim at the eldritch"

            show Elsyne Surprised2
            Elsyne "Oh"
            Elsyne "Amazing"
            Elsyne "You dispelled the effect of my power"

            play sound audio.gun_shot
            "Rai fired his shot"
            "And it hit, that shot snapped one of her tentacles, more than he hoped for"

            FRai "Haah.. haah.."
            FRai "(Did I go too far)"
            FRai "(But that shouldn't be fatal)"

            show Elsyne Angry
            Elsyne "Hmm?"

            "The tentacles regenerated"

            show FRai Surprised
            FRai "(What???)"
            FRai "(It can regenerate???)"

            show Elsyne Smile2
            Elsyne "I'm afraid that's not gonna work"
            Elsyne "Are you hesitating?"

            show Elsyne Sad2
            Elsyne "(I knew he also didn't want to land a fatal blow)"
            Elsyne "(I'll just scare him for a little)"
            show FRai Sad
            FRai "I... Can't..."

            show Elsyne Angry
            play sound audio.kick
            Elsyne "Hmmph" with vpunch

            show FRai Default at right with easeinleft
            show FRai Default at left with easeinright
            "Elsyne answered back with flurry of blows from her, but just as before, rai managed to dodge every single one of them"


        label R3scene14_1:
            scene waterfallNight with fade
            show Elsyne Default2
            show FRai Annoyed at left
            FRai "(If this keeps up, i don't think my stamina could last for a little longer)"
            FRai "(What should i do?)"

        menu:
            "Charge at her":
                jump R3scene14_1_a

            "Keep dodging":
                jump R3scene14_1_b

        label R3scene14_1_a:
            # Bad End

            show FRai Annoyed
            FRai "(I can't keep this up)"
            FRai "(I should take on the offensive)"

            show FRai Serious at center with easeinleft
            FRai "Rrraaahhh" with vpunch
            show FRai Serious at left with easeinright

            "Rai charged at her recklessly"

            show Elsyne Surprised2
            Elsyne "(Huh?)"
            Elsyne "(Did he lost it already)"
            Elsyne "(Fine then, i'll just put him to sleep)"
            FRai "SURRENDER NOW, ELSYNEEE"
            with vpunch
            play sound audio.stab
            "One of Elsyne's tentacle stabbed Rai's leg, lightly"

            show FRai Surprised
            FRai "(!!!)"
            FRai "(What's this...)"

            show Elsyne Sad2
            Elsyne "I'm sorry, Rai."

            show FRai Annoyed
            FRai "(Uhh...)"
            FRai "(My consciousness is fading out.)"
            Elsyne "So it ends here..."
            Elsyne "Don't worry, that wasn't lethal"
            Elsyne "You will faint for a while"
            Elsyne "But it'll be fine"

            show FRai Sad
            FRai "El... syne."
            Elsyne "Thanks for everything Rai"
            Elsyne "But it was time for me to go"
            Elsyne "I'm sorry... But please..."
            Elsyne "Please forget everything about me"
            Elsyne "I'll be leaving the Farmland for now"
            Elsyne "Don't go look out for me..."
            Elsyne "Until we meet again..."
            
            hide Elsyne Default2 with dissolve
            show black with dissolve

            "Afterward, Elsyne escaped the scene, and Rai, having failed his mission, went back to the IPD empty handed..."
            "Except for the memories that he made in the Farmland."
            "And you know, one shall change their action. Not everyone have those privilege of having second chance - But you - You have thos"


        menu:
            "Rewind the time":
                jump R3scene14_1

        label R3scene14_1_b:
            # Goo end

            show FRai Sad
            FRai "(No... I don't want to hurt her...)"

            show FRai Serious
            FRai "(I'll just keep looking for an opening.)"
            FRai "(There must be some.)"

            show Elsyne Surprised2
            Elsyne "(Huh, he's not going to attack again at all...)"

            show Elsyne Angry at left with easeinright
            Elsyne "TAKE THIS!" with vpunch

            "Elsyne approached Rai suddenly, trying to struck him from point blank range"

            show FRai Surprised
            FRai "Ah!!"
            show Elsyne Angry at center with easeinleft
            "But suddenly, she stopped. Rai was already covering his head with his hands, he was prepared."

            show Elsyne Sad2
            Elsyne "This isn't right."
            Elsyne "I.. don't want to hurt you... Not again.."

            # SPRITE ELSYNE RETURN TO HUMAN FORM
            # hide Elsyne Sad2 with dissolve

            show Elsyne Sad with dissolve
            Elsyne "That's it"
            Elsyne "I... Surrender"
            Elsyne "Let's just end this, shall we?"

            show FRai Surprised
            FRai "Huh?"
            Elsyne "I know that from the beginning, you didn't mean to land a fatal blow, did you?"
            Elsyne "It was the same for me"
            Elsyne "I... I can't bear to hurt someone who cares for me."

            show Elsyne Smile
            Elsyne "Even though we just barely met, you've shown me kindness..."
            Elsyne "You made me feel this happiness..."

            show Elsyne Sad
            Elsyne "I'm tired with all of this..."
            Elsyne "All I ever wanted was to live a peaceful life."
            Elsyne "Living like a normal girl."
            Elsyne "But I've accepted everything"
            Elsyne "I know I was a terrible person"
            Elsyne "Someone who took a lot of life... I don't deserve that kind of life after everything that i've done"
            Elsyne "And so, I'll turn myself in"
            Elsyne "I'm prepared for the consequences"
            Elsyne "I know that sooner or later there'll be someone that will come for me"

            show Elsyne Smile
            Elsyne "But I'm glad... I met you..."
            Elsyne "You gave me the chance to make me feel what I wanted to experience..."
            Elsyne "So once again... Thank You."

            show FRai Sad
            FRai "Don't be like that"
            FRai "I know, what you've been doing was not from your own will"
            FRai "In this case, you're just a victim"
            FRai "But you remembered what I said right? Everyone has the right to receive kindness and feel happiness, even if it's someone like you."
            FRai "Furthermore, I know you didn't have that kind of malice inside."
            FRai "Even if the things that you did can't be undone, you can still try to prevent those from happening again."
            Elsyne "Uh-huh."
            Elsyne "Thanks."
            FRai "I promise, the IPD will treat you well."
            FRai "I swear."
            Elsyne "Alright..."

            show FRai Default
            FRai "Before we leave, would you like to go back home for one more time?"
            Elsyne "Nope, I'm fine"
            Elsyne "I've left my farewell letter to Ma at home"
            Elsyne "She should find it later"
            FRai "Well then, if that's your wish"
            FRai "Oh and one more thing, I see that you've  been holding on to something strange for a while."
            Elsyne "Ah, this?"
            Elsyne "I don't remember where i got it, but yes, i've been holding on to it since then"
            FRai "May I have it?"
            Elsyne "Sure, here you go"
            FRai "Thanks"
            FRai "Alright then"
            FRai "Since we're done here, let's go to the IPD now"
            Elsyne "Uh-huh."

            "And so, Rai have successfully completed his mission, and furthermore, he has resolved things peacefully"
            "And thus, his adventure comes to an end."
            "Until he opens what Elsyne gave him.."

            stop music
            stop nature

            $ persistent.k3_caught = True

            show black with fade
            pause(2.0)

            show CG12 with fade
            $ persistent.cg12_unlocked = True
            pause(10.0)
            show black with fade
            pause(5.0)

            jump ending


    label ending:
    if persistent.k2_caught and persistent.k3_caught:
        $ persistent.phase1 = False
        $ persistent.phase2 = False
        $ persistent.phase3 = True

    return
