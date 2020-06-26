import shutil
import os
import time
import subprocess
import platform

def Read():
    path=input("Enter the file path to read it: ")
    file=open(path,"r")
    print(file.read())
    input("Press enter...")
    file.close()

def Write():
    path=input("Enter the path of the file to write or create: ")
    if os.path.isfile(path):
        print("Rebuilding the existing file...")
    else:
        print("Creating the new file...")
    text=input("Enter text: ")
    file=open(path,"w")
    file.write(text)

def Add():
    path=input("Enter the file path: ")
    text=input("Enter the text to add: ")
    file=open(path,"a")
    file.write('\n'+text)

def Delete():
    path=input("Enter the path of the file for deletion: ")
    if os.path.exists(path):
        print("File Found!")
        os.remove(path)
        print("File Deleted!")
    else:
        print("File Not Found!")

def Dirlist():
    path=input("Enter the directory path to display: ")
    sortlist=sorted(os.listdir(path))
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

def Check():
    fp=int(input("Check existence of \n1. File \n2. Directory\n"))
    if fp==1:
        path=input("Enter the file path: ")
        os.path.isfile(path)

    if os.pth.isfile(path)==True:
        print("File Found!")
    else:
        print("File Not Found!")
    if fp==2:
        path=input("Enter the directory path: ")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print("Directory Found!")
        else:
            print("Directory Not Found!")

def Move():
    path1=input("Enter the source path of the file to move: ")
    path2=input("Enter the destination path and file name: ")
    shutil.move(path1,path2)
    print("File Moved!")

def Rename():
    path1=input("Enter the source path of the file to rename: ")
    path2=input("Enter the destination path and new file name: ")
    shutil.move(path1,path2)
    print("File Renamed!")

def Copy():
    path1=input("Enter the path of the file to copy: ")
    path2=input("Enter the path to copy to: ")
    shutil.copy(path1,path2)
    print("File Copied!")

def Makedir():
    path=input("Enter path of directory to make \nExamples: \nWindows: C:\\Hello\\Newdir \nLinux/macOS: /home/hello/Newdir \nEnter here: ")
    os.makedirs(path)
    print("Directory Created!")

def Removedir():
        path=input("Enter the path of the directory for removal: ")
        treedir=int(input("1. Delete directory \n2. Delete directory tree \n3. Exit \n"))
        if treedir==1:
            os.rmdir(path)
        if treedir==2:
            shutil.rmtree(path)
            print("Directory Deleted!")
        if treedir==3:
            exit()

def Openfile():
    path=input("Enter the path of the program: ")
    try:
        os.startfile(path)
    except:
        print("File Not Found!")

run=1
while run==1:
    try:
        os.system("clear")
    except OSError:
        os.system("cls")
    print("\n>>>>>>>>>> Helios Compass 0.1 <<<<<<<<<<\n")
    platform.platform()
    print("The current date and time is: ",time.asctime())
    print(" ")
    print("Please choose an option number: \n")

    dec=int(input("""1. Read a file
2. Write to a file
3. Append text to the end of a file
4. Delete a file
5. List files in a directory
6. Check file existance
7. Move a file
8. Copy a file
9. Rename a file
10. Create a directory
11. Delete a directory
12. Open a program
13. Exit

"""))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Rename()
    if dec==10:
        Makedir()
    if dec==11:
        Removedir()
    if dec==12:
        Openfile()
    if dec==13:
        exit()
    run=int(input("1. Return to menu\n2. Exit \n"))
    if run==2:
        exit()
