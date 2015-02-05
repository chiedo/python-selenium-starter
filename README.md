Python-selenium-starter
=========
Starter set up for writing selenium tests with Python

Installing Selenium
----------
- Install pip first if needed obviously (google is your friend here)
- pip install -U selenium

Setting Up Your Environment Variables
----------
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

Getting Started
----------
Then Run the following to execute the tests
```
python run.py
```

Run the following to see all the possible arguments
```
python run.py --help
```
Examples
---------
To run with only in the desktop browsers:
```
python run.py --mobile
```
To run with only the in the desktop browsers:
```
python run.py --desktop
```
To override the base url you set in run.py
```
python run.py --base_url "http://google.com"
````
To only run one test
```
python run.py --test "example_a.py"
````
To only run in one browser
```
python run.py --capabilities "{'os_version': '7', 'browser_version': '8.0', 'os': 'Windows', 'resolution': '1024x768', 'browser': 'IE'}"
````

Notes
---------
- You can see more details here https://www.browserstack.com/automate/python.
- You will notice that your username and value are hard coded in those examples though. Just replace those areas with the environment variables we set up to make your code more shareable.
