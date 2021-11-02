# AirBnB_clone

![Logo AirBnb](https://github.com/JuanSebastianGB/AirBnB_clone/blob/main/images/65f4a1dd9c51265f49d0.png?raw=true)

## Main Resources provided by Holberton

-   [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw "cmd module")
-   [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g "uuid module")
-   [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q "datetime")
-   [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g "unittest module")
-   [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg "args/kwargs")
-   [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A "Python test cheatsheet")
## Description :memo:

First step towards building a full web application.
This project is build to implement the essential, which is the back-en console.

![For description](https://github.com/JuanSebastianGB/AirBnB_clone/blob/main/images/815046647d23428a14ca.png?raw=true)

## Modules :file_folder:

| Classes | Attributes | Metods
|--|--|--
| **BaseModel** | `created_at`<br> `updated_at` | `save`<br>`to_dict`
| **FileStorage** |  | `all`<br>`new`<br>`save`<br>`reload`
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
## Database - storage :package:  

First abstracted storage engine of the project: File storage.

Every time is launched the program, this restores all objects created before. Storing them into a file named 'file.json'.

-   Python doesn’t know how to convert a string to a dictionary (easily)
-   It’s not human readable
-   Using this file with another program in Python or other language will be hard.

So, because of that are converted the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

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