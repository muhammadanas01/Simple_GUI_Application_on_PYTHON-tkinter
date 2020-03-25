import tkinter as tk
from tkinter import ttk
import os
import csv  #use to write or edit or delete csv file


# main window
win = tk.Tk()
win.title('GUI application by @anas')


# widgets labels and buttons imported by ttk lib
# labels
name_label = ttk.Label(win, text = 'Enter Your Name: ')
name_label.grid(row=0, column=0 , sticky = tk.W)   
#sticky is used to aligned my variable ab same position here W= west

age_label = ttk.Label(win, text = 'Enter Your Age: ')
age_label.grid(row=1, column=0, sticky = tk.W )

email_label = ttk.Label(win, text = 'Enter Your e-mail: ')
email_label.grid(row=2, column=0, sticky = tk.W)

gender_label = ttk.Label(win, text = 'Select Your Gender: ')
gender_label.grid(row=3, column=0, sticky = tk.W)



# Boxes to enter name using Entry mod
name_var = tk.StringVar()   #to store data from the box
name_entrybox = ttk.Entry(win, width = 16, textvariable = name_var)   
#textvariable means that box give entered value to assigned variable
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()   #focus is used to locate cursor position at name box everytime user run application


age_var = tk.StringVar()   #to store data from the box
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=1,column=1)


email_var = tk.StringVar()  #to store data from the box
email_entrybox = ttk.Entry(win, width=16, textvariable= email_var)
email_entrybox.grid(row=2, column =1)




# MAKING COMBOBOX to select from given values ---- like  male or female
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width = 14, textvariable=gender_var, state= 'readonly')  
#state is readonly means that user not enter his own value he/she select among given options
gender_combobox['values'] = ('Male', 'Female' , 'Others')   #['values']  = ('') are mandatory
gender_combobox.current(0)     #current is used to select the the value by default -- at 0 index it's 'Male'
gender_combobox.grid(row=3,column = 1)


# Radio button  
user_type = tk.StringVar()

radio_button1 = ttk.Radiobutton(win, text= "Student", value = 'Student', variable= user_type)  
#this time we use variable instead of textvariable because we just have to select the value and value='Student' is assing Student in variable
radio_button1.grid(row=4, column=0)

radio_button2 = ttk.Radiobutton(win, text= "Teacher", value = 'Teacher', variable= user_type)  
radio_button2.grid(row=4,column = 1)


# Check Button
check_btn_var = tk.IntVar()
check_button1 = ttk.Checkbutton(win, text= 'Check If You Like this Program', variable =check_btn_var)
check_button1.grid(row=5, columnspan= 3)  # we use columnspan instead of colum because this time it does bad to UI


# # Button making


# #adding all given data in txt file
# def action():
#     #these two line are not necessary these are just used to print data on console/terminal
#     print(f'Name : {name_var.get()} is {age_var.get()} years and e-mail is {email_var.get()}')
#     if check_btn_var.get() == 0:
#         print(f'Gender: {gender_var.get()} Type: {user_type.get()} Liked it: No')
#     else:
#         print(f'Gender: {gender_var.get()} Type: {user_type.get()} Liked it: Yes')

#     with open('Python/GUI.txt', 'a') as rf:    #open a file in append mode, type your path here where you want to make a file if you're windows user type open(r'Python\GUI.txt') like that otherwise there will be error
#         rf.write(f'Name : {name_var.get()} is {age_var.get()} years and e-mail is {email_var.get()}\n'
#         f'Gender: {gender_var.get()} Type: {user_type.get()} Liked it: No\n') # this line iss used to write a line in tour file

#     name_entrybox.delete(0, tk.END)  # it is used to delete the written data after you submit it from(0 to END) 
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)
    

# submit_button = ttk.Button(win, text = 'SUBMIT', command = action,)
# submit_button.grid(row=6, column=1)



#adding all given data in csv file
def action():
    #these two line are not necessary these are just used to print data on console/terminal
    print(f'Name : {name_var.get()} is {age_var.get()} years and e-mail is {email_var.get()}')
    if check_btn_var.get() == 0:
        liked = 'No'
    else:
        liked = 'Yes'
    print(f'Gender: {gender_var.get()} Type: {user_type.get()} Liked it: {liked}')

# Code Change from here
    with open('Python/GUI.csv', 'a') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['UserName','Age','E-mail','Gender','Type','Liked'])
        
        if os.stat('Python/GUI.csv').st_size==0:  #this if statement write header only one time in your csv file
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName': name_var.get(),
            'Age' : age_var.get(),
            'E-mail': email_var.get(),
            'Gender': gender_var.get(),
            'Type': user_type.get(),
            'Liked' : liked, 
        })
    
    name_entrybox.delete(0, tk.END)  # it is used to delete the written data after you submit it from(0 to END) 
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    

submit_button = ttk.Button(win, text = 'SUBMIT', command = action,)
submit_button.grid(row=6, column=1)

#main loop for running window continuously
win.mainloop()
