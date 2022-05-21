# SeedSigner Emulator
> Allows to execute [SeedSigner](https://github.com/SeedSigner) air-gapped hardware wallet in your desktop.

![](img/demo.gif)


## How it works
New display driver that replaces the existing SeedSigner ST7789 1.3 driver, making possible to execute the device in a desktop enviroment.

I have tried to make it as non-invasive as possible so that the emulator can be used with other versions of Seedsigner with as little effort as possible.

You only have to merge the **seedsigner** from this repository with the seedsigner folder under [SeedSigner](https://github.com/SeedSigner/seedsigner) repository

![](img/tree_content.png)


## Usage from source

1- First clone [SeedSigner](https://github.com/SeedSigner/seedsigner) repo

```sh
git clone https://github.com/SeedSigner/seedsigner.git
```

2- Go to directory _seedsigner/src_

```sh
cd seedsigner/src
```

3- Download the contents of this respository [Seedsigner emulator (.zip)](https://github.com/enteropositivo/seedsigner-emulator/archive/refs/heads/master.zip), and merge the contents of the folder **seedsigner** with the existing **seedsigner** content.  

4- Install the following requeriments:

```sh
pip3 install embit
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade setuptools
pip3 install dataclasses
pip3 install pyzbar
pip3 install 
sudo apt install libzbar0
pip3 install git+https://github.com/jreesun/urtypes.git@e0d0db277ec2339650343eaf7b220fffb9233241
pip3 install qrcode **
sudo apt-get install python3-tk
pip3 install tk
```

Run the emulator
```sh
python3 main.py
```

## Make a standalone executable

You'll need to install PYinstaller to be able to generate an executable.

```sh
pip install pyinstaller
```
go to your proyect main forlder where _main.py_ stands and execute the following command

```sh
pyinstaller --clean --add-data seedsigner\\resources;seedsigner\\resources main.py
```

I'll upload releases for linux and windows


## Pending Tasks

- [ ] Fix screen saver
- [ ] Allow desktop webcam



## Alpha release !!

This is the first release and there are still many things to be solved.  The webcam is not deployed and the screensaver is not working properly.

**so be patient because I will be solving everything**


## Contact

Follow me at Twitter – [@EnteroPositivo](https://twitter.com/enteropositivo)  



