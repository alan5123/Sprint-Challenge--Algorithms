'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
         # there can't be a match cuz we are looking for 2 letters   
    if len(word) < 2:
        return 0
    if word[0] + word[1] == "th":
         # recursively call the list excluding the last two, makes the array smaller
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])