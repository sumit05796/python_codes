text = input('Enter desired text: ')
def count_vowels(str):
    count = 0
    for j in str:
        if j == 'a' or j == 'A' or\
           j == 'e' or j == 'E' or\
           j == 'o' or j == 'O' or\
           j == 'i' or j == 'I' or\
           j == 'u' or j == 'U' :
                count += 1        
    return count
print(text, count_vowels(text))    