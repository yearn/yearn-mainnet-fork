#! /bin/bash

ganache-cli \
  -h 0.0.0.0 \
  --accounts 10 \
  --hardfork istanbul \
  --fork https://mainnet.infura.io/v3/${WEB3_INFURA_PROJECT_ID} \
  --gasLimit 12000000 \
  --mnemonic brownie \
  --port 8545
