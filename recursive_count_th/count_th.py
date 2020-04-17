'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    #Look at what is being tested.  Where are instances of "th" located?
    # 2/3 tested words start with "th"
    if word.startswith("th"):
        count = 1  # Count "th" as 1 instance
    #How do we account for the tested word that has "th" in the middle?
    #Slice?
    if len(word) > 2:
        return count_th(word[1: len(word)]) + count
    else:
        return count
    
    

#"word" is just a parameter.
#Can't use a loop
#What is the base case?  How do we get the function to stop counting?
#Stop after word.lenth is reached
#Look at what is being tested.  Where are instances of "th" located?
# 2/3 tested words start with "th"
#Count "th" as 1 instance
#How do we account for the tested word that has "th" in the middle?
#if word contains "th" return total += count
#If 

