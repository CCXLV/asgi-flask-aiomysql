# Flask ASGI & Async MySQL connection
using async flask, hypercorn and aiomysql

## How to set up
```cmd
pip3 install -r requirements.txt
```
rename the file `secrets.env.example` to `secrets.env` and put your mysql url like the following
`mysql+aiomysql://user:password@localhost:3306/db_name`

after that create the table in the db
```cmd
flask init_db
```

and finally run the app
```cmd
hypercorn -b 127.0.0.1:5000 asgi:flask_app
```
