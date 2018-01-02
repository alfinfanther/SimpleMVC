
def showAllView(list):
    lst =[]
    ldata={}
    for xc in list:
        ldata['full_name'] = xc.full_name
        ldata['email'] = xc.email
        lst.append(ldata)
    print(lst)