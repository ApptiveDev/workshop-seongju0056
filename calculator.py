def add(a, b):
    return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def pow(a, b):
    return a ** b



def abs(a):
    if a < 0:
	return -a
    else:
	return a


def mod(a, b):
    return a % b


if __name__ == "__main__":
    # 간단한 테스트 코드
    # 간단한 테스트 코드
    print("add:", add(10, 5))
    print("subtract:", subtract(10, 5))
    print("multiply:", multiply(10, 5))
    print("divide:", divide(10, 5))
    print("pow:", pow(2, 3))
    print("abs:", abs(-10))
    print("mod:", mod(10, 3))

    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(10, 5) == 50
    assert divide(10, 5) == 2
    assert pow(2, 3) == 8
    assert abs(-10) == 10
    assert mod(10, 3) == 1

    print("모든 테스트를 통과했습니다!")
