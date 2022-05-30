```
                                                __________  ____ ________________
                                               / ____/ __ \/ __ \__  / ___/_  __/
                                              / /_  / / / / /_/ //_ <\__ \ / /
                                             / __/ / /_/ / _, _/__/ /__/ // /
                                            /_/    \____/_/ |_/____/____//_/

```
F0R3ST - the fast port-scanner on Python(on SYN connections).

The script was developed as a console utility, written for Python 3.7 (not sure if it will work on lower versions).

```
```
Steps to help you get everything up and running correctly:

1)All libraries are standard and must be present in your version of the interpreter.

2)Since connections are organized through a socket, this error may occur:
```
Exception in thread Thread-***:
Traceback (most recent call last):
  File "/usr/lib/python3.7/threading.py", line 917, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.7/threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
  File "./f0r3st.py", line 127, in f0r3st
    sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  File "/usr/lib/python3.7/socket.py", line 151, in __init__
    _socket.socket.__init__(self, family, type, proto, fileno)
OSError: [Errno 24] Too many open files
```
There is nothing wrong with it, you just did not have enough file descriptors (in most Unix systems their limit is 1024). You just need to increase the limit:
```
$ ulimit -n 2000
```
If that doesn't help, increase it some more.

3)You can run the script either with the interpreter itself, or just give bash a chance:
```
$ chmod +x f0r3st.py
$ ./f0r3st.py --option
```
or
```
$ python3 f0r3st.py --option
```


Let's look at the `MANUAL`:
```
$ python3 f0r3st.py -help

Use: python3 f0r3st.py -host [ip/domain]
Additional flags:
-port [80|80-443]— specify port range for scan, by default 1-10000
-v - more interesting information, for example OS

```
Here it is simple, the key 
```
-host
```
points to the target, you can specify either an IP address or a domain.

Now go to 
```
-port
```
by default all ports from 1 to 10000 will be scanned (this is done for speed, because many services run on these ports), the key above will help you change this value to whatever you want, you can specify a single port.
The very last 
```
-v
```
key will show you the host system (at least nmap will try to detect it). It is up to you if you don't want to use it. If you are going to use it - install Nmap.

Typical program output:
```
$ python3 f0r3st.py -host google.com


                     ░▒▓█ f 0 r 3 s t █▒▓░

Nice! Host is active!
Go to scan!
******************************
80 port open it's http
443 port open it's HTTPS
******************************
Total time: 6sec

                i wish you good finds! goodbye...
                
```
```
```
Use it wisely. I hope it comes in handy)
