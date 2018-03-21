import os.path
# from whoosh.index import create_in,open_dir
from whoosh import index
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT

schema = Schema(title=TEXT(stored=True), content=TEXT,path=ID(stored=True),tags=KEYWORD, icon=STORED)

if not os.path.exists("index"):
    os.mkdir("index")
ix = index.create_in("index",schema)
ix = index.open_dir("index")

writer = ix.writer()
writer.add_document(title=u"my document", content=u"this is my document", path=u"/a", tags=u"first short", icon=u"/icons/star.png")
writer.add_document(title=u"my second document", content=u"this is my second document", path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
writer.commit()

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content",ix.schema).parse("second")
    result = searcher.search(query)
    print (result[0])