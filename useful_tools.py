import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon","Paul McCartney","george Harrison","Ringo star"]

def get_file_exit(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)