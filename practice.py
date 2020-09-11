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