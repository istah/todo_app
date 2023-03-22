contents = ['1', '2', '3']

filenames = ['doc.txt', 'report.txt', 'pre.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()
