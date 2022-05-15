
'''
practice:

下載 xkcd 前十張圖片 (0~9)，檔名格式為 <編號>-<檔案名稱>
    example: 614-woodpecker.png
'''

import requests
from pathlib import Path
Path("./images").mkdir(parents=True, exist_ok=True)


for i in range(10):
    url = f'https://xkcd.com/{i}/info.0.json'
    res = requests.get(url)
    if res.ok:
        res_json = res.json()
        img_url = res_json['img']

        img_name = img_url.split('/')[-1]
        with open(Path(f"./images/{i}-{img_name}"), "wb") as f:
            img_res = requests.get(img_url)
            f.write(img_res.content)


'''
Hint

















1. res.ok
2. 用 split 取得檔名
'''
