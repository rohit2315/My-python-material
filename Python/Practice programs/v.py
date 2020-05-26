for i in range(4):
    for j in range(7):
        if (i==j) or (i+j==6):   # end means you store a empty string
            print('*',end='')    #help(print) by default after writing print it goes to next line
        else:
            print(end=' ')    
  
    print()   