import itertools
def liet_ke_hoan_vi(danh_sach):
    print(f"Danh sách ban đầu: {danh_sach}") 
    cac_hoan_vi = list(itertools.permutations(danh_sach))
    print(f"Có tổng cộng {len(cac_hoan_vi)} hoán vị:")
    for index, value in enumerate(cac_hoan_vi, 1):
   
        print(f"Hoán vị {index}: {list(value)}")
if __name__ == "__main__":

    my_list = [1, 2, 3]
    liet_ke_hoan_vi(my_list)