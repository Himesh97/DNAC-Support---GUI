def reset():
    f = open("clicked.txt" , "w")
    clicked = 0
    f.write(str(clicked))
    f.close

def isClicked():
    f = open("clicked.txt" , "r")
    for i in f:
        flag = i
        return flag
    
