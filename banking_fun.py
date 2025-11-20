import sys
sys.path.append(r".\Finance")
from Finance import banking


bal = 100
bal = banking.withdraw(bal)
bal = banking.deposit(bal)
print(bal)






