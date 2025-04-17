import glob
news = []
filenames = glob.glob('Files/*.txt')

print(filenames)

for filename in filenames:
    new = filename[6:]
    news.append(new)


