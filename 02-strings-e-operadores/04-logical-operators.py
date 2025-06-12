print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False

balance = 1000
withdrawal = 250
limit = 200
especial_account = True

print(balance >= withdrawal and withdrawal <= limit or especial_account and balance >= withdrawal)  # True

print((balance >= withdrawal and withdrawal <= limit) or (especial_account and balance >= withdrawal))  # True