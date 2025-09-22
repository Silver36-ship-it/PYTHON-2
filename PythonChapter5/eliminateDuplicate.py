def get_unique(value):
    new_set = set(value)
    sorted_set = sorted(new_set)
    return sorted_set
def main():
    number = [1,1,2,4,4,2,3,4,5,6,7,8,9]
    print(get_unique(number))
    words = ['hey','hey','girl','boy','silver','nnenna','nnenna']
    print(get_unique(words))
main()


