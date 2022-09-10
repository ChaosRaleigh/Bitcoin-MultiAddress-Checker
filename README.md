# Bitcoin-MultiAddress-Checker
 Check unlimited BTC address 

## Warning!!! Do not immediately use the python script

## Requirements:
1) Virtual Machine
2) Any Linux Distribution
3) BTC Addresses dump database
4) Your list of addresses to crosscheck with the database. I named it mylist.txt
5) Modify the wget address, Step 2. 
6) Patience :D

## Here are the steps to check unlimited amount of address

1) Create a shared folder on your VirtualBox. Ensure that your list of addresses is inside the folder.
2) Type sudo apt-get fromdos.
3) Power up your virtual machine with Linux
4) Navigate to your shared folder. cd /media/yoursharedfolder 
5)Open the terminal. Type wget http://addresses.loyce.club/blockchair_bitcoin_addresses_and_balance_September_08_2022.tsv.gz -0 - | gunzip > latestbtcaddress.txt
6) type join <(sort latestbtcaddress.txt) <(sort mylist.txt | fromdos) > output.txt
7) cat output.txt to check if your own list has balances inside. 

## So what is the BTCAddressBulkChecker.py for????
### Well, if you want to verify your output.txt to another blockchain explorer like blockchain.com, follow these steps.
1) Open your Microsoft Excel. 
2) Click the Data tab and import the output.txt. 
3) Save as output.csv.

## Misc
1) The BTC addresses dump can also be found from this website https://blockchair.com/dumps. 
2) Click Bitcoin/Addresses and install the tsv file. We cannot use windows to open this tsv file as it contains millions of BTC addresses. I personally used Kali Linux to do this ;).
3) Remember that when creating a notepad in Windows it is considered a DOS file so when importing it in Linux.

## Credits
### I humbly appreciate Loyce for hosting a server to store the database dump. 