new_lines = []

with open("../data/census.csv") as f:
    lines = f.readlines()
    for line in lines:
        new_line = line.replace(", ", ",")
        new_lines.append(new_line)

with open("../data/clean_census.csv", "w") as f:
    for line in new_lines:
        f.write(line)