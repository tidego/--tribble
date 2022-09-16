def main():
    x_1 = x_2 = x_3 = eval(input())
    for i in range(100):
        x_1 = 3.9 * x_1 * (1 - x_1)
        x_2 = 3.9 * (x_2 - x_2 * x_2)
        x_3 = 3.9 * x_3 - 3.9 * x_3 * x_3
        #  a = 3.9*a*(1-a) = 3.9*(a-a*a) = 3.9*a-3.9*a*a
        print('第一', x_1)
        print('第二', x_2)
        print('第三', x_3)


main()