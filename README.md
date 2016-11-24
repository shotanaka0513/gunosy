##制作物
記事URLを入れると記事カテゴリを返す、ナイーブベイズを使った教師あり文書分類器ウェブアプリの実装

####開発環境
```
Python 3.5
Django 1.10
```

####ライブラリ
```
beautifulsoup4==4.5.1
Django==1.10
numpy==1.11.2
pandas==0.19.1
python-dateutil==2.6.0
pytz==2016.7
requests==2.12.0
six==1.10.0
```


####
```
GunosyのWebサイト(https://gunosy.com/)のエンタメ,スポーツ,おもしろ,国内,海外,コラム,IT・科学,グルメカテゴリー
内のそれぞれの１から１００ページのタイトル。（カテゴリー内のページ数が１００までの表示なのでそのような仕様になっています。）


■訓練データとしてタイトルを選択した理由
１、タイトルはその記事の象徴しているから。
２、処理時間が短くなるから。

最大訓練データ数は８(カテゴリー)×２０（カテゴリー１ページあたりの記事数）×100（ページ）=16000

また汎用性を持たせるためgettrain.pyモジュールの41行目と42行目のCATEGORY_PAGE_START_INDEX = 1、
CATEGORY_PAGE_END_INDEX = 100を変更すると取得するカテゴリーページを変更することが出来ます。

```

####実行方法

１、課題のgunosyフォルダをクローン  
```
$git clone https://github.com/shotanaka0513/gunosy.git  
```
２、クローンしたgunosyフォルダへ移動  
```
$cd gunosy    
```
３、lsコマンドでgunosyフォルダ内を確認  
```
$ls 
  
README.md		crawler			gunosy
__pycache__		db.sqlite3		manage.py
classifier		guesscategory		requirements.txt
```

４、実装に必要なライブラリをインストール(virtualenv等で仮想環境で実装することを推奨します。)
```
pip install -r requirements.txt
```

５、guesscategory/view.pyに以下のコメントを外す。（訓練データの収集の実行のため。）
```変更前
    10	# 訓練する際は以下の４行のコードを挿入してください。
    11	# nb = classifier.naivebayes.NaiveBayes()
    12	# crawler.gettrain.gunosy_train(nb)
    13	# print("訓練データの収集が完了しました。ctrl+cを押して、python manage.py runserverでappを実行して下さい。")
    14	# sys.exit()
```

```変更後
    10 訓練する際は以下の４行のコードを挿入してください。
    11 nb = classifier.naivebayes.NaiveBayes()
    12 crawler.gettrain.gunosy_train(nb)
    13 print("訓練データの収集が完了しました。ctrl+cを押して、python manage.py runserverでappを実行して下さい。")
    14 sys.exit()
```




６、訓練データを収集
```
$python manage.py runserver
```

７、５でコメントを外した部分を再びコメントとしてつける。

```変更前
    10	# 訓練する際は以下の４行のコードを挿入してください。
    11	# nb = classifier.naivebayes.NaiveBayes()
    12	# crawler.gettrain.gunosy_train(nb)
    13	# print("訓練データの収集が完了しました。ctrl+cを押して、python manage.py runserverでappを実行して下さい。")
    14	# sys.exit()
```


８、Djangoアプリの実行
```
$python manage.py runserver
```

９、８を終了後、ブラウザに以下のurlにアクセス  
http://127.0.0.1:8000/guesscategory/

１０、フォームに記事urlを入力  

１１、訓練データを元に入力された記事urlのカテゴリが返ってくる。


####その他の仕様
Gunosyのサイトをクローリングスクレイピングする際にアクセス制限がかかった場合はtime.sleepで時間間隔を
指定してアクセスをして下さい。
訓練データ数の変更はcrawler/gettrain.pyの３７行目から４７行目を参照。
