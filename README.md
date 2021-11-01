# AirBnB_clone

![Logo AirBnb](https://github.com/JuanSebastianGB/AirBnB_clone/blob/main/images/65f4a1dd9c51265f49d0.png?raw=true)

## Description :memo:

First step towards building a full web application.
This project is build to implement the essential, which is the back-en console.

![For description](https://github.com/JuanSebastianGB/AirBnB_clone/blob/main/images/815046647d23428a14ca.png?raw=true)
## Console :computer:

### Execution

The console works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```


## Tests :heavy_check_mark:

### 2. Unittests

All the files, classes, functions are tested with unit tests

```
python3 -m unittest discover tests
```



Unit tests also work in non-interactive mode:

```
echo "python3 -m unittest discover tests" | bash
```

  
## Authors :pen:

-   **Juan Sebastian Perea**  <[Juanse1595](https://github.com/Juanse1595)> | [@JuanSePeBe95](https://twitter.com/JuanSePeBe95)

-   **Juan Sebastian Gonzalez**  <[JuanSebastianGB](https://github.com/JuanSebastianGB)> | [@juancho1141](https://twitter.com/juancho1141)