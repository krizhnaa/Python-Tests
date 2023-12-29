
try:
    txt_file = open("file.txt", 'r')
except FileNotFoundError:
    txt_file = open("file.txt", 'w')
    txt_file.write("It has content now")
    # print("Some error")
else:
    content = txt_file.read()
    print(content)
finally:
    print("IDC")