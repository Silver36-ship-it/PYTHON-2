def rotate(value1,value2,value3):
    return value3,value1,value2
def main():
    a = 'doug'
    b = 22
    c = 1984
    a,b,c = rotate(a,b,c)
    print(a,b,c)
    a,b,c = rotate(a,b,c)
    print(a,b,c)
    a,b,c = rotate(a,b,c)
    print(a,b,c)
main()