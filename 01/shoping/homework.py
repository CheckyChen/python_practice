# author:checky

goods_dict = {
    "001": {"name": "爱马仕腰带", "price": 1999},
    "002": {"name": "劳力士男表", "price": 19999},
    "003": {"name": "巴宝莉眼镜", "price": 4999},
    "004": {"name": "路虎发现四", "price": 99999}
}

# 打印商品列表
def print_goods(goods_dict):
    print("---------欢迎购物，商品列表：---------")
    print("商品编号\t\t名称\t\t\t\t价格")
    for key,value in goods_dict.items():
        print(key,'\t\t',value["name"],'\t\t',value["price"])


# 获取一个商品，并返回
def get_one_goods(id,goods_dict):
    tmp_dict = {}
    res = goods_dict.get(id,None)
    if res is None:
        return None
    tmp_dict[id] = res
    return tmp_dict


# 判断商品数量的合法性
def check_goods_count(number):
    try:
        number = int(number)
    except BaseException as ex:
        print("商品数量必须为数字！")
        return False

    if type(number) is int:
        tmp_number = int(number)
        if tmp_number <= 0:
            print("商品数量必须大于0！")
            return False
        return True

def check_money(number):
    try:
        number = int(number)
    except BaseException as ex:
        print("金额必须为数字！")
        return False
    if type(number) is int:
        tmp_number = int(number)
        if tmp_number <= 0:
            print("金额必须大于0！")
            return False
        return True

buy_car = []

# 打印购物车
def print_buy_car(buy_car):
    if len(buy_car)>0:
        total_price = 0
        print("购物车：")
        for item in buy_car:
            name = item["name"]
            price = float(item["price"])
            count = item["count"]
            total_price += price*count
            print(name,"X",count,"金额：",price*count)
        return total_price
    else:
        return None

# 结账
def pay_money(total_money):
    while True:
        pay = input("请输入支付的金额：")
        if check_money(pay):
            pay = float(pay)
            if pay < total_money:
                print("支付金额必须大于总金额！")
                continue
            elif pay > total_money:
                print("支付成功，找您%f"%(pay-total_money))
                break
            else:
                print("支付成功！")
                break



if __name__ == '__main__':

    while True:
        choice_goods = {}
        print_goods(goods_dict)
        choice = input("请选择商品(输入'q'退出！)：")
        if choice == "q" or choice == "Q":
            total_money = print_buy_car(buy_car)
            if total_money:
                pay_money(total_money)
            print("---------欢迎下次光临！---------")
            break
        else:
            goods = get_one_goods(choice, goods_dict)
            if goods:
                count = input("请输入商品的数量：")
                flag = check_goods_count(count)
                if flag:
                    choice_goods["name"] = goods[choice]["name"]
                    choice_goods["price"] = goods[choice]["price"]
                    choice_goods["count"] = int(count)
                    buy_car.append(choice_goods)
                    continue
            else:
                print("没有找到商品！")
                continue