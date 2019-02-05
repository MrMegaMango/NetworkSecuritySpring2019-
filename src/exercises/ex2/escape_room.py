import random
class EscapeRoom:
    def start(self):
        global time,code,comma_digit_list,look_glasses,glasses,look_hairpin,hairpin,look_board,mirror,look_hammer,hammer,glasses,unlock_chest,user_code,unlock_door,open_chest,pry_board,wear_glasses,inventory,status
        time=100
        code=random.randint(0,9999)
        code_string=str(code)
        while len(code_string)<4:
            code_string='0'+code_string
        code_string=list(set(code_string))  #to remove duplicates
        comma_digit_list=",".join(sorted(code_string))
        glasses, look_hairpin, hairpin, look_board, mirror, look_hammer, hammer, look_glasses, glasses, unlock_chest, user_code, unlock_door,open_chest,pry_board,wear_glasses,status = (0,)*16
        inventory=""
    def command(self, command_string):
        global time,code,comma_digit_list,glasses,look_hairpin,hairpin,look_board,mirror,look_hammer,hammer,look_glasses,glasses,unlock_chest,user_code,unlock_door,open_chest,pry_board,wear_glasses,inventory,status
        time=time-1
        command_list=command_string.split(' ')
        if command_list[0] == "look":
            if len(command_list)==1:
                return "You are in a locked room. There is only one door and it has a numeric keypad. Above the door is a clock that reads " + str(time) + ". Across from the door is a large mirror. Below the mirror is an old chest. The room is old and musty and the floor is creaky and warped."
            elif command_list[1] == "door":
                if wear_glasses == 0:
                    return "The door is strong and highly secured. The door is locked and requires a 4-digit code to open."
                else:
                    return "The door is strong and highly secured. The door is locked and requires a 4-digit code to open. But now you're wearing these glasses you notice something! There are smudges on the digits "+comma_digit_list+"."
            elif command_list[1] == "mirror":
                if look_hairpin == 0:
                    look_hairpin = 1
                    return "You look in the mirror and see yourself... wait, there's a hairpin in your hair. Where did that come from?"
                else:
                    return "You look in the mirror and see yourself."
            elif command_list[1] == "chest":
                return "An old chest. It looks worn, but it's still sturdy."
            elif command_list[1] == "floor":
                look_board=1
                return "The floor makes you nervous. It feels like it could fall in. One of the boards is loose."
            elif command_list[1] == "board":
                if look_board == 0:
                    return "You don't see that here."
                elif pry_board == 0:
                    look_board=1 #might not be needed
                    return "The board is loose, but won't come up when you pull on it. Maybe if you pried it open with something."
                else:
                    return "The board has been pulled open. You can look inside."
            elif command_list[1] == "hairpin":
                if mirror == 0:
                    return "You don't see that here."
                else:
                    return "You see nothing special"
            elif command_list[1] == "hammer":
                if hammer == 0:
                    return "You don't see that here."
                else:
                    return "You see nothing special."
            elif command_list[1] == "glasses":
                if glasses == 0:
                    return "You don't see that here."
                else:
                    return "These look like spy glasses. Maybe they reveal a clue!"
            elif command_list[1] == "clock":
                return "You see nothing special."
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
                    return "You can't look in that!"
                if item:
                    item=" a "+item
                return "Inside the "+command_list[2]+" you see:"+item+"."
            else:
                return "You don't see that here."
        elif command_list[0]=="get":
            if len(command_list)==2:
                if command_list[1]=="hairpin":
                    if hairpin==0:
                        if look_hairpin==0:
                            return "You don't see that."
                        else:
                            hairpin=1
                            return "You got it."
                    else:
                        return "You already have that."
                elif command_list[1]=="board":
                    if look_board == 0:
                        return "You don't see that."
                    else:
                        return "You can't get that."
                elif command_list[1] in ["door","clock","mirror","chest","floor"]:
                    return "You can't get that."
                elif command_list[1]=="hammer":
                    if hammer == 1:
                        return "You already have that."
                elif command_list[1]=="glasses":
                    if glasses == 1:
                        return "You already have that."
                else:
                    return "You don't see that."
            else:
                if command_list[1]=="hammer":
                    if hammer==0:
                        if command_list[-1]=="chest":
                            if open_chest==0:
                                return "It's not open."
                            else:
                                hammer=1
                                return "You got it."
                    else:
                        return "You don't see that."
                elif command_list[1]=="glasses":
                    if glasses==0:
                        if command_list[-1]=="board":
                            if pry_board==0: #pry board, not open board
                                return "It's not open."
                            else:
                                glasses=1
                                return "You got it."
                    else:
                        return "You don't see that."
                elif command_list[-1] not in ["chest","board"]: #does not in work?
                    return "You can't get something out of that!"
                else: #only thing left is "anything else from chest or board"
                    return "You don't see that."
        elif command_list[0]=="unlock":
            if command_list[1]=="chest":
                if unlock_chest==1:
                    return "It's already unlocked."
                elif command_list[3]=="hairpin":
                    if hairpin==1:
                        unlock_chest=1
                        return "You hear a click! It worked!"
                    else:
                        return "Go get a hairpin first."
                else:
                    return "You don't have a " + command_list[-1] +"." # fixed
            elif command_list[1]=="door":
                if unlock_door==0:
                    user_code=command_list[-1]
                    if user_code.isdigit():
                        if int(user_code)==code:
                            unlock_door=1
                            return "You hear a click! It worked!"
                        elif len(str(user_code))<4:
                            return "The code must be 4 digits."
                        else:
                            return "That's not the right code!"
                else:
                    return "It's already unlocked."
            elif command_list[1] == "hairpin" and look_hairpin:
                return "You don't see that here."
            elif command_list[1] == "board" and look_board:
                return "You don't see that here."
            elif command_list[1] == "hammer" and hammer:
                return "You don't see that here."
            elif command_list[1] == "glasses" and glasses:
                return "You don't see that here."
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                return "You can't unlock that!"
            else:
                return "You don't see that here."
        elif command_list[0]=="open":
            if command_list[1] == "chest":
                if open_chest==0:
                    if unlock_chest==0:
                        return "It's locked."
                    else:
                        open_chest=1
                        return "You open the chest."

                else:
                    return "It's already open!"
            elif command_list[1] == "door":
                if unlock_door == 1:
                    status=1
                    return "You open the door."
                else:
                    return "It's locked."
            elif command_list[1] == "hairpin" and look_hairpin:
                return "You don't see that."
            elif command_list[1] == "board" and look_board:
                return "You don't see that."
            elif command_list[1] == "hammer" and hammer:
                return "You don't see that."
            elif command_list[1] == "glasses" and glasses:
                return "You don't see that."
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                return "You can't open that!"
            else:
                return "You don't see that."
        elif command_list[0]=="pry":
            if command_list[1]=="board":
                if pry_board==0:
                    if look_board==0:
                        return "You don't see that."
                    elif command_list[-1]=="hammer":
                        if hammer==0:
                            return "You don't have a hammer."
                        else:
                            pry_board=1
                            return "You use the hammer to pry open the board. It takes some work, but with some blood and sweat, you manage to get it open."

                else:
                    return "It's already pried open."
            elif command_list[1] == "hairpin" and look_hairpin:
                return "You don't see that."
            elif command_list[1] == "board" and look_board:
                return "You don't see that."
            elif command_list[1] == "hammer" and hammer:
                return "You don't see that."
            elif command_list[1] == "glasses" and glasses:
                return "You don't see that."
            elif command_list[1] in ["clock","mirror","hairpin","floor","board","hammer","glasses"]:
                return "Don't be stupid! That won't work!"
            else:
                return "You don't see that."
        elif command_list[0]=="wear":
            if command_list[1]=="glasses":
                if wear_glasses==0:
                    if glasses==0:
                        return "You don't have a glasses."
                    else:
                        wear_glasses=1
                        return "You are now wearing the glasses."
                else:
                    return "You are already wearing them!"
            else:
                return "You dont have a "+command_list[-1]+"."
        elif command_list[0]=="inventory":
            if hairpin==1:
                inventory = "a hairpin"
            if hammer==1:
                inventory = "a hairpin, a hammer"
            if glasses==1:
                inventory = "a hairpin, a hammer, a glasses"
            return "You are carrying:"+ inventory +"."
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
        return "Congratulations! You escaped!"
    else:
        return "Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died."
if __name__=="__main__":
    main()
