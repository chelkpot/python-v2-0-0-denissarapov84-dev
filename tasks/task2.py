# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    minutes_in_day = n % 1440
    hours = minutes_in_day // 60
    minutes = minutes_in_day % 60
    print(hours, minutes)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()