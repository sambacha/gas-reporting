---
title: JSON RPC Methods for L1/L2 Gas Est.
description: Assorted RPC Methods for Gas Estimiation for L1 and L2's
---

> [!WARNING]
> Under Construction 

## `eth_feeHistory`

### Parameters

-   `blockCount`: (integer) Number of blocks in the requested range. Between 1 and 1024 blocks can be requested in a single query. If blocks in the specified block range are not available, then only the fee history for available blocks is returned.
-   `newestBlock`: (string) Integer representing the highest number block of the requested range, or one of the string tags `latest`, `earliest`, or `pending`.
-   `array` of `integers`: (optional) A monotonically increasing list of percentile values to sample from each block's effective priority fees per gas in ascending order, weighted by gas used.

## Returns

-   `oldestBlock`: Lowest number block of the returned range expressed as a hexadecimal number.
-   `baseFeePerGas`: An array of block base fees per gas, including an extra block value. The extra value is the next block after the newest block in the returned range. Returns zeroes for blocks created before [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559).
-   `gasUsedRatio`: An array of block gas used ratios. These are calculated as the ratio of `gasUsed` and `gasLimit`.
-   `reward`: An array of effective priority fee per gas data points from a single block. All zeroes are returned if the block is empty.



#### Ethereum

```jsonc
{
    "jsonrpc": "2.0",
    "result": {
        "baseFeePerGas": [
            "0x3da8e7618",
            "0x3e1ba3b1b",
            "0x3dfd72b90",
            "0x3d64eee76",
            "0x3d4da2da0",
            "0x3ccbcac6b"
        ],
        "gasUsedRatio": [
            0.5290747666666666,
            0.49240453333333334,
            0.4615576,
            0.49407083333333335,
            0.4669053
        ],
        "oldestBlock": "0xfab8ac",
        "reward": [
            [
                "0x59682f00",
                "0x59682f00"
            ],
            [
                "0x59682f00",
                "0x59682f00"
            ],
            [
                "0x3b9aca00",
                "0x59682f00"
            ],
            [
                "0x510b0870",
                "0x59682f00"
            ],
            [
                "0x3b9aca00",
                "0x59682f00"
            ]
        ]
    },
    "id": 0
}
```

### Optimism

```jsonc
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": [
      "0x648d7b",
      "0x643d9d",
      "0x64434e",
      "0x644f34",
      "0x643033",
      "0x645f0d",
      "0x642570",
      "0x641205",
      "0x655826",
      "0x659001",
      "0x65b3b0"
    ],
    "gasUsedRatio": [
      0.037383566666666666,
      0.1759079,
      0.18598443333333334,
      0.11635633333333334,
      0.24277953333333332,
      0.0732412,
      0.13510776666666666,
      0.697108,
      0.25637576666666667,
      0.2238549
    ],
    "oldestBlock": "0x70f7b5e"
  }
}
```
