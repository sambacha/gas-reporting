#!/bin/bash
curl 'https://api-us.taichi.network:10001/rpc/private' \
-X POST \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Content-Length: 78' \
-d '{"id":3241702970864080,"jsonrpc":"2.0","method":"eth_blockNumber","params":[]}'
