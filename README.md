


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