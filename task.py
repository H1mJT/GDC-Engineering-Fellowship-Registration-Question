import sys, operator



def help():
    print('''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics''')

def add(x,y):
    

    try :
        z=int(x)
    except:
        print("Priority must be an integer.")
        exit()

    x=str(x)
    y=str(y)
    try:
        f=open("task.txt", "a")
    except:
        fa= open("task.txt","w+")
        fa.close()
        f=open("task.txt","a")
    f.write(x+" "+y+"\n" )
    print('Added task: "'+y+'" with priority',x)
    f.close()


def ls():
    lines={}
    try:
        file=open("task.txt")
    except:
        print("No tasks remained.")
    i=0
    for line in file:
        pieces=line.split(" ",1)
        lines[pieces[1].strip("\n")]=pieces[0]
    d=sorted(lines.items(), key=operator.itemgetter(1))
    for word in d:    
        print(str(i+1)+". "+d[i][0]+ " ["+str(d[i][1])+"]\n")
        i=i+1
    if i==0:
        print("No tasks remained.")
    file.close()



def delete(z):
    try:
        z=int(z)
    except:
        print("Index must be an integer.")
        exit()

    try:
    
        lines={}
        try:
            file=open("task.txt")
        except:
            print("No tasks to delete.")
        
        
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
                if wor.strip("\n") != d[z-1][0]:
                    f.write(word)
        print("Deleted task #"+str(z))
    except:
        print('item with index ', z, ' does not exist. Nothing deleted.')
    


def done(m):
    try:
        m=int(m)
    except:
        print("Index must be an integer.")
        exit()
    try:
        
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
                if wor.strip("\n") != d[m-1][0]:
                    f.write(word)
                    
                else:
                    
                    fs.write(wor)
        print("Marked item as done.")
            
    except:
        print('no incomplete item with index', m, 'exists.')
                    

    
    

def report():
    file = open("task.txt","r")
    Counter = 0
      
   
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
        lines[pieces[1].strip("\n")]=pieces[0]
    d=sorted(lines.items(), key=operator.itemgetter(1))
    for word in d:    
        print(str(i+1)+". "+str(d[i][0])+" ["+ str(d[i][1])+ "]\n")
        i=i+1
        
    file = open("completed.txt","r")
    Counter = 0
      
   
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

