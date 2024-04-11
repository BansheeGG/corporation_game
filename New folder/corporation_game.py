import random
import io
import city_gen
import corporations
MainCity = 0
GameActive = False

GamePage = open("game_page.html", "w")

class PlayerCharacter():
    name = ""
    gender = ""
    money = 0
    equipment = []
    body = [100, 100, 100, 100, 100, 100]
    player_district = 0

    def PrintBodyStatus(self):
        print(
            "HEAD: " + str(self.body[0]) + "\n" +
            "TORSO: " + str(self.body[2]) + "\n" +
            "L. ARM: " + str(self.body[1]) + "\n" +
            "R. ARM: " + str(self.body[3]) + "\n" +
            "L. LEG: " + str(self.body[4]) + "\n" +
            "R. LEG: " + str(self.body[5]) + "\n"
            
        )


def StartGame():
    print("CORPORATION GAME - v0.1\nMade by BANSHEE")
    _input = int(input("[1 - Start New Game|2 - Load Existing Game|3 - Quit]"))
    match _input:
        case 1:
            GameActive = True
            CreateNewSave()
        case 2:
            GameActive = True
            LoadSave()
        case 3:
            quit()


def CreateNewSave():
    Player = PlayerCharacter
    Player.name = input("What is your name? ")
    Player.gender = input("What's your gender?")

    MainCity = city_gen.CreateCity(9)
    Player.player_district = corporations.Choose(MainCity.districtNames)
    Greeting = "You are " + Player.name + ", a citizen living in " + Player.player_district + " in the city of " + MainCity.cityName + "."
    print(Greeting)
    GamePage.write("<text>" + Greeting + "</text><br>\n<text>Current Money: " + str(Player.money) + "</text><br>")
    GamePage.write("<button>" + "You're unemployed! Find a place to work." + "</button><br>\n" +
                   "<button>" + "You don't have anywhere to stay." + "</button><br>\n" +
                   "<button>" + "Contacts" + "</button><br>\n" +
                   "<button>" + "Wander the streets" + "</button><br>\n" +
                   "<button>" + "Save and Quit" + "</button><br>\n"
                   )
    pass

def LoadSave():
    pass

StartGame()

while GameActive == True:
    pass