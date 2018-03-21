# encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import jieba

def cuttest(test_sent):
    result = jieba.cut(test_sent)
    print("  ".join(result))

def testcase():
    cuttest("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱Python和C++。")
    cuttest("我不喜欢日本和服。")
    cuttest("永和服装饰品有限公司")
    cuttest("我爱北京天安门")
    cuttest("abc")

if __name__ == "__main__":
    testcase()
    jieba.set_dictionary("foobar.txt")
    print("================================")
    testcase()