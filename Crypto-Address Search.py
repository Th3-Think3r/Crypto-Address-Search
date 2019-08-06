# This progran will test if a collection of characters is a bitcoin wallet
# Unfortunately, many addresses for cryptocurrencies have the same number of characters. Please look at the first digit of your address and read the output accordingly.

print('This program is designed to determine the type of crypto you are investigating.')
print('If you have any issues with this program please contact me (ktpoorman@ua.edu)')
print('Please copy and paste your characters into the prompt and hit enter')
wallet = input('What is your cryptocurrency address?')
if wallet.startswith('1'):
    print('Bitcoin (BTC); Go to https://www.blockexplorer.com')
if wallet.startswith('3'):
    print('Bitcoin (BTC); Go to https://www.blockexplorer.com')
if wallet.startswith('4'):
    print('Monero (XMR)')
if wallet.startswith('L'):
    print('Litecoin (LTC)')
if wallet.startswith('l'):
    print('Litecoin (LTC)')
if wallet.startswith('q'):
    print('Bitcoin Cash (BCH); Go to https://blockexplorer.com')
if wallet.startswith('D'):
    print('Verge (XVG); Dogecoin (DOGE); Cardano (ADA)')
if wallet.startswith('0x'):
    print('Ether or Ethereum-based Token (ETH)')
if wallet.startswith('r'):
    print('Ripple (XRP)')
if wallet.startswith('X'):
    print('Dash')
if wallet.startswith('x'):
    print('Dash')
if wallet.startswith('T'):
    print('Tron (TRX')
if wallet.startswith('A'):
    print('Neo (NERO')
if wallet.startswith('t'):
    print('ZCash (ZEC)')
if wallet.startswith('z'):
    print('ZCash (ZEC)')
