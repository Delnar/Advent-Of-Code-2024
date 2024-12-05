from rule import Rule
from rule_collection import RuleCollection
from page_collection import PageCollection

with open('input.txt', 'r') as file:
    lines = file.readlines()


rc = RuleCollection()
book = []

for line in lines:
	line = line.strip()
	# if the line does not contain a | character, skip it
	if "|" in line:
		rc.add_rule(Rule(line))
	elif "," in line:
		book.append(PageCollection(line))

total = 0
for page in book:
	if page.obeys_rule_collection(rc):
		total += page.get_middle_page()

print(total)


