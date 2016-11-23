# 命名規則： PEP8
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
import sys
import os
# パスを通す。
sys.path.append(os.path.dirname(os.path.abspath('gunosy')) + '/classifier')
sys.path.append(os.path.dirname(os.path.abspath('gunosy')) + '/crawler')
import naivebayes
import gethtmltext
import gettrain


def hello_guess_category(request):
    # オブジェクトを作成。
    nb = naivebayes.NaiveBayes()
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
