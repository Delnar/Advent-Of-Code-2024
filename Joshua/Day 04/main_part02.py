from node_collection import NodeCollection

# 
# input.txt
# sample.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

nc = NodeCollection(lines)

count = 0
wordCount = 0
for node in nc.nodes:
    if node.character != 'A':
        continue
    
    # nc.printXWord(node.x, node.y)
    wordCount += nc.compXMASWord(node.x, node.y)  # Upper Left
    count += 1

print(f"Total A nodes: {count}")
print(f"Word Count: {wordCount}")
