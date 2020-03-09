#!/usr/bin/python3
import synthesis_database
import rule_database

def process():
	while True:
		match = False
		for rule in rule_database.rule_database:
			meet_requirement = True
			for requirement in rule[0]:
				if synthesis_database.search(requirement) == False:
					meet_requirement = False
			if meet_requirement:
				if rule[1][1] == "1":
					return rule[1][0]
				else:
					synthesis_database.add(rule[1][0])
			
		if match == False:
			return False

if __name__ == '__main__':
	print("Please input some facts, separate with whitespace.")
	input_facts = input().split(" ")
	for fact in input_facts:
		synthesis_database.add(fact)

	result = process()
	if result != False:
		print("I know! It's", result)
	else:
		print("Sorry, I don't konw.")		
