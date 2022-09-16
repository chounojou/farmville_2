label phase2:

    scene IPD WORKSHOP

    "It’s a bright and sunny day at the Interdimensional Police Department or IPD for short."
    "The sunlight is shining through the windows today."
    "A perfect day to go outside and lay down on a sandy beach with a friend or two but not for Rai Galilei."
    "He’s one of the busy officers from IPD."

    "Today is like any of his work days, a lot of new paperworks awaits Rai in his office, which he happily accepts as it is." 
    "Waking up and walking to his office like normal. Accompanied by the usual chit-chatter with colleagues."
    "Rai finally reached his office desk. It doesn’t look like one at the moment as it is covered by mountains of paperwork. He lets out a big stretch. And it’s time for him to do his work."

    "Before sitting down on his desk, he grabs a can of cola and cracks it open."
    "His number one favorite drink to accompany him through all the paperwork of the day."
    "He takes a sip as he sits down on his chair."

    show rai_default

    Rai "Ah.. another day with my wife, Shigoto-san."
    Rai "Hmm, let's see what I have to do today."

    Rai "Man… It’s just the beginning of the day yet someone has already put this much paper here."
    
    Rai "I can’t work properly if my table is full of papers."
    
    Rai "I need to tidy it up a bit, I think I should put some of the papers in the drawer for the meantime."
    
    "While Rai was tidying up the papers that were on his desk, one of his Galilean coworkers came by his table."

    show rai_default at left with easeinleft
    show galilean_default at right with easeinright

    Galilean_1 "Good morning! Sorry to disturb you so early in the morning…"
    Rai "Oh! Good morning!"
    Rai "It’s okay. Is there something that I could help you with?"
    Galilean_1 "Ah yes, I’m just here to remind you about the meeting that we will be holding in a bit." 
    Galilean_1 "Please don’t forget to bring the necessary files for it!"
    Rai "Thank you for the reminder. I’ll get it ready."
    Galilean_1 "Okay then, I shall excuse myself now. Have a good day!"

    hide rai_default with dissolve
    hide galilean_default with dissolve 

    "As Rai gets back on his chair, he sees a post-it-note reminder on his PC screen to help fix the CCTV."
    "He can help fix the CCTV first, or attend the meeting first, or he can just ignore all of that and tidy up the files in his drawers."

    "Which one will he do?"
    menu:
        "Tidy File":
            jump scene1_intro

        "Fix CCTV":
            jump scene2_intro

        "Attend Meeting":
            jump scene3_intro

    label scene1_intro:
        scene IPD_WORKPLACE
        show rai_confused

        Rai "Wait, what…?"

        "It was surprisingly tidy."
        "There are only a few cases that will make Rai have the intention to tidy up his work drawer. The first one is if it was untidy."
        "And the second one is if there were several important papers that seemed to look stuck or tucked between a pile of folders in his work drawer."
        "If that was the case then he would have no choice but to look for it fearing that it would get buried."
        "What was miraculous and magical about it is that even though he was prone to be forgetful, it was as neat as if he had just recently tidied it."

        show rai_shocked
        Rai "When did I… tidy it up? Kinda forgot really."

        "What's going on today? Is the Rai Galilei starting to experience senility or fatigue from work so much that his mind is forced to forget the activities that he did yesterday or maybe even more recent than that?"
        "Who knows."
        "But for Rai this seems like a plus for him since it’s already clean. He can just put the papers that’s currently in his hands easily."

        show rai_default
        Rai "Maybe it’s one of my coworkers. Oh well, time to get back to Shigoto-san."

        hide rai_default with dissolve

    menu:
        "Tidy File":
            jump scene1_intro

        "Fix CCTV":
            jump scene2_intro

        "Attend Meeting":
            jump scene3_intro
    
    label scene2_intro:
        scene CCTV_ROOM
        # SFX Knock

        show galilean_default
        Galilean_2 "Uhh sir? Forgive me for the intrusion, but I’m here to give you this. It's from the CCTV Operator Guy. He says to give it to you."

        show rai_default
        Rai "Oh, okay. Just put it on the table, thank you."
        Galilean_2 "Then, I'll excuse myself."
        hide galilean_default with dissolve

        "After they left, Rai read the paper."
        "Need help in the CCTV Room -Artemisia"

        Rai "My god, I thought it’s a prank. Damn you Artemisia."

        "Rai laughs as he folds the paper neatly and walks towards the CCTV Room."

        # SFX Footstep
        # Black Screen

        scene CCTV_ROOM

        show artemisia_default
        Artemisia "Welcome sir, sorry to summon you with a piece of paper."

        show rai_happy
        Rai "Ah, you mean this?"

        "Rai shows the paper that has already been folded into a shuriken-shaped. He throws the shuriken across the room, making it fly and it returns neatly into his hand."

        Artemisia "Ohmagah, Milord… Ahem- I mean. Such a talent to neatly fold an origami and to make it fly like that."
        Rai "Oh don't flatter me, also this… origami thing you said? I learned it from the Youtube video you gave during my expedition in the Far East Dimension."

        show rai_serious
        Rai "Anyway, what seems to be the problem regarding the CCTV?"
        Artemisia "Right. As I said from the message, there seems to be a problem with some of the CCTVs in certain spots. We’ve been dealing with some sort of signal lost sometimes"

        "Artemisia shows a monitor with IPD camera layout."

        show rai_thinking
        Rai "Hmm, the spots are odd. Just around the jail corridors."
        Artemisia "What do you mean sir?"

        show rai_serious
        Rai "CCTVs placements that are broken are too odd, as if it was done on purpose to create a blind spot. Maybe it’s just me though."
        Artemisia "I see. How observant of you sir."

        show rai_excited
        Rai "Aww hehe, I’ve been working here for so long that I feel like IPD is an extension of my body. So, where do I start?"
        Artemisia "Yes sir. So--"

        "Before Artemisia could finish their sentence, someone came running into the room."

        show galilean_default
        Galilean_2 "Sorry for the intrusion sir, but there’s an emergency meeting!"
        Artemisia "What happened?"
        Galilean_2 "We caught an inmate that tried to break out of  jail. We believe that someone outside of our premises tried to help him, but he wouldn't open his mouth."
        Rai "Sorry Artemisia. It’s an emergency. I’ll see you soon."
        Artemisia "Roger sir. Good luck."

        # Black Screen

        jump scene3_intro
    
    label scene3_intro:
        scene MEETING_ROOM
        show rai_serious

        Rai "Felix Lynx,huh?"

        "Rai said to himself as he flipped over to the next paper about the inmate."

        Rai "Crime Record: Illegal Dimension Hopper, 2nd Degree Interdimensional Murder. Fitting for a cat."

        "As he examines and searches the database for the inmate, his background, family connection, relation to other criminals. Something immediately clicks."

        show rai_shocked
        Rai "But really, why does he seem familiar… Ah right, this kusogaki."

        show rai_annoyed
        Rai "He’s the one that ate the fish that I just bought during my trip in the Quantal World. That glutton!"

        "Skimming the profile once more, he makes sure to not let this case miss again."

        Rai "So, not getting tired of getting caught again?"

        "Rai asked his colleagues to leave them alone and shut the door, making him and the Cat Guy have a proper talk."

        show felix_default
        Felix "Speak for yourself, yellow bratty. I won't spill much."
        Rai "Well I won't ask much. But again, trying to catch some fish"
        Felix "That again? HAHAHAHAHA, YELLOW SHORTIE, guess you drank too much cola. I will repeat and speak for it again. It is because I can."

        "Rai's emotion set bar almost snapped from the nickname he just got."

        Artemisia "Sir Rai, we need help. Something weird is happening."

        show rai_surprised 
        Rai "I’m in the middle of something. Show me through the monitor.."

        "The small TV at the corner of the room suddenly flashed with a bright light then a static video showed. Not long after that, it’s back to normal and shows some bent CCTV cameras."

        show felix_annoyed
        Felix "Damn, that looks bad."

        show felix_serious
        Felix "Must be those two stupi–"

        show rai_surprised
        Rai "..What did you just say?"

        show rai_happy
        Rai "Ah…"
        Rai "I see!"
        Felix "What are you talking about man?! Get away from me!"

        show rai_excited
        Rai "Well thanks to you, I know there is someone who is trying to mess up the surveillance just now. I don't need you anymore…"

        show rai_default
        Rai "Contacting IPD, Team Galileian, Team Artemisia, escort this inmate back to his jail. I'm done with him. Retrieve the Inmates Collar from him and send me the data after jailing him. Moving to the CCTV room ASAP."
        Artemisia "Aye aye Sir."
        Rai "Now checking the cameras."

        "Rai sees the weirdly ‘bent’ CCTV camera. He runs towards the main room to consult the Galileian officer there."

        show rai_serious
        Rai "I got the report that our CCTV is weirdly shaped. Fast Report, ASAP."
        Galilean_2 "Yes sir. As you can see, our signal was disrupted just before the camera bent, and now it seems like it was crushed by something. While we’re here, this is the record from the CCTV before it was ‘bent’."
        
        "Rai checks the camera and notices the way the camera ‘bent’."

        show rai_surprised
        Rai "THERE!"

        show rai rai_serious
        Rai "For some millisecond, there’s a long, flexible and a very fast moving object that hit the cameras"
        Rai "Did someone managed to breach into IPD?!"
        Galilean "Err, as far as i know, it’s just the janitor that passed by those corridors"

        show rai_concern
        Rai "Okay then, give me the copy to this stick drive. I might need it for the latest investigation."
        Galilean "Okay sir"

        "As he passes him the stick drive, Rai is still wondering who the other culprit is."
        "After a minute passed."

        Galilean "Here’s the data that you need sir."

        "One finished in no time.  His communicator rings."

        Artemisia "Artemisia to Galilei."

        show rai_serious
        Rai "Galilei here."
        Artemisia "We just extracted the data for the inmates you asked, where should we send it?"
        Rai "Oh, it's already extracted? Send it to the database."
        Artemisia "Understood sir. We will process the data then. Artemisia out."

        "Rai then walked toward his room to continue his search and to deduce the identity of the cat’s accomplice."
        "Watching the latest sound recording of the jailbreak from Felix’s collar, Rai learns the inmate’s behavior."
        "He slowly crafts his theories and analyzes the hypothesis about how he managed to attempt a jailbreak."
        "During the middle of the video, Rai suddenly pauses the record and plays it backwards."

        show rai_thinking
        Rai "Wait…"

        "The inmate seems to be mumbling something."
        "He continued to learn about the inmate for this case."

        Rai "Hmm.. For now this will be the only information that I have…"

        "He examines and tries to make out something from the mumbling."

        Rai "Farmland?"
        Rai "He said something like going to a place called Farmland?"

        show rai_serious
        Rai "All is connected…"

        "A fiery ambition flickers in his eyes, a flame that never goes down as long as the criminals are roaming around."
        "Rai runs as fast as he can towards his office to pack his things and head towards Farmland Dimension."

        "Which criminal will he catch?"

    menu:
        "MIRA'S route":
            jump route2

        "Elsyne's Route":
            jump route3

    label route2:
        label scene1:
            scene FARM
            "A place dominated by a combination of green and brown. Cool air blows all over the place. Sounds from nature—be it the sounds of the animals or the rustle of leaves—fill the ears."
            "A boy—or a man?—stands in the middle of a meadow."
            "He looks around carefully. Researching every corner he can reach calmly..."
            "Until someone comes near him. He greets the boy."

            show farmer_default
            Farmer "Hello, boy!"

            "The boy turns slowly. He smiles politely."

            show rai_happy
            Rai "Hello, Sir!"
            Farmer "What are you doing here, young boy?"

            show rai_surprised
            Rai "Uh-uh, for a job!"

            # Ting! (kayak bunyi ada ide gitu)

            Farmer "Oh, you're the new kid who's going to work here, aren't you?"

            show rai_default
            Rai "But I am not kid tho..."
            Farmer "Welcome! Thank you for coming all the way here."

            show rai_happy
            Rai "No worries!"

            show rai_default
            Rai "It’s for my mission, too."
            Farmer "Please prepare yourself and come to see me again."

            show rai_happy
            Rai "Okay!"

            "Rai turns around and leaves the farmer behind."
            "He looks at his surroundings, making sure of the situation according to the information he got in the base."
            "He recalls that report."

            show rai_serious
            Rai "IPD is not a place that would commit such a mistake.” • Looking peaceful as it is, there's still must be something."
            
            "Rai signs and shrugs his shoulders."
            "He knows that not much can be done with the lack of information."
            "That's why he's here, anyway. It won’t walk on by itself."

            show rai_excited
            Rai "Let's get ready!"

            "After Rai prepares himself, he returns to meet the farmer at the same location."

            Farmer "Are you ready, young man?"
            Rai "Ready anytime, Sir!"

        label scene1_1:
            Farmer "A fiery spirit, apparently." 
            Farmer "Okay. There's some work you need to do." 
            Farmer "What kind of work are you going to do, huh?"

        menu:
            "Something simple, maybe…?":
                jump scene1_1_a

            "Whatever is needed now, Sir.":
                jump scene1_1_b

        label scene1_1_a:
            Farmer "Simple, huh?"
            Farmer "You are the type who wants to do the easiest, huh? Even though you're still young, you still have a lot of energy, you know."

            "Rai just laughs awkwardly."

            jump scene1_2

        label scene1_1_b:
            Farmer "Hahaha!"
            Farmer "Such a determined person! Good to hear."
            
            show rai_default
            Rai "Glad to be helped."

            jump scene1_2

        label scene1_2:
            Farmer "Great. Now we can move on to your first job."
            Farmer "Here, take this."

            "The Farmer gives small old paper. It was a small map containing the places on the farm."
            "Rai flipped the paper."
            "On the other side, there is a list."

            Farmer "Go to the shed."
            
            "He pointed to the paper given to Rai."

            Farmer "You can check the list of jobs listed there."
            Farmer "Good luck!"

            "He smiles."
            "Rai bows to The Farmer and leaves immediately."
            "Rai checks the paper again. He tries to remember all the jobs."

            show rai_thinking
            Rai "Shed, huh? There must be a lot of stuff in there."

            show rai_serious
            Rai "There must be a lot… {i}something.{/i}"

            "As this one policeman had already pointed out, there were indeed a lot of things in that place."
            "A huge amount."

        label scene2:
            scene Shed
            # Bunyi pintu dibuka

            "Rai finally arrives at the shed and looks around. Nothing much."
            "…cause it's too much."

            show rai_surprised
            Rai "Whoa—look at here."

            show rai_nervous
            Rai "Very {i}neat.{/i} Ha ha."

            # Suara kertas
            "Rai checks upon the jobs list. One of them is arranging farming equipment."
            "Not a difficult job, actually. It just needs patience and energy."

            #suara barang-barang dikumpulin. klutuk klutuk gitu
            "Rai starts picking stuff up near his feet." 
            "There's no point in thinking all the time doing nothing."

            show rai_default
            Rai "Just get over it"
            Rai "Well, where should I store all this?"

            "Rai looks to his right."
            "He sees a wooden shelf glued to the wall."

            # Ting!

            Rai "Maybe it’s there, yes."
            
            #Suara langkah sambil bawa barang gitu
            "Rai approached the shelf while carrying the items."
            "He put the things on the shelf."

            #Tak tak tak! Bunyi barang ditaruh
            Rai "Let's see. This one over here, then this one over here..."

            "Rai began to arrange the items."
            "He pushes the items that were previously on the shelf to the edge of the shelf."
            "At that time..."

            # Bunyi benda jatuh
            show rai_surprised
            Rai "Oh? What is this?"

            "Something fell."
            "It is the size of a fist."
            "Rai tries to pick it up. Quite surprised by the weight that slightly exceeds his expectations."

            # Antenna like object - a part of comm device

            show rai_thinking
            Rai "It's a tool for winding a well's bucket rope, isn't it?"

            "Rai flips it over to observe it. He tries to imagine operating the device."

        label scene2_1:
            show rai_thinking
            Rai "But based on the times that exist in this timeline, it shouldn't be this sophisticated. How did it get here?"

        menu:
            "Save it.":
                jump scene2_1_a

            "Ignore it.":
                jump scene2_1_b

        label scene2_1_a:
            show rai_serious
            Rai "Looks like this could be an evidence. I have to keep this up. I'll ask the farmer as well."

            "Rai stores it in an inaccessible place in the shed. If it's related to the farm, he doesn't think he can take it for granted."

            jump scene2_2

        label scene2_1_b:
            show rai_thinking
            Rai "Looks like the farmer has good connections. It’s possible for him to have something like this. Maybe I should ask him later."

            "Rai puts it back on the shelf. He made sure it won’t fall again."

            jump scene2_2

        label scene2_2:
            show rai_excited
            Rai "Alright, let's continue again!"

            "Rai returns to pick up the scattered items."
            "He arranges the items by function in each place on the farm as he had seen the entire contents of the map."
            "Maybe that way, it can help farmers take things as needed."

            #Suara langkah sambil bawa barang gitu, bunyi barang ditaruh
            "After fully filling the shelf on the right, he moved to the shelf on the left."
            "He picks up another item that was on the floor and carries it over to the shelf. He arranges the same as the previous shelf."

            show rai_default
            Rai "This thing here, and this thing there..."

            #Tuk! or Tak! bunyi barang kecil kepentok 1x
            "Again, something caught his attention."
            "Something hit the back of Rai's hand."
            "It was a small object shaped like a ring."
            "Rai takes it."

            show rai_thinking
            Rai "Hmm? Is this one of the farm's belongings? I don't think so."

            "He wondered why on his first day such a strange thing had happened."
            "Yeah, it's actually normal considering he's also been on a mission and something unusual happens everyday even to ordinary people."
            "Like... Casually eating sand for example."
            "Back to topic."
            "Rai checks the thing."

            #Ring like object - a part of comm device
            "It is a circle with a hole in the middle."
            "There are some sort of four patterns or lines on the edges."
            "If this is called a ring, it doesn't seem like it's because it doesn't have volume, aka a flat object. It's like a coin with a hole."

            Rai "What part does this thing need on the farm, huh? Hmm...."

            "Rai thinks aloud and remembers things that are roughly on the farm."

            show rai_annoyed
            Rai "There's no use. I can't remember."

        label scene2_3:
            "Rai looks at the object carefully."

            show rai_thinking
            Rai "What should I do?"

        menu:
            "Check the shed.":
                jump scene2_3_a

            "Keep it.":
                jump scene2_4

        label scene2_3_a:
            show rai_serious
            Rai "There might be something that fits this thing. I have to find it."

            "Rai searches in the shed."
            "He checks the items there one by one, with nothing left behind. Search it from left to right, bottom to top."
            "He even goes up to the pile of wooden boxes there."

            #bunyi box jatuh
            "And of course, falls {i}gracefully.{/i}"

            show rai_nervous
            Rai "Aeugh...."

            show rai_default
            Rai "At least I'm still alive..."

            "Rai is speechless. He knows it was his fault."

            show rai_serious
            Rai "I shouldn't be in a hurry. There’s still time."

            "Rai gets up and brushes the dust off his clothes."

            show rai_happy
            Rai "Whatever happens, happen!"

            jump scene2_4

        label scene2_4:
            #Ring object
            "Rai sees the object in his hand."

            show rai_serious
            Rai "I'd better save this for now."

            "Rai keeps it in his pocket."
            "Rai piles back the scattered boxes that he had previously stepped on."

            show rai_default
            Rai "Surely no one noticed. {b}Definitely.{/b}"

            "Rai looks around."
            "Everything looks better than before. Farm items are neatly arranged."

            Rai "One job done."

            show rai_happy
            Rai "Now onto the next job!"

            "Rai rechecks the list of jobs he held. He marks the work as completed."
            "He looks at the sentence listed in the next assignment."

            show rai_thinking
            Rai "Complete the inventory, huh?"
            Rai "I've already checked the items that I think need to be replaced anyway."

            "Rai writes a list of all the items to be purchased. He also rechecks all the items as needed."
            "After all is done, he stares at the list."

            show rai_happy
            Rai "I think it's time to see the farmer."
            Rai "Even if I have money, it seems strange to go shopping without asking."

            "Rai pockets his notepad."

            show rai_excited
            Rai "Okay, let's gooo!!"

        label scene2_5:
            scene In front of the farm

            show farmer_default
            "Rai leaves the shed and goes to meet the farmer."
            "Not long after, he sees the farmer from a distance. The Farmer is in the middle of something."

            show rai_default
            Rai "Hey, sir!"

            "The farmer stops his activity. He looks up and smiles."

            Farmer "Are you done?"

            "Rai approaches the farmer. He shows the paper that the farmer had given him earlier."

            show rai_excited
            Rai "Already for the first part!"
            Farmer "Good work."

            "He patted Rai's shoulder."

            Farmer "Now which one do you want to do?"

            show rai_happy
            Rai "I want to go shopping for equipment first. There are a few things to buy as there are items that don't look like they can be used anymore."
            Farmer "I see. Wait a sec..."

            "The farmer reaches for his trouser pocket. He takes some money out."

            Farmer "Here’s the money." 
            Farmer "Make sure to buy what you need. If it's not enough, just come back and buy some more, okay?"

            show rai_excited
            Rai "Okaayy!"
            Rai "I'll be right back."
            Farmer "Be careful, okay. Bring it in a little bit."

            show rai_happy
            Rai "Yes, sir!"

            #SFX Footstep
            "Rai waves to the farmer as he leaves. Rai puts the money and the shopping list into the bag."
            "Once he finishes organizing, he looks back at the map and heads straight for the village."

        label scene3:
            scene village
            #SFX suara keramaian
            "Finally Rai arrives at the village."
            "He sees the hustle and bustle of the village people who were busy passing here and there to get to their destination."
            "Rai tries to avoid the crowds by walking on the side of the road. He leans against the wall to find a gap in the busy street."

            show rai_nervous
            Rai "Maybe this isn't the right time."

            "Rai struggles through those people."
            "It’s understandable that a place like this is indeed packed with crowds because it is close to the marketplace."
            "He makes it through the crowded place after some time."

            Rai "Finally... I'm out..."

            "Rai pants after struggling through all the obstacles that exist."
            "Okay, that's an exaggeration."
            "In short, he returns to his consciousness to go to his destination, the market."
            "As said before, this place is indeed full of people."

            #kesenggol bahunya
            "Rai bumbles with someone."

            show villager_default
            Villager "Hey! Walk with your eyes open, Kid. Be careful."

            show rai_surprised
            Rai "Uh oh- I'm sorry!"
            Villager "Oh? Are you a newcomer?"

            "Rai who previously looked down, meets the person's eyes."
            "Looks like she's a villager here."

            show rai_nervous
            Rai "...right, I'm new here."
            Villager "Ah..."
            Villager "By the way, what is a young fellow like you doing here?"

            show rai_default
            Rai "Oh, about that..."

            "Rai says that he needs to buy farm equipment. Therefore, he had to go to the market."

            Villager "Market, huh? You're going in the right direction."

            "Of course, he brings a map too. Though he won't say that."

            Villager "Usually the farmer will go to the market. Is he busy?"

            show rai_happy
            Rai "I think so. So I want to help."
            Villager "Why?"

            show rai_default
            Rai "I'm an intern there."
            Villager "Aaah~ That's why you did it huh. It's part of your job."

            "Rai nods in agreement."

            Villager "Then, since I'm going there too, how about we go together?"


            show rai_happy
            Rai "Yeah, sure!"

            show seller
            Seller "Hey!!"

            show rai_surprised
            Rai "Waaahhh!!"

            "Someone shouted right behind Rai."

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

            show rai_excited
            Rai "Hello, my name is Rai, I’m new here!"
            Seller "Welcome, Boy!"

            show rai_happy
            Rai "Thank you."

            "They shake hands."

            Villager "Anyway, let's go to the market."

            "They walk together towards the market."
            "The villager and seller tell stories about the village and the people who live here. They also tell him about some places around it."

            scene Market
            "After walking quite a distance, they arrived at the place where the seller will be selling his stuff."
            Seller "Then I'll prepare first, okay?"

            show rai_happy
            Rai "Let me help you!"
            
            "Like a good kid he is, Rai helps the salesman line up his wares."
            "He lined up each fruit and vegetable and grouped them."

            Seller "By the way, where's {i}the kid{/i}?"
            Villager "Come to think of it, that's true. Where's {i}the kid{/i}?"

            show rai_thinking
            Rai "Other kid?"

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
            Seller "I haven’t seen anyone coming for her, I don't think she has any family or relatives here."
            Villager "Yeah, maybe that's why."

            jump scene3_2

        label scene3_1_b:
            Villager "That's right. I hope she will be found soon."

            jump scene3_2

        label scene3_2:
            Seller "We've actually been looking for her around the village."
            Seller "It might be possible though that she already met her family who are outside the village."
            Villager "Yes, who doesn’t treasure such a lovely child like her."
            Seller "She looks very cheerful, doesn't she?"
            Villager "Though she's a little weird, haha."

            "Rai raises an eyebrow."
            
            show rai_thinking
            Rai "What do you mean by ‘weird’?"
            Seller "She... she tried.. a way too hard to blend in, you know."
            Seller "She doesn't look like most people, but she always insists that she's the same as everyone else even though no one mentioned that she’s not."
            Villager "She doesn't have to do that though. We'll definitely respond to her like everyone else."
            Seller "Yeah, she's too much."
            Seller "But that makes her cute."

            "Personality, demeanor, appearance."
            "Rai tries to process all the information he got. As if trying to connect the dots, he tries to arrange them in his head."
            "Maybe he should write it down after he went home from the market."

            Seller "So, boy. What do you want to buy?"

            "Rai immediately takes out his shopping list."

            show rai_happy
            Rai "Oh! I want to buy this and this. Then..."
            
            "Rai points and reads the list listed. He buys quite a lot."
            "After putting all the groceries in a plastic bag, Rai pays the seller some money."

            Seller "Thank you."
            Seller "Don't forget to stop by again."
            Villager "If there's anything you want to ask, just come over. We'll try to help too."
            
            Rai "I'm happy to ask."
            
            show rai_excited
            Rai "Thank you for helping me."
            Rai "Also for giving me some information."

            "After saying goodbye, Rai heads to the next place."
            "He goes to a place where people were selling farm equipment. He walks deeper into the market."

        label scene4:
            scene Market
            #SFX Suara keramaian

            "The noise of the crowd can be heard everywhere. He looks left and right to make sure he didn't go past where he planned to go."
            "Until finally, he hears a voice that caught his attention."
            "It is the merchant."
            "Rai approaches the merchant. The person noticed him and immediately greets him."

            show merchant_default
            Merchant "Hello, boy."
            Merchant "Is there anything that you need?"

            show rai_thinking
            Rai "Hello, uhmm.. {i}Sir{/i}...?"

            "Rai doubts about how to address this person. He guessed from this person's stature that he was a man. In addition, his voice is quite heavy."

            show rai_nervous
            Rai "Uhm, I'm here looking for stuff."

            "Rai takes out his shopping list."

            show rai_default
            Rai "This."
            Merchant "Can't you just read it straight away?"
            
            "Rai, who had wanted to give a list, immediately pulls it back."

            show rai_nervous
            Rai "It's not like that. Maybe you'd like to check it out in person."
            Merchant "Say it."
            Rai "Uh oh..."

            "The man immediately waved his hand and sighed."

            Merchant "Don't be so nervous."
            Merchant "I just... want you to mention the items you're looking for while I'm looking for them."

            "Rai nods."

            show rai_default
            Rai "I need a shovel and a hoe."

            "The merchant began to move to find the items."

            Merchant "Then?"
            
            "Merchant approaches Rai while carrying the previously requested item. • Rai looks at his shopping list again."

            Rai "A few nails and screws..."

            "The merchant goes back to look for the requested item."

            Merchant "What else?"

        label scene4_1:
            show rai_default
            Rai "And...."

        menu:
            "I'm not sure you have one but...":
                jump scene4_2

            "This stuff.":
                jump scene4_1_a

        label scene4_1_a:
            show merchant_default
            Merchant "Didn't I told you to name the stuff right away?!"

            show rai_surprised
            Rai "A…"

            "Rai was surprised by the merchant's response."

            Merchant "Go. I don't have time"

            show rai_nervous
            Rai "W-wait. I need---"

            #SFX suara gebrak meja
            Merchant "I SAID GO!"

            "Feeling unable to fight any further, Rai decides to go home with the items he already has in hand."
            "Before leaving, of course Rai left some money to pay for the goods."

            show rai_sad
            Rai "...Thank you."

            "Rai returns to the farm."
            "He knew it might be too hasty to ask directly. But that doesn't mean he'll just give up."
            "Tomorrow he will return to the merchant. After all, the items he needed were lacking."
            "Well, we'll see tomorrow."

            jump scene4
        
        label scene4_2:
            show merchant_default
            Merchant "What? Say it."

            show rai_nervous
            Rai "Aeugh... still I'm not sure...."

            "The merchant turns around and puts his hands on his hips."

            Merchant "I have it all. Whatever you're looking for."

            show rai_surprised
            Rai "Hm? Anything?"

            "The merchant nods."

            #Ring object

            show rai_happy
            Rai "Then do you have anything similar to a ring like this?"

            "Even though it was only a glance, the merchant looked surprised when he saw the object in Rai's hand."

            show rai_serious
            Rai "Aha. Gotcha."
            Merchant "I don't know."
            
            show rai_sad
            Rai "But you said you have everything..."

            "The merchant looked restless."

            Rai "I was just wondering if you know what this thing is."

            show rai_happy
            Rai "But if you don't know, then fine. That means you don't {i}own it all{/i}."

            "For some reason, the merchant's pride was scratched."

            Merchant "...Saw."

            show rai_thinking
            Rai "Hm?"

            "The merchant brings the nails and screws that Rai had ordered earlier."

            Merchant "I saw it before."
            Rai "Only that?"

            "Rai observes the merchant's movements who responded silently."

            Merchant "Maybe it belongs to that {i}kid{/i}."
            Rai "Again?"
            Rai "Who exactly is this {i}kid{/i}?"

            "Rai had heard about this child several times today."
            "Even so, Rai doesn't fully have an idea about this child. It could be that this child is related to the mission because it sounds important to the people here."

            Merchant "Instead of 'who', maybe 'what' to be exact."

            show rai_surprised
            Rai "What do you mean?"
            Merchant "I know you get what I meant."

            show rai_nervous
            Rai "Ahaha..."

            "Rai shrugs his shoulders."

            show rai_default
            Rai "Hmmm.'What else can we dig here??"

            show rai_thinking
            Rai "So can you explain about this kid?"
            Merchant "I can't really tell you."

            show rai_annoyed
            Rai "Again?"
            Merchant "This time I mean it. She's just one of my customers."

            show rai_thinking
            Rai "Customer?"
            Merchant "Yes."
            Merchant "She came to see me a few times."

            show rai_default
            Rai "What for?"
            Merchant "What do you think she was doing?"

            show rai_angry
            Rai "This guy really...."
            Merchant "If you want to find out what this kid is doing, I can't tell-- whether I know that or not."
            Merchant "Customer’s privacy policy, you know?"

            "Rai understands this, although usually in missions there is no such thing as 'local policy'."

        label scene4_3:
            #tempered glass
            Merchant "But if you're still stubborn, maybe this can still help."

            "The merchant gives a clear rectangular object. The thickness is not too thick but not as thin as paper."

            show rai_thinking
            Rai "What is she doing with that thing?"
            Merchant "She said she wanted to get this fixed but I don't know how."

            "Rai accepts it."
            "Upon closer inspection, there were indeed cracks and scratches on the surface."

            Merchant "I don't even know the material. So I was planning to give it back when she comes back."
            Merchant "But look? We can't even see a strand of her hair."

            show rai_sad
            Rai "Oh, I see..."

            "Suddenly there is silence."

            show rai_happy
            Rai "Then, I'll take this clear thing and buy the items on the list."
            Merchant "Just name the stuff."
            Rai "Okay~"

            "Rai fills his bag with the items he had bought. He also gets additional luggage in the form of a medium-sized box containing equipment."
            "After packing everything, Rai pays for them."
            "Rai says goodbye and leaves the place."

        label scene5:
            #SHED night
            #SFX bunyi nata barang
            "The time has shown night. The sky was dark. The sound of nocturnal animals outside the shed was heard."
            "With an oil lamp in his hand, Rai packed up the things he had bought."
            "He arranged the stuff in the remaining space of the wooden shelf."
            "There are lots of things and it takes time. Fortunately, Rai felt he had enough energy left to tidy things up."

            show rai_default
            Rai "Well, this one over here... this one over there..."

            show rai_happy
            Rai "Done!"

            "Rai appreciated himself with applause."
            "After seeing that all the items looked like they wouldn't fall, Rai walked over to the mat that had been prepared in advance."
            "He plopped down on the mat."
            "Rai's tiredness and fatigue immediately grabbed him."
            "Rai lets out a long breath."

            show rai_default
            Rai "It's normal to be tired, especially on missions. Who wouldn’t break a sweat after a long day of going here and there anyway?"

            "Rai looks up at the ceiling."
            "For the first day, it was quite a long day."

            Rai "Let's see."

            "Rai recalled today's events."
            "He also glances at objects that were suspected to be evidence that had been collected."

            show rai_serious
            Rai "A ring-shaped object and a glass the size of a palm."

            "Rai looks away from the item."
            "He remembers the conversation he had with the villagers. They have been mentioning that one particular kid so many times."

            show rai_thinking
            Rai "Who exactly is this kid?"
            Rai "Was it that important for the child to be in the village?"

            show rai_serious
            Rai "Could it be that she... has anything to do with this mission...?"

            "Even if he wondered so, it was certain that Rai would suspect this child."
            "It was too obvious that she has a big influence in the village even though she wasn't that famous."

            show rai_thinking
            Rai "Is it that hard to say the child's name? How come no one knows her name."
            Rai "Or did she not introduce her name? From her personality, it doesn't seem like that."

            "Rai felt something was up."
            "He was still confused as to how everything had happened in the village but there was no sign of any big commotion or anything about the girl's disappearance."

        label scene5_1:
            show rai_serious
            Rai "Or maybe... that kid..."
        
        menu:
            "Has she been kidnapped?":
                jump scene5_1_a

            "Is she hiding?":
                jump scene5_1_b

        label scene5_1_a:
            show rai_thinking
            Rai "If that’s the case, was it because she provoked someone? I think she's also kinda naive."

            "Rai didn't mean to offend, but he thought about it considering she was denying the fact that she wasn't human."

            show rai_sad
            Rai "I hope she's okay."

            jump scene5_2

        label scene5_1_b:
            show rai_thinking
            Rai "Why is she hiding? Was she threatened by anyone?"

            "Rai remembered that the villagers said he was acting weird though it didn't bother most people. "

            show rai_serious
            Rai "Or... there's something else that she should be hiding."

            jump scene5_2

        label scene5_2:
            "Whatever it is, Rai knows all of this is related, either directly or indirectly."

            show rai_default
            Rai "Well, I'll find out later anyway."

            show rai_happy
            Rai "Time to rest!"

            #bunyi kain digesek atau bunyi bed sheet
            "Without thinking, Rai adjusted position. He immediately slid into the dream world."

        label scene6:
            #shed
            #chirp chirp

            "Morning has come. The sun had risen to the surface brightly."
            "Rai immediately wakes up and arranges his mat. • He changes his clothes and gets ready to meet the farmer."

            show rai_excited
            Rai "Okay, let's gooo!!!"

            #bunyi pintu
            "After getting ready, Rai goes out of the shed to the farmer."

            #depan farm
            #footstep
            show rai_happy
            Rai "Good morning, farmer!"

            show farmer_default
            Farmer "Oh! Morning too, young man."

            "Rai hands over the things the farmer asked for yesterday."
            "The Farmer thanked Rai. A wide smile appeared on his face."

            Farmer "You seem so excited."

            show rai_default
            Rai "I'm ready to work."
            Farmer "Yeah, yeah. That's great." 
            Farmer "Then, move on to the next job, okay?"

            show rai_happy
            Rai "Ready!"
            Farmer "Do you still have the map from yesterday?"

            "Rai nods."

            Farmer "Now you have to irrigate the cornfield. Take the water in the river."
            Farmer "You know where the bucket is, right?"

            show rai_default
            Rai "Yeah, I'll pick it up later."
            Farmer "Good. Cheer up."

            "Rai immediately rushes to the shed and takes the bucket. He also brings other things in case he needs them."
            "After preparing, Rai goes to the river."

        label scene7:
            #RIVER
            #suara sungai dan angin
            "The air feels a lot more refreshing than at the farm. The sound of running water really creates such a calm atmosphere."
            "Rai walks down the rocky road carefully."
            "Rai collects the water with the bucket that he was carrying."

            Unknown "W-woah!!"

            "Someone's voice startled Rai."

            show fisherman_default
            
            "It turns out that someone was sitting by the river. He’s holding the fishing rod."
            "Apparently, he was pulling a fish."
            "Because he looks troubled, Rai intends to help. The fisherman's face, which was looking happy, turned into confusion."

            Fisherman "Who...?"
            
            "Rai takes a closer look and it surprises the fisherman."

            show rai_happy
            Rai "Sorry, sorry. I didn't mean to startle you."
            Fisherman "Ah yea...."

            show rai_default
            Rai "By the way, what did you get?"

            "The fisherman hesitantly hands over the thing."
            
            #kail thingy

            "It looks like a fishing hook."
            "But the ends are not bent but straight and not too sharp."

            Fisherman "...Why do strange things keep happening..."

            show rai_thinking
            Rai "Eh? What did you say?"
            Fisherman "N-no! It's nothing."

            "Rai looks at the object carefully again."

            Rai "Is that a broken fishing hook?"
            Fisherman "I don’t think so. The tip is too blunt for a hook."

            show rai_default
            Rai "It is true. Is this again related to the mission?"

            show rai_happy
            Rai "Sorry if this sounds rude since we just met but may I take that thing? It looks interesting!"
            Fisherman "Of course you can."
            Fisherman "Besides, it can't be used for fishing anyway."

            "Rai receives the hook-shaped object from the fisherman."

            show rai_thinking
            Rai "...hm? How come this mission seems easy huh?"
            Fisherman "W-what?"

            show rai_happy
            Rai "It's nothing."

            show rai_thinking
            Rai "It's getting more and more awkward."
            Rai "Why is it that almost everywhere there must be something odd, like at least one?"
            Rai "And again, it's easy to find and get them."

            show rai_default
            Rai "Oh yeah, are you catching fish? How many have you got?"
            Fisherman "Here..."

            "The fisherman shows a bucket filled with fish. The fish filled half the bucket."

            show rai_happy
            Rai "How about I fish with you?"

            "The fisherman smiles."

            Fisherman "Glad to accept your offer."

            #bunyi nyebur
            "Rai throws himself into the river and starts catching fish that he saw."
            "After Rai gave fish to the fisherman, he was given some fish by him."
            "Rai walks home with water and fish in his hand."

        label scene8:
            "After Rai gave the fish to the farmer, he went to the cornfield."
            "After previously he saw a green-blue scene, now he sees a green-yellow landscape. Plants towering above Rai lined up."

            #bunyi air dituang
            "Rai who had brought water, starts watering the corn plants."

            show rai_happy
            Rai "Water, water~ Keep watering!"

            "The vast place was already starting to get wet with water."
            "Rai sighs and sits on the edge of the field."

            show rai_default
            Rai "Okay, next..."

            "Rai grabs a hoe and drags it to the empty part of the cornfield."

            show rai_excited
            Rai "Time to dig!"

            #bunyi nyangkul
            "Rai plowes the ground diligently."
            "Every now and then he wets the ground with water to make it easier to dig."

            show rai_surprised
            Rai "Oh?"

            "Something is stuck on the hoe."

            #rubber

            show rai_thinking
            Rai "This..."

            "Rai takes the thing."
            "The texture is like cloth. It stretches easily."

            #bunyi cangkul ditaruh/tanah 1x
            "Rai puts down his hoe. He put it in his pocket."

            show rai_default
            Rai "I'll check it again later."

        label scene8_1:
            #CG START

            #Bunyi gagak

            "Rai who was wiping his sweat heard the sound of a crow behind him."
            "The crow perched on the scarecrow."

            show rai_happy
            Rai "Oh! Hello, sir crow!"
            Crow "Hello! Hello!"

            "Rai laughs happily at the crow's response."

            show rai_default
            Rai "What are you doing here?"
            Crow "Food! Eat!"

            show rai_surprised
            Rai "Oh! Looking for food huh?"

            "Rai takes some corn kernels in his pocket."

            show rai_excited
            Rai "Do you want this~?"
            Crow "Caw!"

            "The crow flew over and pecked at the corn kernels."
            "After picking up some, he immediately flew back into the scarecrow."

            show rai_happy
            Rai "Is that good, Sir Crow?"
            Crow "Delicious!"
            Rai "Good!"

            "Rai wipes the sweat that ran down his cheeks."
            "The weather is quite hot too."

            show rai_thinking
            Rai "By the way, does Sir Crow often come here?"
            Crow "Here! There!"

            show rai_default
            Rai "Ooh. Go back and forth everywhere huh?"

            #ting!
            "Rai suddenly remembered something."

            show rai_thinking
            Rai "Mister crow, do you know someone who is missing?"

            "The crow tilted its head, confused."

            show rai_nervous
            Rai "Uhm, she's a girl. Looks like she used to visit the village. But suddenly she's out of sight."
            Rai "Do you know anything, sir crow?"
            Crow "The ears! Long!"

            show rai_thinking
            Rai "Long ears? Is she an elf too? Is she related to the seller?"
            Rai "Is there anything else Mr Crow knows?"
            Crow "Noisy!"

            show rai_nervous
            Rai "Uh oh, did you mean the girl or me?"
            Crow "You!"

            show rai_surprised
            Rai "Eh?!"
            Crow "Not!"

            show rai_annoyed
            Rai "...."

            show rai_happy
            Rai "Thank you, Sir Crow. If you would lik---"

            #bunyi kepakan sayap
            #CG END

            #CORNFIELD
            "The crow, without waiting for Rai to finish speaking, had already left to fly."

            show rai_annoyed
            Rai "Wow~ what a very polite crow."

            "Maybe the crow had other business. Let's just assume so."
            "Rai collects his farming tools."

            show rai_excited
            Rai "It's finally over. Time to go back!"

            "After closing the water reservoir, Rai went to store the equipment in the shed."

        label scene9:
            #shed
            "Arriving at the shed, Rai puts all of his equipmenst in their proper place. He puts large items near the boxes, while small items on the shelves."

            show rai_surprised
            Rai "Oh yeah, that thing earlier."

            #rubber
            "Rai takes a look at the thing that he just got."

            show rai_thinking
            Rai "It's some kind of rubber, right? That's the one on the clothes."
            Rai "Does this have anything to do with it?"

            "As Rai stacks up some hay, he notices something strange."

            show rai_thinking
            Rai "What's this?"

            #MiRA’s hair
            "Rai picked it up and examined it."

            Rai "Why is this hay blue?"
            Rai "Oh wait..Is this hair....?"

            "When Rai touched it, it didn't look like the texture of the hair. It feels slicker and stiffer."
            "It is similar to string but thinner."

            Rai "The fact that it's here when it wasn't there before, is it possible that..."

            show rai_serious
            Rai "Anyone else has barged in?"

            "Rai knows that only him and the farmer were in and out of the shed. There are no other workers here."
            "The farmer has also handed over some of the work to Rai."

            show rai_thinking
            Rai "If it really has something to do with that kid, does that mean she's nearby?"

            "Rai just assumed. But it could be true."

            show rai_serious
            Rai "Perhaps it's time I report directly to base."

            "Rai plans to return to IPD. That way, maybe he will discover more about the evidence that he had gathered."

            show rai_default
            Rai "I'll tell the farmer first."

            "Rai then continues on to the next job."

        label scene10:
            #suara gemuruh dari luar ruangan
            #black screen
            "At some place...."

            Unknown "Ha ha ha!"
            Unknown "HA HA HA!!"

            "They chuckle."

            Unknown "Are you coming, oh {i}my friend{/i}?"

            #suara petir
            "They can't wait for Rai's arrival."

        label scene11:
            #lokasi IPD
            "Rai arrives at the IPD."
            "As usual, Rai reports to the boss as soon as he arrives. He met with his fellow Galileans to take care of the evidence that had been obtained."
            "After handing it over to his co-worker, Rai lets him check thoroughly."

            show rai_serious
            Rai "What about the results?"

            show galilean_default
            Galilean_3 "As you might expect, it's all related. All the data is connected."
            Rai "Is it true that..."
            Galilean_3 "You're right."

            "His Galilean co-worker shows the results of their lab analysis."
            "It looks like a cellphone that has a unique design. The shape is stiff but looks solid."

            show rai_thinking
            Rai "How can a device like this exists in that dimension?"
            Galilean_3 "I don't know for sure either."
            Rai "Is there anything that can be done with this thing?"
            Rai "Could it be a transmitter or something?"
            Galilean_3 "We caught some signals from this device earlier."
            Galilean_3 "Not as accurate but enough to know the possible location."

            show rai_serious
            Rai "Alright. Send the coordinates to me immediately."
            Galilean_3 "Yes, sir."

            "Rai receives the location code of the person they are looking for. Rai smirked for a moment."

            show rai_default
            Rai "I got it. Thank you."
            
            "After they separated, Rai immediately prepared to move to the intended location, back to Farmland. But this time not the farm, but to a hill near there."
            
            Rai "Get ready, whoever you are."

            "With an unreadable expression, Rai stepped out of the IPD."

        label scene12:
            #HILL
            #Suara angin

            "Rai starts to climb up the hill."
            "He had brought provisions to meet this person face to face. His clothes were still the same as his identity as an apprentice at the farm because there was still the possibility that he might meet people he had known before."
            "Fortunately, the hiking trail looks perfect, it seems that the residents here are used to it."
            "…Or that's what Rai thought earlier."

            show rai_nervous
            Rai "Uhm, where should I go?"

            "Like the experience Rai had, he should return to the starting point of the climb. But when he looked back, the traces of the existing path had completely disappeared."

            show rai_surprised
            Rai "How come...."

            "Luckily Rai was out in the open so he could see the whole surroundings."

            show rai_thinking
            Rai "Let's see. If I came from over there, I should have gone to..."
            
            show adventurer_default
            Adventurer "Oh, are you lost, Kiddo?"

            "Of course Rai was surprised."

            Adventurer "Did that surprise you? I hope you're okay."
            
            show rai_happy
            Rai "I am alright."

            "Rai was still stroking his chest. He was surprised of her presence."

            Adventurer "So is it true about my question earlier?"

            show rai_surprised
            Rai "Oh! Yeah, I got lost, I guess."

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

            show rai_default
            Rai "Yes that's right."
            Adventurer "Then, just follow the direction of the moss. It can guide you."

            show rai_excited
            Rai "Okay!"

            "They both smiled."

            show rai_happy
            Rai "Then, I shall get going. I want to continue my journey."

            "The adventurer crossed her arms looking at Rai."

            Adventurer "Yes, be careful, okay."
            Adventurer "Recently there's been a strange sound coming from over there."

            show rai_thinking
            Rai "Sound?"

            "Rai directly faced the adventure."

            Adventurer "Yeah. Since there weren't many people there, no one knew for sure nor checked the source of the sound."
            Rai "What does that sound like?"
            Adventurer "It sounded like a blacksmith at work or two shovels colliding."

            show rai_default
            Rai "Oooh...."

            "Rai gets it."

            show rai_happy
            Rai "Thanks for the info. I'll be careful!"
            Adventurer "Yeah, I believe in you. Hope we meet again."
            Rai "Yes!"

            "Rai waves, then continues his journey to the west side of the hill."

        label scene13:
            #CAVE TUNNEL
            #Tetesan air

            "After walking quite a distance, Rai reaches the cave."
            "According to information, the location is around here."
            "When Rai arrived, it was true that there were many caves on display. Luckily Rai knows the closest approximate location to the destination."
            "Rai walks through the cave. He saw the surroundings that were filled with stalagmites and stalactites all around."

            show rai_thinking
            Rai "Hmmm..."

            "Rai tries to repeat the information he had received so far."

            show rai_serious
            Rai "The device is related to the person IPD is looking for. But, does that cat kid has anything to do with it?"
            Rai "Are they related to the farmer?"
            Rai "What is their motive?"
            Rai "What are they trying to do?"
            Rai "If it's getting the IPD or my attention, they sure are getting it"

            "Many questions flooded Rai's mind. But that's normal in missions. Rai really had to keep thinking."

        label scene13_1:
            #CAVE BERCABANG 1
            show rai_surprised
            Rai "Oh?"

            "There are two cave mouths in front of it."

            show rai_thinking
            Rai "Which one should I go through?"

        menu:
                "Right":
                    jump scene13_1_a

                "Left":
                    jump scene13_2

        label scene13_1_a:
            #cave bercabang 1
            show rai_default
            Rai "To the right, huh?"

            "Without any warning, Rai falls into a deep hole."
            "It seemed there were several minutes before Rai stopped and hit the ground. The banging sound is quite loud."

            show rai_nervous
            Rai "Aeugh...."

            "Rai tries to get up and goes back to find out where he was."
            "Rai walks through the visible cave path."

            jump scene13_1

        label scene13_2:
            #cave bercabang 1
            "Rai walks to the mouth of the cave on the left. He makes sure that the path he had chosen did have traces of being passed by people, such as the footprints of boots."

            show rai_default
            Rai "It's seems like it’s going to be a long way.."

            "The deeper Rai goes, the darker the cave is."
            "Although he didn't carry an oil lamp or other lighting, he could see in the dark. Strange indeed."

            #cave bercabang 2
            "And again, he faces two cave mouth options."
            "One has footprints from sports shoes. Others have large puddles of water."

            show rai_thinking
            Rai "Which one is it?"

        menu:
                "Caves with footprints.":
                    jump scene13_2_a

                "Caves with puddles.":
                    jump scene13_3

        label scene13_2_a:
            #cave bercabang 2
            show rai_default
            Rai ""

            #DARK
            "When Rai stepped in, suddenly the surroundings were dark."

            show rai_thinking
            Rai "Ah, did I go the wrong way? Yet there are traces, very clear."

            "Rai was waiting for the surroundings to become clear."

            #HILL
            "After a while, it turned out that Rai was outside the cave with the surrounding green scenery."

            show rai_default
            Rai "Back here huh?"

            "After looking left and right, Rai goes back to the cave entrance not far from where he is sitting."

            jump scene13_1

        label scene13_3:
            show rai_excited
            Rai "I'm not that easily fooled."

            "Rai walks into the mouth of the cave. He calmly entered without doing one hundred percent supervision. Of course he's in work mode."

            show rai_thinking
            Rai "The previous imprint was obvious but the imprint in the cave before that was the footprints of boots. It shouldn't be that different right?"

            "Rai nods."

            show rai_serious
            Rai "This fellow is good at hiding traces too."

            "With that, Rai continues to walk through the cave."

        label scene14:
            #Final Cave
            "After going through a long hallway, Rai arrives at a huge place."
            "The place was also bright, as if it didn't feel like it was in a cave."
            "Rai goes around to see the place. He sees several tables with small devices on them."

            #FOOTSTEP
            "Rai instantly in alert mode."

            Unknown "Oh? I have a guest?"

            "Rai takes a closer look at who it was."

            Unknown "Welcome!"

            show mira_default

            "It turned out to be a girl in a dress."

            show mira_excited
            The_Girl "You must be tired from walking all the way here? Come on! I'll serve you some tea."

            show rai_annoyed
            The_Girl "...Who--"

            show mira_serious
            The_Girl "Hey, are you listening? I'm asking you."

            "The tone when she spoke sounds different from before. It startled Rai a bit."

            show mira_happy
            The_Girl "Ah, I'm sorry. My program--ah, I mean my body's condition is not completely good but it's still under maintenance anyway!"

            "Rai notices this girl's appearance. Obviously she wasn't human. Especially with the big antennae on her head."

            show rai_annoyed
            Rai "That's not a long ear, Mr. Crow."

            show mira_excited
            The_Girl "Come on, come in! There's no need to be shy."

            "Rai approaches The Girl without any words."
            
            show mira_happy
            The_Girl "Well, that's it. Come sit here."

            "The Girl pats the small chair across from her before returning to sit on the other side. Rai comes close but chooses not to sit down."

            The_Girl "Eeeh, just take a seat. I'm not going to get mad at you."

            show mira_excited
            The_Girl "In fact, I'm glad to have friends to talk to over tea!"

            show rai_thinking
            Rai "Won't be mad? Are you sure?"

            "The Girl nods. She took a sip of something from a cup."

            show mira_default
            The_Girl "Sure. I haven't spoken to anyone in a long time."

            show rai_serious
            Rai "Hah! You must be very busy."

            show mira_surprised
            The_Girl "Hm? Not really. In fact  have nothing to do now."

            show rai_thinking
            Rai "Question, what do you have in that cup?"

            #gebrak meja
            "The Girl pounds the table."
            
            show mira_angry
            The_Girl "I'm a human!!"

            show rai_default
            Rai "But I didn't say you {i}aren’t{/i} human?"

            show mira_pissed
            The_Girl "Ugh!"

            show mira_angry
            The_Girl "Well whatever! It's tea, okay?"

            "The Girl continues to sip her tea while Rai keeps an eye on her."

            show rai_thinking
            Rai "So.. Mind to tell me what all of those things are?"

            show mira_default
            The_Girl "Why mind that? Didn't you tried so hard just to get here? Just enjoy the beautiful view, while i enjoy my tea."

            show rai_surprised
            Rai "She saw me struggling at the cave earlier huh---"
            Rai "How did you know that?"

            show mira_happy
            The_Girl "I have super powers!"

            show rai_default
            Rai "You said you are a human.."

            show mira_serious
            The_Girl "You think humans can't have any powers?"

            "Rai becomes silent."
            "Indeed he’s also a human with something similar like superpowers, he couldn't deny that. But the power of people in general with the strength of IPD members is different."

            show mira_default
            The_Girl "You’re just like… the woman in the village. You should maintain your manners!"

            show mira_serious
            The_Girl "I guess you should just go home if you don't like it here."

            show rai_sad
            Rai "Why? Aren't you glad I'm here?"

            show rai_excited
            Rai "I'm accompanying a girl who was alone in this secluded cave~"

            show mira_pissed
            MiRA "Even though you casually barged in? In the middle of my tea party?"

            show rai_default
            Rai "Hmm?"

            "The Girl stands up. In an instant the atmosphere turns tense."

            show mira_serious
            The_Girl "I guess I have to give up being a {i}good girl.{/i}"

            "Rai remained with his confused smile while The Girl had a flat expression this time."

        label scene15:
        #CAVE FINAL

            show mira_sad
            The_Girl "You don't want to do it the peaceful way, do you?"
            
            show rai_serious 
            Rai "Oh? So we’re jumping to the point now?"
            Rai "Good. Been waiting for that"
           
            show rai_happy 
            Rai "Do people who’s trying to break through IPD's defenses want to go the peaceful way?"
            
            "The Girl is annoyed. Then, she cleared her throat."
            
            show mira_excited 
            The_Girl "First of all. As a good girl, I will introduce myself." 
            
            show mira_happy
            MiRA "I'm MiRA. An ordinary human who chats with other humans."
            
            show rai_happy 
            Rai "Well..Thank you for introducing yourself."
            
            show rai_serious
            Rai "Though.. The human part is a bit questionable."
            
            show mira_angry 
            MiRA "What do you mean?!"

            "MiRA was offended by Rai's words."
            
            show rai_serious
            Rai "Take a look of yourself."
           
            show mira_surprised 
            MiRA "Eh?!" 
            
            show rai_happy 
            Rai "The point is, you better turn yourself in and come with us, okay? I’ll be good if you just cooperate with me!"
            
            show mira_pissed 
            MiRA "I am a human!" 
            
            "She’s not responding to Rai’s words. Rai can not believe that this girl is still in denial."
            
            show rai_excited
            Rai "Yes, yes. Of course."
            Rai "So, come with me, will you?"

            #CG START
            "When Rai is about to pull MiRA’s hand, this girl's expression becomes serious." 
            "Along with that, around her a hologram-like screen appears."
            
            show mira_angry 
            MiRA "I'm not leaving!"
            
            show rai_thinking
            Rai "Can robots be unstable too?"
            Rai "Is there something wrong with the program?"
            
            show mira_pissed
            MiRA "I told you multiple times, I am a human!"
            
            show rai_default 
            Rai "Yep."
            Rai "This girl is a little bit cuckoo in the head"
            
            show rai_nervous
            Rai "I'm sorry, but you know.. That appearance of yours..."
            
            show mira_angry 
            MiRA "I have two hands and two legs, isn't that enough?!"
            
            "Rai's expression calms down."
            
            show mira_pissed 
            MiRA "You guys, kept saying that I'm not human." 
            
            show mira_angry 
            MiRA "Even though I only look a little different from you guys!"
            
            show rai_nervous
            Rai "But it's not just a little..."
            
            show mira_angry 
            MiRA "The people in the village are like that too! You are the same!"
            
            "MiRA shows something in her hand."
            
            show mira_happy
            MiRA "You must know what I'm thinking, right?"
            
            show rai_serious 
            Rai "Perhaps..."
            
            show mira_angry 
            MiRA "No one listened to me!" 
            MiRA "No one believed me!"
            
            show mira_excited
            MiRA "And so I will blow up the village!" 
            
            "Rai's expression turns serious. Of course Rai can not let it happen. Intervention from a world that is not where it belongs is not allowed."
            
            show rai_serious
            Rai "Okay listen. Calm down first---"
            
            show mira_angry 
            MiRA "Huh! You think I'll listen to you?!"
            
            show rai_annoyed 
            Rai "Ugh...."
            
            show mira_angry 
            MiRA "I'll get rid of everyone who talks about me behind my back, you’re all bad people!"
            
            show rai_serious 
            Rai "Are you sure about your decision?"
            
            show mira_sad
            MiRA "What is it that makes me unsure? You saw how they treated me, right?"
            
            "Rai zips his mouth."

        label scene15_1:
            show mira_serious 
            MiRA "It's useless for you to persuade me. I've been here longer than you, you know."
            
            show mira_angry
            MiRA "They always bring up that I'm different. Do you know that?!"
            
            show mira_pissed
            MiRA "They don't believe what I'm saying… They always have that look on their face...."
            
            show mira_angry 
            MiRA "They keep... discriminating me!"
            
            "MiRA slightly bowed. Her voice is low, almost like a whisper."

            show mira_sad 
            MiRA "Do you know... how does that feel?"

        menu:
                "Let her be.":
                    jump scene15_1_a

                "Calm her down.":
                    jump scene15_2

        label scene15_1_a:
            #STILL IN CG
        
            show mira_sad 
            MiRA "Haha…"
            
            show rai_nervous 
            Rai "What?"
            
            show mira_sad 
            MiRA "See…?"
            
            show rai_default 
            Rai "Eh?"
            
            show mira_angry 
            MiRA "Even you are the same as them!"
            MiRA "Why won't you just believe me?!!"
            
            show rai_surprised
            Rai "WAIT!"
            
            "MiRA presses the forbidden button. Red screens appear everywhere. Each screen displays different corners of the village. It could be seen from the screen that the village is in chaos due to explosions everywhere."
            
            show mira_excited
            MiRA "EAT THAT!"

            "MiRA laughs with satisfaction seeing the destruction in front of her eyes." 
            "Rai widens his eyes. Rai tries to believe what happened." 
            "The mission before his eyes, failed."

            show rai_annoyed 
            Rai "I wish I could redo it again..."

            jump scene15_1

        label scene15_2:
            show mira_sad 
            MiRA "Though... even though...."
            MiRA "I just want to be accepted.."
            
            show rai_sad 
            Rai "You know what will happen if you press the button right?"
            Rai "Are you sure you want to do that?"
            
            show mira_pissed 
            MiRA "Yes! O-of course!"
            
            show mira_sad 
            MiRA "I guess..."
            
            show rai_sad 
            Rai "By doing that... you know? You might regret it..." 
            "All those people in the village, they’ve been looking for you, you know?"

            show mira_surprised 
            MiRA "...."
            MiRA "Huh?"
            
            show rai_serious 
            Rai "Despite the way they look at you, I do think they are still concerned about your wellbeing. They are wondering about your whereabouts." 
            
            show rai_sad 
            Rai "The guy and the grocery seller I met last time even thought that you tried too much to blend in."
            Rai "They even said that they are fine accepting you as a person even if you are not like them."
            
            show rai_serious 
            Rai "I don’t think their speech nor manner implied any malicious intention. It’s just a misunderstanding on your side." 
            
            show mira_pissed 
            MiRA "You’re lying!!"
            
            show rai_serious
            Rai "Why would I? Let me ask you this again. From what I’ve told you and from what you’ve seen from the villagers." 
            Rai "Do you think those actions were fueled by hatred? Malice?"
            Rai "Does it even make sense for someone who is trying to discriminate against you to be concerned about you?" 
            
            show mira_pissed 
            MiRA "Ugh...."
            
            show rai_default 
            Rai "So, just hand over that dangerous thing and come with me, okay?"
            Rai "We’ll get everything straight with a chat, shall we?"

            #CG END

            #CAVE FINAL
            "MiRA steps closer to Rai."
            "MiRA gives the trigger to Rai."

            show rai_excited 
            Rai "Good girl!"
            
            "Rai secures that thing."

            show rai_happy 
            Rai "Then let's go outside now. The sun must be shining bright outside!"
            
            "Rai led MiRA out of her residence."
            "Before leaving, Rai asked MiRA to turn off all existing tools."
            "They walk out of the cave in silence."

        label scene16:
            #HILL
            #suara angin, footstep

            "Rai and MiRA come out of the cave. They walked down the hill."
            "The wind blows filling the silence between them. It’s time to head back to IPD, bringing along his newly found inmate, Rai contacts the IPD to open up a portal."

            show rai_default
            Rai "Just a minute, MiRA."

            "MiRA nods."
            "Rai walks a little away from her."
            "MiRA looked up at the sky sadly."

            show mira_sad
            MiRA "The sky…"
            MiRA "I-it's beautiful"
            MiRA "What have I been doing all this time?"

            "MiRA knew that all of this was wrong. She also knew that the people there weren't actually that mean to her."
            "Deep down, MiRA was actually grateful to be there. All of them were trying to get to know MiRA."
            "She herself made the barrier between her and others."
            "She should have been more open while she could. She was worrying too much"
            "Worrying that people won’t accept her. When in fact, she was the one who didn’t accept herself."

            #SFX Footsteps
            "Rai goes back to MiRA again."

            show rai_default
            Rai "Let's go."

            "Rai and MiRA head back down the hill."
            "Rai walks in front of MiRA."
            "Rai doesn't handcuff MiRA because she wants to cooperate."

            show mira_default 
            MiRA "...Thank you..."
            
            show rai_default 
            Rai "Hmm?" 
            
            "Rai glances at MiRA."

            Rai "Oh, it's nothing."
            
            show mira_serious 
            MiRA "..."             
            Rai "You know what.."
            Rai "I don’t think it’s that bad being a robot."
            
            show mira_pissed 
            MiRA "A HUMA-"
            
            show mira_default2 
            MiRA "...An android."
            
            show rai_happy 
            Rai "An android, yes."
            Rai "In fact.. I do think you look cool!"
            
            show mira_surprised 
            MiRA "Really?!"
            
            show mira_happy 
            MiRA "Thank you!!"
            
            show mira_default2 
            MiRA "Hearing that made me really happy." 
            MiRA "I guess that’s what I've been wanting to hear."
            
            "Rai ended the journey by taking MiRA to IPD."
            "Rai missed something though."
            "There’s something left on MiRA’s table.."

            jump ending
   

    label route3:
        label R3scene1:
            #FARM
            #Various farm animal noises

            show rai_default 
            Rai "Alright, so here’s the place huh..."
            
            "Rai is looking around, gazing through the fields, to familiarize himself with the scenery that will be with him for quite a long time."
            
            #whirling winds
            show rai_default 
            Rai "Ahh~ the breeze here feels nice, exactly like what I expected."
            Rai "Oh right, I should look for the farmer first huh? He must be expecting me by now."
            
            "Rai looks around, trying to find the farmer, just to find nothing such as that in sight."
            
            show rai_thinking 
            Rai "He’s nowhere to be seen around... maybe he’s inside the barn? I should go check."
            
            "Rai went towards the barn, but just as he tried to open the door, suddenly a big hand touched his shoulders."
            
            show farmer_default
            Farmer "Hey kid!"
            
            show rai_surprised 
            Rai "A-ah... hello sir!"
            Rai "(Whoa, that surprised me.)"
            
            show rai_annoyed
            Rai "(I’m not a kid though, hmph.)" 
            Rai "(Oh well, for the sake of this mission, I'll let it slide this time.)"
            
            Farmer "Who are you? What are you doing? Are you trying to break into my farm?? Are you—"
            
            "The farmer suddenly stops."

            Farmer "Ah, my bad for jumping to conclusions, but you do kinda look suspicious kid, haha."

            show rai_nervous 
            Rai "A- actually, i’m looking for you just now sir."
            Farmer "Hmm? What kind of business did you have with this old man?"
            Farmer "Oh wait... are you perhaps the..."
            
            show rai_happy 
            Rai "Yeah! I’m the intern that’s going to help you around here for a while sir! Nice to meet you!"
            Farmer "Likewise, kid!"

            "The farmer observed Rai for a bit."
            
            Farmer "Hmm... but you sure you could put up with the farmwork kid?"
            Farmer "Ah, but you’re the one who came here on your own will..." 
            Farmer "I’m sure you already thought this through."
            
            show rai_annoyed
            Rai "Don’t underestimate me just yet sir!"
            
            show rai_excited 
            Rai "Even though I look like this, physical labor is nothing for me!"
            Rai "You can count on me sir!"
            
            show rai_nervous 
            Rai "(*gulp* I might have exaggerated it a little bit...)" 
            Rai "(Oh well, if that’s what it took to earn his trust.)"
            
            Farmer "Hahaha, you’re such a confident kid, I like that."
            Farmer "Alright, but you must be tired from your trip today right? I’ll start the work tomorrow" 
            Farmer "You should rest up for today, or if you want, you could go around the neighborhood to get yourself used to our environment, it’s your call."
            
            show rai_happy 
            Rai "Thanks for your consideration sir! I might go with the latter suggestion, I also want to see what’s around here."
            
            Farmer "Alright then, I’ll leave you to yourself kid" 
            Farmer "Have fun and see you tomorrow."
            
            show rai_happy 
            Rai "See you tomorrow sir, have a nice day!"
            
            hide farmer_default

            show rai_default 
            Rai "(Alright, now that i’m free, maybe i should be getting started on the investigation)"
            
            show rai_thinking 
            Rai "(Hmm... where should i go though...)"

        menu:
            "Maybe I should take a stroll on the forest nearby":
                jump R3scene1_1_a

            "Maybe I should go to the village and see the market there":
                jump R3scene1_1_b

            "Maybe I should go fishing on the river":
                jump R3scene1_1_a

        label R3scene1_1_a:
            show rai_thinking
            Rai "Hmm.... But I’m already kinda tired today."

            show rai_default
            Rai "Maybe I should go to the village and the market instead, i’m also curious about the people of this world."

            jump R3scene2

        label R3scene1_1_b:
            show rai_default
            Rai "Yeah, I should probably check the village for now."
            Rai "This is also my chance to learn about the villagers."
            Rai "Maybe I would also find some clues."
            Rai "Alright let’s go!"

            jump R3scene2

        label R3scene2:
            #Village
            #Crowd Noises

            show rai_surprised
            Rai "So this is the village huh..."
            
            show rai_excited 
            Rai "Whoa... what a lively village!"

            show villager_default
            Villager "Haha! Sure it is."
            Villager "Is this your first time here? Never seen you around before."
            
            show rai_surprised 
            Rai "Ah hello there."
            
            show rai_default 
            Rai "That’s right, I just came here today."
            Villager "What kind of business did you have around here?"
            Villager "It’s been a while since a youngster like you showed up outta nowhere."

            show rai_happy 
            Rai "I’m helping out the Farmer around the farm for now" 
            Rai "Maybe you could say it was an internship? Hehe."
            Villager "Ah, so that's how it is." 
            Villager "Well, good luck on your job."
            Villager "Maybe you should check out the market after this."
            Villager "There’s a lot of interesting stuff there for sure."
            
            show rai_happy 
            Rai "Yes, that’s what I planned to do after this."
            Rai "Thanks for the suggestion though."
            
            "Rai suddenly realized something."
            
            show rai_thinking 
            Rai "(Wait, did he say that it’s been a while since someone like me showed up?)"
            Rai "(I wonder if they’re the ones that I'm looking for?)"
            Rai "(Should I ask him for more information about them?)"

        menu:
            "Ask the villager about the other newcomer":
                jump R3scene2_1_a

            "Nope, time to get going":
                jump R3scene2_1_b

        label R3scene2_1_a:
            show rai_surprised 
            Rai "Ah, wait!"
            
            show rai_default 
            Rai "I recalled that you said it’s been a while since someone like me showed up around here?"
            Rai "Does that mean there’s someone relatively new around here like me?"
            Villager "Yeah, you wanna know about it?"
            
            show rai_default
            Rai "Yes, please tell me about them."
            Villager "Alright, I guess it would be easier for you to get along with fellow newcomers huh?" 
            Villager "I don’t really know about her, but not long ago i heard that someone around your age, a young woman, started living with the butcher" 
            Villager "I don’t know, maybe she adopted her?" 
            Villager "But it’s kinda weird that someone like her decided to adopt someone as a daughter."
            
            show rai_thinking 
            Rai "Weird?"
            Villager "Uh... if i could put it into words... the Butcher is like someone that you don’t want to mess around with" 
            Villager "A straightforward, and sometimes aggressive person, maybe that’s how i would describe her"
            
            show rai_thinking 
            Rai "I see..." 
            Rai "Thank you for the information!"
            Rai "It’s getting late, maybe i should get going"
            Rai "See you later!"
            Villager "Hope you found that information helpful, good luck!"

            jump R3scene3

        label R3scene2_1_b:
            show rai_default 
            Rai "(Ah, nevermind)"
            Rai "(maybe i would find out about it sooner or later)" 
            Rai "(Time to get going!)"
            
            show rai_thinking 
            Rai "Sorry for taking up your time"
            Rai "It’s getting late, maybe i should get going"
            Rai "See you later!"
            Villager "It’s alright, happy to help."
            Villager "Good luck!"

            jump R3scene3

        label R3scene3:
            #Market
            "After walking for a short while, Rai arrived at the market, but unlike his expectations..."

            #Sfx silent
            show rai_surprised
            Rai "Eh?..."

            show rai_default 
            Rai "(Looks like everyone is already preparing to pack up for today.)"
            Rai "(Maybe I came too late?)"
            Rai "(Oh well, I'll just come back to the farm and return here tomorrow.)"

            "Rai returned back into the farm, and spent the rest of the day resting up to prepare for his first day tomorrow."

        label R3scene4:
            #Black screen
            "The next day..."

            #Morning chicken sfx

            show rai_surprised
            Rai "Whoa!"
            #Gedubrak

            #Shed
            show rai_annoyed 
            "O-oh... it’s already morning huh..."
            
            show rai_default 
            Rai "I should be getting ready for today."
            
            "After preparing himself for the long day, Rai went toward the field." 
            "The Farmer, as expected, had already waited for him there."
            
            #Farm
            show farmer_default
            Farmer "Good morning kid, it’s your first day working today, you’re ready?"

            show rai_excited
            Rai "Readier than ever sir!" 
            Rai "Or you could say that i am, Rai-dy, heheh"
            Farmer "Ha, good one kid" 
            Farmer "Alright, for your first day, you’re free to choose what kind of work you wanna do" 
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
            Farmer "It’s also a good opportunity to get acquainted with the mart vendors, should be good for you"

            jump R3scene4_2

        label R3scene4_1_b:
            Farmer "Oh you want to help restocking at the market?"
            Farmer "Sure sure"
            Farmer "You must also be eager to know more about the neighborhood right?"
            Farmer "Alright, go on."

            jump R3scene4_2

        label R3scene4_2:
            Farmer "That reminded me, you already went to the village yesterday right? How was it?"
            
            show rai_default
            Rai "The village is lively, the people are also nice"
            Rai "But too bad, i was too late when i came to the market yesterday, everyone’s already wrapped up for that day."
            Farmer "I see I see... That’s more reason to send you there today"
            Farmer "Alright, i need you to go to the butcher on the market"
            Farmer "Tell her to get the Farmer’s usual stuffs"
            Farmer "She should know already"
            Farmer "Oh, and also tell her to put it on my tab."

            show rai_thinking
            Rai "(The butcher huh...)"
            Rai "(This might be my chance to look for a lead.)"

            show rai_happy
            Rai "Ok, got it!"
            Rai "I’ll be off now, goodbye!"
            Farmer "Take care!"

            jump R3scene5

        label R3scene5:
            #Market
            #Crowd noises

            show rai_default 
            Rai "So this is how the market looks like on these hours huh" 
            Rai "It’s just as lively as the village, I mean, look at those crowds."
            
            show rai_thinking 
            Rai "Actually at first I wanted to look around first" 
            Rai "But i think i should go straight to the butcher, what the villager said yesterday still bugging me."
            
            "Rai, decided to get rid of any desire to procrastinate inside him, went straight to the butcher, even though he originally wanted to look around for a while."

            show rai_default 
            Rai "Excuusee meee."
            
            show butcher_default
            Butcher "Yo kid, what did you need?"
            
            "The butcher turns around to see Rai."

            Butcher "Make it quick kid"
            Butcher "I don’t have all day, you’re not the only customer here"

            show rai_nervous 
            Rai "A-ah yes..."
            
            show rai_nervous 
            Rai "(Whoa, she’s so intimidating)" 
            Rai "(Get yourself together Rai Galilei)"
            
            show rai_serious
            Rai "I was sent here by the Farmer, he said to get the usual."
            Butcher "Heh, don’t be so serious kid" 
            Butcher "Sorry for the earlier, I’ll get your order up right now, please wait a little."
            
            show rai_nervous 
            Rai "O-okay?"
            
            "The Butcher went to fetch Rai’s order. In the meanwhile"
            
            # [CG Starts]
            show rai_thinking
            Rai "(Hmm… look at these juicy meats, they look delicious)" 
            Rai "(I wonder if i should use some of the money the IPD provided me to buy some?)"
            Rai "(To throw myself a welcoming BBQ party perhaps?)"
            
            show rai_default
            Rai "(Oh no I shouldn’t)"
            Rai "(These are for emergencies only)"
            Rai "(I can’t splurge it carelessly like that)"
            Butcher "Your order’s here kid."
            
            
            # [CG End]
            
            Butcher "That was quick heh?"
            Butcher "Glad i have someone to help out here now"
            
            show rai_happy 
            Rai "Thanks ma’am"
            Rai "Oh also, the farmer told me to put these on his tab"
            Butcher "Ye, i know that already" 
            Butcher "But give this to him after you get back"
            
            "The Butcher handed Rai a piece of paper."

            show rai_thinking 
            Rai "What is this for?"
            
            Butcher "That’s the thing i needed him to prepare tomorrow in place of today’s payment" 
            Butcher "I’ll get my daughter to fetch it tomorrow at the farm."

            show rai_default
            Rai "Ah, got it"
            Rai "I’ll give it to him when i get back"
            Butcher "Oh before you go, may I ask something else?"
            Rai "Yes?"
            Butcher "Since you’re also new here, I want to ask you to be my daughter’s friend" 
            Butcher "She came here not too long ago, and she’s kinda shy"
            Butcher "Hope she can open up more with someone who’s also new in the farmland."
            
            show rai_surprised
            Rai "E-eh?? That was so sudden"
            Butcher "So you’re rejecting my request?"
            
            show rai_default
            Rai "No, not like that"
            Rai "Actually, I’m grateful for the chance" 
            Rai "Maybe she could also give me pointers around the farmland, and something like that"
            Butcher "Heh, good" 
            Butcher "BUT"
            Butcher "I only asked you to get along with her"
            Butcher "Don’t even try to do anything to her."
            Butcher "Don’t you dare put her in danger" 
            Butcher "You didn’t want to incur this Lioness’ wrath, right?"


            show rai_nervous 
            Rai "Y-you didn’t have to worry about that"
            Butcher "Good, we’re done here for today" 
            Butcher "Now go"

            show rai_default 
            Rai "Alright, i’ll be going now"
            
            "After getting things done, Rai left the market, and went back to the farm." 
            "Finishing off the rest of his duty that day" 
            "The day goes on after that" 
            "Until the next day comes..."

        label R3scene6:
            #Black screen

            "The next day..."

            #shed
            Rai "Phew, that was quite heavy"
            Rai "Man, the shed was really messy, I’m glad everything were back on where they belong"
            Rai "Oh right, someone was supposed to come here today huh?"
            Rai "I wonder when she’ll come"

            #[Door opens]
            Unknown "Excuse meee"
            
            show rai_surprised 
            Rai "Huh, who’s that?"
            Rai "Comiiing."

            show elsyne_surprised
            The_Girl "Eeeek!"
            The_Girl "W...who are you?"

            show elsyne_scared
            The_Girl "A... A thief?"
            The_Girl "D... Did someone break in?"
            The_Girl "W... Where’s the Farmer?"
            
            show elsyne_default 
            The_Girl "Ah, wait"

            "The girl realized something"

            show elsyne_shy
            The_Girl "Y... You’re the customer from yesterday right?"
            The_Girl "S... Sorry for the earlier"

            show rai_default 
            Rai "Wait wait, it’s fine, really" 
            Rai "Have you calmed down"

            The_Girl "Y.. Yes"
            Rai "Okay then" 
            Rai "So, are you the one who’s sent by the butcher to pick up her request?"
            The_Girl "Yup"
            Elsyne "I... I’m Elsyne, nice to meet you"
            
            show rai_happy 
            Rai "Same here!"
            Rai "My name’s Rai, by the way"
            Elsyne "M... Mr Rai huh..."
            Rai "No no, just Rai is fine."
            Elsyne "Ah, okay."
            Rai "I’ll go fetch the things for you, wait here for a sec ok."
            Elsyne "Mmhm."

            
            "Rai went to the back, and returned with a sack full of farm commodities."

            Rai "Phew, here you go."
            Elsyne "Uh-huh, thanks." 
            Elsyne "I’m going now, bye."
            
            show rai_surprised 
            Rai "W-wait, you sure you can bring that back all by yourself?" 
            Rai "Do you need me to accompany you?"
            Elsyne "I’m fine all by myself, no need to worry." 
            Elsyne "And even though you were to accompany me, you’re sure you know where to go?"
            
            show rai_excited 
            Rai "Ah, haha..."
            Elsyne "S... Sorry, I didn't mean to offend you."
            Elsyne "A... Actually, mom asked me to show you around after this."
            Elsyne "You should go with me."
            Rai "All right then, let’s go."
            Elsyne "Mmhm"
            
            show rai_excited 
            Rai "Okay!"
            Rai "We should probably go bring these things first right?"
            Elsyne "Mmm." 
            Elsyne "Let’s go back to the village first."

            # [Village]
            
            Elsyne "Here"
            Rai "Phew, arrived at last"
            Rai "It’s not even that far, but these things are quite heavy"
            Rai "I’m already sweating"
            Elsyne "Told you"
            Elsyne "I would’ve been fine by myself"

            show rai_happy 
            Rai "Don’t worry about that though!"
            Rai "As the Farmer’s helper, i should be getting used to these kind of work"
            Elsyne "Mmmm,if you say so" 
            Elsyne "Wait here"
            
            show rai_surprised 
            Rai "Eh?"
            
            "Elsyne went inside, and returned back with a cup of water in a flash"
            
            Elsyne "Here, drink."
            Rai "Thanks, I appreciate it"
            Elsyne "Mmhm"
            Elsyne "Ma told me to do that if someone’s visiting"

            show rai_thinking 
            Rai "Ma? You mean the butcher?"
            Rai "I didn’t expect she’s someone to said something like that"
            Elsyne "Yes..."
            Elsyne "She might looks a little rough outside, but actually she’s really kind"
            Rai "You’re right" 
            Rai "She got this really intimidating aura when we first met"
            Rai "But when she’s talking about you, she somehow softened"
            Elsyne "Uh-huh"

            show rai_thinking 
            Rai "(So that’s how it is huh)" 
            Rai "(She’s the someone who can douse the Butcher’s raging flames)" 
            Rai "(She must be that precious for her)"
            Rai "(That reminded me, should i ask her about her views toward the village and the villagers?"

        menu:
            "Yes, i want to know her opinion about the village":
                jump R3scene6_1_a

            "No, that’s too personal, i shouldn’t interfere":
                jump R3scene6_1_b

        label R3scene6_1_a:
            Rai "So, I’ve been meaning to ask you something, is it okay?"
            Elsyne "Hmm? Go on"
            Rai "You’ve been living here not long before i arrived right?"
            Rai "What did you think about this village and the villagers"
            Elsyne "Ah, that"
            Elsyne "They’re... a bunch of nice people"
            Elsyne "When Ma first took me in, i didn’t expect them to be so welcoming"
            
            show elsyne_sad 
            Elsyne "I was so scared back then..." 
            Elsyne "The fear of being rejected, shunned, or..."
            Elsyne "Being feared"
            Elsyne "But... yeah..."
            Elsyne "I’m grateful of the kindness that they’ve shown towards me"
            Elsyne "Sometimes... i don’t think i deserved this all these kindness"
            Elsyne "Someone like me..."

            show rai_serious 
            Rai "I’m sorry, but you’re wrong there"
            Elsyne "Huh?"
            Rai "Everyone deserves kindness, no matter how little they are"
            Rai "Even though they’re a criminal who took thousands of life, i don’t think they should be robbed entirely of kindness" 
            Rai "Though, you’re nothing like that, so please be more confident of yourself"
            Rai "You’re more than deserved for all of this" 
            Elsyne "......"
            
            show elsyne_happy 
            Elsyne "A...alright, thanks for those encouraging words" 
            Elsyne "I think... I should be more proud of myself from now on."
            
            show rai_happy 
            Rai "That’s the spirit!"
            Elsyne "(What a weird guy...)" 
            Elsyne "(He knows nothing...)"
            Elsyne "No, he shouldn’t know anything about that"
            Elsyne "My true self...."

            jump R3scene6_2

        label R3scene6_1_b:
            show rai_serious
            Rai "This is my chance to get more information from her"
            Rai "Should I really pass on this chance?"

        menu:
            "Yes, i want to know her opinion about the village":
                jump R3scene6_1_a

        label R3scene6_2:
            Rai "Oh anyway, where should we go next?"
            Elsyne "Depends, your call"
            
            show rai_thinking
            Rai "Hmmm let’s see..."
            Rai "I’ve been to the village and the market, so how about..."
            Elsyne "There’s a forest and a river near the farm, have you been there?"
            Rai "Oh? Your personal recommendation?" 
            Rai "No i haven’t been there yet"
            Rai "But if you’re the one who recommended it, it must be a nice place"
            Elsyne "Uh-huh, i often went there after work to wind down"
            Elsyne "You could either take a stroll in the breezy forest, or sit down and relax to the sound of the flowing river."
            Elsyne "It’s such a lovely place, i’m sure you would like it"

            show rai_excited 
            Rai "Alright then, that sounds interesting" 
            Rai "I’m fine with whichever we go first"
            Rai "We should be off now"
            Elsyne "Sure"
            Rai "Alright, what’re we waiting for then? Let’s gooo"

        label R3scene7:
        #Forest
        #Birds chirping

        show rai_surprised
        Rai "Whoa, so this is the forest huh..." 
        Rai "I didn’t expect there’s a forest this dense nearby"
        Elsyne "Yup"
        show rai_happy 
        Rai "Aaahhh, what a nice breeze"
        Rai "I understand why you liked this place"
        Elsyne "Uh-huh"
        Rai "So, what’d you usually do here?" 
        Rai "Just aimlessly strolling around? Or there’s something else?"
        Elsyne "Mostly just wandering around" 
        Elsyne "But sometimes I also hunt here"
        
        show rai_surprised
        Rai "What???"
        Rai "You? Hunting?"
        Elsyne "W...why so surprised"
        Elsyne "As the Butcher’s daughter, i should know a thing or two about hunting"
        Elsyne "I’m not that frail, you know"
        
        show rai_nervous 
        Rai "A-ah, sorry"
        
        show tree_default

        show rai_surprised 
        Rai "Huh, what’s that giant tree over there?" 
        Rai "Wait, is it ALIVE?"
        Elsyne "Plants are also a living thing you know"
        Elsyne "But yes, that’s the guardian of this forest, the Talking Tree"
        Elsyne "Looks like he’s taking a nap right now"

        # [Snore]

        Talking_Tree "Zzzz...."
        Rai "We shouldn’t bother him then, let’s move on"
        Elsyne "Uh-huh"
        
        show rai_thinking 
        Rai "So... Can you tell me more about him?" 
        Rai "Those kind of tree aren’t something that you usually see everyday" 
        Rai "Except if you lived on the farmland, i guess"
        Elsyne "Sure"
        Elsyne "Ma told me that at first, the tree was originally believed to be some kind of myths in the village"
        Elsyne "But later, it turned it to be a real thing"
        Rai "Whoa, neat"
        Elsyne "Uh-huh"
        Elsyne "Oh, we’ve arrived"
        Rai "I can see the clearing over there"
        Rai "So we’ve arrived at the exit?"
        Elsyne "Not quite"
        Elsyne "You’ll see soon enough"

    label R3scene8:
        #River
        #Flowing Water

        show rai_surprised 
        Rai "Wow, it’s the river!"
        Elsyne "Yup"
        Elsyne "This is our next destination"
        Elsyne "The river is a pretty popular spot among the villager"
        Elsyne "On the weekend you could see people fishing, picnicking, or even swimming here"
        Rai "I see..."
        Rai "And if i recall correctly, you liked to sit down and relax to the sound of the flowing river here right?"
        Elsyne "Yeah"
        Rai "I do agree with you"
        Rai "It’s so calming around here"
        Rai "I think one of these days i’m gonna snuck outta the farm to take a nap for a while here..."

        show rai_thinking 
        Rai "Anyway, this river should lead somewhere right?"
        Rai "What is at the end of the river? A lake?"

        show elsyne_smile
        Elsyne "*giggles* Glad you asked"
        Elsyne "It’s more than just a lake" 
        Elsyne "I was saving this for the last"
        Elsyne "We should hurry up then" 
        Elsyne "Come, let’s go!"
        Rai "(She suddenly became more cheerful when i mentioned about it)" 
        Rai "(I wonder what’s on there?"

        show rai_surprised 
        Rai "Ah, coming!"

        "The two of them quickly went and followed the river. Elsyne’s enthusiasm seems weird for Rai at first, but when they arrived at their final destination, everything cleared up."

        label R3scene9:
            #Waterfall
            #Waterfall crashing down

            show elsyne_smile 
            Elsyne "Here we are!"

            show rai_surprised 
            Rai "So... when you said it was more than a lake..."
            Rai "It’s actually a waterfall???"
            Elsyne "Yup"
            Rai "I don’t even remember how many times i feel amazed by the Farmland today..."
            
            show rai_excited 
            Rai "The farmland never ceases to amaze me!"
            
            show elsyne_happy 
            Elsyne "Glad you’re having fun"

            show elsyne_shy 
            Elsyne "When Ma told me to bring you around, i was afraid that you’ll feel bored with me"

            show elsyne_happy 
            Elsyne "But i’m glad that’s not the case"
            Rai "Bored?"
            
            show rai_excited 
            Rai "On the contrary, this might be the most exciting day i’ve ever had since i first came to the Farmland"
            
            show elsyne_smile 
            Elsyne "I see..."
            Elsyne "You know..."
            Elsyne "This waterfall might be my favorite place among everything else on the Farmland"
            Elsyne "Especially at night"
            Elsyne "Either after working, or after going on a hunt, for me, nothing can beat the feel of the waterfall at nighttime"
            Elsyne "Maybe we should go together sometimes at night"
            Rai "Sounds great!" 
            Rai "I’ll be looking forward to it"
            Elsyne "Now that we’ve seen everything, let’s go back"
            Elsyne "You must be tired for today right?"
            Rai "Yeah" 
            Elsyne "I can’t lie about that, it’s been a while since I walked this far"
            Rai "But you shouldn’t worry about me" 
            Rai "I’m fine and everything has been a blast today!"

            show rai_thinking 
            Rai "Ah right" 
            Rai "But does that mean we should walk all the way back through the river and forest again"
            Elsyne "No"
            Elsyne "There’s a shortcut actually"

            show rai_surprised 
            Rai "Wait, so we can actually go straight here from the farm without going through the forest and river?"
            Elsyne "Uh-huh"
            Elsyne "But since I'm giving you a tour today, it won’t be fun that way."
            Rai "That makes sense" 
            Rai "It’s getting late now, let’s get going."
            
            "Having ended their tour, the two of them went back to the farm, and parted ways there for today"

        label R3scene10:
            #shed

            "That night, Rai tried to recall today’s events before finally going to sleep."

            show rai_thinking
            Rai "(Hmm... Perhaps I have gathered some valuable information about my suspect after today.)"
            Rai "(I do recall something weird.)"
            Rai "(Firstly, when i talked about ‘a criminal who took thousands of lives’, she went quiet for a while.)"
            Rai "(I don’t know if she’s still being absorbed in the somber atmosphere from before.)"
            Rai "(Or if she’s hiding something.)"
            Rai "(And second, she hunts?)"
            Rai "(When we went to the forest earlier, i didn’t found a trace about a hunt or something like that)"
            Rai "(Unless if the hunter was the kind that can incapacitate or dispose of their prey easily without leaving a trace, like using some kind poison, perhaps?)"
            Rai "(Furthermore, she should be working at the Butcher’s from morning until a little past afternoon right? When did she find the time to hunt?)"
            Rai "(At dusk? Or maybe in the evening?)" 
            Rai "(And I also recalled that she often visited the waterfall at nighttime, maybe that was also connected?)"
            Rai "(I know I shouldn’t be that distrustful towards her, but i need to confirm this myself)"
            Rai "(Considering the type of person that she is, maybe a direct confrontation won’t work’)" 
            Rai "(Maybe I should try to investigate the forest at night?)"
            Rai "(But that could be dangerous though)"
            Rai "(Alright, that’s enough for today)"
            Rai "(I’m already feeling tired, and i need to wake up early tomorrow)"
            Rai "(Well, goodnight)"

            "Meanwhile, on Elsyne’s side"

            #village night
            show elsyne_default
            Elsyne "(Today was so much fun...)"
            Elsyne "(It’s been a while since i last interacted this much with a stranger ever since i came here)"
            Elsyne "(Rai... huh)"
            Elsyne "(I don’t think we’re just strangers anymore)"
            Elsyne "(A friend... maybe?)"

            show elsyne_sad
            Elsyne "(Do I really deserve this kind of happiness?)"
            Elsyne "(Even after everything that he said earlier today?)"
            Elsyne "(Someone like me who...)"
            Elsyne "(No, I shouldn’t think about that anymore.)"
            Elsyne "(I’m trying to live a new life here... even with this stained past.)"
            Elsyne "(And i also shouldn’t let him know the truth)"
            Elsyne "(About me...)"
            Elsyne "(About who I really am...)"
            Elsyne "(And about what i really am)"
            Elsyne "(I should protect this secret...)"
            Elsyne "(From Ma... From Rai... or from anyone...)"
            Elsyne "(At any cost.)"

        label R3scene11:
            #Farm
            show rai_default
            Rai "Here we go"
            Rai "That’s all for today"
            Rai "Ah that went faster than i expected"

            show rai_happy
            Rai "Siiir, i’m done for today"

            show farmer_default
            Farmer "Oh? Good job boy"
            Farmer "Very well then, you’re free for today"
            Farmer "Go rest up or something"

            Rai "(Heh, “Boy” huh?)"
            Rai "(So that means he didn’t see me as a kid anymore?)"
            Rai "(Wow, what with the sudden changes of heart)"
            Rai "Thank you sir!"
            Rai "Ah, i’ve been meaning to ask you this sir"
            Rai "I’m planning to go out tonight, may I borrow the flashlight that’s been stored in the shed?"
            Farmer"Hmm? Feel free to use it boy"
            Farmer "You’ve been a great help for me lately"
            Farmer "It would be hard for me to refuse, you know"
            Farmer "Oh, and may I ask where’ll you go tonight?"
            Farmer "It’s not like i forbid you to go anywhere"
            Farmer "But please, steer clear from the forest at night"

            show rai_nervous
            Rai "Ah it’s nothing much, i just want to look around"
            Rai "But i think i would need a lighting, just in case"
            
            show rai_thinking
            Rai "(Huh? Did he just say something about the forest at night?)"
            
            show rai_nervous 
            Rai "A-ah, and also if you don’t mind me asking sir."

            show rai_thinking 
            Rai "Why did you say to avoid the forest at night?" 
            Rai "Did something happen there lately?"
            Farmer "Well, going to the forest at night generally is a bad idea boy"
            Farmer "But lately, something has been sighted there at night"
            Farmer "Someone reported they saw a figure with a lot of tentacles sprouting from their back"
            Farmer "Even if the eyewitness said that the creature doesn’t seem to be dangerous because they didn’t attacked the witness"
            Farmer "But it’s better to be safe than sorry, you know"
            Rai "(A figure with a lot of tentacles huh...)"
            Rai "(That matched up with my report about the target)"
            
            show rai_serious 
            Rai "(I know I must be going in the right direction here"

            show rai_happy 
            Rai "Alright, thanks for the warning sir!"
            Rai "I’ll be sure to remember that"
            Farmer "Take care boy"
            Farmer "And i think that’s also all for today for me"
            Farmer "I’ll be going now, goodbye"
            
            hide farmer_default
            
            show rai_serious 
            Rai "Alright, I should start preparing right now"
            Rai "And maybe I'll go to the forest at around 9PM."

        label R3scene12:
            #Forest night
            #Owl voices

            show rai_serious
            Rai "Okay, here goes nothing"
            Rai "Luckily i still remembered my way around the forest, thanks to Elsyne"
            Rai "Let’s just go for a quick patrol for now"

            "After a while"
            
            show rai_thinking 
            Rai "(Hmm... so far there’s nothing out of ordinary)"

            show rai_nervous 
            Rai "(Except for this chill though...)" 
            Rai "(And this feeling of something watching you...)"
            Rai "(Maybe that was just my imagination"
            Rai "(I should just ignore that)"
            
            # [Rustling grasses]
            show rai_surprised 
            Rai "(What was that???)"
            Rai "(I swear there’s something from that direction...)"
            Rai "(I should check it out)"

            "Rai tried to sneak towards the direction that he believed that there’s something over there"
            
            Rai "(This might be a good spot to hide)"
            Rai "(And fortunately, i have dimmed my flashlight)"
            Unknown "I’m sorry, little one"
            
            # [Tentacle stabbing]
            Unknown "(Hmm? I can feel that something... no, someone’s nearby)"
            Unknown "(Urrghh... i can’t pinpoint what they are)"
            Unknown "(I might have used too much of my energy today)"
            Unknown "WHO’S THERE???"
            
            show rai_surprised 
            Rai "(Grrk)"
            Rai "(It can speak?)"
            Rai "(No, that voice... is that?)"

            "The unknown figure approached Rai’s hiding spot, but luckily, they didn’t notice him..." 
            "Or did they?"
            
            show darkelsyne_surprised
            Elsyne "(There’s nothing here...)"
            Elsyne "(But this feeling... it’s kinda familiar...)"
            Elsyne "(...No it couldn’t be???"
            Elsyne "(Him???)"
            Elsyne "Hnngh, i need to get away, fast"

            "The unknown figure suddenly fled with a blinding speed, but unfortunately, Rai already got an idea, about what is that figure"

            show rai_surprised 
            Rai "(No...)"
            Rai "(My eyes didn’t play a trick on me right???)"
            Rai "(That figure... and also that voice...)"
            Rai "(Is that...)"
            Rai "(Elsyne???)"
            Rai "(I should probably go back for now)"
            Rai "(Maybe tomorrow, i’m gonna confront her about it directly)"
            Rai "(For the sake of the mission..."
            
            "Having his doubt somewhat confirmed, the officer decided to end his investigation and went back to the Farm."
















    label ending:
    "Tamat"


    $ persistent.phase1 = False
    $ persistent.phase2 = False
    $ persistent.phase3 = True

    return