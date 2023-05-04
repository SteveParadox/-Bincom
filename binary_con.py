import random

def binary_numbers():
    binary_num = [random.randint(0,1) for i in range(4)]
    binary_ = ''.join(str(d) for d in binary_num)
    decimal_num = int(binary_, 2)

    return binary_num, binary_, decimal_num

binary_num, binary_, decimal_num = binary_numbers()

print("Binary digits: ", binary_num)
print("Binary string: ", binary_)
print("Decimal number: ", decimal_num)
