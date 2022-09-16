def main():
    print('混沌程序启动')
    print('请输入一个0-1的数字')
    x = eval(input())
    for i in range(100):
        x = 3.9 * x * (1 - x)
        print(x)
    main()
print(main())