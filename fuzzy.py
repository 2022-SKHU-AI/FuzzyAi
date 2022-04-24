import numpy
from matplotlib import pyplot as plt

import az
from Age import Age
from Feeling import Feeling
from Rank import Rank

VERY_HIGH = lambda : 4
HIGH = lambda : 3
MIDDLE = lambda : 2
LOW = lambda : 1
VERY_LOW = lambda : 0

rankTable = ['인턴', '사원', '주임', '대리', '계장', '과장', '차장', '부장', \
             '이사', '상무이사', '전무이사', '부사장', '사장', '부회장', '회장', '명예회장']

if __name__ == "__main__":
    try:
        #speaker = int(input("하는 사람의 나이 입력: "))
        speaker = 30
        #listener = int(input("듣는 사람의 나이 입력: "))
        listener = 60
        #rank = input("직급 입력(과장, 부장 등..): ")
        rank = "부장"
        rankValue = rankTable.index(rank)
        #look = list(input("표정 입력(분노 경멸 혐오 행복의 형태로 입력.\n입력 예시 : 0.05 0.03 0.02 0.55): ").split())
        look = "0.05 0.03 0.02 0.55".split()
        lookValue = -(float(look[0])+float(look[1])+float(look[2]))+float(look[3])
    except Exception as e:
        print(e)
        print("잘못 입력 하셨습니다.")
    
    ageMembership = Age()
    rankMembership = Rank()
    feelingMembership = Feeling()
    az_ = az.Az()
    
    speakerIsYoung, speakerIsOld = ageMembership.value(speaker)
    listenerIsYoung, listenerIsOld = ageMembership.value(listener)
    rankIsLow, rankIsHigh = rankMembership.value(rankValue)
    feelingIsPassive, feelingIsNormal, feelingIsPositive = feelingMembership.value(lookValue)
    
    #step 1~2 (Fuzzification, Fuzzy Logic Operation)
    rule = [] #2차원 리스트 [전건부 값, 후건부 값]
    rule.append([min(max(speakerIsOld, rankIsHigh), feelingIsPassive), VERY_HIGH()])
    rule.append([min(max(speakerIsOld, rankIsHigh), feelingIsNormal), HIGH()])
    rule.append([min(max(speakerIsOld, rankIsHigh), feelingIsPositive), MIDDLE()])
    rule.append([min(speakerIsOld, listenerIsYoung, feelingIsPassive), VERY_HIGH()])
    rule.append([min(speakerIsOld, listenerIsYoung, feelingIsNormal), MIDDLE()])
    rule.append([min(speakerIsOld, listenerIsYoung, feelingIsPositive), LOW()])
    rule.append([min(speakerIsYoung, listenerIsOld, feelingIsPassive), MIDDLE()])
    rule.append([min(speakerIsYoung, listenerIsOld, feelingIsNormal), HIGH()])
    rule.append([min(speakerIsYoung, listenerIsOld, feelingIsPositive), VERY_HIGH()])
    rule.append([min(speakerIsYoung, rankIsLow, feelingIsPassive), MIDDLE()])
    rule.append([min(speakerIsYoung, rankIsLow, feelingIsNormal), LOW()])
    rule.append([min(speakerIsYoung, rankIsLow, feelingIsPositive), VERY_LOW()])


    #step 3 (Implication)
    fuzzySet = [0, 0, 0, 0, 0]
    for i in rule:
        if i[0] > fuzzySet[i[1]]:
            fuzzySet[i[1]] = i[0]

    print(fuzzySet)
    #step 4
    #plt.ylim([0.0, 1.0])  # 그래프 y 범위를 0~1로 정함
    sum = 0 # 그래프의 넓이(분자)
    denominator = 0 # 분모


    # 그래프 x값을 0~100까지 순회함
    for x in numpy.arange(0.0, 100.01, 0.1):
        temp = az_.value(x) # x값에 따른 후건부 그래프 값을 확인
        y = 0
        index = temp.index(max(temp)) # x값에 따른 현재 후건부 상태를 확인(verylow인지 low인지 등)

        # 후건부 그래프 중 겹치는 부분 확인
        # 겹치는 부분에서 더 큰 값을 index로 지정



        # step 5
        
        # 구분구적법 응용
        # x가 이미 꽤 작으므로 y * x를 전부 더해주면 넓이가 됨
        # 더 정교하려면 x를 더 촘촘하게 해주면 됨
        # 근데 그럼 시간이 오래걸림
        sum += y * x

        denominator += y # 분모에 가로 길이를 더하는거 아님??
        #print(round(x, 2), round(y, 2))
        plt.scatter(x , y, c ='black' , s = 1)
    plt.show() # 그래프 표시

    print("당신의 아재력은", round(sum/denominator, 2), "%")