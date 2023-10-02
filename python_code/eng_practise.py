'''
    English practise, randomised
    
    #! FOR VISUAL STUDIO CODE EDITOR

    Author: WattoX00
    Date:   01/01/2023
'''

'''
Txt format:
word[nation] /word[foring];
...

'''
import random
#* paste the path of the .txt file between the r""
f = open(r"","r", encoding="UTF-8")
#* variables
counter = 0
point=0
max_=0
list_file = []
no_num = []

#* read the txt file
read = f.read()
#* split the txt file into a big list
split_read = read.split("\n")
#* find the last element of the list
for i in split_read:
    max_+=1
    
while counter != max_:
    #* random number
    rand = random.randint(0,max_-1)
    #* if there was line that we use before, restart the loop (counter+=0)
    if rand in no_num:
        pass
    else:
        #* split the list into "lines"
        read_line = split_read[rand]
        #* clearing the format that required
        words = read_line.split("/")
        word = ''.join(str(words[1]).split(';'))
        #* words[0] - hun 
        operation = str(input('\033[0m'+str(words[0])+"- "))
        #* checks if the input is equal to the solution
        if operation == word:
            #* adding color green
            #! only works in Visual Studio Code
            print('\033[32m',word)
            point+=1
        else:
            #* adding color red
            #! only works in Visual Studio Code
            print('\033[31m',word)
        #* adding +1 to the counter
        counter+=1
    #* now appending the rand to the no_num lsit
    no_num.append(rand)
#* calculating the percentages
percentage = (point/counter)*100
print(point,"/",counter,"\n",str(percentage)+"/100%")