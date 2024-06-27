#file = open("storage.txt", "r")
#print(file.readline(6))

#file = open("storage.txt", "r")
#var = file.readlines()
#print(var)

''''lines = [line.strip() for line in open("storage.txt")]
for line in lines:
    print(line)'''

'''lines = [line.strip() for line in open("storage.txt")]
print(lines)

file = open("storage.txt", "r")
print(file.readlines())'''

'''file = open("storage.txt", "w")
file.write("Hello\n")
file.write("Summer\n")
file.write("Goodbye\n")
file.close()'''
            
'''file = open("storage.txt", "w")
print("Hello", file=file)
print("Love", file=file)
print("Goodbye", file=file)
file.close()'''


while True:
    file = open("storage.txt", "a")
    name = input("Name: ")
    print(name, file=file)
    file.close()




      