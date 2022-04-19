<span align="center">

# Gas Price Reporting Index

> Collection of All Gas Price Prediction and Reporting Services and their various formats
 
 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5702504.svg)](https://doi.org/10.5281/zenodo.5702504)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/sambacha/gas-reporting)

 </span>
 

 <details>
 <summary> Frontmatter </summary>
 
<table>
<thead>
  <tr>
    <th>title<br></th>
    <th>Gas Price Reporting API Index</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>summary</td>
    <td>Index of all the different gas pricing API's available</td>
  </tr>
  <tr>
    <td>version</td>
    <td><a href="mailto:&#x76;&#49;&#x2e;&#x31;&#x2e;&#x35;&#x40;&#x32;&#x30;&#50;&#49;&#x2e;&#49;&#48;&#x2e;&#50;&#50;">v1.1.5@2021.10.22</a></td>
  </tr>
  <tr>
    <td>license</td>
    <td>CC-NC-2.5 / MIT for code</td>
  </tr>
</tbody>
</table>
 
 </details>
 
> Notice: GasNow as of 2021-10-01 will be shutting down due to SparkPools closure

 
## [Gas Reporting Index - TOC](https://github.com/sambacha/gas-reporting/edit/master/README.md)

- [Cite This Work](#cite-this-work)
- [Fee Speed Definitions](#fee-speed-definitions)
- [Gas Price Reporting Index](#gas-price-reporting-index)
  * [Cite This Work](#cite-this-work)
  * [Fee Speed Definitions](#fee-speed-definitions)
    + [api.txprice.com](#apitxpricecom)
    + [Blocknative](#blocknative)
      - [gas.blocknative.com](#gasblocknativecom)
      - [bnc-ext](#bnc-ext)
      - [BlockNative Chrome Extenstion](#blocknative-chrome-extenstion)
      - [sample response](#sample-response)
    + [WalletConnect](#walletconnect)
      - [specification](#specification)
      - [sample response](#sample-response-1)
    + [Flashbots](#flashbots)
      - [specification](#specification-1)
      - [request sample](#request-sample)
      - [response](#response)
    + [EtherScan](#etherscan)
    + [GasNow [no longer in service]](#gasnow--no-longer-in-service-)
      - [GasNow Legacy](#gasnow-legacy)
    + [Gnosis](#gnosis)
    + [MetaMask](#metamask)
      - [Consensys CoDeFi](#consensys-codefi)
    + [1inch](#1inch)
    + [ethGasStation](#ethgasstation)
    + [etherchain.org](#etherchainorg)
    + [poanetwork](#poanetwork)
    + [Zoltu](#zoltu)
    + [MyCrypto](#mycrypto)
    + [EtherScan](#etherscan-1)
    + [Zapper](#zapper)
    + [archerdao](#archerdao)
    + [gas ticker](#gas-ticker)
- [URL Index](#url-index)


## Cite This Work

> [see CITATION.cff](https://github.com/sambacha/gas-reporting/blob/master/CITATION.cff)

```latex
Bacha, S. (2021). Gas Reporting Index (Version 1.1.5) [Computer software]. https://doi.org/10.5281/zenodo.1234
```

```bibtex
@software{Bacha_Gas_Reporting_Index_2021,
author = {Bacha, Sam},
ipfs = {$CID},
license = {CC-2.5-NC/MIT},
month = {10},
title = {{Gas Reporting Index}},
url = {https://github.com/sambacha/gas-reporting},
version = {1.1.5},
year = {2021}
}
```


## Fee Speed Definitions

- Fastest: next block (i.e. <30 seconds) <br>
- Fast: below 2 minutes (<10 blocks) <br>
- Medium: around 5 minutes (<20 blocks) <br>
- Slow: below 30 minutes (a.k.a safe-low, <120 blocks) <br>

### api.txprice.com

> Note: This is a proxy for Blocknative's Gas Pricing Service

```jsonc
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

### Blocknative

> @note there are two seperate entries 

#### gas.blocknative.com

> Note: This is powered by Blocknative's global mempool data platform
 
```jsonc
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

```http
GET https://gas-price-api.1inch.exchange/v1.0 HTTP/1.1
Host:gas-price-api.1inch.exchange
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0
Accept:application/json, text/plain, */*
Accept-Language:en-US,en;q=0.5
Accept-Encoding:gzip, deflate, br
Referer:https://1inch.exchange/
Origin:https://1inch.exchange
Connection:keep-alive
If-None-Match:W/"55-14kgjK/la5g2ZUcb/96cMvcDlDQ"
Content-Type:text/plain
```

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
{ "safeLow": 102, "standard": 105, "fast": 114.6, "fastest": 120 }
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

## Appendix - MetaMask

### Custom Network Over pricing 

Metamask will pad the estimated gas without exceeding the most recent block `gasLimit`. However, **If the network is a a custom network it will return the `eth_estimateGas` value** 

[see metamask/controllers](https://github.com/MetaMask/controllers/blob/77b1410a0611bbea785e5528b44143aebe5d407f/src/transaction/TransactionController.ts#L995)

## URL Index

Current offchain list:

- https://gas,blocknative.com/
- https://ethgasstation.info/json/ethgasAPI.json
- https://www.etherchain.org/api/gasPriceOracle
- https://gasprice.poa.network/
- https://www.gasnow.org/api/v3/gas/price
