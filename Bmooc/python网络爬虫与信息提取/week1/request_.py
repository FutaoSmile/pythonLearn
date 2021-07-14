# 导入库
import requests
import logging

logging.basicConfig(level=logging.INFO)


def demo():
    response = requests.get('https://baidu.com')  # 发送get请求
    print(response.status_code)  # 响应状态码
    print(response.encoding)  # 编码- 从响应头推测，如果响应有不包含charset则默认为ISO-8859-1
    print(response.text)  # 响应的文本
    print(response.apparent_encoding)  # 编码，从响应体推测
    response.encoding = response.apparent_encoding  # 设置返回值编码
    print(response.text)  # 响应的文本
    print(response.content)  # 响应的二进制
    print(type(response))  # 输出类型
    print(response.headers)  # 响应头
    response.raise_for_status()  # 如果状态码不是200 则抛出异常

    print(requests.get('https://api.github.com/user').text)


def getHtmlText(url, param, body):
    """
    爬取网页的通用代码
    :param param: 请求参数 url后面
    :param body: 请求体
    :param **kv: 请求参数，键值对
    :param url: 请求的URL
    :return: 网页文本
    """
    try:
        resp = requests.get(url, params=param, data=body)
        logging.info("request url: %s", resp.url)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except Exception as e:
        logging.error("请求失败: %s", e)
        raise Exception("请求失败")


req_param = {'account': '123', 'pwd': '123'}
print(getHtmlText("https://baidu.com", req_param, req_param))
