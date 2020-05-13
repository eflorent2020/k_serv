# K_SRV

## specs 

see: https://gist.github.com/emmanuel-florent/16fdecf3d6b72125397cf0dbbc415c36

## depencies

```
apt-get install git make python3
```

## development
### Unix
```
make install
make pytest
make run
```

### Windows
```
make -f MakeFile.win install
make -f MakeFile.win pytest
make -f MakeFile.win run
```


## References

- https://flask.palletsprojects.com/en/1.1.x/#user-s-guide
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://flask.palletsprojects.com/en/1.1.x/testing/#testing-json-apis