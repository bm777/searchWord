t = input("entrer your number of test >")
for i in range(0, int(t)):
	sentence = input("enter your sentence > ")
	word = input("enter your word > ")
	liste = []
	liste = sentence.split(" ")
	print(liste)
	state = False
	ct = 0
	for w in liste:
		if w == word:
			state = True
			ct += 1
	if state == True:
		print("Le mot ['"+word +"'] apparait "+str(ct)+" fois dans la phrase.")
	else:
		print("Le mot '["+word +"]' n'apparait pas dans la phrase.")
