import os

def activate_text_env(path):
    """
    Function to read api key text file from gdrive into colab.
    """
    with open(path) as f:
        while True:
            variable = f.readline().strip()
            if len(variable) == 0:
                break
            key = f.readline().strip()
            os.environ[variable] = key
    return 0