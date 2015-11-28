# Hostil Planet

Git repository :

http://github.com/JauriaStuios/HostilPlanet

Latest build :

http://jauriastudios.mooo.com/builds/HostilPlanet/


### Dependencies:

You might need to install this before running the game:
```
  Python 2.7:     http://www.python.org/
  PyGame 1.9:     http://www.pygame.org/
```

### Compile:

You might need to install this before compiling the game ( not required to play ):

```
  cx_freeze 4.3.3
```

And run on windows:

```
python setup.py build_msi
```

And on linux or mac:

```
python setup.py build
```


### Running the game:

On Windows or Mac OS X, locate the "run_game.pyw" file and double-click it.

Othewise open a terminal / console and "cd" to the game directory and run:

```

python run_game.pyw

-full : to run in window mode
-scale2x : use the scale2x scaler
-lowres : to run in 320x240
-tv : to do a silly scanline effect

level.tga : to play a certain level

```

### How to play:

Use your arrow keys to
move the robot.

Button 1 - Jump 
Button 2 - Shoot
            


### Misc:

press 'd' on the main menu to enter 'debug' mode and have a list of all
levels in the data/levels/ folder.  That way you can play in development
or totally broken / reject levels.

press F10 uring game for enable godmode


### License:

(c) 2015 Jauria Studios
(c) 2007 The Olde Battleaxe & Friends
