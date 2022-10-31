# IP = input("Enter the ip >>")
IP = "192.168.156.3"
# Prefix = int(input("Enter prefix >>"))
Prefix = 24
a = []
BINARY = []
Prefix_binary = []

def Print_values(a): # Print value of array and add to BINARY content of it
    for i in range(0, 8):
        print(a[i], end="")
        BINARY.append(a[i])


def Split_IP(IP): # Split 192.168.0.1 into list of 192, 168, 0, 1
    return IP.split(".")


def Change_order(a): # swap the start with the end
    for i in range(0, 4):
        temp = a[i]
        a[i] = a[7 - i]
        a[7 - i] = temp


def Divide_IP(IP): # convert decimal to binary
    a = []
    for i in range(1, 9):
        a.append(int(IP) % 2)
        IP = int(IP) / 2
    Change_order(a)
    Print_values(a)


def Go_through_IP(IP): # does Divide_IP for every octant
    IP = Split_IP(IP)
    for i in range(0, 4):
        Divide_IP(IP[i])
        print("", end=" ")

def Prefix_to_binary(Prefix): # convert prefix (/24) to binary
    for i in range(0,Prefix):
        Prefix_binary.append(1)
    if (Prefix != 33):
        for i in range (Prefix, 32):
            Prefix_binary.append(0)
    print()

def Print_binary(Binary): # prints array of data in ******** ******** ******** ******** format
    print("\n\nPrint binary")
    for i in range(0,32):
        if (i%8==0 and i != 0):
                print("", end= " ")
        print(Binary[i], end="")


def Logical_And(b1,b2): # compares two binaries with Logical AND
    print("\n\nLogical and (&)")
    for i in range(0,32):
        if (i%8==0 and i != 0):
                print("", end= " ")
        print(b1[i]&b2[i], end="")

Go_through_IP(IP)
Prefix_to_binary(Prefix)
Print_binary(Prefix_binary)
Print_binary(BINARY)
Logical_And(Prefix_binary, BINARY)
