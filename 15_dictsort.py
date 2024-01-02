my_dict={"e":5,"b":2,"c":3,"a":1,"d":4}
my_list=list(my_dict.items())
asc_my_list=sorted(my_list)
des_my_list=sorted(my_list,reverse=True)

asc_my_dict=dict(asc_my_list)
des_my_dict=dict(des_my_list)
print("Ascending order :",asc_my_dict)
print("Descending order :",des_my_dict)
