from Digimon_Class import Digimon, Active, Inactive
import logging
import re
from pathlib import Path
from playsound import playsound

def main():
    logging.basicConfig(filename="Digimon_Tracker.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    # Welcome screen and ASCII art.
    print("_"*50)
    print(r"""
    ______ _____ _____ ________  ________ _   _ 
    |  _  \_   _|  __ \_   _|  \/  |  _  | \ | |
    | | | | | | | |  \/ | | | .  . | | | |  \| |
    | | | | | | | | __  | | | |\/| | | | | . ` |
    | |/ / _| |_| |_\ \_| |_| |  | \ \_/ / |\  |
    |___/  \___/ \____/\___/\_|  |_/\___/\_| \_/
       _____ ___    _   ___ _  _____ ___       _   _ 
      |_   _| _ \  /_\ / __| |/ / __| _ \ __ _/ | / |
        | | |   / / _ \ (__| ' <| _||   / \ V / |_| |
        |_| |_|_\/_/ \_\___|_|\_\___|_|_\  \_/|_(_)_|                                            
    """)

    # Current version info
    print("               Version 1.01")
    print("_"*50)
    playsound(Path(__file__).parent / 'Digi_Beep.mp3')
    print("\nWelcome to the Digimon Tracker, a way to catalog all of your digital monsters!\n")
 
    # Loads Digimon from the .csv file
    fname = "Digimon_Info.csv"
    lst_digimon = []
    lst_digimon = load_digimon(fname)
    logging.info("Loaded Digimon into catalog successfully.")

    # Inserts Digimon to the .csv file
    while(True):
        digimon = insert_digimon()
        if digimon == None:
            break
        logging.info("Inserted a new Digimon into catalog.")        
        lst_digimon.append(digimon)
    
    # Prints current catalog of devices
    print("\n\n-------»Current Catalog«-------\n")
    for elem in lst_digimon:
        print(elem)
    print("-----------------------------------")

    # Saves Digimon into the .csv file
    save_digimon(fname, lst_digimon)
    logging.info("Successfully saved Digimon to " + fname)
    print("\n\n")



# Save Digimon function
def save_digimon(fname, lst_digimon):
    with open(fname, "w") as f:
        for digimon in lst_digimon:
            if type(digimon) == Active:
                f.write(digimon._device + "," + digimon._version + "," + digimon._shape + "," + digimon._color +"\n")
            elif type(digimon) == Inactive:
                f.write(digimon._device + "," + digimon._version + "," + digimon._shape + "," + digimon._color + "\n")
            else:
                pass



# Load Digimon function
def load_digimon(fname) -> list:
    lst_digimon = []

    with open(fname, "r") as f:
        for line in f:
            info = line.split(',')
            if info[0] == "Digital Monster":
                digimon = Active(info[0], info[1], info[2], info[3])
            elif info[0] == "Digital Monster X":
                digimon = Active(info[0], info[1], info[2], info[3])
            else:
                digimon = None

            if digimon != None:
                lst_digimon.append(digimon)

    return lst_digimon




# Insert Digimon function
def insert_digimon() -> Digimon:

    print("\nWhat would you like to do?")
    print("\t1) Add New Digimon to the Catalog")
    print("\t2) Exit & View the Current Catalog")
    loop_start = input(">>> ")

    # Break out of function if user wants to quit
    if loop_start not in ["1"]:
        return None    
    
    while True:
        try:
            device = input("\nWhat is the name of your device?\n>>>")
            check = re.search(',', device)

            if check != None:
                raise ValueError
            check = re.search('!', device)

            if check != None:
                raise ValueError
            check = re.search('?', device)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nDevice name cannot special characters (commas, questions marks or exclamation).\n")
            logging.error("User attempted to enter comma into device name.")
        else:
            break

    while True:
        try:
            version = input("\nWhat is the version of your device?\n>>>")
            check = re.search(',', version)

            if check != None:
                raise ValueError
            check = re.search('!', version)

            if check != None:
                raise ValueError
            check = re.search('?', version)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nVersion name cannot special characters (commas, questions marks or exclamation).\n")
            logging.error("User attempted to enter comma into version name.")
        else:
            break

    while True:
        try:
            shape = input("\nWhat is the shape of your device?\n>>>")
            check = re.search(',', shape)

            if check != None:
                raise ValueError
            check = re.search('!', shape)

            if check != None:
                raise ValueError
            check = re.search('?', shape)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nName of shape cannot special characters (commas, questions marks or exclamation).\n")
            logging.error("User attempted to enter comma into shape name.")
        else:
            break


    while True:
        try:
            color = input("\nWhat is the color of your device?\n>>>")
            check = re.search(',', color)

            if check != None:
                raise ValueError
            check = re.search('!', color)

            if check != None:
                raise ValueError
            check = re.search('?', color)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nName of color cannot special characters (commas, questions marks or exclamation).\n")
            logging.error("User attempted to enter comma into color name.")
        else:
            break
      

    if loop_start == "1":
        digimon = Active(device, version, shape, color)
    else:
        digimon = None

    print("\nDigimon enterted into catalog successfully!\n")
    return digimon



if __name__ == "__main__":
    main()