def  print_binary(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = ["0", "."]
    while num > 0:
        if len(binary) > 32:
            return "ERROR"
        r = num * 2
        if r >= 1:
            binary.append("1")
            num = r - 1
        else:
            binary.append("0")
            num = r

    return "".join(binary)


print(print_binary(0.72))

