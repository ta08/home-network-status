#/bin/sh

/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | tr -d ' ' | jq -R 'split(":") | {"key": .[0], "value": (.[1]|if test("^[+-]?(?:\\d+\\.?\\d*|\\.\\d+)+$") then tonumber else . end)}' | jq -r -s 'from_entries' | jq  --arg timestamp "$(date '+%Y-%m-%dT%H:%M:%S%z')" '. =.+{"createdAt": $timestamp}' | jq -c 'del(.channel)'| http POST localhost:9200/network_status/wifi

