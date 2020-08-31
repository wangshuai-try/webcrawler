# 1.背景
- 后台sku配置错误，导致H5渲染失败。

# 2.解决方案
1. 爬取所有渠道的appkey。因为渠道较多，人工校验成本较大，而且url请求参数为type，appkey，所以首先考虑的是通过爬取后台所有的渠道appkey来获取所有渠道信息。
2. 保存appkey和渠道名称。通过爬取到的appkey来请求数据，并筛选出大喜马，小喜马的sku信息。
3. sku信息校验。目前只校验了json格式是否正确，以及图片地址是否可以请求
4. [github](https://github.com/wangshuai-try/check_sku)
# 3.库
- 3.1 requests  
    - 一个第三方网络库，基于python自带的urllib库封装。
    - 可通过pip install requests安装
- 3.2 lxml  
    - python的一个解析库,支持HTML和XML的解析,支持XPath解析方式,而且解析效率非常高XPath,全称XML Path Language,即XML路径语言
    - 可通过pip install lxml安装
- 3.3 selenium
    - 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
    - 需要下载对应浏览器版本驱动,这里使用Chrome浏览器。[驱动下载地址点我](http://npm.taobao.org/mirrors/chromedriver/)
        - 浏览器驱动放置在python根目录下即可
    - 可通过pip install selenium安装
- 3.4 下载库速度慢解决
    - 可以设置下载地址为国内镜像源的方式来解决
    - file->settings->project interpreter->点击右方+号->manage repositories->点击下方+号
      添加以下镜像源
        - https://pypi.tuna.tsinghua.edu.cn/simple/
        - https://mirrors.ustc.edu.cn/pypi/web/simple/
        - https://mirrors.aliyun.com/pypi/simple/
      

