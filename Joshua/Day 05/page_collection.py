from rule import Rule
from rule_collection import RuleCollection

class PageCollection:
	
	def __init__(self, pages):
		self.pages = []
		pages = pages.split(",")
		for page in pages:
			self.pages.append(int(page))

	def get_middle_page(self):
		return self.pages[len(self.pages) // 2]
	
	def obeys_rule_collection(self, rc):
		for rule in rc.rules:
			# if none of the pages are in the before or after of the rule, go to the next rule
			if rule.before not in self.pages or rule.after not in self.pages:
				continue
			
			# index of rule.before page
			before_index = self.pages.index(rule.before)
			# index of rule.after page
			after_index = self.pages.index(rule.after)

			if before_index > after_index:
				return False
			
		return True
	
	def fix_page_order(self, rc):
		for rule in rc.rules:
			# if none of the pages are in the before or after of the rule, go to the next rule
			if rule.before not in self.pages or rule.after not in self.pages:
				continue
			
			# index of rule.before page
			before_index = self.pages.index(rule.before)
			# index of rule.after page
			after_index = self.pages.index(rule.after)

			if before_index > after_index:
				# swap the two pages
				self.pages[before_index], self.pages[after_index] = self.pages[after_index], self.pages[before_index]
