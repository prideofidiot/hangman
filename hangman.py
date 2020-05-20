# hangman
def hangman(word):
    wrong=0
    stage=["",
           "_______       ",
           "|             ",
           "|      |      ",
           "|      o      ",
           "|     /|\     ",
           "|     / \     ",
           "|             "
           ]
    rletter=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to hangman!")
    while wrong < len(strange) - 1:
        print("\n")
        msg="guess a letter"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong += 1
        print(" ",join(board))
        e = wrong + 1
        print("\n".join(stage[0:e]))
        if  "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose. that's {}.".format(word))

hangman("cat")
