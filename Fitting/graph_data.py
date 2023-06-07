import matplotlib.pyplot as plt
import sys


def parse_file(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split('\t')
            x.append(float(values[0].replace(',', '.')))
            y.append(float(values[1].replace(',', '.')))
    return x, y

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No data file. Usage: python graph_data.py filename")
        sys.exit(1)

    filename = sys.argv[1]
    x, y = parse_file(filename)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(filename)
plt.show()

