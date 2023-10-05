def are_anagram(str1, str2):
    #check the lenght of the string 
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)


    for i in range(len(sorted_str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
    return True

def main():
    x = "apple"
    y = "apple"

    result = are_anagram(x, y)
    return print(result)

if __name__ == "__main__":
    main() 