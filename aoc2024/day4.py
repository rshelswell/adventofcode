def forwards(pos, xmax, wordsearch):
    if pos%xmax < xmax-3:
        # print("forwards", wordsearch[pos:pos+4])
        if wordsearch[pos:pos+4] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False

def backwards(pos, xmax, wordsearch):
    if pos%xmax >= 3:
        # print("backwards", wordsearch[pos:pos-4:-1])
        if wordsearch[pos:pos-4:-1] == "XMAS":#
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False
    
def upwards(pos, xmax, ymax, wordsearch):
    if pos//xmax >= 3:
        # print("upwards", wordsearch[pos:pos-3*xmax-1:-xmax])
        if wordsearch[pos:pos-3*xmax-1:-xmax] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False
    
def downwards(pos, xmax, ymax, wordsearch):
    if pos//xmax < ymax-4:
        # print("downwards", wordsearch[pos:pos+3*xmax+1:xmax])
        if wordsearch[pos:pos+3*xmax+1:xmax] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False

def se(pos, xmax, ymax, wordsearch):
    if pos//xmax < ymax-4 and pos%xmax < xmax-3:
        # print("se", wordsearch[pos:pos+4*(xmax+1):xmax+1])
        if wordsearch[pos:pos+3*(xmax+1)+1:xmax+1] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False
    
def sw(pos, xmax, ymax, wordsearch):
    if pos//xmax < ymax-4 and pos%xmax >= 3:
        # print("sw", wordsearch[pos:pos+4*(xmax-1):xmax-1])
        if wordsearch[pos:pos+4*(xmax-1):xmax-1] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False
    
def ne(pos, xmax, ymax, wordsearch):
    if pos//xmax >= 3 and pos%xmax < xmax-3:
        # print("ne", wordsearch[pos:pos-3*xmax:-(xmax-1)])
        if wordsearch[pos:pos-3*xmax:-(xmax-1)] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False
    
def nw(pos, xmax, ymax, wordsearch):
    if pos//xmax >= 3 and pos%xmax >= 3:
        # print("nw", wordsearch[pos:pos-3*(xmax+2):-(xmax+1)])
        if wordsearch[pos:pos-3*(xmax+2):-(xmax+1)] == "XMAS":
            # print("\t++ yes! ++")
            return True
        else:
            return False
    else:
        return False

def day_4a():
    f= open("aoc2024/day4.example")
    lines = f.readlines()
    f.close()
    x_max = len(lines[0])-1
    y_max = len(lines)
    wordsearch = "".join([line.strip() for line in lines])
    xmas_count = 0
    for p in range(0, len(wordsearch)):
        if wordsearch[p] == "X":
            print(f"x = {p%x_max}, y={p//x_max}")
            xmas_count += 1 if forwards(p, x_max, wordsearch) else 0
            xmas_count += 1 if backwards(p, x_max, wordsearch) else 0
            xmas_count += 1 if upwards(p, x_max, y_max, wordsearch) else 0
            xmas_count += 1 if downwards(p, x_max, y_max, wordsearch) else 0
            xmas_count += 1 if se(p, x_max, y_max, wordsearch) else 0
            xmas_count += 1 if sw(p, x_max, y_max, wordsearch) else 0
            xmas_count += 1 if ne(p, x_max, y_max, wordsearch) else 0
            xmas_count += 1 if nw(p, x_max, y_max, wordsearch) else 0
            print(xmas_count)
    print(x_max, y_max, len(wordsearch))
    print(wordsearch[:144])
