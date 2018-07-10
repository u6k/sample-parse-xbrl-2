# XBRL解析サンプル 2 _(sample-parse-xbrl-2)_

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> XBRL解析のサンプル・スクリプト

## Install

ビルドする。

```
$ docker-compose build
```

## Usage

解析するXBRLを入手して、`sample.xbrl`ファイルとして同フォルダに配置する。

実行する。

```
$ docker-compose run app
```

例えば、証券コード`1301`の文書`ED2017062700544`に含まれる`jpcrp030000-asr-001_E00012-000_2017-03-31_01_2017-06-27.xbrl`を`sample.xbrl`として配置して実行すると、次のようになる。

```
$ sudo docker-compose run app
{'edinet_code': 'E00012', 'trading_symbol': '13010', 'company_name': '株式会社極洋', 'accounting_standards': 'Japan GAAP', 'current_fy_start': '2016-04-01', 'current_fy_end': '2017-03-31'}
{'netsales': 236561000000.0, 'ordinary_income_loss': 3709000000.0, 'profit_loss': 2422000000.0, 'comprehensive_income': 2857000000.0, 'net_assets': 25391000000.0, 'total_assets': 97391000000.0, 'bps': 2378.09, 'dps': 60.0, 'basic_eps': 230.66, 'diluted_eps': 213.01, 'equity_to_asset_ratio': 0.256, 'roe': 0.102, 'per': 12.7, 'cf_from_operating': 601000000.0, 'cf_from_investing': -1998000000.0, 'cf_from_financing': 105000000.0, 'shares_outstanding': 10928000.0, 'assets': 97391000000.0, 'current_assets': 72351000000.0, 'non_current_assets': 25040000000.0, 'liabilities': 72000000000.0, 'current_liabilities': 45195000000.0, 'non_current_liabilities': 26804000000.0}
```

## Link

参考リンク

- [UFOキャッチャーからXBRLをダウンロード&パースするクラスを作った - Qiita](https://qiita.com/sawadybomb/items/67059635545cf0a11c8e)

## Maintainer

- u6k
  - [GitHub](https://github.com/u6k/)
  - [Twitter](https://twitter.com/u6k_yu1)
  - [u6k.Blog](https://blog.u6k.me/)

## Contribute

ライセンスの範囲内で、ご自由にご使用ください。

## License

[MIT License](https://github.com/u6k/sample-parse-xbrl-2/blob/master/LICENSE)

