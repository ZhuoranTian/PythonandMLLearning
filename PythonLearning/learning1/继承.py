class Father(object):
    def __init__(self, name): #构造函数
        self.name = name
        print("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name


class Son(Father):
    def getName(self):
        return 'Son ' + self.name


if __name__ == '__main__':
    son = Son('runoob')
    print(son.getName())