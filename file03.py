def main(data):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ls = []
    for i in data:
        if i.isdigit():
            ls.append(i)
    return ls
# Read data from file
f = open('txt_file/data03.txt', 'r')
r = f.read()
print(main(r))