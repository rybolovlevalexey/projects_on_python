n = int(input())
dict_classes = dict()
for i in range(n):
    st = input()
    if ':' not in st:
        dict_classes[st.strip()] = -1
    else:
        name, others = st.split(' : ')
        if ' ' in others:
            others = others.split()
        else:
            others = [others]
        dict_classes[name] = others
m = int(input())
sp = list()
for j in range(m):
    name = input()
    flag = False
    if dict_classes[name] != -1:
        for parents in dict_classes[name]:
            if parents in sp:
                flag = True
                break
    if flag:
        print(name)
    sp.append(name)
