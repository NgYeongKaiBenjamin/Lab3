import price_info

print("Price Info")

def test_total_cost_shopping():
    result=[]
    price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70}
    quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2}
    result = price_info.total_cost_shopping(price_list,quantity_list)
    assert(result==24.9)

def test_cost_of_fruits():
    result=[]
    result=price_info.cost_of_fruits("orange", 15)
    assert(result==21)

