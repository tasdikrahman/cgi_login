## CGI-Login

So this is a Simple user Login system implemented using `CGIHTTPServer` with `sqlite3` as the db.

`reg_no`, `username`, `password` are entered by the user and queried to `sqlite3` to check whether the user with the particular `reg_no` exists or not in the `user_base.db`

If the user exits, redirect the `index.html` to a page which displays the particular users details like `username` and `reg_no` upon successful login.

If the user does not exist. Ask him, if he wants to create an account,if yes update the db accordingly

##Usage

![Usage](https://raw.githubusercontent.com/prodicus/cgi_login/master/cgi_login_demo.gif)

## File structure. 

Do a 

```bash

$ git clone https://github.com/prodicus/cgi_login.git
$ cd cgi_login
~/cgi_login $ tree
.
├── cgi-bin
│   ├── create_db.py
│   └── user_check.py
├── cgi_login_demo.gif
├── index.html
└── README.md

1 directory, 5 files
```

Next step would be to create the initial `db` file.

```bash
~/cgi_login/cgi-bin $ ./create_db.py
Creating the database
table created
default users created 

displaying them
[(1081310234, 'foo', 'admin123'), (1081310251, 'admin', 'admin')]
~/cgi_login/cgi-bin $ 
```

So we start with two default users, namely `foo` and `admin`.


**Note :**

The `cgi` scripts should reside in `cgi-bin` or `htdocs` folder otherwise they wont be executed. Remember to make the scripts executable. Now the `user_base.db` file should also have read and write operations for the other users too as `SQLite3` needs those permissions to create a lock on the db file. So inside the `cgi-bin` directory, do a 

`~/cgi_login $ chmod 755 *`


## Running `CGIHTTPServer` 

Now you can use a full blown server software like `apache2` or `nginx` for trying this out. But for this example, I have done it using `CGIHTTPServer` provided by default with the `python` distribution.


```bash
$~/cgi_login $ python -m CGIHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Now go to your browser and type the url [http://localhost:8000/](http://localhost:8000/) and it would serve you `index.html`.

##License

MIT License [http://prodicus.mit-license.org/](http://prodicus.mit-license.org/) &copy; Tasdik Rahman
