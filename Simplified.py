# This progran will test if a collection of characters is a bitcoin wallet or possibly a different cryptocurrency
# Unfortunately, many addresses for cryptocurrencies have the same number of characters. Please look at the first digit of your address and read the output accordingly.

import sys

print("""
This program is designed to determine the type of crypto you are investigating.

Type "exit" and hit enter to leave the program at any time

It will additionally tell you a block explorer to use to further your investigation

If you have any issues using this program or there is incorrect information presented please contact me (ktpoorman@ua.edu)

Please copy and paste your characters into the prompt and hit enter
""")
wallet = input('What is your cryptocurrency address? ')
if len(wallet) == 34:
    if wallet.startswith('1'):
        print('')
        print('Bitcoin (BTC); For more information about this address, visit https://blockchain.com/btc/address/' + wallet)
        print('')
        print('To check if address is associated with exchange visit: https://walletexplorer.com/address/' + wallet)
    if wallet.startswith('3'):
        print('')
        print('Bitcoin (BTC) SegWit; For more information about this address, visit https://blockchain.com/btc/address/' + wallet)
        print('')
        print('Litecoin (LTC) SegWit; For more information about this address, visit https://live.blockcypher.com/ltc/address/' + wallet)
    if wallet.startswith('L'):
        print('')
        print('Litecoin (LTC); For more information about this address, visit https://live.blockcypher.com/ltc/address/' + wallet)
    if wallet.startswith('l'):
        print('')
        print('Litecoin (LTC); For more information about this address, visit https://live.blockcypher.com/ltc/address/' + wallet)
    if wallet.startswith('D'):
        print('')
        print('This address could be any of the following: Verge (XVG); Dogecoin (DOGE); DigiByte (DGB); Pivx (PIVX)')
        print('')
        print('For XVG, visit https://verge-blockchain.info/address/' + wallet)
        print('')
        print('For DOGE, visit https://live.blockcypher.com/doge/address/' + wallet)
        print('')
        print('For DGB, visit https://chainz.cryptoid.info/dgb/address.dws?' + wallet)
        print('')
        print('Pivx (PIVX); For more information about this address, visit https://chainz.cryptoid.info/pivx/address.dws?' + wallet)
    if wallet.startswith('r'):
        print('')
        print('Ripple (XRP); For more information about this address, visit https://bithomp.com/explorer/' + wallet)
    if wallet.startswith('X'):
        print('')
        print('Dash; For more information about this address, visit https:// Go to live.blockcypher.com/dash/' + wallet)
    if wallet.startswith('x'):
        print('')
        print('Dash; For more information about this address, visit https:// Go to live.blockcypher.com/dash/' + wallet)
    if wallet.startswith('T'):
        print('')
        print('Tron (TRX); For more information about this address, visit https://tronscan.org/#/address/' + wallet)
    if wallet.startswith('A'):
        print('')
        print('This address could be any of the following: Ark (ARK); Neo (NEO)')
        print('')
        print('For NEO, visit https://neotracker.io/address/' + wallet)
        print('')
        print('For ARK, visit https://explorer.ark.io/wallets/' + wallet)
    if wallet.startswith('a'):
        print('')
        print('Zcoin (XZC); For more information, visit https://chainz.cryptoid.info/xzc/address.dws?' + wallet)
    if wallet.startswith('R'):
        print('')
        print('This address could be any of the following: Komodo (KMD); ReddCoin (RDD)')
        print('')
        print('For KMD, visit https://kmdexplorer.io/address/' + wallet)
        print('')
        print('For RDD, visit https://live.reddcoin.com/address/' + wallet)
    if wallet.startswith('P'):
        print('')
        print('PotCoin (POT); For more information about this address, visit https://chainz.cryptoid.info/pot/search.dws?q=' + wallet)
    if wallet.startswith('N'):
        print('')
        print('This address could be any of the following: NAVCoin (NAV); NEM (XEM)')
        print('')
        print('For NAV, visit https://chainz.cryptoid.info/nav/search.dws?q=' + wallet)
        print('')
        print('For XEM, visit http://explorer.nemchina.com/#/s_account?account=' + wallet)
if len(wallet) == 35:
    if wallet.startswith('t'):
        print('')
        print('ZCash (ZEC); For more information about this address, visit https://chain.so/address/ZEC/' + wallet)
    if wallet.startswith('z'):
        print('')
        print('ZCash (ZEC); addresses that being with "z" conduct private transactions')
if len(wallet) == 42:
    print('')
    print('Bitcoin (BTC); For more information about this address, visit https://chain.so/address/BTC/' + wallet)
if len(wallet) == 52:
    if wallet.startswith('F'):
        print('')
        print('Factom (FCT); For more information about this address, visit https://' + wallet)
if len(wallet) == 76:
    if wallet.startswith('4'):
        print('')
    print('Siacoin (SIA); For more information about this address, visit https://explore.sia.tech/hashes/' + wallet)
if len(wallet) == 95:
    if wallet.startswith('4'):
        print('')
        print('Monero (XMR); The monero blockchain will require a transaction ID (TX ID).')
        print('')
        print('For more information about this address, visit https://moneroblocks.info/search/' + wallet)
if len(wallet) == 104:
    if wallet.startswith('D'):
        print('')
        print('Cardano (ADA); For more information about this address, visit https://cardanoexplorer.com/address/' + wallet)

if wallet == 'exit':
    sys.exit()

    #else: print('Could not determine, please be sure you copy and pasted the entire wallet into prompt before hitting enter.')
        
