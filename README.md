# Gas Price Reporting Index

> Collection of All Gas Price Prediction and Reporting Services and their various formats

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6548453.svg)](https://doi.org/10.5281/zenodo.6548453) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/sambacha/gas-reporting)

Previous Releases: <br />
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5702504.svg)](https://doi.org/10.5281/zenodo.5702504)


## SoK EVM Gas Reporting Index: Catalogue of Transaction Pricing Services and their implementation differences 

> [see CITATION.cff](https://github.com/sambacha/gas-reporting/blob/master/CITATION.cff)

### Version 2.0 (2024 Latest)

```citation
Bacha, Sam. (2024). SoK EVM Gas Pricing APIs: Transaction Pricing Services and their implementation differences (Version 2.0.0) [Computer software]. https://doi.org/10.5281/zenodo.1234
```

### Version 1.1.12 (2022 Release)

```
Bacha, S. (2021, 2022). EVM Gas Reporting Index: Catalog of Transaction Pricing Services and their implementation differences (Version 1.1.12) [Computer software]. https://doi.org/10.5281/zenodo.1234
```

```bibtex
@software{Bacha_Gas_Reporting_Index_2022,
author = {Bacha, Sam},
license = {CC-2.5-NC/MIT},
month = {6},
title = {{Gas Reporting Index}},
url = {https://github.com/sambacha/gas-reporting},
version = {1.1.12},
year = {2021-2022}
}
```

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Gas Price Reporting Index](#gas-price-reporting-index)
   * [EVM Gas Reporting Index: Catalogue of Transaction Pricing Services and their implementation differences ](#evm-gas-reporting-index-catalogue-of-transaction-pricing-services-and-their-implementation-differences)
   * [EIP-2930: Optional Access List transactions](#eip-2930-optional-access-list-transactions)
      + [Accessed addresses](#accessed-addresses)
      + [`eth_createAccessList`](#eth_createaccesslist)
         - [Conclusion](#conclusion)
   * [Gas Fee Speed Definitions](#gas-fee-speed-definitions)
   * [Gas Reporting Table Format](#gas-reporting-table-format)
   * [Gas Snapshot Format](#gas-snapshot-format)
      + [JSON-Schema definition](#json-schema-definition)
      + [gas-snapshot](#gas-snapshot)
         - [Example output](#example-output)
   * [eth_maxPriorityFeePerGas](#eth_maxpriorityfeepergas)
      + [Definition](#definition)
      + [Calculating the current maximum priority fee per gas](#calculating-the-current-maximum-priority-fee-per-gas)
      + [Go-Ethereum Calculation ](#go-ethereum-calculation)
   * [eth_feeHistory](#eth_feehistory)
      + [Definition](#definition-1)
   * [Gas Pricing API Providers and Oracles](#gas-pricing-api-providers-and-oracles)
      + [Blocknative](#blocknative)
         - [gas.blocknative.com](#gasblocknativecom)
         - [bnc-ext](#bnc-ext)
         - [BlockNative Chrome Extenstion](#blocknative-chrome-extenstion)
         - [sample response](#sample-response)
      + [Curve-Finance](#curve-finance)
         - [`getGas`](#getgas)
      + [WalletConnect](#walletconnect)
         - [specification](#specification)
         - [sample response](#sample-response-1)
      + [Flashbots](#flashbots)
         - [specification](#specification-1)
         - [request sample](#request-sample)
         - [response](#response)
      + [EtherScan](#etherscan)
      + [GasNow [no longer in service]](#gasnow-no-longer-in-service)
         - [GasNow Legacy](#gasnow-legacy)
      + [Gnosis](#gnosis)
      + [MetaMask](#metamask)
         - [Consensys CoDeFi](#consensys-codefi)
      + [1inch](#1inch)
      + [v1.0](#v10)
      + [v1.2](#v12)
      + [ethGasStation](#ethgasstation)
      + [etherchain.org](#etherchainorg)
      + [etherchain-gasnow](#etherchain-gasnow)
      + [poanetwork](#poanetwork)
      + [Zoltu](#zoltu)
      + [MyCrypto](#mycrypto)
      + [EtherScan](#etherscan-1)
      + [Zapper](#zapper)
      + [archerdao](#archerdao)
      + [gas-ticker](#gas-ticker)
   * [Appendix](#appendix)
      + [Custom Network Over pricing](#custom-network-over-pricing)
      + [URL Index](#url-index)
      + [EVM Params](#evm-params)

<!-- TOC end -->



<!-- TOC --><a name="gas-price-reporting-index"></a>
# Gas Price Reporting Index

> Collection of All Gas Price Prediction and Reporting Services and their various formats

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6548453.svg)](https://doi.org/10.5281/zenodo.6548453) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/sambacha/gas-reporting)

Previous Releases: <br />
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5702504.svg)](https://doi.org/10.5281/zenodo.5702504)


<!-- TOC --><a name="evm-gas-reporting-index-catalogue-of-transaction-pricing-services-and-their-implementation-differences"></a>
## EVM Gas Reporting Index: Catalogue of Transaction Pricing Services and their implementation differences 

> [see CITATION.cff](https://github.com/sambacha/gas-reporting/blob/master/CITATION.cff)

Bacha, Sam. (2024). SoK EVM Gas Pricing APIs: Transaction Pricing Services and their implementation differences (Version 2.0.0) [Computer software]. https://doi.org/10.5281/zenodo.1234

```
Bacha, S. (2021, 2022). EVM Gas Reporting Index: Catalog of Transaction Pricing Services and their implementation differences (Version 1.1.12) [Computer software]. https://doi.org/10.5281/zenodo.1234
```

```bibtex
@software{Bacha_Gas_Reporting_Index_2022,
author = {Bacha, Sam},
license = {CC-2.5-NC/MIT},
month = {6},
title = {{Gas Reporting Index}},
url = {https://github.com/sambacha/gas-reporting},
version = {1.1.12},
year = {2021-2022}
}
```


<!-- TOC --><a name="eip-2930-optional-access-list-transactions"></a>
## EIP-2930: Optional Access List transactions

> [source, @fvictorio/gas-costs-after-berlin#EIP-2930-Optional-Access-List-transactions](https://hackmd.io/@fvictorio/gas-costs-after-berlin#EIP-2930-Optional-Access-List-transactions)

This EIP adds a new type of transaction that can include an access list in the transaction payload. This means that you can declare beforehand which addresses and slots should be considered as accessed before the transaction’s execution starts. For example, an SLOAD of a non-accessed slot costs 2100, but if that slot was included in the transaction’s access list, then that same opcode will cost 100.

But if the gas costs are lower when an address or storage key is already accessed, does this mean that we can add everything to the transaction’s access list and get a gas reduction? Yay, free gas! Well, not exactly, because you also need to pay gas for each address and each storage key that you add.

Let’s see an example. Say we are sending a transaction to contract A. An access list could look like this:

```javascript
accessList: [{
  address: "<address of A>",
  storageKeys: [
    "0x0000000000000000000000000000000000000000000000000000000000000000"
  ]
}]
```
If we send a transaction with this access list, and the first opcode that uses the 0x0 slot is a SLOAD, it will cost 100 instead of 2100. That’s a gas reduction of 2000. But each storage key included in the transaction’s access list has a cost of 1900. So we only save 100 of gas. (If the first opcode to access that slot is an SSTORE instead, we would save 2100 of gas, which means that we’d save 200 of gas in total if we consider the cost of the storage key.)

> You always pay gas for the address in the access list ("<address of A>" in the example).

<!-- TOC --><a name="accessed-addresses"></a>
### Accessed addresses

So far, we’ve been talking only about the `SLOAD` and `SSTORE` opcodes, but those aren’t the only ones that change after Berlin. For example, the CALL opcode had a fixed cost of 700. But after `EIP-2929` its cost is 2600 if the address is not in the access list and 100 if it is. And, like the accessed storage keys, it doesn’t matter what OPCODE accessed that address before (for example, if an `EXTCODESIZE` was called first, then that opcode will cost 2600, and any subsequent `EXTCODESIZE`, `CALL`, `STATICCAL`L that uses the same address will cost 100).

How is this affected by transactions with access lists? For example, if we send a transaction to contract A, and that contract calls another contract B, then we can include an access list like this:

```javascript
accessList: [{ address: "<address of B>", storageKeys: [] }]
```
We’ll have to pay a cost of 2400 to include this access list in the transaction, but then the first opcode that uses the address of B will cost 100 instead of 2600. So we saved 100 of gas by doing this. And if B uses its storage somehow and we know which keys it will use, then we can also include them in the access list and save 100/200 of gas for each one (depending on whether the first opcode is an SLOAD or an SSTORE).

But why are we talking about another contract? What happens with the contract that we are calling? Why don’t we do this?

```javascript
accessList: [
  {address: "<address of A>", storageKeys: []},
  {address: "<address of B>", storageKeys: []},
]
```
We could do it, but it wouldn’t be worth it because EIP-2929 specifies that the address of the contract that is being called (that is, tx.to) is always included in the accessed_addresses list. So we are paying 2400 more for nothing.

Let’s analyze our example of the previous section again:

```javascript
accessList: [{
  address: "<address of A>",
  storageKeys: [
    "0x0000000000000000000000000000000000000000000000000000000000000000"
  ]
}]
```
This will actually be wasteful unless we include several storage keys more. If we assume that a storage key is always used first by an SLOAD, then we need at least 24 storage keys just to break even.

As you can imagine, analyzing this and creating an access list by hand is not fun. Luckily, there is a better way.

<!-- TOC --><a name="eth_createaccesslist"></a>
### `eth_createAccessList`
Geth (starting from version 1.10.2) includes a new eth_createAccessList RPC method that you can use to generate access lists. It is used like eth_estimateGas, but instead of a gas estimation, it returns something like this:

```jsonc
{
  "accessList": [
    {
      "address": "0xb0ee076d7779a6ce152283f009f4c32b5f88756c",
      "storageKeys": [
        "0x0000000000000000000000000000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000000000000000000000000001"
      ]
    }
  ],
  "gasUsed": "0x8496"
}
```
That is, it gives you the list of addresses and storage keys that will be used by that transaction, plus the gas consumed if the access list is included. (And, like eth_estimateGas, this is an estimation; the list could change when the transaction is actually mined.) But, again, this doesn’t mean that this gas will be lower than the gas used if you just send the same transaction without an access list!

<!-- TOC --><a name="conclusion"></a>
#### Conclusion

Does this mean that we always save gas when using transaction’s with access lists? No.

<!-- TOC --><a name="gas-fee-speed-definitions"></a>
## Gas Fee Speed Definitions

- Fastest: next block (i.e. <30 seconds) <br>
- Fast: below 2 minutes (<10 blocks) <br>
- Medium: around 5 minutes (<20 blocks) <br>
- Slow: below 30 minutes (a.k.a safe-low, <120 blocks) <br>


<!-- TOC --><a name="gas-reporting-table-format"></a>
## Gas Reporting Table Format

Gas Reporting from `forge test --gas-report`

> forge snapshot 

| **CONTRACT_NAME:string** |                     |             |             |             |             |
| ------------------------ | ------------------- | ----------- | ----------- | ----------- | ----------- |
| **Deployment Cost**      | **Deployment Size** |             |             |             |             |
| type:number              | type:number         |             |             |             |             |
| **Function Name**        | **min**             | **avg**     | **median**  | **max**     | **# calls** |
| type:string              | type:number         | type:number | type:number | type:number | type:number |

<!-- TOC --><a name="gas-snapshot-format"></a>
## Gas Snapshot Format

> .gas-snapshot

```julia
FooTest:testSetFoo() (gas: 64071)
BarTest:testFuzzCurrentBar(uint256) (runs: 256, μ: 408, ~: 423)
```

<!-- TOC --><a name="json-schema-definition"></a>
### JSON-Schema definition

Each test object represents a test function and has the following properties:

| key     	| boolean    	| value                                                                                           	|
|---------	|------------	|-------------------------------------------------------------------------------------------------	|
| name    	| (required) 	| The name of the test function.                                                                  	|
| gas     	| (optional) 	| The gas used by the test function. This property is required if the test is not a fuzz test.    	|
| runs    	| (optional) 	| The number of runs for the test function. This property is required if the test is a fuzz test. 	|
| avg     	| (optional) 	| The average gas used across all runs. This property is required if the test is a fuzz test.     	|
| median  	| (optional) 	| The median gas used across all runs. This property is required if the test is a fuzz test.      	|


The `oneOf` constraint ensures that a test object must have either the gas property (for non-fuzz tests) or the runs, avg, and median properties (for fuzz tests).

This JSON Schema describes the structure of the .gas-snapshot file format used by Forge. It allows for both regular tests with a single gas value and fuzz tests with multiple runs and statistical data (average and median gas used).

<!-- TOC --><a name="gas-snapshot"></a>
### gas-snapshot

The schema defines an object with a single property tests, which is an array of test objects.

```jsonc
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "tests": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the test function"
          },
          "gas": {
            "type": "integer",
            "description": "The gas used by the test function"
          },
          "runs": {
            "type": "integer",
            "description": "The number of runs for the test function (only applicable for fuzz tests)"
          },
          "avg": {
            "type": "integer",
            "description": "The average gas used across all runs (only applicable for fuzz tests)"
          },
          "median": {
            "type": "integer",
            "description": "The median gas used across all runs (only applicable for fuzz tests)"
          }
        },
        "required": [
          "name"
        ],
        "oneOf": [
          {
            "required": [
              "gas"
            ]
          },
          {
            "required": [
              "runs",
              "avg",
              "median"
            ]
          }
        ]
      }
    }
  },
  "required": [
    "tests"
  ]
}
```
<!-- TOC --><a name="example-output"></a>
#### Example output

```console
╭──────────────────────────┬─────────────────┬───────┬────────┬───────┬─────────╮
│ GasMeterFactory contract ┆                 ┆       ┆        ┆       ┆         │
╞══════════════════════════╪═════════════════╪═══════╪════════╪═══════╪═════════╡
│ Deployment Cost          ┆ Deployment Size ┆       ┆        ┆       ┆         │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ 35287                    ┆ 206             ┆       ┆        ┆       ┆         │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ Function Name            ┆ min             ┆ avg   ┆ median ┆ max   ┆ # calls │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ build                    ┆ 38653           ┆ 38653 ┆ 38653  ┆ 38653 ┆ 15      │
╰──────────────────────────┴─────────────────┴───────┴────────┴───────┴─────────╯
```

<!-- TOC --><a name="eth_maxpriorityfeepergas"></a>
## eth_maxPriorityFeePerGas

<!-- TOC --><a name="definition"></a>
### Definition

> https://github.com/ethereum/execution-apis/blob/main/src/eth/fee_market.yaml

The `eth_maxPriorityFeePerGas` was originally a client specific RPC Method (go-ethereum), it only recently was made part of the official Ethereum JSON-RPC specification. This method was introduced as part of the EIP-1559 (Ethereum Improvement Proposal 1559) transaction pricing mechanism implementation by the go-ethereum team. It is used to retrieve the current maximum priority fee per gas accepted for the network.

You can calculate a default ``maxPriorityFeePerGas`` using ``eth_feeHistory`` when ``eth_maxPriorityFeePerGas`` is not available.

<!-- TOC --><a name="calculating-the-current-maximum-priority-fee-per-gas"></a>
### Calculating the current maximum priority fee per gas

The eth_maxPriorityFeePerGas method allows users, wallets, and dApps to query the Ethereum node and obtain the current maximum priority fee per gas.

The priority fee is an additional fee that can be added to a transaction to incentivize miners to prioritize its inclusion in a block. The returned value represents the maximum priority fee per gas in wei, and this value is a dynamic parameter and can change over time depending on network congestion and block builder preferences.

> It represents the maximum accepted priority fee at a given moment but does not guarantee that a transaction with that priority fee will be included in the next block. Inclusion depends on various factors such as gas price, gas limit, and transaction competition.

<!-- TOC --><a name="go-ethereum-calculation"></a>
### Go-Ethereum Calculation 

Client implementations can vary, for example in go-ethereum (geth) it calculates what is the 60th percentile tip over the last 20 blocks by default.

> https://github.com/ethereum/go-ethereum/blob/f265cc24b4b17b55b468b315303a3a599fc01d81/eth/ethconfig/config.go#L40-L47
> 
```golang
// FullNodeGPO contains default gasprice oracle settings for full node.
var FullNodeGPO = gasprice.Config{
	Blocks:           20,
	Percentile:       60,
	MaxHeaderHistory: 1024,
	MaxBlockHistory:  1024,
	MaxPrice:         gasprice.DefaultMaxPrice,
	Igno
```

Usage:

To use this method, you need to send a JSON-RPC request to an Ethereum node with the method name eth_maxPriorityFeePerGas.

> The request does not require any parameters.

<!-- TOC --><a name="eth_feehistory"></a>
## eth_feeHistory

<!-- TOC --><a name="definition-1"></a>
### Definition

> https://github.com/ethereum/execution-apis/blob/main/src/eth/fee_market.yaml

`eth_feeHistory` returns transaction base fee per gas and effective priority fee per gas for the requested/supported block range.

 > The request does require the following parameters:

`blockCount`: Requested range of blocks. Clients will return less than the requested range if not all blocks are available.    
`rewardPercentiles`: A monotonically increasing list of percentile values. For each block in the requested range, the transactions will be sorted in ascending order by effective tip per gas and the corresponding effective tip for the percentile will be determined, accounting for gas consumed.    
`gasUsedRatio`: An array of block gas used ratios. These are calculated as the ratio of `gasUsed` and `gasLimit`.

<!-- TOC --><a name="gas-pricing-api-providers-and-oracles"></a>
## Gas Pricing API Providers and Oracles

Listed in no particular order. 

> Notice: GasNow as of 2021-10-01 will be shutting down due to SparkPools closure


<!-- TOC --><a name="blocknative"></a>
### Blocknative

> @note there are two seperate entries

<!-- TOC --><a name="gasblocknativecom"></a>
#### gas.blocknative.com

> Note: This is powered by Blocknative's global mempool data platform

> v2 Blocknative

```jsonc
{
    "system": "ethereum",
    "network": "main",
    "unit": "gwei",
    "maxPrice": 50,
    "currentBlockNumber": 15326495,
    "msSinceLastBlock": 40251,
    "blockPrices": [
        {
            "blockNumber": 15326496,
            "estimatedTransactionCount": 322,
            "baseFeePerGas": 11.075381056,
            "estimatedPrices": [
                {
                    "confidence": 99,
                    "price": 13,
                    "maxPriorityFeePerGas": 2.49,
                    "maxFeePerGas": 22.45
                },
                {
                    "confidence": 95,
                    "price": 13,
                    "maxPriorityFeePerGas": 2.13,
                    "maxFeePerGas": 22.09
                },
                {
                    "confidence": 90,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.92,
                    "maxFeePerGas": 21.88
                },
                {
                    "confidence": 80,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.68,
                    "maxFeePerGas": 21.64
                },
                {
                    "confidence": 70,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.58,
                    "maxFeePerGas": 21.54
                }
            ]
        }
    ],
    "estimatedBaseFees": [
        {
            "pending+1": [
                {
                    "confidence": 99,
                    "baseFee": 12.46
                }
            ]
        },
        {
            "pending+2": [
                {
                    "confidence": 99,
                    "baseFee": 14.02
                }
            ]
        },
        {
            "pending+3": [
                {
                    "confidence": 99,
                    "baseFee": 15.77
                }
            ]
        },
        {
            "pending+4": [
                {
                    "confidence": 99,
                    "baseFee": 17.75
                }
            ]
        },
        {
            "pending+5": [
                {
                    "confidence": 99,
                    "baseFee": 19.96
                }
            ]
        }
    ]
}
```

> v1 Blocknative 

```json
{
  "system": "ethereum",
  "network": "main",
  "unit": "gwei",
  "maxPrice": 336,
  "currentBlockNumber": 13095949,
  "msSinceLastBlock": 4542,
  "blockPrices": [
    {
      "blockNumber": 13095950,
      "baseFeePerGas": 113.110076547,
      "estimatedTransactionCount": 172,
      "estimatedPrices": [
        {
          "confidence": 99,
          "price": 129,
          "maxPriorityFeePerGas": 15.96,
          "maxFeePerGas": 242.18
        },
        {
          "confidence": 95,
          "price": 119,
          "maxPriorityFeePerGas": 6.84,
          "maxFeePerGas": 233.06
        },
        {
          "confidence": 90,
          "price": 118,
          "maxPriorityFeePerGas": 5.09,
          "maxFeePerGas": 231.31
        },
        {
          "confidence": 80,
          "price": 116,
          "maxPriorityFeePerGas": 3.21,
          "maxFeePerGas": 229.43
        },
        {
          "confidence": 70,
          "price": 115,
          "maxPriorityFeePerGas": 2.28,
          "maxFeePerGas": 228.5
        }
      ]
    }
  ]
}
```

<!-- TOC --><a name="bnc-ext"></a>
#### bnc-ext

<!-- TOC --><a name="blocknative-chrome-extenstion"></a>
#### BlockNative Chrome Extenstion

[blocknative eth gas estimate extenstion](https://chrome.google.com/webstore/detail/blocknative-eth-gas-estim/ablbagjepecncofimgjmdpnhnfjiecfm/)

[https://blocknative-api.herokuapp.com/data](https://blocknative-api.herokuapp.com/data)

<!-- TOC --><a name="sample-response"></a>
#### sample response

```json
{
  "pendingBlockNumberVal": 13378149,
  "seconds": 17,
  "maxPrice": 768,
  "estimatedTransactions": 279,
  "estimatedPrices": [{
    "confidence": 99,
    "price": 86,
    "maxPriorityFeePerGas": 2.96,
    "maxFeePerGas": 170.76
  }, {
    "confidence": 95,
    "price": 85,
    "maxPriorityFeePerGas": 1.75,
    "maxFeePerGas": 169.55
  }, {
    "confidence": 90,
    "price": 85,
    "maxPriorityFeePerGas": 1.56,
    "maxFeePerGas": 169.36
  }, {
    "confidence": 80,
    "price": 85,
    "maxPriorityFeePerGas": 1.48,
    "maxFeePerGas": 169.28
  }, {
    "confidence": 70,
    "price": 85,
    "maxPriorityFeePerGas": 1.37,
    "maxFeePerGas": 169.17
  }],
  "baseFeePerGas": 83.897778652
}
```
 
<!-- TOC --><a name="curve-finance"></a>
### Curve-Finance
 
<!-- TOC --><a name="getgas"></a>
#### `getGas`
 
[https://api.curve.fi/api/getGas](https://api.curve.fi/api/getGas)
 

```bash
 https://api.curve.fi/api/getGas
```
 
```json
{
    "success": true,
    "data": {
        "gas": {
            "rapid": 36000000000,
            "fast": 35000000000,
            "standard": 35000000000,
            "slow": 35000000000
        },
        "eip1559Gas": {
            "base": 35292604977,
            "prio": [
                1220000000,
                500000000,
                350000000,
                230000000
            ],
            "max": [
                56110000000,
                55390000000,
                55240000000,
                55120000000
            ]
        }
    },
    "generatedTimeMs": 1668181797396
}
``` 

<!-- TOC --><a name="walletconnect"></a>
### WalletConnect

<!-- TOC --><a name="specification"></a>
#### specification

[https://github.com/pedrouid/ethereum-api#api](https://github.com/pedrouid/ethereum-api#api)

[https://ethereum-api.xyz/gas-prices](https://ethereum-api.xyz/gas-prices)

```
http GET https://ethereum-api.xyz/gas-prices
```

<!-- TOC --><a name="sample-response-1"></a>
#### sample response

```json
{
  "timestamp": 1633172858972,
  "slow": {
    "time": 756,
    "price": 39
  },
  "average": {
    "time": 84,
    "price": 42
  },
  "fast": {
    "time": 30,
    "price": 54
  },
  "fastest": {
    "time": 24,
    "price": 58
  }
}
```

<!-- TOC --><a name="flashbots"></a>
### Flashbots

> eth_gasFee

<!-- TOC --><a name="specification-1"></a>
#### specification

[see source documentation](https://docs.flashbots.net/flashbots-protect/api/json-rpc#eth_gasfees)

// prettier-ignore

```jsonc
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    block,                     // Number, current block number
    baseFeePerGas,             // String, a hex number for the baseFee at the current block
    default: {
      maxFeePerGas,            // String, a hex number for the recommended default maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended default maxPriorityFeePerGas
    },
    low: {
      maxFeePerGas,            // String, a hex number for the recommended low maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended low maxPriorityFeePerGas
    },
    med: {
      maxFeePerGas,            // String, a hex number for the recommended med maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended med maxPriorityFeePerGas
    },
    high: {
      maxFeePerGas,            // String, a hex number for the recommended high maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended high maxPriorityFeePerGas
    },
  }
}
```

<!-- TOC --><a name="request-sample"></a>
#### request sample

```sh
curl -s -L -X POST 'https://protection.flashbots.net/v1/rpc' \
-H 'Content-Type: application/json' \
--data-raw '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_gasFees",
  "params": []
}'
```

<!-- TOC --><a name="response"></a>
#### response

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "block": 13467179,
        "baseFeePerGas": "0x0bd0606957",
        "default": {
            "maxFeePerGas": "0x12ec776ebc",
            "maxPriorityFeePerGas": "0x01e47257df"
        },
        "low": {
            "maxFeePerGas": "0x11d7682749",
            "maxPriorityFeePerGas": "0xe45ecec3"
        },
        "med": {
            "maxFeePerGas": "0x12ec776ebc",
            "maxPriorityFeePerGas": "0x01e47257df"
        },
        "high": {
            "maxFeePerGas": "0x1412552c31",
            "maxPriorityFeePerGas": "0x0302bff9d4"
        }
    }
}
```

<!-- TOC --><a name="etherscan"></a>
### EtherScan

[https://docs.etherscan.io/api-endpoints/gas-tracker](https://docs.etherscan.io/api-endpoints/gas-tracker)

[https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken](https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken)

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "13053741",
    "SafeGasPrice": "20",
    "ProposeGasPrice": "22",
    "FastGasPrice": "24",
    "suggestBaseFee": "19.230609716",
    "gasUsedRatio": "0.370119078777807,0.8954731,0.550911766666667,0.212457033333333,0.552463633333333"
  }
}
```

<!-- TOC --><a name="gasnow-no-longer-in-service"></a>
### GasNow [no longer in service]

> gasnow.org/taichi

```bash
wss://www.gasnow.org/ws
```

```json
{
  "type": "gasprice",
  "data": {
    "gasPrices": {
      "rapid": 67000000000,
      "fast": 64455346560,
      "standard": 63455346560,
      "slow": 63455346560
    },
    "cumulativeCounts": [
      {
        "gwei": "63",
        "cumulativeCount": 93
      },
      {
        "gwei": "64",
        "cumulativeCount": 81
      },
      {
        "gwei": "65",
        "cumulativeCount": 65
      },
      {
        "gwei": "66",
        "cumulativeCount": 35
      },
      {
        "gwei": "67",
        "cumulativeCount": 34
      },
      {
        "gwei": "68",
        "cumulativeCount": 32
      },
      {
        "gwei": "69",
        "cumulativeCount": 30
      },
      {
        "gwei": "70",
        "cumulativeCount": 25
      },
      {
        "gwei": "71",
        "cumulativeCount": 22
      },
      {
        "gwei": "73",
        "cumulativeCount": 21
      },
      {
        "gwei": "74",
        "cumulativeCount": 19
      },
      {
        "gwei": "75",
        "cumulativeCount": 17
      },
      {
        "gwei": "78",
        "cumulativeCount": 16
      },
      {
        "gwei": "80",
        "cumulativeCount": 15
      },
      {
        "gwei": "81",
        "cumulativeCount": 13
      },
      {
        "gwei": "87",
        "cumulativeCount": 12
      },
      {
        "gwei": "88",
        "cumulativeCount": 11
      },
      {
        "gwei": "89",
        "cumulativeCount": 9
      },
      {
        "gwei": "94",
        "cumulativeCount": 8
      },
      {
        "gwei": "96",
        "cumulativeCount": 6
      },
      {
        "gwei": "98",
        "cumulativeCount": 5
      },
      {
        "gwei": "109",
        "cumulativeCount": 4
      },
      {
        "gwei": "112",
        "cumulativeCount": 3
      },
      {
        "gwei": "120",
        "cumulativeCount": 2
      },
      {
        "gwei": "221",
        "cumulativeCount": 1
      }
    ],
    "timestamp": 1629975608579
  }
}
```

<br>

<!-- TOC --><a name="gasnow-legacy"></a>
#### GasNow Legacy

```json
{
  "code": 200,
  "data": {
    "rapid": 131000000000,
    "fast": 116000000000,
    "standard": 100000000000,
    "slow": 91600000000,
    "timestamp": 1613914581546
  }
}
```

<!-- TOC --><a name="gnosis"></a>
### Gnosis

[endpoint url](https://safe-relay.gnosis.io/api/v1/gas-station/)

```json
{
  "lastUpdate": "2021-02-21T13:38:38.945308Z",
  "lowest": "2",
  "safeLow": "109000000001",
  "standard": "119000000001",
  "fast": "131000000001",
  "fastest": "10680081443136"
}
```

<!-- TOC --><a name="metamask"></a>
### MetaMask

<!-- TOC --><a name="consensys-codefi"></a>
#### Consensys CoDeFi

[endpoint url](https://api.metaswap.codefi.network/gasPrices)

```json
{
  "low": {
    "suggestedMaxPriorityFeePerGas": "1.37826449268",
    "suggestedMaxFeePerGas": "70.067746222",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 30000
  },
  "medium": {
    "suggestedMaxPriorityFeePerGas": "1.5",
    "suggestedMaxFeePerGas": "81.637728684",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 45000
  },
  "high": {
    "suggestedMaxPriorityFeePerGas": "2",
    "suggestedMaxFeePerGas": "93.585975639",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 60000
  },
  "estimatedBaseFee": "57.241234774",
   "networkCongestion": 0.5,
}
```

```json
{
  "SafeGasPrice": "100",
  "ProposeGasPrice": "108",
  "FastGasPrice": "119"
}
```

<!-- TOC --><a name="1inch"></a>
### 1inch

[https://gas-price-api.1inch.exchange/v1.0](https://gas-price-api.1inch.exchange/v1.0)

<!-- TOC --><a name="v10"></a>
### v1.0

```json
{
  "fast": 96820000000,
  "instant": 125000000000,
  "standard": 90000000000,
  "slow": 82000000000
}
```

<!-- TOC --><a name="v12"></a>
### v1.2

> gas-price-api.1inch.io/v.1.2

```json
{
    "baseFee": "93731028208",
    "low": {
        "maxPriorityFeePerGas": "1170000000",
        "maxFeePerGas": "94901028208"
    },
    "medium": {
        "maxPriorityFeePerGas": "2340000000",
        "maxFeePerGas": "96071028208"
    },
    "high": {
        "maxPriorityFeePerGas": "5850000000",
        "maxFeePerGas": "99581028208"
    },
    "instant": {
        "maxPriorityFeePerGas": "5850000000",
        "maxFeePerGas": "129455336670"
    }
}
```

<!-- TOC --><a name="ethgasstation"></a>
### ethGasStation

[endpoint url](https://ethgasstation.info/json/ethgasAPI.json)

```json
{
  "fast": 1200.0,
  "fastest": 1200.0,
  "safeLow": 1020.0,
  "average": 1050.0,
  "block_time": 13.327868852459016,
  "blockNum": 11900622,
  "speed": 0.997822721438169,
  "safeLowWait": 12.9,
  "avgWait": 1.5,
  "fastWait": 0.5,
  "fastestWait": 0.5,
  "gasPriceRange": {
    "1200": 0.5,
    "1180": 0.5,
    "1160": 0.6,
    "1140": 0.6,
    "1120": 0.7,
    "1100": 0.7,
    "1080": 1.2,
    "1060": 1.5,
    "1040": 11.5,
    "1020": 12.9,
    "1000": 14.3,
    "980": 17.4,
    "960": 18.9,
    "940": 21.1,
    "920": 222.1,
    "900": 222.1,
    "880": 222.1,
    "860": 222.1,
    "840": 222.1,
    "820": 222.1,
    "800": 222.1,
    "780": 222.1,
    "760": 222.1,
    "740": 222.1,
    "720": 222.1,
    "700": 222.1,
    "680": 222.1,
    "660": 222.1,
    "640": 222.1,
    "620": 222.1,
    "600": 222.1,
    "580": 222.1,
    "560": 222.1,
    "540": 222.1,
    "520": 222.1,
    "500": 222.1,
    "480": 222.1,
    "460": 222.1,
    "440": 222.1,
    "420": 222.1,
    "400": 222.1,
    "380": 222.1,
    "360": 222.1,
    "340": 222.1,
    "320": 222.1,
    "300": 222.1,
    "280": 222.1,
    "260": 222.1,
    "240": 222.1,
    "220": 222.1,
    "200": 222.1,
    "190": 222.1,
    "180": 222.1,
    "170": 222.1,
    "160": 222.1,
    "150": 222.1,
    "140": 222.1,
    "130": 222.1,
    "120": 222.1,
    "110": 222.1,
    "100": 222.1,
    "90": 222.1,
    "80": 222.1,
    "70": 222.1,
    "60": 222.1,
    "50": 222.1,
    "40": 222.1,
    "30": 222.1,
    "20": 222.1,
    "10": 222.1,
    "8": 222.1,
    "6": 222.1,
    "4": 222.1,
    "1050": 1.5
  }
}
```

```json
{
  "fast": 1200.0,
  "fastest": 1200.0,
  "safeLow": 1020.0,
  "average": 1050.0,
  "block_time": 13.327868852459016,
  "blockNum": 11900622,
  "speed": 0.997822721438169,
  "safeLowWait": 12.9,
  "avgWait": 1.5,
  "fastWait": 0.5,
  "fastestWait": 0.5,
  "gasPriceRange": {
    "1200": 0.5,
    "1180": 0.5,
    "1160": 0.6,
    "1140": 0.6,
    "1120": 0.7,
    "1100": 0.7,
    "1080": 1.2,
    "1060": 1.5,
    "1040": 11.5,
    "1020": 12.9,
    "1000": 14.3,
    "980": 17.4,
    "960": 18.9,
    "940": 21.1,
    "920": 222.1,
    "900": 222.1,
    "880": 222.1,
    "860": 222.1,
    "840": 222.1,
    "820": 222.1,
    "800": 222.1,
    "780": 222.1,
    "760": 222.1,
    "740": 222.1,
    "720": 222.1,
    "700": 222.1,
    "680": 222.1,
    "660": 222.1,
    "640": 222.1,
    "620": 222.1,
    "600": 222.1,
    "580": 222.1,
    "560": 222.1,
    "540": 222.1,
    "520": 222.1,
    "500": 222.1,
    "480": 222.1,
    "460": 222.1,
    "440": 222.1,
    "420": 222.1,
    "400": 222.1,
    "380": 222.1,
    "360": 222.1,
    "340": 222.1,
    "320": 222.1,
    "300": 222.1,
    "280": 222.1,
    "260": 222.1,
    "240": 222.1,
    "220": 222.1,
    "200": 222.1,
    "190": 222.1,
    "180": 222.1,
    "170": 222.1,
    "160": 222.1,
    "150": 222.1,
    "140": 222.1,
    "130": 222.1,
    "120": 222.1,
    "110": 222.1,
    "100": 222.1,
    "90": 222.1,
    "80": 222.1,
    "70": 222.1,
    "60": 222.1,
    "50": 222.1,
    "40": 222.1,
    "30": 222.1,
    "20": 222.1,
    "10": 222.1,
    "8": 222.1,
    "6": 222.1,
    "4": 222.1,
    "1050": 1.5
  }
}
```

<!-- TOC --><a name="etherchainorg"></a>
### etherchain.org

[endpoint url](https://www.etherchain.org/api/gasPriceOracle)

```json
{"safeLow":1,"standard":1,"fast":1.5,"fastest":2,"currentBaseFee":72.5,"recommendedBaseFee":147.2}
```

```json
{ "safeLow": 102, "standard": 105, "fast": 114.6, "fastest": 120 }
```

<!-- TOC --><a name="etherchain-gasnow"></a>
### etherchain-gasnow

[https://etherchain.org/api/gasnow](https://etherchain.org/api/gasnow)

```js
{code: 200, data: {rapid: 60000000000, fast: 39962373278, standard: 24406984375, slow: 19550000000,…}}
```

```javascript
code: 200
data: {rapid: 60000000000, fast: 39962373278, standard: 24406984375, slow: 19550000000,…}
fast: 39962373278
priceUSD: 1818.52
rapid: 60000000000
slow: 19550000000
standard: 24406984375
timestamp: 1654245505826
```

> Response

```json
{"code":200,"data":{"rapid":65265049007,"fast":49988581398,"standard":23000000000,"slow":19550000000,"timestamp":1654245243247,"priceUSD":1818.52}}
```

> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "$id": "etherchain_gasnow",
  "type": "object",
  "properties": {
    "code": {
      "type": "integer"
    },
    "data": {
      "type": "object",
      "properties": {
        "rapid": {
          "type": "integer"
        },
        "fast": {
          "type": "integer"
        },
        "standard": {
          "type": "integer"
        },
        "slow": {
          "type": "integer"
        },
        "timestamp": {
          "type": "integer"
        },
        "priceUSD": {
          "type": "number"
        }
      },
      "required": [
        "rapid",
        "fast",
        "standard",
        "slow",
        "timestamp",
        "priceUSD"
      ]
    }
  },
  "required": [
    "code",
    "data"
  ]
}
```

<!-- TOC --><a name="poanetwork"></a>
### poanetwork

[endpoint url](https://gasprice.poa.network/)

```json
{
  "health": true,
  "block_number": 11900628,
  "slow": 101.0,
  "standard": 107.0,
  "fast": 115.0,
  "instant": 130.8,
  "block_time": 13.191
}
```

```json
{
  "health": true,
  "block_number": 11900628,
  "slow": 101.0,
  "standard": 107.0,
  "fast": 115.0,
  "instant": 130.8,
  "block_time": 13.191
}
```

<!-- TOC --><a name="zoltu"></a>
### Zoltu

> nanoeth is the **SI** nomenclature for `gwei`

```json
{
  "number_of_blocks": 200,
  "latest_block_number": 11907178,
  "percentile_1": "1e-9 nanoeth",
  "percentile_2": "0.00001 nanoeth",
  "percentile_3": "0.000011001 nanoeth",
  "percentile_4": "1 nanoeth",
  "percentile_5": "6 nanoeth",
  "percentile_10": "10 nanoeth",
  "percentile_15": "152 nanoeth",
  "percentile_20": "170 nanoeth",
  "percentile_25": "181.5 nanoeth",
  "percentile_30": "190.000001459 nanoeth",
  "percentile_35": "200 nanoeth",
  "percentile_40": "214.76 nanoeth",
  "percentile_45": "222.814063547 nanoeth",
  "percentile_50": "229.9 nanoeth",
  "percentile_55": "232 nanoeth",
  "percentile_60": "245 nanoeth",
  "percentile_65": "256 nanoeth",
  "percentile_70": "262 nanoeth",
  "percentile_75": "270.6 nanoeth",
  "percentile_80": "278 nanoeth",
  "percentile_85": "289.02 nanoeth",
  "percentile_90": "300 nanoeth",
  "percentile_95": "314.4 nanoeth",
  "percentile_96": "315.21 nanoeth",
  "percentile_97": "316.075841562 nanoeth",
  "percentile_98": "325 nanoeth",
  "percentile_99": "326 nanoeth",
  "percentile_100": "348 nanoeth"
}
```

<!-- TOC --><a name="mycrypto"></a>
### MyCrypto

```json
{
  "safeLow": 159,
  "standard": 184,
  "fast": 262,
  "fastest": 289,
  "blockNum": 11907235
}
```

```json
{
  "safeLow": 159,
  "standard": 184,
  "fast": 262,
  "fastest": 289,
  "blockNum": 11907235
}
```

<!-- TOC --><a name="etherscan-1"></a>
### EtherScan

[api endpoint _key required_](https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=${YOUR_API_KEY})

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "11907242",
    "SafeGasPrice": "248",
    "ProposeGasPrice": "269",
    "FastGasPrice": "294"
  }
}
```

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "11907242",
    "SafeGasPrice": "248",
    "ProposeGasPrice": "269",
    "FastGasPrice": "294"
  }
}
```

<!-- TOC --><a name="zapper"></a>
### Zapper

[http://api.zapper.fi/v1/gas-price](http://api.zapper.fi/v1/gas-price)

```json
{
  "standard": 113,
  "fast": 114,
  "instant": 136
}
```

<!-- TOC --><a name="archerdao"></a>
### archerdao

[https://api.archerdao.io/v1/gas](https://api.archerdao.io/v1/gas)

```json
{
  "code": 200,
  "data": {
    "immediate": "228202648099",
    "rapid": "67236905683",
    "fast": "13591066085",
    "standard": "1101380018",
    "slow": "0",
    "slower": "0",
    "slowest": "0"
  }
}
```

<!-- TOC --><a name="gas-ticker"></a>
### gas-ticker

[Gas Ticker by ricmoo](https://github.com/ricmoo/gas-ticker)

```jsonc
{
  "blockNumber": 14610954,
  "timestamp": 1650309194.438,
  "slow": {
    "min": 29.397486945,
    "max": 70.143180307,
    "sum": 13465.490242759988,
    "count": 385,
    "mean": 34.97529933184413,
    "median": 35,
    "tp90": 38,
    "stdDev": 5.992331436594249,
    "target90": 37.265690661,
    "targetStdDev": 2.7612260317587007,
    "targetCount": 266,
    "targetBest": 30,
    "targetWorst": 39.532494062
  },
  "medium": {
    "min": 29.397486945,
    "max": 62.428616398,
    "sum": 29594.27666106807,
    "count": 680,
    "mean": 43.520995089805986,
    "median": 39.038827568,
    "tp90": 52.433561707,
    "stdDev": 8.816041449214934,
    "target90": 50,
    "targetStdDev": 4.467921632212077,
    "targetCount": 470,
    "targetBest": 34.911631032,
    "targetWorst": 52.3082
  },
  "fast": {
    "min": 29.397486945,
    "max": 1200.988196226,
    "sum": 753432.9418861985,
    "count": 14637,
    "mean": 51.47454682559257,
    "median": 48.554602972,
    "tp90": 59.570121624,
    "stdDev": 24.12932660961557,
    "target90": 60.216413805,
    "targetStdDev": 6.10997036680254,
    "targetCount": 10100,
    "targetBest": 38.822145579,
    "targetWorst": 64.139501286
  }
}
```

<!-- TOC --><a name="appendix"></a>
## Appendix

<!-- TOC --><a name="custom-network-over-pricing"></a>
### Custom Network Over pricing

Metamask will pad the estimated gas without exceeding the most recent block `gasLimit`. However, **If the
network is a a custom network it will return the `eth_estimateGas` value**

[see metamask/controllers](https://github.com/MetaMask/controllers/blob/77b1410a0611bbea785e5528b44143aebe5d407f/src/transaction/TransactionController.ts#L995)

<!-- TOC --><a name="url-index"></a>
### URL Index

Current offchain list:

- https://gas,blocknative.com/
- https://ethgasstation.info/json/ethgasAPI.json
- https://www.etherchain.org/api/gasPriceOracle
- https://gasprice.poa.network/
- https://www.gasnow.org/api/v3/gas/price

<!-- TOC --><a name="evm-params"></a>
### EVM Params

| Key | Value | Description |
|---|---|---|
| JumpdestGas uint64 | 1 | Once per JUMPDEST operation. |
| EpochDuration uint64 | 30000 | Duration between proof-of-work epochs. |
| CreateDataGas uint64 | 200 |  |
| CallCreateDepth uint64 | 1024 | Maximum depth of call/create stack. |
| ExpGas uint64 | 10 | Once per EXP instruction |
| LogGas uint64 | 375 | Per LOG* operation. |
| CopyGas uint64 | 3 |  |
| StackLimit uint64 | 1024 | Maximum size of VM stack allowed. |
| TierStepGas uint64 | 0 | Once per operation, for a selection of them. |
| LogTopicGas uint64 | 375 | Multiplied by the * of the LOG*, per LOG transaction. e.g. LOG0 incurs 0 * c_txLogTopicGas, LOG4 incurs 4 * c_txLogTopicGas. |
| CreateGas uint64 | 32000 | Once per CREATE operation & contract-creation transaction. |
| Create2Gas uint64 | 32000 | Once per CREATE2 operation |
| SelfdestructRefundGas uint64 | 24000 | Refunded following a selfdestruct operation. |
| MemoryGas uint64 | 3 | Times the address of the (highest referenced byte in memory + 1). NOTE: referencing happens on read, write and in instructions such as RETURN and CALL. |
| TxDataNonZeroGasFrontier uint64 | 68 | Per byte of data attached to a transaction that is not equal to zero. NOTE: Not payable on data of calls between transactions. |
| TxDataNonZeroGasEIP2028 uint64 | 16 | Per byte of non zero data attached to a transaction after EIP 2028 (part in Istanbul) |
| TxAccessListAddressGas uint64 | 2400 | Per address specified in EIP 2930 access list |
| TxAccessListStorageKeyGas uint64 | 1900 | Per storage key specified in EIP 2930 access list |
| CallGasFrontier uint64 | 40 | Once per CALL operation & message call transaction. |
| CallGasEIP150 uint64 | 700 | Static portion of gas for CALL-derivates after EIP 150 (Tangerine) |
| BalanceGasFrontier uint64 | 20 | The cost of a BALANCE operation |
| BalanceGasEIP150 uint64 | 400 | The cost of a BALANCE operation after Tangerine |
| BalanceGasEIP1884 uint64 | 700 | The cost of a BALANCE operation after EIP 1884 (part of Istanbul) |
| ExtcodeSizeGasFrontier uint64 | 20 | Cost of EXTCODESIZE before EIP 150 (Tangerine) |
| ExtcodeSizeGasEIP150 uint64 | 700 | Cost of EXTCODESIZE after EIP 150 (Tangerine) |
| SloadGasFrontier uint64 | 50 |  |
| SloadGasEIP150 uint64 | 200 |  |
| SloadGasEIP1884 uint64 | 800 | Cost of SLOAD after EIP 1884 (part of Istanbul) |
| SloadGasEIP2200 uint64 | 800 | Cost of SLOAD after EIP 2200 (part of Istanbul) |
| ExtcodeHashGasConstantinople uint64 | 400 | Cost of EXTCODEHASH (introduced in Constantinople) |
| ExtcodeHashGasEIP1884 uint64 | 700 | Cost of EXTCODEHASH after EIP 1884 (part in Istanbul) |
| SelfdestructGasEIP150 uint64 | 5000 | Cost of SELFDESTRUCT post EIP 150 (Tangerine) |
| GasLimitBoundDivisor uint64 | 1024 | The bound divisor of the gas limit, used in update calculations. |
| MinGasLimit uint64 | 5000 | Minimum the gas limit may ever be. |
| MaxGasLimit uint64 | 0x7fffffffffffffff | Maximum the gas limit (2^63-1). |
| GenesisGasLimit uint64 | 4712388 | Gas limit of the Genesis block. |
| MaximumExtraDataSize uint64 | 32 | Maximum size extra data may be after Genesis. |
| ExpByteGas uint64 | 10 | Times ceil(log256(exponent)) for the EXP instruction. |
| SloadGas uint64 | 50 | Multiplied by the number of 32-byte words that are copied (round up) for any *COPY operation and added. |
| CallValueTransferGas uint64 | 9000 | Paid for CALL when the value transfer is non-zero. |
| CallNewAccountGas uint64 | 25000 | Paid for CALL when the destination address didn't exist prior. |
| TxGas uint64 | 21000 | Per transaction not creating a contract. NOTE: Not payable on data of calls between transactions. |
| TxGasContractCreation uint64 | 53000 | Per transaction that creates a contract. NOTE: Not payable on data of calls between transactions. |
| TxDataZeroGas uint64 | 4 | Per byte of data attached to a transaction that equals zero. NOTE: Not payable on data of calls between transactions. |
| QuadCoeffDiv uint64 | 512 | Divisor for the quadratic particle of the memory cost equation. |
| LogDataGas uint64 | 8 | Per byte in a LOG* operation's data. |
| CallStipend uint64 | 2300 | Free gas given at beginning of call. |
| Keccak256Gas uint64 | 30 | Once per KECCAK256 operation. |
| Keccak256WordGas uint64 | 6 | Once per word of the KECCAK256 operation's data. |
| SstoreSetGas uint64 | 20000 | Once per SSTORE operation. |
| SstoreResetGas uint64 | 5000 | Once per SSTORE operation if the zeroness changes from zero. |
| SstoreClearGas uint64 | 5000 | Once per SSTORE operation if the zeroness doesn't change. |
| SstoreRefundGas uint64 | 15000 | Once per SSTORE operation if the zeroness changes to zero. |
| NetSstoreNoopGas uint64 | 200 | Once per SSTORE operation if the value doesn't change. |
| NetSstoreInitGas uint64 | 20000 | Once per SSTORE operation from clean zero. |
| NetSstoreCleanGas uint64 | 5000 | Once per SSTORE operation from clean non-zero. |
| NetSstoreDirtyGas uint64 | 200 | Once per SSTORE operation from dirty. |
| NetSstoreClearRefund uint64 | 15000 | Once per SSTORE operation for clearing an originally existing storage slot |
| NetSstoreResetRefund uint64 | 4800 | Once per SSTORE operation for resetting to the original non-zero value |
| NetSstoreResetClearRefund uint64 | 19800 | Once per SSTORE operation for resetting to the original zero value |
| SstoreSentryGasEIP2200 uint64 | 2300 | Minimum gas required to be present for an SSTORE call, not consumed |
| SstoreSetGasEIP2200 uint64 | 20000 | Once per SSTORE operation from clean zero to non-zero |
| SstoreResetGasEIP2200 uint64 | 5000 | Once per SSTORE operation from clean non-zero to something else |
| SstoreClearsScheduleRefundEIP2200 uint64 | 15000 | Once per SSTORE operation for clearing an originally existing storage slot |
| ColdAccountAccessCostEIP2929 | uint64(2600) | COLD_ACCOUNT_ACCESS_COST |
| ColdSloadCostEIP2929 | uint64(2100) | COLD_SLOAD_COST |
| WarmStorageReadCostEIP2929 | uint64(100) | WARM_STORAGE_READ_COST |


## EIP-2930: Optional Access List transactions

> [source, @fvictorio/gas-costs-after-berlin#EIP-2930-Optional-Access-List-transactions](https://hackmd.io/@fvictorio/gas-costs-after-berlin#EIP-2930-Optional-Access-List-transactions)

This EIP adds a new type of transaction that can include an access list in the transaction payload. This means that you can declare beforehand which addresses and slots should be considered as accessed before the transaction’s execution starts. For example, an SLOAD of a non-accessed slot costs 2100, but if that slot was included in the transaction’s access list, then that same opcode will cost 100.

But if the gas costs are lower when an address or storage key is already accessed, does this mean that we can add everything to the transaction’s access list and get a gas reduction? Yay, free gas! Well, not exactly, because you also need to pay gas for each address and each storage key that you add.

Let’s see an example. Say we are sending a transaction to contract A. An access list could look like this:

```javascript
accessList: [{
  address: "<address of A>",
  storageKeys: [
    "0x0000000000000000000000000000000000000000000000000000000000000000"
  ]
}]
```
If we send a transaction with this access list, and the first opcode that uses the 0x0 slot is a SLOAD, it will cost 100 instead of 2100. That’s a gas reduction of 2000. But each storage key included in the transaction’s access list has a cost of 1900. So we only save 100 of gas. (If the first opcode to access that slot is an SSTORE instead, we would save 2100 of gas, which means that we’d save 200 of gas in total if we consider the cost of the storage key.)

> You always pay gas for the address in the access list ("<address of A>" in the example).

### Accessed addresses

So far, we’ve been talking only about the `SLOAD` and `SSTORE` opcodes, but those aren’t the only ones that change after Berlin. For example, the CALL opcode had a fixed cost of 700. But after `EIP-2929` its cost is 2600 if the address is not in the access list and 100 if it is. And, like the accessed storage keys, it doesn’t matter what OPCODE accessed that address before (for example, if an `EXTCODESIZE` was called first, then that opcode will cost 2600, and any subsequent `EXTCODESIZE`, `CALL`, `STATICCAL`L that uses the same address will cost 100).

How is this affected by transactions with access lists? For example, if we send a transaction to contract A, and that contract calls another contract B, then we can include an access list like this:

```javascript
accessList: [{ address: "<address of B>", storageKeys: [] }]
```
We’ll have to pay a cost of 2400 to include this access list in the transaction, but then the first opcode that uses the address of B will cost 100 instead of 2600. So we saved 100 of gas by doing this. And if B uses its storage somehow and we know which keys it will use, then we can also include them in the access list and save 100/200 of gas for each one (depending on whether the first opcode is an SLOAD or an SSTORE).

But why are we talking about another contract? What happens with the contract that we are calling? Why don’t we do this?

```javascript
accessList: [
  {address: "<address of A>", storageKeys: []},
  {address: "<address of B>", storageKeys: []},
]
```
We could do it, but it wouldn’t be worth it because EIP-2929 specifies that the address of the contract that is being called (that is, tx.to) is always included in the accessed_addresses list. So we are paying 2400 more for nothing.

Let’s analyze our example of the previous section again:

```javascript
accessList: [{
  address: "<address of A>",
  storageKeys: [
    "0x0000000000000000000000000000000000000000000000000000000000000000"
  ]
}]
```
This will actually be wasteful unless we include several storage keys more. If we assume that a storage key is always used first by an SLOAD, then we need at least 24 storage keys just to break even.

As you can imagine, analyzing this and creating an access list by hand is not fun. Luckily, there is a better way.

### `eth_createAccessList`
Geth (starting from version 1.10.2) includes a new eth_createAccessList RPC method that you can use to generate access lists. It is used like eth_estimateGas, but instead of a gas estimation, it returns something like this:

```jsonc
{
  "accessList": [
    {
      "address": "0xb0ee076d7779a6ce152283f009f4c32b5f88756c",
      "storageKeys": [
        "0x0000000000000000000000000000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000000000000000000000000001"
      ]
    }
  ],
  "gasUsed": "0x8496"
}
```
That is, it gives you the list of addresses and storage keys that will be used by that transaction, plus the gas consumed if the access list is included. (And, like eth_estimateGas, this is an estimation; the list could change when the transaction is actually mined.) But, again, this doesn’t mean that this gas will be lower than the gas used if you just send the same transaction without an access list!

#### Conclusion

Does this mean that we always save gas when using transaction’s with access lists? No.

## Gas Fee Speed Definitions

- Fastest: next block (i.e. <30 seconds) <br>
- Fast: below 2 minutes (<10 blocks) <br>
- Medium: around 5 minutes (<20 blocks) <br>
- Slow: below 30 minutes (a.k.a safe-low, <120 blocks) <br>


## Gas Reporting Table Format

Gas Reporting from `forge test --gas-report`

> forge snapshot 

| **CONTRACT_NAME:string** |                     |             |             |             |             |
| ------------------------ | ------------------- | ----------- | ----------- | ----------- | ----------- |
| **Deployment Cost**      | **Deployment Size** |             |             |             |             |
| type:number              | type:number         |             |             |             |             |
| **Function Name**        | **min**             | **avg**     | **median**  | **max**     | **# calls** |
| type:string              | type:number         | type:number | type:number | type:number | type:number |

## Gas Snapshot Format

> .gas-snapshot

```julia
FooTest:testSetFoo() (gas: 64071)
BarTest:testFuzzCurrentBar(uint256) (runs: 256, μ: 408, ~: 423)
```

### JSON-Schema definition

Each test object represents a test function and has the following properties:

| key     	| boolean    	| value                                                                                           	|
|---------	|------------	|-------------------------------------------------------------------------------------------------	|
| name    	| (required) 	| The name of the test function.                                                                  	|
| gas     	| (optional) 	| The gas used by the test function. This property is required if the test is not a fuzz test.    	|
| runs    	| (optional) 	| The number of runs for the test function. This property is required if the test is a fuzz test. 	|
| avg     	| (optional) 	| The average gas used across all runs. This property is required if the test is a fuzz test.     	|
| median  	| (optional) 	| The median gas used across all runs. This property is required if the test is a fuzz test.      	|


The `oneOf` constraint ensures that a test object must have either the gas property (for non-fuzz tests) or the runs, avg, and median properties (for fuzz tests).

This JSON Schema describes the structure of the .gas-snapshot file format used by Forge. It allows for both regular tests with a single gas value and fuzz tests with multiple runs and statistical data (average and median gas used).

### gas-snapshot

The schema defines an object with a single property tests, which is an array of test objects.

```jsonc
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "tests": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the test function"
          },
          "gas": {
            "type": "integer",
            "description": "The gas used by the test function"
          },
          "runs": {
            "type": "integer",
            "description": "The number of runs for the test function (only applicable for fuzz tests)"
          },
          "avg": {
            "type": "integer",
            "description": "The average gas used across all runs (only applicable for fuzz tests)"
          },
          "median": {
            "type": "integer",
            "description": "The median gas used across all runs (only applicable for fuzz tests)"
          }
        },
        "required": [
          "name"
        ],
        "oneOf": [
          {
            "required": [
              "gas"
            ]
          },
          {
            "required": [
              "runs",
              "avg",
              "median"
            ]
          }
        ]
      }
    }
  },
  "required": [
    "tests"
  ]
}
```
#### Example output

```console
╭──────────────────────────┬─────────────────┬───────┬────────┬───────┬─────────╮
│ GasMeterFactory contract ┆                 ┆       ┆        ┆       ┆         │
╞══════════════════════════╪═════════════════╪═══════╪════════╪═══════╪═════════╡
│ Deployment Cost          ┆ Deployment Size ┆       ┆        ┆       ┆         │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ 35287                    ┆ 206             ┆       ┆        ┆       ┆         │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ Function Name            ┆ min             ┆ avg   ┆ median ┆ max   ┆ # calls │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ build                    ┆ 38653           ┆ 38653 ┆ 38653  ┆ 38653 ┆ 15      │
╰──────────────────────────┴─────────────────┴───────┴────────┴───────┴─────────╯
```

## eth_maxPriorityFeePerGas

### Definition

> https://github.com/ethereum/execution-apis/blob/main/src/eth/fee_market.yaml

The `eth_maxPriorityFeePerGas` was originally a client specific RPC Method (go-ethereum), it only recently was made part of the official Ethereum JSON-RPC specification. This method was introduced as part of the EIP-1559 (Ethereum Improvement Proposal 1559) transaction pricing mechanism implementation by the go-ethereum team. It is used to retrieve the current maximum priority fee per gas accepted for the network.

You can calculate a default ``maxPriorityFeePerGas`` using ``eth_feeHistory`` when ``eth_maxPriorityFeePerGas`` is not available.

### Calculating the current maximum priority fee per gas

The eth_maxPriorityFeePerGas method allows users, wallets, and dApps to query the Ethereum node and obtain the current maximum priority fee per gas.

The priority fee is an additional fee that can be added to a transaction to incentivize miners to prioritize its inclusion in a block. The returned value represents the maximum priority fee per gas in wei, and this value is a dynamic parameter and can change over time depending on network congestion and block builder preferences.

> It represents the maximum accepted priority fee at a given moment but does not guarantee that a transaction with that priority fee will be included in the next block. Inclusion depends on various factors such as gas price, gas limit, and transaction competition.

### Go-Ethereum Calculation 

Client implementations can vary, for example in go-ethereum (geth) it calculates what is the 60th percentile tip over the last 20 blocks by default.

> https://github.com/ethereum/go-ethereum/blob/f265cc24b4b17b55b468b315303a3a599fc01d81/eth/ethconfig/config.go#L40-L47
> 
```golang
// FullNodeGPO contains default gasprice oracle settings for full node.
var FullNodeGPO = gasprice.Config{
	Blocks:           20,
	Percentile:       60,
	MaxHeaderHistory: 1024,
	MaxBlockHistory:  1024,
	MaxPrice:         gasprice.DefaultMaxPrice,
	Igno
```

Usage:

To use this method, you need to send a JSON-RPC request to an Ethereum node with the method name eth_maxPriorityFeePerGas.

> The request does not require any parameters.

## eth_feeHistory

### Definition

> https://github.com/ethereum/execution-apis/blob/main/src/eth/fee_market.yaml

`eth_feeHistory` returns transaction base fee per gas and effective priority fee per gas for the requested/supported block range.

 > The request does require the following parameters:

`blockCount`: Requested range of blocks. Clients will return less than the requested range if not all blocks are available.    
`rewardPercentiles`: A monotonically increasing list of percentile values. For each block in the requested range, the transactions will be sorted in ascending order by effective tip per gas and the corresponding effective tip for the percentile will be determined, accounting for gas consumed.    
`gasUsedRatio`: An array of block gas used ratios. These are calculated as the ratio of `gasUsed` and `gasLimit`.

## Gas Pricing API Providers and Oracles

Listed in no particular order. 

> Notice: GasNow as of 2021-10-01 will be shutting down due to SparkPools closure


### Blocknative

> @note there are two seperate entries

#### gas.blocknative.com

> Note: This is powered by Blocknative's global mempool data platform

> v2 Blocknative

```jsonc
{
    "system": "ethereum",
    "network": "main",
    "unit": "gwei",
    "maxPrice": 50,
    "currentBlockNumber": 15326495,
    "msSinceLastBlock": 40251,
    "blockPrices": [
        {
            "blockNumber": 15326496,
            "estimatedTransactionCount": 322,
            "baseFeePerGas": 11.075381056,
            "estimatedPrices": [
                {
                    "confidence": 99,
                    "price": 13,
                    "maxPriorityFeePerGas": 2.49,
                    "maxFeePerGas": 22.45
                },
                {
                    "confidence": 95,
                    "price": 13,
                    "maxPriorityFeePerGas": 2.13,
                    "maxFeePerGas": 22.09
                },
                {
                    "confidence": 90,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.92,
                    "maxFeePerGas": 21.88
                },
                {
                    "confidence": 80,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.68,
                    "maxFeePerGas": 21.64
                },
                {
                    "confidence": 70,
                    "price": 12,
                    "maxPriorityFeePerGas": 1.58,
                    "maxFeePerGas": 21.54
                }
            ]
        }
    ],
    "estimatedBaseFees": [
        {
            "pending+1": [
                {
                    "confidence": 99,
                    "baseFee": 12.46
                }
            ]
        },
        {
            "pending+2": [
                {
                    "confidence": 99,
                    "baseFee": 14.02
                }
            ]
        },
        {
            "pending+3": [
                {
                    "confidence": 99,
                    "baseFee": 15.77
                }
            ]
        },
        {
            "pending+4": [
                {
                    "confidence": 99,
                    "baseFee": 17.75
                }
            ]
        },
        {
            "pending+5": [
                {
                    "confidence": 99,
                    "baseFee": 19.96
                }
            ]
        }
    ]
}
```

> v1 Blocknative 

```json
{
  "system": "ethereum",
  "network": "main",
  "unit": "gwei",
  "maxPrice": 336,
  "currentBlockNumber": 13095949,
  "msSinceLastBlock": 4542,
  "blockPrices": [
    {
      "blockNumber": 13095950,
      "baseFeePerGas": 113.110076547,
      "estimatedTransactionCount": 172,
      "estimatedPrices": [
        {
          "confidence": 99,
          "price": 129,
          "maxPriorityFeePerGas": 15.96,
          "maxFeePerGas": 242.18
        },
        {
          "confidence": 95,
          "price": 119,
          "maxPriorityFeePerGas": 6.84,
          "maxFeePerGas": 233.06
        },
        {
          "confidence": 90,
          "price": 118,
          "maxPriorityFeePerGas": 5.09,
          "maxFeePerGas": 231.31
        },
        {
          "confidence": 80,
          "price": 116,
          "maxPriorityFeePerGas": 3.21,
          "maxFeePerGas": 229.43
        },
        {
          "confidence": 70,
          "price": 115,
          "maxPriorityFeePerGas": 2.28,
          "maxFeePerGas": 228.5
        }
      ]
    }
  ]
}
```

#### bnc-ext

#### BlockNative Chrome Extenstion

[blocknative eth gas estimate extenstion](https://chrome.google.com/webstore/detail/blocknative-eth-gas-estim/ablbagjepecncofimgjmdpnhnfjiecfm/)

[https://blocknative-api.herokuapp.com/data](https://blocknative-api.herokuapp.com/data)

#### sample response

```json
{
  "pendingBlockNumberVal": 13378149,
  "seconds": 17,
  "maxPrice": 768,
  "estimatedTransactions": 279,
  "estimatedPrices": [{
    "confidence": 99,
    "price": 86,
    "maxPriorityFeePerGas": 2.96,
    "maxFeePerGas": 170.76
  }, {
    "confidence": 95,
    "price": 85,
    "maxPriorityFeePerGas": 1.75,
    "maxFeePerGas": 169.55
  }, {
    "confidence": 90,
    "price": 85,
    "maxPriorityFeePerGas": 1.56,
    "maxFeePerGas": 169.36
  }, {
    "confidence": 80,
    "price": 85,
    "maxPriorityFeePerGas": 1.48,
    "maxFeePerGas": 169.28
  }, {
    "confidence": 70,
    "price": 85,
    "maxPriorityFeePerGas": 1.37,
    "maxFeePerGas": 169.17
  }],
  "baseFeePerGas": 83.897778652
}
```
 
### Curve-Finance
 
#### `getGas`
 
[https://api.curve.fi/api/getGas](https://api.curve.fi/api/getGas)
 

```bash
 https://api.curve.fi/api/getGas
```
 
```json
{
    "success": true,
    "data": {
        "gas": {
            "rapid": 36000000000,
            "fast": 35000000000,
            "standard": 35000000000,
            "slow": 35000000000
        },
        "eip1559Gas": {
            "base": 35292604977,
            "prio": [
                1220000000,
                500000000,
                350000000,
                230000000
            ],
            "max": [
                56110000000,
                55390000000,
                55240000000,
                55120000000
            ]
        }
    },
    "generatedTimeMs": 1668181797396
}
``` 

### WalletConnect

#### specification

[https://github.com/pedrouid/ethereum-api#api](https://github.com/pedrouid/ethereum-api#api)

[https://ethereum-api.xyz/gas-prices](https://ethereum-api.xyz/gas-prices)

```
http GET https://ethereum-api.xyz/gas-prices
```

#### sample response

```json
{
  "timestamp": 1633172858972,
  "slow": {
    "time": 756,
    "price": 39
  },
  "average": {
    "time": 84,
    "price": 42
  },
  "fast": {
    "time": 30,
    "price": 54
  },
  "fastest": {
    "time": 24,
    "price": 58
  }
}
```

### Flashbots

> eth_gasFee

#### specification

[see source documentation](https://docs.flashbots.net/flashbots-protect/api/json-rpc#eth_gasfees)

// prettier-ignore

```jsonc
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    block,                     // Number, current block number
    baseFeePerGas,             // String, a hex number for the baseFee at the current block
    default: {
      maxFeePerGas,            // String, a hex number for the recommended default maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended default maxPriorityFeePerGas
    },
    low: {
      maxFeePerGas,            // String, a hex number for the recommended low maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended low maxPriorityFeePerGas
    },
    med: {
      maxFeePerGas,            // String, a hex number for the recommended med maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended med maxPriorityFeePerGas
    },
    high: {
      maxFeePerGas,            // String, a hex number for the recommended high maxFeePerGas
      maxPriorityFeePerGas,    // String, a hex number for the recommended high maxPriorityFeePerGas
    },
  }
}
```

#### request sample

```sh
curl -s -L -X POST 'https://protection.flashbots.net/v1/rpc' \
-H 'Content-Type: application/json' \
--data-raw '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_gasFees",
  "params": []
}'
```

#### response

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "block": 13467179,
        "baseFeePerGas": "0x0bd0606957",
        "default": {
            "maxFeePerGas": "0x12ec776ebc",
            "maxPriorityFeePerGas": "0x01e47257df"
        },
        "low": {
            "maxFeePerGas": "0x11d7682749",
            "maxPriorityFeePerGas": "0xe45ecec3"
        },
        "med": {
            "maxFeePerGas": "0x12ec776ebc",
            "maxPriorityFeePerGas": "0x01e47257df"
        },
        "high": {
            "maxFeePerGas": "0x1412552c31",
            "maxPriorityFeePerGas": "0x0302bff9d4"
        }
    }
}
```

### EtherScan

[https://docs.etherscan.io/api-endpoints/gas-tracker](https://docs.etherscan.io/api-endpoints/gas-tracker)

[https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken](https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken)

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "13053741",
    "SafeGasPrice": "20",
    "ProposeGasPrice": "22",
    "FastGasPrice": "24",
    "suggestBaseFee": "19.230609716",
    "gasUsedRatio": "0.370119078777807,0.8954731,0.550911766666667,0.212457033333333,0.552463633333333"
  }
}
```

### GasNow [no longer in service]

> gasnow.org/taichi

```bash
wss://www.gasnow.org/ws
```

```json
{
  "type": "gasprice",
  "data": {
    "gasPrices": {
      "rapid": 67000000000,
      "fast": 64455346560,
      "standard": 63455346560,
      "slow": 63455346560
    },
    "cumulativeCounts": [
      {
        "gwei": "63",
        "cumulativeCount": 93
      },
      {
        "gwei": "64",
        "cumulativeCount": 81
      },
      {
        "gwei": "65",
        "cumulativeCount": 65
      },
      {
        "gwei": "66",
        "cumulativeCount": 35
      },
      {
        "gwei": "67",
        "cumulativeCount": 34
      },
      {
        "gwei": "68",
        "cumulativeCount": 32
      },
      {
        "gwei": "69",
        "cumulativeCount": 30
      },
      {
        "gwei": "70",
        "cumulativeCount": 25
      },
      {
        "gwei": "71",
        "cumulativeCount": 22
      },
      {
        "gwei": "73",
        "cumulativeCount": 21
      },
      {
        "gwei": "74",
        "cumulativeCount": 19
      },
      {
        "gwei": "75",
        "cumulativeCount": 17
      },
      {
        "gwei": "78",
        "cumulativeCount": 16
      },
      {
        "gwei": "80",
        "cumulativeCount": 15
      },
      {
        "gwei": "81",
        "cumulativeCount": 13
      },
      {
        "gwei": "87",
        "cumulativeCount": 12
      },
      {
        "gwei": "88",
        "cumulativeCount": 11
      },
      {
        "gwei": "89",
        "cumulativeCount": 9
      },
      {
        "gwei": "94",
        "cumulativeCount": 8
      },
      {
        "gwei": "96",
        "cumulativeCount": 6
      },
      {
        "gwei": "98",
        "cumulativeCount": 5
      },
      {
        "gwei": "109",
        "cumulativeCount": 4
      },
      {
        "gwei": "112",
        "cumulativeCount": 3
      },
      {
        "gwei": "120",
        "cumulativeCount": 2
      },
      {
        "gwei": "221",
        "cumulativeCount": 1
      }
    ],
    "timestamp": 1629975608579
  }
}
```

<br>

#### GasNow Legacy

```json
{
  "code": 200,
  "data": {
    "rapid": 131000000000,
    "fast": 116000000000,
    "standard": 100000000000,
    "slow": 91600000000,
    "timestamp": 1613914581546
  }
}
```

### Gnosis

[endpoint url](https://safe-relay.gnosis.io/api/v1/gas-station/)

```json
{
  "lastUpdate": "2021-02-21T13:38:38.945308Z",
  "lowest": "2",
  "safeLow": "109000000001",
  "standard": "119000000001",
  "fast": "131000000001",
  "fastest": "10680081443136"
}
```

### MetaMask

#### Consensys CoDeFi

[endpoint url](https://api.metaswap.codefi.network/gasPrices)

```json
{
  "low": {
    "suggestedMaxPriorityFeePerGas": "1.37826449268",
    "suggestedMaxFeePerGas": "70.067746222",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 30000
  },
  "medium": {
    "suggestedMaxPriorityFeePerGas": "1.5",
    "suggestedMaxFeePerGas": "81.637728684",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 45000
  },
  "high": {
    "suggestedMaxPriorityFeePerGas": "2",
    "suggestedMaxFeePerGas": "93.585975639",
    "minWaitTimeEstimate": 15000,
    "maxWaitTimeEstimate": 60000
  },
  "estimatedBaseFee": "57.241234774",
   "networkCongestion": 0.5,
}
```

```json
{
  "SafeGasPrice": "100",
  "ProposeGasPrice": "108",
  "FastGasPrice": "119"
}
```

### 1inch

[https://gas-price-api.1inch.exchange/v1.0](https://gas-price-api.1inch.exchange/v1.0)

### v1.0

```json
{
  "fast": 96820000000,
  "instant": 125000000000,
  "standard": 90000000000,
  "slow": 82000000000
}
```

### v1.2

> gas-price-api.1inch.io/v.1.2

```json
{
    "baseFee": "93731028208",
    "low": {
        "maxPriorityFeePerGas": "1170000000",
        "maxFeePerGas": "94901028208"
    },
    "medium": {
        "maxPriorityFeePerGas": "2340000000",
        "maxFeePerGas": "96071028208"
    },
    "high": {
        "maxPriorityFeePerGas": "5850000000",
        "maxFeePerGas": "99581028208"
    },
    "instant": {
        "maxPriorityFeePerGas": "5850000000",
        "maxFeePerGas": "129455336670"
    }
}
```

### ethGasStation

[endpoint url](https://ethgasstation.info/json/ethgasAPI.json)

```json
{
  "fast": 1200.0,
  "fastest": 1200.0,
  "safeLow": 1020.0,
  "average": 1050.0,
  "block_time": 13.327868852459016,
  "blockNum": 11900622,
  "speed": 0.997822721438169,
  "safeLowWait": 12.9,
  "avgWait": 1.5,
  "fastWait": 0.5,
  "fastestWait": 0.5,
  "gasPriceRange": {
    "1200": 0.5,
    "1180": 0.5,
    "1160": 0.6,
    "1140": 0.6,
    "1120": 0.7,
    "1100": 0.7,
    "1080": 1.2,
    "1060": 1.5,
    "1040": 11.5,
    "1020": 12.9,
    "1000": 14.3,
    "980": 17.4,
    "960": 18.9,
    "940": 21.1,
    "920": 222.1,
    "900": 222.1,
    "880": 222.1,
    "860": 222.1,
    "840": 222.1,
    "820": 222.1,
    "800": 222.1,
    "780": 222.1,
    "760": 222.1,
    "740": 222.1,
    "720": 222.1,
    "700": 222.1,
    "680": 222.1,
    "660": 222.1,
    "640": 222.1,
    "620": 222.1,
    "600": 222.1,
    "580": 222.1,
    "560": 222.1,
    "540": 222.1,
    "520": 222.1,
    "500": 222.1,
    "480": 222.1,
    "460": 222.1,
    "440": 222.1,
    "420": 222.1,
    "400": 222.1,
    "380": 222.1,
    "360": 222.1,
    "340": 222.1,
    "320": 222.1,
    "300": 222.1,
    "280": 222.1,
    "260": 222.1,
    "240": 222.1,
    "220": 222.1,
    "200": 222.1,
    "190": 222.1,
    "180": 222.1,
    "170": 222.1,
    "160": 222.1,
    "150": 222.1,
    "140": 222.1,
    "130": 222.1,
    "120": 222.1,
    "110": 222.1,
    "100": 222.1,
    "90": 222.1,
    "80": 222.1,
    "70": 222.1,
    "60": 222.1,
    "50": 222.1,
    "40": 222.1,
    "30": 222.1,
    "20": 222.1,
    "10": 222.1,
    "8": 222.1,
    "6": 222.1,
    "4": 222.1,
    "1050": 1.5
  }
}
```

```json
{
  "fast": 1200.0,
  "fastest": 1200.0,
  "safeLow": 1020.0,
  "average": 1050.0,
  "block_time": 13.327868852459016,
  "blockNum": 11900622,
  "speed": 0.997822721438169,
  "safeLowWait": 12.9,
  "avgWait": 1.5,
  "fastWait": 0.5,
  "fastestWait": 0.5,
  "gasPriceRange": {
    "1200": 0.5,
    "1180": 0.5,
    "1160": 0.6,
    "1140": 0.6,
    "1120": 0.7,
    "1100": 0.7,
    "1080": 1.2,
    "1060": 1.5,
    "1040": 11.5,
    "1020": 12.9,
    "1000": 14.3,
    "980": 17.4,
    "960": 18.9,
    "940": 21.1,
    "920": 222.1,
    "900": 222.1,
    "880": 222.1,
    "860": 222.1,
    "840": 222.1,
    "820": 222.1,
    "800": 222.1,
    "780": 222.1,
    "760": 222.1,
    "740": 222.1,
    "720": 222.1,
    "700": 222.1,
    "680": 222.1,
    "660": 222.1,
    "640": 222.1,
    "620": 222.1,
    "600": 222.1,
    "580": 222.1,
    "560": 222.1,
    "540": 222.1,
    "520": 222.1,
    "500": 222.1,
    "480": 222.1,
    "460": 222.1,
    "440": 222.1,
    "420": 222.1,
    "400": 222.1,
    "380": 222.1,
    "360": 222.1,
    "340": 222.1,
    "320": 222.1,
    "300": 222.1,
    "280": 222.1,
    "260": 222.1,
    "240": 222.1,
    "220": 222.1,
    "200": 222.1,
    "190": 222.1,
    "180": 222.1,
    "170": 222.1,
    "160": 222.1,
    "150": 222.1,
    "140": 222.1,
    "130": 222.1,
    "120": 222.1,
    "110": 222.1,
    "100": 222.1,
    "90": 222.1,
    "80": 222.1,
    "70": 222.1,
    "60": 222.1,
    "50": 222.1,
    "40": 222.1,
    "30": 222.1,
    "20": 222.1,
    "10": 222.1,
    "8": 222.1,
    "6": 222.1,
    "4": 222.1,
    "1050": 1.5
  }
}
```

### etherchain.org

[endpoint url](https://www.etherchain.org/api/gasPriceOracle)

```json
{"safeLow":1,"standard":1,"fast":1.5,"fastest":2,"currentBaseFee":72.5,"recommendedBaseFee":147.2}
```

```json
{ "safeLow": 102, "standard": 105, "fast": 114.6, "fastest": 120 }
```

### etherchain-gasnow

[https://etherchain.org/api/gasnow](https://etherchain.org/api/gasnow)

```js
{code: 200, data: {rapid: 60000000000, fast: 39962373278, standard: 24406984375, slow: 19550000000,…}}
```

```javascript
code: 200
data: {rapid: 60000000000, fast: 39962373278, standard: 24406984375, slow: 19550000000,…}
fast: 39962373278
priceUSD: 1818.52
rapid: 60000000000
slow: 19550000000
standard: 24406984375
timestamp: 1654245505826
```

> Response

```json
{"code":200,"data":{"rapid":65265049007,"fast":49988581398,"standard":23000000000,"slow":19550000000,"timestamp":1654245243247,"priceUSD":1818.52}}
```

> Schema

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "$id": "etherchain_gasnow",
  "type": "object",
  "properties": {
    "code": {
      "type": "integer"
    },
    "data": {
      "type": "object",
      "properties": {
        "rapid": {
          "type": "integer"
        },
        "fast": {
          "type": "integer"
        },
        "standard": {
          "type": "integer"
        },
        "slow": {
          "type": "integer"
        },
        "timestamp": {
          "type": "integer"
        },
        "priceUSD": {
          "type": "number"
        }
      },
      "required": [
        "rapid",
        "fast",
        "standard",
        "slow",
        "timestamp",
        "priceUSD"
      ]
    }
  },
  "required": [
    "code",
    "data"
  ]
}
```

### poanetwork

[endpoint url](https://gasprice.poa.network/)

```json
{
  "health": true,
  "block_number": 11900628,
  "slow": 101.0,
  "standard": 107.0,
  "fast": 115.0,
  "instant": 130.8,
  "block_time": 13.191
}
```

```json
{
  "health": true,
  "block_number": 11900628,
  "slow": 101.0,
  "standard": 107.0,
  "fast": 115.0,
  "instant": 130.8,
  "block_time": 13.191
}
```

### Zoltu

> nanoeth is the **SI** nomenclature for `gwei`

```json
{
  "number_of_blocks": 200,
  "latest_block_number": 11907178,
  "percentile_1": "1e-9 nanoeth",
  "percentile_2": "0.00001 nanoeth",
  "percentile_3": "0.000011001 nanoeth",
  "percentile_4": "1 nanoeth",
  "percentile_5": "6 nanoeth",
  "percentile_10": "10 nanoeth",
  "percentile_15": "152 nanoeth",
  "percentile_20": "170 nanoeth",
  "percentile_25": "181.5 nanoeth",
  "percentile_30": "190.000001459 nanoeth",
  "percentile_35": "200 nanoeth",
  "percentile_40": "214.76 nanoeth",
  "percentile_45": "222.814063547 nanoeth",
  "percentile_50": "229.9 nanoeth",
  "percentile_55": "232 nanoeth",
  "percentile_60": "245 nanoeth",
  "percentile_65": "256 nanoeth",
  "percentile_70": "262 nanoeth",
  "percentile_75": "270.6 nanoeth",
  "percentile_80": "278 nanoeth",
  "percentile_85": "289.02 nanoeth",
  "percentile_90": "300 nanoeth",
  "percentile_95": "314.4 nanoeth",
  "percentile_96": "315.21 nanoeth",
  "percentile_97": "316.075841562 nanoeth",
  "percentile_98": "325 nanoeth",
  "percentile_99": "326 nanoeth",
  "percentile_100": "348 nanoeth"
}
```

### MyCrypto

```json
{
  "safeLow": 159,
  "standard": 184,
  "fast": 262,
  "fastest": 289,
  "blockNum": 11907235
}
```

```json
{
  "safeLow": 159,
  "standard": 184,
  "fast": 262,
  "fastest": 289,
  "blockNum": 11907235
}
```

### EtherScan

[api endpoint _key required_](https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=${YOUR_API_KEY})

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "11907242",
    "SafeGasPrice": "248",
    "ProposeGasPrice": "269",
    "FastGasPrice": "294"
  }
}
```

```json
{
  "status": "1",
  "message": "OK",
  "result": {
    "LastBlock": "11907242",
    "SafeGasPrice": "248",
    "ProposeGasPrice": "269",
    "FastGasPrice": "294"
  }
}
```

### Zapper

[http://api.zapper.fi/v1/gas-price](http://api.zapper.fi/v1/gas-price)

```json
{
  "standard": 113,
  "fast": 114,
  "instant": 136
}
```

### archerdao

[https://api.archerdao.io/v1/gas](https://api.archerdao.io/v1/gas)

```json
{
  "code": 200,
  "data": {
    "immediate": "228202648099",
    "rapid": "67236905683",
    "fast": "13591066085",
    "standard": "1101380018",
    "slow": "0",
    "slower": "0",
    "slowest": "0"
  }
}
```

### gas-ticker

[Gas Ticker by ricmoo](https://github.com/ricmoo/gas-ticker)

```jsonc
{
  "blockNumber": 14610954,
  "timestamp": 1650309194.438,
  "slow": {
    "min": 29.397486945,
    "max": 70.143180307,
    "sum": 13465.490242759988,
    "count": 385,
    "mean": 34.97529933184413,
    "median": 35,
    "tp90": 38,
    "stdDev": 5.992331436594249,
    "target90": 37.265690661,
    "targetStdDev": 2.7612260317587007,
    "targetCount": 266,
    "targetBest": 30,
    "targetWorst": 39.532494062
  },
  "medium": {
    "min": 29.397486945,
    "max": 62.428616398,
    "sum": 29594.27666106807,
    "count": 680,
    "mean": 43.520995089805986,
    "median": 39.038827568,
    "tp90": 52.433561707,
    "stdDev": 8.816041449214934,
    "target90": 50,
    "targetStdDev": 4.467921632212077,
    "targetCount": 470,
    "targetBest": 34.911631032,
    "targetWorst": 52.3082
  },
  "fast": {
    "min": 29.397486945,
    "max": 1200.988196226,
    "sum": 753432.9418861985,
    "count": 14637,
    "mean": 51.47454682559257,
    "median": 48.554602972,
    "tp90": 59.570121624,
    "stdDev": 24.12932660961557,
    "target90": 60.216413805,
    "targetStdDev": 6.10997036680254,
    "targetCount": 10100,
    "targetBest": 38.822145579,
    "targetWorst": 64.139501286
  }
}
```

## Appendix

### Custom Network Over pricing

Metamask will pad the estimated gas without exceeding the most recent block `gasLimit`. However, **If the
network is a a custom network it will return the `eth_estimateGas` value**

[see metamask/controllers](https://github.com/MetaMask/controllers/blob/77b1410a0611bbea785e5528b44143aebe5d407f/src/transaction/TransactionController.ts#L995)

### URL Index

Current offchain list:

- https://gas,blocknative.com/
- https://ethgasstation.info/json/ethgasAPI.json
- https://www.etherchain.org/api/gasPriceOracle
- https://gasprice.poa.network/
- https://www.gasnow.org/api/v3/gas/price

### EVM Params

| Key | Value | Description |
|---|---|---|
| JumpdestGas uint64 | 1 | Once per JUMPDEST operation. |
| EpochDuration uint64 | 30000 | Duration between proof-of-work epochs. |
| CreateDataGas uint64 | 200 |  |
| CallCreateDepth uint64 | 1024 | Maximum depth of call/create stack. |
| ExpGas uint64 | 10 | Once per EXP instruction |
| LogGas uint64 | 375 | Per LOG* operation. |
| CopyGas uint64 | 3 |  |
| StackLimit uint64 | 1024 | Maximum size of VM stack allowed. |
| TierStepGas uint64 | 0 | Once per operation, for a selection of them. |
| LogTopicGas uint64 | 375 | Multiplied by the * of the LOG*, per LOG transaction. e.g. LOG0 incurs 0 * c_txLogTopicGas, LOG4 incurs 4 * c_txLogTopicGas. |
| CreateGas uint64 | 32000 | Once per CREATE operation & contract-creation transaction. |
| Create2Gas uint64 | 32000 | Once per CREATE2 operation |
| SelfdestructRefundGas uint64 | 24000 | Refunded following a selfdestruct operation. |
| MemoryGas uint64 | 3 | Times the address of the (highest referenced byte in memory + 1). NOTE: referencing happens on read, write and in instructions such as RETURN and CALL. |
| TxDataNonZeroGasFrontier uint64 | 68 | Per byte of data attached to a transaction that is not equal to zero. NOTE: Not payable on data of calls between transactions. |
| TxDataNonZeroGasEIP2028 uint64 | 16 | Per byte of non zero data attached to a transaction after EIP 2028 (part in Istanbul) |
| TxAccessListAddressGas uint64 | 2400 | Per address specified in EIP 2930 access list |
| TxAccessListStorageKeyGas uint64 | 1900 | Per storage key specified in EIP 2930 access list |
| CallGasFrontier uint64 | 40 | Once per CALL operation & message call transaction. |
| CallGasEIP150 uint64 | 700 | Static portion of gas for CALL-derivates after EIP 150 (Tangerine) |
| BalanceGasFrontier uint64 | 20 | The cost of a BALANCE operation |
| BalanceGasEIP150 uint64 | 400 | The cost of a BALANCE operation after Tangerine |
| BalanceGasEIP1884 uint64 | 700 | The cost of a BALANCE operation after EIP 1884 (part of Istanbul) |
| ExtcodeSizeGasFrontier uint64 | 20 | Cost of EXTCODESIZE before EIP 150 (Tangerine) |
| ExtcodeSizeGasEIP150 uint64 | 700 | Cost of EXTCODESIZE after EIP 150 (Tangerine) |
| SloadGasFrontier uint64 | 50 |  |
| SloadGasEIP150 uint64 | 200 |  |
| SloadGasEIP1884 uint64 | 800 | Cost of SLOAD after EIP 1884 (part of Istanbul) |
| SloadGasEIP2200 uint64 | 800 | Cost of SLOAD after EIP 2200 (part of Istanbul) |
| ExtcodeHashGasConstantinople uint64 | 400 | Cost of EXTCODEHASH (introduced in Constantinople) |
| ExtcodeHashGasEIP1884 uint64 | 700 | Cost of EXTCODEHASH after EIP 1884 (part in Istanbul) |
| SelfdestructGasEIP150 uint64 | 5000 | Cost of SELFDESTRUCT post EIP 150 (Tangerine) |
| GasLimitBoundDivisor uint64 | 1024 | The bound divisor of the gas limit, used in update calculations. |
| MinGasLimit uint64 | 5000 | Minimum the gas limit may ever be. |
| MaxGasLimit uint64 | 0x7fffffffffffffff | Maximum the gas limit (2^63-1). |
| GenesisGasLimit uint64 | 4712388 | Gas limit of the Genesis block. |
| MaximumExtraDataSize uint64 | 32 | Maximum size extra data may be after Genesis. |
| ExpByteGas uint64 | 10 | Times ceil(log256(exponent)) for the EXP instruction. |
| SloadGas uint64 | 50 | Multiplied by the number of 32-byte words that are copied (round up) for any *COPY operation and added. |
| CallValueTransferGas uint64 | 9000 | Paid for CALL when the value transfer is non-zero. |
| CallNewAccountGas uint64 | 25000 | Paid for CALL when the destination address didn't exist prior. |
| TxGas uint64 | 21000 | Per transaction not creating a contract. NOTE: Not payable on data of calls between transactions. |
| TxGasContractCreation uint64 | 53000 | Per transaction that creates a contract. NOTE: Not payable on data of calls between transactions. |
| TxDataZeroGas uint64 | 4 | Per byte of data attached to a transaction that equals zero. NOTE: Not payable on data of calls between transactions. |
| QuadCoeffDiv uint64 | 512 | Divisor for the quadratic particle of the memory cost equation. |
| LogDataGas uint64 | 8 | Per byte in a LOG* operation's data. |
| CallStipend uint64 | 2300 | Free gas given at beginning of call. |
| Keccak256Gas uint64 | 30 | Once per KECCAK256 operation. |
| Keccak256WordGas uint64 | 6 | Once per word of the KECCAK256 operation's data. |
| SstoreSetGas uint64 | 20000 | Once per SSTORE operation. |
| SstoreResetGas uint64 | 5000 | Once per SSTORE operation if the zeroness changes from zero. |
| SstoreClearGas uint64 | 5000 | Once per SSTORE operation if the zeroness doesn't change. |
| SstoreRefundGas uint64 | 15000 | Once per SSTORE operation if the zeroness changes to zero. |
| NetSstoreNoopGas uint64 | 200 | Once per SSTORE operation if the value doesn't change. |
| NetSstoreInitGas uint64 | 20000 | Once per SSTORE operation from clean zero. |
| NetSstoreCleanGas uint64 | 5000 | Once per SSTORE operation from clean non-zero. |
| NetSstoreDirtyGas uint64 | 200 | Once per SSTORE operation from dirty. |
| NetSstoreClearRefund uint64 | 15000 | Once per SSTORE operation for clearing an originally existing storage slot |
| NetSstoreResetRefund uint64 | 4800 | Once per SSTORE operation for resetting to the original non-zero value |
| NetSstoreResetClearRefund uint64 | 19800 | Once per SSTORE operation for resetting to the original zero value |
| SstoreSentryGasEIP2200 uint64 | 2300 | Minimum gas required to be present for an SSTORE call, not consumed |
| SstoreSetGasEIP2200 uint64 | 20000 | Once per SSTORE operation from clean zero to non-zero |
| SstoreResetGasEIP2200 uint64 | 5000 | Once per SSTORE operation from clean non-zero to something else |
| SstoreClearsScheduleRefundEIP2200 uint64 | 15000 | Once per SSTORE operation for clearing an originally existing storage slot |
| ColdAccountAccessCostEIP2929 | uint64(2600) | COLD_ACCOUNT_ACCESS_COST |
| ColdSloadCostEIP2929 | uint64(2100) | COLD_SLOAD_COST |
| WarmStorageReadCostEIP2929 | uint64(100) | WARM_STORAGE_READ_COST |
