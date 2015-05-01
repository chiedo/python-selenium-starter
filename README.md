Python-selenium-starter
=========
Starter set up for writing selenium tests with Python. The Goal is to make it easier to write and run tests
using Selenium for multiple browsers and devices. With this repo, you should be able to just start writing your tests
and not be concerned with the basic set up of your test framework. This has options to also run on browserstack but could easily be modified to use another service with some elementary coding.

Installing Selenium
----------
- Install pip first if needed obviously (google is your friend here)
- pip install -U selenium


Getting Started
-----------
- You can add more tests by adding modules to the tests directory. Copy the structure in the examples and your tests
should be executed automagically by the above.
- You will likely want to update the data in the config.py file. But should not need to update anything in the
run.py file unless you are applying a general fix to this repo that you plan to contribute..

General Examples
---------
To run all tests on Firefox
```
python run.py
```
To override the base url you set in run.py
```
python run.py --base_url "http://google.com"
````
To only run one test
```
python run.py --test "example_a.py"
````
To see more options
```
python run.py --help
```

Browserstack options
=========
- Before anything, you need to get your Selenium automate username and automate value from the following URL.https://www.browserstack.com/accounts/automate
- Once you have those values modify your ~/.bash_profile to end with the following. (use ~/.bashrc instead if on linux)
```
export SELENIUM_AUTOMATE_USERNAME="REPLACE_THIS"
export SELENIUM_AUTOMATE_VALUE="REPLACE_THIS"
```
- Then run the following in your terminal (remember to modify to ~/.bashrc if on linux)
```
source ~/.bash_profile
```

Open a tab and run the following to start the local testing server. That will make sure you can still access the site via the correct IP address, etc.
```
./local_testing_binaries/osx/BrowserStackLocal $SELENIUM_AUTOMATE_VALUE localhost,3000,0 -forcelocal -vv
```
Then Run the following to execute the tests and hook into the browser stack local testing server
```
python run.py --browserstack --use_local
```

Browserstack Examples
--------
To run with only in the desktop browsers:
```
python run.py --browserstack --mobile
```
To run with only the in the desktop browsers:
```
python run.py --browserstack --desktop
```
To override the base url you set in run.py
```
python run.py --browserstack --capabilities "{'os_version': '7', 'browser_version': '8.0', 'os': 'Windows', 'resolution': '1024x768', 'browser': 'IE'}"
````

Browserstack Notes
----------
- For more browserstack options, you can see more details here https://www.browserstack.com/automate/python.
- You will notice that your username and value are hard coded in those examples though. Just replace those areas with the environment variables we set up to make your code more shareable.
- Local testing is VERY slow... Do as you wish
