# qicc_demo

一份简单的工商信息查询代码

数据源--企查查

两个文件分别用以单次查询和批量查询

单次查询会把所有关联公司的需要工商信息都打印在控制台中

批量查询需要通过文本，把公司名逐行写在文本中，运行时需要文本目录和qicc.py文件在同一目录，唯一参数为文件名。爬取公司信息时选取企查查第一个检索公司的信息
并把获取的信息以out_输入文件名的方式输出到新文本中

注意：企查查对非登录账号有检索次数限制，批量数据过多时容易被拦截
相关方法：
  1：使用代理，通过不同ip访问。
  2：注册个企查查账号，登录后把cookie中的sessionid拷贝到head里，可以模拟登录访问
  
个人代码中只取用了几个有限的工商信息，纯属偶尔所写，有需要可以针对企查查页面数据添加相关字段
