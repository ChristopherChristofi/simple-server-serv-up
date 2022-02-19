# simple-server-serv-up

## Description:
If you want to play around with some basic web development practice with something like React, then here is a simple HTTP server implementation to help set you up - without all the hefty install this, sign up here, backend configuration.

## Requirements:

- Python 3+

## Quickstart:

Run in the command-line:

```sh
python3 serv.py
```

then open (default) 127.0.0.1:8000/

- redirects to default path 'index.html'

or define your own port location and IP identifier:

```sh
python3 serv.py --host 192.0.2.0 --port 1000
```

serving 192.0.2.0:1000/

## Help:

- Host option: --host / -h
- Port option: --port / -p

For help information run in the command-line:

```sh
python3 serv.py -i
```
