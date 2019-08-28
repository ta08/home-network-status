# home-network-status
<a id="markdown-home-network-status" name="home-network-status"></a>

This scripts were created for visualizing home network statuses with `Elasticsearch`. So main purpose of these is to send json data into Elasticsearch.

At the visualization phase, I used `grafana` and make a dashboard like <https://ta08.github.io/posts/20190823t23/> (written in Japanese) . No codes are here about the visualization phase. 


<!-- TOC -->

- [Prerequirement](#prerequirement)
- [Usage](#usage)
    - [postwifistatusasjson.sh](#postwifistatusasjsonsh)
    - [postpingasjson.py](#postpingasjsonpy)
- [Elasticsearch memo](#elasticsearch-memo)

<!-- /TOC -->


## Prerequirement
<a id="markdown-prerequirement" name="prerequirement"></a>

Both of scripts use Elasticsearch. Please run Elasticsearch on your local machine with 9200 port.

## Usage
<a id="markdown-usage" name="usage"></a>

### post_wifi_status_as_json.sh
<a id="markdown-postwifistatusasjsonsh" name="postwifistatusasjsonsh"></a>

Just only work on MacOS. Prepare `network_status` as index at your Elasticsearch. This scirpt requires `jq`, `httpie` commands.

ElasticsearchにWifiの情報をJSONに整形して突っ込む。

```
watch -n 5 ./post_wifi_status_as_json.sh
```

### post_ping_as_json.py
<a id="markdown-postpingasjsonpy" name="postpingasjsonpy"></a>

Work with Python 3.7.4. Lower versions are not confirmed to work but I think it will work. Please install libraries with requirements.txt.

Elasticsearchにpingの結果をJSONに整形して突っ込む。

```sh
ping -i 5 8.8.8.8 | python -u post_ping_as_json.py ping_google
```

## Elasticsearch memo
<a id="markdown-elasticsearch-memo" name="elasticsearch-memo"></a>

```sh
http get http://localhost:9200/_cat/indices
```

```sh
http post http://localhost:9200/<index>
```

```sh
http post http://localhost:9200/<index>/<type>
```
