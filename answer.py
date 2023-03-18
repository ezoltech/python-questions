#  1.  write a  program that accepts the name and mark of 5-students
#  and will display their name with corresponding mark as follows:

#   Name               Mark
#  ================================== 
#  Abebe               60 
#  Aster               80
#  solution:


print("Name".ljust(60), "Mark");
print("=" * 70);
for i in range(5):
    name = input("Enter name: ");
    mark = input("Enter mark: ");
    print(name.ljust(60), mark);
# 2. write a  program that will display the sum of all numbers that are divisible by 3 starting from 1-30
# solution:

sum = 0
for i in range(1, 31):
    if i % 3 == 0:
        sum += i
print("The sum of all numbers that are divisible by 3 starting from 1-30 is", sum);
# 3.  write a program that will display the following pyramid?
# a.         4                    b.  A   B  C  D
#          3 3                        A   B  C
#       2  2 2                        A   B
#   1   1  1 1                        A
# solution 
# a:
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="");
    print();

#  b:
n = 4
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

# 4.  write a program that accept 10 numbers from keyboard and display their average?
# solution:

n = 10
sum = 0
for i in range(n):
    num = int(input("Enter a number: "));
    sum += num
average = sum / n
print("The average of the 10 numbers is", average);

# 5. write a program that will read a message from key board and append to a file and finally will display contents of the file?
#  solution:

filename = "message.txt"
with open(filename, "a") as f:
    message = input("Enter a message: ")
    f.write(message + "\n")
with open(filename, "r") as f:
    contents = f.read()
    print(contents)
