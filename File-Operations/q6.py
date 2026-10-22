# write multiple lines using writelines()

data = ['vuvov ovbv ovno\n iibi v iubviv iuvb\neubv qu caoo qof edvs']

with open('demo.txt', 'w') as f:
    f.writelines(data)