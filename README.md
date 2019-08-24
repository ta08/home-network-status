# home-network-status

dupulicated は elasticsearch導入前にローカルで頑張っていたときのスクリプト。

## check_ip.sh (duplicated)

前回保存したifconfigのと今回のifconfigの結果が異なっていれば新しくファイルを保存する。

## trafic_post.sh

ElasticsearchにWifiの情報をJSONに整形して突っ込む。

## convert2json.py

Elasticsearchにpingの結果をJSONに整形して突っ込む。
