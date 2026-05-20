import re
def tinh_tong_am_duong(chuoi):
    cac_so_tim_thay = re.findall(r'-?\d+', chuoi)
    tong_duong = 0
    tong_am = 0

    for item in cac_so_tim_thay:
        so = int(item)
        if so > 0:
            tong_duong += so
        elif so < 0:
            tong_am += so
            
    return tong_duong, tong_am

if __name__ == "__main__":

    chuoi_ban_dau = "-100#^sdfkj8902w3ir021@swf-20"
    duong, am = tinh_tong_am_duong(chuoi_ban_dau)
    
    print(f"Chuỗi ban đầu là: '{chuoi_ban_dau}'")
    print(f"Kết quả: Giá trị dương: {duong}. Giá trị âm: {am}.")