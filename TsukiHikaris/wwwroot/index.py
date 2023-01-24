import KamitaTomoe.output as output
import KamitaTomoe.html as html
import KamitaTomoe.gain as gain
import KamitaTomoe.session as session
import os 
chdir()
os.chdir(session._root)
print(gain.post())
if(gain.posts('user') == 'shizhi' and gain.posts('password') == '123'):
    output.echo('''登陆成功''')
else:
    output.echo('''
    <html>
    <head>
        <style>
        body {
        background: linear-gradient(#e66465, #9198e5);
        font-family: Roboto;
        display: flex;
        align-items: center;
        justify-content: center;
        }
        .login {
            background-color: #0b132b;
            width: 400px;
            color: #f8f9fa;
            padding: 40px;
            box-shadow: 10px 10px 25px #000000;
            text-align: center;
        }

        .login input {
            display: block;
            margin: 20px auto;
            text-align: center;
            background: none;
            padding: 12px;
            font-size: 15px;
            border-radius: 22px;
            outline: none;
            color: #f8f9fa;
        }

        .login input[type="text"],
        .login input[type="password"] {
            border: 2px solid #3498db;
            width: 220px;
        }

        .login input[type="submit"] {
            width:150px;
            border: 2px solid #2ecc71;
            cursor: pointer;
        }

        .login input[type="text"]:focus,
        .login input[type="password"]:focus {
            border-color: #2ecc71;
            width: 250px;
            translate: 0.5s;
        }

        .login input[type="submit"]:hover {
            background-color: #2ecc71;
            translate: 0.5s;
        }

        </style>
    </head>

    <body>
        <form action="index.py" class="login" method="POST">
            <h1>login登录</h1>
            <input name="user" type="text" placeholder="请输入用户名" />
            <input name="password" type="password" placeholder="请输入密码" />
            <input type="submit" value="submit提交" />
        </form>

    </body>

    </html>
    ''')
