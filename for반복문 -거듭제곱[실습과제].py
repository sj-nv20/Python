#거듭제곱

#"2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.
#코드를 실행하면 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.

for i in range(11):
    print("2^{} = {}".format(i,2**i))

#모범답안
for i in range(11):
    print("{}^{} = {}".format(2, i, 2 ** i))
