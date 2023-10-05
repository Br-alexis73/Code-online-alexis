def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    first_num, second_num = 0, 1
    for i in range(2, n + 1):
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num

    return second_num

def main():
    n = 5
    result = fibonacci(n)
    print(result)

if __name__ == "__main__":
    main()
