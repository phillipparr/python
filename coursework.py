#Question one
numbers = [1046527, 1041147, 8356237, 9753423, 9865433, 99733411, 8217,
897933, 67868712, 7676317]
def isPrime(alist):
    print('Number: {}'.format(alist))
    for num in alist:
        for i in range(2,num-1):
            if num % i == 0:
                print ('{}: Not Prime'.format(num))
                break
        else:
            print('{}: Prime'.format(num))
isPrime(numbers)

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
