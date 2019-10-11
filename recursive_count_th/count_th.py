'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    substring = "th"
    if word.find(substring) == -1: 
        print(count) 
    else:
        left_index = word.find(substring)
        left_index += 2
        count += 1
        
        count_th(word[left_index:]) 
    print(count)


text = "ththtthththh"
count_th(text)