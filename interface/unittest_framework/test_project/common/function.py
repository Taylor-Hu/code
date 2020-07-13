# 主要是存储一些公共的方法
class Function:
    # 实现功能为：判断一个字符串能否被有效地转换为一个数字
    def check_number(self, number):
        is_valid = True
        is_correct = True
        point = 0
        minus = 0
        digit = 0

        for char in number:
            ascii = ord(char)
            if ascii < 45 or ascii == 47 or ascii > 57:
                is_valid = False
                break
            if ascii == 46:
                point += 1
            if ascii == 45:
                minus += 1
            if ascii >= 48 and ascii <= 57:
                digit += 1

        if is_valid and point <= 1 and minus <= 1 and digit >= 1:
        # if is_valid and point <= 1 and minus <= 1:
            if minus == 1 and ord(number[0]) != 45:
                is_correct = False
            else:
                is_correct = True
        else:
            is_correct = False

        return is_correct


    def check_number_2(self, number):
        is_correct = True
        point = 0
        minus = 0
        digit = 0

        for char in number:
            ascii = ord(char)
            if ascii < 45 or ascii == 47 or ascii > 57:
                raise Exception("Error-Number")
            if ascii == 46:
                point += 1
            if ascii == 45:
                minus += 1
            if ascii >= 48 and ascii <= 57:
                digit += 1

        if point <= 1 and minus <= 1 and digit >= 1:
            if minus == 1 and ord(number[0]) != 45:
                is_correct = False
            else:
                is_correct = True
        else:
            is_correct = False

        return is_correct


    # 原生代码计算x的y次方
    def power(self, x, y):
        try:
            x = float(x)
            y = int(y)
        except:
            # print("你的输入参数不正确")
            return 'Error'
            # raise Exception
        else:
            result = 1
            if y < 0:
                for i in range(-y):
                    result *= x
                result = 1 / result
            else:
                for i in range(y):
                    result *= x

            return result

    # 编写一个代码，创建一个文本文件，并写入一段内容，无返回值，请对其进行测试。
    def write_file(self, content, path):
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(content)


    # 自己简单实现一个断言
    def assertTrue(self, actual):
        if actual == True:
            print("测试成功")
        else:
            print("测试失败")


if __name__ == '__main__':
    func = Function()
    number = input("请输入一个数字：")
    print(func.check_number(number))