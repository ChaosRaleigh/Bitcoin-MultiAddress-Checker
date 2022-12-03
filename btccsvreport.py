import os
import datetime
import pandas as pd

date = datetime.datetime.now()
today = date.strftime("%B_%d_%Y") 
print(today)
os.chdir('/media/sf_Crypto_Balance/'+(today))
#print("Current working directory: {0}".format(os.getcwd()))

df = pd.read_csv((today)+"_checkedbalance.txt", delim_whitespace=True)
df.columns = ['Address', today]

Wallet_Balance=(df.loc[:,today])

Balance_storage=[]
for balance in Wallet_Balance:
    new_balance = int(balance)/100000000
    Balance_storage.append(new_balance)

df.loc[:,today] = Balance_storage
df.to_csv((today)+"_checkedBTCbalance.csv", index=None)



