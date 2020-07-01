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
    0x031B: ['Gerudo Fortress -> Gerudo Training Grounds Lobby', "%s\x01Only registered members are\x01allowed!"],
    # 0x6013: GTG with no card
    # 0x6014: GTG with card
}

INDOORS_SIGNS = {
    0x020E: ['Kakariko Village -> Kak Potion Shop Front', "%s\x01Closed until morning"], # Potion Shop at night, Color the location name light blue
    0x020F: ['Kakariko Village -> Kak Shooting Gallery', "%s\x01Open only during the day"], # Kak shooting gallery (check child message), color location light blue
    0x0211: ['Kakariko Village -> Kak Bazaar', "%s\x01Open only during the day"], # Kak Bazaar at night (is this the same message as child?), color location light blue
    0x023A: ['Lake Hylia -> LH Fishing Hole', "%s"],
    # 0x0301: Hyrule Field (GV -> field, lake->field, kak->field)
    # 0x0302: Hyrule Castle Town
    # 0x0303: The Temple of Time
    # 0x030F: Zoras fountain dont disturb lord jabu jabu --king zora xvi
    # 0x0311: All those reckless enough to venture into the desert--please drop by our shop. Carpet merchant
    # 0x0313: Forest Temple
    0x0318: ['Lake Hylia -> LH Lab', "%s"],
    
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
    0x0315: ['Hyrule Field -> Lon Lon Ranch', "%s"],
    0x0316: ['Hyrule Field -> Lon Lon Ranch', "%s"],
    0x0317: ['Hyrule Field -> Lake Hylia', "%s"],
    # 0x0319: ['Hyrule Field -> Gerudo Valley', "%s"], # This sign is also in gf pointing to gv
    0x031C: ['GF Outside Gate -> Wasteland Near Fortress', "%s"], # hw if you chase a mirage... MAKE SUR EITS NOT IN COLOSSSUS
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
    # Dungeons
    'Deku Tree Lobby': "\x05\42Deku Tree\x05\40",
    'Dodongos Cavern Beginning': "\x05\41Dodongo's Cavern\x05\40",
    'Jabu Jabus Belly Beginning': "\x05\43Jabu Jabu's Belly\x05\40",
    'Forest Temple Lobby': "\x05\42Forest Temple\x05\40",
    'Fire Temple Lower': "\x05\41Fire Temple\x05\40",
    'Water Temple Lobby': "\x05\43Water Temple\x05\40",
    'Spirit Temple Lobby': "\x05\46Spirit Temple\x05\40",
    'Shadow Temple Entryway': "\x05\45Shadow Temple\x05\40",
    'Bottom of the Well': "\x05\41Bottom of the Well\x05\40",
    'Ice Cavern Beginning': "\x05\43Ice Cavern\x05\40",
    'Gerudo Training Grounds Lobby': "\x05\46Gerudo Training Grounds\x05\40",

    # Indoors
    'KF Midos House': "\x05\44Mido's House\x05\40",
    'KF Sarias House': "\x05\44Saria's House\x05\40",
    'KF House of Twins': "\x05\44House of Twins\x05\40",
    'KF Know It All House': "\x05\44Know It All House\x05\40",
    'KF Kokiri Shop': "\x05\44Kokiri Shop\x05\40",
    'LH Lab': "\x05\44Lakeside Laboratory\x05\40",
    'LH Fishing Hole': "\x05\44Fishing Pond\x05\40",
    'GV Carpenter Tent': "\x05\44Carpenter's Tent\x05\40",
    'Market Guard House': "\x05\44Guard House\x05\40",
    'Market Mask Shop': "\x05\44Mask Shop\x05\40",
    'Market Bombchu Bowling': "\x05\44Bombchu Bowling\x05\40",
    'Market Potion Shop': "\x05\44Potion Shop\x05\40",
    'Market Treasure Chest Game': "\x05\44Treasure Chest Game\x05\40",
    'Market Bombchu Shop': "\x05\44Bombchu Shop\x05\40",
    'Market Man in Green House': "\x05\44House\x05\40", # Better name for this?
    'Kak Carpenter Boss House': "\x05\44House\x05\40", # Better name for this?
    'Kak House of Skulltula': "\x05\44House of Skulltula\x05\40",
    'Kak Impas House': "\x05\44Impa's House\x05\40",
    'Kak Impas House Back': "\x05\44Impa's House\x05\40", # Differentiate or nah?
    'Kak Odd Medicine Building': "\x05\44Oddity Shop\x05\40", # Better name?
    'Graveyard Dampes House': "\x05\44Dampe's House\x05\40",
    'GC Shop': "\x05\44Goron Shop\x05\40",
    'ZD Shop': "\x05\44Zora Shop\x05\40",
    'LLR Talons House': "\x05\44Talon's House\x05\40",
    'LLR Stables': "\x05\44Lon Lon Stable\x05\40",
    'LLR Tower': "\x05\44Lon Long Tower\x05\40",
    'Market Bazaar': "\x05\44Bazaar\x05\40",
    'Market Shooting Gallery': "\x05\44Shooting Gallery\x05\40",
    'Kak Bazaar': "\x05\44Bazaar\x05\40",
    'Kak Shooting Gallery': "\x05\44Shooting Gallery\x05\40",
    'Colossus Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'HC Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'OGC Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'DMC Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'DMT Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'ZF Great Fairy Fountain': "\x05\44Great Fairy Fountain\x05\40",
    'KF Links House': "\x05\44\x0F's House\x05\40",
    'Temple of Time': "\x05\44Temple of Time\x05\40",
    'Kak Windmill': "\x05\44Windmill\x05\40",
    'Kak Potion Shop Front': "\x05\44Potion Shop\x05\40",
    'Kak Potion Shop Back': "\x05\44Potion Shop\x05\40",

    # Overworld - THESE SHOULD ALL BE COLORED APPROPRIATELY
    'Kokiri Forest': "\x05\40Kokiri Forest\x05\x40",
    'LW Bridge From Forest': "\x05\40Lost Woods Bridge\x05\x40",
    'LW Bridge': "\x05\40Lost Woods Bridge\x05\x40",
    'Lost Woods': "\x05\40Lost Woods\x05\x40",
    'LW Forest Exit': "\x05\40Lost Woods\x05\x40", # Is this right?
    'GC Woods Warp': "\x05\40Goron City\x05\x40",
    'Zora River': "\x05\40Zora River\x05\x40",
    'LW Beyond Mido': "\x05\40Lost Woods\x05\x40",
    'SFM Entryway': "\x05\40Sacred Forest Meadow\x05\x40",
    'Hyrule Field': "\x05\40Hyrule Field\x05\x40",
    'Lake Hylia': "\x05\40Lake Hylia\x05\x40",
    'Gerudo Valley': "\x05\40Gerudo Valley\x05\x40",
    'Market Entrance': "\x05\40Market Entrance\x05\x40",
    'Kakariko Village': "\x05\40Kakariko Village\x05\x40",
    'ZR Front': "\x05\40Zora River\x05\x40",
    'Lon Lon Ranch': "\x05\40Lon Lon Ranch\x05\x40",
    'Zoras Domain': "\x05\40Zora's Domain\x05\x40",
    'GV Fortress Side': "\x05\40Gerudo Valley\x05\x40",
    'Gerudo Fortress': "\x05\40Gerudo Fortress\x05\x40",
    'GF Outside Gate': "\x05\40Gerudo Fortress\x05\x40",
    'Wasteland Near Fortress': "\x05\40Haunted Wasteland\x05\x40",
    'Wasteland Near Colossus': "\x05\40Haunted Wasteland\x05\x40",
    'Desert Colossus': "\x05\40Desert Colossus\x05\x40",
    'Market': "\x05\40Market\x05\x40",
    'Castle Grounds': "\x05\40Castle Grounds\x05\x40",
    'ToT Entrance': "\x05\40Temple of Time Entrance\x05\x40",
    'Graveyard': "\x05\40Graveyard\x05\x40",
    'Kak Behind Gate': "\x05\40Kakariko Village\x05\x40",
    'Death Mountain': "\x05\40Death Mountain Trail\x05\x40",
    'Goron City': "\x05\40Goron City\x05\x40",
    'GC Darunias Chamber': "\x05\40Goron City\x05\x40",
    'DMC Lower Local': "\x05\40Death Mountain Crater\x05\x40",
    'DMC Lower Nearby': "\x05\40Death Mountain Crater\x05\x40",
    'Death Mountain Summit': "\x05\40Death Mountain Trail\x05\x40", # I think...
    'DMC Upper Local': "\x05\40Death Mountain Crater\x05\x40",
    'DMC Upper Nearby': "\x05\40Death Mountain Crater\x05\x40",
    'ZR Behind Waterfall': "\x05\40Zora River\x05\x40",
    'Zoras Domain': "\x05\40Zora's Domain\x05\x40",
    'ZD Behind King Zora': "\x05\40Zora's Domain\x05\x40",
    'Zoras Fountain': "\x05\40Zora's Fountain\x05\x40",
    'LH Owl Flight': "\x05\40Lake Hylia\x05\x40",
    'DMT Owl Flight': "\x05\40Death Mountain Trail\x05\x40",
    'Kak Impas Ledge': "\x05\40Kakariko Village\x05\x40",

    # Grotto
    # Fill these in eventually, not needed until I worry about mixed pools
}



def replace_overworld_signs(messages, world):
    # print("-----------------------------------------")
    # print(world.get_entrance('Kokiri Forest -> KF Kokiri Shop').connected_region.name)
    # print("-----------------------------------------")

    SIGNS = {**INDOORS_SIGNS, **OW_SIGNS, **DUNGEON_SIGNS}

    for sign_id, entrance in SIGNS.items():
        try:
            destination = REGION_NAMES[world.get_entrance(entrance[0]).connected_region.name]
        except KeyError:
            destination = world.get_entrance(entrance[0]).connected_region.name
            print("MISSING REGION NAME: " + destination)
        update_message_by_id(messages, sign_id, entrance[1]%destination)
