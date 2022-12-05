import sys
import string

x = sys.argv
s = sys.argv[1]
n = sys.argv[2]

words = s.split(" ")

filterwords = []
for word in words:
    for c in word:
        counter = sum(1 for char in word if char.isalpha())
        if(counter > int(n)):
            filterwords.append(word)

print(filterwords)


# temp = []
# for i,value in enumerate(s):
#     for j in string.punctuation:
#         if value != j:
#             if j == " ":
                
#     print(i,value)
#counter = 0

# for i in s:
#         if i != j:
#             counter += 1
