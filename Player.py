HMs = ["rock smash", "cut", "defog", "fly", "surf", "strength", "rock climb", "waterfall", "teleport"]


class Player:
    def __init__(self, name: str, currentRegion: str, availableHMs: [str], gymBadges: [int]):
        self.name = name
        self.currentRegion = currentRegion
        self.availableHMs = availableHMs
        self.gymBadges = gymBadges

    def __str__(self):
        return f"{self.name} has {len(self.gymBadges)} gym badges and these HMs: {self.availableHMs}."

    def changeName(self):
        newName = input(f"What do you want your new name to be {self.name}?\n")
        self.name = newName
        print(f"Alright, I will call you {self.name} from now on.")

    def listHMs(self):
        for i in range(len(HMs)):
            print(f"{i}: {HMs[i]}")

    def changeAvailableHMs(self):
        input1 = ""
        input2 = ""
        print(f"Your current HMs: {self.availableHMs}")

        while "a" not in input1.lower() and "r" not in input1.lower():
            input1 = input("Are you adding (a) or removing (r) an HM?\n")
            if input1 == 'c':
                return

        if "a" in input1.lower():
            while input2 not in HMs:
                print(f"Possible HMs: {HMs}")
                input2 = input("Sweet! What HM did you get?\n")
                if input2 == 'c':
                    return

            if input2 not in self.availableHMs:
                self.availableHMs.append(input2)
                print("Successfully added the HM!")
                return input2
            else:
                print("HM had already been added previously.")

        else:
            while input2 not in HMs:
                print(f"Possible HMs: {HMs}")
                input2 = input("Sorry about the soft reset. Which HM are you removing? (Enter 'c' to cancel)\n")
                if input2 == 'c':
                    return

            if input2 in self.availableHMs:
                self.availableHMs.remove(input2)
                print("Successfully removed HM.")
            else:
                print("The HM was already absent from the list.")

        print(f"Updated HMs list: {self.availableHMs}")

    def changeGymBadges(self):
        input1 = ""
        input2 = 0
        print(f"Your current gym badges: {self.gymBadges}")

        while "a" not in input1.lower() and "r" not in input1.lower():
            input1 = input("Are you adding (a) or removing (r) a gym badge?\n")
            if input1 == 'c':
                return

        if "a" in input1.lower():
            while input2 > 8 or input2 < 1:
                try:
                    input2 = int(input("Congrats! Which badge have you earned? (Enter a number between 1 and 8) (Enter 0 to cancel)\n"))
                    if input2 == 0:
                        return
                except ValueError:
                    print("Your input was not an integer...")
                    continue
                if input2 > 8 or input2 < 1:
                    print("Make sure your input is between 1 and 8.")

            if input2 not in self.gymBadges:
                self.gymBadges.append(int(input2))
                print("Badge successfully added!")
                return input2

            else:
                print("You have already marked the badge as done.")

        else:
            while input2 > 8 or input2 < 1:
                try:
                    input2 = int(input("Sorry about the soft reset. Which badge are you removing?  (Enter a number between 1 and 8) (Enter 0 to cancel)\n"))
                    if input2 == 0:
                        return
                except ValueError:
                    print("Your input was not an integer...")
                    continue
                if input2 > 8 or input2 < 1:
                    print("Make sure your input is between 1 and 8.")

            if input2 in self.gymBadges:
                self.gymBadges.remove(input2)
                print("Successfully removed the gym badge.")
            else:
                print("You did not have that gym badge marked as complete so nothing was removed.")

        print(f"Your updated gym badges: {self.gymBadges}")
