# This progran will test if a collection of characters is a bitcoin wallet or possibly a different cryptocurrency
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
wallet = input('What is your cryptocurrency address? ')
if wallet.startswith('1' or '3') and len(wallet) == 34:
    print('')
    print('Bitcoin (BTC); For more information about this address, visit https://blockchain.com/btc/address/' + wallet)
if wallet.startswith('3') and len(wallet) == 34:
    print('')
    print('Bitcoin (BTC) SegWit; For more information about this address, visit https://blockchain.com/btc/address/' + wallet)
    print('')
    print('Litecoin (LTC) SegWit; For more information about this address, visit https:///live.blockcypher.com/ltc/address/' + wallet)
if wallet.startswith('bc1') and len(wallet) == 42:
    print('')
    print('Bitcoin (BTC); For more information about this address, visit https://btc.com/' + wallet)
if wallet.startswith('4') and len(wallet) == 95:
    print('')
    print('Monero (XMR); For more information about this address, visit https://moneroblocks.info/search/' + wallet)
if wallet.startswith('L') and len(wallet) == 34:
    print('')
    print('Litecoin (LTC); For more information about this address, visit https:/live.blockcypher.com/ltc/' + wallet)
if wallet.startswith('l') and len(wallet) == 34:
    print('')
    print('Litecoin (LTC); For more information about this address, visit https:// Go to live.blockcypher.com/ltc/' + wallet)
if wallet.startswith('q'):
    print('')
    print('Bitcoin Cash (BCH); For more information about this address, visit https://www.blockchain.com/bch/address/' + wallet)
if wallet.startswith('D') and len(wallet) == 34:
    print('')
    print('This address could be any of the following: Verge (XVG); Dogecoin (DOGE); DigiByte (DGB)')
    print('')
    print('For XVG, visit https://verge-blockchain.info/address/' + wallet)
    print('')
    print('For DOGE, visit https://live.blockcypher.com/doge/address/' + wallet)
    print('')
    print('For DGB, visit https://chainz.cryptoid.info/dgb/address.dws?' + wallet)
if wallet.startswith('D') and len(wallet) == 104:
    print('')
    print('Cardano (ADA); For more information about this address, visit https://cardanoexplorer.com/address/' + wallet)
if wallet.startswith('0x'):
    print('Ether (ETH) or Ethereum-based Token')
if wallet.startswith('r') and len(wallet) == 34:
    print('')
    print('Ripple (XRP); For more information about this address, visit https:// Go to blockchair.com/ripple/' + wallet)
if wallet.startswith('X') and len(wallet) == 34:
    print('')
    print('Dash; For more information about this address, visit https:// Go to live.blockcypher.com/dash/' + wallet)
if wallet.startswith('x') and len(wallet) == 34:
    print('')
    print('Dash; For more information about this address, visit https:// Go to live.blockcypher.com/dash/' + wallet)
if wallet.startswith('T') and len(wallet) == 34:
    print('')
    print('Tron (TRX); For more information about this address, visit https://tronscan.org/#/address/' + wallet)
if wallet.startswith('A') and len(wallet) == 34:
    print('')
    print('This address could be any of the following: Ark (ARK); Neo (NEO)')
    print('')
    print('For NEO, visit https://neotracker.io/address/' + wallet)
    print('For ARK, visit https://explorer.ark.io/wallets/' + wallet)
if wallet.startswith('t') and len(wallet) == 35:
    print('')
    print('ZCash (ZEC); For more information about this address, visit https:// Go to chain.so/zcash/' + wallet)
if wallet.startswith('z') and len(wallet) == 35:
    print('')
    print('ZCash (ZEC); For more information about this address, visit https:// Go to chain.so/zcash/' + wallet)
if wallet.startswith('R') and len(wallet) == 34:
    print('')
    print('This address could be any of the following: Komodo (KMD); ReddCoin (RDD)')
    print('')
    print('For KMD, visit https://kmdexplorer.io/address/' + wallet)
    print('For RDD, visit https://live.reddcoin.com/address/' + wallet)
if wallet.startswith('P') and len(wallet) == 34:
    print('')
    print('PotCoin (POT); For more information about this address, visit https://chainz.cryptoid.info/pot/search.dws?q=' + wallet)
if wallet.startswith('N') and len(wallet) == 34:
    print('')
    print('This address could be any of the following: NAVCoin (NAV); NEM (XEM)')
    print('')
    print('For NAV, visit https://chainz.cryptoid.info/nav/search.dws?q=' + wallet)
    print('For XEM, visit http://explorer.nemchina.com/#/s_account?account=' + wallet)
if wallet.startswith('F') and len(wallet) == 52:
    print('')
    print('Factom (FCT); For more information about this address, visit https://' + wallet)
if wallet.startswith('4') and len(wallet) == 76:
    print('')
    print('Siacoin (SIA); For more information about this address, visit https://explore.sia.tech/hashes/ ' + wallet)

if wallet == 'exit':
    sys.exit()

    #else: print('Could not determine, please be sure you copy and pasted the entire wallet into prompt before hitting enter.')
    
    

