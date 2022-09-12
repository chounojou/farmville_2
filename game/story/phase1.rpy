label phase1:

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

    #Galilean 1 appear
    # N : easeinright itu dateng ngeslide dari kanan
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
        "Attend Meeting":
            jump scene1_intro

        "Fix CCTV":
            jump scene2_intro

        "Tidy Files":
            jump scene3_intro

    label scene1_intro:
        scene MEETING_ROOM

        "Interdimensional Officers Discussion, an annual meeting with other branches to discuss progress between High-Ranking Officers in each branch."
        "Rai arrives with the file that his boss asked him to bring, he also made sure that he got a copy for everyone as well."
        "When Rai enters the meeting room he sees that no one is there except for his boss."

        show rai_confused
        Rai "What happened Boss? Am I late?"

        show Boss_default at right with easeinright
        Boss "No, the higher-ups suddenly rescheduled our meeting for next week due to the lack of some documents that we need."

        show rai_sad
        Rai "Too bad, I was hoping I could be useful today Boss."

        Boss "Don't worry, I already said that you eagerly wait for them."

        "Rai’s Boss reassures him with a shoulder pat."

        Boss "Is that the document that I asked you to fetch? It’s the notes for the meeting."

        show rai_default
        Rai "Yes it is Boss, here you go. Is there another task that you need me to do?"
        Boss "No, you may go."

        show rai_happy
        Rai "Affirmative Boss."

        hide rai_happy with dissolve
        hide Boss_default with dissolve

        "Rai walks back to his office remembering that he wanted to tidy up the files that were on his drawers a while ago."
        #SFX Footstep
        #BG : Blackscreen
        jump scene3_intro

    label scene2_intro:

        scene IPD_WORKPLACE
        "As Rai was about to go to the CCTV Room, he heard a knock"

        #SFX knock

        show galilean_default
        Galilean_2 "Uhh sir? Forgive me for the intrusion, but I’m here to give you this. It's from the CCTV Operator Guy. He says to give it to you."

        show rai_default
        Rai "Oh, okay. Just put it on the table, thank you."

        Galilean_2 "Then, I'll excuse myself."
        hide galilean_default with dissolve

        "After they left, Rai started reading the paper."

        "Need help in the CCTV Room -Artemisia"

        Rai "My god, I thought it’s a prank. Damn you Artemisia."

        "Rai laughs as he folds the paper neatly and walks towards the CCTV Room."

        #SFX Footstep
        #Blackscreen

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
        Artemisia "Right. As I said from the message, there seems to be a problem with some of the CCTVs in certain spots. Here are the camera locations."

        "Artemisia shows a monitor with IPD camera layout."

        show rai_thinking
        Rai "Hmm, the spot is kinda suspicious."
        Artemisia "What do you mean sir?"

        show rai_serious
        Rai "I saw it from my office. The CCTVs placements are too specific, as if it was purposely moved to create a blind spot. Maybe it’s just my imagination though. Forget it."
        Artemisia "I see. How observant of you sir."

        show rai_excited
        Rai "Aww hehe, I’ve been working here for so long that I feel like IPD is an extension of my body. So, where do I start?"
        Artemisia "Yes sir. Before that…"

        hide rai_excited
        hide artemisia_default
        #Blackscreen

    label scene2_2intro:
        scene IPD_WORKPLACE
        show rai_happy
        Rai "Ah yes. More Shigoto-san. More work. Shigoto-san daisuki~"
        "Rai walks happily to the first camera. The first place is near the IPD Entrance."

        show rai_concern
        Rai "Hmm, no wonder. The lenses are too dirty and the screws are also a bit loose. Luckily it’s a small maintenance."

        "Rai tinkers with the tools given by the Artemisia to repair the CCTV."
        "After he tightens back the screw and changes the lens, he reports back through the receiver to check if it’s working again or not."

        Artemisia "Looking good sir."

        show rai_happy
        Rai "Okay, thanks Artemisia."

        "He does the same to the CCTV near the IPD Hall, the Receptionist, the Pantry, and the one in the Conference Room."

        show rai_default
        Rai "Now, what should I do next?"

        "As Rai walks back, he sees a certain CCTV that’s badly damaged, it looks like it’s broken. As he approaches it a burnt smell emanates from it and he quickly reports it."

        show rai_nervous
        Rai "I found one CCTV that smells burnt.. Is this one of the CCTV spots that you mentioned?"
        Artemisia "I think so, can you try to fix it?"

        show rai_confused
        Rai "Uhh… I’ll try."

        "Rai picks up the tools and starts to tinker with the CCTV, unscrewing the cover then slowly removing the cover lid. And he’s met with a bunch of complicated components. Lots of wired cables, a chipset, and many other things."

        show rai_default
        Rai "I'm not sure what to do. Here is the photo of the inner CCTV that I mentioned."
        Artemisia "Wait, I think we have a manual for this in the drawers."
        Rai "A manual? I guess I can fetch it myself. Does this CCTV need to be immediately fixed?"
        Artemisia "You can take your time sir. This one is not that urgent. I will leave it to you, thank you for letting me know."
        Rai "Okay then. I'll pick up the manual later. Galilei out."
        hide rai_default
        Artemisia "Over and out."

        "After Rai re-screws the broken CCTV back. And walks back to his office to pick up the manual that’s on the drawers,"

        jump scene3_intro

    label scene3_intro:
        scene IPD_WORKPLACE
        show rai_surprised
        Rai "!!!"
        Rai "Oh god When was the last time I opened this drawer?!"
        Rai "There could be an explosion of papers anytime now!"
        Rai "I’ll have to move the old files to the archive room or it’s gonna be even messier!"

        show rai_sad
        Rai "Man, I did learn a few tips on how to tidy up files properly but then again this many is just ueee..."

        "After a while of ‘ueees’ Rai kinda successfully sorts out the files. There were a lot of bookbinders titled ‘ATHENEAN’ and some were marked as ‘GALILEAN’."
        "Both of them seem to be a big pile of paperworks, flash disks, SD Cards, and burnt clothes strapped in a plastic ziploc bag that looked like a confiscated item."
        "It was packed tightly in the corner of the drawer."

        show rai_happy
        Rai "Oh wow, I forgot I saved this piece of burnt cloth during my time as an Athenean. Ah… Good old times."

        show rai_serious
        Rai "It's been a long time ago since IPD accepted me. I remember when Boss gave me the codename RAI and placed me into the GALILEAN unit, Thus Rai Galilei was born! Hehe, what a time."

        "As Rai speaks to himself, he sips another cola while arranging the drawer."

        "He finds another peculiar book. It’s a dark-brown binder book, strapped with purple cloth, weaving an ‘ATHENEAN’ on its cover. The backside is a lot of hand-woven ribbon with colorful colors, mostly in red and blue."
        "When he flips it, one of the papers slips from the binder, Rai picks it up and reads the written text on it."

        show rai_excited
        Rai "What's this… hmm.  It reads… 'It feels like a fairytale - Maxwell’."

        show rai_happy
        Rai "Ah yeah, looking back, I do remember a bit when I was in the Athenean unit. Fine work, a good one. Yes yes, good memory indeed. Me likey."

        "Rai flips the binder book, reminiscing a lot about the job. After finishing with ‘ATHENEAN’, he picks up the ‘GALILEIAN’ one and starts to examine it."
        "The binder is in a hue color of black, brown and light yellow, kinda like a rusted steel. Complemented with a hand-woven gray ribbon as the strap circling around it, making it look like a chained book."

        show rai_happy
        Rai "Ah, this book. It’s my favorite one. It made me feel like I was writing a new spell in my grimoires. Fuhahahahaha!"

        "Rai laughs hysterically for a sec. His chuuni sense is back."

        show rai_default
        Rai "Ekhm. But really, looking at this, let’s see… Aha!"

        "As he slowly takes the polaroid photo of him and his coworker, celebrating his birthday in IPD."
        "It was completely dark that day because there was a jailbreak (which turned out to be a prank) and the inmates were creating a big mess by shutting down IPD’s electricity."

        show rai_excited
        Rai "Naughty Inmates. Made us IPD wear NV Google for three days straight because of the power outage."
        "Still it was so fun, I felt like an espionage agent when that day happened. Working on my laptop at the corner of the office, completely with a NV to maintain the surroundings, because they were playing hide and seek."
        "It ended up as a big surprise: ‘A Jailbreak Session’."

        "Rai laughs while remembering the photo."

        show rai_happy
        Rai "But that trick won't happen again, right?"

        #SFX SIREN
        "Suddenly IPD Siren rang loudly, notifying that there’s an inmate that successfully did a jailbreak."

        show rai_surprised
        Rai "OH MY GOD, REALLY? Did I just jinx myself? I spoke too soon. Damn that disturbed my flashback."

        "Rai’s receiver turns on."

        Artemisia "Artemisia to Galilei."

        show rai_serious
        Rai "Galilei Here."
        Artemisia "We need you to be in IPD Jail Hall ASAP"
        Rai "Northway or Southway, Artemisia?"
        Artemisia "Northway sir."
        Rai "I’m on my way."

        hide rai_serious
        "Rai quickened his pace to Northway IPD Jail Hall."

    label scene3_2intro:
        scene IPD_CELL
        #SFX RUNNING
        "As Rai arrives, there were three Galileian and an Artemisia in there examining the recent jailbreak room."

        show rai_serious
        Rai "Data report. What’s the identity of the inmate? Did you see their number? Or anything?!"

        show felix_default
        show galilean_default
        Galilean_3 "Yes sir. His name is Felix Linx. According to his files he’s a half human, half cat hybrid with pink hair and three orange stripes on both of his cheeks"

        hide felix_default
        show rai_serious
        Rai "His codename?"
        Galilean_3 "Based on the mugshot and the data that we’ve got, we dubbed this Inmate as ‘Catboy Paradise’. Lately because he has spoken about ‘True Paradise’."

        show rai_confused
        Rai "Uhh, why does that codename sound so familiar?"

        show artemisia_default
        Artemisia "Pardon sir?"
        Rai "Nothing. Moving on, so that’s the suspect. Where’s his location? We can track him using his collar, right?"

        Galilean_3 "That was the plan, on the CCTV footage his collar is still on him but he somehow managed to deactivate it."

        hide galilean_default

        Rai "Leave him to me, I’ll catch him."
        Artemisia "What do you mean sir?"

        "As Artemisia is still questioning what Rai’s words mean, Rai starts to contact the main branch via his receiver. Inputting the combination that only a few officers know about."

        Rai "Rai Galilei to Center. Permission to perform IPD Protocol Code 008-Romeo Alpha India-777, for codename ‘Catboy Paradise’. Over and out."

        "As Rai finished his report, his partners were left speechless, still amazed with what he just spoke."

        Artemisia "Wait, that code. Does that mean…?"
        Rai "Yes. It is like what you thought, Artemisia. I will go after him myself."
        Artemisia "Very well sir. We’ll provide you with the latest escape route of the inmate. It seems he ran away to code 611-813 Dimension aka the Farmland Dimension. We’ll leave him to you."

        hide rai_serious
        hide artemisia_default
        #Blackscreen
        #GO TO INMATES#1 ROUTE
        # This ends of intro/prolog
        jump scene1_1

    #Mulainya pengejaran sus pertama yaitu Felix
    label scene1_1:
        scene FARM
        "It is a peaceful morning in Farmland. The sun had just climbed out of its hiding. Its warm light dyed the sky a yellowish orange."
        "It seemed like a normal morning, but an interdimensional portal near a barn, which isn’t normal."
        "A young man walked out of it and looked around."

        show rai_default
        Rai "The air is kinda cold..."
        Rai "Hm, is that a barn?"

        show rai_excited
        Rai "I don’t see any houses, so maybe it’s only the farmer here… which makes my job easier."

        show rai_happy
        Rai "Less possible suspicion. Good, good."
        Rai "Even if the inmate’s not here, maybe I can dig some information about this dimension from the farmer."

        show rai rai_excited
        Rai "Alright, I should change my clothes"
        Rai "Undercover field mission starts!"

        #From here use farmer  rai sprite
        #screen fade to black

        scene FARM
        #SFX FOOTSTEPS
        Rai "There’s really no one else outside.."

        show rai_nervous
        Rai "It’s kinda creepy… at least there’s animals. I can see them."

        ##[SFX chicken noises, duck quacking, horse neighing, sheep baa-ing, cow moo-ing (all noises at once, chaotic)]

        show rai_surprised
        Rai "Whoa, wha-"

        #SFX #[SFX barn door opening]
        show farmer_default
        show rai_nervous
        Rai "H-hello, sir. Good morning."
        Farmer "What are you doing here? Who are you?"
        Rai "My name is Rai. I.. would like to take a look around this farm, sir."
        Farmer "A visitor, this early?"
        Rai "Well..I am actually new here"
        Rai "I’m interested in being a farmer, sir. So i kinda want to know what a farmer’s work is like"
        Rai "If you allow me, I would like to see everything in this farm up close!"
        Farmer "Hmm…"
        Rai "I just want to study. If you don’t mind, sir, could you let me stay here for a while to train myself? I’d sleep in the shed!"

        Rai "Please be convinced." #ngomong dalam hati?

        Farmer "Hmm, well.. if you say so"
        Farmer "Having an assistant for some time would be nice.."
        Farmer "Wait here."

        hide farmer_default
        ##[SFX footstep, followed by SFX barn door opening]

        show rai_thinking
        Rai "?"

        #SFX FOOTSTEPS
        show farmer_default
        Farmer "Here you go!"
        Rai "Seeds?"
        Farmer "For your first lesson, go feed the animals. And make sure they don't jump out of their fence."
        Farmer "Oh, and, the hay for horses is right next to their field fence."
        Farmer "The sheeps are eating every time with grass in their fence, so don't worry about them."
        Rai "What about the cow over there?"

        "Moooo" #Cow (Wyen’s cow form)
        Farmer "I’ll take care of the cow."
        Rai "Okay then!"

        show rai_nervous
        Rai "Wait, are you not gonna teach me?"
        Farmer "It’s your first task, and an easy one. What could go wrong with it anyway?"
        Farmer "Also, I got work to do. Just make sure you don’t give the chickens too much food. Good luck!"
        Farmer "I’ll be right back."

        show rai_surprised
        Rai "Ah, wait!"
        Farmer "Hmm? Is there anything you need?"

        show rai_nervous
        Rai "Uh, um, Like i said, I just came here not a long time ago, so I’m not really familiar with all the places here."
        Farmer "Sorry i can’t show you around for now, i need to grab some water from the well."
        Farmer "Though, I have a map if you need it! Here."

        show rai_happy
        Rai "Ah! Thank you very much!"
        Farmer "You’re welcome."
        Farmer "Alright, I have to go now. Good luck on your task!" #Farmer gone?

        ##[SFX running away footsteps]

        Rai "Got it"
        show rai_surprised
        Rai "..wait, I’m supposed to search for clues and find the runaway inmate!"
        Rai "I should search the whole farm.. guess I have to do it and feed all the animals at the same time."
        menu:
            "Feed ducks" if bebek == False:
                $bebek = True
                jump scene1_1_1

            "Feed horses" if kuda == False:
                $kuda = True
                jump scene1_1_2

        #Blackscreen
        label scene1_1_1:
            scene FARM
            show rai_default
            Rai "Here you go duck."
            #[SFX ducks quacking]

            show rai_excited
            Rai "Alright, while they’re busy eating.. I’ll search this field!" #ngomong didalam hati?
            Rai "Hm.. it's just grass here."
            Duck "Quack!"
            Rai "I don't speak duck language."
            Ducks "Quack quack!"

            show rai_sad
            Rai "I don't understand.."
            Farmer "The ducks like you, lad." #Farmer back?

            show rai_surprised
            Rai  "Whoa! Since when are you here?"
            Farmer "Just now, haha."
            Rai "You can understand these ducks?"

            Farmer "Hm, you could say so."
            Farmer "I don't understand their language of course, but I've been living with animals for a long time already."
            Farmer "I know what they're trying to say from how they act."
            Farmer "These ducks don't usually quack at strangers. But they don't seem to have a problem with you being here."
            Farmer "Them quacking at you means they like you."

            show rai_happy
            Rai "The ducks like me..!"
            Ducks "Quack quack!"
            Rai "By the way, sir. Why aren't these ducks in water?"
            Farmer "Ducks can swim, yes, but they mainly live on land."
            Rai "Ooh, I see."
            Farmer "How's your first job going?"
            Rai "So far so good."
            Rai "These ducks are friendly."
            Farmer "That's good to hear."
            Rai "I'll go feed the other animals now!"
            Farmer "Alright! I'm always around the shed, so go there if you need my help."
            Rai "Okay!"

            if bebek == False:
                $bebek = True


            if bebek == True and kuda == True:
                jump scene1_2
            else:
                jump scene1_1_2

        label scene1_1_2:
            scene FARM
            show rai_default
            Rai "Hello, horses. How’s your day?"

            #[SFX horse noises]
            "Hrrreeuuhh"

            Rai "Wow, you don't sound okay. You must be hungry."

            #[SFX horse noises]
            "Hrghheeuuh"
            Rai "Here's your breakfast!"

            #[SFX horse noises]
            show rai_excited
            Rai "'Okay, time to search!'"
            Rai "'Maybe there's something in the grass.'"

            #[SFX horse noises]
            Rai "Hmm? Is there something?"

            #[SFX footstep on grass]
            show rai_surprised
            Rai "Who's there?!"

            show rai_serious
            Rai "...."

            show rai_thinking
            Rai "'Maybe it's just my imagination.'"
            Rai "'This is an open field, there's nowhere to hide.'"
            Rai "'But if it is a person, then that person is very fast.'"
            Rai "'Whatever. I have to go feed the other animals.'"

            if kuda == False:
                $kuda = True


            if bebek == True and kuda == True:
                jump scene1_2
            else:
                jump scene1_1_1

    label scene1_2:
        scene FARM
        #[SFX chicken noises]
        show rai_default
        Rai "Alright, chickens. Breakfast time!"

        #[SFX chicken noises but louder]
        Rai "Whew, there’s more chickens than I thought."

        #[SFX chicken noises but even louder]
        show rai_annoyed
        Rai "You’re all so noisy.. Is the food not enough?"
        Rai "Alright, I’ll give you a bit more, so calm down."
        Rai "Hey, no need to fly- wait what-"

        #[SFX chicken noises but EVEN louder and chaotic]
        show rai_surprised
        Rai "Wait.. stop.. there’s enough for everyone-"
        Rai "OW- AAAAARRRGGHH"

        show farmer_default
        Farmer "What happened?!"
        Rai "Mr farmer! Help me!!"

        #[SFX chicken noises]
        Farmer "Shoo, shoo!"

        #[SFX chicken noises]

        Farmer "Calm down! I’m here, okay?"

        #[SFX chicken noises but less loud]
        Rai "Phew.."
        Rai "Are the chickens always like this?"
        Farmer "No.. they're usually not like this."
        Farmer "They are noisy when there’s a stranger, but If I’m here, they always calm down right away."

        show rai_nervous
        Rai "That’s weird.."
        Farmer "They might be warning me about something."

        show rai_nervous
        Rai "Something? Or.. Someone?"
        Rai "But I didn't see anyone!"

        show rai_thinking
        Rai "'Could it be the inmate..?'"
        Rai "'Then, what I heard when I was feeding the horses.. aren’t my imagination?'"
        Rai "'Ill have to go search later.'"
        Farmer "What’s with that face?"

        show rai_surprised
        Rai "Huh?"
        Farmer "Ha.. Maybe the chickens were just left with no food for a bit too long"

        show rai_nervous
        Rai "Well.. It could be"

        Farmer "By the way!"
        Farmer "Is your job done?"
        Rai "Ah, yes! I’ve done it!"
        Farmer "Good, good."
        Farmer "Here's some money. Go buy breakfast at the market."

        show rai_happy
        Rai "...thank you!"

        Farmer "I gave you a map, right?"
        Farmer "Always carry it with you so you won’t be lost."
        Rai "Yes, I will."
        Rai "I'll go to the market later."
        Farmer "Why not now?"
        Farmer "It’s past the time for breakfast already. Or have you eaten breakfast?"

        show rai_nervous
        Rai "Well, I.. I think I’m gonna hang around in the farm for a while."
        Farmer "Adjusting yourself with the farm life, huh?"
        Rai "Kinda"
        Rai "'There’s no way I’m telling him I’m actually searching for a runaway inmate..'"
        Farmer "Take your time then."
        Farmer "If you want to go somewhere else too, then feel free to do so."
        Rai "Okay!"
        Farmer "I'll be going to feed the cow. Good luck on your search!"

        Rai "Thank you!"

        #[Screen fades to black]
        scene FARM
        show rai_thinking
        Rai "'Hmm..'"
        Rai "'The sound i heard while feeding the horse ealier..'"
        Rai "It could actually be the inmate, cats are fast to move from one place to another places. Cat-people must be fast too.'"
        Rai "'I’ve been searching around this farm, but seems that there really is no one else here.'"
        Rai "'Oh right, the map.'"

        Rai "'Let’s see..'"

        #[SFX paper unroll (srek)]
        #[Asset: Farmland map start]
        Rai "'Hmm, there's a river near the forest.'"
        Rai "'Knowing his past crime, maybe he’s searching for fish?'"
        Rai "'Then, he might be there.'"
        Rai "'Or at the market, at a fish shop.'"
        Rai "'The forest could be a nice hiding place too, I should go and search it.'"

        #[Asset: Farmland map end]
        #[Screen fades to black]

        scene FARM
        show rai_serious
        Rai "'I’ll go to the market first.'"

        show rai_thinking
        Rai "'Oh wait. What about the farmer?'"
        Rai "'I have to tell him I'm going out, or he might be suspicious of me.'"

        #[Screen fades to black]
        scene FARM
        show farmer_default
        Farmer "Oh, you're back! How’s your search?"

        show rai_sad
        Rai "No result.."
        Farmer "See, it’s probably just random people."
        show rai_nervous
        Rai "Yeah.."
        Rai "Um, sir-"
        Farmer "It’s way past breakfast time already. You should go to the market now!"
        Rai "Oh, right! I’m going. Bye-bye!"
        Farmer "Come back in time for lunch! Byee!"

        #[Screen fades to black]

        scene Market
        show rai_happy
        Rai "'He told me to go to the market when I was about to say so. What a coincidence!'"

        #[SFX people chattering]
        Rai "'Wow, it sure is crowded here.'"

        #[SFX tummy growl]
        show rai_sad
        Rai "'I’m hungry.. I wanna buy some food.'"
        Rai "'Good thing I have money.'"

        show rai_happy
        Rai "'Oh hey, a bread seller!'"
        Rai "Hello there, little miss! Can I get some bread?"
        Bread_Seller "Here you go! It'll be 3 coins."
        Rai "3 coins.. here!"
        Rai "Mm, these breads smell good!"
        Bread_Seller "Hehe, I made these myself."
        Rai "Whoa.. amazing!"
        Bread_Seller "Thank you!"
        Rai "Ah, um, by the way, is there a fish shop or someone who sells fish around here?"

        "The girl points at a two floored shop."

        Bread_Seller "That building over there."

        Rai "Thank you!"

        #[Screen fades to black]
        scene Fish_shop_first_floor
        #[SFX footstep]

        show fisherman_default
        Fisherman "AAAAAAAAAAAHHH!!! MY FISHH!!!"

        show rai_surprised
        Rai "?!"
        Fisherman "MY FISH WERE STOLEN! MY FISH!!"

        show meat_butcher_default
        Meat_Butcher "Ugh, just shut up already! It was like fifteen minutes ago and you’re still bringing that up?"
        Fisherman "A HUGE TIGER STOLE MY FISH!! He should pay.. he should pay!"
        Meat_Butcher "If you want to make him pay, then get moving! You’re not doing anything at all!"
        Fisherman "Ouch, how mean…"
        Rai "Um, excuse me!"
        Rai "Sorry for interrupting, but can you tell me more about the stolen fishes?"
        Meat_Butcher "And who are you?"

        show rai_excited
        Rai "Ah, I’m just someone curious. And maybe I could help!"
        Meat_Butcher "This is none of your business."
        Fisherman "Oh, finally a good and kindhearted person!"
        Meat_Butcher "Haaaa?!"
        Fisherman "*gulp*"

        show rai_nervous
        Rai "Uh.."
        Rai "Um, could you tell me more about the stolen fishes, sir?"
        Fisherman "My fish, my precious fish were stolen!"
        Rai "Please explain it in detail, sir."
        Fisherman "Not so long ago, a biiig scary tiger entered my shop, and snatched some of my fish away!"

        show rai_annoyed
        Rai "In even more detail, sir."
        Meat_Butcher "It’s useless."
        Rai "Oh?"
        Meat_Butcher "So, around fifteen minutes ago, a catboy came to this shop."
        Meat_Butcher "He has messy pink hair. "

        show rai_serious
        Rai "‘The inmate..!’"
        Meat_Butcher "At first he seemed like a normal customer, but then he grabbed some fish and ran out immediately."
        Rai "So you were here when it happened?"
        Meat_Butcher "Yep."
        Meat_Butcher "And he’s fast. There were some people in and outside this shop, but nobody could catch him."

        show rai_thinking
        Rai "I see.."
        Meat_Butcher "So? You’re gonna find him?"
        Rai "Yes. I said I would help."
        Fisherman "You really will help me?!"
        Fisherman "Such a good person! What can I do without your help..! Thank you, thank you!"

        show rai_nervous
        Rai "Ahaha, you’re welcome."
        Rai "I’ll go search for the thief now. I’ll be back soon."
        Fisherman "Safe travels!"
        Meat_Butcher "It’s not like he’s gonna come back next week…"

        #[Screen fades to black]
        scene Market
        Rai "Have you seen a cat boy around here, sir? He has pink and bushy hair."
        Merchant "Catboy..? Nope."

        show rai_sad
        Rai "Alright…"
        Rai "Please tell the Fisherman at the fish shop if you spot him!"
        Merchant "...hm."

        show felix_smug
        Felix "Heh, you’re too slow..." #he just gone or what?

        #[SFX footstep]

        Rai "Ah, hello, miss! Have you seen a cat boy around here? He’s pink and bushy haired."
        #Man "No, sorry." #?????

        show rai_sad
        Rai "I see, alright.."
        Rai "Please tell the Fisherman at the fish shop if you see him!"

        show rai_annoyed
        Rai "'Aaagh, I’ve been searching everywhere and asked everyone I see, but he’s nowhere!"

        show rai_serious
        Rai "'But I can’t give up!'"
        Rai "'I have to ask more people.'"
        Rai "Hello, miss! Have you seen a catboy around here? He has pink and bushy hair."

        show villager_default
        Villager "Umm, yes?"

        Rai "Where?!"
        Villager "Uh, there…"
        "AAAAAHH! THIEF!!" #Sound only? also this is soud of Old lady

        show rai_surprised
        Rai "Wha-"

        show felix_default
        show rai_serious
        Rai "You..!"

        show felix_suprised
        Felix "Hmm?"
        Rai "Don't move!"
        Felix "What do you mean don’t move? You’re threatening me?"
        Felix "You don’t even have a weapon."
        Rai "Ugh.."

        show felix_smug
        Felix "Aha. Are you gonna catch me?"
        Felix "Catch me if you caaan!"

        #[SFX running footsteps]
        Rai "You’re not going away!"

        #[SFX running footsteps]
        #[Screen fades to black]

        scene Market
        #[SFX running footsteps]
        show rai_annoyed
        Rai "Huff... huff…"
        Rai "So.. tired…"
        Rai "‘Where is he going..?’"

        show rai_surprised
        Rai "!!!"
        Felix "Heh. You were so focused on chasing me, you don’t realize I’m leading you to a corner."
        Felix "Well, good luck chasing me, if you can. Byeee!"

        "The inmate climbed up the walls and left."

        show rai_annoyed
        Rai "'Aaargh, how didn’t I realize?!"
        Rai "‘There’s no way I can chase him now.. I’m too tired to keep on running.’"

        show rai_thinking
        Rai "Now what do I do?"
        Rai "‘He can be hiding anywhere right now. It’s been a while since he left. With that speed, he must’ve gone far away.’"
        Rai "‘This is very close to the village.. he could be there.’"
        Rai "‘But what if he went the opposite way instead? He might even be hiding in the forest.’"
        menu:
            "Reminicence":
                jump scene1_2_1
            "What if he isn't in the village?":
                jump scene1_3

        label scene1_2_1:
            #Fadeout Blackscreen
            #Flashback Filter?
            scene Market
            show rai_default
            Rai "Please tell the Fisherman at the fish shop if you spot him!"

            jump scene1_3

    label scene1_3:
        scene Market
        show rai_thinking
        Rai "‘If the inmate is back to the market.. I’ve told everyone to go to the fish shop if they see the inmate, so I’ve got more eyes to help me.’"
        Rai "‘And maybe the people at the market can catch him..’"

        #[Flashback filter]
        scene Fish_shop_first_floor
        show meat_butcher_default
        Meat_Butcher "And he’s fast. There were some people in and outside this shop, but nobody could catch him."

        #[Screen fades to black]
        scene Market
        show rai_nervous
        Rai "‘Hopefully.’"
        Rai "‘But I think it’s safe to go to the village and search.’"

        #[Screen fades to black]
        scene Village
        #[SFX people chattering]
        Rai "‘Wow, it’s crowded in the morning.’"

        #[SFX 2 people bumping into each other]
        show rai_surprised
        Rai "Uwah-"

        show villager_default
        Villager "Aaaah! I’m so sorry!"

        show rai_nervous
        Rai "Ah, no, it’s my fault. I was spacing out and didn’t notice you."

        show rai_surprised
        Rai "Wait, you’re the one at the market!"
        Villager "Oh! I remember you!"
        Villager "You asked me something about a catboy."
        Rai "Right, the catboy-"
        Villager "Ah, um, as an apology for bumping into you, I’ll give you a potato!"

        show rai_nervous
        Rai "No need to-"
        Villager "Here you go! Fresh potato!"
        Rai "Um, you don’t need to…"
        Villager "No, no, please take it!"

        show rai_happy
        Rai "...Thank you!"

        #[SFX tummy growl]
        Villager "So you’re hungry! Good thing I gave you the potato. Eat up!"

        show rai_nervous
        Rai "..."
        Rai "It’s raw..."
        Rai "I can’t eat it.."
        Villager "..."
        Rai "..."
        Villager "Want me.. to cook it for you?"
        Rai "‘I need to hurry, but I’m really hungry.. It’s time for lunch already.’"

        show rai_happy
        Rai "..If you don’t mind!"
        Villager "It’s ok! My house is right there. Follow me!"

        #[SFX footsteps]
        #[Screen fades to black]
        show Village
        #[SFX footsteps]
        Villager "I’ll boil the potato. Wait here, it won’t take long!"
        Rai "Okay."

        show rai_sad
        Rai "‘Too bad I can’t taste the farmer’s cooking…’"
        Rai "But at least I can still have lunch."

        #[SFX water blub blub]
        "Rai sat on a bench, right below the kitchen window. The window is wide open. The sound of boiling water can be heard from inside the kitchen."

        #[SFX footsteps]
        Villager "Here’s the potato!"

        show rai_happy
        Rai "Thank you!"

        #[SFX munching potat]
        show rai_serious
        Rai "By the way.. have you seen the catboy in this village? The one at the market."
        Villager "Hmmm..."
        Villager "I don’t."

        show rai_sad
        Rai "Oh."
        Villager "Ah,um, don’t be sad!"
        Villager "Here’s the thing, there’s people guarding the village entrance."
        Villager "They tell nearby villagers whenever there’s a visitor, a.k.a people who don’t live in this village, then that will be relayed to the whole village."
        Villager "So the whole village would’ve known if the catboy was here."
        Rai "Huh? I didn’t see any guards when I came here."
        Villager "Because the guards look like any other villagers."
        Villager "They don’t stop and interrogate every single person who comes, but they always watch over the entrance."
        Villager "Like I said, they tell nearby villagers whenever there’s a visitor, then those villagers tell the other villagers about the visitor."
        Villager "So the whole village would’ve known if there’s someone visiting, like you."

        show rai_surprised
        Rai "Are you saying the whole village knows I’m here now?"
        Villager "Yep!"
        Rai "I see.."
        Rai "By the way, I have something to ask." #rai default?
        Villager "Yes?"
        Rai "Is it hard to find a way in the forest?"
        Villager "Oh, you wanna go to the forest?"
        Rai "Yeah."
        Rai "‘Since the inmate isn’t here, I have to get moving.’"
        Villager "I’ve never wandered around the whole forest, but I heard there’s a path you can follow. And there’s a talking tree that can help you if you’re lost!"

        show rai_surprised
        Rai "Talking tree?"
        Villager "Yep! It’s a myth, but it may be true, who knows!"

        show rai_nervous
        Rai "Ahaha.."
        Villager "Sorry I can't help you much."
        Rai "It’s alright! You helped me a lot already! You gave me food and told me what I need."
        Villager "Mhm!"
        Rai "I gotta go now. Thank you for the potato and everything! Bye-bye!"
        Villager "Oh, bye-bye!"

        #[Screen fades to black]
        scene Forest
        Rai "Hmm, it’s pretty hard searching with all these trees everywhere.."
        Rai "And I can’t see the path."

        show talking_tree_default
        Talking_Tree "Goood daaaayy, my child… Yoooourr faaacee loookss liiikeeee youuu cooulddd useee soomeee heeeelp..!"

        show rai_surprised
        Rai "EEEEE?!"
        Rai "‘The talking tree.. you’re real!"

        #[CG 1 START]
        Talking_Tree "Ha-ha-ha. Iiii ammm, myy chiiild.."

        #show rai_surprised
        Rai "Wow.. you’re huge.."
        Rai "Someone told me you help people that get lost in this forest."
        Talking_Tree "Whyyy, haaavee youuuu looost yooouur waaay, myy chiiild…?"
        Rai "I think so."
        Talking_Tree "Waaallkk toooo yooouurr leeeftt..!"
        Talking_Tree "Thaaaat waaayy yooouuu wiiiill approooaaachh theee paaathh oooof thiiiss fooooreesst.."
        #show rai_excited
        Rai "Okay!"

        #[CG 1 END]
        #[SFX footsteps]

        show rai_happy
        Rai "Oh, there it is!"
        Talking_Tree "Oooohh, yooouu haaaveee diiiscoooveered theee paaathh…"

        show rai_surprised
        Rai "Whoa, you can see me?"
        Talking_Tree "Iiiii aaamm veeerryy taaallll, myyy chiiildd, Iiii caaan seee yoouuu frooom heeeree… Iiii caaann viiieeeww eeeverythiiing iiinn thiiiss foreeesst..."

        show rai_excited
        Rai "So cool..!"
        Talking_Tree "Ha-ha-ha…!"
        Rai "Hmm?"
        Talking_Tree "Whaaatt isss iiiitt, myyy chiiildd…?"
        Rai "There’s something on this tree.."

        #[Asset Scratches on tree]
        show rai_thinking
        Rai "Scratches.. it could be caused by the inmate, or a wild animal."
        #[Asset Scratches on tree]

        #[Screen fades to black]
        scene Forest
        Rai "Mr Talking Tree, do you know who did this?"
        Talking_Tree "Oooohh yeeess Iiiii doooo, myyy chiiiildd.."
        Talking_Tree "Aaaaatt daaawwnn, theeereee waasss aaaa feeeliiinee laaaadd waaandeeeeriingg iiinn thiiiss fooorreeesst…"

        show rai_surprised
        Rai "Feline lad? The catboy?!"
        Rai "Does he have pinkish bushy hair?"
        Talking_Tree "Heeee dooeeess...!"
        Rai "So he was here!"

        show rai_thinking

        Rai "What’s with the scratch though?"
        Talking_Tree "Iiii scaaareeedd hiiimm oofff! Heeee weeentt awaaayy iiinn hoorrooor..! Ha-ha-ha…!"

        show rai_happy
        Rai "You like to play tricks, huh?"
        Talking_Tree "Iiii maaayy beee aaancieeent, buuut thaaaat wiiill neeeveerr hiiindeer myy frooliic…! Ha-ha-ha…!"
        Rai "Oh? How old are you, if.. you don't mind telling?"
        Talking_Tree "Hmmmmmmmmmmm…"
        Talking_Tree "Iiii dooo nooott knoooww.. Iiii haaavee beeenn heereee siinceee theeee aaancieeennt tiiimeeess..!"
        Talking_Tree "Iii doooo noooot reemembeer.. hooowww looongg Iiii haaaveee stoood…"

        show rai_surprised
        Rai "Ooh.."

        show rai_thinking
        Rai "Hmm, do you know what is the catboy here for, sir?"
        Talking_Tree "Theee feeliineee seeemed tooo beee seeeaarchiing fooor sooomeethiing..! Iiiii dooo nooot knoooww whaaatt iitt iiiiss…"
        Rai "I see…"
        Rai "Mr talking tree, you can see this whole forest, right? Is the catboy here?"
        Talking_Tree "Iiiii doooo nooott seee aaaa caaatbooy, myyy chiiildd…!"
        Rai "What about the river? Can you see anyone from here?"
        Talking_Tree "No ooonee iisss theeeree..! Eemptyyy…!"
        Rai "Alright. Thank you, Mr. Talking tree."
        Talking_Tree "Areee youuu gooiiing tooo deeepaaarrt noooww, myy chiiildd..?"
        Rai "Yeah. I have to meet someone."
        Talking_Tree "Iiitt haaass beeen aaa greeaat deeliightt taaalkiiingg tooo yooouu, myyy chiiildd.. Iiitt haaass beeen aaaa looongg tiimeee siincee Iii laasstt haaadd aaa taalkk wiithh aanyoonee.."

        show rai_happy
        Rai "Thank you for helping me too."
        Rai "Bye-bye, Mr talking tree!"
        Talking_Tree "Faaareeweell, myy chiildd…"

        #[SFX running footsteps]
        show rai_serious
        Rai "‘I left the market for hours already. I have to go back!"

        #[Screen fades to black]
        scene Fish_shop_first_floor
        show fisherman_default
        show rai_serious
        Rai "I’m back! Any news?"
        Fisherman "This is terribly painful, but I have to say, there is no news."
        Rai "I see.."
        Rai "I’ll go search again."
        Fisherman "..."

        #[SFX footsteps]
        show meat_butcher_default
        Meat_Butcher "Hey."
        Meat_Butcher "You.. Why do you actually want to help? You got too much freetime?"
        Rai "Maybe."
        Meat_Butcher "...."
        Rai "..Miss. Do you not trust me?"
        Meat_Butcher "Yeah, well.. you're pretty suspicious."
        Meat_Butcher "You came outta nowhere and just said you want to help."

        show rai_nervous
        Rai "Ahaha.."
        Rai "'I hope she doesn't find out about my mission..'"
        Meat_Butcher "But, if you really want to help.."
        Meat_Butcher "That's very.. kind."

        show rai_surprised
        Rai "..."
        show rai_happy
        Rai "Thank you."
        Rai "I’m going to search more."

        #[SFX footsteps]
        hide rai_surprised

        Fisherman "I’m going. I must help him."
        Meat_Butcher "Huh? Hey, wait!"
        Meat_Butcher "..."
        Meat_Butcher "I'm going too!"

        #[Screen fades to black]
        scene Market
        #[SFX running footsteps]

        show rai_serious
        Rai "‘Where.. where is he..’"
        "AAAAAAAHH!! THIEF!! HELP!" #the sound of Lady

        show rai_surprised
        Rai "‘What, again?’"

        show felix_default
        Felix "It’s you again..."

        show felix_smug
        Felix "You’re never gonna catch me!"

        #[SFX running footsteps]
        show rai_serious
        Rai "I will this time!!"

        #[SFX running footsteps]
        "Chase scene ensues. The police officer and the inmate are running, jumping, and parkouring through the crowded market."

        show rai_serious
        Rai "Excuse me!"
        "Whoa!!" #the soud of Lady
        Rai "I’m sorry- whoa!"
        "Whoaah!" #the sound of Children

        show rai_nervous
        Rai "‘Oh my God, I almost hit those children!"
        Felix "Ahaha! You can’t catch up to me, don’t you?" #show felix_smug?
        Rai "He’s too fast..! I have to do something to slow him down!"

        label scene1_3_1:
            scene Market
            show rai_default
            Rai "‘Wood plank..!’"
            #[SFX wood planks falling]
            show rai_serious
            Rai "This is gonna hurt!"

            #[SFX wood plank go whoosh]
            show felix_annoyed
            Felix "Ugh-!"
            Felix "‘My back..!’"

            show rai_excited
            Rai "‘Now’s my chance!’"

            #[SFX running footsteps]
            Felix "‘Crap, he’s catching up!’ • ‘I can’t let it happen!’"
            #[SFX wooden barrel falling harshly (tabrak tabrakan)]

            show felix_smug
            Felix "My turn!"

            show rai_surprised
            Rai "Whop-"

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
                show rai_serious
                Rai "‘That was close..!’"

                show felix_annoyed
                Felix "Tch.."

                show felix_thingking
                Rai "‘Oh no, I’m falling behind..’ • ‘But he won’t get too far with that injury!’"

                #[SFX running footsteps]
                show felix_annoyed
                Felix "‘Oh no you won't!’"
                "Felix turned to a building and disappears behind it."
                Rai "‘Where is he going..?’"

                jump scene1_4

            label scene1_3_1a2:
                scene Market
                show rai_surprised
                Rai "Oh no-"

                #[Screen fades to black]
                #[SFX wooden barrel falling harshly (tabrak tabrakan)]

                "Rai may have some broken bones now."

                jump scene1_3_1

            label scene1_3_1a3:
                scene Market
                show rai_surprised
                Rai "!?"
                Rai "Wait, where’s my gun!?"
                #[Screen fades to black]
                #[SFX wooden barrel falling harshly (tabrak tabrakan)]
                "Rai forgot he doesn’t have a weapon and his fists aren’t enough to destroy the wooden barrels."

                jump scene1_3_1

    label scene1_4:
        #[Screen fades to black]
        scene Market
        #[SFX people chattering (rame)]
        show rai_thinking
        Rai "‘Where is he..’"

        show rai_annoyed
        Rai "‘Ugh, I can’t find him in this crowd!’"

        show rai_thinking
        Rai "‘But this crowd.. that means..’"
        "Hey, that’s the catboy that stole fishes!" #the sound of Cutlery Seller
        "Is that the thief the farmer boy was talking about?" #the sound of Woman
        "Someone catch him!" #the sound of Girl
        #[SFX people chattering but louder(rame)]

        show rai_happy
        Rai "There he is! Nice!"

        show felix_annoyed
        Felix "‘Ugh, that yellow head must’ve planned this..’"
        Felix "‘If there’s a building I could climb..’"
        Felix "‘There it is!’"
        #[SFX landing on roof]
        "My shop roof!" #the sound of Vegetable and fruit seller

        show rai_serious
        Rai "‘Oh no, he’s gonna climb to a higher building..’"
        Rai "‘I have to climb too to catch him..!’"
        #[SFX climbing building]
        Rai "‘I gotta at least get to the highest floor of this building for a good view.’"
        "Uwaa?!" #sound of Shop customer

        show rai_nervous
        Rai "‘Oh man, everyone from the window can see me..’"
        #[SFX landing on floor]
        Rai "‘Good thing this window is open. Now where is he.."

        show rai_surprised
        Rai "There you are!"

        #[CG 2 START]
        Felix "Oh, still not giving up?"
        Rai "I’m the one who should’ve said that!"
        #show rai_annoyed
        Rai "‘Tch! I can’t jump to that roof..!"
        Rai "I can throw something, but it’s useless from this distance.."
        Felix "Ha. Why are you so persistent?"
        Felix "The other people didn’t even want to go this far to catch me."
        Felix "Can’t you just go home and forget everything?"
        Rai "This is my job."
        Felix "Huh, are you paid to catch me?"
        Rai "...."
        Felix "You know you can’t match my speed, right? Yet you’re trying to chase me."
        Rai "..."
        #[CG 2 END]

        scene Market
        Felix "It’s useless. If i were you, I would give up."
        "Rai pulls out a handcuff."
        Rai "There’s now way I’m giving up after all I did to find you!"

        show rai_annoyed
        Felix "Ha,of course."
        Felix "IPD."
        #[Screen fades to black]

        scene Fish_shop_first_floor
        show felix_annoyed
        Felix "I’m not going back there!"

        show rai_surprised
        Rai "He’s going to jump down..!"

        show felix_smug
        Felix "Ha! Goodbye, slowpoke!"

        show fisherman_default
        show felix_suprised
        Felix "Get outta my way-"
        #[SFX punch]

        show felix_hurt
        Felix "AAARGHH!!"

        show rai_surprised
        Rai "Whoa."
        Rai "You.. you punched him mid-air.."
        Fisherman "I-i did it!!!"
        Fisherman "I defeated him.. Did… did you see that, young man?  I defeated him!!"

        show rai_happy
        Rai "You defeated him!!"
        "YEAAAHH!!" #the sound of Crowd
        #[SFX crowd cheering]
        Fisherman "My deepest thanks, really…"
        Fisherman "You’ve chased this tiger everywhere, without rest and without complaint!"

        show rai_happy
        Rai "That's too much.. but thank you."

        show meat_butcher_default
        Meat_Butcher "Nice job, kid."

        show rai_sad
        Rai "I’m not a kid.."
        "Hahaha!" #the sound of Crowd
        Rai "'These people.. they're all kind.'"
        Rai "'I can't do much without all the people I've met. I can't succeed my mission without them.'"

        show rai_serious
        Rai "Alright now, catboy.."
        Rai "Pay for the fish that you stole."

        show felix_annoyed
        Felix "Ugh.."
        Felix "Here."

        show rai_annoyed
        Rai "Whaat, so you have money all this time?"
        Rai "Should have paid for it instead of adding some list to your already existing crimes."

        show felix_hurt
        Felix "..."
        Rai "Well, we’re gonna have lots to talk about when we get back to... Where you’re supposed to be."

        show felix_annoyed
        Felix "Ugh…"
        Rai "Here’s your money, Mr. Fisherman. Here’s yours, and here’s yours, miss."
        Rai "And I’ll be taking this catboy with me."

        show rai_happy
        Rai "Alright, everything’s done then."
        Rai "I shall pack my things up"
        Fisherman "Thank you, once again!"
        Meat_Butcher "Thanks."
        Felix  "...Hey officer."

        show rai_surprised
        Rai "Eh? W-what do you have there?!"
        show rai_thinking
        Rai "Where did you get this?"
        Rai "A..."
        Rai "Code?"

        $ persistent.phase1 = False
        $ persistent.phase2 = True
        $ persistent.phase3 = False

    return
