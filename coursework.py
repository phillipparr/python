#Question one
# This reads a file and returns a list of integers
def read_file(file):
    open_file=open(file,'r')
    text_file=open_file.read()
    text_file=text_file.strip().split(',')
    text_file = [i.strip() for i in text_file]
    text_file = [int(i) for i in text_file]
    print("Numbers: ",text_file)
    return text_file

# This checks if a single integer is prime
def isPrime(number):
    for i in range(2,number-1):
        if number % i == 0:
            return False
        else:
            return True

# This allows you to use the isPrime function on a list and prints the results
def print_numbers(numbers):
    for num in numbers:
        if isPrime(num):
            print('{}: Prime'.format(num))
        else:
            print('{}: Not Prime'.format(num))

# This is an example of using the file you just read and passing it through
# the functions above, using the given test file
numbers = read_file('numbers.txt')
print_numbers(numbers)

#Question two
string1 = 'BBEBDEAEBADAAEDCDDBCBACBBCBDDBABBDEECDBAECACEECC'
string2 = 'CCBADACDCCADDBDABDEDCDDBCBACBBCBDDBABBDEECCACCBDCEBABBBEDC'
def common_string(a,b):
    common_string=[]
    for i in range(len(a)):
        if a[i] in b:
            common_string.append(a[i])
            for j in range(i+1,len(a)):
                if a[i:j] in b:
                    common_string.append(a[i:j])
                else:
                    continue
        else:
            continue
    print(max(common_string, key = len))
common_string(string1,string2)
