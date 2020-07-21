def initial_display():
    arr = ['1','2','3','4','5','6','7','8','9']
    print("|\t" + arr[0] + "\t|\t" + arr[1] + "\t|\t" + arr[2] + "\t|\t")
    print("|\t" + arr[3] + "\t|\t" + arr[4] + "\t|\t" + arr[5] + "\t|\t")
    print("|\t" + arr[6] + "\t|\t" + arr[7] + "\t|\t" + arr[8] + "\t|\t")


gamelist=["", "", "","","","","","",""]
def take_userinput(index , icon):
    flag = False
    indx = int(index)-1
    gamelist[indx] = icon
    a = gamelist[0]
    b = gamelist[1]
    c = gamelist[2]
    d = gamelist[3]
    e = gamelist[4]
    f = gamelist[5]
    g = gamelist[6]
    h = gamelist[7]
    i = gamelist[8]

    print_gamelist()
    if (a==b and b==c) and a and b and c:
        print(a+ " Won")
        flag = True
    elif (a==d and d==g) and a and d and g:
        print(a + " Won")
        flag = True
    elif (a==e and e==i) and a and e and i:
        print(a + " Won")
        flag = True
    elif (b==e and e==h) and b and e and h:
        print(b + " Won")
        flag = True
    elif (c==f and f==i) and c and f and i:
        print(c+ " Won")
        flag = True
    elif (d==e and e==f) and d and e and f:
        print(d + " Won")
        flag = True
    elif (g==h and h==i) and g and h and i:
        print(g + " Won")
        flag = True
    elif (g==e and e==c) and g and e and c:
        print(a+ " Won")
        flag = True
    return flag

def print_gamelist():
    print("|\t"+gamelist[0] + "\t|\t" + gamelist[1] + "\t|\t" + gamelist[2] + "\t|\t")
    print("|\t"+gamelist[3] + "\t|\t" + gamelist[4] + "\t|\t" + gamelist[5] + "\t|\t")
    print("|\t"+gamelist[6] + "\t|\t" + gamelist[7] + "\t|\t" + gamelist[8] + "\t|\t")


def menu():
    print("NOTE: YOU HAVE TO FOLLOW THE FOLLIOWING PATTERN.")
    initial_display()
    player1 = input("Player 1 Please Select : X OR O : ")
    player1=player1.upper()
    player2 = ""
    flag = False
    if player1=='X':
       player2= "O"
    elif player1=='O':
       player2= 'X'
    counter =0
    for x in range (0,9):
        if counter%2 ==0:
            userinput = input("Player 1 : Please select the cell number : ")
            flag = take_userinput(userinput,player1)

        else:
            userinput = input("Player 2 : Please select the cell number : ")
            flag = take_userinput(userinput,player2)
        if flag:
            break
        counter+=1
    if flag == False:
        print("Game Draw")
menu()
