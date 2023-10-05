def is_palindrome(str):
    str = str.replace(" ", "").lower()
    reversed_str = str[::-1]

    for i in range(len(str)):
        if str[i] != reversed_str[i]:
            return False

    return True

def main():
    str = "hello"
    result = is_palindrome(str)
    return print(result)

if __name__ == "__main__":
    main()