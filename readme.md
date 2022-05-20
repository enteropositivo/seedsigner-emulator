# SeedSigner Emulator
> Allows to execute [SeedSigner](https://github.com/SeedSigner) air-gapped hardware wallet in your desktop.

![](img/demo.gif)


> newly created repository please give me some time to review everything and prove that anyone can use it easily


## How it works
New display driver that replaces SeedSigner ST7789 1.3 display driver, making possible to show how the device works in a desktop enviroment.

I have tried to make it as non-invasive as possible so that the emulator can be used with other versions of Seedsigner with as little effort as possible.

## Usage from source

First clone [SeedSigner](https://github.com/SeedSigner/seedsigner) repo

```sh
git clone https://github.com/SeedSigner/seedsigner.git
```

Go to directory _seedsigner/src_ and clone or copy the contents of this repository and mix with the existing SeedSigner content.  

Install these requeriments:

```sh
pip3 install --upgrade pip
pip3 install setuptools
pip3 install embit
python3 -m pip install --upgrade Pillow
pip3 install dataclasses
pip3 install pyzbar
sudo apt install libzbar0
pip3 install git+https://github.com/jreesun/urtypes.git@e0d0db277ec2339650343eaf7b220fffb9233241
pip3 install qrcode
pip3 install tk
sudo apt-get install python3-tk
```

Run the emulator
```sh
python3 main.py
```

## Alpha release !!

This is the first release and there are still many things to be solved.  The webcam is not deployed and the screensaver is not working properly.

**so be patient because I will be solving everything**


## Make a standalone executable

You can make an executable using PYinstaller

```sh
pip install pyinstaller
```
go to your proyect main forlder where _main.py_ stands and execute

```sh
pyinstaller --clean --add-data seedsigner\\resources;seedsigner\\resources main.py
```

Perhaps you'll need to lace next to the executable the follwing libraries
- libiconv
- libzbar

I'll upload releases for linux and windows


## Contact

Follow my Twitter – [@EnteroPositivo](https://twitter.com/enteropositivo)  




