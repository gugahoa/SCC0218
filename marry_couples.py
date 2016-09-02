def marry(women, men):
	married = {}
	couples = []
	for man in men:
		for woman in men[man]:
			if woman not in married:
				married[woman] = man
				couples.append([man, woman])
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
		"Salsicha": ["Clare", "Amy", "Bertha"],
		"Maquinista": ["Clare", "Bertha", "Amy"]
	}

	couples = marry(women, men)
	for man, woman in couples:
		print(man, woman)
