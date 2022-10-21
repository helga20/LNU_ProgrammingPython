'''def longestWord(words):
    finalList = []    
    for word in words:
        finalList.append((len(word), word))   
    finalList.sort()     
    print("The word with the longest length is:", finalList[-1][1],
          " and length is ", len(finalList[-1][1]))

def shortestWord(words):
    fList = []    
    for word in words:
        fList.append((len(word), word))   
    fList.sort(reverse=True)     
    print("The word with the shortest length is:", fList[-1][1],
          " and length is ", len(fList[-1][1]))
print("Enter words:")
list_word = list(map(str, input().split()))
longestWord(list_word)
shortestWord(list_word)'''

'''def longestWord(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) > max1):
            max1 = len(i)
            temp = i
    print("The word with the longest length is:", temp,
          " and length is ", max1)

def shortestWord(a):
    min1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) < min1):
            min1 = len(i)
            temp = i
    print("The word with the shortest length is:", temp,
          " and length is ", min1)

print("Enter words:")
list_word = list(map(str, input().split()))
longestWord(list_word)
shortestWord(list_word)'''


'''def longestWord(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) > max1):
            max1 = len(i)
            temp = i
    print("The word with the longest length is:", temp,
          " and length is ", max1)

def shortestWord(a):
    min1 = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) < min1):
            min1 = len(i)
            temp = i
    print("The word with the shortest length is:", temp,
          " and length is ", min1)

print("Enter words:")
list_word = list(map(str, input().split()))
longestWord(list_word)
shortestWord(list_word)
'''

'''def name_surname(n_s):
    name_list = n_s.split()
    initsialy = ""
    for i in range(len(name_list)):
        n_s = name_list[i]
        initsialy += (n_s[0].upper() + '.')     
    return initsialy 

entered = input('Please Enter your name and surname: \n')
names = entered.split()
print(name_surname(entered))  '''


'''words = input('Please, enter words: \n')
first_word = words[:words.find(' ')]
second_word = words[words.find(' ') + 1:]
print(second_word + ' ' + first_word)'''



'''def word_func(word):
    word_list = word.split()
    empty = ''
    for i in range(len(word_list)):
        word = word_list[i]
        empty += (word[0].upper() + word[1:-1] + word[-1].upper() + '-')
    return empty
    
words = 'my favourite language is python'
print(word_func(words))'''


'''def func(word):
    for n in word:
        if n.isdigit() == False:
           word = word.replace(n, " ")
    my_list = word.split(' ')
    print(my_list)
    longest = 0 
    for item in range(len(my_list)):
        if len(my_list[item]) > longest:
            longest = len(my_list[item])
    return longest
     

name  = "n3lr99l00000ldfw8fd8sd890sf0s980sf0sd889890s"
term = "name"

print(func(name))'''

#print("талон" * 1000)


import turtle
import math

def xt(t):
    return 16 * math.sin(t) ** 3
def yt(t):
    return 13 * math.cos(t) - 5 \
           * math.cos(2 * t) - 2 * \
           math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(800)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()