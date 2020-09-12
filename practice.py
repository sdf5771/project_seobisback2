# 문자열 연습
print("ㅡㅡㅡㅡ 문자열 연습 ㅡㅡㅡㅡ")
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
# 참 / 거짓 boolean
print("ㅡㅡㅡㅡ참 / 거짓 booleanㅡㅡㅡㅡ")
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print(not (5 < 10))
# 변수 연습
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 "+ animal + "의 이름은 "+ name +"에요")
hobby = "공놀이"
#print(name + "는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print(name, "는 ", age,"살이며, ", hobby,"을 아주 좋아해요")
# 콤마(,) 는 공백이 하나 포함되며 str로 감싸줄 필요가 없다.
# 플러스(+) 는 공백이 포함되지 않으며 str로 감싸주어야 오류가 나지 않고 정확하게 출력된다.
print(name + "는 어른일까요? " + str(is_adult))

#주석

'''여러 문장을
한 번에 주석처리하려면
따옴표 3개를 겹쳐서 사용하고 닫아주면 된다 '''

#주석을 설정하고자 할 때, 여러 문장을 선택하고 ctrl + /를 하면 주석이 설정되고
#반대로 설정된 주석을 해제하고자 할 때는 ctrl + / 를 하면 주석이 해제된다


#퀴즈 변수를 이용하여 다음 문장을 출력하시오.
'''
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : xx 행 열차가 들어오고 있습니다.
'''
station = "신도림"

print(station + "행 열차가 들어오고 있습니다.")


#연산자
print("ㅡㅡㅡㅡ 연산자 ㅡㅡㅡㅡ")
print(1 + 1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) #1
print(5//3) #1
print(10//3) #3

print(10 > 3) # 10보다 3이 더 크다True
print(4 >= 7) # 4는 7보다 크거나 같다False
print(10 < 3) # 10은 3보다 작다False
print(5 <= 5) # 5는 5보다 크거나 같다True

print(3 == 3) # 같다 True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) #같지 않다 True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7 ) # False

#수식
print("ㅡㅡㅡㅡ 수식 ㅡㅡㅡㅡ")
print(2 + 3 * 4) #14
print((2 + 3) *4) #20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # number 변수에 2를 더하라
print(number) #18
number *= 2 #36
print(number)
number /= 2 #18
print(number)

#숫자처리함수
print("ㅡㅡㅡㅡ숫자처리함수ㅡㅡㅡㅡ")
print(abs(-5)) #5 절대값
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) #12 최대
print(min(5, 12)) #5 최소
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) # 내림 . 4
print(ceil(3.14)) # 올림 . 4
print(sqrt(16)) # 제곱근 . 4

#랜덤함수
print("ㅡㅡㅡㅡ랜덤함수ㅡㅡㅡㅡ")
from random import *

print(random()) #랜덤함수 0.0 이상 ~ 1.0 미만의 임의의 값 생성
print(random()* 10) # 0.0 이상 ~ 10.0 미만의 임의의 값 생성
print(random() * 100)# 0.0 이상 ~ 100.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 이상 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 이상 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 이상 ~ 10 미만의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성
print(int(random()*10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 부터~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# 퀴즈 ) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하세요.

#조건 1 : 랜덤으로 날짜를 뽑아야함
#조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#(출력문 예제)
#오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

date = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
#print 문 안에서 date 변수를 사용하려면 string 으로 변환해주어야함 str(date)

#문자열
print("ㅡㅡㅡㅡ문자열ㅡㅡㅡㅡ")
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱 (필요한 만큼만 잘라서 사용) 컴퓨터에서는 0번째부터 시작
print("ㅡㅡㅡㅡ슬라이싱ㅡㅡㅡㅡ")
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 가져오려는 자리 수 보다 + 1 즉 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 2 : 4직전까지
print("일 : " + jumin[4:6]) # 4 : 6 직전까지
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("생년월일 : " + jumin[0:6]) # 0 : 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 번째부터 끝까지
print("뒤 7자리 : " + jumin[7:14]) # 7 : 14 직전까지
print("뒤 7자리 : (뒤에서부터)" + jumin[-7:]) # 맨 뒷자리는 -1의 자리가 된다 즉 7부터 끝까지