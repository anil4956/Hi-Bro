# Constants
MARVEL_CHARS = ["ironman", "captainamerica", "thor", "hulk", "blackidow", "hawkeye", "doctortrange", "scarletwitch", "vision", "falcon"]
BIKE_BRANDS =  ["aprilla", "vvs", "specialized", "giant", "santacruz", "scott", "ridley", "fuji", "bmw", "inja", "", "amis"]
DC_CHARS = ["superman", "batman", "wonderwoman", "flash", "aquaman", "greenlantern", "artiananhunter", "alyborg", "batgirl", "robin"]

import random

print("Password Generator")
print("==================")
print("\n")
s = set()
try:
    password_gen = input("How many passwords are needed?: ")
    if password_gen.isnumeric():
        password_gen = int(password_gen)
    else:
        raise ValueError("Please enter a number.")

#try:
 #   password_gen = input("How many passwords are needed?: ")
    
#except TypeError:
#    print("Please enter a  number")
#except ValueError:
 #   print("Please enter a  number")
#else:
 #   print("Please enter a number")
  

    for i in range(1,password_gen+1):
        psd_1 = random.choice(MARVEL_CHARS)
        psd_2 = random.choice(BIKE_BRANDS)
        psd_3 = random.choice(DC_CHARS)
        password = psd_1+psd_2+psd_3
        if password_gen in range(24):
            print(f"{i:3} --> {password:1}")
            s.add(password)
    
        else:
            print("Please enter a value between 1 to 24")
            break
    
    if password_gen==0:
        print("Please enter a value between 1 and 24")

except:
    None
print(len(s))
      
    
    
