def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


#调用calc_sum()并没有计算出结果，而是返回函数
#f = calc_sum([1, 2, 3, 4])
#f
#对函数进行调用时，才计算出结果
#f()
#10
#由于可以返回函数，我们可以在后续代码里就可以决定要不要调用该函数
