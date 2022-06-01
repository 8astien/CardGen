# CardGen

Python Project - made with Python 3.10, tkinter and Pillow 

This software generate cards for a custom RPG game 

In order to launch the software, you need to install dependencies in their Python 3.10 version : 

```
sudo apt install python3.10-tk
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
sudo apt install python3.10-distutils
python3.10 -m pip install --upgrade Pillow
```

Then run it : 

```
python3.10 interface.py
```

Once every field is filled, you can import an image for your card. 

A pop-up window will confirm the successfull generation of your card.

Generated cards are placed in the Cards folder at the root of the project. 
