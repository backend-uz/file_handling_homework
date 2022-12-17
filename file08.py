def main(data):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mx = '0'
    i = 0
    while i < len(data):
        if data[i].isdigit():
            if data[i] > mx:
                mx = data[i]
        i += 1
    return mx
# Read data from file
f = open('txt_file/data08.txt', 'r')
r = f.read() #ss
print(main(r))