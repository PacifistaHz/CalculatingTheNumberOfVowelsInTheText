text=input("Enter a string: ")
text=text.lower()
vowels="aeiouAEIOU"
counter=0
for i in text:
    for j in vowels:
        if i==j:
            counter+=1
print("%s' vowels in the tesxt are: %d" % (text,counter))