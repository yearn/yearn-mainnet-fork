# yearn-mainnet-fork

## Usage

```bash
export WEB3_INFURA_PROJECT_ID=<YOUR_WEB3_INFURA_PROJECT_ID>
export ETHERSCAN_TOKEN=<YOUR_ETHERSCAN_TOKEN>
docker-compose up --build
```

The first time this will take some minutes to download all dependencies, but any subsequent call should just run in several seconds.


## Testing with MetaMask

1. Change RPC provider

   In MetaMask change to the `localhost:8545` provider.

2. Import test accounts

   The following three test accounts have been populated with some 100 ETH, 1M DAI, 1000 CRV and 250 YFI :rocket:

   You can import a testaccount into your MetaMask by copy-pasting at least one of the private keys into 'account' -> 'import'
   
   


| Wallet address                             | Private key                                                        |
|:------------------------------------------ |:------------------------------------------------------------------ |
| 0x9fde0c31B3b21E8031C08A5c43f851c9C6544E35 | 0x8724398c1580e64667ec0c5d8fff0d1f2e3dd59338c114283c1ea8970b5309b4 |
| 0x5fe0676e41741A3a2d84C41DC46cC991812FE110 | 0xe52789058ba8b5da1c4e82a644fa21d9ceeea35931714a1c12444c0a74e35db7 |
| 0x5307DB0c8Fb2Dc616B94f3b2f9fe7a99920e5e52 | 0x01ac1291b438aeaa2961d9aef838e359707f33203c7a1fbb1b8bc59a48899b12 |


## Changing initial tokens

You can always change initial token supplies in this file:

`supply_tokens.py`


After making any changes run again:

`docker-compose up --build`
