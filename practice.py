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