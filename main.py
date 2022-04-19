
money = int (input("Введите сумму вклада:"))
per_cent = {"TKB":5.6,"SKB":5.9,"VTB":4.28,"SBER":4.0}
TKB = float(per_cent["TKB"])*(money/100)
SKB = float(per_cent["SKB"])*(money/100)
VTB = float(per_cent["VTB"])*(money/100)
SBER = float(per_cent["SBER"])*(money/100)
deposit = {"TKB":TKB,"SKB":SKB,"VTB":VTB,"SBER":SBER}
print (deposit)
max_val = max(deposit.values())
print("Максимальная сумма, которую вы можете заработать:", max_val)
