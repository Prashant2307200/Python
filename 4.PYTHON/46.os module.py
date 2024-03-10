import os

print(dir(os))

if(not os.path.exists("data")):
    os.mkdir('data')

for folder in range(100):
    if(not os.path.exists(f"data/Day{folder+1}")):
        os.mkdir(f"data/Day{folder+1}")

for folder in range(100):
    os.rename(f"data/Day{folder+1}",f"data/Tutorial {folder+1}")

folders = os.listdir("data")
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())
os.chdir('./Users')