# tic-tac-toe - text based

print(
    "-- A   B   C\n"
    "1    |   |   \n"
    "  -----------\n"
    "2    |   |   \n"
    "  -----------\n"
    "3    |   |   \n"
)

moves_dict = {'A1': ' ',
              'A2': ' ',
              'A3': ' ',
              'B1': ' ',
              'B2': ' ',
              'B3': ' ',
              'C1': ' ',
              'C2': ' ',
              'C3': ' ',
              }


def xInput():
    x_in = input("X player, enter a number and letter").capitalize()
    if x_in in moves_dict.keys() and moves_dict[x_in] == ' ':
        moves_dict[x_in] = "X"
    else:
        xInput()


def oInput():
    o_in = input("O player, enter a number and letter").capitalize()
    if o_in in moves_dict.keys() and moves_dict[o_in] == ' ':
        moves_dict[o_in] = "O"
    else:
        oInput()


def checkWin() -> str:
    x_list = []
    o_list = []
    for k, v in moves_dict.items():
        if v == "X":
            x_list.append(k)
        if v == "O":
            o_list.append(k)
    xwin = inarow(x_list)
    owin = inarow(o_list)
    if xwin:
        return 'x'
    elif owin:
        return 'o'
    else:
        return 'n'


def inarow(inlist: list) -> bool:
    a = 0
    b = 0
    c = 0
    one = 0
    two = 0
    three = 0
    for item in inlist:
        if item.startswith("A"):
            a += 1
        if item.startswith("B"):
            b += 1
        if item.startswith("C"):
            c += 1
        if item.endswith("1"):
            one += 1
        if item.endswith("2"):
            two += 1
        if item.endswith("3"):
            three += 1
    finallist = [a, b, c, one, two, three]
    if finallist.count(3) >= 1:
        return True
    elif inlist.count("A1") == 1 and inlist.count("B2") == 1 and inlist.count("C3") == 1:
        return True
    elif inlist.count("A3") == 1 and inlist.count("B2") == 1 and inlist.count("C1") == 1:
        return True
    else:
        return False


def turn():
    xInput()
    if checkWin() == 'x':
        print('X Wins!')
        quit()
    elif checkWin() == 'o':
        print('O Wins!')
        quit()
    print(
        f"-- A   B   C\n"
        f"1  {moves_dict['A1']} | {moves_dict['B1']} | {moves_dict['C1']} \n"
        f"  -----------\n"
        f"2  {moves_dict['A2']} | {moves_dict['B2']} | {moves_dict['C2']} \n"
        f"  -----------\n"
        f"3  {moves_dict['A3']} | {moves_dict['B3']} | {moves_dict['C3']} \n"
    )
    oInput()
    if checkWin() == 'x':
        print('X Wins!')
        quit()
    elif checkWin() == 'o':
        print('O Wins!')
        quit()
    print(
        f"-- A   B   C\n"
        f"1  {moves_dict['A1']} | {moves_dict['B1']} | {moves_dict['C1']} \n"
        f"  -----------\n"
        f"2  {moves_dict['A2']} | {moves_dict['B2']} | {moves_dict['C2']} \n"
        f"  -----------\n"
        f"3  {moves_dict['A3']} | {moves_dict['B3']} | {moves_dict['C3']} \n"
    )


while True:
    turn()
