import os

def activate_text_env(path):
    """
    Function to read api key text file from gdrive into colab.
    """
    with open(path) as f:
        lines = f.readlines()
        variables = lines[::2]
        keys = lines[1::2]

    for v, k in zip(variables, keys):
        os.environ[v.strip()] = k.strip()

    return 0