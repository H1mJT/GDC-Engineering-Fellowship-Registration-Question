import sys, operator


#Help block
def help1():
    print('''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics''')

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
    lines={}
    try:
        file=open("task.txt")
    except:
        print("No tasks remained.")
    i=0
    for line in file:
        pieces=line.split(" ",1)  
        lines[pieces[1].strip("\n")]=pieces[0]             #Stores the tasks and priority as key value pair in dict
    d=sorted(lines.items(), key=operator.itemgetter(1))    #Sorts the dict by priority
    for word in d:    
        print(str(i+1)+". "+d[i][0]+ " ["+str(d[i][1])+"]\n")
        i=i+1
    if i==0:
        print("No tasks remained.")
    file.close()


#del task block
def delete(z):
    try:
        z=int(z)
    except:
        print("Index must be an integer.")
        exit()
    #Counts number of lines in task.txt
    file = open("task.txt","r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
      
    for i in CoList:
        if i:
            Counter += 1
    #Checks if the given index exists
    if Counter < z:
        print('item with index ', z, ' does not exist. Nothing deleted.')
    else:
        lines={}
        try:
            file=open("task.txt")
        except:
            print("No tasks to delete.")
        
        
        for line in file:
            pieces=line.split(" ",1)
            lines[pieces[1].strip("\n")]=pieces[0]             #Stores the tasks and priority as key value pair in dict
        d=sorted(lines.items(), key=operator.itemgetter(1))    #Sorts the dict by priority
        file.close()
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
    #Counts number of lines in task.txt
    file = open("task.txt","r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    
    for i in CoList:
        if i:
            Counter += 1
    #Checks if the given index exists
    if Counter < m:
        print('item with index ', m, ' does not exist. Nothing marked as done.')

    else:
        
        lines={}
        file=open("task.txt")
        try:
            fs=open("completed.txt", "a")
        except:
            fg=open("completed.txt", "w+")
            fg.close()
            fs=open("completed.txt", "a")
        
        #print(m-1)
        
        for line in file:
            pieces=line.split(" ",1)
            lines[pieces[1].strip("\n")]=pieces[0]
        d=sorted(lines.items(), key=operator.itemgetter(1))
        file.close()
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
    file = open("task.txt","r")
    Counter = 0
      
    #Counts number of lines in task.txt
    Content = file.read()
    CoList = Content.split("\n")
      
    for i in CoList:
        if i:
            Counter += 1
    print('Pending :', Counter)
    
    lines={}
    file=open("task.txt")
    i=0
    for line in file:
        pieces=line.split(" ",1)
        lines[pieces[1].strip("\n")]=pieces[0]            #Stores the tasks and priority as key value pair in dict
    d=sorted(lines.items(), key=operator.itemgetter(1))   #Sorts the dict by priority
    for word in d:    
        print(str(i+1)+". "+str(d[i][0])+" ["+ str(d[i][1])+ "]\n")
        i=i+1
        
    file = open("completed.txt","r")
    Counter = 0
      
    #Counts number of lines in completed.txt
    Content = file.read()
    CoList = Content.split("\n")
      
    for i in CoList:
        if i:
            Counter += 1
    print('Completed :', Counter)
   
    file=open("completed.txt")
    i=1
    for line in file:
        print(str(i)+'. '+str(line))
        i=i+1


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
    else:
        print("Not enough parameters in command.")
        
    
elif func == "ls":
    ls()
elif func == "help":
    help1()
elif func == "del":
    if len(sys.argv) == 3:
        prio=str(sys.argv[2])
        delete(prio)
    else:
        print("Not enough parameters in command.")
elif func == "done":
    if len(sys.argv) == 3:
        prio=str(sys.argv[2])
        done(prio)
    else:
        print("Not enough parameters in command.")
elif func == "report":
    report()
else:
    print("\nWrong command. PLease refer to help.\n\n")
    help1()

