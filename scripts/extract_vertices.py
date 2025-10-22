import struct

INPUT = "C:/Users/Steve/Desktop/ddrmm-luigi-mod/bin/luigimdl0.bin"
OUTPUT = "C:/Users/Steve/Desktop/ddrmm-luigi-mod/exports/luigi.obj"

def is_reasonable_float(f):
    return -1000.0 < f < 1000.0

def is_vertex_group(x, y, z):
    return all(is_reasonable_float(f) for f in (x, y, z))

vertices = []

with open(INPUT, "rb") as f:
    data = f.read()

# Cerca terzetti float32
for i in range(0, len(data) - 12, 4):
    x, y, z = struct.unpack(">fff", data[i:i+12])  # > = big endian
    if is_vertex_group(x, y, z):
        vertices.append((x, y, z))

print(f"Trovati {len(vertices)} vertici")

# Scrive in .obj
with open(OUTPUT, "w") as out:
    for v in vertices:
        out.write(f"v {v[0]} {v[1]} {v[2]}\n")
