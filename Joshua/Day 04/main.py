from node_collection import NodeCollection

with open('input.txt', 'r') as file:
    lines = file.readlines()

nc = NodeCollection(lines)

count = 0
wordCount = 0
for node in nc.nodes:
    if node.character != 'X':
        continue
    wordCount += nc.compWord("XMAS", node.x, node.y, -1, -1)  # Upper Left
    wordCount += nc.compWord("XMAS", node.x, node.y,  0, -1)  # Upper
    wordCount += nc.compWord("XMAS", node.x, node.y,  1, -1)  # Upper Right
    wordCount += nc.compWord("XMAS", node.x, node.y, -1,  0)  # Left
    wordCount += nc.compWord("XMAS", node.x, node.y,  1,  0)  # Right
    wordCount += nc.compWord("XMAS", node.x, node.y, -1,  1)  # Lower Left
    wordCount += nc.compWord("XMAS", node.x, node.y,  0,  1)  # Lower
    wordCount += nc.compWord("XMAS", node.x, node.y,  1,  1)  # Lower Right
    count += 1

print(f"Total X nodes: {count}")
print(f"Word Count: {wordCount}")
