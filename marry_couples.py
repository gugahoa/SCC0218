def marry(women, men):
	couples = {}
	men_iter = [(man, candidates) for (man, candidates) in men.items()]

	while (len(men_iter) > 0):
		(man, candidates) = men_iter.pop()
		for woman in candidates:
			if woman not in couples:
				couples[woman] = man
				break

			if women[woman].index(couples[woman]) > women[woman].index(man):
				men_iter.append((couples[woman], men[couples[woman]]))
				couples[woman] = man
				break

	return couples

if __name__ == "__main__":
	women = {
		"Amy": ["Felipao", "Salsicha", "Maquinista"],
		"Bertha": ["Salsicha", "Felipao", "Maquinista"],
		"Clare": ["Felipao", "Salsicha", "Maquinista"],
	}

	men = {
		"Felipao": ["Amy", "Bertha", "Clare"],
		"Maquinista": ["Clare", "Bertha", "Amy"],
		"Salsicha": ["Clare", "Amy", "Bertha"],
	}

	couples = marry(women, men)
	for woman, man in couples.items():
		print(woman, man)
