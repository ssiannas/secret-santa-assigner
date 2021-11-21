# Secret Santa client-server

This is a very basic client-server setup that enables groups of friend to do a Secret Santa assignment over the internet.


## How to run

**On the host machine**, configure the port and participant number in the `src/config.py` file and run the `server.py` file which will initalize the server as such:

```
python server.py
```

or you can pass the initialization arguments directly to the script as such

```
python server.py [-p --port PORT] [-n --number PARTICIPANT_NUMBER]
```



**On the client machine**, also configure the proper ip and port and run the `client.py` file as such:

```
python client.py
```

or you can pass the initialization arguments directly to the script again:

```
python client.py [-p --port PORT] [-ip --addr HOST_ADDRESS]
```


The arguments are optionals and default to the ones contained in the `src/config.py` file

There are no requirements further than a basic python3.x installation
