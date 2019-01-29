# dcard-crawler

本專案利用[requests](https://github.com/requests/requests)呼叫DCARD API取得文章

## 安裝方法
<pre><code>$ git clone https://github.com/cutejaneii/dcard-crawler.git</code></pre>
## 使用方法
參數說明：

| 參數 | 縮寫 | 預設值 | 說明 | 
| ------ | ------ | ------ | ------ |
| forum | -f | trending | 看板名稱 |
| article_id | -a | 1 | 文章ID |
| mode | -m | 0 | 爬蟲模式，0代表最受歡迎文章，1代表較新文章， |
| count | -c | 10 | 抓取的文章數量 |
| get_responses | -r | 0 | 是否要取得回覆，0代表不取，1代表取 |
| keyword | -k | KFC | 關鍵字 |


詳見說明：
<pre><code>python dcard_main.py -h</code></pre>

### 取得最受歡迎的文章

### 取得較新的文章

### 取得較舊的文章

### 利用「關鍵字」取得文章

<pre><code>python dcard_main.py -m 3 -k 張學友</code></pre>

