#输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）
#按照统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASII码由小到大排序输出
#清空目前的统计结果，重新统计
while True:
    try:
        list1=[]
        arr = input()
        dic = {}
        for i in arr:
            if not (i.isalpha() or i.isdigit() or i.isspace()):
                continue
            else:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i]=1
        dic=sorted(dic.items(),key = lambda x:x[0])#先按字符ASC排
        dic=sorted(dic,key = lambda x:x[1],reverse=True)#再按统计数目排
        print(''.join(k for (k , v) in dic))
    except:
        break