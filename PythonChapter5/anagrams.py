def get_anagram(word):
    if len(word) <= 1:
        return [word]
    anagram_list = []
    for char in range(len(word)):
        current_char = word[char]
        remaining_char = word[:char] + word[char + 1:]
    return anagram_list.append(remaining_char)
def main():
    word = 'abcd'
    print(get_anagram(word))
main()