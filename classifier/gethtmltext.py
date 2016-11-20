# 命名規則： PEP8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def url_to_text(url):
    # try文とif文でカプセル化します。
    # 空のurlが入力されたときの処理
    if url is '' or url is None:
        return None
    try:
        html = urlopen(url)
    # ページがサーバー上で見つからないとき(または取り出すとき)のエラー
    except HTTPError as e:
        # エラーの内容を端末に出力
        print(e)
        return None
    # サーバーが見つからないときのエラー
    except URLError as e:
        # エラーの内容を端末に出力
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
    # Noneオブジェクトにアクセスしようとするときのエラー
    except AttributeError as e:
        # エラーの内容を端末に出力
        print(e)
        return None

    text = bsObj.find("h1").get_text()
    return text
