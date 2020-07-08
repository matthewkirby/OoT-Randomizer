from collections import namedtuple
from World import World
from Messages import update_message_by_id, get_message_by_id

# New messages added to the table at 0x0390-0x0394, 0x0290-0x0293

# COULD ADD A NEW FUNCTION TO CENTER TEXT.
# - Would need to know length of each character in pixels
# - Would need max length of text in pixels
# - Can then compute how much spec to prepend to a line.

# THINGS REMAINING TO DO
# - owls
# - Fix the doors no longer being locked after changing msg
# - Deal with the front/back kak potion shop doors
# - Write a function to center text
# - Add grotto region names

#   id      Entrance list                                                   opts    category    Message
SIGN_LIST = {
    # Dungeon
    0x0307: [['Kakariko Village -> Bottom of the Well'],                    0x13,   'dungeon',      "Dark! Narrow! Scary!\x01{}"], # Square sign in front of well
    0x030A: [['Dodongos Cavern Entryway -> Dodongos Cavern Beginning'],     0x13,   'dungeon',      "{}\x01Don't enter without permission!"], # Sign pointing into dodongo's cavern
    0x030F: [['Zoras Fountain -> Jabu Jabus Belly Beginning'],              0x13,   'dungeon',      "{}\x01Don't disturb Lord Jabu-Jabu!\x01--King Zora XVI"], # Sign outside of jabu as child
    0x0312: [['KF Outside Deku Tree -> Deku Tree Lobby'],                   0x13,   'dungeon',      "Just ahead:\x01{}"], # Sign in kokiri pointing towards deku tree
    0x031B: [['Gerudo Fortress -> Gerudo Training Grounds Lobby'],          0x13,   'dungeon',      "{}\x01Only registered members are\x01allowed!"], # Sign outside of gtg
    0x6013: [['Gerudo Fortress -> Gerudo Training Grounds Lobby'],          0x00,   'dungeon',      "This is the\x01{}\x04Nobody is allowed to enter\x01without a membership card."], # Talk to gtg entrance without card
    0x6014: [['Gerudo Fortress -> Gerudo Training Grounds Lobby'],          0x00,   'dungeon',      "This is the\x01{}\x04Membership card verified.\x04One try for 10 Rupees!\x04\x1b\x01Try\x01Don't try"], # Talk to npc to enter gtg with card LOOKS BAD

    # Indoors
    # The kak potion shop doors read the same message, have the same scene, and the same actor_id. How do I tell them apart??
    # 0x020E: [['Kakariko Village -> Kak Potion Shop Front'],                 0x20,   'indoor',   "{}\x01Closed until morning"], # Kak Potion Shop at night (msg 0290 and 0293 splits off here)
    0x0290: [['Market -> Market Potion Shop'],                              0x20,   'indoor',       "{}\x01Closed until morning"], # New message for Market Potion shop at night
    # 0x0293: [['Kak Backyard -> Kak Potion Shop Back']], # New message for Kak potion shop back at night
    0x020F: [['Kakariko Village -> Kak Shooting Gallery'],                  0x20,   'indoor',       "{}\x01Open only during the day"], # Kak shooting gallery at night (msg 0291 splits off here)
    0x0291: [['Market -> Market Shooting Gallery'],                         0x20,   'indoor',       "{}\x01Open only during the day"], # New message for Market shooting gallery at night
    0x0210: [['Market -> Market Mask Shop'],                                0x20,   'indoor',       "{}\x01Now hiring part-time\x01Apply during the day"], # Mask shop at night
    0x0211: [['Kakariko Village -> Kak Bazaar'],                            0x20,   'indoor',       "{}\x01Open only during the day"], # Kak Bazaar at night (msg 0x0292 splits off here)
    0x0292: [['Market -> Market Bazaar'],                                   0x20,   'indoor',       "{}\x01Open only during the day"], # New message for Market bazaar at night
    0x023A: [['Lake Hylia -> LH Fishing Hole'],                             0x20,   'indoor',       "{}"],
    0x0318: [['Lake Hylia -> LH Lab'],                                      0x13,   'indoor',       "{}"],
    0x031E: [['Kokiri Forest -> KF Kokiri Shop'],                           0x13,   'indoor',       "{}"],
    0x031F: [['Kokiri Forest -> KF Links House'],                           0x13,   'indoor',       "{}"],
    0x0333: [['Zoras Domain -> ZD Shop'],                                   0x13,   'indoor',       "{}"],
    0x033C: [['Kokiri Forest -> KF Midos House'],                           0x13,   'indoor',       "{}"],
    0x033D: [['Kokiri Forest -> KF Know It All House'],                     0x13,   'indoor',       "{}"],
    0x033E: [['Kokiri Forest -> KF House of Twins'],                        0x13,   'indoor',       "{}"],
    0x033F: [['Kokiri Forest -> KF Sarias House'],                          0x13,   'indoor',       "{}"],
    0x5020: [['Graveyard -> Graveyard Composers Grave'],                    0x20,   'indoor',       "{}"], # Read the gravestone atop the composer grave
    0x020D: [['Market -> Market Treasure Chest Game'],                      0x20,   'indoor',       "{}\x01Temporarily Closed\x01Open Tonight!"], # Treasure chest game at night
    0x0226: [['Kak Backyard -> Kak Odd Medicine Building'],                 0x20,   'indoor',       "{}\x01Closed\x04Gone for Field Study\x01Please come again!\x01--Granny"], # Granny's Potion Shop as child

    # Overworld
    0x0301: [['Gerudo Valley -> Hyrule Field'],                             0x13,   'overworld',    "{}"], # Arrow sign GV -> field (msgs 391 and 392 split off here)
    0x0391: [['Lake Hylia -> Hyrule Field'],                                0x13,   'overworld',    "{}"], # New msg for Arrow sign lake -> field
    0x0392: [['Kakariko Village -> Hyrule Field'],                          0x13,   'overworld',    "{}"], # New msg for arrow sign kak -> field
    0x0305: [['Death Mountain -> Kak Behind Gate'],                         0x13,   'overworld',    "{}"], # Arrow sign DMT-> kak (msg 390 splits off here)
    0x0390: [['Hyrule Field -> Kakariko Village'],                          0x13,   'overworld',    "{}"], # New message for field -> kak arrow sign
    0x0306: [['Kakariko Village -> Graveyard'],                             0x13,   'overworld',    "{}"],
    0x0308: [['Kak Behind Gate -> Death Mountain'],                         0x13,   'overworld',    "{}"],
    0x030B: [['Death Mountain -> Goron City'],                              0x13,   'overworld',    "{}"],
    0x030C: [['Hyrule Field -> ZR Front'],                                  0x13,   'overworld',    "{}"],
    0x0393: [['Zoras Fountain -> ZD Behind King Zora'],                     0x13,   'overworld',    "{}"], # New msg for arrow sign zf -> zd
    0x0314: [['Kokiri Forest -> Lost Woods'],                               0x13,   'overworld',    "{}"],
    0x0315: [['Hyrule Field -> Lon Lon Ranch'],                             0x13,   'overworld',    "{}"],
    0x0316: [['Hyrule Field -> Lon Lon Ranch'],                             0x13,   'overworld',    "{}"],
    0x0317: [['Hyrule Field -> Lake Hylia'],                                0x13,   'overworld',    "{}"],
    0x0319: [['Hyrule Field -> Gerudo Valley'],                             0x13,   'overworld',    "{}"], # Arrow sign field -> gv (msg 394 splits off here)
    0x0394: [['Gerudo Fortress -> GV Fortress Side'],                       0x13,   'overworld',    "{}"], # New msg for arrow sign gf -> gv
    0x031C: [['GF Outside Gate -> Wasteland Near Fortress'],                0x13,   'overworld',    "{}"],
    0x0320: [['Kokiri Forest -> LW Bridge From Forest'],                    0x13,   'overworld',    "{}"],
    0x0321: [['Death Mountain -> Goron City'],                              0x13,   'overworld',    "Follow the trail along the edge of\x01the cliff and you will reach\x01{}"], # Sign half-way up dmt
    0x0323: [['Death Mountain Summit -> DMC Upper Local'],                  0x13,   'overworld',    "\x05\41Death Mountain Summit\x05\40\x01Entrance to {}\x01ahead"], # Square sign dmt -> crater
    0x0339: [['Hyrule Field -> Market Entrance',
              'Hyrule Field -> Lon Lon Ranch'],                             0x13,   'overworld',    "{}\x01{}"], # Sign outside of Kokiri Forest in Hyrule Field
    0x033A: [['Hyrule Field -> Market Entrance',
              'Hyrule Field -> Lon Lon Ranch'],                             0x13,   'overworld',    "You are here: {}\x01This way to {}"], # Sign in field between market and llr
    0x6069: [['GV Fortress Side -> Gerudo Fortress'],                       0x13,   'overworld',    "{} is located beyond\x01this gate.\x01A kid like you has no business there."], # Gerudo gaurd on the gv bridge as child

    # Owls
    # 0x4003: [[],], # Lake owl
    # DMT owl
}

REGION_NAMES = {
    # Dungeons
    "\x05\42Deku Tree\x05\40":                  ['Deku Tree Lobby'],
    "\x05\41Dodongo's Cavern\x05\40":           ['Dodongos Cavern Beginning'],
    "\x05\43Jabu Jabu's Belly\x05\40":          ['Jabu Jabus Belly Beginning'],
    "\x05\42Forest Temple\x05\40":              ['Forest Temple Lobby'],
    "\x05\41Fire Temple\x05\40":                ['Fire Temple Lower'],
    "\x05\43Water Temple\x05\40":               ['Water Temple Lobby'],
    "\x05\46Spirit Temple\x05\40":              ['Spirit Temple Lobby'],
    "\x05\45Shadow Temple\x05\40":              ['Shadow Temple Entryway'],
    "\x05\41Bottom of the Well\x05\40":         ['Bottom of the Well'],
    "\x05\43Ice Cavern\x05\40":                 ['Ice Cavern Beginning'],
    "\x05\46Gerudo Training Grounds\x05\40":    ['Gerudo Training Grounds Lobby'],

    # Indoors
    "\x05\44Mido's House\x05\40":               ['KF Midos House'],
    "\x05\44Saria's House\x05\40":              ['KF Sarias House'],
    "\x05\44House of Twins\x05\40":             ['KF House of Twins'],
    "\x05\44Know It All House\x05\40":          ['KF Know It All House'],
    "\x05\44Kokiri Shop\x05\40":                ['KF Kokiri Shop'],
    "\x05\44Lakeside Laboratory\x05\40":        ['LH Lab'],
    "\x05\44Fishing Pond\x05\40":               ['LH Fishing Hole'],
    "\x05\44Carpenter's Tent\x05\40":           ['GV Carpenter Tent'],
    "\x05\44Guard House\x05\40":                ['Market Guard House'],
    "\x05\44Mask Shop\x05\40":                  ['Market Mask Shop'],
    "\x05\44Bombchu Bowling\x05\40":            ['Market Bombchu Bowling'],
    "\x05\44Potion Shop\x05\40":                ['Market Potion Shop', 'Kak Potion Shop Front', 'Kak Potion Shop Back'],
    "\x05\44Treasure Chest Game\x05\40":        ['Market Treasure Chest Game'],
    "\x05\44Bombchu Shop\x05\40":               ['Market Bombchu Shop'],
    "\x05\44Back Alley House\x05\40":           ['Market Man in Green House'],
    "\x05\44Carpenter's House\x05\40":          ['Kak Carpenter Boss House'],
    "\x05\44House of Skulltula\x05\40":         ['Kak House of Skulltula'],
    "\x05\44Impa's House\x05\40":               ['Kak Impas House', 'Kak Impas House Back'],
    "\x05\44Oddity Shop\x05\40":                ['Kak Odd Medicine Building'],
    "\x05\44Dampe's House\x05\40":              ['Graveyard Dampes House'],
    "\x05\44Goron Shop\x05\40":                 ['GC Shop'],
    "\x05\44Zora Shop\x05\40":                  ['ZD Shop'],
    "\x05\44Talon's House\x05\40":              ['LLR Talons House'],
    "\x05\44Lon Lon Stable\x05\40":             ['LLR Stables'],
    "\x05\44Lon Lon Tower\x05\40":              ['LLR Tower'],
    "\x05\44Bazaar\x05\40":                     ['Market Bazaar', 'Kak Bazaar'],
    "\x05\44Shooting Gallery\x05\40":           ['Market Shooting Gallery', 'Kak Shooting Gallery'],
    "\x05\44Great Fairy Fountain\x05\40":       ['Colossus Great Fairy Fountain', 'HC Great Fairy Fountain', 'OGC Great Fairy Fountain', 'DMC Great Fairy Fountain', 'DMT Great Fairy Fountain', 'ZF Great Fairy Fountain'],
    "\x05\44\x0F's House\x05\40":               ['KF Links House'],
    "\x05\44Temple of Time\x05\40":             ['Temple of Time'],
    "\x05\44Windmill\x05\40":                   ['Kak Windmill'],
    
    # Overworld
    "\x05\41Kokiri Forest\x05\x40":             ['Kokiri Forest'],
    "\x05\42Lost Woods Bridge\x05\x40":         ['LW Bridge From Forest', 'LW Bridge'],
    "\x05\42Lost Woods\x05\x40":                ['Lost Woods', 'LW Beyond Mido', 'LW Forest Exit'],
    "\x05\41Goron City\x05\x40":                ['GC Woods Warp', 'GC Darunias Chamber', 'Goron City'],
    "\x05\43Zora River\x05\x40":                ['Zora River', 'ZR Behind Waterfall', 'ZR Front'],
    "\x05\41Sacred Forest Meadow\x05\x40":      ['SFM Entryway'],
    "\x05\44Hyrule Field\x05\x40":              ['Hyrule Field'],
    "\x05\43Lake Hylia\x05\x40":                ['Lake Hylia'],
    "\x05\46Gerudo Valley\x05\x40":             ['Gerudo Valley', 'GV Fortress Side'],
    "\x05\44Market Entrance\x05\x40":           ['Market Entrance'],
    "\x05\45Kakariko Village\x05\x40":          ['Kakariko Village', 'Kak Behind Gate', 'Kak Impas Ledge'],
    "\x05\46Lon Lon Ranch\x05\x40":             ['Lon Lon Ranch'],
    "\x05\43Zora's Domain\x05\x40":             ['Zoras Domain', 'ZD Behind King Zora'],
    "\x05\41Gerudo Fortress\x05\x40":           ['Gerudo Fortress', 'GF Outside Gate'],
    "\x05\46Haunted Wasteland\x05\x40":         ['Wasteland Near Fortress', 'Wasteland Near Colossus'],
    "\x05\44Desert Colossus\x05\x40":           ['Desert Colossus'],
    "\x05\44Market\x05\x40":                    ['Market'],
    "\x05\44Castle Grounds\x05\x40":            ['Castle Grounds'],
    "\x05\44Temple of Time Entrance\x05\x40":   ['ToT Entrance'],
    "\x05\45Graveyard\x05\x40":                 ['Graveyard'],
    "\x05\41Death Mountain Trail\x05\x40":      ['Death Mountain', 'Death Mountain Summit'],
    "\x05\41Death Mountain Crater\x05\x40":     ['DMC Lower Local', 'DMC Lower Nearby', 'DMC Upper Local', 'DMC Upper Nearby'],
    "\x05\43Zora's Fountain\x05\x40":           ['Zoras Fountain'],

    # Grottos
    "Royal Family's Tomb":                      ['Graveyard Composers Grave'],
}

SignActor = namedtuple('SignActor', ['origmsg', 'newmsg', 'actor_id', 'scene', 'mask', 'actorprops'])
sign_actor_table = [
    #         origmsg   newmsg      actorid     scene   mask        actorprops
    SignActor(0x01,     0x91,       0x0039,     0x57,   0xFF00,     None),          # Arrow sign from lake -> field
    SignActor(0x01,     0x92,       0x0039,     0x52,   0xFF00,     None),          # Arrow sign from kak -> field
    SignActor(0x05,     0x90,       0x0039,     0x51,   0xFF00,     None),          # Arrow sign from Field -> Kak
    SignActor(0x0E,     0x93,       0x0039,     0x59,   0xFF00,     None),          # Arrow sign from fountain -> domain
    SignActor(0x0E,     0x90,       0x0009,     0x21,   0x003F,     (0x0380, 0x5)), # Market potion at night
    SignActor(0x0F,     0x91,       0x0009,     0x21,   0x003F,     (0x0380, 0x5)), # Market shooting gallery at night
    SignActor(0x11,     0x92,       0x0009,     0x21,   0x003F,     (0x0380, 0x5)), # Market bazaar at night
]


def replace_overworld_signs(messages, world):
    testid = 0x6014
    print('--------------------------------')
    print(get_message_by_id(messages, testid))
    print('--------------------------------')

    for sign_id, entrance_info in SIGN_LIST.items():
        entrance_list, opts, category, sign_text = entrance_info
        destination_list = [world.get_entrance(entr).connected_region.name for entr in entrance_list]

        # Replace the text with cleaner, formatted text (there HAS to be a better way to do this...)
        for idx in range(len(destination_list)):
            clean_dest = None
            for formatted_region, raw_region_list in REGION_NAMES.items():
                if destination_list[idx] in raw_region_list:
                    clean_dest = formatted_region
                    break

            # Print a message if not found
            if clean_dest is None:
                print("MISSING REGION NAME: " + destination_list[idx])
                clean_dest = destination_list[idx]

            destination_list[idx] = clean_dest

        # Update the messages table
        teststr = entrance_list[0]+"\x01"
        update_message_by_id(messages, sign_id, teststr+sign_text.format(*destination_list), opts) # Opts at the end are the text box type and position values WRAP THIS INTO THE TABLE ABOVE

    print('--------------------------------')
    print(get_message_by_id(messages, testid))
    print('--------------------------------')
