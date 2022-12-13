def main(data):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    ls = []
    for i in data:
        ls.append(i)
    return ls

f = open('txt_file/data01.txt')
# Read data from file
print(main(f))