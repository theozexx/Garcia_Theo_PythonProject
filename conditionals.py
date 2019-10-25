#check a temperature and output a result
#
temperature = int (input("\ninput a number between 0 and 100\n"))

if temperature <= 4:
	print("\nwater is solid frozen...you could just looked at it... \n")

if temperature < 100:
	print("\nWater is liquid...cuz it's water...what you expected?\n")

if temperature >= 100:
	print("\nThe water is gas...because it's boiling!\n")

