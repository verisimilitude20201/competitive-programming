def convert_to_binary(num)
	binary = []
	binary.append(".")
	while num > 0:
		r = num * 2
		if r >= 1:
		    binary.append("1")
			num = r - 1
		else:
			binary.append("0")
			num = r
	
	return "".join(binary)