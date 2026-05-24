order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    print("==================================================")
    
    user_choice = input("Vui lòng chọn chức năng (1-4): ").strip()
    
    if user_choice == "1":
        print("\n--- DANH SÁCH ĐƠN HÀNG ---")
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order_id in enumerate(order_list, start=1):
                print(f"{index}. {order_id}")
                
    elif user_choice == "2":
        print("\n--- THÊM ĐƠN HÀNG MỚI ---")
        new_order = input("Nhập mã đơn hàng mới: ")
        new_order_cleaned = new_order.strip().upper()
        
        if new_order_cleaned == "":
            print("Lỗi: Mã đơn hàng không được để trống!")
        else:
            order_list.append(new_order_cleaned)
            print(f"Thêm thành công đơn hàng: {new_order_cleaned}")
            
    elif user_choice == "3":
        print("\n--- XÓA ĐƠN HÀNG ---")
        delete_order = input("Nhập mã đơn hàng cần xóa: ")
        delete_order_cleaned = delete_order.strip().upper()
        
        if delete_order_cleaned in order_list:
            order_list.remove(delete_order_cleaned)
            print(f"Đã xóa thành công đơn hàng: {delete_order_cleaned}")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
            
    elif user_choice == "4":
        print("\nThoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")