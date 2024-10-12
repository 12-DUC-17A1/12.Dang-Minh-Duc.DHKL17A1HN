import json
from datetime import datetime
#Ghi dữ liệu giao dịch vào file JSON
def save_transaction(transaction_data, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(transaction_data)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
#Hỏi người dùng về giao dịch
def record_transaction():
    transaction_type = input("Nhập loại giao dịch: ")
    amount = float(input("Nhập số tiền giao dịch: "))
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"type": transaction_type,
            "amount": amount,
            "time": time_now}
#Chương trình chính
transactions_file = 'transactions.json'
while True:
    transaction = record_transaction()
    save_transaction(transaction, transactions_file)
    cont = input("Bạn có muốn ghi tiếp giao dịch? (1: Có, 0: Không): ")
    if cont == '0':
        break
