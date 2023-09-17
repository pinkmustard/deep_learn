# 최소 제곱법 파이썬

import numpy as np

# 독립변수 x와 그에 해당하는 종속변수 y를 넘파이 배열로 저장
x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# x와 y의 평균을 구함
mx = np.mean(x)
my = np.mean(y)

# 최소 제곱법의 분모 부분에 해당하는 부분 (x-x평균)^2의 합
divisor = sum([(i-mx)**2 for i in x])

# 최소 제곱법의 분자 부분에 해당하는 부분 (x-x평균)*(y-y평균)의 합
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

# 분자 부분을 구함
dividend = top(x, mx, y, my)

# 기울기 a와 y절편 b를 구함
# b = y의 평균 - (x의 평균*기울기)
a = dividend / divisor
b = my - (mx * a)

# x, y 평균과 기울기, y절편 출력
print("x평균: %.2f y평균: %.2f" %(mx, my))
print("기울기 a: %.2f, y절편 b: %.2f" %(a, b))