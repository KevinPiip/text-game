import time

formating = "=================================================================================================================="
wyd = "What do you do?"
again = "Insert your answer again: "

#===========================================================================================================================================

def menu1():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                                                             |")
    print("|             > [1] ________________ Tutorial                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [2] ________________ New Game                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [3] ________________ Quit game                |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [4] ________________ Release notes            |")
    print("|                                                             |")
    print("|                                                             |")
    print("===============================================================")
    wasd = input()
    if wasd == "s":
        menu2()
    elif wasd == "w":
        menu4()
    elif wasd == "d":
        tutorial()
    else:
        menu1()


def menu2():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [1] ________________ Tutorial                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|             > [2] ________________ New Game                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [3] ________________ Quit game                |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [4] ________________ Release notes            |")
    print("|                                                             |")
    print("|                                                             |")
    print("===============================================================")
    wasd = input()
    if wasd == "w":
        menu1()
    elif wasd == "s":
        menu3()
    elif wasd == "d":
        game()
    else:
        menu2()


def menu3():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [1] ________________ Tutorial                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [2] ________________ New Game                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|             > [3] ________________ Quit game                |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [4] ________________ Release notes            |")
    print("|                                                             |")
    print("|                                                             |")
    print("===============================================================")
    wasd = input()
    if wasd == "w":
        menu2()
    elif wasd == "s":
        menu4()
    elif wasd == "d":
        quit()
    else:
        menu3()

def menu4():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [1] ________________ Tutorial                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [2] ________________ New Game                 |")
    print("|                                                             |")
    print("|                                                             |")
    print("|               [3] ________________ Quit game                |")
    print("|                                                             |")
    print("|                                                             |")
    print("|             > [4] ________________ Release notes            |")
    print("|                                                             |")
    print("|                                                             |")
    print("===============================================================")
    wasd = input()
    if wasd == "w":
        menu3()
    elif wasd == "s":
        menu1()
    elif wasd == "d":
        relnotes()
    else:
        quit()


def relnotes():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                        # ALFA 7.0                           |")
    print("|                                                             |")
    print("|                  #-Quit confirmation added                  |")
    print("|                                                             |")
    print("|                      #-New menu system                      |")
    print("|                                                             |")
    print("|                    #-Quit game anywhere                     |")
    print("|                                                             |")
    print("|                         #-Tutorial                          |")
    print("|                                                             |")
    print("|                     #-Time delays added                     |")
    print("|                                                             |")
    print("|                                                             |")
    print("===============================================================")
    wasd = input()
    if wasd == "a":
        menu4()
    else:
        relnotes()


def tutorial():
    print("===============================================================")
    print("|   use W to go up, S to go down, D to select, A to go back   |")
    print("|                                                             |")
    print("|                     This is the tutorial                    |")
    print("|              In the game you are given 2 choises            |")
    print("|  To choose press the number in front of the text and enter  |")
    print("|               [1] - gives you the first choise              |")
    print("|               [2] - gives you the second choise             |")
    print("|        You can type whenever you see 'What do you do?'      |")
    print("|  If you accidentally type something else you will see this  |")
    print("|               text 'Insert your answer again: '             |")
    print("|              You can then type your answer again            |")
    print("|                  Each day is a checkpoint                   |")
    print("|   you can fast quit the game whenever you want by typing    |")
    print("|                         'quit game'                         |")
    print("|   it doesnt ask for confirmation and all progress is lost   |")
    print("===============================================================")
    wasd = input()
    if wasd == "a":
        menu1()
    #elif wasd == "s":
    #    tutorial2()
    else:
        tutorial()

#===========================================================================================================================================

def rusure2():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        youlose()
    else:
        print("%s" % again)
        rusure2()

def rusure3():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        youlose2()
    else:
        print("%s" % again)
        rusure3()

def rusure4():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        game8()
    else:
        print("%s" % again)
        rusure4()

def rusure5():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        game44()
    else:
        print("%s" % again)
        rusure5()

def rusure6():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        game45()
    else:
        print("%s" % again)
        rusure6()

def rusure7():
    print("%s" % formating)
    print("Are you sure you wanna quit? progress wont be saved!")
    time.sleep(2)
    print("[1] Yes")
    print("[2] No")
    reply = input(": ")
    if reply == "1":
        quit()
    elif reply == "2":
        menu1()
    else:
        print("%s" % again)
        rusure7()

#===========================================================================================================================================

def youlose():
    print("_GAME OVER_")
    time.sleep(2)
    print("[1] Restart game")
    print("[2] Quit game")
    reply = input(": ")
    if reply == "1":
        game()
    elif reply == "2":
        rusure2()
    else:
        youlose()

def youlose2():
    print("_GAME OVER_")
    time.sleep(2)
    print("[1] Restart to last checkpoint")
    print("[2] Quit game")
    reply = input(": ")
    if reply == "1":
        game8()
    elif reply == "2":
        rusure3()
    else:
        youlose2()

#===========================================================================================================================================

def game():
    print("%s" % formating)
    print("You wake up to loud music. Your neighbours are having a party but you have to go to work early in the morning")
    time.sleep(2)
    print("[1] Check time")
    print("[2] Go to computer")
    reply = input("%s: " % wyd)
    if reply == "1":
        game1()
    elif reply == "2":
        game2()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game()

def game1():
    print("%s" % formating)
    print("The time is 2:17. 'Should i just try to go back to sleep?'")
    time.sleep(2)
    print("[1] Go back to sleep")
    print("[2] Go to your computer")
    reply = input("%s: " % wyd)
    if reply == "1":
        game()
    elif reply == "2":
        game2()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game1()

def game2():
    print("%s" % formating)
    print("You are sitting in front of your computer. It's turned off.")
    time.sleep(2)
    print("[1] Turn your computer on")
    print("[2] Go back to bed")
    reply = input("%s: " % wyd)
    if reply == "1":
        game3()
    elif reply == "2":
        game()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game2()

def game3():
    print("%s" % formating)
    print("you are on your desktop")
    time.sleep(2)
    print("[1] Go watch YouTube videos")
    print("[2] Start hacking into your neighbours wifi")
    reply = input("%s: " % wyd)
    if reply == "1":
        game4()
    elif reply == "2":
        game5()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game3()

def game4():
    print("%s" % formating)
    print("You fell into the youtube hole and were there all night.")
    time.sleep(2)
    youlose()

def game5():
    print("%s" % formating)
    print("You hacked into your neghbours wifi")
    time.sleep(2)
    print("[1] Kick them off the wifi")
    print("[2] DDoS their wifi")
    reply = input("%s: " % wyd)
    if reply == "1":
        game6()
    elif reply == "2":
        game7()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game5()

def game6():
    print("%s" % formating)
    print("You kicked them off the wifi. It's quiet for a bit but they reconnect and music starts blasting again")
    time.sleep(2)
    print("[1] DDoS their wifi")
    print("[2] Go back to bed and try to sleep")
    reply = input("%s: " % wyd)
    if reply == "1":
        game7()
    elif reply == "2":
        game()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game6()

def game7():
    print("%s" % formating)
    print("You DDoS-ed your neighbours wifi. You know that it is illegal but atleast you get to sleep now!")
    time.sleep(2)
    print("[1] Go have your sleep now")
    print("[2] Stay up and watch some YouTube videos")
    reply = input("%s: " % wyd)
    if reply == "1":
        game8()
    elif reply == "2":
        game4()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game7()

def game8():
    print("%s" % formating)
    print("Sleep tight! (CHECKPOINT)")
    time.sleep(2)
    print("[1] Quit game (Your game isn't saved)")
    print("[2] Continue to day 2")
    print("[3] Save game")
    reply = input("%s: " % wyd)
    if reply == "1":
        rusure4()
    elif reply == "2":
        game9()
    elif reply == "3":
        print("this feature isn't available")
        game8()
    else:
        print("%s" % again)
        game8()

#===========================================================================================================================================

def game9():
    print("%s" % formating)
    print("You wake up")
    time.sleep(2)
    print("[1] Look at the time")
    print("[2] Go back to sleep")
    reply = input("%s: " % wyd)
    if reply == "1":
        game10()
    elif reply == "2":
        game11()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game9()

def game10():
    print("%s" % formating)
    print("The time is 7:50. You know your alarm is gonna go off at 8:00")
    time.sleep(2)
    print("[1] Keep sleeping, you still have some time before the alarm")
    print("[2] Wake up and get ready for work")
    reply = input("%s: " % wyd)
    if reply == "1":
        game11()
    elif reply == "2":
        game12()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game10()

def game11():
    print("%s" % formating)
    print("Your alarm woke you up. It's 8am")
    time.sleep(2)
    print("[1] Get ready for work")
    print("[2] Call in sick for work")
    reply = input("%s: " % wyd)
    if reply == "1":
        game12()
    elif reply == "2":
        game13()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game11()

def game12():
    print("%s" % formating)
    print("You woke up and got ready for work.")
    time.sleep(2)
    print("[1] Go to work now")
    print("[2] Go fuck around on your pc before going to work")
    reply = input("%s: " % wyd)
    if reply == "1":
        game14()
    elif reply == "2":
        game15()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game12()

def game13():
    print("%s" % formating)
    print("You called in sick and didnt go to work.")
    time.sleep(2)
    print("[1] Go to your pc")
    print("[2] Go back to bed and keep sleeping")
    reply = input("%s: " % wyd)
    if reply == "1":
        game16()
    elif reply == "2":
        game17()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game13()

def game14():
    print("%s" % formating)
    print("You arrive at the office")
    time.sleep(2)
    print("[1] Go to your office and start working")
    print("[2] Socialise with your co-worker")
    reply = input("%s: " % wyd)
    if reply == "1":
        game18()
    elif reply == "2":
        game19()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game14()

def game15():
    print("%s" % formating)
    print("You are on your pc for a while and then go to work.")
    time.sleep(2)
    game14()

def game16():
    print("%s" % formating)
    print("You are on your desktop")
    time.sleep(2)
    print("[1] Go to the internet")
    print("[2] Start a new project")
    reply = input("%s: " % wyd)
    if reply == "1":
        game20()
    elif reply == "2":
        game21()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game16()

def game17():
    print("%s" % formating)
    print("You wake up to a bright flash and a loud bang")
    time.sleep(2)
    print("[1] Go investigate what the hell that was")
    print("[2] Grab your gun, what if their robbers")
    reply = input("%s: " % wyd)
    if reply == "1":
        game22()
    elif reply == "2":
        game23()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game17()

def game18():
    print("%s" % formating)
    print("You work for a while but all of a sudden the police is there to arrest you")
    time.sleep(2)
    print("[1] Try to run away")
    print("[2] Give up")
    reply = input("%s: " % wyd)
    if reply == "1":
        game24()
    elif reply == "2":
        game25()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game18()

def game19():
    print("%s" % formating)
    print("Your co-worker tells you that the police is looking for you")
    time.sleep(2)
    print("[1] Run away")
    print("[2] Don't give a fuck about it and go to work")
    reply = input("%s: " % wyd)
    if reply == "1":
        game26()
    elif reply == "2":
        game18()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game19()

def game20():
    print("%s" % formating)
    print("You find out you are wanted for hacking")
    time.sleep(2)
    print("[1] Investigate further")
    print("[2] Run away")
    reply = input("%s: " % wyd)
    if reply == "1":
        game27()
    elif reply == "2":
        game30()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game20()

def game21():
    print("%s" % formating)
    print("You start a new project but its interrupted by a bright flash and a loud bang, the police is raiding your home and arrests you")
    time.sleep(2)
    youlose2()

def game22():
    print("%s" % formating)
    print("It's the polce, they arrest you for hacking")
    time.sleep(2)
    youlose2()

def game23():
    print("%s" % formating)
    print("You grab your gun and investigate. It's the police, they see your gun and you are shot to death")
    time.sleep(2)
    youlose2()

def game24():
    print("%s" % formating)
    print("It's too late, they arrest you")
    time.sleep(2)
    youlose2()

def game25():
    print("%s" % formating)
    print("They arrest you")
    time.sleep(2)
    youlose2()

def game26():
    print("%s" % formating)
    print("You run away from work and see that the police is entering the office. You barely get out.")
    time.sleep(2)
    print("[1] Run home")
    print("[2] Run to your friend")
    reply = input("%s: " % wyd)
    if reply == "1":
        game29()
    elif reply == "2":
        game30()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game26()

def game27():
    print("%s" % formating)
    print("While investigating you hear a SWAT truck pull up")
    time.sleep(2)
    print("[1] There's nothing you can do. Just go to the door and give up")
    print("[2] Run away through the window")
    reply = input("%s: " % wyd)
    if reply == "1":
        game25()
    elif reply == "2":
        game30()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game27()

def game29():
    print("%s" % formating)
    print("You find that police has already raided your home")
    time.sleep(2)
    print("[1] Run to your friends house")
    print("[2] Theres no point in running. Go to the police station and give yourself up")
    reply = input("%s: " % wyd)
    if reply == "1":
        game30()
    elif reply == "2":
        game25()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game29()

def game30():
    print("%s" % formating)
    print("you ran to your friend and tell him the story. He lets you stay in his basement with all his hacking equipment.")
    time.sleep(2)
    print("[1] Go to his pc and start figuring out why the police is after you")
    print("[2] Go sleep on the couch")
    reply = input("%s: " % wyd)
    if reply == "1":
        game31()
    elif reply == "2":
        game32()
    elif reply == "quit game":
        quit()
    else:
        print("%s"% again)
        game30()

def game31():
    print("%s" % formating)
    print("You are sitting in front of your friends pc. It's turned off")
    time.sleep(2)
    print("[1] Turn on the computer")
    print("[2] Go sleep on the couch")
    reply = input("%s: " % wyd)
    if reply == "1":
        game33()
    elif reply == "2":
        game32()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game31()

def game32():
    print("%s" % formating)
    print("You wake up to the police raiding your friends house. They haven't made it to the basement yet.")
    time.sleep(2)
    print("[1] Hide somewhere")
    print("[2] Run through the window")
    reply = input("%s: " % wyd)
    if reply == "1":
        game34()
    elif reply == "2":
        game35()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game32()

def game33():
    print("%s" % formating)
    print("You are on the desktop.")
    time.sleep(2)
    print("[1] Go to the internet")
    print("[2] Start hacking")
    reply = input("%s: " % wyd)
    if reply == "1":
        game36()
    elif reply == "2":
        game37()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game33()

def game34():
    print("%s" % formating)
    print("You hide under the stairs and find a secret passage.")
    time.sleep(2)
    print("[1] Go in there")
    print("[2] Stay under the stairs")
    reply = input("%s: " % wyd)
    if reply == "1":
        game38()
    elif reply == "2":
        game39()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game34()

def game35():
    print("%s" % formating)
    print("You sneak out the basement window and run away. The police sees you and starts chasing you.")
    time.sleep(2)
    print("[1] Keep running")
    print("[2] Give up")
    reply = input("%s: " % wyd)
    if reply == "1":
        game40()
    elif reply == "2":
        game25()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game35()

def game36():
    print("%s" % formating)
    print("You find out that your neighbour who you DDoS-ed is working for the police")
    time.sleep(2)
    print("[1] Keep investigating")
    print("[2] Start hacking him")
    reply = input("%s: " % wyd)
    if reply == "1":
        game41()
    elif reply == "2":
        game37()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game36()

def game37():
    print("%s" % formating)
    print("You hack into your neigbours security system and find out he's working for the FBI")
    time.sleep(2)
    print("[1] Investigate it further")
    print("[2] This is fucked, I should give up")
    reply = input("%s: " % wyd)
    if reply == "1":
        game41()
    elif reply == "2":
        game41()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game37()

def game38():
    print("%s" % formating)
    print("The passage leads to a dark room that smells really gross. You dont know whats going on there and the floor is wet. You find a light switch")
    time.sleep(2)
    print("[1] Click the light switch")
    print("[2] Don't click the light switch")
    reply = input("%s: " % wyd)
    if reply == "1":
        game44()
    elif reply == "2":
        game45()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game38()

def game39():
    print("%s" % formating)
    print("The police finds you really fast. its embarrassing. You piss yourself. The polise shoots you on the spot cos your such a loser. GO FUCK URSELF")
    time.sleep(2)
    youlose2()

def game40():
    print("%s" % formating)
    print("You try to run but you're a fat cunt and the police catches up to you in 10 seconds.")
    time.sleep(2)
    youlose2()

def game41():
    print("%s" % formating)
    print("The police is now raiding your friends house")
    time.sleep(2)
    print("[1] Give up")
    print("[2] Hide somewhere")
    reply = input("%s: " % wyd)
    if reply == "1":
        game25()
    elif reply == "2":
        game34()
    elif reply == "quit game":
        quit()
    else:
        print("%s" % again)
        game41()

def game44():
    print("%s" % formating)
    print("The lights come on. The floor is full of blood and you see a girl tied to a table with a camera pointed at her. You pass out")
    time.sleep(2)
    print("[1] Quit game")
    print("[2] Save game")
    print("[3] Day 3")
    reply = input("%s: ")
    if reply == "1":
        rusure5()
    elif reply == "2":
        print("This feature isn't available")
        game44()
    elif reply == "3":
        print("Day 3 is not available at this moment!")
        game44()
    else:
        print("%s" % again)
        game44()

def game45():
    print("%s" % formating)
    print("You dont know where you are and cant see a thing. you get disorianted and fall down somewhere and get knocked out.")
    time.sleep(2)
    print("[1] Quit game (the game wont be saved)")
    print("[2] Save game")
    print("[3] Day 3 (not out yet)")
    reply = input("%s: " % wyd)
    if reply == "1":
        rusure6()
    elif reply == "2":
        print("This feature isn't available")
        game45()
    elif reply == "3":
        print("Day 3 is not available at this moment!")
        game45()
    else:
        print("%s" % again)
        game45()








    




#===========================================================================================================================================


menu1()


#alfa release 6.3
#Copyright Kevin Piip