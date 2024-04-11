import random
import os
import corporations

cityNames = ["Night City", "Gangwon", "Nueva Santes", "Seoul", "Little Appalchia", "Golem City", "Prague", "New Stockholm", "West Cleveland"]


class Citizen:
    name = ""
    gender = ""
    age = 0
    occupation = ""
    alignment = ""

class District:
    districtName = ""
    districtPopulation = 0
    districtBusinesses = []

class City:
    cityName = ""
    cityPopulation = 0
    districtCount = 0
    districtNames = []
    districtTypes = []
    districtClasses = []


def CreateCity(districtAmount):
    MainCity = City
    MainCity.cityName = corporations.Choose(cityNames)
    MainCity.districtCount = districtAmount
    i = 0
    while i != districtAmount + 1:
        _district = District
        _district.districtName = "District " + str(i)
        _district.districtPopulation = random.randint(350000, 2000000)
        MainCity.cityPopulation += _district.districtPopulation
        MainCity.districtNames.append(_district.districtName)
        MainCity.districtClasses.append(_district)
        i += 1
    newpath = r'C:\Users\U297JQ5\OneDrive - Volkswagen AG\Desktop\New folder\Cities\ ' + str(MainCity.cityName) + str(random.randint(100000,999999))
    os.makedirs(newpath)
    citizens = open(newpath + r"\citizens.txt", "a")
    districts = open(newpath + r"\districts.txt", "a")

    for i in MainCity.districtNames:
        districts.write(MainCity.districtNames[MainCity.districtNames.index(i)] + ", Population: " + str(MainCity.districtClasses[MainCity.districtNames.index(i)].districtPopulation) + "\n")

    firstnames = open(r"generation_resources\fem first names.txt","r").readlines()
    lastnames = open(r"generation_resources\last names.txt", "r").readlines()
    occupations = open(r"generation_resources\occupations.txt", "r").readlines()

    i = 0
    while i != 75 + 1:
        _citizen = Citizen
        _citizen.name = firstnames[random.randint(0, 49)].strip("\n") + " " + lastnames[random.randint(0, 49)].strip("\n")
        _citizen.age = random.randint(18,120)
        _citizen.occupation = occupations[random.randint(0, 34)].strip("\n")
        citizens.write(_citizen.name.strip("\n") + ", Age: " + str(_citizen.age) + ", Occupation: " + _citizen.occupation + "\n")
        i += 1

    return MainCity