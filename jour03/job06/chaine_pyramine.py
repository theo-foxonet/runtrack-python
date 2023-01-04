def pyramide(string):
    start = 0
    length = 1
    while start < len(string):
        line = string[start: start+length]
        line += "*" * (length - len(line))
        print(line)
        start += length
        length += 1
pyramide("abcdefghijklmnopqrstuvwxyz" * 10)