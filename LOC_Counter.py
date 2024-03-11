from customtkinter import *
import glob

win=CTk()
win.title("Code Counter")
win.geometry("500x450")
win.resizable(0,0)
set_default_color_theme("green")

def count_code(dir_path):
    dir_path=dir_path+"\**\*.*"
    total_lines=0
    for file_path in glob.glob(dir_path, recursive=True):
        file_path=file_path.replace("\\","\\\\")

        file=open(file_path,'r')
        lines_count=len(file.readlines())
        total_lines+=lines_count
        file.close()
    
    return total_lines

def submit_button():
    lines=count_code(entry.get())
    label.configure(text=f"{lines}")


def set_Appearance(choice):
    if(choice=="Dark"):
        set_appearance_mode("dark")

    elif(choice=="Light"):
        set_appearance_mode("light")

    else:
        set_appearance_mode("system")

frame=CTkFrame(win,width=450,height=100)
frame.grid(row=0,column=0,padx=25,pady=20)

label=CTkLabel(frame,text="",font=("Arial",55),height=98,width=448)
label.pack()

entry = CTkEntry(win,placeholder_text="Enter Path of the directory",height=50,width=450)
entry.grid(row=1,column=0, padx=25,pady=10)

button=CTkButton(win,text="Submit",command=submit_button)
button.grid(row=2,column=0)

optionmenu_var =StringVar(value="Dark")
optionmenu = CTkOptionMenu(win, values=["Dark", "Light","System"],variable=optionmenu_var,command=set_Appearance)
optionmenu.set("Appearance Mode")
optionmenu.grid(row=3,column=0,sticky="SW",padx=25,pady=150)


win.mainloop()
