import os
from os import path
import multiprocessing
from playsound import playsound
import random
from colorama import Fore, Style, Back
import time
from collections import namedtuple
import json
import typing as typ


def main():
	os.system('clear')
	soundsFilePath = "resources/sounds/"
	wordFilePath = "resources/words/"
	score = 0
	question = 0
	questions = 2
	result = 0
	myFiles = getFileList(wordFilePath)[0:questions]
	Entry = namedtuple('result','word score')
	userName = input("Enter your Name: ")
	print("Hello: " + userName)
	myResults = loadResults(userName)
	for x in range(len(myFiles)):
		start = time.time()
		myWord = myFiles[question].split(".")[0]
		wordSound = multiprocessing.Process(target=playsound, args=(wordFilePath+myFiles[question],))
		wordSound.start()
		string = input("Question " + str(question+1) + ": Please spell the word: ")
		if(len(string)>0):
			if string.lower() == myWord.lower():
				result = 1
				print(Fore.GREEN + "Well done!" + Style.RESET_ALL)
				playsound(soundsFilePath+"correct.m4a")
			else:
				result = 0
				print(Fore.RED + "Wrong answer" + Style.RESET_ALL)
				playsound(soundsFilePath+"wrong.m4a")
				print("This word is spelt: " + '\033[1m' + myWord + '\033[0m')
				print("Please repeat the word 3 times")
				for y in range(0,3):
					while string!=myWord:
						string = input("Attempt " + str(y + 1) + ": ")
					string = None
			wordSound.terminate()
			stop = time.time()
			score+=calculateScore(myWord,stop-start,result)
			myResults=appendToList(myResults,Entry(myWord,result))
			question+=1
	print(Back.CYAN + Fore.RED + "Your score is " + str(score) + Style.RESET_ALL)
	print(myResults)
	saveResult(userName,myResults)
	saveScore(userName,round((10*score)/questions))
	displayLeaderBoard()

def loadResults(iPlayerName):
	resultPathFile = "save/" + iPlayerName + ".txt"
	scores = []
	if path.exists(resultPathFile):
		iFile = open(resultPathFile,"r")
		records = iFile.read().split('\n')
		Entry = namedtuple('result','word score')
		for x in records:
			pair = x.split(':')
			if (len(pair[0])>0):
				entry = Entry(pair[0],int(pair[1]))
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
	NewTuple = namedtuple('result','word score')
	myNewTuple = NewTuple(myTuple.word,newScore)
	myTupleList.append(myNewTuple)
	return myTupleList

def saveResult(iPlayerName, iResults):
	resultsPathFile = "save/" + iPlayerName + ".txt"
	oFile = open(resultsPathFile,"w")
	print(iResults)
	for x in iResults:
		if(len(x.word)>0):
			oFile.write(x.word + ":" + str(x.score) + '\n')
	oFile.close()

def saveScore(userName,score):
	f = open("score.txt","a")
	f.write(userName + ':' + str(score) + '\n')
	f.close()

def displayLeaderBoard():
	f = open("score.txt","r")
	records = f.read().split('\n')
	leaderBoard = []
	Entry = namedtuple('Player','name score')
	print("\n--- Leader Board ---")
	for x in records:
		pair = x.split(':')
		if (len(pair[0])>0):
			entry = Entry(pair[0],int(pair[1]))
			leaderBoard.append(entry)
	leaderBoard.sort(key=lambda x: getattr(x, 'score'),reverse = True)
	topFivePlayers = leaderBoard[:5]
	for idx, x in enumerate(topFivePlayers):
		print(str(idx + 1) + "\t" + x.name + "\t" + str(x.score))

def calculateScore(word,time,result):
	return round(100*((len(word)/time)*result))

def getFileList(path):
	rawFiles = (os.listdir(path))
	files = []
	validFileTypes = [".m4a",".mp3"]
	for x in rawFiles:
		for y in validFileTypes:
			if y in x:
				files.append(x)
	random.shuffle(files)
	return files

if __name__ == '__main__':
    main()
    print("Done")