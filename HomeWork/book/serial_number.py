"""
    1．程序自动生成销售单的流水号。
      流水号组成部分为：8位日期+3位的员工编号+5位的序列号。组合完成后的流水号中没有符号“+”，如：“2023111600700099”、 “2023111600700100”。
      其中，日期格式如：“20231116”；员工编号如：“007”、“010”；序列号如：“00001”，下一单则为：“00002”，序列号每次增加一个。
      要求：员工上班先输入工号，程序需要先读取上一次的流水号，若没有，则5位序列号从“00001”开始；若已有流水号，则在此基础上序列化自增。
      提示：有没有流水号，本来是从数据库读取的，但我们没有数据库，为方便，可以用户输入流水号或者不输入流水号，来模拟有和没有流水号。
"""
import datetime


def generate_sales_order_number(employee_id, last_serial_number):
    # 生成当前日期
    current_date = datetime.date.today().strftime("%Y%m%d")

    # 生成序列号
    if last_serial_number:
        new_serial_number = str(int(last_serial_number) + 1).zfill(3)
    else:
        new_serial_number = "001"

    # 生成流水号
    sales_order_number = current_date + employee_id + new_serial_number
    return sales_order_number


# 模拟员工输入工号和员工数量
employee_id = input("请输入员工编号：")
employee_count = int(input("请输入员工数量："))

# 模拟从数据库读取上一次的流水号，若没有则默认为空
last_serial_number = input("请输入上一次的流水号（若无则直接回车）：")

# 生成销售单流水号
for i in range(1, employee_count + 1):
    current_employee_id = employee_id + str(i).zfill(3)
    sales_order_number = generate_sales_order_number(current_employee_id, last_serial_number)
    last_serial_number = sales_order_number[-3:]
    print("员工编号为", current_employee_id, "的销售单流水号为：", sales_order_number)