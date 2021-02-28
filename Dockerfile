FROM python:3.8-buster
ARG WEB3_INFURA_PROJECT_ID
ARG ETHERSCAN_TOKEN

RUN pip3 install eth-brownie
RUN apt update && apt install -y npm
RUN npm install --global ganache-cli
RUN mkdir -p /app/yearn-mainnet-fork
WORKDIR /app/yearn-mainnet-fork

ADD supply_tokens.py /app/yearn-mainnet-fork/supply_tokens.py
RUN brownie run supply_tokens.py --network mainnet-fork
ADD entrypoint.sh /app/yearn-mainnet-fork

ENTRYPOINT ["./entrypoint.sh"]
