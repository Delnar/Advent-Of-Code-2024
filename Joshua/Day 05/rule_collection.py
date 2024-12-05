from rule import Rule

class RuleCollection:

	def __init__(self):
		self.rules = []

	def add_rule(self, rule):
		# if rule is of type Rule, add it to the rules list
		if isinstance(rule, Rule):
			self.rules.append(rule)
		# if rule is of type str, create a new Rule object and add it to the rules list
		elif isinstance(rule, str):
			self.rules.append(Rule(rule))

	def print_rules(self):
		for rule in self.rules:
			print(rule)