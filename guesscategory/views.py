# 命名規則： PEP8
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
import classifier.naivebayes
import crawler.gethtmltext
import crawler.gettrain


# nb = classifier.naivebayes.NaiveBayes()
# crawler.gettrain.gunosy_train(nb)
# print("訓練データの収集が完了しました。ctrl+cを押して、python manage.py runserverでappを実行して下さい。")
# sys.exit()


def hello_guess_category(request):
    # オブジェクトを作成。
    nb = classifier.naivebayes.NaiveBayes()
    # フォームからurlを取得
    url = request.GET.get('url')
    # urlのhtmlファイルのテキストを取得
    html_text = crawler.gethtmltext.url_to_text(url)
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
