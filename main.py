"""
This is the main file.
It gives the menu the user interacts with, updates the matrix and more.
"""

# !/usr/bin/env python3
from regionDict import regionDict
from doorDict import doorDict
from Player import Player
from regionMatrix import regionMatrix


specialEvents = [
    'Obtained Bike',
    'Obtained Galactic Key',
    'Talk With Roark',
    'Obtained Wind Works Key',
    'Talked With Fantina',
    'Moved The Psyduck',
    'Talked With Volkner',
    'Cleared the Galactic Conference Hall',
    'Freed Windworks Guy',
    'Did Stark Mountain Cutscene'
]


# Complete
def printRegions():
    for region in regionDict:
        print(region)


# Complete
def printDoors():
    for door in doorDict:
        print(door)


# Complete
def printSpecificDoor():
    region = ''
    door = ''
    while region not in regionDict:
        region = input("What region is the door in? (Enter 'p' to see all regions)\n")
        if region == 'p':
            printRegions()
        if region == 'c':
            return

    print("Here are the doors in that region.")
    for d in doorDict:
        if doorDict[d][1] == region:
            print(d)

    while door not in doorDict:
        door = input("What door do you want to know about? (Enter 'c' to cancel)\n")
        if door == 'c':
            return

    print(f"Name: {door}, Destination: {doorDict[door][0]}, Region: {doorDict[door][1]}, Can You Re-enter the door: {doorDict[door][2]}")


# Complete
def printDoorsInRegion():
    region = ""
    while region not in regionDict:
        region = input("What is the name of the region you want to print the doors of? (Enter 'p' to see all regions)\n")
        if region == 'p':
            printRegions()
        if region == 'c':
            return

    for key, value in doorDict.items():
        if value[1] == region:
            print(key)


# Complete
def printDoorsInRegion2(region):
    for key, value in doorDict.items():
        if value[1] == region and value[0] == "":
            print(key)


# Complete
def listMenu():
    print("0: Change Name\n"
          "1: Change Gym Badges\n"
          "2: Change Acquired HMs (teleport included)\n"
          "3: Change A Special Event Status\n"
          "4: Add a Door's Destination\n"
          "5: Find a path\n"
          "6: Print Regions\n"
          "7: Print Doors\n"
          "8: Print Doors in a Specific Region\n"
          "9: List Unexplored Doors\n"
          "10: Print Stats on a Specific Door\n"
          "18: Quit\n")


# Complete
def addPath(door1, door2):
    addedPaths = 0
    # Check if doors are in different regions and they're re-enter-ability.
    if doorDict[door1][2] == False:
        return 0

    region1 = doorDict[door1][1]
    region2 = doorDict[door2][1]
    region1id = regionDict[region1]
    region2id = regionDict[region2]

    # !!! Make it so it only adds a path if it is shorter than the existing 3 paths.
    if region1 != region2:
        # Make a path from region1 to region2
        # Gets the length of each path from region1 to region2
        pathSizes = []
        for i in range(len(regionMatrix[region1id][region2id][2])):
            pathSizes.append([len(regionMatrix[region1id][region2id][2][i].split(' -> ')), i])

        # Makes the longest path the first element in pathSizes
        pathSizes.sort(key=lambda x: x[0], reverse=True)
        if len(pathSizes) > 0:
            if 2 < pathSizes[0][0]:
                if len(regionMatrix[region1id][region2id][2]) >= 3:
                    del regionMatrix[region1id][region2id][2][pathSizes[0][1]]

                regionMatrix[region1id][region2id][2].append(f"{door1} -> {door2}")
                addedPaths += 1

            elif len(regionMatrix[region1id][region2id][2]) < 3:
                regionMatrix[region1id][region2id][2].append(f"{door1} -> {door2}")
                addedPaths += 1

        else:
            regionMatrix[region1id][region2id][2].append(f"{door1} -> {door2}")
            addedPaths += 1

        # Quits early if it is a deadend
        if region1 == 'deadend' or region2 == 'deadend':
            doorDict[door1][0] = door2
            return 1

        # Get list1 (the regions that can get to region1 excluding region2 and region1)
        list1 = []
        for entries in regionMatrix:
            # Checks to see that at least one path exists AND we aren't currently on region1 AND we aren't currently on region2
            if len(entries[region1id][2]) > 0 and entries[0][0] != region1 and entries[0][0] != region2:
                list1.append(entries[region1id][0])

        # Get list2 (the regions that region2 can get to excluding region1)
        list2 = []
        for entry in regionMatrix[region2id]:
            if len(entry[2]) > 0 and entry[1] != region1 and entry[1] != region2:
                list2.append(entry[1])

        # Make a path from region1 to all regions in list2 where the path does not include region1
        for region in list2:
            if region == 'deadend':
                continue
            regionId = regionDict[region]
            for path in regionMatrix[region2id][regionId][2]:
                ickyPath = False
                doors = path.split(" -> ")
                for door in doors:
                    if doorDict[door][1] == region1:
                        ickyPath = True

                if ickyPath:
                    continue

                newPath = f"{door1} -> {door2} -> {path}"
                # Gets the length of each path from region1 to region
                pathSizes2 = []
                for i in range(len(regionMatrix[region1id][regionId][2])):
                    pathSizes2.append([len(regionMatrix[region1id][regionId][2][i].split(' -> ')), i])

                # Makes the longest path the first element in pathSizes2
                pathSizes2.sort(key=lambda x: x[0], reverse=True)
                if len(pathSizes2) > 0:
                    if len(newPath.split(' -> ')) < pathSizes2[0][0]:
                        if len(regionMatrix[region1id][regionId][2]) >= 3:
                            del regionMatrix[region1id][regionId][2][pathSizes2[0][1]]

                        regionMatrix[region1id][regionId][2].append(newPath)
                        addedPaths += 1

                    elif len(regionMatrix[region1id][regionId][2]) < 3:
                        regionMatrix[region1id][regionId][2].append(newPath)
                        addedPaths += 1

                else:
                    regionMatrix[region1id][regionId][2].append(newPath)
                    addedPaths += 1

        # Make paths from list1's regions to list2's regions
        # Loop through each region that can get to region 1
        for region in list1:
            if region == 'deadend':
                continue
            regionId = regionDict[region]
            # Loops through the paths from the region to region1
            for path in regionMatrix[regionId][region1id][2]:
                # If any door on the path is in the same region as door1 or door2, it should not make a new path.
                ickyPath = False
                doors = path.split(" -> ")
                for door in doors:
                    if doorDict[door][1] == region2:
                        ickyPath = True

                if ickyPath:
                    continue

                newPath2 = f"{path} -> {door1} -> {door2}"
                # Gets the length of each path from region to region2
                pathSizes3 = []
                for i in range(len(regionMatrix[regionId][region2id][2])):
                    pathSizes3.append([len(regionMatrix[regionId][region2id][2][i].split(' -> ')), i])

                # Makes the longest path the first element in pathSizes3
                pathSizes3.sort(key=lambda x: x[0], reverse=True)
                if len(pathSizes3) > 0:
                    if len(newPath2.split(' -> ')) < pathSizes3[0][0]:
                        if len(regionMatrix[regionId][region2id][2]) >= 3:
                            del regionMatrix[regionId][region2id][2][pathSizes3[0][1]]

                        regionMatrix[regionId][region2id][2].append(newPath2)
                        addedPaths += 1

                    elif len(regionMatrix[regionId][region2id][2]) < 3:
                        regionMatrix[regionId][region2id][2].append(newPath2)
                        addedPaths += 1

                else:
                    regionMatrix[regionId][region2id][2].append(newPath2)
                    addedPaths += 1

                # Loop through each region that region2 can get to.
                for r in list2:
                    if r == 'deadend':
                        continue
                    if region == r:
                        continue

                    rId = regionDict[r]

                    for path2 in regionMatrix[region2id][rId][2]:
                        # If any door on path1 shares a region with any door on path2 no path should be added.
                        ickyPath2 = False
                        doors2 = path2.split(" -> ")
                        for door in doors:
                            for d in doors2:
                                if doorDict[door][1] == doorDict[d][1]:
                                    ickyPath2 = True

                        if ickyPath2:
                            continue

                        newPath3 = f"{path} -> {door1} -> {door2} -> {path2}"
                        # Gets the length of each path from region to r
                        pathSizes4 = []
                        for i in range(len(regionMatrix[regionId][rId][2])):
                            pathSizes4.append([len(regionMatrix[regionId][rId][2][i].split(' -> ')), i])

                        # Makes the longest path the first element in pathSizes4
                        pathSizes4.sort(key=lambda x: x[0], reverse=True)
                        if len(pathSizes4) > 0:
                            if len(newPath3.split(' -> ')) < pathSizes4[0][0]:
                                if len(regionMatrix[regionId][rId][2]) >= 3:
                                    del regionMatrix[regionId][rId][2][pathSizes4[0][1]]

                                regionMatrix[regionId][rId][2].append(newPath3)
                                addedPaths += 1

                            elif len(regionMatrix[regionId][rId][2]) < 3:
                                regionMatrix[regionId][rId][2].append(newPath3)
                                addedPaths += 1

                        else:
                            regionMatrix[regionId][rId][2].append(newPath3)
                            addedPaths += 1

    # Finally, we update the destination of the doors.
    doorDict[door1][0] = door2
    return addedPaths


# IDK if I'll ever implement this function because of the complexity...
def removePath():
    return


# Complete
def findPath():
    region1 = ""
    region2 = ""
    while region1 not in regionDict:
        region1 = input("What is the name of the region you are starting in? (Enter 'p' to see all regions)\n")
        if region1 == 'p':
            printRegions()
        if region1 == 'c':
            return

    while region2 not in regionDict:
        region2 = input("What is the name of the region you want to end in? (Enter 'p' to see all regions)\n")
        if region2 == 'p':
            printRegions()
        if region2 == 'c':
            return

    region1id = regionDict[region1]
    region2id = regionDict[region2]

    if len(regionMatrix[region1id][region2id][2]) > 0:
        print()
        for path in sorted(regionMatrix[region1id][region2id][2], key=len):
            print(path)
        print()
    else:
        print("No path exists yet, sorry.")


# Complete
def editDoor(player):
    previousRegion = ""
    while previousRegion not in regionDict:
        input1 = input(f"I believe you were just in the {player.currentRegion} region. Is that correct? (y or n)\n")
        if input1 == "y":
            previousRegion = player.currentRegion
        else:
            previousRegion = input("Sorry about the confusion. What region were you just in? (Enter 'p' to see all regions)\n")
            if previousRegion == "p":
                printRegions()
            if previousRegion == 'c':
                return

    print(f"You were in the {previousRegion} region.\nThese are the doors in the {previousRegion} region.\n")
    printDoorsInRegion2(previousRegion)
    print()
    enteredDoor = ""
    while enteredDoor not in doorDict:
        if previousRegion != 'sandgem/jubilife':
            enteredDoor = (previousRegion + input(f"Which door did you enter? (Only input the text that is not included in the region)\n"))
        else:
            enteredDoor = input(f"Which door did you enter? (Make sure you input a valid door)\n")
        if enteredDoor == (previousRegion + 'c'):
            return

    exitedDoor = ""
    input1 = input(f"Did you exit into a deadend? (y or n)\n")

    if input1 == "y":
        exitedDoor = "deadend"
    else:
        newRegion = ""
        while newRegion not in regionDict:
            newRegion = input("What region did you end up in? (Enter 'p' to see all regions)\n")
            if newRegion == "p":
                printRegions()
            if newRegion == 'c':
                return

        player.currentRegion = newRegion

        print(f"These are the doors in the {player.currentRegion} region.")
        printDoorsInRegion2(player.currentRegion)

        while exitedDoor not in doorDict:
            if player.currentRegion != 'sandgem/jubilife':
                exitedDoor = (player.currentRegion + input(f"Which door did you exit? (Only input text that is not included in the region)\n"))
            else:
                exitedDoor = input(f"Which door did you exit? (Make sure you input a valid door)\n")
            if exitedDoor == (player.currentRegion + 'c'):
                return

    input1 = input(f"You entered {enteredDoor} and exited {exitedDoor}. Is this correct? (y or n)\n")

    if input1 == "y":
        print(f"Let me update the paths between regions.")
        addedPaths1 = addPath(enteredDoor, exitedDoor)
        addedPaths2 = addPath(exitedDoor, enteredDoor)
        print(f"Successfully added {addedPaths2 + addedPaths1} paths!")
        return
    else:
        print(f"I am assuming you made an error and am quiting out of this without adding any paths between {enteredDoor} and {exitedDoor}")
        return


# Complete
def listUnexploredDoors():
    for key, value in doorDict.items():
        if value[0] == "":
            print(f"Door: {key}. Region: {value[1]}")


# Complete
def updateSpecialEvents():
    input1 = ''
    while input1 not in specialEvents:
        input1 = input("What special event are you completing? (This cannot be undone) (Enter 'p' to see all special events or 'c' to cancel)\n")
        if input1 == 'p':
            for event in specialEvents:
                print(event)

        if input1 == 'c':
            return

    return input1


# Complete (I skipped the HMs fly and defog because it didn't make much sense to include them.)
def canUse(HM, player):
    # Update all the doors that require rock smash.
    if HM == 'teleport':
        for key, value in doorDict.items():
            if 'PC_teleport' in key:
                value[2] = True
                addPath(key, value[0])
    elif HM == 'surf':
        if 5 in player.gymBadges:
            # Update any paths that require surf and waterfall.
            if 'waterfall' in player.availableHMs and 8 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'surfAndWaterfall' in key or 'surfTo' in key:
                        value[2] = True
                        addPath(key, value[0])
            # Update any paths that require surf and rock climb.
            elif 'rock climb' in player.availableHMs and 7 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'surfAndRockClimb' in key or 'rockClimbAndSurf' in key or 'surfTo' in key:
                        value[2] = True
                        addPath(key, value[0])
            else:  # Update any paths that only require surf.
                for key, value in doorDict.items():
                    if 'surfTo' in key:
                        value[2] = True
                        addPath(key, value[0])
    elif HM == 'waterfall':
        if 7 in player.gymBadges:
            if 'surf' in player.availableHMs and 5 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'surfAndWaterfall' in key:
                        value[2] = True
                        addPath(key, value[0])
    elif HM == 'rock climb':
        if 8 in player.gymBadges:
            if 'surf' in player.availableHMs and 5 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'surfAndRockClimb' in key or 'rockClimbAndSurf' in key or 'rockClimbTo':
                        value[2] = True
                        addPath(key, value[0])
            else:
                for key, value in doorDict.items():
                    if 'rockClimbTo' in key:
                        value[2] = True
                        addPath(key, value[0])
    elif HM == 'cut':
        if 2 in player.gymBadges:
            for key, value in doorDict.items():
                if 'cutTo' in key:
                    value[2] = True
                    addPath(key, value[0])
    elif HM == 'rock smash':
        if 1 in player.gymBadges:
            if 'strength' in player.availableHMs and 6 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'strengthAndRockSmash' in key or 'rockSmashAndStrength' in key or 'rockSmashTo' in key:
                        value[2] = True
                        addPath(key, value[0])
            else:
                for key, value in doorDict.items():
                    if 'rockSmashTo' in key:
                        value[2] = True
                        addPath(key, value[0])
    elif HM == 'strength':
        if 6 in player.gymBadges:
            if 'rock smash' in player.availableHMs and 1 in player.gymBadges:
                for key, value in doorDict.items():
                    if 'strengthAndRockSmash' in key or 'rockSmashAndStrength' in key or 'strengthTo' in key:
                        value[2] = True
                        addPath(key, value[0])
            else:
                for key, value in doorDict.items():
                    if 'strengthTo' in key:
                        value[2] = True
                        addPath(key, value[0])


# This will check for updates on new gym badges or HM's and also update the regionMatrix accordingly.
# Complete
def update(updatedItem, player):
    if updatedItem == 'rock smash':
        if 1 in player.gymBadges:
            canUse('rock smash', player)
    elif updatedItem == 'cut':
        if 2 in player.gymBadges:
            canUse('cut', player)
    elif updatedItem == 'fly':
        return
    elif updatedItem == 'surf':
        if 5 in player.gymBadges:
            canUse('surf', player)
    elif updatedItem == 'strength':
        if 6 in player.gymBadges:
            canUse('strength', player)
    elif updatedItem == 'rock climb':
        if 7 in player.gymBadges:
            canUse('rock climb', player)
    elif updatedItem == 'waterfall':
        if 8 in player.gymBadges:
            canUse('waterfall', player)
    elif updatedItem == 'teleport':
        canUse('teleport', player)
    elif updatedItem == 1:
        if 'rock smash' in player.availableHMs:
            canUse('rock smash', player)
        # Also updates the GTS
        doorDict['jubilife_walkToGTS'][2] = True
        doorDict['GTS_walkToJubilife'][2] = True
        addPath('jubilife_walkToGTS', 'GTS_walkToJubilife')
    elif updatedItem == 2:
        if 'cut' in player.availableHMs:
            canUse('cut', player)
    elif updatedItem == 3:
        # Updates the tunnel in hearthome.
        doorDict['hearthome_rightTunnel'][2] = True
        if doorDict['hearthome_rightTunnel'][0] != '':
            addPath('hearthome_rightTunnel', doorDict['hearthome_rightTunnel'][0])
    elif updatedItem == 4:
        return
    elif updatedItem == 5:
        if 'surf' in player.availableHMs:
            canUse('surf', player)
    elif updatedItem == 6:
        if 'strength' in player.availableHMs:
            canUse('strength', player)
    elif updatedItem == 7:
        if 'rock climb' in player.availableHMs:
            canUse('rock climb', player)
    elif updatedItem == 8:
        if 'waterfall' in player.availableHMs:
            canUse('waterfall', player)
    elif updatedItem == 'Obtained Bike':
        for key, value in doorDict.items():
            if 'bikeTo' in key:
                value[2] = True
                addPath(key, value[0])
    elif updatedItem == 'Obtained Galactic Key':
        # Updates all the galactic doors
        doorDict['GWarehouse_walkToGWarehouseKey'][2] = True
        addPath('GWarehouse_walkToGWarehouseKey', 'GWarehouseKey_walkToGWarehouse')
        doorDict['GMasterBall_walkToGMasterBallEnt'][2] = True
        doorDict['GMasterBallEnt_walkToGMasterBall'][2] = True
        addPath('GMasterBall_walkToGMasterBallEnt', 'GMasterBallEnt_walkToGMasterBall')
        doorDict['GHQ1f_walkToGHQ1fStairs'][2] = True
        doorDict['GHQ1fStairs_walkToGHQ1f'][2] = True
        addPath('GHQ1f_walkToGHQ1fStairs', 'GHQ1fStairs_walkToGHQ1f')
    elif updatedItem == 'Talked With Roark':
        # Updates the front of Oreburgh's gym
        doorDict['oreburgh_gym'][2] = True
        if doorDict['oreburgh_gym'][0] != '':
            addPath('oreburgh_gym', doorDict['oreburgh_gym'][0])
    elif updatedItem == 'Obtained Wind Works Key':
        # Updates the wind works entrance
        doorDict['floaroma_windWorksEnt'][2] = True
        if doorDict['floaroma_windWorksEnt'][0] != '':
            addPath('floaroma_windWorksEnt', doorDict['floaroma_windWorksEnt'][0])
    elif updatedItem == 'Talked With Fantina':
        # Updates the front of Hearthome's gym
        doorDict['hearthome_gym'][2] = True
        if doorDict['hearthome_gym'][0] != '':
            addPath('hearthome_gym', doorDict['hearthome_gym'][0])
    elif updatedItem == 'Moved the Psyduck':
        # Updates the path from Solaceon to Celestic (idk why anyone would ever do this)
        doorDict['solaceon_walkToCelestic'][2] = True
        doorDict['celestic_walkToSolaceon'][2] = True
        addPath('solaceon_walkToCelestic', 'celestic_walkToSolaceon')
    elif updatedItem == 'Talked With Volkner':
        # Updates the front of Sunnyshore's gym
        doorDict['sunnyshore_gym'][2] = True
        if doorDict['sunnyshore_gym'][0] != '':
            addPath('sunnyshore_gym', doorDict['sunnyshore_gym'][0])
    elif updatedItem == 'Cleared the Galactic Conference Hall':
        # Updates the conference hall path
        doorDict['GConferenceLeft_walkToGConferenceRight'][2] = True
        addPath('GConferenceLeft_walkToGConferenceRight', 'GConferenceRight_walkToGConferenceLeft')
    elif updatedItem == 'Freed Windworks Guy':
        # Updates the bridge in floaroma
        doorDict['floaroma_walkToRoute205'][2] = True
        addPath('floaroma_walkToRoute205', 'route205_walkToFloaroma')
    elif updatedItem == 'Did Stark Mountain Cutscene':
        # Updates the locked house in the survival area (this would only happen in a last ditch effort)
        doorDict['survival_lockedHouse'][2] = True
        if doorDict['survival_lockedHouse'][0] != '':
            addPath('survival_lockedHouse', doorDict['survival_lockedHouse'][0])


# This function adds a path from all the regions that can walk to the other regions but not the other way around.
# Complete
def finishMatrix():
    for key, value in doorDict.items():
        if 'walkTo' in key and value[2]:
            addPath(key, value[0])


def main():
    finishMatrix()
    playerName = input("Welcome trainer! What is your name?\n")
    player = Player(name=playerName, currentRegion='sandgem/jubilife', availableHMs=[], gymBadges=[])
    print(f"Welcome to the random Platinum Map Tracker {player.name}!")
    print("In any of the menus, you can enter 'c' to cancel.")

    while True:
        # The main menu
        input1 = -1
        while (input1 > 10 and input1 != 18) or input1 < 0:
            listMenu()
            try:
                input1 = int(input(f"What would you like to do?\n"))
            except ValueError:
                print("Input was not an integer. Try again...")
                continue

        if input1 == 0:
            player.changeName()
        elif input1 == 1:
            changedBadge = player.changeGymBadges()
            if changedBadge:
                update(changedBadge, player)
        elif input1 == 2:
            changedHM = player.changeAvailableHMs()
            if changedHM:
                update(changedHM, player)
        elif input1 == 3:
            specialEvent = updateSpecialEvents()
            if specialEvent:
                update(specialEvent, player)
        elif input1 == 4:
            editDoor(player)
        elif input1 == 5:
            findPath()
        elif input1 == 6:
            printRegions()
        elif input1 == 7:
            printDoors()
        elif input1 == 8:
            printDoorsInRegion()
        elif input1 == 9:
            listUnexploredDoors()
        elif input1 == 10:
            printSpecificDoor()
        elif input1 == 18:
            print("Thank you for using the random Platinum Map Tracker!\n (✌ﾟ∀ﾟ)✌")
            break


main()
