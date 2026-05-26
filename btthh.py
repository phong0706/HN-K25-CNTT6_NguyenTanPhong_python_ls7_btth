raw_input = "   nGuyen vaN aN   ;   2007   "
current_year = 2026

while True:
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ")
    
    match user_choice:
        case '1':
            print(f"Dữ liệu hiện tại: '{raw_input}'")
            
        case '2':
            data_parts = raw_input.split(';')
            full_name = data_parts[0].strip().title()
            birth_year = int(data_parts[1].strip())
            age = current_year - birth_year
            print(f"Họ tên: {full_name} | Tuổi: {age}")
            
        case '3':
            data_parts = raw_input.split(';')
            full_name = data_parts[0].strip().title()
            birth_year_str = data_parts[1].strip()
            
            name_parts = full_name.split()
            last_name = name_parts[0]
            middle_name = name_parts[1]
            first_name = name_parts[2]
            
            email = f"{last_name[0].lower()}{middle_name[0].lower()}{first_name.lower()}@company.com"
            member_id = f"{first_name.upper()}{birth_year_str[-2:]}"
            
            print(f"\n+{'':-^30}+")
            print(f"|{'THẺ THÀNH VIÊN':^30}|")
            print(f"+{'':-^30}+")
            print(f"| ID:    {member_id:<22} |")
            print(f"| Name:  {full_name:<22} |")
            print(f"| Email: {email:<22} |")
            print(f"+{'':-^30}+")
            
        case '4':
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chỉ nhập số từ 1 đến 5!")    