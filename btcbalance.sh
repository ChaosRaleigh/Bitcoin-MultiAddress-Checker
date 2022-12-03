#!/bin/bash
today=$(date +%B_%d_%Y)
FILE=/media/sf_Crypto_Balance/$today/$today"_checkedbalance.txt"

mkdir -p /media/sf_Crypto_Balance/$today && cd /media/sf_Crypto_Balance/$today && wget http://addresses.loyce.club/blockchair_bitcoin_addresses_and_balance_LATEST.tsv.gz -O - | gunzip -c > $today"_btcbalance.txt"  && join <(sort $today"_btcbalance.txt") <(sort "/media/sf_Crypto_Balance/btcmylist.txt" | fromdos) > $today"_checkedbalance.txt"

