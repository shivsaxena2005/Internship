def file():
    t = []
    with open('tasks.txt', 'r') as f:
        t += f.read().split('\n')
    return t


while True:
    print("Enter Appropriate no. based on your requirement")
    print("1.Add a Task\n2.Remove a Task\n3.View a Task\n4.exist")
    x = input()
    if(x == '4'):
        break
    elif(x == '3'):
        t = 1
        try:
            tasks = file()
        except:
            print("Some error to open the saved tasks")    
            break
        for i in tasks:
            if(i != ''):
                print(t,": ",i)
            t += 1
    elif(x == '1'):
        task = input("Enter your task: ")
        try:
            tasks = file()
        except:
            print("Some error occur to open the file")
            break
        tasks.append(task)
        try:
            with open('tasks.txt','w') as f:
                for t in tasks:
                    f.write(t + '\n')
        except:
            print("Some error occur")
            break
    elif(x == '2'):
        try:
            tasks = file()
        except:
            print("Some error occur")
            break  
        print("Here is your all tasks Enter appropriate no. so easily i can remove")
        for i in range(len(tasks)):
            if(tasks[i] != ''):
                print(i+1,": ",tasks[i])
        t = int(input("Enter corresponding no.: "))
        tasks.remove(tasks[t-1])
        try:
            with open('tasks.txt','w') as f:
                for i in tasks:
                    f.write(i + '\n')
        except:
            print("Some error")
            break        



