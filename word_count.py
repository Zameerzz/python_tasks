from heapq import nlargest

n = 10
text = open("sample.txt", "r")
d = {}
result_dict = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
print(d)
for key in list(d.keys()):  # update top ten elements to result_dict
    result_dict = nlargest(n, d, key=d.get)
print("a dictionary with top ten elements", result_dict)
