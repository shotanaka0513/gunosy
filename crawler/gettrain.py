# 命名規則： PEP8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from pandas import DataFrame
from classifier import naivebayes
from django.conf import settings
import pandas as pd
import os


def get_train():

    nb = naivebayes.NaiveBayes()

    categories = [
        'エンタメ',
        'スポーツ',
        'おもしろ',
        '国内',
        '海外',
        'コラム',
        'IT・科学',
        'グルメ',
    ]

    for category in categories:
        category_dframe = pd.read_csv(os.path.join(
            settings.DATA_DIR,
            'articles/{}/{}.csv'.format(category, category)),
            index_col=0)

        for i in category_dframe.index:
            url = category_dframe['0'][i]
            # try文でカプセル化します。
            # 各カテゴリーのhtmlを取得
            # ページがサーバー上で見つかるかどうかをチェック。
            try:
                html = urlopen(url)
            except HTTPError as e:
                # エラーの内容を端末に出力
                print(e)
                continue
                # 各カテゴリーのhtmlオブジェクトを作成
                # サーバーがあるかどうかをチェック。
            try:
                html_object = BeautifulSoup(html.read())
            except URLError as e:
                # エラーの内容を端末に出力
                print(e)
                continue

            title = html_object.find(
                "h1", {"class": "article_header_title"}).get_text()
            # デバック
            nb.train(title, category)
            print("title = {},\n category = {},".format(title, category))
    nb.catprob_to_csv()
    nb.wordprob_to_csv()
