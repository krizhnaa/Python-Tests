sentence = input("Enter Your Sentence : ").split()
# 🚨 Don't change code above 👆
# Write your code below 👇

result = { sent: len(sent) for sent in sentence}


print(result)