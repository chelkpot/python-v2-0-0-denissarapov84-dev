# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    count_100 = n // 100
    n %= 100
    count_20 = n // 20
    n %= 20
    count_10 = n // 10
    n %= 10
    count_5 = n // 5
    n %= 5
    count_1 = n
    print(count_100 + count_20 + count_10 + count_5 + count_1)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()