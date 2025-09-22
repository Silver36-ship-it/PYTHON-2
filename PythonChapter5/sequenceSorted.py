def is_ordered(sequence):
    return list(sequence) == sorted(sequence)
def main():
    number = [1,2,3,4,5,6]
    print(is_ordered(number))
    print(is_ordered((1,2,3,4)))
    print(is_ordered('abc'))
main()