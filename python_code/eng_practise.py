'''
    English practise, randomised
    
    #! FOR VISUAL STUDIO CODE EDITOR

    Author: WattoX00
    Date:   02/10/2023
'''

'''
Txt format:
word[nation] /word[foring];
'''
import tkinter as tk
from tkinter import filedialog
import random
import time

#* File opening
def open_file():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])
    if file_path:
        practise(file_path)

def practise(file_path):
    start_time = time.time()
    try:
        with open(file_path, "r", encoding='UTF-8') as f:
            read = f.read()
    except FileNotFoundError:
        print("\nFile not found.\n")
        return
    counter: int = int()
    point: int = int()
    max_: int = int()
    no_num: list = []
    split_read = read.split("\n")
    for _ in split_read:
        max_ += 1
    while counter != max_:
        rand = random.randint(0, max_ - 1)
        if rand not in no_num:
            read_line = split_read[rand]
            words = read_line.split("/")
            word = ''.join(str(words[1]).split(';'))
            try:
                operation = input('\033[0m' + str(words[0]) + "- ")
            except KeyboardInterrupt:
                print("\nProgram closed\n")
                quit()
            if operation == word:
                print('\033[32m', word)
                point += 1
            else:
                print('\033[31m', word)
            counter += 1
        no_num.append(rand)
    percentage = round((point / counter) * 100,1)
    print("\n"+str(point)+ "/"+ str(counter), "\t", str(percentage) + "%/100%\n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes_time = elapsed_time / 60
    if minutes_time < 1:
        print(round(elapsed_time, 2), "seconds.")
    else:
        print(round(minutes_time, 2), "minutes.")
    root.destroy()
#* Window
root = tk.Tk()
root.title("English practise!")
open_file()
root.mainloop()