# gui-name-display-tutorial
##What is a GUI, you ask?
GUI stands for ‘graphical user interface’, and it is pronounced like ‘gooey’.

If you have written Python programs before, these will probably have dealt with input as text typed in by the user, and with output appearing on the screen.

Adding a GUI to your program lets the user interact with it using buttons, menus, text boxes, and other familiar user interface features.

##Python and Pip
First, we need to make sure we have Python downloaded. https://www.python.org/downloads/

Next, we need to install `guider` with pip. 

###Windows 
`pip3 install guizero`

###MacOS
`sudo pip3 install guizero`

##Getting started 
I am using Visual Studio Code but feel free to use any text editor or Python IDLE. 
Create a new file named `gui_test.py`

Add a line of code at the top of your file to import the `App` class from the `guizero` module:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/zt2kj2w1t93pfg2wo3ku.png)

Now add two more lines of code to create an App and then display it on the screen:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/1lw9a05tyf7imn1lvefd.png)

Save your file and run it. You should see a GUI window that looks like this:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/lokn5w22jul57d0kdnxm.png)

If you are in VScode, you can hit the play button on the top right or right-click and select the option below.
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/ke8l0jm5w4s68h0178zn.png)

##Adding widgets
Let’s start adding content to the GUI. We refer to items you can add to a GUI (such as text, text boxes, buttons, etc.) as "widgets". There are a couple of rules to follow when adding a widget.
-If you want to use a new type of widget, you must import it. As an example, if you wanted to use the Text widget, you would add it to the import statement, like this:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/ihr3hb24zps8zubvckf3.png)

-All code that creates a widget must be added above the event loop, meaning above the app.display() line of code, and below the line of code where you create the app:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/5zypi0ywv6t2w13lvrd3.png)

Throughout this guide, whenever we ask you to add widgets to the GUI, you should add them anywhere between these two lines of code.

##Text widget
Probably the simplest widget you can add is the Text widget, which displays some text on the screen.

-Add `Text` to the `import` statement (check back in the Adding widgets section if you are not sure how to do this).

-Add a `Text` widget to the GUI

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/y87tpmazclhjul0c7ni8.png)
Here we have created a `Text` widget with the name `welcome_message`. The first argument (in the brackets) tells the widget who its boss is! To be more specific, we are telling this `Text` widget that it will be controlled by the `app` object that we created earlier. The first argument given to any widget always tells it the name of its boss.

Save and run your code. You should now see something like this in your GUI. 
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/kt3tfbnzrzygq64w5dck.png)

Did you notice that we could tell the `Text` widget what content we wanted it to display by specifying `text="Welcome to my app"`? This is called a keyword argument, because we have specified the keyword `text` and the value we want. We can specify other keyword arguments too by just adding them after the `text` one and separating them by commas: (feel free to throw in your own size, font and color)
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/9fe82hxo4bkio38io5v6.png)

Save your code and run it. You should now see the changes in your GUI. 
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/4weqlnn0zz6oflqaz1nb.png)

##Textbox widget 
A `TextBox` widgets allows the user to type in data, a bit like the GUI version of Python’s `input()` function, which you may have used before. Here’s how to add a `TextBox`:

-Add `TextBox` to your `import` statement.
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/w63mk93pramvvqhyl41x.png)

-Add a `TextBox` widget to the GUI
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/64055tffwrdeodu4qzzv.png)

Run your code and you should now see your text box.
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/am80vq9w80y6ok9qsr9u.png)

##Pushbutton widget
You can use a `PushButton` widget to create a button, and write code so that when the button is pushed, a function is called.

To keep your script nice and tidy, it is a good idea to put all the code which defines functions at the top of your program, immediately below the `import` line.

Above the code which creates the GUI app, write a function called `say_my_name`:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/2la8mdugbbjhw7lbm5oi.png)

So this `say_my_name` function refers to the `Text` widget that you’ve written earlier welcome_message. It will set the value of `welcome_message` to what was typed into your TextBox widget (`my_name`).

You can use the value property with many widgets to retrieve their current value or to set it to something new.

-Add `PushButton` to your `import` statement.
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/vvly1bkvuqeslxxfs8as.png)

-Add a `PushButton` widget to the GUI:
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/j47w218zlsi2rwhnvrr1.png)
The first argument tells the `PushButton` that the `app` is its boss. Then we use two keyword arguments: `command` tells the button which function to call when it is pressed, and `text` is the text which will be displayed on the button.
![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/80n5cy9r5pxcsq269had.png)
