# challenge portfolio Anna
 
## TASK 1: SOFTWARE CONFIGURATION

### Subtask 1: Why did I choose to participate in the portfolio challenge?

I am a manual software tester with more than one year of commercial experience. 

I love challenges and **learning by doing**. I enjoy learning in a group and gaining knowledge from others by **finding solutions together**. 

I would like to expand my knowledge of:
* automated testing
* Python
* tools




## TASK 2: SELECTORS

### Subtask 2: selectors on the login page

### https://scouts-test.futbolkolektyw.pl/en/login

Login_filed_xpath
1. //*[@id="login"]
2. /html/body/div/form/div/div[1]/div[1]/div/input
3. //input[@name="login"]

Password_filed_xpath
1. //*[@id="password"]//div
2. //input[@name="password"]
3. /html/body/div/form/div/div[1]/div[2]/div/input//div

Sign_in_button_xpath
1. //*[text()="Sign in"]
2. //*[@id="__next"]/form/div/div[2]/button/span[1]
3. /html/body/div/form/div/div[2]/button/span[1]

English_language_xpath
1. //*[@id="__next"]/form/div/div[2]/div/div
2. //*[contains(@class, "MuiTypography-root MuiLink")]
3. /html/body/div/form/div/div[2]/div/div

Remind_password_button_xpath
1. //*[text()="Remind password"]
2. //*[@id="__next"]/form/div/div[1]/a
3. /html/body/div/form/div/div[1]/a


### https://scouts-test.futbolkolektyw.pl/pl/login

Polski_language_xpath
1. //*[@id="__next"]/form/div/div[2]/div/div
2. //*[text()="Polski"]
3. /html/body/div/form/div/div[2]/div/div

Zaloguj_button_xpath
1. //*[@id="__next"]/form/div/div[2]/button/span[1]
2. //*[text()="Zaloguj"]
3. /html/body/div/form/div/div[2]/button/span[1]

