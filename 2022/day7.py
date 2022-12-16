class Directory:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self.childen = list()
        self.size = size
    def add_subdirectory(self, name):
        self.childen.append(Directory(name,self))

    def add_file(self, size):
        self.size += size
        self.parent.add_file(size)

    def get_size(self):
        return self.size

def pt2():
    with open('day7test.input', 'r') as f:
        for l in f:
            # parse structure
            print(l)
            l = l.strip()
            if l[0:4] == '$ cd':
                # change directory command
                if l[5:7] == '..':
                    # go to parent directory
                    pass
                else:
                    # change to child directory
                    child_name = l[5:]


# print(pt1())
print(pt2())