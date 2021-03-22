i=0
j=2
while True:
    password = input('請輸入密碼:')
    if password == ('a123456'):
        print('登入成功!')
        break
    elif i<2:
        print('密碼錯誤! 還有', j, '次機會')
        j=j-1
        i=i+1
    else:
        print('登入失敗')
        break