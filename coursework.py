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
    for i in range(2,number):
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
    text_file=text_file.replace('--',' ')
    text_file=text_file.lower().split()
    characters=['"','!',',',';','\'','-',')','(',':','/','%','&','?','.']
    for i in characters:
        text_file=[j.rstrip(i) for j in text_file]
        text_file=[k.lstrip(i) for k in text_file]
    return text_file

# Sample output of the read function using the given test file
all_words = get_words('desktop/sense_and_sensitivity.txt')
print("there are ",len(all_words),"words")

# Function that returns a dictionary of words that end in ly for keys
# and the number of times each word appears as for values
def get_dic(words):
    new_words=[]
    ly_dic={}
    for i in words:
        if i.endswith('ly'):
            new_words.append(i)
    for item in new_words:
        if item in ly_dic:
            ly_dic[item]+=1
        else:
            ly_dic[item]=1
    return ly_dic

# Sample output of the get_dic function using the output of the get_words function
ly_words = get_dic(all_words)
print("there are ",len(ly_words),"ly words")

def get_top_ly_words(dic):
    most_common = []
    while len(most_common) < 10:
        max_word=max(dic, key=dic.get)
        top_word=[]
        top_word.append(max_word)
        top_word.append(dic[max_word])
        top_word=tuple(top_word)
        most_common.append(top_word)
        del dic[max_word]
    return most_common

# Sample output of get_top_ly_words function
common_words=get_top_ly_words(ly_words)
print('The top ten ly words are:')
for i in common_words:
    print(i[0],i[1])
