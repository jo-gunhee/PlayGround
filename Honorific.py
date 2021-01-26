'''
심심해서 만드는 프로그램
문서 작업을 하거나 보고서를 작성 할 때 높임말과 반말을 섞어 사용해 불편함을 
감수하고 직접 하나하나 수정하는 과정에서 불편함을 느껴 심심풀이 땅콩삼아 만들었다.
'''
print("한국어 높임말 변환 프로그램입니다.")
a = input("변환할 문장이나 문단을 입력해주세요: ")
print()
k = input("1: 높임말 -> 반말 \n2:반말 -> 높임말\n입력: ")
if(k == "1"):
    a = a.replace("입니다", "이다")
    a = a.replace("합니다", "한다")
    a = a.replace("했습니다", "했다")
    a = a.replace("갔습니다", "갔다")
    a = a.replace("왔습니다", "왔다")
    a = a.replace("저는", "나는")
    a = a.replace("먹었습니다", "먹다")
    a = a.replace("봤습니다", "봤다")
elif(k == "2"):
    a = a.replace("이다", "입니다")
    a = a.replace("한다", "합니다")
    a = a.replace("했다", "했습니다")
    a = a.replace("갔다", "갔습니다")
    a = a.replace("왔다", "왔습니다")
    a = a.replace("나는", "저는")
    a = a.replace("먹다", "먹었습니다")
    a = a.replace("봤다", "봤습니다")
else:
    print("잘못된 입력입니다.\n프로그램을 종료합니다.")
    exit(0)
print()
o = input("1: 입력한 값에서 추가로 변환하고자 하는 문장이나 단어가 있다.\n2: 높임말,반말만 변환하여 출력하고 싶다.\n입력: ")
if(o == "1"):
    while(o == "1"):
        print("바꿀 단어 혹은 문장을 그만 입력하고 싶을 때는 !@ 을 입력해주세요.")
        rr = input("기존의 단어: ")
        if(rr == "!@"):
            break
        tt = input("바꿀 문장: ")
        if(tt == "!@"):
            break
        a = a.replace(rr, tt)
    print("수정된 글: ", a)
elif(o == "2"):
    print("수정된 문장: ", a)
