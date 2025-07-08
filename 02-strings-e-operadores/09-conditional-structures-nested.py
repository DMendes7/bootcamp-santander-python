normal_account = True
university_account = False

balance = 2000
withdrawal = 500
special_check = 450

if normal_account:
    if balance >= withdrawal:
        print("Withdrawal successful")
    elif withdrawal <= (balance + special_check):
        print("Withdrawal successful with special check")
    else:
        print("Withdrawal not possible")
elif university_account:
    if balance >= withdrawal:
        print("Withdrawal successful")
    else:
        print("Withdrawal not possible")
else:
    print("Withdrawal not possible, account type not recognized") 