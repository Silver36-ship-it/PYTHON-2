def is_palindrome(word):
    ignore_case = word.lower()
    return ignore_case[0:] == ignore_case[::-1]
def main():
    word = 'Gieaaaaaaaaaaaaaaaeig'
    print(is_palindrome(word))
main()