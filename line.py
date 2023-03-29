
def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None 
	Joyce_word_count = 0
	Joyce_strcker_count = 0
	Joyce_image_count = 0
	Mingta_word_count = 0
	Mingta_strcker_count = 0
	Mingta_image_count = 0
	for line in lines:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if name == "Joyce":
			if s[2] == "貼圖":
				Joyce_strcker_count += 1
			elif s[2] == "圖片":
				Joyce_image_count += 1
			else:
				for m in (s[2:]):
					Joyce_word_count += len(m)
		elif name == "Mingta":
			if s[2] == "貼圖":
				Mingta_strcker_count += 1
			elif s[2] == "圖片":
				Mingta_image_count += 1
			else:
				for m in (s[2:]):
					Mingta_word_count += len(m)
	print("Joyce說了",Joyce_word_count,"個字", "傳了", Joyce_strcker_count,"個貼圖", "傳了", Joyce_image_count,"個圖片")
	print("Mingta說了",Mingta_word_count,"個字","傳了", Mingta_strcker_count,"個貼圖", "傳了", Mingta_image_count,"個圖片")
	
def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("LINE.txt")
	lines = convert(lines)
	# write_file("output.txt", lines)

main()