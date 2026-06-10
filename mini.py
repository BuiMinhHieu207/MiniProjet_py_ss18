products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]


def menu():
    print("_"*50)
    print("     QUẢN LÍ CỬA HÀNG - MINI STORE       ")
    print("_"*50)
    print("1. Xem danh sách sản phẩm hiện có")
    print("2. Thêm mới 1 sản phẩm")
    print("3. Cập nhật sản phẩm theo ID")
    print("4. Thoát chương trình")
    print("_"*50)


def show_products():
    if not products:
        print("Cữa hàng hiện chưa có sản phẩm nào!")
        return
    print("--- DANH SÁCH SẢN PHẨM ---")
    print(f"{'ID':<5} | {'Tên sản phẩm':<10} | {'Giá bán':<10}")
    print("_"*30)
    for item in products:
        print(f"{item["id"]:<5} | {item["name"]:<10} | {item["price"]:<10}")




def add_product():
    print("--- THÊM SẢN PHẨM --- ")
    while True:
        new_id = input("Nhập mã sản phẩm: ")
        new_id = new_id.upper().strip()
        if new_id == "":
            print("Không được để trống!")
            continue

        new_name = input("Nhập tên sản phẩm: ")
        if new_name == "":
            print("Không được để trống!")
            continue

        new_price = int(input("Nhập giá sản phẩm: "))
        if new_price == "":
            print("Không được để trống!")
            continue

        new_product = {
            "id": new_id,
            "name": new_name,
            "price": new_price
        }
        products.append(new_product)
        print("Đã thêm sản phẩm thành công!")
        break



def update_price():
    found = False
    update_product = input("Nhập ID muốn cập nhật: ")
    update_product = update_product.upper().strip()
    for product in products:
        if product["id"] == update_product:
            print(f"Tìm thấy sản phẩm: {product["name"]} (giá hiện tại: {product["price"]})")
            product["price"] = input("Nhập giá mới: ")
            found = True
            print("Cập nhật thành công!")
    if not found:
        print("Không tìm thấy ID!")



def main():
    while True:
        menu()
        choice = input("Nhập chức năng: ")
        match(choice):
            case "1":
                show_products()
            case "2":
                add_product()
            case "3":
                update_price()
            case "4":
                print("Cảm ơn bạn đã dùng phần mềm!")
                print("[Chương trình kết thúc]")
                break
            case _:
                print("Không hợp lệ!")

main()