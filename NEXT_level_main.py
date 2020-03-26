# IF YOU ARE BEGINNER OR USING PYTHON FIRST TIME READ main.py FILE IN SAME REPOSITORY 

import tkinter as tk
from tkinter import ttk
import os
import csv

# main window
win = tk.Tk()
win.title("GUI Application by @anas")

# Labels
# make list of my labels that are used in this code
labels = ['Enter Your Name: ','Enter Your Age: ','Enter Your e-mail: ','Select Your Gender']

# this time we use loop to create our all labels in one time without repeat our code
for label in range(len(labels)):    
    current_label = 'label' + str(label)  # label is integer value because we call len(labels)
    current_label = ttk.Label(win, text=labels[label])
    current_label.grid(row=label, column = 0)



# EntryBOXes
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'e-mail': tk.StringVar(),
    # 'gender': gender_var,
}

counter = 0
for i in user_info:
    current_entrybox = 'entry' + i # it's work like------- entryname----- entryage
    current_entrybox = ttk.Entry(win, width= 16, textvariable = user_info[i])
    current_entrybox.grid(row=counter, column = 1)
    counter +=1



# Combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width = 14, textvariable=gender_var, state= 'readonly') 
gender_combobox['values'] = ('Male', 'Female' , 'Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column = 1) 
user_info['gender'] = gender_var


# Radio button  
user_type = tk.StringVar()

radio_button1 = ttk.Radiobutton(win, text= "Student", value = 'Student', variable= user_type)  
#this time we use variable instead of textvariable because we just have to select the value and value='Student' is assing Student in variable
radio_button1.grid(row=5, column=0)

radio_button2 = ttk.Radiobutton(win, text= "Teacher", value = 'Teacher', variable= user_type)  
radio_button2.grid(row=5,column = 1)

user_info['usertype'] = user_type



# Button
def action():
    # print(user_info['name'].get())
    # print(user_info['age'].get())
    # print(user_info['e-mail'].get())
    # print(user_info['gender'].get())
    for item in user_info:
        print(user_info[item].get())

    with open('Python/GUI2.csv', 'a') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['UserName','Age','E-mail','Gender','Type','Liked'])
        
        if os.stat('Python/GUI.csv').st_size==0:  #this if statement write header only one time in your csv file
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName': user_info['name'].get(),
            'Age' : user_info['age'].get(),
            'E-mail': user_info['e-mail'].get(),
            'Gender': user_info['gender'].get(),
            'Type': user_info['usertype'].get(),
        })
    
    for i in user_info:
        current_entrybox.delete(0, tk.END)
        current_entrybox.delete(0, tk.END)
        current_entrybox.delete(0, tk.END)





submit_button = ttk.Button(win, text='SUBMIT', command = action)
submit_button.grid(row = counter+3, columnspan=2)

# mainloop
win.mainloop()
