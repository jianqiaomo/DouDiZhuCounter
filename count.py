# *_*coding:utf-8 *_*
import sys
import copy

LeftValue = [0, 0, 0]
mult = 0
buffer = [0, 0]
screenin = []
BaseValue = 2
Welcome = '''
######################################
             三人斗地主          
               计分器            

游戏结束:               输入stop
撤回刚才的输入:         输入recall
设置底分(默认=2):       输入setup

记分:    输入炸弹数/抢地主数 赢家编号
######################################
'''

if __name__ == '__main__':
    while (1):
        if buffer == [0, 0]:
            print(Welcome)
        print(" ")
        str = input("input: (eg. MultipleTimes (space) Winner(s)) ")
        if str == 'stop':
            sys.exit(0)
        elif str == 'setup':
            if buffer != [0, 0]:
                print("Error: You can only set up at the beginning!")
                print(buffer[len(buffer) - 1])
                continue
            while(1):
                str1 = input("What would you like to set up? BaseValue? yes/no ")
                if str1 == 'yes':
                    str2 = input("BaseValue: ")
                    BaseValue = int(str2)
                    break
                elif str1 == 'no':
                    break
                else:
                    print("Error: input yes or no")
                    continue
        elif str == 'recall':
            buffer.pop()
            buffer.insert(0, 0)
            LeftValue = buffer[len(buffer) - 1]
            print("recall the last result")
            print("player #1 #2 #3")
            print(buffer[len(buffer) - 1])
        else:
            screenin = str.split()
            screenin = [int(x) for x in screenin]

            if len(screenin) == 3:
                mult = BaseValue * (2 ** (screenin[0]))
                if (screenin[1] < 1 or screenin[1] > 3 or screenin[2] < 1 or screenin[2] > 3):
                    print("player ID error")
                    print(buffer[len(buffer) - 1])
                    continue
                if (screenin[1] > screenin[2]):
                    temp = copy.copy(screenin[2])
                    screenin[2] = screenin[1]
                    screenin[1] = temp
                LeftValue[screenin[1] - 1] = LeftValue[screenin[1] - 1] + mult / 2
                LeftValue[screenin[2] - 1] = LeftValue[screenin[2] - 1] + mult / 2
                if screenin[1] == 2:
                    if screenin[2] == 3:
                        LeftValue[0] = LeftValue[0] - mult
                elif screenin[1] == 1:
                    if screenin[2] == 2:
                        LeftValue[2] = LeftValue[2] - mult
                    elif screenin[2] == 3:
                        LeftValue[1] = LeftValue[1] - mult
            elif len(screenin) == 2:
                mult = BaseValue * (2 ** (screenin[0]))
                LeftValue[screenin[1] - 1] = LeftValue[screenin[1] - 1] + mult
                if screenin[1] == 1:
                    LeftValue[1] = LeftValue[1] - mult / 2
                    LeftValue[2] = LeftValue[2] - mult / 2
                elif screenin[1] == 2:
                    LeftValue[0] = LeftValue[0] - mult / 2
                    LeftValue[2] = LeftValue[2] - mult / 2
                elif screenin[1] == 3:
                    LeftValue[0] = LeftValue[0] - mult / 2
                    LeftValue[1] = LeftValue[1] - mult / 2
            else:
                print("Error: input too much args")
                print(buffer[len(buffer) - 1])
                continue

            buffer.append(copy.copy(LeftValue))
            buffer.pop(0)

            print("player #1 #2 #3")
            print(LeftValue)
