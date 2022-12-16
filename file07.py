def main(data):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sum = 0
    for i in range(len(data)):
        if data[i].isdigit():
            sum = sum + int(data[i])
    return sum
# Read data from file
f = open('txt_file/data07.txt', 'r')
r = f.read()
print(main(r))