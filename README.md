


```bash
fastapi dev fast_zero/app.py -- host 0.0.0.0
```
```python
>>> import socket
>>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> s.connect(("8.8.8.8", 80))
>>> s.getsockname()[0]
'192.168.0.100'
```


## Lição de casa

* https://www.youtube.com/watch?v=t4C1c62Z4Ag&ab_channel=EduardoMendes

* https://www.youtube.com/watch?v=yQtqkq9UkDA&ab_channel=EduardoMendes



## Migrations

```
# criar migration
alembic revision --autogenerate -m "create users table"
# executa a migration
alembic upgrade head
```
