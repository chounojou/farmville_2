
#Characters

define Rai          = Character("Rai", image="Rai")
define FRai         = Character("Rai", image="FRai")
define Boss         = Character("Boss", image="Boss")
define Galilean_1   = Character("Galilean 1", image="Galilean_1")
define Galilean_2   = Character("Galilean 2", image="Galilean_2")
define Galilean_3   = Character("Galilean 3", image="Galilean_3")
define Artemisia    = Character("Artemisia", image="Artemisia")
define Farmer       = Character("Farmer")
define Bread_Seller = Character("{size=-10}Bread Seller{/size}")
define Fisherman    = Character("Fisherman")
define Meat_Butcher = Character("{size=-10}Meat Butcher{/size}")
define Merchant     = Character("Merchant")
define Felix        = Character("Felix", image="Felix")
define Villager     = Character("Villager")
define Talking_Tree = Character("Talking Tree")
define Ducks        = Character("Ducks")
define Duck         = Character("Duck")
define Crowd        = Character("Crowds")
define FV_Seller    = Character("{size=-10}Greengrocer{/size}")

define Seller       = Character("Seller")
define Unknown      = Character("???")
define Crow         = Character("Crow")
define Adventurer   = Character("Adventurer")
define MiRA         = Character("MiRA", image="Mira")
define The_Girl     = Character("The Girl", image="Mira")
define The_Girl2     = Character("The Girl", image="Elsyne")
define Butcher      = Character("Butcher")
define Elsyne       = Character("Elsyne", image="Elsyne")

define Galileans    = Character("Galileans")

define Cow_Screen   = Character("Cow")
define Cow          = Character("Cow", image= "Cow")
define Wyen         = Character("Wyen", image= "Wyen")

define Man          = Character("Man")
define Old_Lady     = Character("Old Lady")

#+++++++++++++++++++++++     Sprites    ++++++++++++++++++++++++++++#
###########################================############################
#=========================== RAI DEFAULT =============================#
###########################================############################
image Rai Default   =    "Sprite/Rai/Rai_Half.png"
image side Rai Default:
    "Sprite/Rai/side Rai_Default.png"
    zoom 0.45

image Rai Annoyed   = "Sprite/Rai/Rai_Half.png"
image side Rai Annoyed   :
    "Sprite/Rai/side Rai_Annoyed.png"
    zoom 0.45

image Rai Surprised = "Sprite/Rai/Rai_Half.png"
image side Rai Surprised :
    "Sprite/Rai/side Rai_Surprised.png"
    zoom 0.45

image Rai Nervous   = "Sprite/Rai/Rai_Half.png"
image side Rai Nervous   :
    "Sprite/Rai/side Rai_Nervous.png"
    zoom 0.45

image Rai Sad       = "Sprite/Rai/Rai_Half.png"
image side Rai Sad       :
    "Sprite/Rai/side Rai_Sad.png"
    zoom 0.45

image Rai Serious   = "Sprite/Rai/Rai_Half.png"
image side Rai Serious   :
    "Sprite/Rai/side Rai_Serious.png"
    zoom 0.45

image Rai Happy     = "Sprite/Rai/Rai_Half.png"
image side Rai Happy     :
    "Sprite/Rai/side Rai_Happy.png"
    zoom 0.45

image Rai Thinking  = "Sprite/Rai/Rai_Half.png"
image side Rai Thinking  :
    "Sprite/Rai/side Rai_Thinking.png"
    zoom 0.45

image Rai Excited   = "Sprite/Rai/Rai_Half.png"
image side Rai Excited   :
    "Sprite/Rai/side Rai_Excited.png"
    zoom 0.45

###########################================############################
#============================ Farmer Rai =============================#
###########################================############################
image FRai Default   = "Sprite/Rai/Farmer Rai_Half.png"
image FRai GDefault   = im.Grayscale("Sprite/Rai/Farmer Rai_Half.png")
image FRai Grayscale = im.Grayscale("Sprite/Rai/Farmer Rai_Half.png")
image side FRai Default:
    "Sprite/Rai/side Farmer Rai_Default.png"
    zoom 0.45
image side FRai GDefault:
    im.Grayscale("Sprite/Rai/side Farmer Rai_Default.png")
    zoom 0.45

image FRai Annoyed   = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Annoyed:
    "Sprite/Rai/side Farmer Rai_Annoyed.png"
    zoom 0.45

image FRai Surprised = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Surprised:
    "Sprite/Rai/side Farmer Rai_Surprised.png"
    zoom 0.45

image FRai Nervous   = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Nervous:
    "Sprite/Rai/side Farmer Rai_Nervous.png"
    zoom 0.45

image FRai Sad       = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Sad:
    "Sprite/Rai/side Farmer Rai_Sad.png"
    zoom 0.45

image FRai Serious   = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Serious:
    "Sprite/Rai/side Farmer Rai_Serious.png"
    zoom 0.45

image FRai Happy     = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Happy:
    "Sprite/Rai/side Farmer Rai_Happy.png"
    zoom 0.45

image FRai Thinking  = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Thinking:
    "Sprite/Rai/side Farmer Rai_Thinking.png"
    zoom 0.45

image FRai Excited   = "Sprite/Rai/Farmer Rai_Half.png"
image side FRai Excited:
    "Sprite/Rai/side Farmer Rai_Excited.png"
    zoom 0.45

########################================############################
#============================ FELIX ===============================#
#=========================== INMATE 1 =============================#
########################================############################
image Felix Default:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Default:
    "Sprite/inmates #1/side Felix Default.png"
    zoom 0.45

image Felix Smirk:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Smirk:
    "Sprite/inmates #1/side Felix Smirk.png"
    zoom 0.45

image Felix Serious:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Serious:
    "Sprite/inmates #1/side Felix Serious.png"
    zoom 0.45

image Felix Annoyed:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Annoyed:
    "Sprite/inmates #1/side Felix Annoyed.png"
    zoom 0.45

image Felix Surprised:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Surprised:
    "Sprite/inmates #1/side Felix Surprised.png"
    zoom 0.45

image Felix Hurt:
    "Sprite/inmates #1/Felix Half.png"
    zoom 0.50
image side Felix Hurt:
    "Sprite/inmates #1/side Felix Hurt.png"
    zoom 0.45

#Inmates 2 (MiRA)
image Mira Default:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Default:
    "Sprite/inmates #2/side Default 1.png"
    zoom 0.20

image Mira Default2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Default2:
    "Sprite/inmates #2/side Default 2.png"
    zoom 0.20

image Mira Annoyed:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Annoyed:
    "Sprite/inmates #2/side Annoyed.png"
    zoom 0.20

image Mira Serious:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Serious:
    "Sprite/inmates #2/side Serious.png"
    zoom 0.20

image Mira Serious2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Serious2:
    "Sprite/inmates #2/side Serious 2.png"
    zoom 0.20

image Mira Angry:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Angry:
    "Sprite/inmates #2/side Angry.png"
    zoom 0.20

image Mira Surprised:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Surprised:
    "Sprite/inmates #2/side Surprise 1.png"
    zoom 0.20

image Mira Surprised2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Surprised2:
    "Sprite/inmates #2/side Surprise 2.png"
    zoom 0.20

image Mira Excited:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Excited:
    "Sprite/inmates #2/side Excited.png"
    zoom 0.20

image Mira Excited2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Excited2:
    "Sprite/inmates #2/side Excited 2.png"
    zoom 0.20

image Mira Happy:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Happy:
    "Sprite/inmates #2/side Happy.png"
    zoom 0.20

image Mira Happy2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Happy2:
    "Sprite/inmates #2/side Happy 2.png"
    zoom 0.20

image Mira Sad:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Sad:
    "Sprite/inmates #2/side Sad.png"
    zoom 0.20

image Mira Sad2:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Sad2:
    "Sprite/inmates #2/side Sad 2.png"
    zoom 0.20

image Mira Sad3:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Sad3:
    "Sprite/inmates #2/side Sad 3.png"
    zoom 0.20

image Mira Sad4:
    "Sprite/inmates #2/Default 1.png"
    zoom 0.33
image side Mira Sad4:
    "Sprite/inmates #2/side Sad 4.png"
    zoom 0.20

#Inmates 3 (Elsyne)
image Elsyne Default:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Default:
    "Sprite/inmates #3/side Default.png"
    zoom 0.45

image Elsyne Default2:
    "Sprite/inmates #3/Default 2.png"
    zoom 0.9
image side Elsyne Default2:
    "Sprite/inmates #3/side Sad 2.png"
    zoom 0.4

image Elsyne Angry:
    "Sprite/inmates #3/Default 2.png"
    zoom 0.9
image side Elsyne Angry:
    "Sprite/inmates #3/side Angry.png"
    zoom 0.4

image Elsyne Shy:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Shy:
    "Sprite/inmates #3/side Shy.png"
    zoom 0.45

image Elsyne Scared:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Scared:
    "Sprite/inmates #3/side Scared.png"
    zoom 0.45

image Elsyne Surprised:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Surprised:
    "Sprite/inmates #3/side Surprised.png"
    zoom 0.45

image Elsyne Surprised2:
    "Sprite/inmates #3/Default 2.png"
    zoom 0.9
image side Elsyne Surprised2:
    "Sprite/inmates #3/side Surprised 2.png"
    zoom 0.4

image Elsyne Sad:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Sad:
    "Sprite/inmates #3/side Sad.png"
    zoom 0.45

image Elsyne Sad2:
    "Sprite/inmates #3/Default 2.png"
    zoom 0.9
image side Elsyne Sad2:
    "Sprite/inmates #3/side Sad 2.png"
    zoom 0.4

image Elsyne Smile:
    "Sprite/inmates #3/Default.png"
    zoom 0.9
image side Elsyne Smile:
    "Sprite/inmates #3/side Smile.png"
    zoom 0.45

image Elsyne Smile2:
    "Sprite/inmates #3/Default 2.png"
    zoom 0.9
image side Elsyne Smile2:
    "Sprite/inmates #3/side Smile 2.png"
    zoom 0.4

#----------------------------------------------------------------------#
#----------------------------------WYEN--------------------------------#
#----------------------------------------------------------------------#
image Wyen Default:
    "Sprite/inmates #4/final/Wyen Half.png"
    zoom 0.60
image side Wyen Default:
    "Sprite/inmates #4/final/side Wyen Default.png"
    zoom 0.45
image Wyen Manic:
    "Sprite/inmates #4/final/Wyen Half.png"
    zoom 0.60
image side Wyen Manic:
    "Sprite/inmates #4/final/side Wyen Manic.png"
    zoom 0.45
image Wyen Smile:
    "Sprite/inmates #4/final/Wyen Half.png"
    zoom 0.60
image side Wyen Smile:
    "Sprite/inmates #4/final/side Wyen Smile.png"
    zoom 0.45
image Wyen Surprised:
    "Sprite/inmates #4/final/Wyen Half.png"
    zoom 0.60
image side Wyen Surprised:
    "Sprite/inmates #4/final/side Wyen Surprise.png"
    zoom 0.45


#Galileans
image Galilean_1 Default:
    "Sprite/Galilean Member/Galilean 1 (Cewek).png"
    zoom 0.50
image Galilean_2 Default:
    "Sprite/Galilean Member/Galilean 2 (Cowok).png"
    zoom 0.50
image Galilean_3 Default:
    "Sprite/Galilean Member/Galilean 3 (Cowok).png"
    zoom 0.50

######### Side Galelians
#image side Galilean_1 Default:
#    "Sprite/Galilean Member/side Galilean 1 (Cewek).png"
#    zoom 0.25
#image side Galilean_2 Default:
#    "Sprite/Galilean Member/side Galilean 2 (cowok).png"
#    zoom 0.25
#image side Galilean_3 Default:
#    "Sprite/Galilean Member/side Galilean 3 (cowok).png"
#    zoom 0.25

#Artemisia
image Artemisia Default:
    "Sprite/Artemisia/Artemisia Clear.png"
    zoom 0.45
image side Artemisia Black:
    "Sprite/Artemisia/Artemisia NotClear.png"
    zoom 0.25

#Boss
image Boss Default:
    "Sprite/Boss!/Boss Default.png"
    zoom 0.55
image Boss DefaultSparkle:
    "Sprite/Boss!/Boss Sparkle.png"
    zoom 0.55
#image side Boss Default:
#    "Sprite/Boss!/side Boss Default.png"
#    zoom 0.23


#Other NPC
image Adventurer Default:
    "Sprite/Adventurer/Adventurer.png"
    zoom 0.50

image Farmer Default:
    "Sprite/Farmer/Farmer.png"
    zoom 0.50

image Fisherman Default:
    "Sprite/Fisherman/Fisherman.png"
    zoom 0.50

image FruitsVeggies Seller:
    "Sprite/Fruits and Veggies Seller/Fruits and Veggies Seller.png"
    zoom 0.50

image MeatButcher Default:
    "Sprite/Butcher/no blood.png"
    zoom 0.50
image MeatButcher GDefault:
    im.Grayscale("Sprite/Butcher/no blood.png")
    zoom 0.50

image MeatButcher Blood:
    "Sprite/Butcher/blood.png"
    zoom 0.50

image Merchant Default:
    "Sprite/Merchant/the merchant.png"
    zoom 0.50

image Villager Default:
    "Sprite/Villager/Villager.png"
    zoom 0.50

image Cow Default:
    "Sprite/Cow/default.png"
    zoom 0.50
image side Cow Default:
    "Sprite/Cow/side Cow Default.png"
    zoom 0.40

image Cow WyenColor:
    "Sprite/Cow/wyen color ver.png"
    zoom 0.50
image side Cow WyenColor:
    "Sprite/Cow/wyen color ver.png"
    zoom 0.40

image TalkingTree Default:
    "Sprite/Talking tree!/just smile.png"
    zoom 0.50
image TalkingTree Smile:
    "Sprite/Talking tree!/beeg smile.png"
    zoom 0.50

#BG
image IPD WORKPLACE = "BG/IPD.jpg"
image Meeting Room  = "BG/Meeting Room.jpg"
image Jail          = "BG/Jail.jpg"
image Jail Red      = "BG/Jail (alarm).jpg"
image Village       = "BG/Village.jpg"
image Village Night = "Bg/Village Night.jpg"
image Market        = "BG/Market.jpg"
image Market Grayscale = im.Grayscale("BG/market.jpg")
image Farm          = "BG/Farm.jpg"
image Hill          = "BG/Hill.jpg"
image Fish Shop     = "BG/Fish shop.jpg"
image GFish Shop     = im.Grayscale("BG/Fish shop.jpg")
image CCTV          = "BG/CCTV.jpg"
image Barn          = "BG/Barn.jpg"
image Shed          = "BG/Shed.jpg"
image Dark Shed     = "Bg/Shed Dark.jpg"
image River         = "Bg/River.jpg"
image Corn Field    = "Bg/Corn field.jpg"

image Rooftop       = "BG/Roof top.jpg"
image market_2nd    = "BG/Roof top.jpg"

image black         = "BG/black-screen.png"
image white         = "BG/white-screen.png"


image caveTunnel:
    "BG/Cave tunnel.jpg"
    zoom 2.0
image caveNyabang:
    "BG/Cave nyabang.jpg"
    zoom 2.0
image caveFinal:
    "BG/Cave - final place.jpg"
    zoom 2.0

image Forest:
    "Bg/Forest.jpg"
    zoom 0.28

image Forest Night:
    "Bg/Forest Night.jpg"
    zoom 0.28

image waterfallDay  = "BG/Waterfall_Day.jpg"
image waterfallNight = "BG/Waterfall_Night.jpg"
image waterfallNightRed ="BG/Waterfall_Night_Red.jpg"

image galaxy        = "BG/WyenChamber.jpg"

#CG
image CG1:
    "CGs/CG_1.png"
    zoom 0.5
default persistent.cg1_unlocked = False
image CG2:
    "CGs/CG_2.png"
    zoom 0.5
default persistent.cg2_unlocked = False
image CG3:
    "CGs/CG_3.png"
    zoom 0.48
default persistent.cg3_unlocked = False
image CG4:
    "CGs/CG_4.png"
    zoom 0.48
default persistent.cg4_unlocked = False
image CG5:
    "CGs/CG_5.png"
default persistent.cg5_unlocked = False
image CG6:
    "CGs/CG_6.png"
default persistent.cg6_unlocked = False

image CG7:
    "CGs/CG_7.png"
default persistent.cg7_unlocked = False
image CG8:
    "CGs/CG_8.png"
default persistent.cg8_unlocked = False
image CG9:
    "CGs/CG_9.png"
default persistent.cg9_unlocked = False
image CG10:
    "CGs/CG_10.png"
default persistent.cg10_unlocked = False
image CG11:
    "CGs/CG_11.png"
default persistent.cg11_unlocked = False
image CG12:
    "CGs/CG_12.png"
default persistent.cg12_unlocked = False
image CG13:
    "CGs/CG_13.png"
default persistent.cg13_unlocked = False


#Assets
image Scratches Zoom:
    "Asset/Hebi/Tree_2_zoom.png"
    zoom 0.9
image Maps:
    "Asset/Map (ver2).png"
    zoom 0.36

image Scratches Zoom = "Asset/Hebi/Tree_2_zoom.png"

image pitchfork:
    im.Flip("Asset/Pitchfork.png", vertical=True)
    zoom 0.35
image moon_key:
    "Asset/moon-key.png"
    zoom 0.35
image star_key:
    "Asset/star-key.png"
    zoom 0.35
image sun_key:
    "Asset/sun-key.png"
    zoom 0.35

image star_sword:
    "Asset/Pedang.png"
    zoom 0.50

image gate_closed:
    "Asset/barn_door_close.png"
    zoom 0.40
image gate_open:
    "Asset/barn_door_open.png"
    zoom 0.40

image wyen_screen:
    "Asset/Hebi/Screen.png"

image Antena Device:
    "Asset/Hotaru/Rai Asset Jarum.png"
    zoom 0.4

image Radar Machine:
    "Asset/Hotaru/mesin radar rai.png"
    zoom 0.25

image Ring:
    "Asset/Hotaru/cincin gepeng.png"
    zoom 0.4

image Tempered Glass:
    "Asset/Hotaru/layar radar.png"
    zoom 0.4

image Rubber:
    "Asset/Hotaru/ban lentur.png"
    zoom 0.4

image Hair:
    "Asset/Sehelai Rambut.png"
    zoom 0.3

image Map:
    "Asset/Map (ver2).png"
    zoom 0.15

#Phases

default persistent.phase1 = True
default persistent.phase2 = False
default persistent.phase3 = False

#Variabel Phase1

define bebek = False
define kuda = False

#Variabel Phase2

default persistent.k2_caught = False
default persistent.k3_caught = False

#Variabel Phase3

#----------------------------------------------------------------------#
#-----------------------------Animation--------------------------------#
#----------------------------------------------------------------------#

image jail_blinking:
    "BG/Jail (alarm).jpg"
    0.5
    "BG/Jail.jpg"
    0.5
    repeat

image galaxy_blinking:
    "BG/WyenChamber_Red.jpg"
    1.0
    "BG/WyenChamber.jpg"
    1.0
    repeat

####Persistent Gallery####

init python:
    gallery = Gallery()

    gallery.button("cg1")
    gallery.image("CG1")
    gallery.condition("persistent.cg1_unlocked")

    gallery.button("cg2")
    gallery.image("CG2")
    gallery.condition("persistent.cg2_unlocked")

    gallery.button("cg3")
    gallery.image("CG3")
    gallery.condition("persistent.cg3_unlocked")

    gallery.button("cg4")
    gallery.image("CG4")
    gallery.condition("persistent.cg4_unlocked")

    gallery.button("cg5")
    gallery.image("CG5")
    gallery.condition("persistent.cg5_unlocked")

    gallery.button("cg6")
    gallery.image("CG6")
    gallery.condition("persistent.cg6_unlocked")

    gallery.button("cg7")
    gallery.image("CG7")
    gallery.condition("persistent.cg7_unlocked")

    gallery.button("cg8")
    gallery.image("CG8")
    gallery.condition("persistent.cg8_unlocked")

    gallery.button("cg9")
    gallery.image("CG9")
    gallery.condition("persistent.cg9_unlocked")

    gallery.button("cg10")
    gallery.image("CG10")
    gallery.condition("persistent.cg10_unlocked")

    gallery.button("cg11")
    gallery.image("CG11")
    gallery.condition("persistent.cg11_unlocked")

    gallery.button("cg12")
    gallery.image("CG12")
    gallery.condition("persistent.cg12_unlocked")

    gallery.button("cg13")
    gallery.image("CG13")
    gallery.condition("persistent.cg13_unlocked")
