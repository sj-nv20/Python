#리스트[실습과제3]

# 제가 구매하고 싶은 물건들의 가격을 리스트에 정리해 놨습니다.
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# 가격의 단위는 모두 원화(￦)인데요.
# 이 물건들의 가격을 미국 달러($)로 하면 얼마일지,
# 그리고 일본 엔화(￥)로 하면 얼마일지 확인해 보려고 합니다.
'''
해야 할 일
우리가 해야 할 일은 크게 두 가지입니다.

함수 작성
반복문을 통해 리스트 요소들 변환
1. 함수 작성
먼저 한국 원화를 미국 달러로 변환해 주는 krw_to_usd 함수, 그리고 미국 달러를 일본 엔화로 변환해 주는 usd_to_jpy 함수를 써야 하는데요. krw_to_usd 함수는 파라미터로 원화 krw을 받아서 변환된 미국 달러 액수를 리턴해 줍니다. 마찬가지로 usd_to_jpy 함수는 파라미터로 달러 usd를 받아서 변환된 일본 엔화 액수를 리턴해 주는 거죠.

참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정합니다.

2. 반복문을 통해 리스트 요소들 변환
반복문을 사용해서 리스트의 요소들을 각각 다른 화폐로 변환해야 하는데요. 그 과정에서 krw_to_usd 함수와 usd_to_jpy 함수를 활용하면 되겠죠?

위 코드를 완성하고 실행하면 아래와 같이 출력됩니다.

한국 화폐: [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
미국 화폐: [34.0, 13.0, 5.0, 21.0, 1.0, 2.0, 8.0, 3.0]
일본 화폐: [4250.0, 1625.0, 625.0, 2625.0, 125.0, 250.0, 1000.0, 375.0]
'''


# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000  # 1000원당 1달러


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd / 8 * 1000


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# amounts를 원화(￦)에서 달러($)로 변환하기
i = 0
while i <= len(prices) - 1:
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
i = 0
while i <= len(prices) - 1:
    prices[i] = usd_to_jpy(prices[i])
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))