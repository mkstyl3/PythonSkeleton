MAKE PROJECT (Python)
=========================

Basics Steps
------------------

1.  Step 1) creating a virtual environment for the project

**see if the package is installed**

$ sudo apt search python3-venv

**if not installed, install package**

$ sudo apt install python3-venv

**now install module venv of python in your virtual environment directory**

$ python3 -m venv [directory_path]


2.  Step 2) enter into our virtual environment for config

$ source .pyvenv/bin/activate

**list package python into environment**

([directory_name])$ pip list

**update package python into environment**

([directory_name])$ pip install -U [package_1 package_2 ...]

**install serve gunicorn**

([directory_name])$ pip install gunicorn

**install framework "falcon" for application python api Rest**

([directory_name])$ pip install falcon

**exit our virtual environment**

([directory_name])$ deactivate


3.  Step 3) create file .sh for run server gunicorn

$ touch start.sh

**content basic for .sh file**

```
#!/bin/bash
source [directory_name]/bin/activate
exec [directory_name]/bin/gunicorn -w 3 -t 99999 -b '0.0.0.0:8082' [name_file.py:class]
```
