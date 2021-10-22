#!/bin/sh
curl --location --request POST 'https://protection.flashbots.net/v1/rpc' \
--header 'Content-Type: application/json' \
--data-raw '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_gasFees",
  "params": []
}'
