# PythonCucumber

This template is an example of how to implement automated tests using Behave (aka Cucumber for Python) with Python and 
Page Object pattern.

## Requirements
A browser-driver needs to be installed such as chromedriver, to open the browser. 

| Browser | terminal command  |
|---------|-------------------|
| Chrome  | pip install chromedriver-py |
| MS Edge | pip install msedge-selenium-tools |

This example is using chrome. If needed, you can modify this in class "googleTest.py", line 8.

## Project Setup
1. Use the terminal and navigate to this test project
2. Run the following commands 
```sh
pip install pytest
pip install selenium
pip install behave
```

### Preconditions
Because some locators (especially when it comes to Google's website) inherit text, you need to adjust this text to your 
language.

If you're not German, please adjust line 13 in class "GoogleLandingPagePO"
```
"//button/div[contains(text(),'<decline all>')]"
```

## Copyright
This template was created by [IT-Service Seeliger](https://its-seeliger.de/)