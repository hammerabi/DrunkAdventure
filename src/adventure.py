#Josh Butcher
#This is a script adventure game written in Python 3.5
import random

def move(direction):
    if any(direction in s for s in player[3][2]):
        switch_location(direction)
    else:
        print ("Invalid direction amigo")
        print ()

def check_for_items(place):
    if (len(place) > 3):
        print ("Congrats! You found your " + place[-1])
        player[2].append(place.pop())
        print ()
    
def plane_crash_event():
    rand = random.randint(1,100)
    if (rand % 10 == 0):
        print ("Oh no! Your plane crashed. Game over.")
        player[4] = False
        quit_game = input("Press any key to quit: ")
        quit()

def make_that_money():
    rando = random.randint(1,100)
    if (rando == 10):
        print ("You steal a car and sell it. You gained $2000")
        player[1] += 2000
    if (rando == 20):
        print ("You find a lost wedding ring on the ground. You gained $6000")
        player[1] += 6000
        
    if (rando == 30):
        print ("A kind stranger gives you some money. You gained $500")
        player[1] += 500
        
    if (rando == 40):
        print ("A nice lady pays you to help her with groceries. You gained $200")
        player[1] += 200
        
    if (rando == 50):
        print ("You sell your luggage. You gained $1000")
        player[1] += 1000
        
    if (rando == 60):
        print ("You steal a bike and sell it on Kijiji. You gained $2500")
        player[1] += 2500        
            
        
def switch_location(new_location):
    
    if player[3][0] == "Denver" and new_location == "N":
        player[3] = locations[1]
    if player[3][0] == "Denver" and new_location == "E":
        player[3] = locations[2]
    if player[3][0] == "Denver" and new_location == "S":
        player[3] = locations[3]
    if player[3][0] == "Denver" and new_location == "W":
        player[3] = locations[4]
        
    if player[3][0] == "Detroit" and new_location == "E":
        player[3] = locations[2]
    if player[3][0] == "Detroit" and new_location == "S":
        player[3] = locations[0]
    if player[3][0] == "Detroit" and new_location == "W":
        player[3] = locations[4]
        
        
    if player[3][0] == "Houston" and new_location == "N":
        player[3] = locations[0]
    if player[3][0] == "Houston" and new_location == "E":
        player[3] = locations[2]
    if player[3][0] == "Houston" and new_location == "W":
        player[3] = locations[4]
        
        
    if player[3][0] == "Los Angeles" and new_location == "N":
        player[3] = locations[1]
    if player[3][0] == "Los Angeles" and new_location == "E":
        player[3] = locations[0]
    if player[3][0] == "Los Angeles" and new_location == "S":
        player[3] = locations[3]
        
    if player[3][0] == "New York" and new_location == "N":
        player[3] = locations[1]
    if player[3][0] == "New York" and new_location == "W":
        player[3] = locations[0]
    if player[3][0] == "New York" and new_location == "S":
        player[3] = locations[3]


#Structure = (name, id, possible directions)
locations = [['Denver', 1, ['N', 'E', 'S', 'W']], ['Detroit', 2, ['E', 'S', 'W']], ['New York', 3, ['N', 'S', 'W']], ['Houston', 4, ['N', 'E', 'W']], ['Los Angeles', 5, ['N', 'E', 'S']]]

player = []

money = 0
inventory = []
location = random.choice(locations)
life = True

name = input("Enter your name: ")

player.append(name) #[0]
player.append(money) #[1]
player.append(inventory) #[2]
player.append(location) #[3]
player.append(life) #[4]
lost_items = ["passport", "wallet", "watch", "dignity", "fiancee"]
locations = list(locations)


#randomly distribute the lost items across the map
for i in lost_items:
    random_digit = random.randint(0,4)
    locations[random_digit].insert(len(locations[random_digit]), i)

'''
Map:
            Detroit
               |
LA <----->  Denver  <----->  New York
               |
            Houston
'''



print ("Hey " + player[0] + ". You've just woken up in " + location[0] + ". You should not have partied so hard... It seems like you're missing all of your stuff! It's time to re-trace your steps and find all of your valuables")
print ()
print ("Here is what you're missing: Passport, Wallet, Watch, Dignity, Fiancee")
print ()
print ("Instructions: To fly somewhere, enter either N (North), E (East), S (South), or W (West).")
print ()

while (len(inventory) != 5 and life == True):
    
    check_for_items(player[3])
    
    user_in = input("What direction would you like to go? ")
    print ()
    
    user_in = user_in.upper()
    
    move(user_in)
    
    plane_crash_event()
    
    make_that_money()
    
    print ("You are now in: " + player[3][0])
    print ()
    print ("You can move: ")
    print (', '.join(player[3][2]))
    print ()
    print ("Your inventory is: ")
    print (', '.join(player[2]))
    print ()

print ("Congratulations " + player[0] + "! You found all of your stuff. Next time, use a safe.")


        
    


