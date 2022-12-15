def main(data):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    c = len(data)
    return c
# Read data from file
f = open('txt_file/data02.txt', 'r')
r = f.read()
print(main(r))