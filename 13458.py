import math
class_n = int( input())
people_n = list(map(int, input().split()))
total_m, manger = map(int, input().split())
manger_n = 0
manger_n += class_n
for i in people_n:
    manger_n += math.ceil((i - total_m)/manger)

print(manger_n)
#리스트1 : 시험장 인원 받는거
#리스트2 : 총감독관이 보는 인원 뺀 반의 인원 리스트
#