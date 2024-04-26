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

* __`TSTART`__
<br>Start a timer to time a block of EXA code. You can do this by noting the current clock time using the __`time()`__ method
in the __`time`__ module. It will return a float which you can store. If the timer is already running, __`TSTART`__ instruction
constitutes an illegal instruction. Both of these cases can and should be tested.

* __`TSTOP`__
<br>Stop the timer and print out the elapsed time (current time - start time). A __`TSTOP`__ instruction which was not preceded 
by a __`TSTART`__ instruction constitutes an illegal instruction. Both of these cases can and should be tested.

* __`SLEEP R/N`__
<br>Suspend execution of code for the specified number of seconds. Use __`time.sleep()`__. This will be a difficult function
to test, as you'd have to check elapsed time. It's possible, but not required.

### ...and even more if you want (these are getting way from the operations a CPU would perform, but they might be fun to do)
* __`MAKES`__
<br>Create a "stack" inside the EXA. Each stack will have a unique numeric ID, just like we are doing with files.

* __`STACK R`__
<br>Get the ID of the current list. Analogous to the __`FILE R`__ instruction.

* __`GRABS R/N`__
<br>Grab a list with the specified ID. An error if the list does not exist.

* __`DELS`__
<br>Delete the current stack. An error there is no current stack (i.e., it was not preceded by __`GRABS`__).

* __`PUSH R/N`__
<br>Append the number or contents of register to the current list. An error if no current stack.

* __`POP R`__
<br>Pop the top/latest item from the stack and put it into R. An error if no current stack or current stack is empty.

* __`SIZE R`__
<br>Place the size of the current stack (0 if empty) into R. An error if no current stack
