with open("data.txt", "r+") as f:
    content = f.read()
    for i in range(3):
        f.write(content)
