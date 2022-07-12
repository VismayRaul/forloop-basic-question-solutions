#---------------------------FINDING THE ELEMENT TYPE FROM THE LIST------------------------------
final_type_list = []
input_list = [12, "hello", 12.5, 2j]
for list_show in range(len(input_list)):
    type_list = type(input_list[list_show])
    final_type_list.append(type_list)
print(final_type_list)