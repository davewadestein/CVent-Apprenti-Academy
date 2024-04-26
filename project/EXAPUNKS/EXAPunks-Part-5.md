# EXAPUNKS Part 5: Extras we might add...

### First, some instructions from the real EXAPUNKS game that we did not implement

* __`RAND LO(R/N) HI(R/N) R`__
   <br>Generate a random number between LO and HI and store it in the destination register.

* __`MAKE`__
   <br>Create a new file inside the EXA. (In part 4 we just used previously-created files, but now we can create our own.
You may have noticed that the __`FILE`__ command from part 4 wasn't really used. The idea is that first you do a __`MAKE`__
which creates a new file inside the EXA, then the __`FILE`__ command will tell you the file's ID–you can generate a unique ID
for each file that is created.)

### ...and some instructions I made up

* __`TSTART`___
<br>Start a timer to time a block of EXA code. You can do this by noting the current clock time using the __`time()`__ method
in the __`time`__ module. It will return a float which you can store. If the timer is already running, __`TSTART`__ instruction
constitutes an illegal instruction. Both of these cases can and should be tested.

* __`TSTOP`__
<br>Stop the timer and print out the elapsed time (current time - start time). A __`TSTOP`__ instruction which was not preceded 
by a __`TSTART`__ instruction constitutes an illegal instruction. Both of these cases can and should be tested.

* __`SLEEP R/N`__
<br>Suspend execution of code for the specified number of seconds. Use __`time.sleep()`__. This will be a difficult function
to test, as you'd have to check elapsed time. It's possible, but not required.

