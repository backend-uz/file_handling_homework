def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num = []
    al = []

    for i in data:
        if i.isdigit():
            num.append(i)
    for i in data:
        if not i.isdigit():
            al.append(i)
            
    ls = []
    ls.append(len(num))
    ls.append(len(al))
    return ls
# Read data from file
f = open('txt_file/data05.txt', 'r')
r = f.read()
print(main(r))