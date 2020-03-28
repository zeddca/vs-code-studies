#华为机试：
#给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，
#一共N辆火车，每辆火车以数字1-9编号。
# 要求以字典序排序输出火车出站的序列号。


def handle(waits, ins, outs, result: list):
    if not waits and not ins:
        result.append(outs)
    if ins:
        temp_outs = outs + ins[-1] + ' '
        handle(waits, ins[:-1], temp_outs, result)
    if waits:
        temp_ins = ins.copy()
        temp_ins.append(waits[0])
        handle(waits[1:], temp_ins, outs, result)
n = int(input())
waits = input().strip().split(' ')
result = []
ins = []
outs = ''
handle(waits, ins, outs, result)
result = sorted(result)
for s in result:
    print(s)