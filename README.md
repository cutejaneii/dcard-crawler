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
| mode | -m | 0 | 爬蟲模式<br> 0：爬最受歡迎文章<br>1：爬較新文章<br>2：爬較舊文章<br>3：依關鍵字爬文章 |
| count | -c | 10 | 抓取的文章數量 |
| get_responses | -r | 0 | 是否要取得回覆，0代表不取，1代表取 |
| keyword | -k | KFC | 關鍵字 |


詳見說明：
<pre><code>$ python dcard_main.py -h</code></pre>

### 取得最受歡迎的文章
取得最受歡迎的10筆文章(預設看板:trending)
<pre><code>$ python dcard_main.py</code></pre>

![image](https://github.com/cutejaneii/dcard-crawler/blob/master/images/mode0_A.png)

取得「美食版」最受歡迎的「5」筆文章
<pre><code>$ python dcard_main.py -f food -c 5</code></pre>

![image](https://github.com/cutejaneii/dcard-crawler/blob/master/images/mode0_B.png)

取得「手作版」最受歡迎的「2」筆文章及回覆
<pre><code>$ python dcard_main.py -f handicrafts -c 2 -r 1</code></pre>

![image](https://github.com/cutejaneii/dcard-crawler/blob/master/images/mode0_C.png)

### 取得較新的文章

取得「美食版」最新的「5」筆文章
<pre><code>$ python dcard_main.py -m 1 -f food -c 5</code></pre>

![image](https://github.com/cutejaneii/dcard-crawler/blob/master/images/mode1_A.png)

取得「美食版」大於文章id為「150000」的「5」筆文章
<pre><code>$ python dcard_main.py -m 1 -f food -c 5 -a 150000</code></pre>

![image](https://github.com/cutejaneii/dcard-crawler/blob/master/images/mode1_B.png)

### 取得較舊的文章

### 利用「關鍵字」取得文章

取得關鍵字為「小宇」的最新「5」筆文章
<pre><code>$ python dcard_main.py -m 3 -k 小宇 -c 5</code></pre>

