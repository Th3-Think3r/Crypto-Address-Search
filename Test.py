# This progran will test if a collection of characters is a bitcoin wallet
# Unfortunately, many addresses for cryptocurrencies have the same number of characters. Please look at the first digit of your address and read the output accordingly.

print('Hello Investigator, this program is designed to determine the type of cryptocurrency you are investigating. Please copy and paste your characters into the prompt and hit enter')
wallet = input('What is your cryptocurrency address?')
if len(wallet) == 34:
    print('Bitcoin (begins with 1 or 3); Litecoin (begins with L); Verge (starts with a D)')
if len(wallet) == 42:
    print('Ethereum Token (beings with 0x) or (Bitcoin Cash (begins with Q')
if len(wallet) == 95:
    print('Monero (beins with a 4')
if len(wallet) == 35:
    print('Ripple')
