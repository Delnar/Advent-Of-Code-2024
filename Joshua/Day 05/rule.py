class Rule:
	def __init__(self, ruleText):
		self.rule = ruleText
		# Split the rule into two parts
		parts = ruleText.split("|")		

		# Before and after are integers
		self.before = int(parts[0])
		self.after  = int(parts[1])

	def __str__(self):
		return f"{self.before} -> {self.after}"