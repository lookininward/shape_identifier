# shape identifier

def shape_identifier():
	
	state = True

	while state == True:
		sides = input("How many sides does the shape have? ")
		if sides < 3:
			print "Shapes with less than 3 sides are not supported."
			print ""
		elif sides == 3:
			print "It is a Triangle."
			print ""
		elif sides == 4:
			print "It is a Quadrilateral."
			print ""
		elif sides == 5:
			print "It is a Pentagon."
			print ""
		elif sides == 6:
			print "It is a Hexagon."
			print ""
		elif sides == 7:
			print "It is a Heptagon."
			print ""
		elif sides == 8:
			print "It is a Octagon."
			print ""
		elif sides == 9:
			print "It is a Nonagon."
			print ""
		elif sides == 10:
			print "It is a Decagon."
			print ""
		elif sides > 10:
			print "Shapes with more than 10 sides are not supported."
			print ""


shape_identifier()



