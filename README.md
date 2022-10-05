# Starting the application

## Before starting...

### Dependencies

Use `pip install <module>` on the following modules:
- cryptography
- pycryptodome

### The outputs/ folder

By default, the program uses the `outputs/` directory from its filepath to store outputs from file encryptions. ***It will be created automatically***, but if you already have an `outputs` in your directory and it is **NOT** a directory, it will cause the program to fail outputting encrypted files.

### Setting up dev environment

Use pip to install these dependencies.

- cryptography
- pycryptodome

### Start the application

To start the application, all you need to do is run this command.

```bash
$ python main.py
```

If all dependencies are installed, then the application should bring you to the start screen where you can choose to `encrypt a file` (task 1) or `mimic a website` (task 2). From there the application will walk you through the steps to either encrypt the image files or a user inputted message.

### Mimic a website

When in `mimic a website`, the application will prompt the user for an input message. Here you can add whatever you want; however, if you would like to successfully 'hack' into the admin system you must input a string with the following format: [6 of any character not affected by URL encoding] followed by '9admin9true9'

#### Successful Hacking string example

```bash
$ python3 main.py

Select an option:

1) encrypt a file
2) mimic a website
4) exit
> 2

Give input message > 1111119admin9true9
```
