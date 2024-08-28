# Archivo de ayuda para ciertos scripts que nos serán de utilidad
from brownie import network, config, accounts, MockV3Aggregator
# network para saber en que network nos encontramos
# config para poder leer desde nuestro brownie-config.yaml
# accounts En caso de que estemos utilizando Development y necesitemos las cuentas locales

# from web3 import Web3 -- ya no es necesario por que ya no se usa Web3.toWei

DECIMALS = 8
STRARTING_PRICE = 200000000000 # en lugar de Web3.toWei(2000, "ether")

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account(): #Función para obtener la cuenta dependiendo de la network donde nos encontremos
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ): # en caso de estar localemnte en Development
    # if network.show_active() == "development":
        return accounts[0]
    else:   # en caso de estar en cualquier otra sea Sepolia, Mainnet u otra
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"teh active network is {network.show_active()}")
    print(f"Deploying the mocks!")
    MockV3Aggregator.deploy(DECIMALS, STRARTING_PRICE, {"from": get_account()})
    print(f"Mocks Deployed")