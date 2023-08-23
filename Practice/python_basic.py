# 邏輯運算子: and, or, not
# 位元運算子: &, |, ~, ^, >>, <<

print('1-邏輯運算子')
print('1.1. ',5<3 and 6<10) #False
print('1.2. ',4<7 and 8<7 and 3>0) #False
print('1.3. ',4<5 or 9>12) #True
print('1.4. ','a'=='a' or 7==2 and 8<5) #True
print('1.5. ',not 2**3 < 10) #False

print('1.6. ',5!=7 and 6<0 and 8==8) #False
print('1.7. ','cat' and 'pig') #and會回傳最後一個運算元 >> pig
print('1.8. ','cat' or 'pig') #or會回傳遞一個True的運算元 >> cat
print('1.9. ','' or 'pig') #pig


# 在Python中，把0, 空字串, None 都視為False
print('2-bool')
print('2.6. ',bool('cat')) #因為cat不是空的字串 >> True
print('2.7. ',not 'cat') #False
print('2.8. ',bool()) #False
print('2.9. ',bool(3.14)) #因不是0也不是空字串也不是None >> True 
print('2.10. ',bool(0.000)) #浮點數0.000也看成是0 >> False
print('2.11. ',bool(0.00001)) #True

#Python 的整數沒有限制, 端看你電腦的記憶體有多大, 因此雖然 Python 的整數是採用 2 的補數來表示, 
#但是要想像左邊有無限多個[正負號位元], 不過實際上要進行位元運算, 我們只要在左側多擺一個正負號位元即可
#正負號位元是 1, 表示是負數，所以只要減 1 後再做一次反向運算, 就可以得到該數的絕對值了
#https://dev.to/codemee/python-de-wei-yuan-yun-suan-5bgb
print('3-位元運算子')
print('AND運算')
print(f'0 AND 0 {0 & 0:5d}')
print(f'0 AND 1 {0 & 1:5d}')
print(f'1 AND 0 {1 & 0:5d}')
print(f'1 AND 1 {1 & 1:5d}')

print('\nOR運算：')
print('0 OR 0 {:6d}'.format(0 | 0))
print('0 OR 1 {:6d}'.format(0 | 1))
print('1 OR 0 {:6d}'.format(1 | 0))
print('1 OR 1 {:6d}'.format(1 | 1))

print('\nXOR運算：')
print('0 XOR 0 {:5d}'.format(0 ^ 0))
print('0 XOR 1 {:5d}'.format(0 ^ 1))
print('1 XOR 0 {:5d}'.format(1 ^ 0))
print('1 XOR 1 {:5d}'.format(1 ^ 1))

x, y = 9, 14
print(f'x = {x:<2}, bin(x) = {bin(x):<10}') #x = 9 , bin(x) = 0b1001 使用位元運算需思考 01001
print(f'y = {y:<2}, bin(y) = {bin(y):<10}') #y = 14, bin(y) = 0b1110 使用位元運算需思考 01110

print('\n3.1. ', x and y) #比較與邏輯運算子 #14
print('3.2. ', x & y) #[AND] 位元運算子，結果為8(以位元表示為01000=1000)
print('3.3. ', x | y) #[OR] 結果為15(以位元表示為01111=1111)
print('3.4. ', x ^ y) #[XOR] 結果為7(以位元表示為00111=0111=111)

print('3.5. ', ~x) #[NOT] 結果-10(以位元表示為10110，減1為10101，再反向為01010，最後等於1010，但視為負數)
#在PYTHON裡，~x = -(x+1)
print(f'-10的位元表示(bin(-10))={bin(-10)}') #-0b1010

print('3.6. ', x << 2) #結果為36(將位元往左移兩位，1001變成100100)
print('3.7. ', x >> 2) #結果為2(將位元往右移兩位，原來沒有的位自動填0，超出範圍的位捨棄掉，1001變成0010)
print(bin(36))
print(bin(2))
