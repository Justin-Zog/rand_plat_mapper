"""
This dictionary stores all 'regions'.

Region: 'An area where the player can walk to any point in if all special events have occurred and they can use every HM.'

A region is stored like so:
Key: 'name of region'
Value: id
    The id of the region. (Used for the regionMatrix) (int)
"""

regionDict = {
    # Gyms and Elite Four and Cynthia
    'firstGym': 0,
    'secondGym': 1,
    'thirdGym': 2,
    'fourthGym': 3,
    'fifthGym': 4,
    'sixthGym': 5,
    'seventhGym': 6,
    'eighthGym': 7,
    'firstEliteFour': 8,
    'secondEliteFour': 9,
    'thirdEliteFour': 10,
    'fourthEliteFour': 11,
    'cynthia': 12,
    # Sandgem and Jubilife
    'sandgem/jubilife': 13,
    # Sandgem PC
    'sandgemPC': 14,
    # Jubilife PC
    'jubilifePC': 15,
    # GTS
    'GTS': 16,
    # Pal Park
    'palPark': 17,
    # Oreburgh
    'oreburgh': 18,
    # Oreburgh PC
    'oreburghPC': 19,
    # Bike Tunnel Above Oreburgh
    'oreburghBikeTunnel': 20,
    # Wayward Cave
    'waywardCave': 21,
    # Floaroma town
    'floaroma': 22,
    # Floaroma PC
    'floaromaPC': 23,
    # Route 205 (Floaroma Area the Galactic Goons are blocking)
    'route205': 24,
    # Fuego Iron Works
    'fuegoIronWorks': 25,
    # Entrance to Floaroma meadow just south of fuego iron works
    'meadowTopEnt': 26,
    # Eterna City
    'eterna': 27,
    # Eterna PC
    'eternaPC': 28,
    # Eterna's Galactic Base
    'eternaGalactic': 29,
    # Route 208
    'route208': 30,
    # Hearthome
    'hearthome': 31,
    # Hearthome PC
    'hearthomePC': 32,
    # Solaceon
    'solaceon': 33,
    # Solaceon PC
    'solaceonPC': 34,
    # Celestic
    'celestic': 35,
    # Celestic PC
    'celesticPC': 36,
    # Foggy house with Draco Meteor
    'foggyCelestic': 37,
    # Veilstone
    'veilstone': 38,
    # Veilstone PC
    'veilstonePC': 39,
    # Valor Villas
    'valorVillas': 40,
    # Valor Villas Rock Climb House
    'valorVillasRockClimbHouse': 41,
    # Sunnyshore
    'sunnyshore': 42,
    # Sunnyshore PC
    'sunnyshorePC': 43,
    # Rock Climb House in Sunnyshore
    'sunnyshoreRockClimbHouse': 44,
    # Victory Road Entrance
    'victoryRoadEnt': 45,
    # Victory Road Entrance PC
    'victoryRoadEntPC': 46,
    # Pokemon League
    'league': 47,
    # Pokemon League PC
    'leaguePC': 48,
    # Pokemon League Cave (victory road's other entrance)
    'leagueCave': 49,
    # Route 213
    'route213': 50,
    # Pastoria
    'pastoria': 51,
    # Pastoria PC
    'pastoriaPC': 52,
    # Route 218 Right
    'route218Right': 53,
    # Route 218 Left
    'route218Left': 54,
    # Canalave
    'canalave': 55,
    # Canalave PC
    'canalavePC': 56,
    # iron Island Cave Exit
    'ironIslandCaveExit': 57,
    # Snowpoint City
    'snowpoint': 58,
    # Snowpoint PC
    'snowpointPC': 59,
    # Lake Acuity Entrance
    'lakeAcuityEnt': 60,
    # Fight Area
    'fight': 61,
    # Fight Area PC
    'fightPC': 62,
    # Resort Area
    'resort': 63,
    # Resort PC
    'resortPC': 64,
    # Resort Bike House
    'resortBikeHouse': 65,
    # Resort Bike Cave
    'resortBikeCave': 66,
    # Survival Area
    'survival': 67,
    # Survival Area PC
    'survivalPC': 68,
    # Survival Surf House
    'route226House': 69,
    # Survival Cut Scene Area House
    'route227House': 70,
    # Survival Cut Scene Cave
    'starkCave': 71,
    # Survival Cut Scene Tunnel
    'route227Tunnel': 72,
    # Survival Rock Climb House
    'survivalRockClimbHouse': 73,

    # Misc. (Indoors and random places that matter)
    'eternaForest': 74,
    'oldChateauEnt': 75,
    'bikeHighway': 76,
    'deadend': 77,
    'mall': 78,
    'oldChateauHallway': 79,
    'oldChateauMain': 80,
    'mansion': 81,
    'ravagedPathTop': 82,
    'ravagedPathBottom': 83,
    'jubilifeTV': 84,
    # MC => Mt. Coronet
    'MC_geminiStairs': 85,
    'MC_southSummitMain': 86,
    'MC_southSummitBottomCave': 87,
    'MC_northSummitTopCave': 88,
    'MC_northSummitPitArea': 89,
    'MC_twoCaveOneStair': 90,
    'MC_manyPonds': 91,
    'MC_manyPondsRCStairs': 92,
    "MC_bridges": 93,
    'MC_bridgesStairs': 94,
    'MC_rockClimbCaveNorth': 95,
    'MC_rockClimbCaveSouth': 96,
    'MC_waterfall_northWFCave': 97,
    'MC_waterfall_southWFCave': 98,
    'MC_waterfall_rockClimbRight': 99,
    'MC_waterfall_rockClimbLeft': 100,
    'MC_strengthRight': 101,
    'MC_strengthLeft': 102,
    'MC_strengthUpper': 103,
    'MC_strengthBottom': 104,
    # Wayward Cave
    'waywardRight': 105,
    'waywardLeft': 106,
    # The Lakes
    'lakeAcuity': 107,
    'lakeAcuityCaveEnt': 108,
    'lakeValor': 109,
    'lakeValorCaveEnt': 110,
    'lakeVerity': 111,
    'lakeVerityCaveEnt': 112,
    # Floaroma Meadow
    'floaromaMeadowSouth': 113,
    'floaromaMeadowNorth': 114,
    # Sendoff Spring
    'sendoffSpringCave': 115,
    'sendoffSpringExit': 116,
    # Iron Island Caves
    'ironIslandCaveEnt': 117,
    'ironIslandCaveEsc': 118,
    'ironIslandCaveStairs': 119,
    # Galactic Bases
    'GEterna1f': 120,
    'GEternaCrates': 121,
    'GEternaTech': 122,
    'GMasterBall': 123,
    'GMasterBallEnt': 124,
    'GWarehouse': 125,
    'GWarehouseKey': 126,
    'GConferenceRight': 127,
    'GConferenceLeft': 128,
    'GHQ1f': 129,
    'GHQ1fStairs': 130,
    'GHQtwoTeleporters': 131,
    'GHQtwoStairs': 132,
    'GHQthreeTeleporters': 133,
    'GHQspreadTeleporters': 134,
    'GHQGreenTeleporter': 135,
    # Solaceon Ruins
    'SREnt': 136,
    'SRHiker': 137,
    'SRMan': 138,
    'SRThreeStair': 139,
    'SRThreeDown': 140,
    'SRThreeUp': 141,
    # Bike Tunnel Insides
    'bikeHighwayGirlTop': 142,
    'bikeHighwayGirlBottom': 143,
    'bikeHighwayTopInside': 144,
    'bikeHighwayBottomInside': 145,
    # Rock Smash Cave
    'rockSmashCaveMain': 146,
    'rockSmashCaveUpper': 147,

    # Important Deadends
    'arceus': 148,
    'spearPillar': 149,
    'bikeShop': 150,
    'bikeShopHostage': 151,
    'windWorksHostage': 152,

    # IDK if PointCrow even put these entrances in the game but...
    # newMoonIsland
    'newMoonIsland': 153,
    # fullMoonIsland
    'fullMoonIsland': 154
}
