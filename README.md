# Gas Price Reporting Index

> Collection of All Gas Price Prediction and Reporting Services and their various formats


### Fee Speed Definitions

Fastest: next block (i.e. <30 seconds) <br>
Fast: below 2 minutes (<10 blocks)  <br>
Medium: around 5 minutes (<20 blocks)  <br>
Slow: below 30 minutes (a.k.a safe-low, <120 blocks)  <br>
 <br>



## Catalog

- [Gas Price Reporting Index](#gas-price-reporting-index)
    + [Fee Speed Definitions](#fee-speed-definitions)
  * [Catalog](#catalog)
    + [gaswatch](#gaswatch)
    + [gnosis](#gnosis)
    + [MetaMask  / Consensys CoDeFi](#metamask----consensys-codefi)
    + [1Inch Exchange](#1inch)
    + [ethGasStation](#ethgasstation)
    + [etherchain.org](#etherchainorg)
    + [poanetwork](#poanetwork)
    + [Zoltu](#zoltu)
    + [MyCrypto](#mycrypto)
    + [EtherScan](#etherscan)
  * [URL Index](#url-index)


### api.txprice.com

```jsonc
{
    "system": "ethereum",
    "network": "main",
    "unit": "gwei",
    "maxPrice": 336,
    "currentBlockNumber": 13095949,
    "msSinceLastBlock": 4542,
    "blockPrices": [{
        "blockNumber": 13095950,
        "baseFeePerGas": 113.110076547,
        "estimatedTransactionCount": 172,
        "estimatedPrices": [{
            "confidence": 99,
            "price": 129,
            "maxPriorityFeePerGas": 15.96,
            "maxFeePerGas": 242.18
        }, {
            "confidence": 95,
            "price": 119,
            "maxPriorityFeePerGas": 6.84,
            "maxFeePerGas": 233.06
        }, {
            "confidence": 90,
            "price": 118,
            "maxPriorityFeePerGas": 5.09,
            "maxFeePerGas": 231.31
        }, {
            "confidence": 80,
            "price": 116,
            "maxPriorityFeePerGas": 3.21,
            "maxFeePerGas": 229.43
        }, {
            "confidence": 70,
            "price": 115,
            "maxPriorityFeePerGas": 2.28,
            "maxFeePerGas": 228.5
        }]
    }]
}
```

### gaswatch (gasnow.org/taichi)
```json
{"code":200,"data":{"rapid":131000000000,"fast":116000000000,"standard":100000000000,"slow":91600000000,"timestamp":1613914581546}}
```

### gnosis

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

### MetaMask  / Consensys CoDeFi

[endpoint url](https://api.metaswap.codefi.network/gasPrices)

```json 
{"SafeGasPrice":"100","ProposeGasPrice":"108","FastGasPrice":"119"}
```

```json
{
    "SafeGasPrice": "100",
    "ProposeGasPrice": "108",
    "FastGasPrice": "119"
}
```

#### 1inch 

[https://gas-price-api.1inch.exchange/v1.0](https://gas-price-api.1inch.exchange/v1.0)

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


### ethGasStation 

[endpoint url](https://ethgasstation.info/json/ethgasAPI.json)

```json
{"fast": 1200.0, "fastest": 1200.0, "safeLow": 1020.0, "average": 1050.0, "block_time": 13.327868852459016, "blockNum": 11900622, "speed": 0.997822721438169, "safeLowWait": 12.9, "avgWait": 1.5, "fastWait": 0.5, "fastestWait": 0.5, "gasPriceRange": {"1200": 0.5, "1180": 0.5, "1160": 0.6, "1140": 0.6, "1120": 0.7, "1100": 0.7, "1080": 1.2, "1060": 1.5, "1040": 11.5, "1020": 12.9, "1000": 14.3, "980": 17.4, "960": 18.9, "940": 21.1, "920": 222.1, "900": 222.1, "880": 222.1, "860": 222.1, "840": 222.1, "820": 222.1, "800": 222.1, "780": 222.1, "760": 222.1, "740": 222.1, "720": 222.1, "700": 222.1, "680": 222.1, "660": 222.1, "640": 222.1, "620": 222.1, "600": 222.1, "580": 222.1, "560": 222.1, "540": 222.1, "520": 222.1, "500": 222.1, "480": 222.1, "460": 222.1, "440": 222.1, "420": 222.1, "400": 222.1, "380": 222.1, "360": 222.1, "340": 222.1, "320": 222.1, "300": 222.1, "280": 222.1, "260": 222.1, "240": 222.1, "220": 222.1, "200": 222.1, "190": 222.1, "180": 222.1, "170": 222.1, "160": 222.1, "150": 222.1, "140": 222.1, "130": 222.1, "120": 222.1, "110": 222.1, "100": 222.1, "90": 222.1, "80": 222.1, "70": 222.1, "60": 222.1, "50": 222.1, "40": 222.1, "30": 222.1, "20": 222.1, "10": 222.1, "8": 222.1, "6": 222.1, "4": 222.1, "1050": 1.5}}
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
{"safeLow":102,"standard":105,"fast":114.6,"fastest":120}
```


### poanetwork

[endpoint url](https://gasprice.poa.network/)

```json
{"health":true,"block_number":11900628,"slow":101.0,"standard":107.0,"fast":115.0,"instant":130.8,"block_time":13.191}
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
{"safeLow":159,"standard":184,"fast":262,"fastest":289,"blockNum":11907235}
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

[api endpoint *key required*](https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=${YOUR_API_KEY})

```json
{"status":"1","message":"OK","result":{"LastBlock":"11907242","SafeGasPrice":"248","ProposeGasPrice":"269","FastGasPrice":"294"}}
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


## URL Index

Current offchain list:

- https://ethgasstation.info/json/ethgasAPI.json
- https://www.etherchain.org/api/gasPriceOracle
- https://gasprice.poa.network/
- https://www.gasnow.org/api/v3/gas/price
