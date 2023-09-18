import numpy as np

# 내가 예상한 가상의 기울기 a와 b를 설정
fake_a = 3
fake_b = 76

# 실제 독립변수와 종속변수를 넘파이 배열로 저장
x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# 내가 설정한 기울기와 y절편에 따른 일차식의 값을 함수로 나타냄
def predict(x):
    return fake_a * x + fake_b

# 예측 y값을 받을 수 있는 빈 리스트 생성
predict_result = []

# 예측 y값을 추가 시키고 x, y, 예측 y값을 출력
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("x값: %d, 실제 y값: %.2f, 예측 y값: %.2f" %(x[i], y[i], predict_result[i]))

#평균 제곱 오차(MSE)를 구하는 함수
n = len(x)
def mse(y, y_pred):
    return (1/n) * sum((y-y_pred)**2)

#출력
print("MSE값: %.2f" %mse(y, predict_result))

