print("黑白猜開始...")
player1 = input("請輸入第一位玩家名稱:")
player2 = input("請輸入第二位玩家名稱:")

isGameOver = False

while isGameOver == False:
    option1 = input(player1 + "請選擇以下選項: 1.石頭 2.布 3.剪刀 ")
    print("***No CHEATIGN!\n" * 20)
    option2 = input(player2 + "請選擇以下選項: 1.石頭 2.布 3.剪刀 ")

    if option1 == option2:
        print("平手!請再猜一次!")
    else:
        if (option1 == "1" and option2 == "3") or (option1 == "2" and option2 == "1") or (option1 == "3" and option2 == "2"):
            print(player1 + "猜贏，要開始比方向囉!")
            option1 = input(player1 + "請選擇以下選項: 1.上 2.左 3.下 4.右 ")
            print("***No CHEATIGN!\n" * 20)
            option2 = input(player2 + "請選擇以下選項: 1.上 2.左 3.下 4.右 ")

            if option1 == option2:
                print(player1 + "贏了!")
                isGameOver = True
            else:
                print("平手!請再猜一次!")
        else:
            print(player2 + "猜贏，要開始比方向囉!")
            option2 = input(player2 + "請選擇以下選項:: 1.上 2.左 3.下 4.右 ")
            print("***No CHEATIGN!\n" * 20)
            option1 = input(player1 + "請選擇以下選項:: 1.上 2.左 3.下 4.右 ")

            if option1 == option2:
                print(player2 + "贏了")
                isGameOver = True
            else:
                print("平手!請再猜一次!")
