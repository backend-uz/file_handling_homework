def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mn = '0'
    for i in range(len(data)):
        if data[i].isdigit:
            if data[i] < mn:
                mn += data[i]
    return mn
            
# Read data from file
f = open('txt_file/data09.txt', 'r')
r = f.read()
print(main(r))