balance = 1000
withdraw = 500

status = "Success" if balance > withdraw else "Failure"

print(f"Withdrawal status: {status}")