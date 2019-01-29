# dcard-crawler

本專案利用[requests](https://github.com/requests/requests)呼叫DCARD API取得文章

## 安裝方法
<pre><code>$ git clone https://github.com/cutejaneii/dcard-crawler.git</code></pre>
## 使用方法
參數說明：

| Plugin | README |
| ------ | ------ |

| 參數 | 縮寫 | 預設值 | 說明 | 
| ------ | ------ | ------ | ------ |
| forum | -f | trending | |
| article_id | | |
| mode | | |
| count | | |
| get_responses | | |
| keyword | | |


詳見說明：
<pre><code>python dcard_main.py -h</code></pre>

### 取得最受歡迎的文章

### 取得較新的文章

### 取得較舊的文章

### 利用「關鍵字」取得文章

<pre><code>python dcard_main.py -m 3 -k 張學友</code></pre>

