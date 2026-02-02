import numpy as np

def main():
	val = input('''Vilken uppgift vill du kontrollera?
				1: Tetraederkoll 
				2: Rätblock och kub
			 	3: Rotation och Volym
				9: Speed run
				> ''')
	# Del 1
	if val == "1":
		val = input('''Vilken sub-uppgift vill du kontrollera?
		1: Avståndsformeln
		2: Tetraederkontroll
		> ''')
		if val == "1":
			upg_1_1()
		elif val == "2":
			upg_1_2()
		return

	# Del 2
	if val == "2":
		val = input('''Vilken sub-uppgift vill du kontrollera?
		1: Skalärprodukt
		2: Rätblockkontroll
		3: Kubkontroll
		> ''')
		if val == "1":
			upg_2_1()
		elif val == "2":
			upg_2_2()
		elif val == "3":
			upg_2_3()
		return
	
	# Del 3
	if val == "3":
		val = input('''Vilken sub-uppgift vill du kontrollera?
		1: Rotationsmatriser
		2: Rotera en kub
		3: Vektorprodukt
		4: Volymberäkning (tetraeder volym)
		> ''')
		if val == "1":
			upg_3_1()
		if val == "2":
			upg_3_2()
		if val == "3":
			upg_3_3()
		if val == "4":
			upg_3_4()
		return
		

	# Speed run
	elif val == "9":
		upg_1_1()
		upg_1_2()
		upg_2_1()
		upg_2_2()
		upg_2_3()
		upg_3_1()
		upg_3_2()
		upg_3_3()
		upg_3_4()
		return
	else:
		return

def upg_1_1():
	p1 = [float(i) for i in input("Ange koordinaterna för punkt 1 med ' ' mellan dem > ").split()]
	p2 = [float(i) for i in input("Ange koordinaterna för punkt 2 med ' ' mellan dem > ").split()]
	print("Avståndet är", distance(p1, p2), "längdenheter")

def upg_1_2():
	punkter = []
	for i in range(1, 5):
		punkter.append([float(i) for i in input(f"Ange koordinaterna för punkt {i} med ' ' mellan dem > ").split()])
	tolerans = float(input("Ange toleransen > "))
	if is_tetraeder(punkter, tolerans):
		print("Det är en regelbunden tetraeder!")
		return
	print("Det är INTE en regelbunden tetraeder.")

def upg_2_1():
	v1 = [float(i) for i in input("Ange x och y för vektor 1 med ' ' mellan dem >").split()]
	v2 = [float(i) for i in input("Ange x och y för vektor 2 med ' ' mellan dem >").split()]
	print(dot_product(v1, v2))

def upg_2_2():
	punkter = []
	print('''Ange hörnen på rätblocket i följande ordning:
	   p0-p1-p2-p3 är ett ansikte, p4-p5-p6-p7 är motsvarande ansikte''')
	for i in range(0, 8):
		punkter.append([float(i) for i in input(f"Ange koordinaterna för punkt {i} med ' ' mellan dem > ").split()])
	tolerans = float(input("Ange toleransen > "))
	if is_rectangular_block(punkter, tolerans):
		print("Det är ett rätblock!")
	else:
		print("Det är INTE ett rätblock.")

def upg_2_3():
	punkter = []
	print('''Ange hörnen på kuben i följande ordning:
	   p0-p1-p2-p3 är ett ansikte, p4-p5-p6-p7 är motsvarande ansikte''')
	for i in range(0, 8):
		punkter.append([float(i) for i in input(f"Ange koordinaterna för punkt {i} med ' ' mellan dem > ").split()])
	tolerans = float(input("Ange toleransen > "))
	if is_cube(punkter, tolerans):
		print("Det är en kub!")
	else:
		print("Det är INTE en kub.")

def upg_3_1():
	vinkel_grader = float(input("Ange rotationsvinkeln i grader > "))
	vinkel = np.radians(vinkel_grader)
	axis = input("Ange rotationsaxeln (x, y eller z) > ").lower()
	if axis == "x":
		R = rotationsmatris_x(vinkel)
	elif axis == "y":
		R = rotationsmatris_y(vinkel)
	elif axis == "z":
		R = rotationsmatris_z(vinkel)
	else:
		print("Felaktig axel angiven.")
		return
	print("Rotationsmatrisen är:")
	print(R)

def upg_3_2():
	punkter = []
	for i in range(0, 8):
		punkter.append([float(i) for i in input(f"Ange koordinaterna för punkt {i} med ' ' mellan dem > ").split()])
	vinkel_grader = float(input("Ange rotationsvinkeln i grader > "))
	vinkel = np.radians(vinkel_grader)
	axis = input("Ange rotationsaxeln (x, y eller z) > ").lower()
	roterade_punkter = rotate_cube(punkter, vinkel, axis)
	print("De roterade punkterna är:")
	if roterade_punkter is None:
		return
	for i, p in enumerate(roterade_punkter):
		print(f"Punkt {i}: {p}")

def upg_3_3():
	v1 = [float(i) for i in input("Ange x, y och z för vektor 1 med ' ' mellan dem >").split()]
	v2 = [float(i) for i in input("Ange x, y och z för vektor 2 med ' ' mellan dem >").split()]
	cross = vektorprodukt(v1, v2)
	print("Vektorprodukten är:", cross)
def upg_3_4():
	punkter = []
	for i in range(1, 5):
		punkter.append([float(i) for i in input(f"Ange koordinaterna för punkt {i} med ' ' mellan dem > ").split()])
	volym = tetraeder_volym(punkter)
	print("Volymen av tetraedern är:", volym)


def distance(p1, p2):
	"""
	Beräknar avståndet mellan två punkter i 3D
	:param p1: Punkt 1 koordinater, lista/array med [x, y, z]
	:param p2: Punkt 2 koordinater, lista/array med [x, y, z]
	:return: Avståndet som en float
	"""
	p1 = np.array(p1)
	p2 = np.array(p2)
	diff = p1 - p2
	d = np.linalg.norm(diff)
	return d

def is_tetraeder(punkter, tolerans=0.001):
	"""
	Kontrollera om 4 punkter bildar en regelbunden tetraeder
	:param punkter: Lista med 4 punkter [[x, y, z], [x, y, z], ...]
	:param tolerans: Max skillnad mellan kantlängder som accepteras
	:return: True om tetraeder, False annars
	"""
	distances = []
	for i in range(3):
		for j in range(i+1, 4):
			distances.append(distance(punkter[i], punkter[j]))
	distances = np.array(distances)
	min_d = np.min(distances)
	max_d = np.max(distances)
	diff = max_d - min_d
	if diff > tolerans:
		return False
	return True

def dot_product(v1, v2):
	"""
	:param v1: 2d Vektor [x, y]
	:param v2: 2d Vektor [x, y]
	:return: Skalärprodukten av v1 och v2 i form av float
	"""
	return np.dot(v1, v2)

def is_rectangular_block(punkter, vinkel_tolerans=0.001):
	"""
	Kontrollera om 8 punkter bildar ett rätblock
	:param punkter: Hörnen på rätblocket på formen: [[x, y, z], [x, y, z], ...]
					Måste vara ordnade så att:
					p0-p1-p2-p3 är ett ansikte, p4-p5-p6-p7 är motsvarande ansikte
	:param vinkel_tolerans: Max skillnad från 90 grader i skalärprodukt som accepteras
	:return: True om rätblock, False annars
	"""
	bottom_face = punkter[0:4]
	top_face = punkter[4:8]
	side_face_1 = [punkter[0], punkter[1], punkter[5], punkter[4]]
	side_face_2 = [punkter[0], punkter[3], punkter[7], punkter[4]]
	if not is_rectangle(bottom_face, vinkel_tolerans):
		print("Bottenytan är inte en rektangel.")
		return False
	if not is_rectangle(top_face, vinkel_tolerans):
		print("Toppenytan är inte en rektangel.")
		return False
	if not is_rectangle(side_face_1, vinkel_tolerans):
		print("Sida 1 är inte en rektangel.")
		return False
	if not is_rectangle(side_face_2, vinkel_tolerans):
		print("Sida 2 är inte en rektangel.")
		return False
	return True


def is_rectangle(punkter, vinkel_tolerans=0.001):
	"""
	Kontrollera om 4 punkter bildar en rektangel
	:param punkter: Hörnen på rektangeln på formen: [[x, y, z], [x, y, z], ...]
	:param vinkel_tolerans: Max skillnad från 90 grader i skalärprodukt som accepteras
	:return: True om rektangel, False annars
	"""
	for i in range(4):
		p0 = np.array(punkter[i])
		p1 = np.array(punkter[(i+1)%4])
		p3 = np.array(punkter[(i+3)%4])
		v1 = p1 - p0
		v3 = p3 - p0
		dot = np.dot(v1, v3)
		if abs(dot) > vinkel_tolerans:
			return False
	return True

def is_cube(punkter, tolerans=0.001):
	"""
	Kontrollera om 8 punkter bildar en kub
	:param punkter: Hörnen på kuben på formen: [[x, y, z], [x, y, z], ...]
					Måste vara ordnade så att:
					p0-p1-p2-p3 är ett ansikte, p4-p5-p6-p7 är motsvarande ansikte
	:param tolerans: Max skillnad från 90 grader i skalärprodukt som accepteras
	:return: True om kub, False annars
	"""
	if not is_rectangular_block(punkter, tolerans):
		print("Det är inte ett rätblock.")
		return False
	
	vectors = []
	vectors.append(distance(punkter[0], punkter[1]))
	vectors.append(distance(punkter[1], punkter[2]))
	vectors.append(distance(punkter[0], punkter[4]))
	unique_distances = np.unique(np.round(vectors, decimals=5))
	if len(unique_distances) != 1:
		print("Kantlängderna är inte lika.")
		return False
	return True

def rotationsmatris_x(vinkel):
	"""
	Skapa en rotationsmatris för rotation kring x-axeln
	:param vinkel: Vinkeln i radianer
	:return: 3x3 numpy array som är rotationsmatrisen
	"""
	cos = np.cos(vinkel)
	sin = np.sin(vinkel)
	R = np.array([[1, 0, 0],
				   [0, cos, -sin],
				   [0, sin, cos]])
	return R
def rotationsmatris_y(vinkel):
	"""
	Skapa en rotationsmatris för rotation kring y-axeln
	:param vinkel: Vinkeln i radianer
	:return: 3x3 numpy array som är rotationsmatrisen
	"""
	cos = np.cos(vinkel)
	sin = np.sin(vinkel)
	R = np.array([[cos, 0, sin],
				   [0, 1, 0],
				   [-sin, 0, cos]])
	return R
def rotationsmatris_z(vinkel):
	"""
	Skapa en rotationsmatris för rotation kring z-axeln
	:param vinkel: Vinkeln i radianer
	:return: 3x3 numpy array som är rotationsmatrisen
	"""
	cos = np.cos(vinkel)
	sin = np.sin(vinkel)
	R = np.array([[cos, -sin, 0],
				   [sin, cos, 0],
				   [0, 0, 1]])
	return R

def rotate_cube(punkter, vinkel, axel="x"):
	"""
	Rotera alla punkter i en kub
	
	:param punkter: Lista med 8 punkter på formen: [[x, y, z], [x, y, z], ...]
	:param vinkel: Rotationsvinkeln i radianer
	:param axel: "x", "y" eller "z" för rotationsaxeln
	"""
	if is_cube(punkter) == False:
		print("Punkterna bildar inte en kub.")
		return None

	roterande_punkter = []

	if axel == "x":
		R = rotationsmatris_x(vinkel)
	elif axel == "y":
		R = rotationsmatris_y(vinkel)
	elif axel == "z":
		R = rotationsmatris_z(vinkel)
	else:
		print("Felaktig axel angiven.")
		return None
	for p in punkter:
		v = np.array(p)
		v_roterad = np.dot(R, v)
		roterande_punkter.append(v_roterad.tolist())
	return roterande_punkter

def vektorprodukt(v1, v2):
	"""
	Beräkna vektorprodukten v1 x v2
	:param v1: Vektor 1 på formen [x, y, z]
	:param v2: Vektor 2 på formen [x, y, z]
	:return: Vektorprodukten som en lista [x, y, z]
	"""
	v1 = np.array(v1)
	v2 = np.array(v2)
	cross = np.cross(v1, v2)
	return cross.tolist()

def triplescalarprodukt(u, v, w):
	"""
	Beräkna tripleskalärprodukten u * (v x w)
	:param u: Vektor 1 på formen [x, y, z]
	:param v: Vektor 2 på formen [x, y, z]
	:param w: Vektor 3 på formen [x, y, z]
	:return: Tripleskalärprodukten som en float
	"""
	u = np.array(u)
	v = np.array(v)
	w = np.array(w)
	cross = np.cross(v, w)
	triple = np.dot(u, cross)
	return triple

def tetraeder_volym(punkter):
	"""
	Beräkna volymen av en tetraeder med hörn i de givna punkterna
	:param punkter: Lista med 4 punkter [[x, y, z], [x, y, z], ...]
	:return: Volymen som en float
	"""

	p0 = np.array(punkter[0])
	p1 = np.array(punkter[1])
	p2 = np.array(punkter[2])
	p3 = np.array(punkter[3])

	v1 = p1 - p0
	v2 = p2 - p0
	v3 = p3 - p0

	volym = abs(triplescalarprodukt(v1, v2, v3)) / 6.0
	return volym

main()