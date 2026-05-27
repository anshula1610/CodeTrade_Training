#a function is defined for calculating the total bill and the tip of a particular percentage of tip and the amount of bill
# print only displays output and is not stored
# return is used in functions that sends back the answer from the functiona and it can be stored

def calculate_tip(bill,tip_percent):
    tip_amount=(bill*tip_percent)/100
    total_bill=bill+tip_amount
    return {
        "tip":tip_amount,
        "total":total_bill
    }

result1 = calculate_tip(500,10)
print(f"Bill: 500, Tip:{result1['tip']}, Total_Bill:{result1['total']}")

result2 = calculate_tip(1500,20)
print(f"Bill: 1500, Tip:{result2['tip']}, Total_Bill:{result2['total']}")

result3 = calculate_tip(2500,30)
print(f"Bill: 2500, Tip:{result3['tip']}, Total_Bill:{result3['total']}")