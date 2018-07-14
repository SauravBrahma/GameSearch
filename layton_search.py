# -*- coding: utf-8 -*-
import itertools
import time

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

'''have to figure out which way is more beautiful to use this algorithm...
def iterative_deepening(depth, OPEN, CLOSE):
    for _ in range(depth):
        search_method("depth_first", OPEN, CLOSE)
        
    depth += 1
    obj = Obj(16,0,0)
    OPEN=[]
    CLOSE=[]
    OPEN.append(obj)
    iterative_deepening(depth, OPEN, CLOSE)
'''
# Initialize statements.
start = time.time()
OPEN=[]
CLOSE=[]
answer=[]
obj = Obj(16,0,0)
OPEN.append(obj)
op_com = ['a', 'b', 'c']
op_list = list(itertools.permutations(op_com, 2))
min_path = 15
depth = 1

# available algorithms -> depth_first, width_first, iterative_deepening
algorithm = "depth_first"

while len(OPEN):
    give_dictionary = OPEN.pop(0)
    if give_dictionary.return_list() == [8, 8, 0]:
        answer.append(give_dictionary.return_list())
        while give_dictionary.parents is not None:
            answer.insert(0, give_dictionary.parents.return_list())
            give_dictionary = give_dictionary.parents
        if len(answer)-1 == min_path: break
        
    CLOSE.append(give_dictionary)
    for_open = []

    for i in range(len(op_list)):
        flag = False
        new_obj = operator(give_dictionary, op_list[i][0], op_list[i][1])

        if new_obj is not None:
            new_obj.parents = give_dictionary

            for j in OPEN:
                if new_obj.cups == j.cups: flag = True
            for j in CLOSE:
                if new_obj.cups == j.cups: flag = True

            if flag is False: for_open.append(new_obj)

    OPEN = for_open + OPEN          # depth-first search
    #OPEN += for_open                # width-first search

else: print("[-] Couldn't find paths which includes Goal.")

pc = 0
for i in answer:
    print("--------- %d ---------" % pc)
    print("A : {0} , B : {1} , C : {2}".format(i[0], i[1], i[2]))
    print("")
    pc += 1

print("Time: ", time.time()-start)


'''
The numbers below are average execution times in my environment.
depth : 0.0015
width : 0.0032
'''
