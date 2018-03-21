import os.path
from whoosh import index
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED

class MySchema(SchemaClass):
    path = ID(stored=True)
    title = TEXT(stored=True)
    content = TEXT
    tags = KEYWORD

if not os.path.exists('index'):
    os.mkdir('index')
ix = index.create_in("index", MySchema)
ix = index.open_dir("index")

writer = ix.writer()
writer.add_document(title=u"my document", content=u"this is my document", path=u"/a", tags=u"firlst short")
writer.add_document(title=u"my second document", content=u"this is my second document", path=u"/b",tags=u"second short")
writer.commit()

from whoosh.qparser import QueryParser
try:
    searcher = ix.searcher()
    query = QueryParser("content", ix.schema).parse("second")
    result = searcher.search(query)
    print result[0]
finally:
    searcher.close()