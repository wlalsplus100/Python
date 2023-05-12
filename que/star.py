while(1):
    op = input("수행할 연산을 입력하세요\n1.덧셈\n2.뻴셈\n3.곱셈\n4.나눗셈\n5.종료 : ")
    if op == '5':
        print('프로그램을 종료합니다')
        break
    if op == '1':
        a = input("첫 번째 수를 입력하세요 : ")
        b = input("두 번째 수를 입력하세요 : ")
        print(a + b)
    elif op == '2':
        a = input("첫 번째 수를 입력하세요 : ")
        b = input("두 번째 수를 입력하세요 : ")
        print(a - b)
    elif op == '3':
        a = input("첫 번째 수를 입력하세요 : ")
        b = input("두 번째 수를 입력하세요 : ")
        print(a * b)
    elif op == '4':
        a = input("첫 번째 수를 입력하세요 : ")
        b = input("두 번째 수를 입력하세요 : ")
        print(a / b)