# -*- coding: utf-8 -*-
import module
import itertools
import time

# Initialize statements.
obj = module.Obj(16, 0, 0)
goal = [8, 8, 0]
min_path = 15

start = time.time()
OPEN=[]
CLOSE=[]
answer=[]
OPEN.append(obj)
op_com = ['a', 'b', 'c']
op_list = list(itertools.permutations(op_com, 2))

while len(OPEN):
    give_dictionary = OPEN.pop(0)
    if give_dictionary.return_list() == goal:
        answer.append(give_dictionary.return_list())
        while give_dictionary.parents is not None:
            answer.insert(0, give_dictionary.parents.return_list())
            give_dictionary = give_dictionary.parents
        if len(answer)-1 == min_path: break
        
    CLOSE.append(give_dictionary)
    for_open = []

    for i in range(len(op_list)):
        flag = False
        new_obj = module.operator(give_dictionary, op_list[i][0], op_list[i][1])

        if new_obj is not None:
            new_obj.parents = give_dictionary

            for j in OPEN:
                if new_obj.cups == j.cups: flag = True
            for j in CLOSE:
                if new_obj.cups == j.cups: flag = True

            if flag is False: for_open.append(new_obj)

    OPEN = for_open + OPEN          # depth-first search
    #OPEN += for_open                # breadth-first search

else: print("[-] Couldn't find paths which includes Goal.")

pc = 0
for i in answer:
    print("--------- %d ---------" % pc)
    print("A : {0} , B : {1} , C : {2}".format(i[0], i[1], i[2]))
    print("")
    pc += 1

print "Time: ", time.time()-start
