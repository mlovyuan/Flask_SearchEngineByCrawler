# Flask_SearchEngineByCrawler

### 簡單做一個搜尋引擎

假如要使用Google的搜尋引擎，一般會想到利用Google提供的API，將欲搜尋的資料藉由API的管道傳入Google的Server，再由它反向傳回搜尋結果顯示在自己的前端頁面上。

除此之外，也有人給出一個方法：藉由爬蟲將搜尋結果呈現在畫面上。如同「披著羊皮的狼」，移花接木般的將Google搜尋的初始畫面改為自己的設計。
<br>
<br>
#### 當使用爬蟲，Server端阻攔時？
雖然說Python提供的爬蟲套件非常方便，但某些Server會在識別出訪問者並非是經由正常通道使用時，拒絕回覆相關資料。

Python的requests套件便有提供解決辦法：使用F12 > Network，將自己瀏覽器傳送的
header複製下來，存入`requests.get()`的第二個參數，讓Server端認為該爬蟲是瀏覽器，從而獲取需要的資料內容。


---
`flask.request.args`用於`GET`請求時來獲取資料。
