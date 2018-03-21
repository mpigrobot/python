#! /usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals
import os.path
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer

analyzer=ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer),
                path=ID(stored=True), tags=KEYWORD, icon=STORED)

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index",schema)

writer = ix.writer()
writer.add_document(title=u"第一篇文档", content=u"这里是中国", path=u"/a", tags=u"first short", icon=u"/icons/star.png")
writer.add_document(title=u"第二篇文档", content=u"这里不是美国", path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("content",ix.schema).parse("美国")
    result = searcher.search(query)
    print result[0].highlights("content")