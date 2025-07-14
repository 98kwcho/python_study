def print_star(num):
    str_star = ""
    for i in range(num):
        str_star += "*"
    return str_star

list_star = [20, 1 , 12, 9 , 18]

for i in range(len(list_star)):

    print(f"{list_star[i]}.\t{print_star(list_star[i])}")

