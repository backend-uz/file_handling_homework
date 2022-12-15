def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ls = []
    for i in data:
        if not i.isdigit():
            ls.append(i)
    return ls
# Read data from file
f = open('txt_file/data04.txt')
r = f.read()
print(main(r))