unit = input('請輸入溫度單位(F/C): ')
value = input('請輸入溫度: ')
if str(unit) == 'F':
 	temp_c = (float(value) - 32)/ 1.8
 	print ('你的攝氏溫度為: ', temp_c)
if str(unit) == 'C':
 	temp_f = float(value) * (9/5) + 32
 	print ('你的華氏溫度為: ', temp_f)