class Directory:

    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size

    def add_subdirectory(self, name):
        self.children[name] = Directory(name, self)
        print("\tadded", self.get_child(name))

    def add_file(self, size):
        self.size += int(size)
        if self.parent is None:
            return
        else:
            self.parent.add_file(int(size))

    def has_children(self):
        return len(self.children)

    def get_size(self):
        return self.size

    def cd(self, name):
        if name == '..':
            return self.parent
        else:
            return self.children[name]

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_child(self, name):
        return self.children[name]

    def __str__(self):
        ret = f'{self.name} {self.size}\n'
        if len(self.children):
            for item in self.children.items():
                ret += "\t" + item[1].str()
        return ret

    def str(self):
        return self.__str__()

    def sum_sizes_upto(self, val):
        if self.size <= val:
            ret = self.size
        else:
            ret = 0
        if len(self.children):
            for item in self.children.items():
                ret += item[1].sum_sizes_upto(val)
        return ret

    def least_size_over(self, val, l=70000000):
        if self.size >= val:
            l = min(self.size, l)
        else:
            return l
        if len(self.children):
            for item in self.children.items():
                l = item[1].least_size_over(val,l)
        return l


def pt1():
    wd = Directory('/')
    with open('aoc2022/day7.input', 'r') as f:
        line = 1
        for l in f:
            # parse structure
            print(l)
            l = l.strip()
            if line != 1 and l[0:4] == '$ cd':
                # change directory command
                wd = wd.cd(l[5:])
            elif l[0].isnumeric():
                wd.add_file(l.split()[0])
            elif l[0:4] == 'dir ':
                wd.add_subdirectory(l[4:])
            line += 1
    while wd.get_parent() is not None:
        wd = wd.get_parent()
    print(wd)
    # print(wd.get_children())
    print(wd.sum_sizes_upto(100000))
    return wd

a = pt1()
print(a.least_size_over(a.get_size()-40000000))
print("target ", a.get_size()-40000000)
#print(pt1())
# print(pt2())
