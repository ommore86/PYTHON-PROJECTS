'''FILES'''

f = open("doc.txt", 'a+')
data = input("Start Typing...\n")
while data!="exit":
    f.write(data+"\n")
    data = input()
f.close()