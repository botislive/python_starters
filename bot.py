import os

os.chdir("C:/Users/lenovo/Documents")
path=os.getcwd()
print(f"Current working directory: {path}")

# List all files in the current directory
files = os.listdir(path)

for file in files:
    if os.path.isfile(file):
        ext=os.path.splitext(file)[1][1:]
        if not os.path.exists(ext):
            os.mkdir(ext)
        os.rename(file, os.path.join(ext, file))