# 命名規則： PEP8
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../classifier/')
import naivebayes
import gethtmltext
import gettrain

# ナイーブベイズ分類器のオブジェクトを作成。
nb = naivebayes.NaiveBayes()
# Gunosyのサイトをスクレイピングし、その記事データを用いて訓練させます。
# gettrain.gunosy_train(nb)


def hello_guess_category(request):
    # view関数が呼ばれたびにスクレイピングして学習しないようにオブジェクトは外部で作成します。
    global nb
    # フォームからurlを取得
    url = request.GET.get('url')
    # urlのhtmlファイルのテキストを取得
    html_text = gethtmltext.url_to_text(url)
    # エラーが出た場合の処理
    if html_text is None:
        category = "urlを入力して下さい。"
    # エラが無かった場合の処理
    else:
        category = "推定カテゴリー ：" + nb.classifier(html_text)
    d = {
        'category': category
    }
    return render(request, 'index.html', d)
