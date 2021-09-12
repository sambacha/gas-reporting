#!/bin/bash
# 2021/09/11

curl 'https://gas-price-api.1inch.io/v1.2/1' \
-H 'sec-ch-ua-platform: "macOS"' \
-H 'Origin: https://app.1inch.io' \
-H 'Connection: keep-alive' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'Sec-Fetch-Dest: empty' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36' \
-H 'If-None-Match: W/"f8-QfE+tgTPt472M8yiWX6RUUUZdJc"' \
-H 'DNT: 1' \
-H 'Host: gas-price-api.1inch.io' \
-H 'Referer: https://app.1inch.io/' \
-H 'Sec-Fetch-Site: same-site' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Accept-Language: en-US,en;q=0.9' \
-H 'sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"' \
--proxy http://localhost:9090 > 1inch-gas.json
