label phase1:
    play music audio.IPD loop
    scene IPD WORKPLACE
    with fade
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

    show Rai Default with dissolve
    Rai Default "Ah.. another day with my wife, Shigoto-san."
    Rai "Hmm, let's see what I have to do today."
    Rai "Man… It’s just the beginning of the day yet someone has already put this much paper here."
    Rai "I can’t work properly if my table is full of papers."
    Rai "I need to tidy it up a bit, I think I should put some of the papers in the drawer for the meantime."

    "While Rai was tidying up the papers that were on his desk, one of his Galilean coworkers came by his table."

    #Galilean 1 appear
    # N : easeinright itu dateng ngeslide dari kanan
    show Galilean_1 Default at left with easeinleft 
    show Rai at right with ease
    Galilean_1 "Good morning! Sorry to disturb you so early in the morning…"
    Rai "Oh! Good morning!"
    Rai "It’s okay. Is there something that I could help you with?"
    Galilean_1 "Ah yes, I’m just here to remind you about the meeting that we will be holding in a bit."
    Galilean_1 "Please don’t forget to bring the necessary files for it!"
    Rai "Thank you for the reminder. I’ll get it ready."
    Galilean_1 "Okay then, I shall excuse myself now. Have a good day!"

    hide Galilean_1 Default 
    with dissolve

    "As Rai gets back on his chair, he sees a post-it-note reminder on his PC screen to help fix the CCTV."
    "He can help fix the CCTV first, or attend the meeting first, or he can just ignore all of that and tidy up the files in his drawers."

    "Which one will he do?"
    menu:
        "Attend Meeting":
            jump scene1_intro

        "Fix CCTV":
            jump scene2_intro

        "Tidy Files":
            jump scene3_intro

    label scene1_intro:
        stop music
        play music audio.meeting_room loop
        scene Meeting Room
        with fade

        "Interdimensional Officers Discussion, an annual meeting with other branches to discuss progress between High-Ranking Officers in each branch."
        "Rai arrives with the file that his boss asked him to bring, he also made sure that he got a copy for everyone as well."
        "When Rai enters the meeting room he sees that no one is there except for his boss."

        show Rai Default at right with easeinright
        Rai Thinking "What happened Boss? Am I late?"

        show Boss DefaultSparkle at left with dissolve
        Boss    "No, the higher-ups suddenly rescheduled our meeting for next week due to the lack of some documents that we need."
        Rai Sad "Too bad, I was hoping I could be useful today Boss."
        Boss    "Don't worry, I already said that you eagerly wait for them."
        
        "Rai’s Boss reassures him with a shoulder pat."

        Boss "Is that the document that I asked you to fetch? It’s the notes for the meeting."
        Rai  "Yes it is Boss, here you go. Is there another task that you need me to do?"
        Boss "No, you may go."
        Rai Happy "Affirmative Boss."

        hide Rai Default
        with dissolve
        play sound audio.footsteps
        "Rai walks back to his office remembering that he wanted to tidy up the files that were on his drawers a while ago."
        
        #SFX Footstep
        #BG : Blackscreen
        stop music
        jump scene3_intro

    label scene2_intro:
        scene IPD WORKPLACE
        with fade

        play sound audio.knock
        "As Rai was about to go to the CCTV Room, he heard a knock"

        #SFX knock
        show Galilean_2 Default at right with easeinright
        Galilean_2 "Uhh sir? Forgive me for the intrusion, but I’m here to give you this. It's from the CCTV Operator Guy. He says to give it to you."

        show Rai Default at left with dissolve
        Rai Default "Oh, okay. Just put it on the table, thank you."
        
        Galilean_2 "Then, I'll excuse myself."
        hide Galilean_2 with dissolve
        show Rai at center with ease
        "After they left, Rai started reading the paper."
        "Need help in the CCTV Room -Artemisia"

        Rai "My god, I thought it’s a prank. Damn you Artemisia."
        play sound audio.footsteps
        "Rai laughs as he folds the paper neatly and walks towards the CCTV Room."
    
        #SFX Footstep
        #Blackscreen

        stop music
        play music audio.cctv_room loop
        scene CCTV
        with fade
        show Artemisia Default at left with dissolve
        Artemisia "Welcome sir, sorry to summon you with a piece of paper."
        show Rai Default at right with easeinright

        Rai Happy "Ah, you mean this?"

        "Rai shows the paper that has already been folded into a shuriken-shaped. He throws the shuriken across the room, making it fly and it returns neatly into his hand."

        Artemisia "Ohmagah, Milord… Ahem- I mean. Such a talent to neatly fold an origami and to make it fly like that."
        Rai "Oh don't flatter me, also this… origami thing you said? I learned it from the Youtube video you gave during my expedition in the Far East Dimension."
        Rai Serious "Anyway, what seems to be the problem regarding the CCTV?"
        Artemisia "Right. As I said from the message, there seems to be a problem with some of the CCTVs in certain spots. Here are the camera locations."

        "Artemisia shows a monitor with IPD camera layout."

        Rai Thinking "Hmm, the spot is kinda suspicious."
        Artemisia "What do you mean sir?"

        show Rai Serious 
        Rai "I saw it from my office. The CCTVs placements are too specific, as if it was purposely moved to create a blind spot. Maybe it’s just my imagination though. Forget it."
        Artemisia "I see. How observant of you sir."

        show Rai Excited 
        Rai "Aww hehe, I’ve been working here for so long that I feel like IPD is an extension of my body. So, where do I start?"
        Artemisia "Yes sir. Before that…"
        
        hide Rai
        hide Artemisia
        with dissolve
        #Blackscreen
        stop music

    label scene2_2intro:
        play music audio.IPD loop
        scene IPD WORKPLACE
        with fade

        show Rai Default with dissolve
        Rai Happy "Ah yes. More Shigoto-san. More work. Shigoto-san daisuki~"
        "Rai walks happily to the first camera. The first place is near the IPD Entrance."
        Rai Serious "Hmm, no wonder. The lenses are too dirty and the screws are also a bit loose. Luckily it’s a small maintenance."

        "Rai tinkers with the tools given by the Artemisia to repair the CCTV."
        "After he tightens back the screw and changes the lens, he reports back through the receiver to check if it’s working again or not."
        
        Artemisia Black "Looking good sir."
        Rai Happy "Okay, thanks Artemisia."

        "He does the same to the CCTV near the IPD Hall, the Receptionist, the Pantry, and the one in the Conference Room."

        Rai Default "Now, what should I do next?"

        "As Rai walks back, he sees a certain CCTV that’s badly damaged, it looks like it’s broken. As he approaches it a burnt smell emanates from it and he quickly reports it."

        Rai Nervous "I found one CCTV that smells burnt.. Is this one of the CCTV spots that you mentioned?"
        Artemisia "I think so, can you try to fix it?"
        Rai Thinking "Uhh… I’ll try."

        "Rai picks up the tools and starts to tinker with the CCTV, unscrewing the cover then slowly removing the cover lid. And he’s met with a bunch of complicated components. Lots of wired cables, a chipset, and many other things."

        Rai Default "I'm not sure what to do. Here is the photo of the inner CCTV that I mentioned."
        Artemisia "Wait, I think we have a manual for this in the drawers."
        Rai "A manual? I guess I can fetch it myself. Does this CCTV need to be immediately fixed?"
        Artemisia "You can take your time sir. This one is not that urgent. I will leave it to you, thank you for letting me know."
        Rai "Okay then. I'll pick up the manual later. Galilei out."
        hide Rai Default
        with dissolve
        Artemisia "Over and out"

        "After Rai re-screws the broken CCTV back. And walks back to his office to pick up the manual that’s on the drawers,"
        stop music
        jump scene3_intro

    label scene3_intro:
        play music audio.IPD loop
        scene IPD WORKPLACE
        with fade

        show Rai Surprised with dissolve
        Rai Surprised "!!!"
        Rai "Oh god When was the last time I opened this drawer?!"
        Rai "There could be an explosion of papers anytime now!"
        Rai "I’ll have to move the old files to the archive room or it’s gonna be even messier!"
        Rai Sad "Man, I did learn a few tips on how to tidy up files properly but then again this many is just ueee..."

        "After a while of ‘ueees’ Rai kinda successfully sorts out the files. There were a lot of bookbinders titled ‘ATHENEAN’ and some were marked as ‘GALILEAN’."
        "Both of them seem to be a big pile of paperworks, flash disks, SD Cards, and burnt clothes strapped in a plastic ziploc bag that looked like a confiscated item."
        "It was packed tightly in the corner of the drawer."

        Rai Happy "Oh wow, I forgot I saved this piece of burnt cloth during my time as an Athenean. Ah… Good old times."
        Rai Serious "It's been a long time ago since IPD accepted me. I remember when Boss gave me the codename RAI and placed me into the GALILEAN unit, Thus Rai Galilei was born! Hehe, what a time."

        "As Rai speaks to himself, he sips another cola while arranging the drawer."

        "He finds another peculiar book. It’s a dark-brown binder book, strapped with purple cloth, weaving an ‘ATHENEAN’ on its cover." 
        "The backside is a lot of hand-woven ribbon with colorful colors, mostly in red and blue."
        "When he flips it, one of the papers slips from the binder, Rai picks it up and reads the written text on it."

        Rai Excited "What's this… hmm.  It reads… 'It feels like a fairytale - Maxwell’."
        Rai Happy "Ah yeah, looking back, I do remember a bit when I was in the Athenean unit. Fine work, a good one. Yes yes, good memory indeed. Me likey."

        "Rai flips the binder book, reminiscing a lot about the job. After finishing with ‘ATHENEAN’, he picks up the ‘GALILEIAN’ one and starts to examine it."
        "The binder is in a hue color of black, brown and light yellow, kinda like a rusted steel. Complemented with a hand-woven gray ribbon as the strap circling around it, making it look like a chained book."

        Rai Happy "Ah, this book. It’s my favorite one. It made me feel like I was writing a new spell in my grimoires. Fuhahahahaha!"

        "Rai laughs hysterically for a sec. His chuuni sense is back."

        Rai Default "Ekhm. But really, looking at this, let’s see… Aha!"

        "As he slowly takes the polaroid photo of him and his coworker, celebrating his birthday in IPD."
        "It was completely dark that day because there was a jailbreak (which turned out to be a prank) and the inmates were creating a big mess by shutting down IPD’s electricity."

        Rai Excited "Naughty Inmates. Made us IPD wear night vision goggles for three days straight because of the power outage."
        "Still it was so fun, I felt like an espionage agent when that day happened. Working on my laptop at the corner of the office, completely with a night vision to maintain the surroundings, because they were playing hide and seek."
        "It ended up as a big surprise: ‘A Jailbreak Session’."

        "Rai laughs while remembering the photo."

        Rai Happy "But that trick won't happen again, right?"

        #SFX SIREN
        play sound audio.siren_loop
        "Suddenly IPD Siren rang loudly, notifying that there’s an inmate that successfully did a jailbreak."

        Rai Surprised "OH MY GOD, REALLY? Did I just jinx myself? I spoke too soon. Damn that disturbed my flashback."

        "Rai’s receiver turns on."

        Artemisia "Artemisia to Galilei."
        Rai Serious "Galilei Here."
        Artemisia "We need you to be in IPD Jail Hall ASAP"
        Rai "Northway or Southway, Artemisia?"
        Artemisia "Northway sir."
        Rai "I’m on my way."

        hide Artemisia
        hide Rai Serious with dissolve
        "Rai quickened his pace to Northway IPD Jail Hall."
        
    label scene3_2intro:
        stop music
        play music audio.IPD_cell loop
        scene Jail Red
        with dissolve
        
        #SFX RUNNING
        play sound audio.running
        "As Rai arrives, there were three Galileian and an Artemisia in there examining the recent jailbreak room."
        show Galilean_3 Default at left with dissolve
        
        show Rai Serious at right with easeinright
        Rai Serious "Data report. What’s the identity of the inmate? Did you see their number? Or anything?!"

        show Felix Default at center with dissolve
        Galilean_3 "Yes sir. His name is Felix Linx. According to his files he’s a half human, half cat hybrid with pink hair and three orange stripes on both of his cheeks"

        hide Felix Default
        show Rai Serious at right
        Rai "His codename?"
        Galilean_3 "Based on the mugshot and the data that we’ve got, we dubbed this Inmate as ‘Catboy Paradise’. Lately because he has spoken about ‘True Paradise’."

        Rai Thinking "Uhh, why does that codename sound so familiar?"

        show Artemisia Default with dissolve
        Artemisia "Pardon sir?"
        Rai "Nothing. Moving on, so that’s the suspect. Where’s his location? We can track him using his collar, right?"

        Galilean_3 "That was the plan, on the CCTV footage his collar is still on him but he somehow managed to deactivate it."
        Rai "Leave him to me, I’ll catch him."
        hide Galilean_3 at left with dissolve
        show Artemisia Default at left with ease
        Artemisia "What do you mean sir?"

        "As Artemisia is still questioning what Rai’s words mean, Rai starts to contact the main branch via his receiver. Inputting the combination that only a few officers know about."

        Rai "Rai Galilei to Center. Permission to perform IPD Protocol Code 008-Romeo Alpha India-777, for codename ‘Catboy Paradise’. Over and out."

        "As Rai finished his report, his partners were left speechless, still amazed with what he just spoke."

        Artemisia "Wait, that code. Does that mean…?"
        Rai "Yes. It is like what you thought, Artemisia. I will go after him myself."
        Artemisia "Very well sir. We’ll provide you with the latest escape route of the inmate. It seems he ran away to code 611-813 Dimension aka the Farmland Dimension. We’ll leave him to you."
        #Blackscreen
        #GO TO INMATES#1 ROUTE
        # This ends of intro/prolog
        stop music
        jump scene1_1

    #Mulainya pengejaran sus pertama yaitu Felix
    label scene1_1:
        play music audio.farm loop
        scene Farm
        with fade
        
        "It is a peaceful morning in Farmland. The sun had just climbed out of its hiding. Its warm light dyed the sky a yellowish orange."
        "It seemed like a normal morning, but an interdimensional portal near a barn, which isn’t normal."
        "A young man walked out of it and looked around."

        show Rai Default at center with dissolve
        Rai Default "The air is kinda cold..."
        Rai "Hm, is that a barn?"
        Rai Excited "I don’t see any houses, so maybe it’s only the farmer here… which makes my job easier."
        Rai Happy "Less possible suspicion. Good, good."
        Rai "Even if the inmate’s not here, maybe I can dig some information about this dimension from the farmer."
        Rai Excited "Alright, I should change my clothes"
        Rai "Undercover field mission starts!"

        #From here use farmer  rai sprite
        #screen fade to black
        #stop music

        #play music audio.Farm loop
        scene Farm
        with fade
        #SFX FOOTSTEPS
        play sound audio.footsteps_grass
        FRai "There’s really no one else outside.."

        show FRai Default with dissolve
        play sound audio.farm_animals
        FRai Nervous "It’s kinda creepy… at least there’s animals. I can see them."

        ##[SFX chicken noises, duck quacking, horse neighing, sheep baa-ing, cow moo-ing (all noises at once, chaotic)]
        FRai Surprised "Whoa, wha-"

        #SFX #[SFX barn door opening]
        play sound audio.barn_door
        show Farmer Default at right with easeinright
        show FRai Default at left with ease

        FRai Nervous "H-hello, sir. Good morning."
        Farmer "What are you doing here? Who are you?"
        FRai "My name is Rai. I.. would like to take a look around this farm, sir."
        Farmer "A visitor, this early?"
        FRai "Well..I am actually new here"
        FRai "I’m interested in being a farmer, sir. So i kinda want to know what a farmer’s work is like"
        FRai "If you allow me, I would like to see everything in this farm up close!"
        Farmer "Hmm…"
        FRai "I just want to study. If you don’t mind, sir, could you let me stay here for a while to train myself? I’d sleep in the shed!"

        FRai "'Please be convinced.'" #ngomong dalam hati?

        Farmer "Hmm, well.. if you say so"
        Farmer "Having an assistant for some time would be nice.."
        Farmer "Wait here."

        hide Farmer Default with dissolve
        ##[SFX footstep, followed by SFX barn door opening]
        play sound audio.footsteps

        play sound audio.barn_door

        show FRai Default at center with ease
        FRai Thinking "?"

        #SFX FOOTSTEPS
        play sound audio.footsteps
        show Farmer Default at right with easeinright
        Farmer "Here you go!"
        FRai "Seeds?"
        Farmer "For your first lesson, go feed the animals. And make sure they don't jump out of their fence."
        Farmer "Oh, and, the hay for horses is right next to their field fence."
        Farmer "The sheeps are eating every time with grass in their fence, so don't worry about them."
        FRai "What about the cow over there?"

        show Cow WyenColor at left with dissolve
        Cow "Moooo" #Cow (Wyen’s cow form)
        Farmer "I’ll take care of the cow."
        FRai "Okay then!"
        FRai Nervous "Wait, are you not gonna teach me?"
        Farmer "It’s your first task, and an easy one. What could go wrong with it anyway?"
        Farmer "Also, I got work to do. Just make sure you don’t give the chickens too much food. Good luck!"
        Farmer "I’ll be right back."
        FRai Surprised "Ah, wait!"
        Farmer "Hmm? Is there anything you need?"
        FRai Nervous "Uh, um, Like i said, I just came here not a long time ago, so I’m not really familiar with all the places here."
        Farmer "Sorry i can’t show you around for now, i need to grab some water from the well."
        Farmer "Though, I have a map if you need it! Here."
        FRai Happy "Ah! Thank you very much!"
        Farmer "You’re welcome."
        Farmer "Alright, I have to go now. Good luck on your task!" #Farmer gone?
        hide Farmer Default
        hide Cow WyenColor 
        with dissolve
        ##[SFX running away footsteps]
        play sound audio.running

        FRai "Got it"
        FRai Surprised "...wait, I’m supposed to search for clues and find the runaway inmate!"
        FRai "I should search the whole farm.. guess I have to do it and feed all the animals at the same time."
        menu:
            "Feed ducks" if bebek == False:
                $bebek = True
                jump scene1_1_1

            "Feed horses" if kuda == False:
                $kuda = True
                jump scene1_1_2

        #Blackscreen
        label scene1_1_1:
            #play music audio.Farm loop
            scene Farm
            show FRai Default 
            with dissolve
            FRai Default "Here you go duck."
            #[SFX ducks quacking]
            play sound audio.ducks

            FRai Excited "Alright, while they’re busy eating.. I’ll search this field!" #ngomong didalam hati?
            Rai "Hm.. it's just grass here."
            Duck "Quack!"
            Rai "I don't speak duck language."
            Ducks "Quack quack!"

            FRai Sad "I don't understand.."
            Farmer "The ducks like you, lad." #Farmer back?

            show FRai Surprised at left with ease
            show Farmer Default at right with dissolve
            FRai Surprised  "Whoa! Since when are you here?"
            Farmer "Just now, haha."
            FRai "You can understand these ducks?"
            Farmer "Hm, you could say so."
            Farmer "I don't understand their language of course, but I've been living with animals for a long time already."
            Farmer "I know what they're trying to say from how they act."
            Farmer "These ducks don't usually quack at strangers. But they don't seem to have a problem with you being here."
            Farmer "Them quacking at you means they like you."
            FRai Happy "The ducks like me..!"
            Ducks "Quack quack!"
            FRai "By the way, sir. Why aren't these ducks in water?"
            Farmer "Ducks can swim, yes, but they mainly live on land."
            FRai "Ooh, I see."
            Farmer "How's your first job going?"
            FRai "So far so good."
            FRai "These ducks are friendly."
            Farmer "That's good to hear."
            FRai "I'll go feed the other animals now!"
            Farmer "Alright! I'm always around the shed, so go there if you need my help."
            FRai "Okay!"

            hide Farmer with dissolve

            if bebek == False:
                $bebek = True


            if bebek == True and kuda == True:
                jump scene1_2
            else:
                jump scene1_1_2

        label scene1_1_2:
            #play music audio.Farm loop
            scene Farm
            show FRai Default 
            with dissolve
            FRai Default "Hello, horses. How’s your day?"

            play sound audio.horse #[SFX horse noises]
            "Hrrreeuuhh"
            FRai "Wow, you don't sound okay. You must be hungry."

            play sound audio.horse #[SFX horse noises]
            "Hrghheeuuh"
            FRai "Here's your breakfast!"
            play sound audio.horse#[SFX horse noises]

            FRai Excited "'Okay, time to search!'"
            FRai "'Maybe there's something in the grass.'"
            play sound audio.horse
            FRai "Hmm? Is there something?"

            #[SFX footstep on grass]
            play sound audio.footsteps_grass
            FRai Surprised "Who's there?!"
            FRai Serious "...."
            FRai Thinking "'Maybe it's just my imagination.'"
            FRai "'This is an open field, there's nowhere to hide.'"
            FRai "'But if it is a person, then that person is very fast.'"
            FRai "'Whatever. I have to go feed the other animals.'"

            if kuda == False:
                $kuda = True


            if bebek == True and kuda == True:
                jump scene1_2
            else:
                jump scene1_1_1

    label scene1_2:
        #play music audio.Farm loop
        scene Farm
        play sound audio.chickens
        #[SFX chicken noises]
        show FRai Default 
        with dissolve
        FRai Default "Alright, chickens. Breakfast time!"

        #[SFX chicken noises but louder]
        play sound audio.chickens
        FRai "Whew, there’s more chickens than I thought."

        #[SFX chicken noises but even louder]
        play sound audio.chickens

        FRai Annoyed "You’re all so noisy.. Is the food not enough?"
        FRai "Alright, I’ll give you a bit more, so calm down."
        FRai "Hey, no need to fly- wait what-"

        #[SFX chicken noises but EVEN louder and chaotic]
        play sound audio.chickens
        FRai Surprised "Wait.. stop.. there’s enough for everyone-" with vpunch
        FRai "OW- AAAAARRRGGHH" with vpunch

        show Farmer Default at right with easeinleft
        Farmer "What happened?!"
        FRai "Mr farmer! Help me!!"

        #[SFX chicken noises]
        play sound audio.chickens
        Farmer "Shoo, shoo!"

        #[SFX chicken noises]
        play sound audio.chickens
        Farmer "Calm down! I’m here, okay?"

        #[SFX chicken noises but less loud]
        play sound audio.chickens
        FRai "Phew.."
        FRai "Are the chickens always like this?"
        Farmer "No.. they're usually not like this."
        Farmer "They are noisy when there’s a stranger, but If I’m here, they always calm down right away."

        show FRai Nervous at left with ease
        FRai Nervous "That’s weird.."
        Farmer "They might be warning me about something."
        FRai "Something? Or.. Someone?"
        FRai "But I didn't see anyone!"
        FRai Thinking "'Could it be the inmate..?'"
        FRai "'Then, what I heard when I was feeding the horses.. aren’t my imagination?'"
        FRai "'Ill have to go search later.'"
        Farmer "What’s with that face?"
        FRai Surprised "Huh?"
        Farmer "Ha.. Maybe the chickens were just left with no food for a bit too long"
        FRai Nervous "Well.. It could be"
        Farmer "By the way!"
        Farmer "Is your job done?"
        FRai "Ah, yes! I’ve done it!"
        Farmer "Good, good."
        Farmer "Here's some money. Go buy breakfast at the market."
        FRai Happy "...thank you!"
        Farmer "I gave you a map, right?"
        Farmer "Always carry it with you so you won’t be lost."
        FRai "Yes, I will."
        FRai "I'll go to the market later."
        Farmer "Why not now?"
        Farmer "It’s past the time for breakfast already. Or have you eaten breakfast?"
        FRai Nervous "Well, I.. I think I’m gonna hang around in the farm for a while."
        Farmer "Adjusting yourself with the farm life, huh?"
        FRai "Kinda"
        FRai "'There’s no way I’m telling him I’m actually searching for a runaway inmate..'"
        Farmer "Take your time then."
        Farmer "If you want to go somewhere else too, then feel free to do so."
        FRai "Okay!"
        Farmer "I'll be going to feed the cow. Good luck on your search!"
        FRai "Thank you!"

        #[Screen fades to black]
        #play music audio.Farm loop
        scene Farm
        with fade
        show FRai Thinking with dissolve
        FRai Thinking "'Hmm..'"
        FRai "'The sound i heard while feeding the horse ealier..'"
        FRai "It could actually be the inmate, cats are fast to move from one place to another places. Cat-people must be fast too.'"
        FRai "'I’ve been searching around this farm, but seems that there really is no one else here.'"
        FRai "'Oh right, the map.'"
        FRai "'Let’s see..'"

        #[SFX paper unroll (srek)]
        play sound audio.paper_unroll
        #[Asset: Farmland map start]
        show black
        show Maps at truecenter 
        with dissolve

        FRai "'Hmm, there's a river near the forest.'"
        FRai "'Knowing his past crime, maybe he’s searching for fish?'"
        FRai "'Then, he might be there.'"
        FRai "'Or at the market, at a fish shop.'"
        FRai "'The forest could be a nice hiding place too, I should go and search it.'"

        #[Asset: Farmland map end]
        #[Screen fades to black]

        scene Farm
        with fade
        show FRai Serious
        FRai Serious "'I’ll go to the market first.'"

        show FRai Thinking
        FRai Thinking "'Oh wait. What about the farmer?'"
        FRai "'I have to tell him I'm going out, or he might be suspicious of me.'"

        #[Screen fades to black]
        scene Farm
        with fade
        show Farmer Default at right
        Farmer "Oh, you're back! How’s your search?"

        show FRai Sad at left with easeinleft
        FRai Sad "No result.."
        Farmer "See, it’s probably just random people."
        show FRai Nervous
        FRai Nervous "Yeah.."
        FRai "Um, sir-"
        Farmer "It’s way past breakfast time already. You should go to the market now!"
        FRai "Oh, right! I’m going. Bye-bye!"
        Farmer "Come back in time for lunch! Byee!"

        stop music
        #[Screen fades to black]
        play music audio.market loop
        scene Market
        with fade
        show FRai Happy with dissolve
        FRai Happy "'He told me to go to the market when I was about to say so. What a coincidence!'"

        #[SFX people chattering]
        play sound audio.people_chattering_loop
        FRai "'Wow, it sure is crowded here.'"

        #[SFX tummy growl]
        play sound audio.tummy_growl

        FRai Sad "'I’m hungry.. I wanna buy some food.'"
        FRai "'Good thing I have money.'"
        FRai Happy    "'Oh hey, a bread seller!'"
        FRai          "Hello there, little miss! Can I get some bread?"
        Bread_Seller "Here you go! It'll be 3 coins."
        FRai          "3 coins.. here!"
        FRai          "Mm, these breads smell good!"
        Bread_Seller "Hehe, I made these myself."
        FRai          "Whoa.. amazing!"
        Bread_Seller "Thank you!"
        FRai          "Ah, um, by the way, is there a fish shop or someone who sells fish around here?"

        "The girl points at a two floored shop."

        Bread_Seller "That building over there."
        FRai         "Thank you!"
        
        #[Screen fades to black]
        stop music
        play music audio.fish_shop loop
        scene Fish Shop
        show Fisherman Default at right
        with fade

        play sound audio.footsteps
        #[SFX footstep]
        Fisherman "AAAAAAAAAAAHHH!!! MY FISHH!!!" with vpunch

        show FRai Default at left with easeinleft
        FRai Surprised "?!"
        Fisherman "MY FISH WERE STOLEN! MY FISH!!"

        show MeatButcher Blood at center with dissolve
        Meat_Butcher "Ugh, just shut up already! It was like fifteen minutes ago and you’re still bringing that up?"
        Fisherman "A HUGE TIGER STOLE MY FISH!! He should pay.. he should pay!"
        Meat_Butcher "If you want to make him pay, then get moving! You’re not doing anything at all!"
        Fisherman "Ouch, how mean…"
        show FRai at center with ease
        FRai "Um, excuse me!"

        show MeatButcher Blood at left with ease
        FRai "Sorry for interrupting, but can you tell me more about the stolen fishes?"
        Meat_Butcher "And who are you?"
        FRai Excited "Ah, I’m just someone curious. And maybe I could help!"
        Meat_Butcher "This is none of your business."
        Fisherman "Oh, finally a good and kindhearted person!"
        Meat_Butcher "Haaaa?!"
        Fisherman "*gulp*"
        FRai Nervous "Uh.."
        FRai "Um, could you tell me more about the stolen fishes, sir?"
        Fisherman "My fish, my precious fish were stolen!"
        FRai "Please explain it in detail, sir."
        Fisherman "Not so long ago, a biiig scary tiger entered my shop, and snatched some of my fish away!"
        FRai Annoyed "In even more detail, sir."
        Meat_Butcher "It’s useless."
        FRai "Oh?"
        Meat_Butcher "So, around fifteen minutes ago, a catboy came to this shop."
        Meat_Butcher "He has messy pink hair. "
        FRai Serious "‘The inmate..!’"
        Meat_Butcher "At first he seemed like a normal customer, but then he grabbed some fish and ran out immediately."
        FRai "So you were here when it happened?"
        Meat_Butcher "Yep."
        Meat_Butcher "And he’s fast. There were some people in and outside this shop, but nobody could catch him."
        FRai Thinking"I see.."
        Meat_Butcher "So? You’re gonna find him?"
        FRai "Yes. I said I would help."
        Fisherman "You really will help me?!"
        Fisherman "Such a good person! What can I do without your help..! Thank you, thank you!"
        FRai Nervous "Ahaha, you’re welcome."
        FRai "I’ll go search for the thief now. I’ll be back soon."
        Fisherman "Safe travels!"
        Meat_Butcher "It’s not like he’s gonna come back next week…"

        #[Screen fades to black]
        stop music
        play music audio.market loop
        scene Market
        with fade
        FRai "Have you seen a cat boy around here, sir? He has pink and bushy hair."
        Merchant "Catboy..? Nope."

        show FRai Sad with dissolve
        FRai Sad "Alright…"
        FRai "Please tell the Fisherman at the fish shop if you spot him!"
        Merchant "...hm."

        show Felix Smirk at right with dissolve
        Felix "Heh, you’re too slow..." #he just gone or what?
        hide Felix Smirk with dissolve

        play sound audio.footsteps
        #[SFX footstep]

        FRai "Ah, hello, miss! Have you seen a cat boy around here? He’s pink and bushy haired."
        Man "No, sorry." #Random person?????
        FRai "I see, alright.."
        FRai "Please tell the Fisherman at the fish shop if you see him!"
        FRai Annoyed "'Aaagh, I’ve been searching everywhere and asked everyone I see, but he’s nowhere!"
        FRai Serious"'But I can’t give up!'"
        FRai "'I have to ask more people.'"
        FRai "Hello, miss! Have you seen a catboy around here? He has pink and bushy hair."

        show FRai Annoyed at right with ease
        show Villager Default at left with dissolve 
        Villager "Umm, yes?"
        FRai "Where?!"
        Villager "Uh, there…"
        Old_Lady "AAAAAHH! THIEF!!" with vpunch #Sound only? also this is soud of Old lady
        
        
        show FRai Default at center with ease
        FRai Surprised "Wha-"
        
        stop music
        play music audio.Felix loop

        show Felix Default at right with dissolve 
        show FRai Serious
        FRai Serious "You..!"

        Felix Surprised "Hmm?"
        FRai "Don't move!"
        Felix "What do you mean don’t move? You’re threatening me?"
        Felix "You don’t even have a weapon."
        FRai "Ugh.."
        Felix Smirk "Aha. Are you gonna catch me?"
        Felix "Catch me if you caaan!"

        #[SFX running footsteps]
        play sound audio.running
        FRai "You’re not going away!"
        play sound audio.running
        #[SFX running footsteps]
        #[Screen fades to black]

        scene Market
        show FRai Annoyed
        with fade
        #[SFX running footsteps]
        play sound audio.footsteps

        FRai Annoyed "Huff... huff…"
        FRai "So.. tired…"
        FRai "‘Where is he going..?’"
        FRai Surprised "!!!"
        Felix Default "Heh. You were so focused on chasing me, you don’t realize I’m leading you to a corner."
        Felix "Well, good luck chasing me, if you can. Byeee!"

        "The inmate climbed up the walls and left."

        FRai Annoyed "'Aaargh, how didn’t I realize?!"
        FRai "‘There’s no way I can chase him now.. I’m too tired to keep on running.’"
        FRai Thinking "Now what do I do?"
        FRai "‘He can be hiding anywhere right now. It’s been a while since he left. With that speed, he must’ve gone far away.’"
        FRai "‘This is very close to the village.. he could be there.’"
        FRai "‘But what if he went the opposite way instead? He might even be hiding in the forest.’"
        menu:
            "Reminicence":
                jump scene1_2_1
            "What if he isn't in the village?":
                jump scene1_3

        label scene1_2_1:
            #Fadeout Blackscreen
            #Flashback Filter? using tint/swirly effect?
            scene Market Grayscale
            show FRai Grayscale
            with fade
            FRai GDefault "Please tell the Fisherman at the fish shop if you spot him!"

            jump scene1_3

    label scene1_3:
        #play music audio.market loop
        scene Market
        show FRai Default
        with dissolve
        FRai Thinking "‘If the inmate is back to the market.. I’ve told everyone to go to the fish shop if they see the inmate, so I’ve got more eyes to help me.’"
        FRai "‘And maybe the people at the market can catch him..’"

        #[Flashback filter]
        scene GFish Shop
        show MeatButcher GDefault
        with fade
        Meat_Butcher "And he’s fast. There were some people in and outside this shop, but nobody could catch him."

        #[Screen fades to black]
        scene Market
        show FRai Default
        with fade
        FRai Nervous "‘Hopefully.’"
        FRai "‘But I think it’s safe to go to the village and search.’"

        #[Screen fades to black]
        stop music
        play music audio.village loop
        scene Village
        with fade #deleted?

        #[SFX people chattering]
        play sound audio.people_chattering_loop
        FRai "‘Wow, it’s crowded in the morning.’"

        #[SFX 2 people bumping into each other]
        show FRai Default at right 
        show Villager Default at left
        with dissolve
        show FRai at center 
        show Villager at center
        with ease

        play sound audio.bump
        FRai Surprised "Uwah-" with vpunch
        show Villager Default at left with ease
        Villager "Aaaah! I’m so sorry!" 

        show FRai Nervous at right with ease
        FRai Nervous "Ah, no, it’s my fault. I was spacing out and didn’t notice you."
        FRai "Wait, you’re the one at the market!"
        Villager "Oh! I remember you!"
        Villager "You asked me something about a catboy."
        FRai "Right, the catboy-"
        Villager "Ah, um, as an apology for bumping into you, I’ll give you a potato!"
        FRai Nervous "No need to-"
        Villager "Here you go! Fresh potato!"
        FRai "Um, you don’t need to…"
        Villager "No, no, please take it!"
        
        #[SFX tummy growl]
        play sound audio.tummy_growl
        FRai Happy "...Thank you!"
        Villager "So you’re hungry! Good thing I gave you the potato. Eat up!"
        FRai Nervous "..."
        FRai "It’s raw..."
        FRai "I can’t eat it.."
        Villager "..."
        FRai "..."
        Villager "Want me.. to cook it for you?"
        FRai "‘I need to hurry, but I’m really hungry.. It’s time for lunch already.’"
        FRai Happy "..If you don’t mind!"
        Villager "It’s ok! My house is right there. Follow me!"

        #[SFX footsteps]
        play sound audio.footsteps

        #[Screen fades to black]
        show Village
        with fade
        #[SFX footsteps]
        show Villager Default at left with dissolve
        Villager "I’ll boil the potato. Wait here, it won’t take long!"
        FRai "Okay."

        show FRai Default with dissolve
        FRai Sad "‘Too bad I can’t taste the farmer’s cooking…’"
        FRai "But at least I can still have lunch."

        #[SFX water blub blub]
        play sound audio.water_boiling
        "Rai sat on a bench, right below the kitchen window. The window is wide open. The sound of boiling water can be heard from inside the kitchen."

        #[SFX footsteps]
        play sound audio.footsteps
        Villager "Here’s the potato!"
        FRai Happy "Thank you!"

        #[SFX munching potat]
        play sound audio.munching_potat
        FRai Serious "By the way.. have you seen the catboy in this village? The one at the market."
        Villager "Hmmm..."
        Villager "I don’t."
        FRai Sad "Oh."
        Villager "Ah,um, don’t be sad!"
        Villager "Here’s the thing, there’s people guarding the village entrance."
        Villager "They tell nearby villagers whenever there’s a visitor, a.k.a people who don’t live in this village, then that will be relayed to the whole village."
        Villager "So the whole village would’ve known if the catboy was here."
        FRai "Huh? I didn’t see any guards when I came here."
        Villager "Because the guards look like any other villagers."
        Villager "They don’t stop and interrogate every single person who comes, but they always watch over the entrance."
        Villager "Like I said, they tell nearby villagers whenever there’s a visitor, then those villagers tell the other villagers about the visitor."
        Villager "So the whole village would’ve known if there’s someone visiting, like you."
        FRai Surprised "Are you saying the whole village knows I’m here now?"
        Villager "Yep!"
        FRai "I see.."
        FRai Default "By the way, I have something to ask." #FRai default?
        Villager "Yes?"
        FRai "Is it hard to find a way in the forest?"
        Villager "Oh, you wanna go to the forest?"
        FRai "Yeah."
        FRai "‘Since the inmate isn’t here, I have to get moving.’"
        Villager "I’ve never wandered around the whole forest, but I heard there’s a path you can follow. And there’s a talking tree that can help you if you’re lost!"
        FRai Surprised "Talking tree?"
        Villager "Yep! It’s a myth, but it may be true, who knows!"
        FRai Nervous "Ahaha.."
        Villager "Sorry I can't help you much."
        FRai "It’s alright! You helped me a lot already! You gave me food and told me what I need."
        Villager "Mhm!"
        FRai "I gotta go now. Thank you for the potato and everything! Bye-bye!"
        Villager "Oh, bye-bye!"

        #[Screen fades to black]
        stop music
        play music audio.forest loop
        scene Forest
        with fade
        FRai "Hmm, it’s pretty hard searching with all these trees everywhere.."
        FRai "And I can’t see the path."

        show TalkingTree Default at right with dissolve
        Talking_Tree "Goood daaaayy, my child… Yoooourr faaacee loookss liiikeeee youuu cooulddd useee soomeee heeeelp..!"

        show FRai Default at left with easeinleft
        FRai Surprised "EEEEE?!" with vpunch
        FRai "‘The talking tree.. you’re real!"

        #[CG 1 START]
        show CG1 with dissolve
        $ persistent.cg1_unlocked = True
        Talking_Tree "Ha-ha-ha. Iiii ammm, myy chiiild.."

        #show FRai Surprised
        FRai Surprised "Wow.. you’re huge.."
        FRai "Someone told me you help people that get lost in this forest."
        Talking_Tree "Whyyy, haaavee youuuu looost yooouur waaay, myy chiiild…?"
        FRai "I think so."
        Talking_Tree "Waaallkk toooo yooouurr leeeftt..!"
        Talking_Tree "Thaaaat waaayy yooouuu wiiiill approooaaachh theee paaathh oooof thiiiss fooooreesst.."
        FRai Excited "Okay!"

        #[CG 1 END]
        hide CG1 with dissolve
        #[SFX footsteps]
        play sound audio.footsteps

        show FRai Default
        FRai Happy "Oh, there it is!"
        Talking_Tree "Oooohh, yooouu haaaveee diiiscoooveered theee paaathh…"
        FRai Surprised "Whoa, you can see me?"
        Talking_Tree "Iiiii aaamm veeerryy taaallll, myyy chiiildd, Iiii caaan seee yoouuu frooom heeeree… Iiii caaann viiieeeww eeeverythiiing iiinn thiiiss foreeesst..."
        FRai Excited "So cool..!"
        Talking_Tree "Ha-ha-ha…!"
        FRai "Hmm?"
        Talking_Tree "Whaaatt isss iiiitt, myyy chiiildd…?"
        FRai "There’s something on this tree.."

        #[Asset Scratches on tree]
        show black
        show Scratches Zoom at truecenter 
        with dissolve
        FRai Thinking "Scratches.. it could be caused by the inmate, or a wild animal."
        #[Asset Scratches on tree]

        #[Screen fades to black]
        #play music audio.forest loop
        scene Forest
        show FRai Default at left
        show TalkingTree Default at right
        with fade

        FRai Default "Mr Talking Tree, do you know who did this?"
        Talking_Tree "Oooohh yeeess Iiiii doooo, myyy chiiiildd.."
        Talking_Tree "Aaaaatt daaawwnn, theeereee waasss aaaa feeeliiinee laaaadd waaandeeeeriingg iiinn thiiiss fooorreeesst…"
        FRai Thinking "Feline lad? The catboy?!"
        FRai "Does he have pinkish bushy hair?"
        Talking_Tree "Heeee dooeeess...!"
        FRai "So he was here!"
        FRai "What’s with the scratch though?"
        Talking_Tree "Iiii scaaareeedd hiiimm oofff! Heeee weeentt awaaayy iiinn hoorrooor..! Ha-ha-ha…!"
        FRai Happy "You like to play tricks, huh?"
        Talking_Tree "Iiii maaayy beee aaancieeent, buuut thaaaat wiiill neeeveerr hiiindeer myy frooliic…! Ha-ha-ha…!"
        FRai "Oh? How old are you, if.. you don't mind telling?"
        Talking_Tree "Hmmmmmmmmmmm…"
        Talking_Tree "Iiii dooo nooott knoooww.. Iiii haaavee beeenn heereee siinceee theeee aaancieeennt tiiimeeess..!"
        Talking_Tree "Iii doooo noooot reemembeer.. hooowww looongg Iiii haaaveee stoood…"
        FRai Surprised "Ooh.."
        FRai Thinking "Hmm, do you know what is the catboy here for, sir?"
        Talking_Tree "Theee feeliineee seeemed tooo beee seeeaarchiing fooor sooomeethiing..! Iiiii dooo nooot knoooww whaaatt iitt iiiiss…"
        FRai "I see…"
        FRai "Mr talking tree, you can see this whole forest, right? Is the catboy here?"
        Talking_Tree "Iiiii doooo nooott seee aaaa caaatbooy, myyy chiiildd…!"
        FRai "What about the river? Can you see anyone from here?"
        Talking_Tree "No ooonee iisss theeeree..! Eemptyyy…!"
        FRai "Alright. Thank you, Mr. Talking tree."
        Talking_Tree "Areee youuu gooiiing tooo deeepaaarrt noooww, myy chiiildd..?"
        FRai "Yeah. I have to meet someone."
        Talking_Tree "Iiitt haaass beeen aaa greeaat deeliightt taaalkiiingg tooo yooouu, myyy chiiildd.. Iiitt haaass beeen aaaa looongg tiimeee siincee Iii laasstt haaadd aaa taalkk wiithh aanyoonee.."
        FRai Happy "Thank you for helping me too."
        FRai "Bye-bye, Mr talking tree!"
        Talking_Tree "Faaareeweell, myy chiildd…"

        #[SFX running footsteps]
        
        FRai Serious "‘I left the market for hours already. I have to go back!"
        play sound audio.running
        #[Screen fades to black]

        stop music
        play music audio.fish_shop loop
        scene Fish Shop
        show Fisherman Default at center
        with fade
        show FRai Default at right with easeinright
        FRai Serious "I’m back! Any news?"
        Fisherman "This is terribly painful, but I have to say, there is no news."
        FRai "I see.."
        FRai "I’ll go search again."
        Fisherman "..."

        #[SFX footsteps]
        play sound audio.footsteps

        show MeatButcher Default at left with dissolve
        Meat_Butcher "Hey."
        Meat_Butcher "You.. Why do you actually want to help? You got too much freetime?"
        FRai "Maybe."
        Meat_Butcher "...."
        FRai "..Miss. Do you not trust me?"
        Meat_Butcher "Yeah, well.. you're pretty suspicious."
        Meat_Butcher "You came outta nowhere and just said you want to help."
        FRai Nervous "Ahaha.."
        FRai "'I hope she doesn't find out about my mission..'"
        Meat_Butcher "But, if you really want to help.."
        Meat_Butcher "That's very.. kind."
        FRai Nervous "..."
        FRai Happy "Thank you."
        FRai "I’m going to search more."

        #[SFX footsteps]
        play sound audio.footsteps

        hide FRai Default with dissolve
        show Fisherman Default at right with ease
        Fisherman "I’m going. I must help him."
        Meat_Butcher "Huh? Hey, wait!"
        Meat_Butcher "..."
        Meat_Butcher "I'm going too!"

        #[Screen fades to black]
        stop music
        play music audio.market loop
        scene Market
        show FRai Default
        with fade
        #[SFX running footsteps]
        play sound audio.running
        
        FRai Serious "‘Where.. where is he..’"
        "AAAAAAAHH!! THIEF!! HELP!" with vpunch #the sound of Lady
        show FRai Default at right with easeinright
        FRai Surprised "‘What, again?’"

        stop music
        play music audio.Felix loop
        show Felix Default at left with easeinleft
        Felix "It’s you again..."
        Felix Smirk "You’re never gonna catch me!"

        #[SFX running footsteps]
        play sound audio.footsteps
        FRai Serious "I will this time!!"

        #[SFX running footsteps]
        play sound audio.footsteps
        "Chase scene ensues. The police officer and the inmate are running, jumping, and parkouring through the crowded market."
        FRai Serious "Excuse me!"
        "Whoa!!" with vpunch #the soud of Lady
        FRai "I’m sorry- whoa!"
        "Whoaah!" with vpunch #the sound of Children
        FRai Nervous "‘Oh my God, I almost hit those children!"
        Felix "Ahaha! You can’t catch up to me, don’t you?" #show Felix Smirk?
        FRai "He’s too fast..! I have to do something to slow him down!"

        label scene1_3_1:
            scene Market
            show FRai Default at right
            with fade
            FRai "‘Wood plank..!’"
            #[SFX wood planks falling]
            play sound audio.wood_planks_falling
            FRai Serious "This is gonna hurt!"

            #[SFX wood plank go whoosh]
            play sound audio.wood_planks_falling
            show Felix Annoyed at left with dissolve
            Felix Annoyed "Ugh-!" with vpunch
            Felix "‘My back..!’"
            FRai Excited "‘Now’s my chance!’"

            #[SFX running footsteps]
            play sound audio.footsteps
            Felix "‘Crap, he’s catching up!’"
            Felix "‘I can’t let it happen!’"
            #[SFX wooden barrel falling harshly (tabrak tabrakan)]
            Felix Smirk "My turn!"
            play sound audio.wooden_barrel_falling
            FRai Surprised "Whop-" with vpunch

            menu:
                "Evade":
                    jump scene1_3_1a1

                "Defend":
                    jump scene1_3_1a2

                "Attack":
                    jump scene1_3_1a3

            label scene1_3_1a1:
                scene Market
                "Rai jumps as high as he can, avoiding the wooden barrels rolling towards him. He fell a few times but that’s okay."

                #[SFX landing after jumping]
                play sound audio.landing_floor

                show FRai Default at right with dissolve
                FRai Serious "‘That was close..!’"

                show Felix Default at left with dissolve
                Felix Annoyed "Tch.."
                FRai "‘Oh no, I’m falling behind..’"
                FRai "‘But he won’t get too far with that injury!’"

                #[SFX running footsteps]
                play sound audio.footsteps

                Felix "‘Oh no you won't!’"
                "Felix turned to a building and disappears behind it."
                FRai "‘Where is he going..?’"

                jump scene1_4

            label scene1_3_1a2:
                scene Market
                show FRai Default
                FRai Surprised "Oh no-" with vpunch

                #[Screen fades to black]
                #[SFX wooden barrel falling harshly (tabrak tabrakan)]
                play sound audio.wooden_barrel_falling
                show black with dissolve
                "Rai may have some broken bones now."
                jump scene1_3_1

            label scene1_3_1a3:
                scene Market
                show FRai Surprised
                FRai "!?"
                FRai "Wait, where’s my gun!?" with vpunch
                #[Screen fades to black]
                #[SFX wooden barrel falling harshly (tabrak tabrakan)]
                play sound audio.wooden_barrel_falling
                show black with dissolve
                "Rai forgot he doesn’t have a weapon and his fists aren’t enough to destroy the wooden barrels."

                jump scene1_3_1

    label scene1_4:
        #[Screen fades to black]
        scene Market
        with fade
        #[SFX people chattering (rame)]
        play sound audio.people_chattering_loop

        show FRai Thinking at right with easeinright
        FRai Thinking "‘Where is he..’"
        FRai Annoyed "‘Ugh, I can’t find him in this crowd!’"
        FRai Thinking "‘But this crowd.. that means..’"
        "Hey, that’s the catboy that stole fishes!" #the sound of Cutlery Seller
        "Is that the thief the farmer boy was talking about?" #the sound of Woman
        "Someone catch him!" with vpunch #the sound of Girl
        
        #[SFX people chattering but louder(rame)]
        play sound audio.people_chattering_loop

        FRai Happy "There he is! Nice!"
        show Felix Default at left with dissolve
        Felix Annoyed "‘Ugh, that yellow head must’ve planned this..’"
        Felix "‘If there’s a building I could climb..’"
        Felix "‘There it is!’"
        hide Felix Default with dissolve

        #[SFX landing on roof]
        play sound audio.landing_roof

        FV_Seller "My shop roof!" #the sound of Vegetable and fruit seller
        show FRai Default at center with ease
        FRai Serious "‘Oh no, he’s gonna climb to a higher building..’"
        FRai "‘I have to climb too to catch him..!’"

        #[SFX climbing building]
        play sound audio.climbing

        FRai "‘I gotta at least get to the highest floor of this building for a good view.’"
        Seller "Uwaa?!" with vpunch #sound of Shop customer
        scene Rooftop with dissolve
        show FRai Default at left with easeinleft
        FRai Nervous "‘Oh man, everyone can see me from the window...’"

        #[SFX landing on floor]
        play sound audio.landing_floor
        
        FRai "‘Good thing this window is open. Now where is he.."
        show Felix Default at right with easeinright
        hide Felix Default with dissolve  
        FRai Surprised "There you are!"      
        #[CG 2 START]
        show CG2 with dissolve
        $ persistent.cg2_unlocked = True
        Felix Default "Oh, still not giving up?"
        FRai Annoyed "I’m the one who should’ve said that!"
        FRai "‘Tch! I can’t jump to that roof..!"
        FRai "I can throw something, but it’s useless from this distance.."
        Felix "Ha. Why are you so persistent?"
        Felix "The other people didn’t even want to go this far to catch me."
        Felix "Can’t you just go home and forget everything?"
        FRai "This is my job."
        Felix "Huh, are you paid to catch me?"
        FRai "...."
        Felix "You know you can’t match my speed, right? Yet you’re trying to chase me."
        FRai "..."
        #[CG 2 END]
        hide FRai Default
        hide Felix Default

        scene Market 
        show FRai Default at right
        show Felix Default at left
        with fade
        Felix Default "It’s useless. If i were you, I would give up."
        "Rai pulls out a handcuff."
        FRai Default "There’s now way I’m giving up after all I did to find you!"
        Felix "Ha, of course."
        Felix "IPD."
        #[Screen fades to black]

        scene Fish Shop
        show Felix Default at right
        with fade
        Felix Annoyed "I’m not going back there!"
        FRai Surprised "He’s going to jump down..!"
        Felix Smirk "Ha! Goodbye, slowpoke!"

        show Fisherman Default at left with dissolve
        show Felix Surprised at right with easeinright
        show Felix Default at center with ease
        Felix "Get outta my way-"
        show Fisherman Default at center with ease
        
        #[SFX punch]
        play sound audio.punch

        Felix Hurt "AAARGHH!!" with vpunch
        hide Felix Default with dissolve
        show FRai Default at left with easeinleft
        FRai Surprised "Whoa."
        FRai "You.. you punched him mid-air.."
        Fisherman "I-i did it!!!"
        Fisherman "I defeated him.. Did… did you see that, young man?  I defeated him!!"
        FRai Happy "You defeated him!!"

        play sound audio.crowd_cheering
        Crowd "YEAAAHH!!" #the sound of Crowd
        #[SFX crowd cheering]
    
        Fisherman "My deepest thanks, really…"
        Fisherman "You’ve chased this tiger everywhere, without rest and without complaint!"
        FRai "That's too much.. but thank you."

        show MeatButcher Default at left with dissolve
        show FRai Default at center 
        show Fisherman Default at right
        with ease

        Meat_Butcher "Nice job, kid."
        FRai Sad "I’m not a kid.."
        Crowd "Hahaha!" #the sound of Crowd
        FRai "'These people.. they're all kind.'"
        FRai "'I can't do much without all the people I've met. I can't succeed my mission without them.'"
        FRai Serious "Alright now, catboy.."
        FRai "Pay for the fish that you stole."
        Felix Annoyed "Ugh.."
        Felix "Here."
        FRai Annoyed "Whaat, so you have money all this time?"
        FRai "Should have paid for it instead of adding some list to your already existing crimes."
        Felix Hurt "..."
        FRai "Well, we’re gonna have lots to talk about when we get back to... Where you’re supposed to be."
        Felix Annoyed "Ugh…"
        FRai "Here’s your money, Mr. Fisherman. Here’s yours, and here’s yours, miss."
        FRai "And I’ll be taking this catboy with me."
        FRai Happy "Alright, everything’s done then."
        FRai "I shall pack my things up"
        Fisherman "Thank you, once again!"
        Meat_Butcher "Thanks."
        Felix  "...Hey officer."
        FRai Surprised "Eh? W-what do you have there?!"
        FRai Thinking "Where did you get this?"
        FRai "A..."
        FRai "Code?"

        stop music

        $ persistent.phase1 = False
        $ persistent.phase2 = True
        $ persistent.phase3 = False

    return
