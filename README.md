# thueat-testing-post

For testing POST API calls using Heroku

Base URL: https://thueat-testing-post.herokuapp.com/

#使用方法：

1.修改app.py,自行添加route即可（里面有例子），返回数据自己随便定就可以了

2.修改后直接push去main，然后新的heroku app 会自动deploy，稍等片刻即可使用

注意：由于heroku app在30分钟无使用的状态下会sleep，所以使用之前先自行在浏览器浏览 base URL 以唤醒heroku app
