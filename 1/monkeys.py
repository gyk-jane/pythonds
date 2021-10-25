# SELF CHECK
# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

import random
import string
from difflib import SequenceMatcher

def generateString(length):
    """Generates a string that is n characters long by choosing random letters from the 26 letters in the alphabet plus the space.
    
    Args:
        Length of string    
    
    Returns:
        A string of random characters.
    """
    ALPHABET = string.ascii_lowercase
    ALPHABET_SPACE = ALPHABET + " "
    
    count = 0
    result = ""
    while (count < length):
        result += random.choice(ALPHABET_SPACE)
        count += 1
    
    return result

def scoreString(randomStr, goalStr):
    """Scores each generated string by comparing the randomly generated string (from randomsString()) to the goal ("methinks it is like a weasel")
    
    Args: 
        randomStr: A randomly selected 28-character string made up of letters from the alphabet plus the space
        
        goalStr: The goal string we are comparing the random string to.
        
    Returns:
        A boolean. True if randomStr equals the goal string.
    """
    return randomStr == goalStr

def callString(randomStr, goalStr, length):
    """Repeatedly calls generate and score functions and ends if 100% of the randomly generated letters are correct. If letters are not correct, then generate a whole new string. Prints the best string generated so far and its score every 1000 tries.
    
    Args:
        Refer to scoreString args.
        
    Returns: 
        A string output of how many tries it took to get the goal string and/or a string output indicating the best score every 1000 tries.
    """
    count = 0
    prevScore = -1
    prevStr = ''
    highScore = -1
    highScoreDict = dict()
    while (not(scoreString(randomStr, goalStr))):
        score = 0
        for i,j in zip(randomStr, goalStr):
            if i == j:
                score += 1
        score = score/len(goalStr)
        
        # Determine highest score so far
        if (prevScore >= highScore):
            highScore = prevScore
            highScoreDict = {
                'randomStr': prevStr,
                'score': highScore,
                'attemptNum': count-1
            }
        prevScore = score
        prevStr = randomStr
        
        if (not(count == 0) and count%10000 == 0):
            # Print update
            scoreUpdate = "The best string so far out of {count} attempts is attempt number {attemptNum}: {randomStr}, with a score of {score}.".format(count=count, attemptNum=highScoreDict['attemptNum'], randomStr=highScoreDict['randomStr'], score=highScoreDict['score'])
            print(scoreUpdate)
            
        else: 
            randomStr = generateString(length)
        
        count += 1
            
    print("\n")
    print ("FINALLY! It took {count} attempts to get the goal string, {goalStr}.".format(count=count, goalStr=goalStr))
    
callString(generateString(4), "four", 4)