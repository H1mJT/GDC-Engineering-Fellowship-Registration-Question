import sys, operator, os.path

#Get output sorted by priority
def sorted_dic():
    lines={}
    file=open("task.txt")
    for line in file:
        pieces=line.split(" ",1)  
        lines[pieces[1].strip("\n")]=pieces[0]             #Stores the tasks and priority as key value pair in dict
    d=sorted(lines.items(), key=operator.itemgetter(1))    #Sorts the dict by priority
    file.close()
    return d

#Counts Number of lines in txt file
def count(x):
    file = open(x,"r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
      
    for i in CoList:
        if i:
            Counter += 1
    file.close()
    return Counter

#Help block
def help1():
    sys.stdout.buffer.write("Usage :-\n$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n$ ./task del INDEX            # Delete the incomplete item with the given index\n$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n$ ./task help                 # Show usage\n$ ./task report               # Statistics".encode('utf8'))

#Add task block
def add(x,y):
    #Checks if Priority input is integer.
    try :
        z=int(x)
    except:
        print("Priority must be an integer.")
        exit()

    x=str(x)
    y=str(y)
    #Checks if task.txt file exists, if exists it opens it else creates the file and opens it.
    try:
        f=open("task.txt", "a")
    except:
        fa= open("task.txt","w+")
        fa.close()
        f=open("task.txt","a")
    #Writes the task to text file and prints output.
    f.write(x+" "+y+"\n" )
    print('Added task: "'+y+'" with priority',x)
    f.close()

#List tasks block
def ls():
    c=os.path.exists("task.txt")
    if c== True:
        d=sorted_dic()
        i=0
        for word in d:    
            a=str(i+1)+". "+d[i][0]+ " ["+str(d[i][1])+"]\n"
            sys.stdout.buffer.write(a.encode('utf8'))
            i=i+1
        if i==0:
            print("There are no pending tasks!")
    else:
        print("There are no pending tasks!")

#del task block
def delete(z):
    try:
        z=int(z)
    except:
        print("Index must be an integer.")
        exit()
    c=os.path.exists("task.txt")
    if c== True:
        Counter=count("task.txt")
    else:
        print("There are no pending tasks! Nothing deleted.")
        exit()
    #Checks if the given index exists
    if z==0: print('Error: task with index #'+ str(z)+' does not exist. Nothing deleted.')
    elif Counter < z: print('Error: task with index #'+ str(z)+' does not exist. Nothing deleted.')
    else:
        d=sorted_dic()
        with open("task.txt", "r") as f:
            words = f.readlines()
        with open("task.txt", "w") as f:
            for word in words:
                wor=word.split(" ",1)
                wor=wor[1]
                if wor.strip("\n") != d[z-1][0]:                #Rewrites all the tasks in text file except for the task to be deleted. 
                    f.write(word)
        print("Deleted task #"+str(z))
    

#Done task block
def done(m):
    try:
        m=int(m)
    except:
        print("Index must be an integer.")
        exit()
    
    c=os.path.exists("task.txt")
    if c== True:
        Counter=count("task.txt")
    else:
        print("There are no pending tasks! Please add tasks before marking as done.")
        exit()
    #Checks if the given index exists
    if m==0: print('Error: no incomplete item with index #'+str(m)+' exists.')
    elif Counter < m:
        print('Error: no incomplete item with index #'+str(m)+' exists.')
    
    else:

        try:
            fs=open("completed.txt", "a")
        except:
            fg=open("completed.txt", "w+")
            fg.close()
            fs=open("completed.txt", "a")
        
        d=sorted_dic()
        with open("task.txt", "r") as f:
            words = f.readlines()
        with open("task.txt", "w") as f:
            for word in words:
                wor=word.split(" ",1)
                wor=wor[1]
                if wor.strip("\n") != d[m-1][0]:     #Rewrites all the tasks in task.txt file except for the task to be marked as done.
                    f.write(word)
                    
                else:                                #Writes the task to be done on completed.txt
                    
                    fs.write(wor)
        print("Marked item as done.")
            
    
#Report task block                    
def report():
    c=os.path.exists("task.txt")
    if c== True:
        Counter=count("task.txt")
    else:
        Counter=0
    b='Pending : '+str(Counter)+'\n'
    sys.stdout.buffer.write(b.encode('utf8'))
    
    if c== True:
        d=sorted_dic()
        i=0
        for word in d:    
            a=str(i+1)+". "+str(d[i][0])+" ["+ str(d[i][1])+ "]\n"
            sys.stdout.buffer.write(a.encode('utf8'))
            i=i+1

    c=os.path.exists("task.txt")
    if c== True:
        Counter=count("completed.txt")
    else:
        Counter=0
    b='Completed : '+str(Counter)+'\n'
    sys.stdout.buffer.write(b.encode('utf8'))
    if c== True:
        file=open("completed.txt")
        i=1
        for line in file:
            a=str(i)+". "+str(line)
            i=i+1
            sys.stdout.buffer.write(a.encode('utf8'))
            


#calls specific blocks from command line variables like add, report, del, done, ls, help

if len(sys.argv) == 1:
    help1()
    exit()
else:
    func=str(sys.argv[1])

if func == "add":
    if len(sys.argv) == 4:
        prio=str(sys.argv[2])
        text=str(sys.argv[3])
        add(prio,text)
    elif len(sys.argv) > 4:
        print("Error: Please follow format 'task add 4 \"Hello world\"' where 4 is priority and Hello world is task to be added.\nTask \"Hello World\" must be within double quote.")
    else:
        print("Error: Missing tasks string. Nothing added!")
        
    
elif func == "ls":
    ls()
elif func == "help":
    help1()
elif func == "del":
    if len(sys.argv) == 3:
        prio=str(sys.argv[2])
        delete(prio)
    elif len(sys.argv) > 3:
        print("Error: Please follow format 'task del 4' where 4 is index to be deleted.") 
    else:
        print("Error: Missing NUMBER for deleting tasks.")
elif func == "done":
    if len(sys.argv) == 3:
        prio=str(sys.argv[2])
        done(prio)
    elif len(sys.argv) > 3:
        print("Error: Please follow format 'task done 4' where 4 is index to be marked as done.")
    else:
        print("Error: Missing NUMBER for marking tasks as done.")
elif func == "report":
    report()
else:
    print("\nWrong command. PLease refer to help.\n\n")
    help1()
