import getpass


def tranferName1(option):
    if option == 1:
        return "石頭"
    elif option == 2:
        return "布"
    else:
        return "剪刀"


def tranferName2(option):
    if option == 1:
        return "上"
    elif option == 2:
        return "左"
    elif option == 3:
        return "下"
    else:
        return "右"


print("黑白猜開始...")
player1 = input("請輸入第一位玩家名稱:")
player2 = input("請輸入第二位玩家名稱:")
isForwardGameOver = False
isGameOver = False

while isGameOver == False:

    try:
        option1 = int(getpass.getpass(player1 + "請選擇以下選項: 1.石頭 2.布 3.剪刀 "))
        option2 = int(getpass.getpass(player2 + "請選擇以下選項: 1.石頭 2.布 3.剪刀 "))

        if (option1 < 0 or option1 > 3) or (option2 < 0 or option2 > 3):
            print("請輸入正確的選項1~3")
        else:
            if option1 == option2:
                print(f"{player1}跟{player2}都猜{tranferName1(option1)}！請再猜一次！")
            else:
                isPlayer1Win = False
                if (option1 == 1 and option2 == 3) or (option1 == 2 and option2 == 1) or (option1 == 3 and option2 == 2):
                    isPlayer1Win = True
                    print(
                        f"{player1}猜{tranferName1(option1)}，{player2}猜{tranferName1(option2)}。{player1}贏，要開始比方向囉!")
                else:
                    isPlayer1Win = False
                    print(
                        f"{player1}猜{tranferName1(option1)}，{player2}猜{tranferName1(option2)}。{player2}贏，要開始比方向囉!")

                isForwardGameOver = False
                while isForwardGameOver == False:
                    try:
                        option1 = int(getpass.getpass(
                            player1 + "請選擇以下選項:: 1.上 2.左 3.下 4.右 "))
                        option2 = int(getpass.getpass(
                            player2 + "請選擇以下選項:: 1.上 2.左 3.下 4.右 "))
                    except:
                        print("請輸入數字！")

                    if (option1 < 0 or option1 > 4) or (option2 < 0 or option2 > 4):
                        print("請輸入正確的選項1~4")
                    else:
                        if option1 == option2:
                            print(f"{player1}跟{player2}猜{tranferName2(option1)}")
                            if isPlayer1Win:
                                print(f"{player1}贏了!")
                            else:
                                print(f"{player2}贏了!")

                            isGameOver = True
                        else:
                            print(
                                f"{player1}猜{tranferName2(option1)}，{player2}猜{tranferName2(option2)}。請再猜一次!")

                        isForwardGameOver = True
    except:
        print("請輸入數字！")
