import csv

maxI = 10

grid = list(csv.reader(open('dailies.txt', 'r), delimiter='\t'))
grid.pop(0);
cols = grid.pop(0)
print cols;
for i, row in enumerate(grid):
    identifier = row[1]
    ingestDate = row[2]
    print identifier, ingestDate
    for i, col in row[3:]:
        print i, col
    if i > maxI:
        break

    