#import numpy
name = []
fen1 = []
fen2 = []
sname = ''
sname = input('球队名称:')
while not sname == 'game over':
    if len(name) >1 and name[0] == name [1]:
       name.pop(0)
    else :
        sname =input('球队的名称:')
        name.append(sname)
        if name[0] == sname:
            sfen= int(input('得分:'))
            fen1.append(sfen)
            a1 =sum(fen1)
        elif name[1] == sname:
            sfen =int(input('得分:'))
            fen2.append(sfen)
            a2 =sum(fen2)
else:
    print('比赛结束')
    if a1 > a2:
        print('Winer is '+name[0])
    elif a1 < a2:
        print('Winer is '+name[1])
    else:
        print('Draw')
