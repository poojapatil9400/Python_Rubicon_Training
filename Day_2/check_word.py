#check give word is present or not in a sentence
str = " I Love Python Programming"
str2 = str.split()
print("Love" in str2)


str = input("Enter string : ")
word= input ("Enter a word to check :")
if word in str:
    print("word is present in string")
else :
    print("word is not present in string")