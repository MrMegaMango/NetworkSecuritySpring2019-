import random
class EscapeRoom:
    def start(self):
        print("started")
        global time,code,comma_digit_list,look_glasses,glasses,look_hairpin,hairpin,look_board,floor,prying,mirror,look_hammer,hammer,glasses,unlock_chest,user_code,unlock_door,open_chest,pry_board,wear_glasses,inventory,status
        time=100
        code=random.randint(0,9999)
        code_string=str(code)
        while len(code_string)<4:
            code_string='0'+code_string
        code_string=list(set(code_string))  #to remove duplicates
        comma_digit_list=",".join(sorted(code_string))
        glasses, look_hairpin, hairpin, look_board, floor, prying, mirror, look_hammer, hammer, look_glasses, glasses, unlock_chest, user_code, unlock_door,open_chest,pry_board,wear_glasses,status = (0,)*18
        inventory=""
    def command(self, command_string):
        global time,code,comma_digit_list,glasses,look_hairpin,hairpin,look_board,floor,prying,mirror,look_hammer,hammer,look_glasses,glasses,unlock_chest,user_code,unlock_door,open_chest,pry_board,wear_glasses,inventory,status
        time=time-1
        command_list=command_string.split(' ')
        if command_list[0] == "look":
            if len(command_list)==1:
                print ("You are in a locked room. There is only one door and it has a numeric keypad. Above the door is a clock that reads " + str(time) + ". Across from the door is a large mirror. Below the mirror is an old chest. The room is old and musty and the floor is creaky and warped.")
            elif command_list[1] == "door":
                if wear_glasses == 0:
                    print("The door is strong and highly secured. The door is locked and requires a 4-digit code to open.")
                else:
                    print("The door is strong and highly secured. The door is locked and requires a 4-digit code to open. But now you're wearing these glasses you notice something! There are smudges on the digits "+comma_digit_list+".")
            elif command_list[1] == "mirror":
                if look_hairpin == 0:
                    print("You look in the mirror and see yourself... wait, there's a hairpin in your hair. Where did that come from?")
                    look_hairpin = 1
                else:
                    print("You look in the mirror and see yourself.")
            elif command_list[1] == "chest":
                print("An old chest. It looks worn, but it's still sturdy.")
            elif command_list[1] == "floor":
                print("The floor makes you nervous. It feels like it could fall in. One of the boards is loose.")
                look_board=1
            elif command_list[1] == "board":
                if floor == 0:
                    print("You don't see that here.")
                elif prying == 0:
                    print("The board is loose, but won't come up when you pull on it. Maybe if you pried it open with something.")
                    look_board=1
                else:
                    print("The board has been pulled open. You can look inside.")
            elif command_list[1] == "hairpin":
                if mirror == 0:
                    print("You don't see that here.")
                else:
                    print("You see nothing special")
            elif command_list[1] == "hammer":
                if hammer == 0:
                    print("You don't see that here.")
                else:
                    print("You see nothing special.")
            elif command_list[1] == "glasses":
                if glasses == 0:
                    print("You don't see that here.")
                else:
                    print("These look like spy glasses. Maybe they reveal a clue!")
            elif command_list[1] == "clock":
                print("You see nothing special.")
            elif command_list[1] == "in":
                item=""
                if command_list[2] == "chest":
                    if hammer == 0:
                        item="hammer"
                        look_hammer=1
                elif command_list[2] == "board":
                    if glasses == 0:
                        item="glasses"
                        look_glasses=1
                else:
                    print("You can't look in that!")
                    return
                if item:
                    item=" a "+item
                print("Inside the "+command_list[2]+" you see:"+item+".")
            else:
                print("You don't see that here.")
        elif command_list[0]=="get":
            if len(command_list)==2:
                if command_list[1]=="hairpin":
                    if hairpin==0:
                        if look_hairpin==0:
                            print("You don't see that.")
                        else:
                            print("You got it.")
                            hairpin=1
                    else:
                        print("You already have that.")
                elif command_list[1]=="board":
                    if look_board == 0:
                        print("You don't see that.")
                    else:
                        print("You can't get that.")
                elif command_list[1] in ["door","clock","mirror","chest","floor"]:
                    print("You can't get that.")
                elif command_list[1]=="hammer":
                    if hammer == 1:
                        print("You already have that.")
                elif command_list[1]=="glasses":
                    if glasses == 1:
                        print("You already have that.")
                else:
                    print("You don't see that.")
            else:
                if command_list[1]=="hammer":
                    if hammer==0:
                        if command_list[-1]=="chest":
                            if open_chest==0:
                                print("It's not open.")
                            else:
                                print("You got it.")
                                hammer=1
                    else:
                        print("You don't see that.")
                elif command_list[1]=="glasses":
                    if glasses==0:
                        if command_list[-1]=="board":
                            if pry_board==0: #pry board, not open board
                                print("It's not open.")
                            else:
                                print("You got it.")
                                glasses=1
                    else:
                        print("You don't see that.")
                elif command_list[-1] not in ["chest","board"]: #does not in work?
                    print("You can't get something out of that!")
                else: #only thing left is "anything else from chest or board"
                    print("You don't see that.")
        elif command_list[0]=="unlock":
            if command_list[1]=="chest":
                if unlock_chest==1:
                    print("It's already unlocked.")
                elif command_list[3]=="hairpin":
                    if hairpin==1:
                        print("You hear a click! It worked!")
                        unlock_chest=1
                    else:
                        print("Go get a hairpin first.")
                else:
                    print("You don't have a " + command_list[-1] +".") # fixed
            elif command_list[1]=="door":
                if unlock_door==0:
                    user_code=command_list[-1]
                    if user_code.isdigit():
                        if int(user_code)==code:
                            print("You hear a click! It worked!")
                            unlock_door=1
                        elif len(str(user_code))<4:
                            print("The code must be 4 digits.")
                        else:
                            print("That's not the right code!")
                else:
                    print("It's already unlocked.")

            elif command_list[1] == "hairpin" and look_hairpin:
                print("You don't see that here.")
            elif command_list[1] == "board" and look_board:
                print("You don't see that here.")
            elif command_list[1] == "hammer" and hammer:
                print("You don't see that here.")
            elif command_list[1] == "glasses" and glasses:
                print("You don't see that here.")
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                print("You can't unlock that!")
            else:
                print("You don't see that here.")
        elif command_list[0]=="open":
            if command_list[1] == "chest":
                if open_chest==0:
                    if unlock_chest==0:
                        print("It's locked.")
                    else:
                        print("You open the chest.")
                        open_chest=1
                else:
                    print("It's already open!")
            elif command_list[1] == "door":
                if unlock_door == 1:
                    print("You open the door.")
                    status=1
                else:
                    print("It's locked.")
            elif command_list[1] == "hairpin" and look_hairpin:
                print("You don't see that.")
            elif command_list[1] == "board" and look_board:
                print("You don't see that.")
            elif command_list[1] == "hammer" and hammer:
                print("You don't see that.")
            elif command_list[1] == "glasses" and glasses:
                print("You don't see that.")
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                print("You can't open that!")
            else:
                print("You don't see that.")
        elif command_list[0]=="pry":
            if command_list[1]=="board":
                if pry_board==0:
                    if look_board==0:
                        print("You don't see that.")
                    elif command_list[-1]=="hammer":
                        if hammer==0:
                            print("You don't have a hammer.")
                        else:
                            print("You use the hammer to pry open the board. It takes some work, but with some blood and sweat, you mange to get it open.")
                            pry_board=1
                else:
                    print("It's already pried open.")
            elif command_list[1] == "hairpin" and look_hairpin:
                print("You don't see that.")
            elif command_list[1] == "board" and look_board:
                print("You don't see that.")
            elif command_list[1] == "hammer" and hammer:
                print("You don't see that.")
            elif command_list[1] == "glasses" and glasses:
                print("You don't see that.")
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                print("Don't be stupid! That won't work!")
            else:
                print("You don't see that.")
        elif command_list[0]=="wear":
            if command_list[1]=="glasses":
                if wear_glasses==0:
                    if glasses==0:
                        print("You don't have a glasses.")
                    else:
                        print("You are now wearing the glasses.")
                        wear_glasses=1
                else:
                    print("You are already wearing them!")
            else:
                print("You dont have a "+command_list[-1]+".")
        elif command_list[0]=="inventory":
            if hairpin==1:
                inventory = "a hairpin"
            if hammer==1:
                inventory = "a hairpin, a hammer"
            if glasses==1:
                inventory = "a hairpin, a hammer, a glasses"
            print("You are carrying:"+ inventory +".")
        if time==0:
            status=2
    def status(self):
        global status
        if status == 0:
            return "locked"
        elif status==2:
            return "died"
        else:
            return "escaped"
def main():
    room=EscapeRoom()
    room.start()
    while room.status()=="locked":
        command = input (">> ")
        output = room.command(command)
    if room.status()=="escaped":
        print("Congratulations! You escaped!")
    else:
        print("Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas...")
        print("Sorry. You died.")
if __name__=="__main__":
    main()
