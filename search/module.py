class Obj:
    def __init__(self, a, b, c):
        self.cups = {'a':[a, 16], 'b':[b, 9], 'c':[c, 7]}
        self.parents = None

    def return_list(self):
        return [self.cups['a'][0], self.cups['b'][0], self.cups['c'][0]]

def operator(dictionary, i, j):
    sub = dictionary.cups[j][1] - dictionary.cups[j][0]
    new_i = dictionary.cups[i][0] - sub
    new_j = dictionary.cups[j][0] + sub

    if new_i < 0:
        new_j += new_i
        new_i = 0

    tmp_list = dictionary.cups.keys()
    for k in range(len(tmp_list)):
        if i == tmp_list[k] or j == tmp_list[k]:
            tmp_list[k] = None

    third = ''
    for k in tmp_list:
        if k != None: third = k
    third_var = dictionary.cups[third][0]

    if(0 <= new_i <= dictionary.cups[i][1] and 0 <= new_j <= dictionary.cups[j][1] and 0 <= third_var <= dictionary.cups[third][1]):
        if i == 'a' and j == 'b' and third == 'c': return Obj(a = new_i, b = new_j, c = third_var)
        if i == 'a' and j == 'c' and third == 'b': return Obj(a = new_i, c = new_j, b = third_var)
        if i == 'b' and j == 'a' and third == 'c': return Obj(b = new_i, a = new_j, c = third_var)
        if i == 'b' and j == 'c' and third == 'a': return Obj(b = new_i, c = new_j, a = third_var)
        if i == 'c' and j == 'a' and third == 'b': return Obj(c = new_i, a = new_j, b = third_var)
        if i == 'c' and j == 'b' and third == 'a': return Obj(c = new_i, b = new_j, a = third_var)
    else:
        print("[-] New Object was not appended because of its out bound capacity.")
        print("[-] %s: %d, %s: %d, %s: %d" % (i, new_i, j, new_j, third, third_var))
