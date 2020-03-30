
formating = "=================================================================================================================="
wyd = "What do you do?"
again = "Insert your answer again: "


print("Welcome to my text based game (DAY 2 DLC NOW AVAILABLE)")
print("#alfa 2.0")
print("#-bug fixes")
print("#-DAY 2 DLC (unfinished)")
print("%s" % formating)
name = input("Insert your character name: ")

def youlose():
    print("_GAME OVER_")
    reply = input("(restart, quit game): ")
    if reply == "restart":
        game()
    elif reply == "quit game":
        quit()
    else:
        youlose()

def game():
    print("%s" % formating)
    print("You wake up to loud music. Your neighbours are having a party but you have to go to work early in the morning")
    reply = input("%s (check time, go to computer): " % wyd)
    if reply == "check time":
        print("It's 2:17")
        game1()
    elif reply == "go to computer":
        game2()
    else:
        print("%s" % again)
        game()

def game1():
    print("%s" % formating)
    print("'Should i just try to go back to sleep?'")
    reply = input("%s (go to sleep, go to computer): " % wyd)
    if reply == "go to sleep":
        game()
    elif reply == "go to computer":
        game2()
    else:
        print("%s" % again)
        game1()

def game2():
    print("%s" % formating)
    print("You are sitting in front of your computer. It's turned off.")
    reply = input("%s (turn pc on, go back to bed): " % wyd)
    if reply == "turn pc on":
        game3()
    elif reply == "go back to bed":
        game()
    else:
        print("%s" % again)
        game2()

def game3():
    print("%s" % formating)
    print("you are on your desktop")
    reply = input("%s (go to youtube, start hacking): " % wyd)
    if reply == "go to youtube":
        game4()
    elif reply == "start hacking":
        game5()
    else:
        print("%s" % again)
        game3()

def game4():
    print("%s" % formating)
    print("You fell into the youtube hole and were there all night.")
    youlose()

def game5():
    print("%s" % formating)
    print("You hacked into your neghbours wifi")
    reply = input("%s (kick them off, ddos wifi): " % wyd)
    if reply == "kick them off":
        game6()
    elif reply == "ddos wifi":
        game7()
    else:
        print("%s" % again)
        game5()

def game6():
    print("%s" % formating)
    print("You kicked them off the wifi. It's quiet for a bit but they reconnect and music starts blasting again")
    reply = input("%s (ddos wifi, go to bed): " % wyd)
    if reply == "ddos wifi":
        game7()
    elif reply == "go to bed":
        game()
    else:
        print("%s" % again)
        game6()

def game7():
    print("%s" % formating)
    print("You DDoS-ed your neighbours wifi. You know that it is illegal but atleast you get to sleep now!")
    reply = input("%s (go to bed, stay up): " % wyd)
    if reply == "go to bed":
        game8()
    elif reply == "stay up":
        game4()
    else:
        print("%s" % again)
        game7()

def game8():
    print("%s" % formating)
    print("Sleep tight!")
    reply = input("%s (quit game, day 2): " % wyd)
    if reply == "quit game":
        quit()
    elif reply == "day 2":
        game9()
    else:
        print("%s" % again)
        game8()

def game9():
    print("%s" % formating)
    print("You wake up")
    reply = input("%s (look at time, go back to sleep): " % wyd)
    if reply == "look at time":
        game10()
    elif reply == "go back to sleep":
        game11()
    else:
        print("%s" % again)
        game9()

def game10():
    print("%s" % formating)
    print("The time is 7:50. You know your alarm is gonna go off at 8:00")
    reply = input("%s (keep sleeping, wake up): " % wyd)
    if reply == "keep sleeping":
        game11()
    elif reply == "wake up":
        game12()
    else:
        print("%s" % again)
        game10()

def game11():
    print("%s" % formating)
    print("Your alarm woke you up. It's 8am")
    reply = input("%s (get ready, call in sick): " % wyd)
    if reply == "get ready":
        game12()
    elif reply == "call in sick":
        game13()
    else:
        print("%s" % again)
        game11()

def game12():
    print("%s" % formating)
    print("You woke up and got ready for work.")
    reply = input("%s (go to work, go to pc): " % wyd)
    if reply == "go to work":
        game14()
    elif reply == "go to pc":
        game15()
    else:
        print("%s" % again)
        game12()

def game13():
    print("%s" % formating)
    print("You called in sick and didnt go to work.")
    reply = input("%s (go to pc, keep sleeping): " % wyd)
    if reply == "go to pc":
        game16()
    elif reply == "keep sleeping":
        game17()
    else:
        print("%s" % again)
        game13()

def game14():
    print("%s" % formating)
    print("You arrive at the office")
    reply = input("%s (go work, talk to co-worker): " % wyd)
    if reply == "go work":
        game18()
    elif reply == "talk to co-worker":
        game19()
    else:
        print("%s" % again)
        game14()

def game15():
    print("%s" % formating)
    print("You are on your pc for a while and then go to work.")
    game14()

def game16():
    print("%s" % formating)
    print("You are on your desktop")
    reply = input("%s (go to internet, start a project): " % wyd)
    if reply == "go to internet":
        game20()
    elif reply == "start a project":
        game21()
    else:
        print("%s" % again)
        game16()

def game17():
    print("%s" % formating)
    print("You wake up to a bright flash and a loud bang")
    reply = input("%s (go investigate, grab your gun): " % wyd)
    if reply == "go investigate":
        game22()
    elif reply == "grab your gun":
        game23()
    else:
        print("%s" % again)
        game17()

def game18():
    print("%s" % formating)
    print("You work for a while but all of a sudden the police is there to arrest you")
    reply = input("%s (try to run, give up): " % wyd)
    if reply == "try to run":
        game24()
    elif reply == "give up":
        game25()
    else:
        print("%s" % again)
        game18()

def game19():
    print("%s" % formating)
    print("Your co-worker tells you that the police is looking for you")
    reply = input("%s (run, go work): ")
    if reply == "run":
        game26()
    elif reply == "go work":
        game18()
    else:
        print("%s" % again)
        game19()

def game20():
    print("%s" % formating)
    print("You find out you are wanted for hacking")
    reply = input("%s (investigate further, run away): " % wyd)
    if reply == "investigate further":
        game27()
    elif reply == "run away":
        game30()
    else:
        print("%s" % again)
        game20()

def game21():
    print("%s" % formating)
    print("You start a new project but its interrupted by a bright flash and a loud bang, the police is raiding your home and arrests you")
    youlose()

def game22():
    print("%s" % formating)
    print("It's the polce, they arrest you for hacking")
    youlose()

def game23():
    print("%s" % formating)
    print("You grab your gun and investigate. It's the police, they see your gun and you are shot to death")
    youlose()

def game24():
    print("%s" % formating)
    print("It's too late, they arrest you")
    youlose()

def game25():
    print("%s" % formating)
    print("They arrest you")
    youlose()

def game26():
    print("%s" % formating)
    print("You run away from work and see that the police is entering the office. You barely get out.")
    reply = input("%s (run home, run to friend): " % wyd)
    if reply == "run home":
        game29()
    elif reply == "run to friend":
        game30()
    else:
        print("%s" % again)
        game26()

def game27():
    print("%s" % formating)
    print("While investigating you hear a SWAT truck pull up")
    reply = input("%s (give up, run): " % wyd)
    if reply == "give up":
        game25()
    elif reply == "run":
        game30()
    else:
        print("%s" % again)
        game27()

def game29():
    print("%s" % formating)
    print("You find that police has already raided your home")
    reply = input("%s (run to friend, go to police): " % wyd)
    if reply == "run to friend":
        game30()
    elif reply == "go to police":
        game25()
    else:
        print("%s" % again)
        game29()

def game30():
    print("%s" % formating)
    print("you ran to your friend and tell him the story. He lets you stay in his basement with all his hacking equipment.")
    reply = input("%s (go to pc, go to sleep): " % wyd)
    if reply == "go to pc":
        game31()
    elif reply == "go to sleep":
        game32()
    else:
        print("%s"% again)
        game30()

def game31():
    print("%s" % formating)
    print("You are sitting in front of your friends pc. It's turned off")
    reply = input("%s (turn pc on, go to sleep): " % wyd)
    if reply == "turn pc on":
        game33()
    elif reply == "go to sleep":
        game32()
    else:
        print("%s" % again)
        game31()

def game32():
    print("%s" % formating)
    print("You wake up to the police raiding your friends house. They haven't made it to the basement yet.")
    reply = input("%s (hide, run): " % wyd)
    if reoly == "hide":
        game34()
    elif reply == "run":
        game35()
    else:
        print("%s" % again)
        game32()

def game33():
    print("%s" % formating)
    print("You are on the desktop.")
    reply = input("%s (go to internet, start hacking): " % wyd)
    if reply == "go to internet":
        game36()
    elif reply == "start hacking":
        game37()
    else:
        print("%s" % again)
        game33()

def game34():
    print("%s" % formating)
    print("You hide under the stairs and find a secret passage.")
    reply = input("%s (go in, stay there): " % wyd)
    if reply == "go in":
        game38()
    elif reply == "stay there":
        game39()
    else:
        print("%s" % again)
        game34()

def game35():
    print("%s" % formating)
    print("You sneak out the basement window and run away. The police sees you and starts chasing you.")
    reply = input("%s (keep running, give up): " % wyd)
    if reply == "keep running":
        game40()
    elif reply == "give up":
        game25()
    else:
        print("%s" % again)
        game35()

def game36():
    print("%s" % formating)
    print("You find out that your neighbour who you DDoS-ed is working for the police")
    reply = input("%s (investigate further, start hacking): " % wyd)
    if reply == "investigate further":
        game41()
    elif reply == "start hacking":
        game37()
    else:
        print("%s" % again)
        game36()



    






game()


#alfa release 2.0
#Copyright Kevin Piip