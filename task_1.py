x = None
while(x != 'exit'):
    x = input(">>")
    if(x == 'exit'):
        break
    first = ''
    t = 0
    sec = ''
    for i in x:
        if(i.isnumeric() or i == ' '):
            if(t == 0):
                first += i
            else:
                sec += i    
        else:
            oper = i
            t = 1

    if(len(x) == (len(first) + len(sec) + 1)):
        match(oper):
            case('+'):
                p = int(first) + int(sec)
                print(p)
            case('-'):
                p = int(first) - int(sec)
                print(p)
            case('*'):
                p = int(first) * int(sec)
                print(p)
            case('/'):
                try:
                    p = int(first) / int(sec)
                    print(p)
                except:
                    print("Can't divide by zero")    
    else:
        print("Invalid Operation")            

