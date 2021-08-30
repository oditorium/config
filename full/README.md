# README

## Jupyter Server

_run `jupyter_server` to set up a Jupyter server_


## Ethereum Development

_run `ethereum_dev` to set up a Truffle Ethereum development environment_

see [here](https://cdmana.com/2021/05/20210506173242922f.html)


In one window run

    cd ~
    mkdir webpack
    cd webpack
    truffle unbox webpack
    tree
    truffle compile
    ganache cli

Edit the confiuration file so that it says

    networks: {
        development: {
            port: 8545,
            host: "127.0.0.1",
            network_id: "*",
        },
    }

Then, in another window, run 

    truffle migrate

Other commands

- `truffle init`
- `truffle develop`