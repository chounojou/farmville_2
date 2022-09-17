default skor_trial_cave = 0
default skor_trial_market = 0
default skor_trial_waterfall = 0

default current_trial = ""
default chosen_trial = ""

default trial_market = False
default trial_cave = False

label phase3:

    "It’s a bright and sunny day at the Interdimensional \nPolice Department or IPD for short."
    "The sunlight is shining through the windows today."
    "A perfect day to go outside and lay down on a sandy \nbeach with a friend or two but not for Rai Galilei."
    "He’s one of the busy officers from IPD."
    "Today is like any of his work days, a lot of new \npaperworks awaits Rai in his office, which he happily \naccepts as it is."
    "Waking up and walking to his office like normal. \nAccompanied by the usual chit-chatter with \ncolleagues."
    "Rai finally reached his office desk."
    "It doesn’t look like one at the moment as \nit is covered by mountains of paperwork."
    "He lets out a big stretch."
    "And it’s time for him to do his work."
    "Before sitting down on his desk, he grabs \na can of cola and cracks it open."
    "His number one favorite drink to accompany him \nthrough all the paperwork of the day. "
    "He takes a sip as he sits down on his chair."

    show rai_default
    Rai "Ah.. another day with my wife, Shigoto-san."
    Rai "Hmm, let's see what I have to do today."

    Rai "Man… It’s just the beginning of the day yet \nsomeone has already put this much paper here."
    Rai "I can’t work properly if my table is full of \npapers."
    Rai "I need to tidy it up a bit, I think I should \nput some of \nthe papers in the drawer for the meantime."

    "While Rai was tidying up the papers that were on \nhis desk, one of his Galilean coworkers came by his table."

    show rai_default at left with easeinleft
    show galilean_default at right with easeinright

    Galilean_1 "Good morning! Sorry to disturb you \nso early in the morning…"

    Rai "Oh! Good morning!"
    Rai "It’s okay. Is there something that I could \nhelp you with?"

    Galilean_1 "Ah yes, I’m just here to remind you about \nthe meeting that we will be holding in a bit."
    Galilean_1 "Please don’t forget to bring the necessary \nfiles for it!"

    Rai "Thank you for the reminder. I’ll get it ready."

    Galilean_1 "Okay then, I shall excuse myself now. \nHave a good day!"

    hide galilean_default with dissolve
    hide rai_default with dissolve

    "As Rai gets back on his chair, he sees a post-it-note \nreminder on his PC screen to help fix the CCTV."

    "He can help fix the CCTV first, or attend the meeting first,"
    "or he can just ignore all of that and \ntidy up the files in his drawers."

    menu intro_menu:
        "Which one will he do?"

        "Tidy File":
            jump intro_p3_1_1
        "Attend Meeting":
            jump intro_p3_2_1
        "Fix CCTV":
            jump intro_p3_3_1

    label intro_p3_1_1:
        #[ IPD Workplace ]

        "Rai picks up the papers on his desk and opens his drawer."

        #[ Rai Appears ]

        #Rai (confused):
        Rai "Wait, what…?"

        "It was surprisingly tidy."
        "There are only a few cases that will make Rai have \nthe intention to tidy up his work drawer."
        "The first one is if it was untidy."
        "And the second one is if there were several important \npapers that seemed to look stuck or tucked between \na pile of folders in his work drawer."

        "If that was the case then he would have no choice \nbut to look for it fearing that it would get buried."
        "What was miraculous and magical about it is that \neven though he was prone to be forgetful,"
        "it was as neat as if he had just recently opened it."

        #Rai (shocked):
        Rai "When did I… tidy it up? Kinda forgot really."

        "What's going on today? Is the Rai Galilei starting \nto experience senility or fatigue from work so much"
        "that his mind is forced to forget the activities that \nhe did yesterday or maybe even more recent than that?"
        "Who knows."
        "But for Rai this seems like a plus for him since it’s \nalready clean. "
        "He can just put the papers that’s currently in his \nhands easily."

        #Rai (default):
        Rai "Maybe it’s one of my coworkers. Oh well, time to \nget back to Shigoto-san."

        #[ Rai Leaves ]
        #[ Black Screen ]

        jump intro_menu

    label intro_p3_2_1:
        #[ Meeting Room ]

        "Interdimensional Officers Discussion, an annual meeting with other branches to discuss progress between High-Ranking Officers in each branch."
        "Rai arrives with the file that his boss asked him to bring in, he also made sure that he got a copy for everyone as well."
        "He suddenly crashes with a Galileian that seems to be in a hurry."

        #[ SFX Bump ]
        #[ Galilean 1 Appears ]

        #Galilean 1:
        Galilean_1 "Oh, I’m sorry Sir Rai. Are you okay?"

        #[ Rai Appears ]

        #Rai (surprised):
        Rai "I’m okay, my bad. I was lost in my thoughts."

        #Galilean 1:
        Galilean_1 "My bad too sir, I am in a hurry, they said there’s some anomalies in the CCTV Room, and I am assigned to investigate it."

        #Rai (default):
        Rai "Okay then, feel free to go first."

        #Galilean 1:
        Galilean_1 "Thank you sir."

        #[ Galilean 1 Leaves ]

        "When the Galilean leaves, Rai enters the meeting room and sees that no one is there except for his boss."

        #Rai (confused):
        Rai "What happened Boss? Am I late?"

        #Boss:
        Boss "No, the higher ups suddenly rescheduled our meeting for next week due to some anomalies that they need to tackle at their own place."

        #Rai (sad):
        Rai "Too bad, I was hoping I could be useful today Boss."

        #Boss:
        Boss "Don't worry, I already said that you eagerly wait for them."

        "Rai’s Boss reassures him with a shoulder pat."

        #Boss:
        Boss "Is that the document that I asked you to fetch? It’s the notes for the meeting."

        #Rai (default):
        Rai "Yes it is Boss, here you go. Is there another task that you need me to do?"

        #Boss:
        Boss "No, you may go. Still, the anomaly that they mention seems weird, it suddenly happens when each representative has already gathered in the meeting room."

        #Rai (thinking):
        Rai "That reminds me, a Galilean also said something about a strange anomaly in the CCTV room. Is it alright if I go there first before going back to my office?"

        #Boss:
        Boss "I would highly appreciate it if you help that sector Rai."

        #Rai (happy):
        Rai "Affirmative Boss."

        #[ Boss Leaves ]
        #[ Rai Leaves ]

        "Thus, Rai starts to walk towards the CCTV room."

        #[ SFX Footsteps ]
        #[ Black Screen ]

        jump intro_p3_3_1

    label intro_p3_3_1:
        #[CCTV Room]

        "Rai sees two Galileans in the CCTV room as he memorizes the location and sector he needs to help repair, if there are any."

        #Rai (serious):
        Rai "Rai Galilei, reporting for duty. I heard there’s some strange anomalies in the CCTV Room. Was there a video leak or something else happened?"

        #Galilean 2:
        "Welcome sir. Well, there was a leak but not as in the video, but the cleaning liquid accidentally spilled."
        "Right now it’s mixed with oil reagents that the Athenean team brought."

        #Rai (default):
        Rai "Oh, I thought our records were leaked. A false alarm then."

        #Galilean 1:
        "Technically sir, it was not a false alarm."

        #Rai (default):
        Rai "Well yeah, make sense. I just remembered, I noticed there are several CCTVs that looked like they needed maintenance."

        #Galilean 2:
        "This is the major reason why we request the cleaning liquid but our hands are currently full because of the spilling incident…"

        #Rai (default):
        Rai "Well, let me do a favor by helping out then."

        #Galilean 1:
        "Very well sir, we will provide you with the gear."

        #[ BLACKSCREEN ]

        jump intro_p3_3_2

    label intro_p3_3_2:
        #[ Cell ]

        "As Rai walks to the cell room, a shadow flashes from his left side and bumps his body, almost knocking him down."

        #[ SFX Crash ]

        "Luckily his body reflex helped him to stand back up straight."
        "The figure that hit him left as quickly as it came. Rai spots a glimpse of animal-like fur."
        "Rai feels a bit dizzy and tries to figure out what happened."

        #[ SFX Sirens ]

        "Sirens roared through the room, a sign that a prisoner had escaped."

        #Galilean 3:
        "Sir Rai, there's a Jailbreaker on the loose!"

        #Rai (serious):
        Rai "I need intels."

        #Galilean 3:
        "Human with cat-like traits. According to the database he has hairy, sharp claws, and a long mustache."

        #Rai (thinking):
        Rai "Wait. Like a cat? Perhaps…"

        "Rai's intuition immediately suspects the person who bumped into him just now."

        #Rai (serious):
        Rai "Rai Galilei to Center, permission to perform IPD Protocol Code 058-Romeo Alpha India-555."
        Rai "Chasing a suspect of jailbreak, based on the characteristics of cat-like fur."

        #[SFX Inhale]

        #Rai (serious):
        Rai "State of the Arts, Engage!"

        "As soon as yelled and his body responded quickly as he wished."
        "He thinks fast as to how he would apprehend the cat-like inmate."

        "As Rai manifested the SotA, dust particles formed in front of him as tiny sparkles of lightning."
        "Blue tiny crystals circle around a light, and with a small swish the sparkles explode lightly."
        "A sign that the activation of SotA is complete."

        #Rai (serious):
        Rai "It's been a long time since I used this. Let’s see if I still remember that spell… Chaser!"

        "Chaser enchants his muscles, increasing his speed.• Maintaining the amount of the SotA, Rai starts to chase the suspect."

        "A radio call came from his receiver."

        #Galilean 1:
        "Would you like to activate the code sir?"

        #Rai (serious):
        Rai "Yes, the code for SotA activation."

        #Galilean 1:
        "First time hearing it officially, sir. We will secure the perimeter by the code we got."
        "We will send the last location where the suspect is detected, based on the tracker in the collar every inmate has."

        #Rai (serious):
        Rai "On it. Galilei out."

        "Digging through his memories of the last moment Rai had used this tactic, he walked down the hall while combing the left side."

        "An eerie feeling emanates from there for some reason…"

        #???:
        "Fancy meeting you here, my sweet margarine blondie cop."

        #Rai (serious):
        Rai "It's you… Catboy."

        #Felix Lynx (smirk) :
        Felix "Yes yes, it's me blondie. Felix Lynx! AHAHAHA!"

        "As Felix leaps towards Rai. He prepares to lunge into him."

        #[SFX jump and claw]

        "The height of the attack forced Rai into a defensive position, as Felix's claw swipes and kicks continued to attack him."

        #[SFX punch and wush wush (parrying punch) (berkali kali)]

        "Parrying attack after attack, Rai manages to hold his own."
        "But Felix's half-animal physiology clearly had the advantage in both stamina and attack power, forcing Rai to act defensively."

        #Rai (serious):
        Rai "Khh, melee attacks. I have to admit, this is difficult."

        #[SFX punch]

        "A deceptive punch shot comes from Felix, forcing Rai to change his stance to defend stronger."
        "The pause that was created made him manage to land a deadly scratch on Rai's face, which was unexpectedly blocked by Rai."
        "His eye glows as bright as the sparkles from the SotA."

        #Felix Lynx (surprised):
        Felix "Impossible… That eye..!"
        Felix "I REMEMBER THAT EYE VERY WELL."

        #Rai (excited):
        Rai "That's my line. And yes, catboy."
        Rai "FEAST UPON THESE EYES THAT BESTOWS UPON THY JUDGMENT!!!"
        Rai "Now it's my turn!! Niji-iro!!!"

        #[SFX electric]

        "SotA particles condense in Rai's iris."
        "It glows like a rainbow, increasing responsiveness and reactivity to the opponent's movements."
        "As the electricity sparks from his fingers and in a flash he attacks Felix with great speed."

        "Felix was unable to fend off every attack from Rai."

        "Felix becomes awry in the face of the attacks."
        "If he resists, the physical contact would shock him."
        "If he allows the attack to enter, the dense SotA particles enveloping Rai's fingers will only further damage his body."

        #Felix (annoyed):
        Felix "THIS BLONDIE!!!"

        #[SFX clawing (berkali kali)]

        "Felix wields a sharp claw, forcing Rai to keep his distance and uses that time to run away."
        "Not wasting much time, Rai immediately pursues him, letting him escape."

        "Rai's fast pace is immediately controlled by manifesting the Lorentz Rule on his fingers."
        "Firing solid particles of electricity as the intended target tries to dodge him."

        "The catboy enters the storage warehouse to cut to the chase."
        "He tries to knock down any object he can spot along the aisles of the storage warehouse."

        #[SFX throwing objects (berkali kali)]

        "Gallons, paint cans, iron trellises, whatever clang along the warehouses' walls Felix can throw on Rai’s way."
        "But Rai finds a way to evade the random obstacles this catboy makes."

        #Rai (serious):
        Rai "Hah! Just like an actual cat huh."

        #[SFX Electric]

        "Rai pumps electric jumps on his soles."
        "He uses a wooden plank as a support to jump somersaults."
        "Avoiding objects that were aimed at his face, lightning bolts and ice particles condenses from the surrounding water vapor."

        "Not satisfied, Rai immediately grabs a screwdriver that was attached to his uniform."
        "He throws it like a shuriken, which he injected electric SotA particles into."

        #[SFX throwing screwdriver (wushh kaya shuriken)]

        "And strike! The screwdriver just stabs Felix's calf."
        "Without wasting time, Rai immediately uses it to cut the distance by condensing SotA particles to increase his jumping power."
        "Ambushing him like a tiger pouncing on its prey."

        #Rai (happy):
        Rai "HA! Gotcha!"

        #Felix (hurt):
        Felix "UWAAAAGH!"

        #[ SFX Kick ]

        "Landing a knee strike on the nape of the suspect."
        "The target was successfully immobilized."

        #[ SFX Exhale ]
        #Rai (default) :
        Rai "State of the Arts, Terminate."

        "After knocking out Felix, Rai felt tired."
        "The State of the Arts that he was using slowly disappeared after he said the turn off chant."
        "He feels a bit heavy after using an ability that he’s never used in a long time."
        "He continued to connect his intercom to report back to the center."

        #Rai (serious) :
        Rai "Rai Galilei to Center, IPD Protocol Code 058-Romeo Alpha India-555, chasing a suspect of jailbreaking: success."
        Rai "Target has been immobilized."
        Rai "I'll bring the suspect back to his cell for further inspection."
        Rai "Galilei out."

        #[ CELL ]
        "Arriving at the cell, Rai realizes a faint buzzing sound from Felix’s pockets."
        "He starts to search for it and finds some sort of a communication device."

        #Rai (default) :
        Rai "Rai Galilei to Artemisia, I found a communication device in the back pocket of the jailbreaker."
        Rai "Request for assistance to check the device."

        #Artemisia :
        Artemisia "Affirmative, request accepted."
        Artemisia "Please connect the device to the computer and wait for a moment."

        #[ Black Screen ]

        #Artemisia :
        Artemisia "Artemisia to officer Rai Galilei, from our analysis It has some kind of tracking feature and we located two other similar devices."
        Artemisia "I will show you on the screen."
        Artemisia "The projector turns on, showing two red dots at a dimension coded as 611-813 Dimension aka the Farmland dimension."

        #Rai (default) :
        Rai "I request for capturing both of the targets."

        #Artemisia :
        Artemisia "Request granted. But I will assign a team of elite officers. You can immediately go to the dimension."

        #Rai (default) :
        Rai "Got it, I will finish here first then prepare for the next target. Galilei out."

        #[ Galilean Leaves ]
        #[ Rai Leaves ]
        #[ Black Screen ]

        jump intro_p3_3_3

    label intro_p3_3_3:
        #[ FARM ]

        "Arriving at the farm, Rai was greeted by the sound of different farm animals from the little chickens and ducks to much bigger ones like sheep, horses, and cows."
        "He looks at his watch waiting for the other Galileis to finish tracking the hideouts that were shown on the map earlier."

        #Rai (thinking) :
        Rai "I think I have some time to kill, I wonder what animals are in here."

        "Rai walks past the noisy shed full of ducks then to the chickens."
        "He enters the fenced grassfield where the sheeps are feeding on fresh grass."

        #Rai (thinking) :
        Rai "Where are the cows? I thought a farm would have cows…."

        "Curious because he didn't see a single cow outside."
        "So he went to the big building where some cows might be kept."

        #Rai  (happy) :
        Rai "Bingo, there you are."

        "Rai goes inside the building, approaching a cow that is having their meal time."

        #Rai (happy) :
        Rai "Let me give you some more, here."

        "Rai grabbed some extra hay near the entrance."
        "As if the cow knew this one human gives extra food, it eats the hay Rai gave with passion."
        "Another cow seemed to get jealous from the first cow getting extra hay so it started making noises asking for the same."

        #Rai (surprised) :
        Rai "Whoa! Calm down friend. Did your owner not give you enough?"
        Rai "There is still more for all of you."

        "Rai then gives other cows the same portion as the first one."

        #Rai (excited) :
        Rai "There you go!"
        Rai "Eat more, grow more, and be the strongest cow in the world!!!"

        #[SFX  Rai petting Cow noises they said www ]

        "When Rai was enjoying petting the cows, beeping came from his communication device."

        #Rai (default) :
        Rai "Is it time already?"
        Rai "Man… Alright. Galilean, what did you get?"

        #Galilean :
        "It’s positive, we found a place just like the coordinates we get. Waiting for the next order."

        #Rai (serious) :
        Rai "So they are not moving? Good job officer, wait for me. I will go there myself."

        #Galilean :
        "Affirmative."

        "Rai then parts ways with all the cows and all the other farm animals then goes to the place where the squad is waiting for him."

        #[ CAVE ]

        "An Artemisia gives the command to Rai Galilei from the data that they successfully got from the communication device."
        "And from the looks of it, it’s like some sort of cave."

        #Rai (serious)  :
        Rai "Artemisia, is this the right coordinates? What I can see is just an abandoned cave."

        #Artemisia (no sprite, in call) :
        Artemisia "Does it fit a hideout of a gang of criminals?"
        Artemisia "I told you to bring some men with you. We don't know how many guys are inside!"

        #Rai (serious) :
        Rai "Alright alright."
        Rai "It’s okay, we need to focus."
        Rai "Galileans check inside the cave!"
        Rai "I will stand by here in case something happens."

        #Galileans :
        "Ten-four!"

        "All three officers start entering the cave with caution."

        #[ SFX Wind and Footstep ]
        "The Galileans came out holding the criminal tightly as they walked out of the cave."
        "They marched down the hill."
        "The wind blowing filled the silence between them."
        "Suddenly the communication device held by Rai rang."

        #Galilean 1 :
        "We found the suspect sir."

        #Rai (happy) :
        Rai "Good job officers"

        #??? (Mira) :
        "No no no.."

        "Rai heard another woman’s voice from the device."
        "He got the location."

        #Rai (serious) :
        Rai "Let's go."

        "They headed lower down the hill as Rai walked in front of her."
        "Rai doesn't handcuff her because she wants to cooperate."
        "Rai glanced at her. They are now going to the other pinged location."

        #[ Waterfall ]
        #Artemisia (no sprite, in call) :
        Artemisia "This is the last location."

        #Rai (default) :
        Rai "Inside the waterfall I assume?"

        #Artemisia (no sprite, in call) :
        Artemisia "I think so. Careful if you go inside the waterfall, our terminal can’t reach that deep."

        #Rai (default) :
        Rai "You guys hear that? Keep each other safe."

        #Galileans :
        "Sir! Yes sir."

        "They search for the area around the waterfall."
        "It took quite some time since the area is wide."

        #[ Black Screen ]

        #Galilean 2 :
        "We found the suspect sir!"

        #Rai (default) :
        Rai "Good job officer, now everyone heard that come back to the meeting point."

        "After Rai and all the Galileans meet at the meeting point."
        "They prepare to go back to the farm."

        #Rai (default) :
        Rai "Before we’re leaving, is there anything else you need to do…?"

        #??? (Elysine):
        "Nope, I’m fine..."
        "I’ve left my farewell letter at home who kept me at her house."
        "She should have found it later."

        jump intro_p3_3_4

    label intro_p3_3_4:
        #[ FARM ]

        "They arrived at the farm with both suspects."
        "The suspects get sent back to IPD first with the Galileans while Rai observes the surroundings for the last time before he joins them back at IPD."

        #Rai :
        Rai "Good thing we caught all of them without any loss."
        Rai "I bet the barn will become famous after this incident because all of this, I feel bad for the co-"

        "The moment Rai says the last line, he suddenly has a strange feeling."
        "Like he has done all of this before."

        #Rai (nervous) :
        Rai "Is this what others call ‘Deja Vu’? Funny…"

        "With his look on the cow barn. \nThe uneasy feeling is still there."

        #Rai (thinking) :
        Rai "What did I miss…?"

        "He glances at the fences with the animals encaged."
        "He noticed a cow was missing from its place."
        "With a little doubt in his mind, Rai approached where the cows got placed."
        "He’s not wrong, one cow is missing."

        "Rai went inside the barn."

        jump wyen_1

    label wyen_1:
        #[SCENE 1]
        #[Black Screen]

        "Inside the barn…"

        #[SFX Barn’s door open]

        #[Inside Barn]

        #[CG opt. 7 Start]

        #Rai (Confused): “
        "Huh? Weird…"
        "..This barn looks quite unusual"
        "It’s nothing like the usual barn I’ve seen before."
        "The interior doesn’t even match the exterior."

        #Rai (Happy):
        "Ushi-san~ are you here?"

        #Rai (Confused):
        "Eh…?"

        #Rai (Confused):
        "Huh? It’s surprisingly empty here…"

        #Rai (Default):
        "Hmmm…Let’s see…"

        #[SFX footstep but on pretty grassy (?) surface (as in the barn) because of hay]

        #Rai (Default):
        "I wonder why this barn is so empty, where are the animals?"

        #(Delay)

        #Rai (Default):
        "Hmmm...Preeetty moist here… anyway, Ushi-san where are-"

        #Rai (Happy):
        "Ah!"

        #[CG opt 7 End]

        #[Inside Barn]

        #[SFX footstep but on pretty grassy (?) surface (as in the barn) because of hay but shorter because Rai approaching the cow]

        #Rai (Happy):
        "There you are Ushi-san!"
        "How do you get here?"

        #[pitchfork flying through screen?]
        #[SFX something flying “whusssh” and then SFX something metallic (pitchfork) hit the wall]
        #[While the metallic SFX plays blink the screen with white screen]

        #Rai (Surprised):
        "What the-"
        "This is… a pitchfork!?"
        "Why’s there’s a pitchfork flying towards me?!-"

        #Farmer:
        "Stop right there."

        #Rai (Surprised):
        "*gasp*"

        #[Farmer ga kita]

        #Farmer:
        "What are you doing here?"
        "This barn is not for the public."
        "Get out from here right now."

        #Rai (Nervous):
        "Ah! I'm sorry sir, I don't know that this place is off-limits."
        "I just want to say goodbye to a cow that I found earlier before I leave."

        #Farmer:
        "Then go say goodbye to that cow and leave as soon as possible."

        #Rai (Serious):
        "...?"
        "(Why the farmer is so tense and wants me to leave as soon as possible…)"
        "(It’s so out of character for him and it’s pretty suspicious too not gonna lie.)"
        "(Not to mention the pitchfork he throwed at me before… it’s a bit too much isn’t it?)"
        "Hmm…"

        #Rai (Default):
        "Before I say goodbye to this cow sir, may I ask something?"
        "Why is this barn off-limit in the first place? Isn’t it just a barn?"

        #Farmer:
        "No actual reason."
        "I just don’t want anybody tampering with my cow."

        #Rai (Serious):
        "Hmmm? But why is there only one cow in this barn though?"

        #Farmer:
        "It’s… not your business."

        #Rai (Serious):
        "..."
        "Now that I think about it, I don't see any cows in this farm except for this one."
        "It’s weird for a professional farmer like you that has already run this farm for years to only have one cow."
        "And from the record that I read before too, there’s no record of plague that attacked cows or anything in the past years either."

        #Farmer:
        "..."

        #Rai (Serious):
        "Let me be honest here, I feel like you’re hiding something here in this barn."
        "Can you tell me what it is, sir?"

        #Farmer:
        "...There’s nothing..."
        "THERE’S NOTHING THAT I HIDE HERE!"
        "ENOUGH! GET OUT RIGHT NOW OR ELSE I WILL FORCE YOU TO GET OUT!"

        #Rai (Serious):
        "... looks like I hit the jackpot huh?"

        #Farmer:
        "SHUT UP! I’M GONNA FORCE YOU TO GET OUT NOW!"

        #[SFX running (farmer run to Rai)]

        #Rai (Serious):
        "(Oh shit! He’s coming!)"

        #[Screen blinking with white screen]
        #[SFX running stopped]

        #???:
        "*chuckle*"
        "That’s enough, farmer."

        #Rai (Surprised):
        "Wha- who’s talking-"

        #[Wyen’s cow form appear]

        #Wyen (Cow) (Default):
        "Hello Mr. police officer, or should I say… Mr. Rai Galilei."

        #Rai (Surprised):
        "The cow’s… talking!? And how does it know my name!?"

        #Famer:
        "Wyen-sama…"
        "I’m sorry I can't protect your identity."

        #Rai (Surprised):
        "Wyen-sama…?"

        #Wyen (Cow) (Default):
        "Aww farmer, it’s okay, it’s not your fault."
        "I have gotten pretty bored lately anyway."

        #Farmer:
        "Yes, Wyen-sama."

        #Wyen (Cow) (Default):
        "So Mr. Rai Galilei…You must be very confused."
        "I’m sorry, now let me introduce myself properly."
        "My name is Wyen Aster. You can say that I'm the master of this place."

        #Rai (Serious):
        "Master… of this place? Wha-What do you mean?"

        #Wyen (Cow) (Default):
        "Owh, there’s no other meaning. It’s just what it is."

        #(Delay)

        #Wyen (Cow) (Default):
        "By the way…"
        "*giggle* My My, You’re pretty cute for a police officer, don’t you?"
        "Not to mention you called me ‘Ushi-san’ before... *giggle* that’s so cute."

        #Rai (Surprised/Flustered):
        "Wha- What are you talking about!?"
        "T-that’s not your problem and- and I’m not cuteeee!"

        #Wyen (Cow) (Default):
        "*giggle* You said you’re not cute but look how cute you are when you’re flustered."

        #Rai (Surprised/Flustered):
        "Ngh…Anyway!"

        #Rai (Serious):
        "So, if you’re the master of this place, then you’re the mastermind who’s pulling the strings behind all of these events right?"

        #Wyen (Cow) (Default):
        "Hmmm… For now, I’ll leave it to your imagination Mr. Rai Galilei because… it won’t be fun if i tell you now right?"

        #[Suddenly the screen is shaking]

        #Rai (Surprised):
        "What- What’s happening!?"

        #[Screen shaking again while blinking with white screen]
        #[Suddenly a door to Wyen’s secret chamber appear]

        #Rai (Surprised):
        "Is that… a door?"

        #Wyen (Cow) (Default):
        "Well Mr. Rai Galilei, if you want to know more, I'll be waiting in my chamber… but before that…"
        "You must face some trials first that will open this door."

        #Rai (Surprised):
        "Trials…?"

        #Wyen (Cow) (Default):
        "Yes and farmer, can you please accompany him and explain the trials to Mr. Rai Galilei?"

        #Famer:
        "Gladly, Wyen-sama."

        #Wyen (Cow) (Default):
        "Thank you farmer, well then… Ushi ma balls later I guess *giggle*"

        #[Wyen’s cow form disappear]

        #Rai (Serious):
        "Wait-! *gasp* that cow just disappeared!"

        #Rai (Serious): "
        "..."
        "Wait…"

        #Rai (Surprised):
        "..."
        "Did that cow… just deez nutted me?!"

        #Rai (Annoyed?):
        "Oh my god, I can’t believe U just got deez nutted by a cow! AAAAAAAGGGH!"

        jump wyen_2

    label wyen_2:
        #Farmer:
        "Well… now Mr. Rai, as Wyen-sama said earlier, shall I explain these trials to you?"

        #Rai (Default):
        "Ah right."
        "So… what’s this trial about?"

        #Farmer:
        "Let me explain it to you now."
        "So, there will be 3 trials that you need to pass."
        "Each trial has its own location but don’t worry I will escort you there."

        #Rai (Default):
        "Hmhm, great to hear that, and then?"

        #Farmer:
        "These trials will test your certain knowledge."
        "It’s to determine whether you have rights to face the Great Wyen-sama or not."

        #Rai (Default):
        "Hmhm, I see, and… if I fail in those trials? What will happen?"

        #Farmer:
        "Well, you’ll die."

        #Rai (Default):
        "Eh?"

        #Rai (surprised):
        "W-WAIT WHAT!!?? I’ll die!?"

        #Farmer:
        "If you fail, that's it."
        "But I will give you the freedom of choosing which trials you want to do first except for the last trial."
        "Each trials will have it’s own theme and i will tell about the theme later when we arrived at the trial’s location"
        "The last trial will have a “special” theme thus you need to pass the first 2 trials first to prove you’re worthy enough for the last trial."

        #Rai (thinking):
        "Interesting… So where are these trials going to be?"

        #Farmer:
        "The first trial will be in the market."
        "The second trial will be in the cave…"
        "And for the last trial will be in the waterfall."
        "With that said you can only choose the market and the cave for now"
        "Now, where do you want to go first Mr Rai?"

        #Rai (thinking):
        "(So… these trials aren’t jokes, are they?)"

        #Rai (nervous):
        "(If I fail, I'll die.)"
        "(I… should be cautious on these trials… especially the last trial.)"


        menu:
            "Where should I go first?"

            "The Market":
                $ chosen_trial = "market"
                #Rai (default):
                "I think we should go to the [chosen_trial] first."

                #Farmer:
                "Understood, let me escort you there."

                #[SFX footsteps]
                #[Fade out Black Screen]

                jump wyen_2_1
            "The Cave":
                $ chosen_trial = "cave"
                #Rai (default):
                "I think we should go to the [chosen_trial] first."

                #Farmer:
                "Understood, let me escort you there."

                #[SFX footsteps]
                #[Fade out Black Screen]
                jump wyen_2_2

    label wyen_2_1:
        #[Black Screen]

        "In the market…"

        #[Fish shop 2nd floor]

        #Farmer:
        "We have arrived Mr. Rai. Welcome to the Fish Shop’s second floor"

        #Rai (Default):
        "Woah, i can see the whole market from here "

        #Farmer:
        "Of course, It’s quite high here after all."

        #Rai (Default):
        "Yes, but still.. this is really crowded though"
        "Is there really a trial here? It’s pretty hard to imagine honestly."

        #Farmer:
        "Don’t worry, let’s continue. We haven’t arrived at the exact trial place."

        #Rai (Default):
        "Oh I see, okay"

        #[Only BG]
        #[SFX footsteps]

        #Farmer:
        "Now, we are here."

        #Rai (Thinking):
        "(...)"
        "(...)"
        "(...?)"
        "(Huh…?)"

        #Rai (Thinking):
        "This is the fish market right? But still, there’s only people… and of course fishes here."
        "There’s no sign of the so called trial though?"

        #Farmer:
        "Please wait a second, I'll take care of this."

        #[SFX clicking (?) the finger (Farmer click(?) his finger)]
        #[BG darkened]

        #Rai (Surprised):
        "Wha-What just happened!?"
        "Everything is frozen!"

        #Farmer:
        "Well, don’t be surprised. I’m Wyen-sama right hand after all, I can do at least this stuff."
        "Now shall we begin?"

        #Rai (Nervous):
        "I-i see, r-right, I’m ready."

        #Farmer:
        "So, this trial’s theme is pretty simple."
        "This trial will test your common knowledge like science, math, etc."

        #Rai (Thinking):
        "Common knowledge huh…it should be pretty easy."

        #Farmer:
        "Now if you’re ready, go over there."
        "There will be a paper inside the drawer with the questions for this trial."

        #Rai (Default):
        "Okay… looks pretty simple"

        #Farmer:
        "You need at least to be able to correctly answer half of the questions, if you don’t then you’ll lose."

        #Rai (Default):
        "Okay, I understand."
        "I’m ready now."

        #Farmer:
        "Then the trial will begin in…"
        "3…"
        "2…”"
        "1…"
        "Start!"

        menu trial_market_q1:
            "What is 3 x 2?"

            "3":
                pass
            "4":
                pass
            "5":
                pass
            "6":
                $ skor_trial_market += 1
                pass

        menu trial_market_q2:
            "What is the capital city of Central Java?"

            "Jakarta":
                pass
            "Special Region of Yogyakarta":
                pass
            "Semarang":
                $ skor_trial_market += 1
                pass
            "Solo":
                pass

        menu trial_market_q3:
            "Which one of the following animals that’s not invertebrate?"

            "Frog":
                $ skor_trial_market += 1
                pass
            "Squid":
                pass
            "Lobster":
                pass
            "Spider":
                pass

        menu trial_market_q4:
            "What is the tallest mountain in the solar system?"

            "Olympus Mons":
                $ skor_trial_market += 1
                pass
            "Mount Everest":
                pass
            "Mauna Kea":
                pass
            "Mount B. Ooba":
                pass

        menu trial_market_q5:
            "Who’s the first president of Indonesia?"

            "Abdurrahman ad-Dakhil":
                pass
            "Koesno Sosrodihardjo":
                $ skor_trial_market += 1
                pass
            "Soeharto":
                pass
            "Joko Widodo":
                pass

        menu trial_market_q6:
            "The answer of question 1 + √169 - (7 + The answer of question 1) = ?"

            "7":
                pass
            "5":
                pass
            "6":
                $ skor_trial_market += 1
                pass
            "8":
                pass

        menu trial_market_q7:
            "What is the the sixth planet in our solar system but from behind?"

            "Earth":
                $ skor_trial_market += 1
                pass
            "Venus":
                pass
            "Mars":
                pass
            "Jupiter":
                pass

        menu trial_market_q8:
            "Which one of the following answers are considered as Alkaline earth metals?"

            "Be, Mg, Ca, Sr, Ba, Ra":
                $ skor_trial_market += 1
                pass
            "H, Li, Na, K, Rb, Cs, Fr":
                pass
            "He, Ne, Ar, Kr, Xe, Rn":
                pass
            "M, P, As, Sb, Bi":
                pass

        menu trial_market_q9:
            "What number is the previous question?"

            "7":
                pass
            "8":
                $ skor_trial_market += 1
                pass
            "9":
                pass
            "10":
                pass

        menu trial_market_q10:
            "8 MA NUTZ.!"

            "GOTTEM":
                $ skor_trial_market += 1
                pass
            "GOTTEM":
                $ skor_trial_market += 1
                pass
            "GOTTEM":
                $ skor_trial_market += 1
                pass
            "GOTTEM":
                $ skor_trial_market += 1
                pass

        if skor_trial_market >= 5:
            $ trial_market = True
            pass
        else:
            $ current_trial = "trial_market_q1"
            jump wyen_bad_end_1

        #Farmer:
        "You have answered all the questions."
        "Now let us see how much score you get."
        "Your score is…"
        "[skor_trial_market]/10"

        #Farmer:
        "Congratulations, you have passed this trial."

        #Rai (Happy):
        "Phew…"

        #[SFX ceklek likes something unlocked]

        #Rai (Surprised):
        "Wow, that surprised me!"

        #Farmer:
        "Well now, please look outside the window, stick your hands outside and open your hands"

        #Rai (Default):
        "Eh? O-okay."

        #[SFX Krincing key]

        #Rai (Surprised):
        "WHOA!!! • A.. Key? • FROM THE SKY!!?? ."

        #Farmer:
        "That’s the key for completing this trial."

        if trial_cave:

            #Farmer:
            "Oh before we move on, Wyen-sama wants to say something to you."

            #Rai (Confused):
            "What? How do you know?"
            "Is that cow here?"

            #Farmer:
            "No, Wyen-sama’s not here but i can do telepathy to Wyen-sama and vice versa."
            "Right hand’s privilege."

            #Rai (Confused):
            "Er… sure… Right hand’s privilege"

            #Farmer:
            "Well, it seems that Wyen-sama want to congratulate you for passing the second trial."
            "Wyen-sama also can’t wait for your arrival in the secret chamber."

            #Rai (Default):
            "Wow, how kind of that cow, huh?"
            "Tell that cow, that i will definitely gonna arrest you.."

            #Farmer:
            "As you command Mr. Rai."
            "..."
            "..."
            "..."
            "Wyen-sama said “I will be waiting. Arrest me if you can.”"

            #Rai (Default):
            "Good."

            #(Delay)

            #Farmer:
            "Well, also now that you have passed the first two trials, now you are eligible for the the “special” last trial."

            #Rai (Thinking):
            "The last trial huh… I wonder how will it be."

            #Farmer:
            "Soon you’ll know why this trial is special, now shall we go?"

            #Rai (Default):
            "Right, there’s no need to think about it further."
            "Let me see with my own eyes now how special this trial be"

            #Farmer:
            "Good, now follow me."

            jump wyen_2_3
        else:
            #Rai (Default):
            "(Oh, surprisingly the key looks pretty.)"
            "(It’s pretty unexpected…)"

            #Farmer:
            "Now let’s continue, shall we?"

            #Rai (Default):
            "Yes!"

            #Rai (Thinking):
            "Oh, Since i have passed the trial in the market, now i only need to go to the cave for the next trial right?"

            #Farmer:
            "That’s right"
            "Before you face the last trial, you need to pass the trial in the cave first after this."

            #Rai (Default):
            "Okay, let’s go!"

            jump wyen_2_2
        return

    label wyen_2_2:
        #[Black Screen]

        "Inside the cave…"

        #[Inside Cave]
        #[SFX Cave Ambience]

        #Farmer:
        "Welcome to the cave, Mr. Rai Galilei."

        #Rai (Default):
        "Sheesh, It’s so damp here."
        "So where’s the trial?"

        #Farmer:
        "Almost there, let’s keep going now."
        "Oh, also watch your steps, it can be pretty slippery inside here"

        #Rai (Happy):
        "Oh, thank you for your concern."

        #[Only BG]
        #[SFX footsteps]

        #Rai (Default):
        "So, Sir Farmer, how long have you been together with that cow?"

        #Farmer:
        "Hmm? Why the sudden question?"

        #Rai (Default):
        "Nothing’s special, I'm just curious."

        #Farmer:
        "Well, if you ask me that question, then unfortunately I don't know."

        #Rai (Confused):
        "Huh? You don’t know how long you have been together with that cow?"

        #Farmer:
        "Yes, in fact, i don’t even remember how I became Wyen-sama’s right hand either."
        "It’s… just there… I just feel that I need to serve Wyen-sama well as the right hand."

        #Rai (Thinking):
        "That’s pretty sus… So I can assume that you never questioned that cow’s order either huh?"

        #Farmer:
        "That’s right and I don't feel the need to question Wyen-sama either, since I believe that Wyen-sama is always right."

        #Rai (Thinking):
        "...I see."

        #Rai (Thinking):
        "(I think he really doesn’t know anything huh…)"
        "(He’s blindly following that cow’s order, so it’s technically useless to get informations from him)"
        "(*sigh* Well, it looks like I really need to ask that cow by myself.)"

        #[Only BG]
        #[SFX footsteps]

        #Farmer:
        "This is the place Mr. Rai."

        #Rai (Default):
        "So this is the trial’s place…"

        #Rai (Confused):
        "But…"
        "This is a dead end though-"

        #Farmer:
        "Yes it is, because… in this trial you’ll need to face me one by one in the battle of death"

        #Rai (Surprised):
        "W-What!?"

        #Farmer:
        "Nah, Just kidding."

        #Rai (Annoyed):
        "..."

        #Farmer:
        "Well actually, that’s not a complete joke either since for this trial, I will be the one that gives you the questions."
        "So it’s kinda fighting with me right?"

        #Rai (Default):
        "Err… Maybe? I guess? I don’t know-"

        #Farmer:
        "Anyway, in this trial there will be some questions in Japanese"
        "You also need to correctly answer half of the questions to pass this trial."
        "Do you understand?"

        #Rai (Thinking):
        "Japanese huh? I will try my best."

        #Farmer:
        "Good. Now, are you ready Mr. Rai?"

        #Rai (Default):
        "Yes, I’m ready."

        #Farmer:
        "Okay, the trial will begin in…"
        "3…"
        "2…"
        "1…"
        "Start!"

        menu trial_cave_q1:
            "What is the seventh planet from the sun"

            "Earth":
                pass
            "Saturn":
                pass
            "Pluto":
                pass
            "Uranus":
                $ skor_trial_cave += 1
                pass

        menu trial_cave_q2:
            "What is the tallest building in the world?"

            "Burj Khalifa":
                $ skor_trial_cave += 1
                pass
            "Shanghai Tower":
                pass
            "Tokyo Skytree":
                pass
            "Lotte World Tower":
                pass

        menu trial_cave_q3:
            "Which one is not included in the Seven Wonders of the World?"

            "Taj Mahal":
                pass
            "Colosseum":
                pass
            "Statue of Liberty":
                $ skor_trial_cave += 1
                pass
            "Machu Picchu":
                pass

        menu trial_cave_q4:
            "{font=HinaMincho-Regular.ttf}あなたのなまえはなんですか？{/font}"

            "{font=HinaMincho-Regular.ttf}フイカりルイです。{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}ライカリレイです。{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}ライガリレイです。{/font}":
                $ skor_trial_cave += 1
                pass
            "{font=HinaMincho-Regular.ttf}フイガリレイです。{/font}":
                pass

        menu trial_cave_q5:
            "How do you say “i will drink water” in Japanese?"

            "{font=HinaMincho-Regular.ttf}みずをのみます。{/font}":
                $ skor_trial_cave += 1
                pass
            "{font=HinaMincho-Regular.ttf}みすをのみます。{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}みずおのみます。{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}みすおのみます。{/font}":
                pass

        menu trial_cave_q6:
            "What do you call a group of fish?"

            "A pack of fish":
                pass
            "A school of fish":
                $ skor_trial_cave += 1
                pass
            "A flock of fish":
                pass
            "A bunch of fish":
                pass

        menu trial_cave_q7:
            "There is 27 letters in the alphabet"

            "False":
                $ skor_trial_cave += 1
                pass
            "True":
                pass

        menu trial_cave_q8:
            "What do you say when you are about to leave your house in Japanese?"

            "{font=HinaMincho-Regular.ttf}ただいま{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}いってらしゃい{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}いきましょう{/font}":
                pass
            "{font=HinaMincho-Regular.ttf}いってきます{/font}":
                $ skor_trial_cave += 1
                pass

        menu trial_cave_q9:
            "Most Spiders have 8 eyes"

            "True":
                $ skor_trial_cave += 1
                pass
            "False":
                pass

        menu trial_cave_q10:
            "{font=HinaMincho-Regular.ttf}あなたはあかちゃんですか？{/font}"

            "{font=HinaMincho-Regular.ttf}はい、あかちゃんです{/font}":
                $ skor_trial_cave += 1
                pass
            "{font=HinaMincho-Regular.ttf}はい、かわいいあかちゃんです。{/font}":
                $ skor_trial_cave += 1
                pass
            "{font=HinaMincho-Regular.ttf}はい。{/font}":
                $ skor_trial_cave += 1
                pass
            "{font=HinaMincho-Regular.ttf}そうです。{/font}":
                $ skor_trial_cave += 1
                pass

        if skor_trial_cave >= 5:
            #Farmer:
            "You have answered all the questions."
            "Now let's see how much score you get."
            "Your score is…"
            "[skor_trial_cave]/10"
            $ trial_cave = True
            pass
        else:
            $ current_trial = "trial_cave_q1"
            jump wyen_bad_end_1

        #Rai (Default):
        "Nice I did it!!"

        #Farmer:
        "Congratulation Mr. Rai, you have passed this trial"

        #Rai (Happy):
        "Yeah!"

        #Rai (Happy):
        "..."

        #Rai (Confused):
        "(...)"
        "(...?)"
        "(It feels strange…)"

        #Farmer:
        "Oh and here’s the key that you get from this trial."

        #[SFX “Krincing” key]


        if trial_market:
            #Farmer:
            "Oh before we move on, Wyen-sama wants to say something to you."

            #Rai (Confused):
            "What? How do you know?"
            "Is that cow here?"

            #Farmer:
            "No, Wyen-sama’s not here but i can do telepathy to Wyen-sama and vice versa."
            "Right hand’s privilege."

            #Rai (Confused):
            "Er… sure… Right hand’s privilege"

            #Farmer:
            "Well, it seems that Wyen-sama want to congratulate you for passing the second trial."
            "Wyen-sama also can’t wait for your arrival in the secret chamber."

            #Rai (Default):
            "Wow, how kind of that cow, huh?"
            "Tell that cow, that i will definitely gonna arrest you.."

            #Farmer:
            "As you command Mr. Rai."
            "..."
            "..."
            "..."
            "Wyen-sama said “I will be waiting. Arrest me if you can.”"

            #Rai (Default):
            "Good."

            #(Delay)

            #Farmer:
            "Well, also now that you have passed the first two trials, now you are eligible for the the “special” last trial."

            #Rai (Thinking):
            "The last trial huh… I wonder how will it be."

            #Farmer:
            "Soon you’ll know why this trial is special, now shall we go?"

            #Rai (Default):
            "Right, there’s no need to think about it further."
            "Let me see with my own eyes now how special this trial be"

            #Farmer:
            "Good, now follow me."

            jump wyen_2_3
        else:
            #Rai (Default):
            "(Oh, surprisingly the key looks pretty.)"
            "(It’s pretty unexpected…)"

            #Farmer:
            "Now let’s continue, shall we?"

            #Rai (Default):
            "Yes!"

            #Rai (Thinking):
            "Oh, Since i have passed the trial in the cave, now i only need to go to the market for the next trial right?"

            #Farmer:
            "That’s right"
            "Before you face the last trial, you need to pass the trial in the market first after this."

            #Rai (Default):
            "Okay, let’s go!"

            jump wyen_2_1
        return

    label wyen_bad_end_1:

        $ skor_trial_cave = 0
        $ skor_trial_market = 0
        $ skor_trial_waterfall = 0

        #Farmer:
        "Well, it seems that you have failed this trial Mr. Rai Galilei."
        "It’s really unfortunate… but goodbye Mr. Rai."

        #Rai (Sad):
        Rai "No-!"

        #[Bad End screen]

        jump expression current_trial
        return

    label wyen_bad_end_2:

        #Wyen (Evil):
        "So that’s your only power huh"
        "*sigh* looks like i overestimated your power…"

        #Rai (Serious):
        Rai "Shit…"

        #[SFX nginggg like the bomb want to explode]

        #Wyen (Evil):
        "*chuckle* Well, It was a good time to know you Mr. Rai Galilei."
        "It’s sad that we must be apart because of this but…"
        "Sayonara… Mr. Police Officer…"

        #[SFX nginggg like the bomb want to explode instesifying and explode]

        jump wyen_ft_q1

    label wyen_2_3:
        #[Black Screen]

        "In the Waterfall…"

        #[Waterfall]
        #[SFX Waterfall]

        #Rai (Happy):
        "Oooh! So this is the last trial place, the waterfall!"
        "The scenery here is so fresh and calming!"

        #Rai (Default):
        "And the waterfall itself… It’s so pret-"
        "..."

        #Rai (Thinking):
        "(...)"
        "(...?)"

        #Farmer:
        "Hmm…? Something’s wrong Mr. Rai?"

        #Rai (Default):
        "Ah no, it’s nothing. Just thinking about something a little."

        #Rai (Thinking):
        "(What is this feeling? Why does it feel…?)"
        "(Like I've been here before?)"

        #Farmer:
        "Well then"
        "So as you know, this is the ‘special’ and also the last trial place."
        "This trial right here is special because it will test your knowledge or to be precise, your memory about yourself."

        #Rai (Surprised):
        "What? About myself?"

        #Farmer:
        "Yes, it can be about your past, your identity, your world, your job… Well, everything about yourself."
        "There would be some trivia question too there"

        #Rai (Surprised):
        "W-Wait wait wait."
        "First of all, how do you guys know everything about me in the first place!?"
        "Where do you get those infos!?"

        #Farmer:
        "So are you ready Mr. Rai?"

        #Rai (Surprised):
        "Answer my question first EeeeEeEe..."
        "Looks like I will need to add invasion of privacy in that cow’s bad deeds when I arrest that cow."

        #Rai (Default):
        "*sigh* Anyway, okay… I'm ready."

        #Farmer:
        "Good"
        "By the way, other than the theme of this trial itself, this place is also special."
        "Now come closer to the waterfall"
        "You’ll see that some words will appear inside it."

        #Rai (Surprised):
        "What? How’s that possible-"

        #Farmer:
        "Don’t mind it that much Mr. Rai, let’s just say… It's magic for now."

        #Rai (Confused):
        "Errr okay then- magic it is-"

        #(Delay)

        #Rai (Default):
        "Wait a minute… so in order for me to be able to read the words in the waterfall, I need to be really close to the waterfall right?"

        #Farmer:
        "Yes of course. Except if you have super eyes that can see anything from distance"

        #Rai (Default):
        "Of course i don’t have it"
        "Well, okay then, let me take off my upper clothes first, so it doesn’t get wet."

        #Farmer:
        "As you like it Mr. Rai"

        #Rai (Default):
        "Okay wait a sec."

        #(Hehehehehehehehehehe Change Rai’s Sprite to the Shirtless one)

        #Rai (Default):
        "Okay done. Now let me get closer to the waterfall…"

        #[SFX Man walking in the waterfall’s pond(?)]

        #Rai (Default):
        "Now let’s see…"

        #[Screen blinking with white screen]

        #Rai (Surprised):
        "Oh wow, some words are appearing now!"

        #Rai (Default):
        "Okay I’m ready now."

        #Farmer:
        "Okay, just like the past trials, you also need to answer half of the questions correctly, so be careful."

        #(Delay)

        #Farmer:
        "Now the last trial will begin in…"
        "3…"
        "2…"
        "1…"
        "Start!"

        menu trial_waterfall_q1:
            "With SOTA, how much are you able to lift now?"

            "1:75":
                pass
            "1:71":
                pass
            "1:77":
                pass
            "1:70":
                $ skor_trial_waterfall += 1
                pass

        menu trial_waterfall_q2:
            "Where do you stay?"

            "IPD sector 7":
                $ skor_trial_waterfall += 1
                pass
            "IPD sector 5":
                pass
            "IPD sector 62":
                pass
            "IPD sector 21":
                pass

        menu trial_waterfall_q3:
            "What is an Eiria?"

            "Border patroller":
                pass
            "Bodyguard":
                pass
            "Doctor":
                $ skor_trial_waterfall += 1
                pass
            "Watchmen":
                pass

        menu trial_waterfall_q4:
            "A kilogram of SOTA can lift … kilograms of mass"

            "25 kg":
                pass
            "50 kg":
                $ skor_trial_waterfall += 1
                pass
            "70 kg":
                pass
            "40 kg":
                pass

        menu trial_waterfall_q5:
            "How much is a cow’s visual field?"

            "330°":
                $ skor_trial_waterfall += 1
                pass
            "180°":
                pass
            "250°":
                pass
            "220°":
                pass

        menu trial_waterfall_q6:
            "How long does a pregnancy last in cows?"

            "9 months":
                $ skor_trial_waterfall += 1
                pass
            "12 months":
                pass
            "10 months":
                pass
            "7 months":
                pass

        menu trial_waterfall_q7:
            "01/04/2021"

            "Lord Akh’hooo":
                pass
            "Akh’hoo the Forbidden one":
                $ skor_trial_waterfall += 1
                pass
            "Akh”hoo the Mighty one":
                pass
            "Lord Akh’hoo the Forbidden one":
                pass

        menu trial_waterfall_q8:
            "A cow’s fart contribute to global warming"

            "False":
                pass
            "True":
                $ skor_trial_waterfall += 1
                pass

        menu trial_waterfall_q9:
            "How many compartments are there in a cow’s stomach?"

            "5":
                pass
            "2":
                pass
            "4":
                $ skor_trial_waterfall += 1
                pass
            "3":
                pass

        menu trial_waterfall_q10:
            "Who acts as a postman in IPD?"

            "Galilean":
                pass
            "Hasanea":
                pass
            "Gaean":
                pass
            "Hermesia":
                $ skor_trial_waterfall += 1
                pass

        if skor_trial_waterfall >= 5:
            pass
        else:
            $ current_trial = "trial_waterfall_q1"
            jump wyen_bad_end_1

        #Farmer:
        "You have answered all the questions."
        "Now let’s us see how many scores do you get."
        "Your score is…"
        "[skor_trial_waterfall]/10"

        #Rai (Default):
        "YEAH!"

        #Farmer:
        "Congratulations Mr. Rai, you have passed the last trial."

        #Rai (Happy):
        "Yaaay!"

        #[SFX something appears (Blussss? Like Mr Hakim in It takes two or maybe cring2 (?)]

        #Rai (Surprised):
        "Whoa!"

        #Farmer:
        "And.. That’s the key that you get from this trial."

        #Rai (Default): "
        "...Even the key magically appears."
        "This place is truly special huh-"

        #[SFX Krincing key]

        #Farmer:
        "Looks like you have passed all the trials Mr. Rai."
        "As expected from the one that caught Wyen-sama’s eyes a long time ago."

        #Rai (Confused):
        "Wait, based on what you just said…"
        "That means that cow has been observing me since a long time ago…"

        #Farmer:
        "Yes, Wyen-sama has been observing you since a long time ago."

        #Rai (Surprised):
        "So that’s why that cow knows everything about me! Since when exactly!?"

        #Farmer:
        "Unfortunately, even myself as the Wyen-sama’s right hand doesn’t know about it either."
        "Only Wyen-sama knows"

        #Rai (Annoyed): "
        "Geez, Now I’m sure that I will put invasion of privacy in that cow bad deeds"

        #Rai (Default):
        "Okay since i already got all the keys, that means i can now open the door and meet that cow right."

        #Farmer:
        "Yes of course, Mr Rai."

        #Rai (Happy):
        "Nice, let’s not waste anymore time!"

        #Rai (Default):
        "I’m gonna arrest that cow for sure now!"

        #Farmer:
        "As you wish Mr. Rai"
        "Let’s go back to the barn"

        jump wyen_3

    label wyen_3:
        #[Black Screen]

        "Inside the barn…"

        #[Inside Barn]

        #[SFX footstep but on pretty grassy (?) surface (as in the barn) because of hay]

        #Rai (Default):
        "At last…"

        #(Delay)

        #Rai (Default):
        "Now I just need to put the keys into its keyhole right Sir Farmer?"

        #Farmer:
        "Absolutely right Mr. Rai. Just insert each keys into its keyholes and the door will be open."

        #Rai (Default):
        "Okay here we go."

        #[SFX keys inserted in the keyhole 3 times]

        #Rai (Default):
        "Okay, each keys have already-"

        #[Screen blink once with white screen]

        #Rai (Surprised):
        "!!!"

        #[Screen transition to white screen and back to normal after a while]
        #[SFX Gate opened]

        #Farmer:
        "The door is now open Mr. Rai."
        "My job here is done as your escort and now you may meet with the Great Wyen-sama."
        "Once again I congratulate you for passing all the trials."

        #Rai (Default):
        "Thank you Sir Farmer and thanks for your escort too."

        #Farmer:
        "No problem Mr Rai. It’s an honor to escort you."
        "Now have a nice ‘conversation’ with Wyen-sama… but remember Wyen-sama won’t be that easy to be arrested."

        #Rai (Default):
        "Hah! Don’t worry! I will definitely arrest that cow for sure!"

        #Farmer:
        "*chuckle* Well let us see later."
        "See you again Mr. Rai"

        #Rai (Default):
        "See you again Sir Farmer!"

        #[Screen transition to white screen]
        #[SFX nyooming (teleported)]
        #[Black Screen]

        #Rai (Surprised):
        "Woah, where… is this?"
        "It’s all dark, I can’t see anything-"

        #Rai (Default):
        "Hello…? Anybody here…?"

        #???:
        "Ah so you have come Mr police officer."

        #Rai (Surprised):
        "Where-"

        #[Wyen’s appear]

        #Wyen (Default):
        "Here Mr. Rai Galilei."

        #Rai (Surprised):
        "What the-"

        #Wyen (Default):
        "*giggle* Surprised? This is my real form Mr. Rai."
        "Anyway…"

        #(Delay)

        #Wyen (Default):
        "Welcome to my secret chamber and congratulations for passing all the trials."

        #Rai (Confused):
        "Um… this is your secret chamber? But this is completely dark…"

        #Wyen (Default):
        "Owh don’t mind it *giggle*"
        "By the way Mr Rai, what do you want to drink? I have many kinds of tea and sweets, which one do you like?"

        #Rai (Surprised):
        "Wha-"

        #Wyen (Default):
        "Yes, we need to celebrate your success for passing all the trials."

        #Rai (Default):
        "Owh. Thank you, but I'm sorry it seems that we don’t need to do that celebration because…"

        #[SFX handcuffs taken out]

        #Rai (Serious):
        "You’re now arrested, cow."

        #Wyen (Default):
        "Oh my… How impatient…"
        "Well then… if that’s what you want…"

        #[SFX Wyen clicking finger]

        #[BG Changed to Galaxy]

        #Rai (Serious):
        "This is-!"
        "So this is the real form of the secret chamber…"

        #Wyen (Evil):
        "Aah, You’re so rude Mr. Rai, I already tried to be kind enough but you don’t accept my kindness, it hurts you know?."
        "You don’t even call me by my name even once, although we already share the same bath together."

        #Rai (Surprised):
        "Huh-"
        "W-What are you talking about!?"
        "I never shared a bath with you!."

        #Wyen (Evil):
        "Nah, you definitely already shared a bath with me!"
        "Remember the waterfall that was used as one of your trials?"

        #Wyen (Manic):
        "That’s my bathing place *chuckle*."

        #Rai (Surprised):
        "I- I-"

        #Wyen (Manic):
        "*chuckle* Oh also If you’re wondering why that Waterfall is so magical, Of course it’s because of my-"

        #Rai (Surprised):
        "LALALALA I DON’T HEAR ANYTHING! I DON’T KNOW WHO I AM, I DON’T CARE!"
        "ANYWAY, now I will need you to come with me!"

        #[SFX footsteps]

        #Wyen (Evil):
        "*chuckle* not so fast Mr. Police officer."

        #[Star sword come from upper screen and jailing Rai]
        #[+SFX]
        #[+maybe shake the screen too a little]

        #Rai (Serious):
        "What is this!?"

        #Wyen (Default):
        "It seems that you underestimate me a little Mr. Rai Galilei."
        "Let me give you a little refresher then."

        #Wyen (Evil):
        "My name is Wyen Aster. The master of this dimension."
        "So technically speaking, you won’t be able to arrest me Mr. Rai Galilei *chuckle*"

        #Rai (Serious):
        "Hah, go talk all you want, but I will definitely arrest you! Now look!"

        #[Screen blinking once and shaking]
        #[SFX rai touching the sword but it’s hot (Cessss (?)]

        #Rai (Serious):
        "Ouch! What the- it’s hot!"

        #Wyen (Evil):
        "Hahaha! Of course it is! That’s from a star, of course it’s hot!"
        "*sigh* I thought that you’re smarter than that Mr police officer."

        #Rai (Serious):
        "Nghh…"

        #Wyen (Evil):
        "Well then, shall we go to the main dish now Mr Rai?"

        #[SFX Wyen clicking finger]
        #[Wyen’s screen appear]

        #Wyen (Evil):
        "This screen will give you the questions that you need to solve."
        "But unlike the trial one, the theme here will be all about your friends."
        "And if you are wrong even on one question you will lose."

        #[CG Mid Start]

        #Wyen (Evil):
        "Now this is the last showdown to determine all."
        "If you fail, that screen will explode and kill you but if you win then you can arrest me."
        "How about it, Mr. Rai Gallilei? Will you accept the challenge?"

        #Rai (Serious):
        "Sure fine!, I accept!"
        "I know this is very risky but I will definitely win and arrest you!."

        #Wyen (Evil):
        "*chuckle* Nice spirit! I love it!"
        "But I warn you that this challenge will not be easy."

        #Rai (Serious):
        "Yes I know! But no matter how hard it is, I believe that I will win!."

        #Wyen (Manic):
        "Hahahahaha! Truly an exceptional human being you are."
        "I really have a right judgment to put my eyes on you!."
        "Now shall we begin? I can’t wait to see your defeated face Mr. Rai Galilei!"

        #Rai (Serious):
        "I’m ready! I can’t wait to arrest you either!."

        #Wyen (Evil):
        "HahahahahaHAHAHAHAHA!"

        #[CG Mid End]

        menu wyen_ft_q1:
            "When was {glitch=50.0}{color=#FF0000}Amicia Michella{/color}{/glitch}'s first live?"

            "December 22, 2019":
                jump wyen_bad_end_2
            "December 21, 2019":
                pass
            "December 18, 2019":
                jump wyen_bad_end_2
            "December 26, 2019":
                jump wyen_bad_end_2

        menu wyen_ft_q2:
            "What is first fan name of {glitch=50.0}{color=#FF0000}Taka Radjiman{/color}{/glitch}?"

            "Sobat Sukses":
                pass
            "Lobak Tachi":
                jump wyen_bad_end_2
            "Teammeat":
                jump wyen_bad_end_2
            "Meatable":
                jump wyen_bad_end_2

        menu wyen_ft_q3:
            "What is the name of {glitch=50.0}{color=#FF0000}Miyu Ottavia{/color}{/glitch}’s otter?"

            "Ogidu":
                jump wyen_bad_end_2
            "Ottapien":
                jump wyen_bad_end_2
            "Oto":
                jump wyen_bad_end_2
            "Otto":
                pass

        menu wyen_ft_q4:
            "What is the zodiac of {glitch=50.0}{color=#FF0000}Riksa Dhirendra{/color}{/glitch}?"

            "Gemini":
                jump wyen_bad_end_2
            "Cancer":
                jump wyen_bad_end_2
            "Capricorn":
                jump wyen_bad_end_2
            "Taurus":
                pass

        menu wyen_ft_q5:
            "In {glitch=50.0}{color=#FF0000}ZEA Cornelia{/color}{/glitch}’s name, What does ZEA stand for?"

            "Z-type Execution Automaton":
                jump wyen_bad_end_2
            "Z-type Executive Automaton":
                pass
            "Z-type Execution Automata":
                jump wyen_bad_end_2
            "Z-type Executive Automata":
                jump wyen_bad_end_2

        menu wyen_ft_q6:
            "The following are the nicknames of {glitch=50.0}{color=#FF0000}Hana Macchia{/color}{/glitch} except?"

            "Mahachia":
                pass
            "Kaki Kunyit":
                jump wyen_bad_end_2
            "Hanamaki":
                jump wyen_bad_end_2
            "Hanmak":
                jump wyen_bad_end_2

        menu wyen_ft_q7:
            "Who is the husbando of {glitch=50.0}{color=#FF0000}Azura Cecillia{/color}{/glitch} in Genshin Impact?"

            "Kaeya":
                jump wyen_bad_end_2
            "Itto":
                jump wyen_bad_end_2
            "Tartaglia (Childe)":
                pass
            "Venti":
                jump wyen_bad_end_2

        menu wyen_ft_q8:
            "Which one of the following answers is {glitch=50.0}{color=#FF0000}Nara Haramaung{/color}{/glitch}’s fan art hashtag?"

            "#Drawmaung":
                jump wyen_bad_end_2
            "#Gambarmaung":
                jump wyen_bad_end_2
            "#Maunggambart":
                pass
            "#Naradraw":
                jump wyen_bad_end_2

        menu wyen_ft_q9:
            "What is the nickname of {glitch=50.0}{color=#FF0000}Etna Crimson{/color}{/glitch} that was given by {glitch=50.0}{color=#FF0000}Tapak Langit{/color}{/glitch}?"

            "Kuli Borgar":
                jump wyen_bad_end_2
            "Bloody Borgar":
                jump wyen_bad_end_2
            "Bloody Ball":
                pass
            "Borgar Hero":
                jump wyen_bad_end_2

        menu wyen_ft_q10:
            "What is the title of {glitch=50.0}{color=#FF0000}Reza Avanluna{/color}{/glitch}’s first original song when debuted as a liver?"

            "Hari yang Cerah":
                jump wyen_bad_end_2
            "Coro Milk":
                jump wyen_bad_end_2
            "Ngimpi":
                jump wyen_bad_end_2
            "Mimpi":
                pass

        menu wyen_ft_q11:
            "What is {glitch=50.0}{color=#FF0000}Layla Alstroemeria{/color}{/glitch}’s dogs name?"

            "Kiara and Luka":
                jump wyen_bad_end_2
            "Kiana and Laika":
                jump wyen_bad_end_2
            "Kiana and Luka":
                jump wyen_bad_end_2
            "Kiara and Laika":
                pass

        menu wyen_ft_q12:
            "What is {glitch=50.0}{color=#FF0000}Bonnivier Pranaja{/color}{/glitch}’s fan name?"

            "Boneto":
                jump wyen_bad_end_2
            "Bonnitos":
                pass
            "Bonnito":
                jump wyen_bad_end_2
            "Bon Bon Bakudan":
                jump wyen_bad_end_2

        menu wyen_ft_q13:
            "When is {glitch=50.0}{color=#FF0000}Siska Leontyne{/color}{/glitch}’s birthday?"

            "May 1st":
                jump wyen_bad_end_2
            "February 14th":
                pass
            "August 29th":
                jump wyen_bad_end_2
            "September 13th":
                jump wyen_bad_end_2

        menu wyen_ft_q14:
            "What is the title of {glitch=50.0}{color=#FF0000}Derem Kado{/color}{/glitch}’s original song?"

            "Nekokati Abrakadabra":
                pass
            "Nekomata Abrakadabra":
                jump wyen_bad_end_2
            "Nekokati Alakazam":
                jump wyen_bad_end_2
            "Neko ga Arimasu":
                jump wyen_bad_end_2

        menu wyen_ft_q15:
            "Where does {glitch=50.0}{color=#FF0000}Nagisa Arcinia{/color}{/glitch} came from?"

            "MOE MOE KYUN":
                jump wyen_bad_end_2
            "MOELEN":
                jump wyen_bad_end_2
            "Mastimland":
                jump wyen_bad_end_2
            "MOELAND":
                pass

        menu wyen_ft_q16:
            "Based on her twitter account, Where does {glitch=50.0}{color=#FF0000}Mika Melatika{/color}{/glitch} live?"

            "Tree":
                jump wyen_bad_end_2
            "Your heart":
                jump wyen_bad_end_2
            "Clinic {glitch=50.0}{color=#FF0000}Hyona{/color}{/glitch}":
                pass
            "Under your bed":
                jump wyen_bad_end_2

        menu wyen_ft_q17:
            "What is the title of {glitch=50.0}{color=#FF0000}Xia Ekavira{/color}{/glitch}’s BGM that was given to {glitch=50.0}{color=#FF0000}Hyona Elatiora{/color}{/glitch}?"

            "Panther’s Coffee":
                pass
            "Panther’s Sunday":
                jump wyen_bad_end_2
            "Panther’s Tea":
                jump wyen_bad_end_2
            "Panther’s Morning":
                jump wyen_bad_end_2

        menu wyen_ft_q18:
            "What is the code color for {glitch=50.0}{color=#FF0000}Hyona Elatiora?{/color}{/glitch}"

            "#7C011E":
                pass
            "#75011D":
                jump wyen_bad_end_2
            "#7D0521":
                jump wyen_bad_end_2
            "#73021D":
                jump wyen_bad_end_2

        #[Star sword disappeared]

        #Wyen (Surprised):
        "*gasp*How could this be possible…"

        #Rai (Happy):
        "Hah! How about that huh!? I can solve your challenge!"

        #Wyen (Surprised):
        "How could you…"

        #Rai (Happy): “
        "Haha! Of course I can!"
        "You’re facing one of the best interdimensional police officer that already solved many cases and was recognized by a lot of-"

        #Wyen (Evil):
        "HOW COULD YOU NOT FIT DEEZ NUT IN YOUR MOUTH!"

        #Wyen (Evil):
        "GOTTEM!"

        #Rai (Surprised):
        "..."

        #Rai (Annoyed):
        "*sigh* of course of course…"
        "Hang in there Rai… Hang in there…"

        #(Delay)

        #Rai (Serious):
        "Anyway, I win! Now you must be a good cow and let me arrest you!"

        #Wyen (Default):
        "*sigh* fine… You win, you can arrest me now."

        #Rai (Default):
        "Nice to have your cooperation."
        "Now please stay-"

        #Wyen (Evil):
        "...*chuckle*Just kidding."

        #[Star sword come from upper screen and jailing Rai again]
        #[+SFX]
        #[+maybe shake the screen too a little]

        #Rai (Serious):
        "What!? This is cheating! I already won!"

        #Wyen (Evil):
        "Oh my Mr. police officer. You should realize that although you win, you’re still inside my domain *chuckle*."

        #Rai (Serious):
        "You never intended to play fair don’t you! You… damned cow!"

        #Wyen (Evil):
        "Oooh, How rude of you Mr. police officer, it’s not good."
        "Well as a punishment for being bad police officer I shall give you a punishment challenge."

        #[SFX Wyen clicking finger]
        #[Wyen’s screen appear]

        #Wyen (Evil):
        "Now Mr. Rai. Go ahead and solve it or else, you’ll die *chuckle*"

        #Rai (Annoyed):
        "Tch… I can't ignore it… I need to solve it or else I'll die."

        #Rai (Serious):
        "Okay… let’s do it!"

        #(Insert a glitched random word for the question and answers. Just glitched keyboard smash or random symbols are fine. Still put the timer and if Rai chooses any answer or the timer reaches zero then continue to the next section.).

        menu:
            "{glitch=50.0}{chaos}{sc}WHjfgejhwgQgbdoiaqb{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}AGHbfsgADkgo87fn2i87{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}bdkjsg&*TWQgdkgfcd{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}KLJOIjdbewhui0f98utrf{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}P87u8SOHCht{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}NJKFg083gnlkdf{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}IYCUIyuirw806tuio{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}lihy9i7ECT^^8iyhi{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc})(J*UYCH84byt5gvoijfli7r982cy6vuyUIY9{/sc}{/chaos}{/glitch}":
                pass

        #Rai (Surprised):
        "W-what is this? I can't read anything!"

        #Rai (Serious):
        "This is cheating!"

        menu:
            "{glitch=50.0}{chaos}{sc}SNuohwdfiebbfvct3rbcr{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}dnqyd7FWMLKJ875R{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}nlrewnyqct51nc{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}niuioyajknhtoyT{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}ti3un8ctyi{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}iofe83t9ytvoj052imnyv8b{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}nifuiBYiuwroyqngYUIFtuiew{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}ubTIWETRHR8vbdns4geq{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}IUnghouiby0wehiy{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}KJGBiuvO3VYUIBhrth{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}iutcv6w96vut4i3{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}giy9864Yigynea98byg{/sc}{/chaos}{/glitch}":
                pass

        menu:
            "{glitch=50.0}{chaos}{sc}ifsy769y(V6BYEfd{/sc}{/chaos}{/glitch}"

            "{glitch=50.0}{chaos}{sc}&(Tr9cv7wrt739by6fdkgbUUbgsau{/sc}{/chaos}{/glitch}":
                pass
            "{glitch=50.0}{chaos}{sc}NjbhyvHUGr86v7ysia7t68GYdv{/sc}{/chaos}{/glitch}":
                pass

        #[Screen blinking with red screen start]

        #Wyen (Evil):
        "Such a pity… You lost Mr. Police officer."

        #Rai (Serious):
        "No! That’s rigged! I can’t even read anything!"

        #Wyen (Evil):
        "Sadly, It is what it is. Goodbye Mr. Rai Galilei. It’s nice to meet you."

        #[SFX nginggg like the bomb want to explode start]

        #Rai (Serious):
        "NOOOO!"

        #[Screen blinking with red screen stop]

        #[SFX nginggg like the bomb want to explode intesifying and stop]
        #[Screen transition to White Screen]

        "..."
        "....."
        ".......?"

        #[Screen back to normal]
        #[Wyen’s secret chamber with happy birthday on it]

        #Rai (Confused):
        "Eh…"
        "I… didn’t die..?"

        #Rai (Surprised):
        "Whoa! What is this?!"

        #[SFX Confetti]

        #Wyen (Default):
        "*giggle* It’s for Mr. Rai’s birthday."

        #Rai (Surprised):
        "W-What?!"

        #Wyen (Default):
        "Today is the celebration of Mr. Rai Galilei’s birthday. Don’t you remember?"

        #Rai (Surprised):
        "B-but…"

        #Wyen (Default):
        "Huh, It seems that you don’t remember…"
        "Well It can’t be helped since you’re “The Rai” after all… Okay, let me explain everything for you now."

        #(Delay)

        #Wyen (Default):
        "I’m Wyen Aster, the master of this dimension… and an entity that was created by the will of inmates to celebrate Rai’s birthday."
        "And also by that will, I created this whole dimension… or shall I say… this game? • Just for the sake of celebrating Mr. Rai’s birthday."

        #Rai (Confused):
        "A game…?"

        #Wyen (Default):
        "Yes, this dimension’s real form is a visual novel game and I… no, everyone you have met and connected to this dimension are just game characters."
        "When you arrived in the trial places, you felt a strange feeling didn’t you?"

        #Rai (Surprised):
        "Ah! You’re right! I did feel strange there! It feels like… a dejavu i guess?"

        #Wyen (Default):
        "Yes… It is because you have already been there… in a different route of this game."
        "You don’t exactly remember it because I used my magic to erase your memories everytime you clear the route."

        #Rai (Surprised):
        "It’s…I-I can’t believe it…"

        #Wyen (Default):
        "Well, but this is the truth."

        #(Delay)

        #Wyen (Default):
        "Owh, also if you still don’t get it, you, yourself ‘The Rai’ is not the real Rai either."
        "You are also a character of this game that was created to represent the real Rai and you can also say that… I created you too."

        #Rai (Surprised):
        "W-WHAT!? SO MYSELF ISN’T THE REAL RAI!?"
        "AND… AND… I WAS ALSO CREATED BY YOU!?"

        #Wyen (Default):
        "*giggle* amusing isn’t it? You were a great actor though."

        #Rai (Sad):
        "...I…Then why I even…"
        "If i’m not the real Rai, for what i need to suffer all of these suffering…"
        "For what I do all of these things…"
        "I…"

        #Wyen (Default):
        "Oh, just because you’re not the real Rai doesn’t mean you’re not real by yourself."
        "For your information, the real Rai is the one that play this game, he’s the one that controls you, so every decision that you make before is also the decision that the real Rai made."
        "I believe that the real Rai is also happy with all the effort you have made too."

        #Rai (Surprised):
        "!!!"
        "That’s right…"

        #Rai (Happy):
        "*sobs* Thank you… Thank you…"

        #Wyen (Default):
        "Now now, don’t cry… You don’t want to ruin the celebration do you?"

        #Rai (Surprised):
        "Ah! That’s right! I’m sorry!"

        #Wyen (Default):
        "Good boy, now we have already reached the end, let me call everyone first."

        #Rai (Confused):
        "Everyone?"

        #Wyen (Default):
        "Okay, everyone please come here!"

        #[Inmates appear]

        #Felix (Smug):
        "Ahhh… at last it ended."

        #Mira (Happy):
        "Yuuhuu, good job everyone~"

        #Elysine (Shy):
        "H-hello.."

        #Rai (Surprised):
        "Wait! You guys! How do you get out!?"

        #Wyen (Default):
        "*giggle* I’m the one that free them out, they are also my creation after all"

        #Rai (Default):
        "Um… okay-"

        #Wyen (Default):
        "Well okay everyone! Let us end this with a blast! On the count of 3 everyone say ‘Happy Birthday Rai!’"
        "Okay? Let’s start!"

        #Everyone:
        "3!"
        "2!"
        "1!"

        #[CG 9 END START]

        #Everyone:
        "HAPPY BIRTHDAY RAI!"
        #[CG 9 END END]

        #=Credit=


#    $ persistent.phase1 = True
#    $ persistent.phase2 = False
#    $ persistent.phase3 = False
    $ persistent.trial_wyen_2_1 = False
    $ persistent.trial_wyen_2_2 = False
    return
