def main(data):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return data.split(',')

f = open('txt_file/data01.txt')
s = f.read()
print(main(s))
# Read data from file