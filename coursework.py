#Question one
# This reads a file and returns a list of integers
def readnumbers(file_name):
    open_file=open(file_name,'r')
    text_file=open_file.read()
    text_file=text_file.strip().split(',')
    text_file = [i.strip() for i in text_file]
    text_file = [int(i) for i in text_file]
    print("Numbers: ",text_file)
    return text_file

# This checks if a single integer is prime
def isPrime(number):
    if number == 2:
        return False
    for i in range(2,number-1):
        if number % i == 0:
            return False
    else:
        return True

# Test a single number
print(isPrime(2))

# This allows you to use the isPrime function on a list and prints the results
def print_numbers(numbers):
    for num in numbers:
        if isPrime(num):
            print('{}: Prime'.format(num))
        else:
            print('{}: Not Prime'.format(num))

# This is an example of using the file you just read and passing it through
# the functions above, using the given test file
numbers = readnumbers('numbers.txt')
print_numbers(numbers)



#Question two

# This reads a file and returns a tuple
def readsequence(file_name):
    open_file=open(file_name,'r')
    text_file=open_file.read()
    text_file=text_file.strip().split('\n')
    text_file=tuple(text_file)
    print(text_file)
    return text_file

# This gives example output from the read_file function
readsequence('sequences.txt')

# This is a function that outputs the longest common string from two strings
def longest_common_string(st1,st2):
    common_string=[]
    for i in range(len(st1)):
        if st1[i] in st2:
            common_string.append(st1[i])
            for j in range(i+1,len(st1)):
                if st1[i:j] in st2:
                    common_string.append(st1[i:j])
                else:
                    continue
        else:
            continue
    longest = max(common_string, key = len)
    length=len(longest)
    print('The longest common substring is', longest, 'of size ', length)
    return longest

# This gives example output from the common_string function
string1 = 'BBEBDEAEBADAAEDCDDBCBACBBCBDDBABBDEECDBAECACEECC'
string2 = 'CCBADACDCCADDBDABDEDCDDBCBACBBCBDDBABBDEECCACCBDCEBABBBEDC'
longest_common_string(string1,string2)

# Question 3

# Read file function
def get_words(file_name):
    open_file=open(file_name,'r')
    text_file=open_file.read()
    text_file=text_file.replace(';','')
    text_file=text_file.replace(',','')
    text_file=text_file.replace('.','')
    text_file=text_file.replace('?','')
    text_file=text_file.replace('!','')
    text_file=text_file.replace(':','')
    text_file=text_file.lower().split()
    print(text_file)
    return text_file
get_words('desktop/sense_and_sensitivity.txt')
