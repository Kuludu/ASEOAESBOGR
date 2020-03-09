#!/usr/bin/python3

synthesis_database = set()

def add(fact):
	synthesis_database.add(fact)

def search(fact):
	if fact in synthesis_database:
		return True
	else:
		return False
