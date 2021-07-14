import json
import time
import requests
import logging

logging.basicConfig(level=logging.INFO)


def req_api(method, path, headers_param, **param):
    start_time = time.time()
    url = 'http://localhost:9701/service/v1/portal' + path
    try:
        resp = requests.request(method, url, json=param, headers=headers_param, timeout=30)
        resp.encoding = resp.apparent_encoding
        # 格式化json结果
        return json.dumps(resp.json(), indent=2, ensure_ascii=False)
    except Exception as e:
        logging.error("请求失败: %s", e)
        return "请求失败咯"
    finally:
        logging.info("请求地址:%s，请求耗时: %s", resp.url, time.time() - start_time)


headers = {'X-Tenant-Id': 'snpas', 'Content-Type': 'application/json', 'User-Agent': ''}
print(req_api('put', '/articles/top', headers, top=10,
              columnIds=('1409405513292070913', '1409405392911351809', '1409820342343450625', '1411959377681768449')))
