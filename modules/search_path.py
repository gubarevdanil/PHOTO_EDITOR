import os

def path_search(file_name):
    abs_path = __file__.split("/")
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, file_name)
    return file_name