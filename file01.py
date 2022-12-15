def main(data):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ls = []
    i = 0
    for i in data.split(','):
        ls.append(int(i))
    return ls
# Read data from file
f = open('txt_file/data01.txt', mode='r')
r = f.read()
print(main(r))