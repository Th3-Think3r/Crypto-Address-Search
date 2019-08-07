# This progran will test if a collection of characters is a bitcoin wallet
# Unfortunately, many addresses for cryptocurrencies have the same number of characters. Please look at the first digit of your address and read the output accordingly.

import sys

print('This program is designed to determine the type of crypto you are investigating.')
print('')
print('Type "exit" and hit enter to leave the program')
print('')
print('It will additionally tell you a block explorer to use to further your investigation')
print('')
print('If you have any issues using this program or there is incorrect information presented please contact me (ktpoorman@ua.edu)')
print('')
print('Please copy and paste your characters into the prompt and hit enter')
print('')
wallet = input('What is your cryptocurrency address?')
if wallet.startswith('1') and len(wallet) == 34:
    print('Bitcoin (BTC); Go to blockexplorer.com')
if wallet.startswith('3') and len(wallet) == 34:
    print('Bitcoin (BTC); Go to blockexplorer.com')
if wallet.startswith('bc1'):
    print('Bitcoin (BTC); Go to blockexplorer.com')
if wallet.startswith('4') and len(wallet) == 95:
    print('Monero (XMR); Go to moneroblocks.info')
if wallet.startswith('L') and len(wallet) == 34:
    print('Litecoin (LTC); Go to live.blockcypher.com/ltc/')
if wallet.startswith('l') and len(wallet) == 34:
    print('Litecoin (LTC); Go to live.blockcypher.com/ltc/')
if wallet.startswith('q'):
    print('Bitcoin Cash (BCH); Go to blockexplorer.com')
if wallet.startswith('D') and len(wallet) == 34:
    print('This address could be any of the following: Verge (XVG); Dogecoin (DOGE); DigiByte (DGB)')
if wallet.startswith('D') and len(wallet) == 104:
    print('Cardano (ADA); Go to cardanoexplorer.com')
if wallet.startswith('0x'):
    print('Ether (ETH) or Ethereum-based Token')
if wallet.startswith('r') and len(wallet) == 34:
    print('Ripple (XRP); Go to blockchair.com/ripple')
if wallet.startswith('X') and len(wallet) == 34:
    print('Dash; Go to live.blockcypher.com/dash/')
if wallet.startswith('x') and len(wallet) == 34:
    print('Dash; Go to live.blockcypher.com/dash/')
if wallet.startswith('T') and len(wallet) == 34:
    print('Tron (TRX); Go to tronscan.org')
if wallet.startswith('A') and len(wallet) == 34:
    print('This address could be any of the following: Ark (ARK); Neo (NEO)')
if wallet.startswith('t') and len(wallet) == 35:
    print('ZCash (ZEC); Go to chain.so/zcash')
if wallet.startswith('z') and len(wallet) == 35:
    print('ZCash (ZEC); Go to chain.so/zcash')
if wallet.startswith('R') and len(wallet) == 34:
    print('This address could be any of the following: Komodo (KMD); ReddCoin (RDD)')
if wallet.startswith('P') and len(wallet) == 34:
    print('PotCoin (POT); Go to ****')
if wallet.startswith('N') and len(wallet) == 34:
    print('This address could be any of the following: NAVCoin (NAV); NEM (XEM)')
if wallet.startswith('F') and len(wallet) == 52:
    print('Factom (FCT); Go to ****')
if wallet.startswith('4') and len(wallet) == 76:
    print('SiaC=coin (SIA); Go to ****')

if wallet == 'exit':
    sys.exit()

    #else: print('Could not determine, please be sure you copy and pasted the entire wallet into prompt before hitting enter.')
    
    

