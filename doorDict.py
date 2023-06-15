"""
This dictionary stores all the 'doors'.
Door: An entrance with a destination.

A door is stored like so:
Key: "name of door"
Value: ['destination', 'region', canReEnter]
    The name of the door that this door leads to. (String)
    The name of the region that this door belongs to. (String)
    A boolean that says whether the player can reEnter the door. (Boolean)
"""

doorDict = {
    # Gyms and Elite Four and Cynthia
    'firstGym': ['', 'firstGym', True],
    'secondGym': ['', 'secondGym', True],
    'thirdGym': ['', 'thirdGym', True],
    'fourthGym': ['', 'fourthGym', True],
    'fifthGym': ['', 'fifthGym', True],
    'sixthGym': ['', 'sixthGym', True],
    'seventhGym': ['', 'seventhGym', True],
    'eighthGym': ['', 'eighthGym', True],
    'firstEliteFour_top': ['', 'firstEliteFour', False],
    'firstEliteFour_bottom': ['', 'firstEliteFour', False],
    'secondEliteFour_top': ['', 'secondEliteFour', False],
    'secondEliteFour_bottom': ['', 'secondEliteFour', False],
    'thirdEliteFour_top': ['', 'thirdEliteFour', False],
    'thirdEliteFour_bottom': ['', 'thirdEliteFour', False],
    'fourthEliteFour_top': ['', 'fourthEliteFour', False],
    'fourthEliteFour_bottom': ['', 'fourthEliteFour', False],
    'cynthia': ['', 'cynthia', False],

    # Sandgem Town
    'sandgem_lakeVerity_ent': ['', 'sandgem/jubilife', True],
    'sandgemPC': ['', 'sandgem/jubilife', True],
    'sandgemPM': ['', 'sandgem/jubilife', True],
    'sandgem_bottomLeftHouse': ['', 'sandgem/jubilife', True],
    'sandgem_bottomRightHouse': ['', 'sandgem/jubilife', True],
    # Sandgem PC
    'sandgemPC_exit': ['', 'sandgemPC', True],
    'sandgemPC_left': ['', 'sandgemPC', True],
    'sandgemPC_right': ['', 'sandgemPC', True],
    # Sandgem Teleports and Hidden Doors
    'sandgem_teleport': ['sandgemPC_teleport', 'sandgem/jubilife', False],
    'sandgemPC_teleport': ['sandgem_teleport', 'sandgemPC', False],
    'sandgem_surfToPalPark': ['palPark_surfToSandgem', 'sandgem/jubilife', False],

    # Jubilife
    'jubilifePC': ['', 'sandgem/jubilife', True],
    'jubilifePM': ['', 'sandgem/jubilife', True],
    'jubilife_bottomHouse': ['', 'sandgem/jubilife', True],
    'jubilife_topRightHouse': ['', 'sandgem/jubilife', True],
    'jubilife_tv': ['', 'sandgem/jubilife', True],
    'jubilife_flagLeft': ['', 'sandgem/jubilife', True],
    'jubilife_flagRight': ['', 'sandgem/jubilife', True],
    'jubilife_tunnel': ['', 'sandgem/jubilife', True],
    'jubilife_topCave': ['', 'sandgem/jubilife', True],
    'jubilife_rightCave': ['', 'sandgem/jubilife', True],
    # Jubilife PC
    'jubilifePC_exit': ['', 'jubilifePC', True],
    'jubilifePC_left': ['', 'jubilifePC', True],
    'jubilifePC_right': ['', 'jubilifePC', True],
    # Jubilife Teleports and Hidden Doors
    'jubilife_teleport': ['jubilifePC_teleport', 'sandgem/jubilife', False],
    'jubilifePC_teleport': ['jubilife_teleport', 'jubilifePC', False],
    'jubilife_walkToGTS': ['GTS_walkToJubilife', 'sandgem/jubilife', False],

    # GTS
    'GTS_ent': ['', 'GTS', True],
    'GTS_house': ['', 'GTS', True],
    # GTS Hidden Doors
    'GTS_walkToJubilife': ['jubilife_walkToGTS', 'GTS', True],

    # Pal Park
    'palParkHouse': ['', 'palPark', True],
    'palPark_ent': ['', 'palPark', True],
    # Pal Park Hidden Doors
    'palPark_surfToSandgem': ['sandgem_surfToPalPark', 'palPark', False],

    # Oreburgh
    'oreburghPC': ['', 'oreburgh', True],
    'oreburghPM': ['', 'oreburgh', True],
    'oreburgh_museum': ['', 'oreburgh', True],
    'oreburgh_gym': ['', 'oreburgh', False],
    'oreburgh_mine_ent': ['', 'oreburgh', True],
    'oreburgh_houseByMine': ['', 'oreburgh', True],
    'oreburgh_houseBelowMuseum': ['', 'oreburgh', True],
    'oreburgh_centerHouse': ['', 'oreburgh', True],
    'oreburgh_houseByGym': ['', 'oreburgh', True],
    'oreburgh_cave': ['', 'oreburgh', True],
    'oreburgh_topLeftHouse': ['', 'oreburgh', True],
    'oreburgh_houseByPM': ['', 'oreburgh', True],
    # Oreburgh PC
    'oreburghPC_exit': ['', 'oreburghPC', True],
    'oreburghPC_left': ['', 'oreburghPC', True],
    'oreburghPC_right': ['', 'oreburghPC', True],
    # Oreburgh Teleports and Hidden Doors
    'oreburgh_teleport': ['oreburghPC_teleport', 'oreburgh', False],
    'oreburghPC_teleport': ['oreburgh_teleport', 'oreburghPC', False],
    'oreburgh_bikeToOreburghBikeTunnel': ['oreburghBikeTunnel_walkToOreburgh', 'oreburgh', False],

    # Wayward Cave Outside
    'waywardCave_ent': ['', 'waywardCave', True],
    'waywardCave_hiddenEnt': ['', 'waywardCave', True],
    # Wayward Cave Hidden Doors
    'waywardCave_cutToOreburghBikeTunnel': ['oreburghBikeTunnel_cutToWaywardCave', 'waywardCave', False],

    # Oreburgh Bike Tunnel (tiny sliver of land above oreburgh that you need a bike to get to)
    'oreburghBikeTunnel_cave': ['', 'oreburghBikeTunnel', True],
    'oreburghBikeTunnel_ent': ['', 'oreburghBikeTunnel', True],
    # Oreburgh Bike Tunnel Hidden Doors
    'oreburghBikeTunnel_cutToWaywardCave': ['waywardCave_cutToOreburghBikeTunnel', 'oreburghBikeTunnel', False],
    'oreburghBikeTunnel_walkToOreburgh': ['oreburgh_bikeToOreburghBikeTunnel', 'oreburghBikeTunnel', True],

    # Floaroma
    'floaromaPC': ['', 'floaroma', True],
    'floaromaPM': ['', 'floaroma', True],
    'floaroma_flowerShop': ['', 'floaroma', True],
    'floaroma_bottomRightHouse': ['', 'floaroma', True],
    'floaroma_topLeftHouse': ['', 'floaroma', True],
    'floaroma_meadowEnt': ['', 'floaroma', True],
    'floaroma_caveBelow': ['', 'floaroma', True],
    'floaroma_windWorksEnt': ['', 'floaroma', False],
    # Floaroma PC
    'floaromaPC_exit': ['', 'floaromaPC', True],
    'floaromaPC_left': ['', 'floaromaPC', True],
    'floaromaPC_right': ['', 'floaromaPC', True],
    # Floaroma Teleports and Hidden Doors
    'floaroma_teleport': ['floaromaPC_teleport', 'floaroma', False],
    'floaromaPC_teleport': ['floaroma_teleport', 'floaromaPC', False],
    'floaroma_surfToRoute205': ['route205_surfToFloaroma', 'floaroma', False],
    'floaroma_walkToRoute205': ['route205_walkToFloaroma', 'floaroma', False],
    'floaroma_surfToFuegoIronWorks': ['fuegoIronWorks_surfToFloaroma', 'floaroma', False],
    'floaroma_surfToMeadowTopEnt': ['meadowTopEnt_surfToFloaroma', 'floaroma', False],

    # Route 205 (Floaroma Area the Galactic Goons are blocking)
    'route205_house': ['', 'route205', True],
    'route205_forestEnt': ['', 'route205', True],
    # Route 205 Hidden Doors
    'route205_surfToFloaroma': ['floaroma_surfToRoute205', 'route205', False],
    'route205_walkToFloaroma': ['floaroma_walkToRoute205', 'route205', True],
    'route205_surfToFuegoIronWorks': ['fuegoIronWorks_surfToRoute205', 'route205', False],
    'route205_walkToFuegoIronWorks': ['fuegoIronWorks_walkToRoute205', 'route205', False],
    'route205_surfToMeadowTopEnt': ['meadowTopEnt_surfToRoute205', 'route205', False],
    'route205_cutToEterna': ['eterna_cutToRoute205', 'route205', False],

    # Fuego Iron Works
    'fuegoIronWorks_ent': ['', 'fuegoIronWorks', True],
    # Fuego Iron Works Hidden Doors
    'fuegoIronWorks_surfToFloaroma': ['floaroma_surfToFuegoIronWorks', 'fuegoIronWorks', False],
    'fuegoIronWorks_surfToRoute205': ['route205_surfToFuegoIronWorks', 'fuegoIronWorks', False],
    'fuegoIronWorks_walkToRoute205': ['route205_walkToFuegoIronWorks', 'fuegoIronWorks', True],
    'fuegoIronWorks_surfToMeadowTopEnt': ['meadowTopEnt_surfToFuegoIronWorks', 'fuegoIronWorks', False],

    # Entrance to Floaroma meadow just south of fuego Iron works
    'meadowTopEnt': ['', 'meadowTopEnt', True],
    # Entrance to Floaroma meadow hidden doors
    'meadowTopEnt_surfToFloaroma': ['floaroma_surfToMeadowTopEnt', 'meadowTopEnt', False],
    'meadowTopEnt_surfToRoute205': ['route205_surfToMeadowTopEnt', 'meadowTopEnt', False],
    'meadowTopEnt_surfToFuegoIronWorks': ['fuegoIronWorks_surfToMeadowTopEnt', 'meadowTopEnt', False],

    # Eterna
    'eternaPC': ['', 'eterna', True],
    'eternaPM': ['', 'eterna', True],
    'eterna_bikeShop': ['', 'eterna', True],
    'eterna_gym': ['', 'eterna', True],
    'eterna_condos': ['', 'eterna', True],
    'eterna_tunnel': ['', 'eterna', True],
    'eterna_houseByGym': ['', 'eterna', True],
    'eterna_houseByPC': ['', 'eterna', True],
    'eterna_forestEnt': ['', 'eterna', True],
    'eterna_houseByGalacticBase': ['', 'eterna', True],
    'eterna_houseUnderStatue': ['', 'eterna', True],
    'eterna_cave': ['', 'eterna', True],
    # Eterna PC
    'eternaPC_exit': ['', 'eternaPC', True],
    'eternaPC_left': ['', 'eternaPC', True],
    'eternaPC_right': ['', 'eternaPC', True],
    # Eterna Teleports and Hidden Doors
    'eterna_teleport': ['eternaPC_teleport', 'eterna', False],
    'eternaPC_teleport': ['eterna_teleport', 'eternaPC', False],
    'eterna_cutToRoute205': ['route205_cutToEterna', 'eterna', False],
    'eterna_cutToEternaGalactic': ['eternaGalactic_cutToEterna', 'eterna', False],

    # Galactic Base in Eterna
    'eternaGalacticEnt': ['', 'eternaGalactic', True],
    # Galactic Base in Eterna Hidden Doors
    'eternaGalactic_cutToEterna': ['eterna_cutToEternaGalactic', 'eternaGalactic', False],

    # Route 208
    'route208_house': ['', 'route208', True],
    'route208_tunnel': ['', 'route208', True],
    'route208_cave': ['', 'route208', True],

    # Hearthome
    'hearthomePC': ['', 'hearthome', True],
    'hearthomePM': ['', 'hearthome', True],
    'hearthome_church': ['', 'hearthome', True],
    'hearthome_redRoof': ['', 'hearthome', True],
    'hearthome_houseByRedRoof': ['', 'hearthome', True],
    'hearthome_contestHall': ['', 'hearthome', True],
    'hearthome_houseByPC': ['', 'hearthome', True],
    'hearthome_houseByPM': ['', 'hearthome', True],
    'hearthome_leftTunnel': ['', 'hearthome', True],
    'hearthome_rightTunnel': ['', 'hearthome', False],
    'hearthome_houseByGym': ['', 'hearthome', True],
    'hearthome_gym': ['', 'hearthome', False],
    'hearthome_amityRight': ['', 'hearthome', True],
    'hearthome_amityLeft': ['', 'hearthome', True],
    'hearthome_bottomLeftTunnel': ['', 'hearthome', True],
    # Hearthome PC
    'hearthomePC_exit': ['', 'hearthomePC', True],
    'hearthomePC_left': ['', 'hearthomePC', True],
    'hearthomePC_right': ['', 'hearthomePC', True],
    # Hearthome Teleports and Hidden Doors
    'hearthome_teleport': ['hearthomePC_teleport', 'hearthome', False],
    'hearthomePC_teleport': ['hearthome_teleport', 'hearthomePC', False],

    # Solaceon
    'solaceonPC': ['', 'solaceon', True],
    'solaceonPM': ['', 'solaceon', True],
    'solaceon_houseByPC': ['', 'solaceon', True],
    'solaceon_houseAbovePC': ['', 'solaceon', True],
    'solaceon_firstBumpHouse': ['', 'solaceon', True],
    'solaceon_secondBumpHouse': ['', 'solaceon', True],
    'solaceon_ruinsEnt': ['', 'solaceon', True],
    'solaceon_daycare': ['', 'solaceon', True],
    'solaceon_psyduckHouse': ['', 'solaceon', True],
    'solaceon_rainTunnel': ['', 'solaceon', True],
    'solaceon_tower': ['', 'solaceon', True],
    'solaceon_tunnel': ['', 'solaceon', True],
    # Solaceon PC
    'solaceonPC_exit': ['', 'solaceonPC', True],
    'solaceonPC_left': ['', 'solaceonPC', True],
    'solaceonPC_right': ['', 'solaceonPC', True],
    # Solaceon Teleports and Hidden Doors
    'solaceon_teleport': ['solaceonPC_teleport', 'solaceon', False],
    'solaceonPC_teleport': ['solaceon_teleport', 'solaceonPC', False],
    'solaceon_walkToCelestic': ['celestic_walkToSolaceon', 'solaceon', False],

    # Celestic
    'celesticPC': ['', 'celestic', True],
    'celestic_bottomLeftHouse': ['', 'celestic', True],
    'celestic_topRightHouse': ['', 'celestic', True],
    'celestic_centerHouse': ['', 'celestic', True],
    'celestic_topLeftHouse': ['', 'celestic', True],
    'celestic_ruins': ['', 'celestic', True],
    'celestic_cave': ['', 'celestic', True],
    # Celesetic PC
    'celesticPC_exit': ['', 'celesticPC', True],
    'celesticPC_left': ['', 'celesticPC', True],
    'celesticPC_right': ['', 'celesticPC', True],
    # Celestic Teleports and Hidden Doors
    'celestic_teleport': ['celesticPC_teleport', 'celestic', False],
    'celesticPC_teleport': ['celestic_teleport', 'celesticPC', False],
    'celestic_walkToSolaceon': ['solaceon_walkToCelestic', 'celestic', False],
    'celestic_rockClimbToFoggyCelestic': ['foggyCelestic_rockClimbToCelestic', 'celestic', False],
    'celestic_walkToFoggyCelestic': ['foggyCelestic_walkToCelestic', 'celestic', False],

    # Foggy Celestic (Draco Meteor House)
    'foggyCelesticHouse': ['', 'foggyCelestic', True],
    # Foggy Celestic Hidden Doors
    'foggyCelestic_rockClimbToCelestic': ['celestic_rockClimbToFoggyCelestic', 'foggyCelestic', False],
    'foggyCelestic_walkToCelestic': ['celestic_walkToFoggyCelestic', 'foggyCelestic', True],

    # Veilstone
    'veilstonePC': ['', 'veilstone', True],
    'veilstone_gym': ['', 'veilstone', True],
    'veilstone_casino': ['', 'veilstone', True],
    'veilstone_mall': ['', 'veilstone', True],
    'veilstone_leftTunnel': ['', 'veilstone', True],
    'veilstone_bottomTunnel': ['', 'veilstone', True],
    'veilstone_galacticCenter': ['', 'veilstone', True],
    'veilstone_galacticLeft': ['', 'veilstone', True],
    'veilstone_galacticRight': ['', 'veilstone', True],
    'veilstone_topLeftHouse': ['', 'veilstone', True],
    'veilstone_houseAbovePCLeft': ['', 'veilstone', True],
    'veilstone_houseAbovePCRight': ['', 'veilstone', True],
    'veilstone_houseByCasino': ['', 'veilstone', True],
    'veilstone_bottomLeftHouseLeft': ['', 'veilstone', True],
    'veilstone_bottomLeftHouseRight': ['', 'veilstone', True],
    # Veilstone PC
    'veilstonePC_exit': ['', 'veilstonePC', True],
    'veilstonePC_left': ['', 'veilstonePC', True],
    'veilstonePC_right': ['', 'veilstonePC', True],
    # Veilstone Teleports and Hidden Doors
    'veilstone_teleport': ['veilstonePC_teleport', 'veilstone', False],
    'veilstonePC_teleport': ['veilstone_teleport', 'veilstonePC', False],

    # Valor Villas
    'valorVillas_topRightHouse': ['', 'valorVillas', True],
    'valorVillas_topHouse': ['', 'valorVillas', True],
    'valorVillas_bottomHouse': ['', 'valorVillas', True],
    'valorVillas_bottomRightHouse': ['', 'valorVillas', True],
    'valorVillas_bottomLeftHouse': ['', 'valorVillas', True],
    'valorVillas_topLeftHouse': ['', 'valorVillas', True],
    'valorVillas_leftBeachHouse': ['', 'valorVillas', True],
    'valorVillas_rightBeachHouse': ['', 'valorVillas', True],
    'valorVillas_rightTunnel': ['', 'valorVillas', True],
    'valorVillas_lakeEnt': ['', 'valorVillas', True],
    'valorVillas_cave': ['', 'valorVillas', True],
    'valorVillas_topTunnel': ['', 'valorVillas', True],
    # !!! THE ENTRANCE TO SENDOFF SPRING HAS BEEN OMITTED BECAUSE THE PATH TO IT DOES NOT !!!
    # !!! OPEN UP UNTIL THE PLAYER HAS ENTERED THE HALL OF FAME !!!
    # Valor Villas Hidden Doors
    'valorVillas_rockClimbToValorVillasRockClimbHouse': ['valorVillasRockClimbHouse_rockClimbToValorVillas', 'valorVillas', False],

    # Valor Villas Rock Climb House
    'valorVillasRockClimbHouse': ['', 'valorVillasRockClimbHouse', True],
    # Valor Villas Rock Climb House Hidden Doors
    'valorVillasRockClimbHouse_rockClimbToValorVillas': ['valorVillas_rockClimbToValorVillasRockClimbHouse', 'valorVillasRockClimbHouse', False],
    'valorVillasRockClimbHouse_rockClimbAndSurfToRoute213': ['route213_surfAndRockClimbToValorVillasRockClimbHouse', 'valorVillasRockClimbHouse', False],

    # Sunnyshore
    'sunnyshorePC': ['', 'sunnyshore', True],
    'sunnyshorePM': ['', 'sunnyshore', True],
    'sunnyshore_houseByPM': ['', 'sunnyshore', True],
    'sunnyshore_topRightRightHouse': ['', 'sunnyshore', True],
    'sunnyshore_topRightLeftHouse': ['', 'sunnyshore', True],
    'sunnyshore_tunnel': ['', 'sunnyshore', True],
    'sunnyshore_gym': ['', 'sunnyshore', False],
    'sunnyshore_market': ['', 'sunnyshore', True],
    'sunnyshore_lighthouse': ['', 'sunnyshore', True],
    # Sunnyshore PC
    'sunnyshorePC_exit': ['', 'sunnyshorePC', True],
    'sunnyshorePC_left': ['', 'sunnyshorePC', True],
    'sunnyshorePC_right': ['', 'sunnyshorePC', True],
    # Sunnyshore Teleports and Hidden Doors
    'sunnyshore_teleport': ['sunnyshorePC_teleport', 'sunnyshore', False],
    'sunnyshorePC_teleport': ['sunnyshore_teleport', 'sunnyshorePC', False],
    'sunnyshore_rockClimbToSunnyshoreRockClimbHouse': ['sunnyshoreRockClimbHouse_rockClimbToSunnyshore', 'sunnyshore', False],
    'sunnyshore_surfAndWaterfallToVictoryRoadEnt': ['victoryRoadEnt_surfAndWaterfallToSunnyshore', 'sunnyshore', False],

    # Sunnyshore Rock Climb House
    'sunnyshoreRockClimbHouse': ['', 'sunnyshoreRockClimbHouse', True],
    # Sunnyshore Rock Climb House Hidden Doors
    'sunnyshoreRockClimbHouse_rockClimbToSunnyshore': ['sunnyshore_rockClimbToSunnyshoreRockClimbHouse', 'sunnyshoreRockClimbHouse', False],

    # Victory Road Entrance
    'victoryRoadEntPC': ['', 'victoryRoadEnt', True],
    'victoryRoadEnt_cave': ['', 'victoryRoadEnt', True],
    # Victory Road Entrance PC
    'victoryRoadEntPC_exit': ['', 'victoryRoadEntPC', True],
    'victoryRoadEntPC_left': ['', 'victoryRoadEntPC', True],
    'victoryRoadEntPC_right': ['', 'victoryRoadEntPC', True],
    # Victory Road Entrance Teleports and Hidden Doors
    'victoryRoadEnt_teleport': ['victoryRoadEntPC_teleport', 'victoryRoadEnt', False],
    'victoryRoadEntPC_teleport': ['victoryRoadEnt_teleport', 'victoryRoadEntPC', False],
    'victoryRoadEnt_surfAndWaterfallToSunnyshore': ['sunnyshore_surfAndWaterfallToVictoryRoadEnt', 'victoryRoadEnt', False],

    # Pokemon League
    'league_ent': ['', 'league', True],
    # Pokemon League PC
    'leaguePC_exit': ['', 'leaguePC', True],
    'leaguePC_left': ['', 'leaguePC', True],
    'leaguePC_right': ['', 'leaguePC', True],
    # Pokemon League Teleports and Hidden Doors
    'league_teleport': ['leaguePC_teleport', 'league', False],
    'leaguePC_teleport': ['league_teleport', 'leaguePC', False],
    'league_surfAndWaterfallToLeagueCave': ['leagueCave_surfAndWaterfallToLeague', 'league', False],

    # Pokemon League Cave (Victory road's other entrance)
    'leagueCave': ['', 'leagueCave', True],
    # Pokemon League Cave Hidden Doors
    'leagueCave_surfAndWaterfallToLeague': ['league_surfAndWaterfallToLeagueCave', 'leagueCave', False],

    # Route 213
    'route213_house': ['', 'route213', True],
    'route213_valorVillasEnt': ['', 'route213', True],
    'route213_tunnel': ['', 'route213', True],
    # Route 213 Hidden Doors
    'route213_surfAndRockClimbToValorVillasRockClimbHouse': ['valorVillasRockClimbHouse_rockClimbAndSurfToRoute213', 'route213', False],

    # Pastoria
    'pastoriaPC': ['', 'pastoria', True],
    'pastoriaPM': ['', 'pastoria', True],
    'pastoria_gym': ['', 'pastoria', True],
    'pastoria_houseByPC': ['', 'pastoria', True],
    'pastoria_tunnel': ['', 'pastoria', True],
    'pastoria_houseByTunnel': ['', 'pastoria', True],
    'pastoria_houseByHarbor': ['', 'pastoria', True],
    'pastoria_houseAbovePM': ['', 'pastoria', True],
    'pastoria_houseLeftOfPM': ['', 'pastoria', True],
    'pastoria_marshHouse': ['', 'pastoria', True],
    'pastoria_mansion': ['', 'pastoria', True],
    'pastoria_mansionTunnel': ['', 'pastoria', True],
    # Pastoria PC
    'pastoriaPC_exit': ['', 'pastoriaPC', True],
    'pastoriaPC_left': ['', 'pastoriaPC', True],
    'pastoriaPC_right': ['', 'pastoriaPC', True],
    # Pastoria Teleports and Hidden Doors
    'pastoria_teleport': ['pastoriaPC_teleport', 'pastoria', False],
    'pastoriaPC_teleport': ['pastoria_teleport', 'pastoriaPC', False],

    # Route 218 Right
    'route218Right': ['', 'route218Right', True],
    # Route 218 Right Hidden Doors
    'route218Right_surfToRoute218Left': ['route218Left_surfToRoute218Right', 'route218Right', False],

    # Route 218 Left
    'route218Left': ['', 'route218Left', True],
    # Route 218 Left Hidden Doors
    'route218Left_surfToRoute218Right': ['route218Right_surfToRoute218Left', 'route218Left', False],

    # Canalave
    'canalavePC': ['', 'canalave', True],
    'canalavePM': ['', 'canalave', True],
    'canalave_lockedDoorHouse': ['', 'canalave', False],
    'canalave_houseAbovePM': ['', 'canalave', True],
    'canalave_houseBelowPM': ['', 'canalave', True],
    'canalave_tunnel': ['', 'canalave', True],
    'canalave_gym': ['', 'canalave', True],
    'canalave_library': ['', 'canalave', True],
    'canalave_houseBelowGym': ['', 'canalave', True],
    'canalave_houseByBoat': ['', 'canalave', True],
    'canalave_ironIslandHouse': ['', 'canalave', True],
    'canalave_ironIslandCave': ['', 'canalave', True],
    # Canalave PC
    'canalavePC_exit': ['', 'canalavePC', True],
    'canalavePC_left': ['', 'canalavePC', True],
    'canalavePC_right': ['', 'canalavePC', True],
    # Canalave Teleports and Hidden Doors
    'canalave_teleport': ['canalavePC_teleport', 'canalave', False],
    'canalavePC_teleport': ['canalave_teleport', 'canalavePC', False],
    'canalave_walkToIronIslandCaveExit': ['ironIslandCaveExit_walkToCanalave', 'canalave', False],
    'canalave_boatToNewMoonIsland': ['newMoonIsland_boatToCanalave', 'canalave', False],
    'canalave_boatToFullMoonIsland': ['fullMoonIsland_boatToCanalave', 'canalave', False],

    # Iron Island Cave Exit
    'ironIslandCaveExit': ['', 'ironIslandCaveExit', True],
    # Iron Island Cave Exit Hidden Doors
    'ironIslandCaveExit_walkToCanalave': ['canalave_walkToIronIslandCaveExit', 'ironIslandCaveExit', True],

    # Snowpoint
    'snowpointPC': ['', 'snowpoint', True],
    'snowpointPM': ['', 'snowpoint', True],
    'snowpoint_gym': ['', 'snowpoint', True],
    'snowpoint_temple': ['', 'snowpoint', True],
    'snowpoint_topRightHouse': ['', 'snowpoint', True],
    'snowpoint_topLeftHouse': ['', 'snowpoint', True],
    'snowpoint_snowRouteTopHouse': ['', 'snowpoint', True],
    'snowpoint_snowRouteMiddleHouse': ['', 'snowpoint', True],
    'snowpoint_snowRouteBottomHouse': ['', 'snowpoint', True],
    'snowpoint_snowRouteCave': ['', 'snowpoint', True],
    # Snowpoint PC
    'snowpointPC_exit': ['', 'snowpointPC', True],
    'snowpointPC_left': ['', 'snowpointPC', True],
    'snowpointPC_right': ['', 'snowpointPC', True],
    # Snowpoint Teleports and Hidden Doors
    'snowpoint_teleport': ['snowpointPC_teleport', 'snowpoint', False],
    'snowpointPC_teleport': ['snowpoint_teleport', 'snowpointPC', False],
    'snowpoint_rockClimbToLakeAcuityEnt': ['lakeAcuityEnt_rockClimbToSnowpoint', 'snowpoint', False],
    'snowpoint_boatToFight': ['fight_boatToSnowpoint', 'snowpoint', False],

    # Lake Acuity Entrance
    'lakeAcuityEnt': ['', 'lakeAcuityEnt', True],
    # Lake Acuity Hidden Doors
    'lakeAcuityEnt_rockClimbToSnowpoint': ['snowpoint_rockClimbToLakeAcuityEnt', 'lakeAcuityEnt', False],

    # Fight Area
    'fightPC': ['', 'fight', True],
    'fightPM': ['', 'fight', True],
    'fight_bottomMostHouse': ['', 'fight', True],
    'fight_bottomHouse': ['', 'fight', True],
    'fight_tunnel': ['', 'fight', True],
    'fight_battleArena': ['', 'fight', True],
    # Fight Area PC
    'fightPC_exit': ['', 'fightPC', True],
    'fightPC_left': ['', 'fightPC', True],
    'fightPC_right': ['', 'fightPC', True],
    # Fight Area Teleports and Hidden Doors
    'fight_teleport': ['fightPC_teleport', 'fight', False],
    'fightPC_teleport': ['fight_teleport', 'fight', False],
    'fight_boatToSnowpoint': ['snowpoint_boatToFight', 'fight', True],
    'fight_surfToResort': ['resort_surfToFight', 'fight', False],

    # Resort
    'resortPC': ['', 'resort', True],
    'resort_villa': ['', 'resort', True],
    'resort_ribbonHall': ['', 'resort', True],
    'resort_houseByRibbonHall': ['', 'resort', True],
    'resort_houseInSandstorm': ['', 'resort', True],
    'resort_tunnel': ['', 'resort', True],
    # Resort PC
    'resortPC_exit': ['', 'resortPC', True],
    'resortPC_left': ['', 'resortPC', True],
    'resortPC_right': ['', 'resortPC', True],
    # Resort Teleports and Hidden Doors
    'resort_teleport': ['resortPC_teleport', 'resort', False],
    'resortPC_teleport': ['resort_teleport', 'resortPC', False],
    'resort_surfToFight': ['fight_surfToResort', 'resort', False],
    'resort_bikeToResortBikeHouse': ['resortBikeHouse_walkToResort', 'resort', False],
    'resort_walkToResortBikeCave': ['resortBikeCave_bikeToResort', 'resort', True],

    # Resort Bike House
    'resortBikeHouse': ['', 'resortBikeHouse', True],
    # Resort Bike House Hidden Doors
    'resortBikeHouse_walkToResort': ['resort_bikeToResortBikeHouse', 'resortBikeHouse', True],

    # Resort Bike Cave
    'resortBikeCave': ['', 'resortBikeCave', True],
    # Resort Bike Cave Hidden Doors
    'resortBikeCave_bikeToResort': ['resort_walkToResortBikeCave', 'resortBikeCave', False],

    # Survival
    'survivalPC': ['', 'survival', True],
    'survivalPM': ['', 'survival', True],
    'survival_lockedHouse': ['', 'survival', False],
    'survival_bottomHouse': ['', 'survival', True],
    'survival_leftRouteHouse': ['', 'survival', True],
    'survival_tunnel': ['', 'survival', True],
    # Survival PC
    'survivalPC_exit': ['', 'survivalPC', True],
    'survivalPC_left': ['', 'survivalPC', True],
    'survivalPC_right': ['', 'survivalPC', True],
    # Survival Teleports and Hidden Doors
    'survival_teleport': ['survivalPC_teleport', 'survival', False],
    'survivalPC_teleport': ['survival_teleport', 'survivalPC', False],
    'survival_rockClimbToSurvivalRockClimbHouse': ['survivalRockClimbHouse_rockClimbToSurvival', 'survival', False],
    'survival_rockClimbAndSurfToRoute226House': ['route226House_surfAndRockClimbToSurvival', 'survival', False],

    # Route 226 House (Surf House)
    'route226House': ['', 'route226House', True],
    # Route 226 House Hidden Doors
    'route226House_surfAndRockClimbToSurvival': ['survival_rockClimbAndSurfToRoute226House', 'route226House', False],
    'route226House_surfToRoute227Tunnel': ['route227Tunnel_surfToRoute226House', 'route226House', False],

    # Route 227 House
    'route227House': ['', 'route227House', True],
    # Route 227 Hidden Doors
    'route227House_walkToRoute227Tunnel': ['route227Tunnel_bikeToRoute227House', 'route227House', True],
    'route227House_bikeToStarkCave': ['starkCave_bikeToRoute227House', 'route227House', False],

    # Stark Cave
    'starkCave': ['', 'starkCave', True],
    # Stark Cave Hidden Doors
    'starkCave_bikeToRoute227House': ['route227House_bikeToStarkCave', 'starkCave', False],

    # Route 227 Tunnel
    'route227Tunnel': ['', 'route227Tunnel', True],
    # Route 227 Tunnel Hidden Doors
    'route227Tunnel_surfToRoute226House': ['route226House_surfToRoute227Tunnel', 'route227Tunnel', False],
    'route227Tunnel_bikeToRoute227House': ['route227House_walkToRoute227Tunnel', 'route227Tunnel', False],

    # Survival Rock Climb House
    'survivalRockClimbHouse': ['', 'survivalRockClimbHouse', True],
    # Survival Rock Climb House Hidden Doors
    'survivalRockClimbHouse_rockClimbToSurvival': ['survival_rockClimbToSurvivalRockClimbHouse', 'survivalRockClimbHouse', False],

    # Eterna Forest
    'eternaForestEnt': ['', 'eternaForest', True],
    'eternaForestExit': ['', 'eternaForest', True],
    # Eterna Forest Hidden Doors
    'eternaForest_cutToOldChateauEnt': ['oldChateauEnt_cutToEternaForest', 'eternaForest', False],

    # Old Chateau Entrance
    'oldChateauEnt': ['', 'oldChateauEnt', True],
    # Old Chateau Entrance Hidden Doors
    'oldChateauEnt_cutToEternaForest': ['eternaForest_cutToOldChateauEnt', 'oldChateauEnt', False],

    # Bike Highway
    'bikeHighwayTop': ['', 'bikeHighway', True],
    'bikeHighwayBottom': ['', 'bikeHighway', True],

    # Deadend
    'deadend': [[], 'deadend', True],

    # Mall
    'mall_basement': ['', 'mall', True],
    'mall_1fLeft': ['', 'mall', True],
    'mall_1fRight': ['', 'mall', True],
    'mall_1fExit': ['', 'mall', True],
    'mall_2fLeft': ['', 'mall', True],
    'mall_2fRight': ['', 'mall', True],
    'mall_3fLeft': ['', 'mall', True],
    'mall_3fRight': ['', 'mall', True],
    'mall_4fLeft': ['', 'mall', True],
    'mall_4fRight': ['', 'mall', True],
    'mall_5f': ['', 'mall', True],

    # Old Chateau Hallway
    'oldChateauHallway_leftMost': ['', 'oldChateauHallway', True],
    'oldChateauHallway_secondLeftMost': ['', 'oldChateauHallway', True],
    'oldChateauHallway_center': ['', 'oldChateauHallway', True],
    'oldChateauHallway_rightMost': ['', 'oldChateauHallway', True],
    'oldChateauHallway_secondRightMost': ['', 'oldChateauHallway', True],
    'oldChateauHallway_exit': ['', 'oldChateauHallway', True],

    # Old Chateau Main
    'oldChateauMain_exit': ['', 'oldChateauMain', True],
    'oldChateauMain_right': ['', 'oldChateauMain', True],
    'oldChateauMain_left': ['', 'oldChateauMain', True],
    'oldChateauMain_topCenter': ['', 'oldChateauMain', True],
    'oldChateauMain_center': ['', 'oldChateauMain', True],

    # Mansion
    'mansion_exit': ['', 'mansion', True],
    'mansion_center': ['', 'mansion', True],
    'mansion_right': ['', 'mansion', True],
    'mansion_leftLeft': ['', 'mansion', True],
    'mansion_leftCenter': ['', 'mansion', True],
    'mansion_leftRight': ['', 'mansion', True],

    # Ravaged Path Top
    'ravagedPathTop': ['', 'ravagedPathTop', True],
    'ravagedPathTop_rockSmashToRavagedPathBottom': ['ravagedPathBottom_rockSmashToRavagedPathTop', 'ravagedPathTop', False],
    # Ravaged Path Bottom
    'ravagedPathBottom': ['', 'ravagedPathBottom', True],
    'ravagedPathBottom_rockSmashToRavagedPathTop': ['ravagedPathTop_rockSmashToRavagedPathBottom', 'ravagedPathBottom', False],

    # Jubilife TV
    'jubilifeTV_4fStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_3fLeftDoor': ['', 'jubilifeTV', True],
    'jubilifeTV_3fRightDoor': ['', 'jubilifeTV', True],
    'jubilifeTV_3fLeftStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_3fRightStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_2fDoor': ['', 'jubilifeTV', True],
    'jubilifeTV_2fLeftStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_2fRightStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_1fStairs': ['', 'jubilifeTV', True],
    'jubilifeTV_exit': ['', 'jubilifeTV', True],

    # Mt. Coronet
    # Gemini Stairs
    'MC_geminiStairsLeft': ['', 'MC_geminiStairs', True],
    'MC_geminiStairsRight': ['', 'MC_geminiStairs', True],
    'MC_geminiStairsCave': ['', 'MC_geminiStairs', True],

    # South Summit Main
    'MC_southSummitMainLeft': ['', 'MC_southSummitMain', True],
    'MC_southSummitMainRight': ['', 'MC_southSummitMain', True],
    # South Summit Main Hidden Doors
    'MC_southSummitMain_rockClimbToMC_southSummitBottomCave': ['MC_southSummitBottomCave_rockClimbToMC_southSummitMain', 'MC_southSummitMain', False],

    # South Summit Bottom Cave
    'MC_southSummitBottomCave': ['', 'MC_southSummitBottomCave', True],
    # South Summit Bottom Cave Hidden Doors
    'MC_southSummitBottomCave_rockClimbToMC_southSummitMain': ['MC_southSummitMain_rockClimbToMC_southSummitBottomCave', 'MC_southSummitBottomCave', False],

    # North Summit Pit Area
    'MC_northSummitPitArea_pitCave': ['', 'MC_northSummitPitArea', True],
    'MC_northSummitPitArea_upperCave': ['', 'MC_northSummitPitArea', True],
    # North Summit Pit Area Hidden Doors
    'MC_northSummitPitArea_rockClimbToMC_northSummitTopCave': ['MC_northSummitTopCave_rockClimbToMC_northSummitPitArea', 'MC_northSummitPitArea', False],

    # North Summit Top Cave
    'MC_northSummitTopCave': ['', 'MC_northSummitTopCave', True],
    # North Summit Top Cave Hidden Doors
    'MC_northSummitTopCave_rockClimbToMC_northSummitPitArea': ['MC_northSummitPitArea_rockClimbToMC_northSummitTopCave', 'MC_northSummitTopCave', False],

    # Two Cave One Stair
    'MC_twoCaveOneStair_stair': ['', 'MC_twoCaveOneStair', True],
    'MC_twoCaveOneStair_cave': ['', 'MC_twoCaveOneStair', True],
    'MC_twoCaveOneStair_exit': ['', 'MC_twoCaveOneStair', True],

    # Many Ponds
    'MC_manyPondsLeft': ['', 'MC_manyPonds', True],
    'MC_manyPondsRight': ['', 'MC_manyPonds', True],
    # Many Ponds Hidden Doors
    'MC_manyPonds_surfAndRockClimbToMC_manyPondsRCStairs': ['MC_manyPondsRCStairs_rockClimbToMC_manyPonds', 'MC_manyPonds', False],

    # Many Ponds Rock Climb Stairs
    'MC_manyPondsRCStairs': ['', 'MC_manyPondsRCStairs', True],
    # Many Ponds Rock Climb Stairs Hidden Doors
    'MC_manyPondsRCStairs_rockClimbToMC_manyPonds': ['MC_manyPonds_surfAndRockClimbToMC_manyPondsRCStairs', 'MC_manyPondsRCStairs', False],

    # Bridges
    'MC_bridgesNorth': ['', 'MC_bridges', True],
    'MC_bridgesSouth': ['', 'MC_bridges', True],
    # Bridges Hidden Doors
    'MC_bridges_walkToMC_bridgesStairs': ['MC_bridgesStairs_strengthToMC_bridges', 'MC_bridges', True],

    # Bridges South
    'MC_bridgesStairs': ['', 'MC_bridgesStairs', True],
    # Bridges South Hidden Doors
    'MC_bridgesStairs_strengthToMC_bridges': ['MC_bridges_walkToMC_bridgesStairs', 'MC_bridgesStairs', False],

    # Rock Climb Cave North
    'MC_rockClimbCaveNorth': ['', 'MC_rockClimbCaveNorth', True],
    # Rock Climb Cave North Hidden Doors
    'MC_rockClimbCaveNorth_rockClimbToMC_rockClimbCaveSouth': ['MC_rockClimbCaveSouth_rockClimbToMC_rockClimbCaveNorth', 'MC_rockClimbCaveNorth', False],

    # Rock Climb Cave South
    'MC_rockClimbCaveSouth': ['', 'MC_rockClimbCaveSouth', True],
    # Rock Climb Cave South Hidden Doors
    'MC_rockClimbCaveSouth_rockClimbToMC_rockClimbCaveNorth': ['MC_rockClimbCaveNorth_rockClimbToMC_rockClimbCaveSouth', 'MC_rockClimbCaveSouth', False],

    # Waterfall Cave South
    'MC_waterfall_northWFCave': ['', 'MC_waterfall_northWFCave', True],
    'MC_waterfall_southWFCave': ['', 'MC_waterfall_southWFCave', True],
    # Waterfall Cave South Hidden Doors
    'MC_waterfall_northWFCave_surfAndWaterfallToMC_waterfall_southWFCave': ['MC_waterfall_southWFCave_surfAndWaterfallToMC_waterfall_northWFCave', 'MC_waterfall_northWFCave', False],
    'MC_waterfall_southWFCave_surfAndWaterfallToMC_waterfall_northWFCave': ['MC_waterfall_northWFCave_surfAndWaterfallToMC_waterfall_southWFCave', 'MC_waterfall_southWFCave', False],

    # Waterfall Cave Rock Climb Part
    'MC_waterfall_rockClimbRight': ['', 'MC_waterfall_rockClimbRight', True],
    'MC_waterfall_rockClimbLeft': ['', 'MC_waterfall_rockClimbLeft', True],
    # Waterfall Cave Rock Climb Hidden Doors
    'MC_waterfall_rockClimbRight_rockClimbToMC_waterfall_rockClimbLeft': ['MC_waterfall_rockClimbLeft_rockClimbToMC_waterfall_rockClimbRight', 'MC_waterfall_rockClimbRight', False],
    'MC_waterfall_rockClimbLeft_rockClimbToMC_waterfall_rockClimbRight': ['MC_waterfall_rockClimbRight_rockClimbToMC_waterfall_rockClimbLeft', 'MC_waterfall_rockClimbLeft', False],

    # Strength Cave
    'MC_strengthRight': ['', 'MC_strengthRight', True],
    'MC_strengthLeft': ['', 'MC_strengthLeft', True],
    'MC_strengthUpper': ['', 'MC_strengthUpper', True],
    'MC_strengthBottom': ['', 'MC_strengthBottom', True],
    # Strength Cave Hidden Doors
    'MC_strengthLeft_rockSmashAndStrengthToMC_strengthRight': ['MC_strengthRight_strengthAndRockSmashToMC_strengthLeft', 'MC_strengthLeft', False],
    'MC_strengthRight_strengthAndRockSmashToMC_strengthLeft': ['MC_strengthLeft_rockSmashAndStrengthToMC_strengthRight', 'MC_strengthRight', False],
    'MC_strengthBottom_strengthToMC_strengthRight': ['MC_strengthRight_strengthToMC_strengthBottom', 'MC_strengthBottom', False],
    # This door will always be False (The strength boulder moves into the wall.)
    'MC_strengthRight_strengthToMC_strengthBottom': ['MC_strengthBottom_strengthToMC_strengthRight', 'MC_strengthRight', False],
    'MC_strengthRight_strengthToMC_strengthUpper': ['MC_strengthUpper_strengthToMC_strengthRight', 'MC_strengthRight', False],
    'MC_strengthUpper_strengthToMC_strengthRight': ['MC_strengthRight_strengthToMC_strengthUpper', 'MC_strengthUpper', False],

    # Wayward Cave
    'waywardRight': ['', 'waywardRight', True],
    'waywardLeft': ['', 'waywardLeft', True],
    # Wayward Hidden Doors
    'waywardRight_walkToWaywardLeft': ['waywardLeft_bikeToWaywardRight', 'waywardRight', True],
    'waywardLeft_bikeToWaywardRight': ['waywardRight_walkToWaywardLeft', 'waywardLeft', False],

    # The Lakes
    'lakeAcuity': ['', 'lakeAcuity', True],
    'lakeAcuityCaveEnt': ['', 'lakeAcuityCaveEnt', True],
    'lakeValor': ['', 'lakeValor', True],
    'lakeValorCaveEnt': ['', 'lakeValorCaveEnt', True],
    'lakeVerity': ['', 'lakeVerity', True],
    'lakeVerityCaveEnt': ['', 'lakeVerityCaveEnt', True],
    # The Lakes Hidden Doors
    'lakeAcuity_surfToLakeAcuityCaveEnt': ['lakeAcuityCaveEnt_surfToLakeAcuity', 'lakeAcuity', False],
    'lakeAcuityCaveEnt_surfToLakeAcuity': ['lakeAcuity_surfToLakeAcuityCaveEnt', 'lakeAcuityCaveEnt', False],
    'lakeValor_surfToLakeValorCaveEnt': ['lakeValorCaveEnt_surfToLakeValor', 'lakeValor', False],
    'lakeValorCaveEnt_surfToLakeValor': ['lakeValor_surfToLakeValorCaveEnt', 'lakeValorCaveEnt', False],
    'lakeVerity_surfToLakeVerityCaveEnt': ['lakeVerityCaveEnt_surfToLakeVerity', 'lakeVerity', False],
    'lakeVerityCaveEnt_surfToLakeVerity': ['lakeVerity_surfToLakeVerityCaveEnt', 'lakeVerityCaveEnt', False],

    # Floaroma Meadow
    'floaromaMeadowNorth': ['', 'floaromaMeadowNorth', True],
    'floaromaMeadowSouth_house': ['', 'floaromaMeadowSouth', True],
    'floaromaMeadowSouth_exit': ['', 'floaromaMeadowSouth', True],
    # Floaroma Meadow Hidden Doors
    'floaromaMeadowNorth_walkToFloaromaMeadowSouth': ['floaromaMeadowSouth_walkToFloaromaMeadowNorth', 'floaromaMeadowNorth', True],
    'floaromaMeadowSouth_walkToFloaromaMeadowNorth': ['floaromaMeadowNorth_walkToFloaromaMeadowSouth', 'floaromaMeadowSouth', False],

    # Sendoff Spring
    'sendoffSpringCave': ['', 'sendoffSpringCave', False],
    'sendoffSpringExit': ['', 'sendoffSpringExit', True],
    # Sendoff Spring Hidden Doors
    'sendoffSpringCave_rockClimbToSendoffSpringExit': ['sendoffSpringExit_rockClimbToSendoffSpringCave', 'sendoffSpringCave', False],
    'sendoffSpringExit_rockClimbToSendoffSpringCave': ['sendoffSpringCave_rockClimbToSendoffSpringExit', 'sendoffSpringExit', False],

    # Iron Island Caves
    'ironIslandCaveEnt_exit': ['', 'ironIslandCaveEnt', True],
    'ironIslandCaveEnt_left': ['', 'ironIslandCaveEnt', True],
    'ironIslandCaveEnt_right': ['', 'ironIslandCaveEnt', True],
    'ironIslandCaveEsc_exitCave': ['', 'ironIslandCaveEsc', True],
    'ironIslandCaveEsc_topCave': ['', 'ironIslandCaveEsc', True],
    'ironIslandCaveEsc_bottomCave': ['', 'ironIslandCaveEsc', True],
    'ironIslandCaveStairs_bottomRight': ['', 'ironIslandCaveStairs', True],
    'ironIslandCaveStairs_bottomLeft': ['', 'ironIslandCaveStairs', True],
    'ironIslandCaveStairs_topLeft': ['', 'ironIslandCaveStairs', True],

    # Galactic Bases
    # Galactic Eterna Building
    'GEterna1f_exit': ['', 'GEterna1f', True],
    'GEterna1f_leftStairs': ['', 'GEterna1f', True],
    'GEterna1f_rightStairs': ['', 'GEterna1f', True],
    'GEterna1f_topLeftDoor': ['', 'GEterna1f', True],
    'GEternaCrates_left': ['', 'GEternaCrates', True],
    'GEternaCrates_center': ['', 'GEternaCrates', True],
    'GEternaCrates_right': ['', 'GEternaCrates', True],
    'GEternaTech_left': ['', 'GEternaTech', True],
    'GEternaTech_center': ['', 'GEternaTech', True],
    'GEternaTech_right': ['', 'GEternaTech', True],
    # Galactic Base Veilstone
    'GMasterBall_green': ['', 'GMasterBall', True],
    'GMasterBall_topRight': ['', 'GMasterBall', True],
    'GMasterBall_top': ['', 'GMasterBall', True],
    'GMasterBallEnt': ['', 'GMasterBallEnt', True],
    'GMasterBall_walkToGMasterBallEnt': ['GMasterBallEnt_walkToGMasterBall', 'GMasterBall', False],
    'GMasterBallEnt_walkToGMasterBall': ['GMasterBall_walkToGMasterBallEnt', 'GMasterBallEnt', False],
    'GWarehouseKey': ['', 'GWarehouseKey', True],
    'GWarehouse_right': ['', 'GWarehouse', True],
    'GWarehouse_left': ['', 'GWarehouse', True],
    'GWarehouse_walkToGWarehouseKey': ['GWarehouseKey_walkToGWarehouse', 'GWarehouse', False],
    'GWarehouseKey_walkToGWarehouse': ['GWarehouse_walkToGWarehouseKey', 'GWarehouseKey', True],
    'GConferenceRight': ['', 'GConferenceRight', True],
    'GConferenceLeft': ['', 'GConferenceLeft', True],
    'GConferenceRight_walkToGConferenceLeft': ['GConferenceLeft_walkToGConferenceRight', 'GConferenceRight', True],
    'GConferenceLeft_walkToGConferenceRight': ['GConferenceRight_walkToGConferenceLeft', 'GConferenceLeft', False],
    'GHQ1f_left': ['', 'GHQ1f', True],
    'GHQ1f_right': ['', 'GHQ1f', True],
    'GHQ1fStairs': ['', 'GHQ1fStairs', True],
    'GHQ1f_walkToGHQ1fStairs': ['GHQ1fStairs_walkToGHQ1f', 'GHQ1f', False],
    'GHQ1fStairs_walkToGHQ1f': ['GHQ1f_walkToGHQ1fStairs', 'GHQ1fStairs', False],
    'GHQtwoTeleporters_left': ['', 'GHQtwoTeleporters', True],
    'GHQtwoTeleporters_right': ['', 'GHQtwoTeleporters', True],
    'GHQtwoTeleporters_stairs': ['', 'GHQtwoTeleporters', True],
    'GHQtwoStairs_teleporter': ['', 'GHQtwoStairs', True],
    'GHQtwoStairs_left': ['', 'GHQtwoStairs', True],
    'GHQtwoStairs_right': ['', 'GHQtwoStairs', True],
    'GHQthreeTeleporters_left': ['', 'GHQthreeTeleporters', True],
    'GHQthreeTeleporters_center': ['', 'GHQthreeTeleporters', True],
    'GHQthreeTeleporters_right': ['', 'GHQthreeTeleporters', True],
    'GHQthreeTeleporters_stairs': ['', 'GHQthreeTeleporters', True],
    'GHQspreadTeleporters_topRight': ['', 'GHQspreadTeleporters', True],
    'GHQspreadTeleporters_bottomRight': ['', 'GHQspreadTeleporters', True],
    'GHQspreadTeleporters_stairs': ['', 'GHQspreadTeleporters', True],
    'GHQspreadTeleporters_room': ['', 'GHQspreadTeleporters', True],
    'GHQGreenTeleporter_green': ['', 'GHQGreenTeleporter', False],
    'GHQGreenTeleporter_exit': ['', 'GHQGreenTeleporter', True],

    # Solaceon Ruins
    'SREnt_ent': ['', 'SREnt', True],
    'SREnt_topRight': ['', 'SREnt', True],
    'SREnt_topLeft': ['', 'SREnt', True],
    'SREnt_bottomRight': ['', 'SREnt', True],
    'SRHiker_bottomLeft': ['', 'SRHiker', True],
    'SRHiker_bottomRight': ['', 'SRHiker', True],
    'SRHiker_topLeft': ['', 'SRHiker', True],
    'SRHiker_topRight': ['', 'SRHiker', True],
    'SRMan_bottomLeft': ['', 'SRMan', True],
    'SRMan_bottomRight': ['', 'SRMan', True],
    'SRMan_topLeft': ['', 'SRMan', True],
    'SRMan_topRight': ['', 'SRMan', True],
    'SRThreeStair_topLeft': ['', 'SRThreeStair', True],
    'SRThreeStair_bottomLeft': ['', 'SRThreeStair', True],
    'SRThreeStair_bottomRight': ['', 'SRThreeStair', True],
    'SRThreeDown_bottomLeft': ['', 'SRThreeDown', True],
    'SRThreeDown_bottomRight': ['', 'SRThreeDown', True],
    'SRThreeDown_topLeft': ['', 'SRThreeDown', True],
    'SRThreeDown_topRight': ['', 'SRThreeDown', True],
    'SRThreeUp_bottomLeft': ['', 'SRThreeUp', True],
    'SRThreeUp_bottomRight': ['', 'SRThreeUp', True],
    'SRThreeUp_topLeft': ['', 'SRThreeUp', True],
    'SRThreeUp_topRight': ['', 'SRThreeUp', True],

    # Bike Highway with the Girl
    'bikeHighwayGirlTop': ['', 'bikeHighwayGirlTop', True],
    'bikeHighwayGirlBottom': ['', 'bikeHighwayGirlBottom', True],
    'bikeHighwayGirlTop_walkToBikeHighwayGirlBottom': ['bikeHighwayGirlBottom_bikeToBikeHighwayGirlTop', 'bikeHighwayGirlTop', True],
    'bikeHighwayGirlBottom_bikeToBikeHighwayGirlTop': ['bikeHighwayGirlTop_walkToBikeHighwayGirlBottom', 'bikeHighwayGirlBottom', False],

    # Bike Highway (no girl)
    'bikeHighwayTopInside': ['', 'bikeHighwayTopInside', True],
    'bikeHighwayBottomInside': ['', 'bikeHighwayBottomInside', True],
    'bikeHighwayTopInside_bikeToBikeHighwayBottomInside': ['bikeHighwayBottomInside_walkToBikeHighwayTopInside', 'bikeHighwayTopInside', False],
    'bikeHighwayBottomInside_walkToBikeHighwayTopInside': ['bikeHighwayTopInside_bikeToBikeHighwayBottomInside', 'bikeHighwayBottomInside', True],

    # Rock Smash Cave
    'rockSmashCaveMainRight': ['', 'rockSmashCaveMain', True],
    'rockSmashCaveMainLeft': ['', 'rockSmashCaveMain', True],
    'rockSmashCaveUpper': ['', 'rockSmashCaveUpper', True],
    'rockSmashCaveMain_rockSmashToRockSmashCaveUpper': ['rockSmashCaveUpper_rockSmashToRockSmashCaveMain', 'rockSmashCaveMain', False],
    'rockSmashCaveUpper_rockSmashToRockSmashCaveMain': ['rockSmashCaveMain_rockSmashToRockSmashCaveUpper', 'rockSmashCaveUpper', False],

    # Victory Road


    # Important Deadends
    'arceus': ['', 'arceus', True],
    'spearPillar': ['', 'spearPillar', True],
    'bikeShop': ['', 'bikeShop', True],
    'bikeShopHostage': ['', 'bikeShopHostage', True],
    'windWorksHostage': ['', 'windWorksHostage', True],

    # NewMoon Island
    'newMoonIsland': ['', 'newMoonIsland', True],
    # NewMoon Island Hidden Doors
    'newMoonIsland_boatToCanalave': ['canalave_boatToNewMoonIsland', 'newMoonIsland', False],

    # FullMoon Island
    'fullMoonIsland': ['', 'fullMoonIsland', True],
    # FullMoon Island Hidden Doors
    'fullMoonIsland_boatToCanalave': ['canalave_boatToFullMoonIsland', 'fullMoonIsland', False]
}
