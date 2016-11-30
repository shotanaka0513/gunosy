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

５、訓練urlの収集
```
python manage.py geturl
```

６、訓練urlからモデルを作成
```
python manage.py gettrain
```

７、Djangoアプリの実行
```
$python manage.py runserver
```

９、８を終了後、ブラウザに以下のurlにアクセス  
http://127.0.0.1:8000/guesscategory/

１０、フォームに記事urlを入力  

１１、訓練データを元に入力された記事urlのカテゴリが返ってくる。


####その他の仕様
訓練データ数の変更はcrawler/geturl.pyの２４行目から３１行目を参照。
