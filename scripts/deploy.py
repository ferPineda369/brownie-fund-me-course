from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

from web3 import Web3

def deploy_fund_me():   # Funcion para hacer el Deploy del contrato FundMe.sol
    account = get_account() # Obtenemos una cuenta para poder hacer el deploy

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_addres = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        #price_feed_addres = mock_aggregator.address
        price_feed_addres = MockV3Aggregator[-1].address

    print(account.balance)
    # print(account.address)
    
    # publish_source=True :: "publicame el codigo fuente"
    # Despliegue del contrato con verificación del código fuente
    fund_me = FundMe.deploy(    # Creamos el contrato
        price_feed_addres,
        {"from": account},      # Decimos desde donde tiene que tomar para la Transaction (account)
        publish_source=config["networks"][network.show_active()].get("verify"))

    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()