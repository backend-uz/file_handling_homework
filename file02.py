def main(data):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    # ls = []
    # for i in data:
    #     ls.append(i)
    # j = ''.join(ls)
    # # c = j.count()
    # return j
    r = data.replace("\n", " ")
    c = len(r)
    return c
# Read data from file
f = open('txt_file/data02.txt', 'r')
r = f.read()
print(main(r))