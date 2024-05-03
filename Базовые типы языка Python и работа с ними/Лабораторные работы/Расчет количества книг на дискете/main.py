# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44
pages_in_book = 100
str_in_pages = 50
symb_in_str = 25
one_symb = 4

one_kb = 1024
one_mb = one_kb * 1024
disk_cap = disk * one_mb
symb_in_book = pages_in_book * str_in_pages * symb_in_str * one_symb
sum_1 = int(disk_cap // symb_in_book)


print("Количество книг, помещающихся на дискету:", sum_1)
