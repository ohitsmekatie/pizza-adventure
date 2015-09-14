#hello. of course i knew you'd look at the code file, ya nerd. <3.

from os import system

pointinstory = 0
#this is the function i've defined for the baller ass border around the story points
def bordered(story):
	storyline = story.splitlines()
	width = max(len(s) for s in storyline)
	res = ["-" * width]
	for s in storyline:
		res.append("| " + (s + " " * width)[:width] + " |")
	res.append ("-" * width)
	return "\n".join(res)

#this is the function for quiting the damn thing if i didn't like your answer
def story_quit():
        quit()
#this is my function that increments the pointinstory variable by 1 each time so you don't repeat story plots when you type things like no, or ehhhhh
def increment_story():
    global pointinstory
    pointinstory = (pointinstory+1)

#i think everything else from this point is preeeetty straight forward. you are smart/probably understood all this anyway
#all the following functions are the prompts, storylines, etc.
def prompt_continue():
    var0 = raw_input("Winners never quit. Type yes to continue or no if you REALLY MEAN IT")
    if(var0 == "yes"):
        if(pointinstory == 0):
            story_line1()
        elif(pointinstory == 1):
            story_line2()
        elif(pointinstory == 2):
            story_line3()
        elif(pointinstory == 3):
            story_line4()
        elif(pointinstory == 4):
            story_line5()
    if(var0 == "no"):
        story_quit()
    if(var0 != "yes" and var0 != "no"):
        not_yesno()

def not_yesno():
    print bordered("The lady has decided to not type yes or no.\nI love you, but you gotta type yes or no.\nWhen we don't follow the rules people like Donald Trump happen.\nWhen people like D. Trump happen the world blows up.\n When the world blows up we have no where to live.\nWhen we have nowhere to live our bodies will blow up in space.")
    yesno = raw_input("Shall we try again? Type yes, no, or whatever you want honestly. I just don't really care")
    if(yesno == "yes"):
        if(pointinstory == 0):
            story_line1()
        elif(pointinstory == 1):
            story_line2()
        elif(pointinstory == 2):
            story_line3()
        elif(pointinstory == 3):
            story_line4()
        elif(pointinstory == 4):
            story_line5()
    if(yesno == "no"):
        if(pointinstory == 0):
            story_line1()
        elif(pointinstory == 1):
            story_line2()
        elif(pointinstory == 2):
            story_line3()
        elif(pointinstory == 3):
            story_line4()
        elif(pointinstory == 4):
            story_line5()
    if(yesno != "no" and yesno != "yes"):
        if(pointinstory == 0):
            story_line1()
        elif(pointinstory == 1):
            story_line2()
        elif(pointinstory == 2):
            story_line3()
        elif(pointinstory == 3):
            story_line4()
        elif(pointinstory == 4):
            story_line5()

def story_line1():
    increment_story()
    print bordered("You see something close to you on the ground.\nWhat is it even? It kind of looks like pizza.\nOh, hell yeah it is pizza!\nYou look at it for a few minutes trying to decide what to do.\nClearly it's trash pizza that has been there for days.")
    var1 = raw_input("Do you want to continue the game & eat this pizza?")
    if(var1 == "yes"):
        system('say -v whisper I knew you would eat it. You are a monster.')
        story_line2()
    if(var1 == "no"):
        system('say -v whispter Winners never quit, Alison')
        prompt_continue()
    if(var1 != "yes" and var1 != "no"):
        not_yesno()

def story_line2():
    increment_story()
    print bordered("Aight, you eat it.\nYou really think that shit is gonna blow up yo body but honestly...\n...you feel great!\nYour muscles start noticably growing.\nAnd it seems like your eyes can now shoot lasers.\nHoly shit.")
    var2 = raw_input("Will you use your powers for good\nor will you just type no and leave them behind?")
    if(var2 == "yes"):
        system('say -v pipe REJOICE! REJOICE REJOICE REJOICE. R E J O I C E. REJOICE!')
        story_line3()
    if(var2 == "no"):
        prompt_continue()
    if(var2 != "yes" and var2 != "no"):
        not_yesno()

def story_line3():
    increment_story()
    print bordered("Great. You are now a superhero.\nIt's seriously that easy.\nMakes ya wonder why you wouldn't eat trash pizza more, amirite?")
    var3 = raw_input("Do you want to stay in Jackson\nor just quit and be a non super hero'd loser?")
    if(var3 == "yes"):
        story_line4()
    if(var3 == "no"):
        prompt_continue()
    if(var3 != "yes" and var3 != "no"):
        not_yesno()

def story_line4():
    increment_story
    print bordered("I know. Jackson is so good.\nYou can't save the world without first saving your people.\nActually wait.\nI mean, you want to save Jackson. You really do.\nBut you also want to blow up Starbucks with your LASER EYES!.\nBoth of them. Even the one you didn't work for.")
    var4 = raw_input("Will you blow up Jackson Starbucks with your laser eyes or will you just leave?")
    if(var4 == "yes"):
        story_line5()
    if(var4 == "no"):
        story_line5()
    if(var4 != "yes" and var4 != "no"):
        not_yesno()

def story_line5():
    print bordered("Yes or no doesn't matter.\nThis is my program and you're gonna blow dat shit up.\nYou are not a terrible person.\nYou first call in a bomb threat to the store.\nAt least this means you won't hurt a human.\nOnce everyone leaves the store you hit dat shit from all sides.\nPOW POW PEW PEW PEW POW BAM PEW BAM POW POW")
    var5 = raw_input("Are you statisfied?")
    if(var5 == "yes"):
        system('say -v zarvox one of us. one of us. one of us.')
        end_story()
    if(var5 == "no"):
        end_story()
    if(var5 != "yes" and var5 != "no"):
        end_story()

def end_story():
    print bordered("You might feel bad.\nYou really might and i'm sorry for that.\nTBH, there are a million other Starbies in the world.\nIf it makes you feel better...\nAll your friends that work at Starbucks have now been transferred\nIt's a new better version of Starbucks\nA new & better coffee shop that pays them more\nand doesn't treat them like shit.\nYAY!\nThis is the end!")

#now that i've defined my million functions because i don't really understand loops... here's where the story begins
print bordered("Hello Friend.\nI have made this thing for you because I love you very much.\nPlease don't judge my weak skills.\n\n\nSome things to note:\nTURN YO VOLUME WAY UP\nYou can choose yes, no or whatever the fuck you want.\nThat is all")
print "\n\n...And so the story begins\n\n"

story_line1()
