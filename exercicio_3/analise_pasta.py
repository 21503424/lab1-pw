import os

def pede_pasta():
# Path
path = '/home/User/Desktop/file.txt'

# Check whether the
# specified path is
# an existing file
isFile = os.path.isfile(path)
print(isFile)

# Path
path = '/home/User/Desktop/'

# Check whether the
# specified path is
# an existing file
isFile = os.path.isfile(path)
print(isFile)

def calcula_tamanho_pasta