raw_input = "   nGuyen vaN aN  ;  2004   "
NAM_HIEN_TAI = 2026


def hien_thi_menu():
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")


def chuc_nang_1():
    """In trực tiếp chuỗi raw_input để kiểm tra dữ liệu thô."""
    print("\n[Chức năng 1] Dữ liệu gốc:")
    print(f"  >> '{raw_input}'")


def chuc_nang_2():
    """Chuẩn hóa họ tên (Title Case) và tính tuổi thành viên."""
    phan = raw_input.split(";")
    ho_ten_raw = phan[0] 
    nam_sinh_raw = phan[1] 

    ho_ten = ho_ten_raw.strip().title()

    
    nam_sinh = int(nam_sinh_raw.strip())

    tuoi = NAM_HIEN_TAI - nam_sinh

    print("\n[Chức năng 2] Thông tin sau chuẩn hóa:")
    print(f"  Họ và tên : {ho_ten}")
    print(f"  Năm sinh  : {nam_sinh}")
    print(f"  Tuổi      : {tuoi}")


def chuc_nang_3():
    """Tạo Mã ID và Email tự động, in thẻ thành viên căn lề."""
    # ── Bóc tách dữ liệu ───────────────────────────────────
    phan       = raw_input.split(";")
    ho_ten_raw = phan[0].strip()          # "nGuyen vaN aN"
    nam_sinh   = phan[1].strip()          # "2004"

    # Tách từng từ trong họ tên
    cac_tu = ho_ten_raw.split()           # ['nGuyen', 'vaN', 'aN']
    ho         = cac_tu[0]               # "nGuyen"
    ten_dem    = cac_tu[1]               # "vaN"
    ten_chinh  = cac_tu[2]               # "aN"

    # ── Tạo Email ──────────────────────────────────────────
    # Chữ cái đầu của Họ + chữ cái đầu của Tên đệm + Tên chính → viết thường
    email = (ho[0] + ten_dem[0] + ten_chinh).lower() + "@company.com"
    # Ví dụ: n + v + an → nvan@company.com

    # ── Tạo Mã ID ──────────────────────────────────────────
    # Tên chính viết hoa + 2 số cuối năm sinh (slicing)
    ma_id = ten_chinh.upper() + nam_sinh[-2:]
    # Ví dụ: AN + 04 → AN04

    # ── In Thẻ Thành Viên (f-string căn lề) ────────────────
    do_rong = 38          # Độ rộng nội dung bên trong khung

    ten_day_du = (ho + " " + ten_dem + " " + ten_chinh).strip().title()

    print("\n[Chức năng 3] Thẻ Thành Viên:")
    print("+" + "-" * do_rong + "+")
    print(f"|{'  CLUB MEMBER CARD':^{do_rong}}|")
    print("+" + "-" * do_rong + "+")
    print(f"|  {'Họ và tên':<12}: {ten_day_du:<{do_rong - 17}}|")
    print(f"|  {'Năm sinh':<12}: {nam_sinh:<{do_rong - 17}}|")
    print(f"|  {'Mã ID':<12}: {ma_id:<{do_rong - 17}}|")
    print(f"|  {'Email':<12}: {email:<{do_rong - 17}}|")
    print("+" + "-" * do_rong + "+")


def chuc_nang_4():
    """In lời chào tạm biệt và kết thúc chương trình."""
    print("\nCảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")


while True:
    hien_thi_menu()
    lua_chon = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if lua_chon == "1":
        chuc_nang_1()
    elif lua_chon == "2":
        chuc_nang_2()
    elif lua_chon == "3":
        chuc_nang_3()
    elif lua_chon == "4":
        chuc_nang_4()
        break                      
    else:
        print("\n⚠  Lựa chọn không hợp lệ, vui lòng nhập lại!")