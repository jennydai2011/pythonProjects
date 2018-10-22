

3 steps
1. send request and get response
2. parse response
3. find next url 

options to send request and get response
1. urllib, urllib.request  -- python built-in, no need to install, need to handle encode
2. request -- need to install,
3. selenium -- simulate browser to send request
4. phantomjs  -- headless browser
5. scrapy - framwork to send request

options to parse response
1. re  -- regular expression, only can handle simple requirements
2. BeautifulSoup  -- object, 
3. lxml -- xpath
4. pyquery -- similar to jquery to select/locate in html
5. scrapy -- framework to parse reponse ( selector)

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
