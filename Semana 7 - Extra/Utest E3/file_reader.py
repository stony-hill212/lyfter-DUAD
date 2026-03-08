def read_lines(path):
    try:
        with open(path,"r")as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")