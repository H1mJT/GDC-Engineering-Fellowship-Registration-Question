import sys, operator



def help():
    print('''
./task add 2 "hello world"    # Add a new item with priority 2 and text "hello world" to the list
./task ls                     # Show incomplete priority list items sorted by priority in ascending order
./task del INDEX              # Delete the incomplete item with the given index
./task done INDEX             # Mark the incomplete item with the given index as complete
./task help                   # Show usage
./task report                 # Statistics''')

def add(x,y):
    
    if 0<=x<=10:
        x=str(x)
        y=str(y)
        f=open("task.txt", "a")
        f.write(x+" "+y+"\n" )
        f.close()
    else:
        print('Please select allowed priority range 0-10')

def ls():
    lines={}
    file=open("task.txt")
    i=0
    for line in file:
        pieces=line.split(" ",1)
        lines[pieces[1].strip("\n")]=pieces[0]
    d=sorted(lines.items(), key=operator.itemgetter(1))
    for word in d:    
        print(i+1,".", d[i][0], " [",d[i][1], "]\n")
        i=i+1
    file.close()
def delete(z):
    try:
    
        lines={}
        file=open("task.txt")
        #print(z-1)
        
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
        
    except:
        print('item with index ', z, ' does not exist. Nothing deleted.')
    

def done(m):
    
    try:
        
        lines={}
        file=open("task.txt")
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
    print('Pending : ', Counter)
    lines={}
    file=open("task.txt")
    i=0
    for line in file:
        pieces=line.split(" ",1)
        lines[pieces[1].strip("\n")]=pieces[0]
    d=sorted(lines.items(), key=operator.itemgetter(1))
    for word in d:    
        print(i+1,".", d[i][0], " [",d[i][1], "]\n")
        i=i+1
        
    file = open("completed.txt","r")
    Counter = 0
      
   
    Content = file.read()
    CoList = Content.split("\n")
      
    for i in CoList:
        if i:
            Counter += 1
    print('Completed : ', Counter)
   
    file=open("completed.txt")
    i=1
    for line in file:
        print(i,'. ', line)
        i=i+1
