#concatenating two string#
x = 'sumit'
y = ' kumar'
print(x+y)                     

#finding length of string#
string_1 = 'good programming'
print(len(string_1))

#accessing single character#
string_1 = 'good programming'
print(string_1[4])            #starts from zero#

#creating a substring#
print(string_1[0:3])
print(string_1[:14])

#splitting a string#
string_2 = 'pyTHon is good programming language '
split_words = string_2.split(' ')
print(split_words)

#accesing individual words#
for i in string_2:
    print(i)
    
#counting substrings#
print('counting substrings = ', string_2.count(' '))

#replacing a substring with another string#
print('replacing a substring = ', string_2.replace('programming', 'DSA'))

#finding a substring#
print('location of substring = ', string_2.find('good'))
print('location of different substring = ', string_2.find('read'))

#comparing substrings#
print('python' == 'Python')
print('python' <= 'Python')
print('python' >= 'Python')

#other operations on string#
print('is 1st letter of every word is uppercase = ', string_2.istitle())
print('every character is digit = ', string_2.isdigit())
print('string contains only  english alphabet = ', string_2.isalpha())
print('all characters of string is in uppercase = ', string_2.isupper())
print('is 1st letter of every word is lowecase = ', string_2.islower())
print('is string starts with p = ', string_2.startswith('p'))
print('is string ends with g = ', string_2.endswith('g'))
print('convert all characters in string to uppercase = ', string_2.upper())
print('convert all characters in string to lowercase = ', string_2.lower())
print('convert upper case to lower and vice-versa = ', string_2.swapcase())
print('removes leading and trailing blank spaces in string = ', string_2.strip())