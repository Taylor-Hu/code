# 求列表的平均值
def average(list):
    sum = 0
    for num in list:
        sum += num

    avg = sum / len(list)
    return round(avg, 2)

# 求最小最大值
def min_max(list):
    list.sort()
    min = list[0]
    max = list[len(list)-1]
    return min, max

# 90%的值：90%的值位于某个值之内，再根据平均值，两者做比较，可以估算数据的波动幅度，或使用标准差来计算波动
def percent(list, ratio):
    list.sort()
    index = int(len(list) * ratio / 100)
    return list[index-1]


# list = [42, 27, 51, 71, 42, 14, 21, 24, 40, 60, 34, 27, 42, 68, 92, 16, 10]
# list.sort()
# print(list)
# print(average(list))
# print(percent(list, 90))


# 利用装饰器统计和保存性能测试数据
import time, psutil, re, os

rt_list = []
cpu_list = []

# def monitor(func):
#     def inner(*args):
#         start_time = int(time.time() * 1000)
#         func(*args)
#         end_time = int(time.time() * 1000)
#         print('请求：%s 的响应时间为：%d 毫秒' % (func.__name__, end_time-start_time))
#         global rt_list
#         rt_list.append(end_time-start_time)
#
#         cpu = psutil.cpu_percent()
#         global cpu_list
#         cpu_list.append(cpu)
#
#     return inner


# 将post请求正文的key=value&key=value&key=value转换为字典
def post_2_dict(post):
    dict = {}
    list = post.split('&')
    for item in list:
        key = item.split('=')[0]
        value = item.split('=')[1]
        dict[key] = value
    return dict


# 下载页面资源文件
def download(session, response):
    list = []
    list += re.findall('href="(.+?)"/>', response)
    list += re.findall('src="(.+?)"', response)
    list += re.findall("url\('(.+?)'\)", response)

    # 读取download目录下的所有资源文件
    down_list = os.listdir('./download')

    for item in list:
        if not item.replace('/', '_') in down_list:
            if item.startswith('/'):
                url = 'http://192.168.80.128' + item
            elif item.startswith('http'):
                url = item
            else:
                url = 'http://192.168.80.128/phpwind/' + item

            resp = session.get(url)

            # temp = item.split('/')
            # filename = temp[len(temp)-1]
            # print(filename)

            filename = item.replace('/', '_')
            with open('./download/' + filename, 'wb') as file:
                file.write(resp.content)


# 利用三层闭包，解决装饰器本身传递参数的问题
def monitor(name, iteration, sleep):
    def wrapper(func):
        def inner(*args):
            for i in range(iteration):
                start_time = int(time.time() * 1000)
                func(*args)
                # time.sleep(sleep)
                end_time = int(time.time() * 1000)
                time.sleep(sleep)
                # print('请求：%s 的响应时间为：%d 毫秒' % (func.__name__, end_time-start_time))
                print('请求：%s 的响应时间为：%d 毫秒' % (name, end_time-start_time))
                global rt_list
                rt_list.append(end_time-start_time)

                cpu = psutil.cpu_percent()
                global cpu_list
                cpu_list.append(cpu)

        return inner
    return wrapper
