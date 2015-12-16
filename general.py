import os

def create_dirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
