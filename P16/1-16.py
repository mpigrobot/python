#! /usr/bin/env python
#coding:utf-8

def del_space(string):
    split_string = string.split(" ")
    string_list = [i for i in split_string if i!=""]
    result_string = " ".join(string_list)
    return result_string

if __name__=="__main__":
    one_str = "Hello,  I am  Qiwsir."
    string = del_space(one_str)
    print one_str
    print string