

1. basic
    url.open
    re compile
    
2. urllib + beautifulsoup   
   beautiful soup is better than re in html parse
   urllib is a native module
   pro:  object vs string parsing
   
3. request + beautifulsoup
   request is better than urllib
   pros: support encoded parameter; has GET/POST/PUT/DELETE; multi-part
   Requests is the new defacto way to do things
   
4. requests+Xpath
   Xpath is better than beaultifulsoup in html parsing
   
5. request + scrapy
   easy to build request
   easy to parse response using selector
 
 
 store data
 PyMongo + MongoDB
 
 distributed scraping
 Scrapy + MongoDB + Redis(task queue)


[用Python写爬虫，用什么方式、框架比较好？](https://www.zhihu.com/question/19899608)
[开源爬虫框架对比](https://zhuanlan.zhihu.com/p/40650078)
[Python爬虫进阶一之爬虫框架概述](https://cuiqingcai.com/2433.html)
