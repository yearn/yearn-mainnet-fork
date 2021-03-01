from brownie import *


def main():
  # small workaround that installs some brownie dependencies. This is wrapped in a the compiler initialization code:
  # https://github.com/eth-brownie/brownie/blob/master/brownie/project/compiler/__init__.py
  # It's pretty handy for caching docker layers and installing all necessary compilers at build time.
  # TODO extend this list with all relevant solidity versions
  print("installing compiler dependencies for brownie")
  Contract.from_explorer("0xD533a949740bb3306d119CC777fa900bA034cd52") #crvToken
  Contract.from_explorer("0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e") #yfiToken
  Contract.from_explorer("0x6b175474e89094c44da98b954eedeac495271d0f") #daiToken