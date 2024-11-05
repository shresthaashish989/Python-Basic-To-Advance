words_upto_19=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
 "seventeen", "eighteen", "nineteen"]
words_upto_tens=["", "", "twenty", "thirty", "forty", "fifty","sixty", "seventy", "eighty", "ninety"]

n=int(input("enter the number:"))
if n==0:
    print("zero")
elif n<=19:
    print(words_upto_19[n])
elif n<=99:
    print(words_upto_tens[n//10]+words_upto_19[n%10])
else:
    print("please enter number between 0 to 99")








