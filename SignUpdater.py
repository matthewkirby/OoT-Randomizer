from World import World
from Messages import update_message_by_id

# Color can be added to dungeons and whatnot in the REGION NAMES section

# Complex things to replace
# 0x300A - has an option to ask about dc
# 0x300D - Comes up when you ask about dc in 0x300A

DUNGEON_SIGNS = {
    0x0307: ['Kakariko Village -> Bottom of the Well'," Dark! Narrow! Scary!\x01%s"],
    0x030A: ['Dodongos Cavern Entryway -> Dodongos Cavern Beginning', "%s\x01Don't enter without permission!"],
    0x0312: ['KF Outside Deku Tree -> Deku Tree Lobby', "Just ahead:\x01%s"],
}

INDOORS_SIGNS = {
    0x023A: ['Lake Hylia -> LH Fishing Hole', "%s"],
    # 0x0301: Hyrule Field (GV -> field, lake->field, kak->field)
    # 0x0302: Hyrule Castle Town
    # 0x0303: The Temple of Time
    # 0x030F: Zoras fountain dont disturb lord jabu jabu --king zora xvi
    # 0x0311: All those reckless enough to venture into the desert--please drop by our shop. Carpet merchant
    # 0x0313: Forest Temple
    # 0x0315: Talon and Malons Lon Lon Rang
    # 0x0316: The Great Ingos Ingo Ranch
    0x0318: ['Lake Hylia -> LH Lab', "%s"],
    # 0x031B: Gerudo Training Ground only registered members are allowed
    # 0x031C: haunted wasteland if you chase a mirage, the desert will swallow you. Only on path is true
    # 0x031D: Spirit Temple
    0x031E: ['Kokiri Forest -> KF Kokiri Shop', "%s"],
    0x031F: ['Kokiri Forest -> KF Links House', "%s"],
    # 0x032D: moutain summit danger ahead - keep out
    0x0333: ['Zoras Domain -> ZD Shop', "%s"],
    0x033C: ['Kokiri Forest -> KF Midos House', "%s"],
    0x033D: ['Kokiri Forest -> KF Know It All House', "%s"],
    0x033E: ['Kokiri Forest -> KF House of Twins', "%s"],
    0x033F: ['Kokiri Forest -> KF Sarias House', "%s"],
    # 0x0345: visit the house of the know it all brothers to get answers to all your item-related questions
}

OW_SIGNS = {
    # 0x0305: ['Hyrule Field -> Kakariko Village', "%s"], # This sign is in 2 spots. I think I need to make a new one! field->kak and dmt->kak
    0x0306: ['Kakariko Village -> Graveyard', "%s"],
    0x0308: ['Kak Behind Gate -> Death Mountain', "%s"],
    0x030B: ['Death Mountain -> Goron City', "%s"],
    0x030C: ['Hyrule Field -> ZR Front', "%s"],
    0x0314: ['Kokiri Forest -> Lost Woods', "%s"],
    0x0317: ['Hyrule Field -> Lake Hylia', "%s"],
    0x0319: ['Hyrule Field -> Gerudo Valley', "%s"], # MAKE SURE THIS ISN'T ALSO IN GERUDO FORTRESS
    0x0320: ['Kokiri Forest -> LW Bridge From Forest', "%s"],
    0x0321: ['Death Mountain -> Goron City', "Follow the trail along the edge of\x01the cliff and you will reach\x01%s"],
    0x0323: ['Death Mountain Summit -> DMC Upper Local', "Death Mountain Summit\x01Entrance to %s\x01ahead"], # Color 'Death Mountain Summit'
    0x6069: ['GV Fortress Side -> Gerudo Fortress', "%s is located beyond this gate.\x01A kid like you has no business there."],
}

SPECIAL_OW_SIGNS = {
    # 0x033A: you are here: hyrule castle this way to lon lon Ranch (this should have the market and llr entrances on it)
    #0x4003: 
        #What are you doing? You've come 
        #a long way to get up here...You should look at the Map 
        #Subscreen sometimes.
        #
        #[Link], this is a beautiful
        #lake full of pure, clear water.
        #
        #At the lake bottom there is
        #a Water Temple used to worship 
        #the water spirits. The Zoras are
        #guardians of the temple. Hoo hoo.

        #The Zoras come from Zora's
        #Domain in northeast Hyrule. An
        #aquatic race, they are longtime
        #allies of Hyrule's Royal Family.

        #I heard that only the Royal Family
        #of Hyrule can enter Zora's Domain...
        #Hoo hoo!

        #I'm on my way back to the castle.
        #If you want to come with me, hold
        #on to my talons!
    # 0x0339: hyrule castle lon lon Ranch (in field after leaving kokiri)
    #DMT owl
}

REGION_NAMES = {
    'Market Shooting Gallery': 'Shooting Gallery'
}



def replace_overworld_signs(messages, world):
    # print("-----------------------------------------")
    # print(world.get_entrance('Kokiri Forest -> KF Kokiri Shop').connected_region.name)
    # print("-----------------------------------------")

    SIGNS = {**INDOORS_SIGNS, **OW_SIGNS, **DUNGEON_SIGNS}

    for sign_id, entrance in SIGNS.items():
        # destination = REGION_NAMES[world.get_entrance(entrance).connected_region.name]
        destination = world.get_entrance(entrance[0]).connected_region.name
        update_message_by_id(messages, sign_id, entrance[1]%destination)
