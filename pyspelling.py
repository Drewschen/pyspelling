import os
from os import path
import multiprocessing
from pickle import TRUE
from playsound import playsound
import random
from colorama import Fore, Style, Back
import time
from collections import namedtuple
import json
import typing as typ

<<<<<<< HEAD

class Score:
	def __init__(self, word, result):
		self.word = word
		self.result = result

class ScoreBoard:
	scores = []

	def appendScore(self, score):
		self.scores.append(score)
		print(self.scores[0].word)

	def getScores():
		return self.scores

	def getLastScore():
		return self.scores[len(self.scores)]


def main():
	Entry = namedtuple('PastResult','word points')
	entry = Entry("Fish",1)

	myScoreboard1 = ScoreBoard()
	myScoreboard1.appendScore(entry)

	print(myScoreboard1.getLastScore.word)

#	myScoreBoard = ScoreBoard()
#
#	myScoreBoard.appendScore(Score("That", 1))
#	myScoreBoard.appendScore(Score("This", 0))
#
#	print (myScoreBoard.getScores)
#
#	print(myScoreBoard.getLastScore.word)





#def main():
#	os.system('clear')
#	wordFilePath = "resources/words/"
#	soundsFilePath = "resources/sounds/"
#	files = (os.listdir(wordFilePath))
#	random.shuffle(files)
#	score = 0
#	question = 0
#	questions = 10
#	result = 0
#	myfiles = files[0:questions]
#	userName = input("Enter your Name: ")
#	print("Hello: " + userName)
#	for x in range(len(myfiles)):
#		start = time.time()
#		myWord = myfiles[question].split(".")[0]
#		wordSound = multiprocessing.Process(target=playsound, args=(wordFilePath+files[question],))
#		wordSound.start()
#		string = input("Question " + str(question+1) + ": Please spell the word: ")
#		if(len(string)>0):
#			if string == myWord:
#				result = 1
#				print(Fore.GREEN + "Well done!" + Style.RESET_ALL)
#				playsound(soundsFilePath+"correct.m4a")
#			else:
#				result = 0
#				print(Fore.RED + "Wrong answer" + Style.RESET_ALL)
#				playsound(soundsFilePath+"wrong.m4a")
#				print("This word is spelt: " + '\033[1m' + myWord + '\033[0m')
#				print("Please repeat the word 3 times")
#				for y in range(0,3):
#					while string!=myWord:
#						string = input("Attempt " + str(y + 1) + ": ")
#					string = None
#			wordSound.terminate()
#			stop = time.time()
#			score+=calculateScore(myWord,stop-start,result)
#			saveResult(userName,myWord,result)
#			question+=1
#	print(Back.CYAN + Fore.RED + "Your score is " + str(score) + Style.RESET_ALL)
#	saveScore(userName,round((10*score)/questions))
#	displayLeaderBoard()
#
#def saveResult(iName, iWord, iResult):
#	resultsPath = "save/"
#	resultsFile = iName + ".txt"
#	iFile = open(resultsPath + resultsFile,"r")
#	records = iFile.read().split('\n')
#	workingRecords = []
#	Entry = namedtuple('PastResult','word points')
#	for x in records:
#		pair = x.split(':')
#		if(len(pair[0])>0):
#			entry = Entry(pair[0],int(pair[1]))
#			workingRecords.append(entry)
#	oFile = open(resultsPath + resultsFile,"a")
#	oFile.write(iWord + ":" + str(iResult) + '\n')
#	oFile.close()
#
#def saveScore(userName,score):
#	f = open("score.txt","a")
#	f.write(userName + ':' + str(score) + '\n')
#	f.close()
#
#def displayLeaderBoard():
#	f = open("score.txt","r")
#	records = f.read().split('\n')
#	leaderBoard = []
#	Entry = namedtuple('Player','name score')
#	print("\n--- Leader Board ---")
#	for x in records:
#		pair = x.split(':')
#		if (len(pair[0])>0):
#			entry = Entry(pair[0],int(pair[1]))
#			leaderBoard.append(entry)
#	leaderBoard.sort(key=lambda x: getattr(x, 'score'),reverse = True)
#	topFivePlayers = leaderBoard[:5]
#	for idx, x in enumerate(topFivePlayers):
#		print(str(idx + 1) + "\t" + x.name + "\t" + str(x.score))
#
#def calculateScore(word,time,result):
#	return round(100*((len(word)/time)*result))
=======

def main():
    os.system('clear')
    titlePage()
    soundsFilePath = "resources/sounds/"
    wordFilePath = "resources/words/"
    score = 0
    question = 0
    questions = 10
    result = 0
    resultsList = [''] * questions
    myFiles = getFileList(wordFilePath)[0:questions]
    Entry = namedtuple('result', 'word score')
    userName = input("Enter your Name: ")
    print("Hello: " + userName)
    userAge = input("Enter your Age: ")
    repeat = False
    myResults = loadResults(userName)
    while question < questions:
        start = time.time()
        myWord = myFiles[question].split(".")[0]
        wordSound = multiprocessing.Process(
            target=playsound, args=(wordFilePath+myFiles[question],))
        wordSound.start()
        string = input("Question " + str(question+1) +
                       ": Please spell the word (enter r to repeat): ")
        repeat = False
        if(len(string) > 0):
            if string.lower() == 'r':
                repeat = True
            else:
                if string.lower() == myWord.lower():
                    result = 1
                    print(Fore.GREEN + "Well done!" + Style.RESET_ALL)
                    playsound(soundsFilePath+"correct.m4a")
                else:
                    result = 0
                    print(Fore.RED + "Wrong answer" + Style.RESET_ALL)
                    playsound(soundsFilePath+"wrong.m4a")
                    print("This word is spelt: " +
                          '\033[1m' + myWord + '\033[0m')
                    print("Please repeat the word 3 times")
                    for y in range(0, 3):
                        while string != myWord:
                            string = input("Attempt " + str(y + 1) + ": ")
                        string = None
                resultsList[question] = result

                i = 0
                print('|', end='')
                while i < len(resultsList):
                    match resultsList[i]:
                        case 0: print(Fore.RED + '-', end='')
                        case 1: print(Fore.GREEN + '+', end='')
                        case _: print(' ', end='')
                    print(Style.RESET_ALL, end='')
                    i += 1
                print('|')

            wordSound.terminate()
            stop = time.time()
            if not repeat:
                score += calculateScore(myWord, stop-start, result)
                myResults = appendToList(myResults, Entry(myWord, result))
                question += 1
    print(Back.CYAN + Fore.RED + "Your score is " + str(score) + Style.RESET_ALL)
    saveResult(userName, myResults)
    saveScore(userName, round((10*score)/questions))
    displayLeaderBoard()


def loadResults(iPlayerName):
    resultPathFile = "save/" + iPlayerName + ".txt"
    scores = []
    if path.exists(resultPathFile):
        iFile = open(resultPathFile, "r")
        records = iFile.read().split('\n')
        Entry = namedtuple('result', 'word score')
        for x in records:
            pair = x.split(':')
            if (len(pair[0]) > 0):
                entry = Entry(pair[0], int(pair[1]))
                scores.append(entry)
    return scores


def appendToList(iTupleList, iTuple):
    listPointer = 0
    myTuple = iTuple
    myTupleList = iTupleList
    newScore = 0
    myElement = None
    for idx, i in enumerate(myTupleList):
        if i.word == myTuple.word:
            newScore = i.score + int(myTuple.score)
            myElement = idx
    if myElement == None:
        pass
    else:
        myTupleList.pop(myElement)
    NewTuple = namedtuple('result', 'word score')
    myNewTuple = NewTuple(myTuple.word, newScore)
    myTupleList.append(myNewTuple)
    return myTupleList


def saveResult(iPlayerName, iResults):
    resultsPathFile = "save/" + iPlayerName + ".txt"
    oFile = open(resultsPathFile, "w")
    for x in iResults:
        if(len(x.word) > 0):
            oFile.write(x.word + ":" + str(x.score) + '\n')
    oFile.close()


def saveScore(userName, score):
    f = open("score.txt", "a")
    f.write(userName + ':' + str(score) + '\n')
    f.close()


def displayLeaderBoard():
    f = open("score.txt", "r")
    records = f.read().split('\n')
    leaderBoard = []
    Entry = namedtuple('Player', 'name score')
    print("\n--- Leader Board ---")
    for x in records:
        pair = x.split(':')
        if (len(pair[0]) > 0):
            entry = Entry(pair[0], int(pair[1]))
            leaderBoard.append(entry)
    leaderBoard.sort(key=lambda x: getattr(x, 'score'), reverse=True)
    topFivePlayers = leaderBoard[:5]
    for idx, x in enumerate(topFivePlayers):
        print(str(idx + 1) + "\t" + x.name + "\t" + str(x.score))


def calculateScore(word, time, result):
    return round(100*((len(word)/time)*result))


def getFileList(path):
    rawFiles = (os.listdir(path))
    files = []
    validFileTypes = [".m4a", ".mp3"]
    for x in rawFiles:
        for y in validFileTypes:
            if y in x:
                files.append(x)
    random.shuffle(files)
    return files


def titlePage():
    print("  ---------      |          --------    \\                /  |--------   |-----\\")
    print(" /         \\     |              |        \\              /   |           |      |")
    print("|           |    |              |         \\            /    |           |      |")
    print("|           |    |              |          \\          /     |           |      |")
    print("|           |    |              |           \\        /      |------     |-----/")
    print("|           |    |              |            \\      /       |           |  \\")
    print("|           |    |              |             \\    /        |           |   \\")
    print(" \\         /     |              |              \\  /         |           |    \\")
    print("  ---------      \\--------   --------           \\/          |---------  |     \\")

>>>>>>> 35e3c5a63101c90cbfabc6d6371366a61fc3f462

if __name__ == '__main__':
    main()
    print("Done")
