# -*- coding: utf-8 -*-
import math
import sys
import os
from pandas import DataFrame
import pandas as pd
from django.conf import settings
# yahoo!形態素解析
import classifier.morphological

flag = 0


def getwords(doc):
    words = [s.lower() for s in classifier.morphological.split(doc)]
    return tuple(w for w in words)


class NaiveBayes:

    def __init__(self):
        self.vocabularies = set()  # 単語の集合
        self.wordcount = {}       # {category : { words : n, ...}}
        self.catcount = {}        # {category : n}

    def wordcountup(self, word, cat):
        self.wordcount.setdefault(cat, {})
        self.wordcount[cat].setdefault(word, 0)
        self.wordcount[cat][word] += 1
        self.vocabularies.add(word)

    def catcountup(self, cat):
        self.catcount.setdefault(cat, 0)
        self.catcount[cat] += 1

    def train(self, doc, cat):
        word = getwords(doc)
        for w in word:
            self.wordcountup(w, cat)
        self.catcountup(cat)

    def classifier(self, doc):
        global flag
        best = None  # 最適なカテゴリ
        max = -sys.maxsize
        word = getwords(doc)

        # 最初にアクセスしたときのみmodelsへ移動する。
        if flag == 0:
            os.chdir("classifier/data/models")
            flag = 1

        self.catprob_dframe = pd.read_csv("catprob.csv", index_col=0)
        self.wordprob_dframe = pd.read_csv("wordprob.csv", index_col=0)
        # カテゴリ毎に確率の対数を求める
        for cat in self.catprob_dframe.columns:
            prob = self.score(word, cat)
            if prob > max:
                max = prob
                best = cat
        return best

    # ここを修正
    def score(self, word, cat):

        score = math.log(self.catprob_dframe[cat][0])
        for w in word:
            # カプセル化
            try:
                score += math.log(self.wordprob_dframe[cat][w])
            # logの真数が0のなるときはscoreに0を加算します。
            except ValueError:
                score += 0
                continue
            # データフレームの要素を取り出すときに、値があるかどうかをエラー処理で確認を致します。
            except KeyError:
                continue
        return score

    def priorprob(self, cat):
        return float(self.catcount[cat]) / sum(self.catcount.values())

    def incategory(self, word, cat):
        # あるカテゴリの中に単語が登場した回数を返す
        if word in self.wordcount[cat]:
            return float(self.wordcount[cat][word])
        return 0.0

    def wordprob(self, word, cat):
        # P(word|cat)が生起する確率を求める
        prob = \
            (self.incategory(word, cat) + 1.0) / \
            (sum(self.wordcount[cat].values()) +
             len(self.vocabularies) * 1.0)
        return prob

    def catprob_to_csv(self):
        self.catdata = {}
        for cat in self.catcount.keys():
            self.catdata.update({cat: [self.priorprob(cat)]})
        catprob_dframe = DataFrame(self.catdata)
        catprob_dframe.to_csv(os.path.join(
            settings.DATA_DIR, 'models/catprob.csv'))

    def wordprob_to_csv(self):
        self.worddata = {}
        for cat in self.catcount.keys():
            self.worddata.setdefault(cat, {})
            for word in self.vocabularies:
                self.worddata[cat].setdefault(word, self.wordprob(word, cat))
        wordprob_dframe = DataFrame(self.worddata)
        wordprob_dframe.to_csv(os.path.join(
            settings.DATA_DIR, 'models/wordprop.csv'))
