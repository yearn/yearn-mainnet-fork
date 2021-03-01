from brownie import *


def main():
    testAccounts = [
        "0x9fde0c31B3b21E8031C08A5c43f851c9C6544E35",
        "0x5fe0676e41741A3a2d84C41DC46cC991812FE110",
        "0x5307DB0c8Fb2Dc616B94f3b2f9fe7a99920e5e52"
    ]

    crvToken = Contract.from_explorer("0xD533a949740bb3306d119CC777fa900bA034cd52")
    yfiToken = Contract.from_explorer("0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e")
    daiToken = Contract.from_explorer("0x6b175474e89094c44da98b954eedeac495271d0f")

    crvWhale = accounts.at("0x4ce799e6ed8d64536b67dd428565d52a531b3640", force=True)
    yfiWhale = accounts.at("0xfeb4acf3df3cdea7399794d0869ef76a6efaff52", force=True)
    daiWhale = accounts.at("0xc3d03e4f041fd4cd388c549ee2a29a9e5075882f", force=True)

    for account in testAccounts:
        crvToken.transfer(account, "1000 ether", {'from': crvWhale})
        yfiToken.transfer(account, "250 ether", {'from': yfiWhale})
        daiToken.transfer(account, "1000000 ether", {'from': daiWhale})
