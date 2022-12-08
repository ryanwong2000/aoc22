# cheater cheater pumpkin eater
# p1: 1443806
# p2: 942298

def read_file(filename, folder="inputs"):
    with open(f"{folder}/{filename}", "r") as infile:
        output = infile.read().splitlines()
    return output

def get_path(path, cd_arg):
    if cd_arg == "/":
        return "/"
    elif cd_arg == "..":
        return "/".join(path.split("/")[:-1])
    else:
        return f"{path}/{cd_arg}".replace("//","/")

infile = read_file("input.in", "day7")

entities = []

path = ""
entity = {}
entity["name"] = "/"
entity["path"] = path
entity["type"] = "dir"
entities.append(entity)
for this_line in infile:
    line_tokens = this_line.split(" ")
    if line_tokens[0] == "$":
        if line_tokens[1] == "cd":
            path = get_path(path, line_tokens[2])
    elif line_tokens[0] == "dir":
        entity = {}
        entity["name"] = line_tokens[1]
        entity["path"] = path
        entity["type"] = "dir"
        entities.append(entity)
    elif line_tokens[0][0].isdigit():
        entity = {}
        entity["name"] = line_tokens[1]
        entity["path"] = path
        entity["type"] = "file"
        entity["size"] = line_tokens[0]
        entities.append(entity)

directories = []

for entity in entities:
    if entity["type"] != "dir":
        continue
    current_path = (entity["path"] + "/" + entity["name"]).replace("//","/")
    dir_size = sum(int(e["size"]) for e in entities if e["type"] == "file" and e["path"].startswith(current_path))
    directories.append({**entity, "size": dir_size})

print(sum(d["size"] for d in directories if d["size"] <= 100000))

total_disk_space = 70000000
space_needed = 30000000
space_available = total_disk_space - sum(d["size"] for d in directories if d["name"] == "/")
space_to_free = space_needed - space_available

dirs = [d for d in directories if d["size"] >= space_to_free]
print(min([d["size"] for d in directories if d["size"] >= space_to_free]))