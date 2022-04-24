import numpy
from matplotlib import pyplot as plt

from az import Az
from Age import Age
from Feeling import Feeling
from Rank import Rank

VERY_HIGH = lambda: 4
HIGH = lambda: 3
MIDDLE = lambda: 2
LOW = lambda: 1
VERY_LOW = lambda: 0

rankTable = ['인턴', '사원', '주임', '대리', '계장', '과장', '차장', '부장', \
             '이사', '상무이사', '전무이사', '부사장', '사장', '부회장', '회장', '명예회장']

if __name__ == "__main__":

    try:
        speaker = int(input("하는 사람의 나이 입력: "))
        listener = int(input("듣는 사람의 나이 입력: "))
        rank = input("직급 입력(과장, 부장 등..): ")
        rankValue = rankTable.index(rank)
        look = list(input("표정 입력(분노 경멸 혐오 행복의 형태로 입력.\n입력 예시 : 0.05 0.03 0.02 0.55): ").split())
        lookValue = -(float(look[0]) + float(look[1]) + float(look[2])) + float(look[3])
    except:
        print("잘못 입력 하셨습니다.")

    # 각 소속함수별 객체 생성
    ageMembership = Age()
    rankMembership = Rank()
    feelingMembership = Feeling()
    az = Az()

    # 입력받은 값을 소속함수에 대입
    speakerIsYoung, speakerIsOld = ageMembership.value(speaker)
    listenerIsYoung, listenerIsOld = ageMembership.value(listener)
    rankIsLow, rankIsHigh = rankMembership.value(rankValue)
    feelingIsPassive, feelingIsNormal, feelingIsPositive = feelingMembership.value(lookValue)

    # step 1~2 (Fuzzification, Fuzzy Logic Operation)
    rule = []  # 2차원 리스트 [전건부 값, 후건부 값]
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

    # step 3 (Implication)
    fuzzySet = [0, 0, 0, 0, 0]
    # 최대값 탐색
    for i in rule:
        if i[0] > fuzzySet[i[1]]:
            fuzzySet[i[1]] = i[0]

    # step 4
    plt.ylim([0.0, 1.0])  # 그래프 y 범위를 0~1로 정함
    sum = 0  # 그래프의 넓이(분자)
    denominator = 0  # 분모

    # 그래프 x값을 0~100까지 순회함
    for x in numpy.arange(0.0, 100.01, 0.1):
        temp = az.value(x)  # x값에 따른 후건부 소속함수 값 확인
        y = []

        # temp값과 퍼지출력값을 비교하여 퍼지가 크면 temp를, 아니면 반대로 값 추가
        y.append(temp[0] if fuzzySet[0] > temp[0] else fuzzySet[0])
        y.append(temp[1] if fuzzySet[1] > temp[1] else fuzzySet[1])
        y.append(temp[2] if fuzzySet[2] > temp[2] else fuzzySet[2])
        y.append(temp[3] if fuzzySet[3] > temp[3] else fuzzySet[3])
        y.append(temp[4] if fuzzySet[4] > temp[4] else fuzzySet[4])

        # 그래프 그리는 부분
        # 하단부분 상하에 있는 '''을 지우시면 그래프가 출력됩니다.
        '''
        plt.scatter(x, max(y), c='red', s=5)

        for i in temp:
            if i != 0:
                plt.scatter(x, i, c='black', s=1)
        
        plt.show() # 그래프 표시
        '''

        # step 5

        # 구분구적법 응용
        sum += max(y) * x # 적분 수행

        denominator += max(y)  # 소속값의 총 합



    print("당신의 아재력은", round(sum / denominator, 2), "%")
