# challenge portfolio Anna
 
## TASK 1: SOFTWARE CONFIGURATION

### Subtask 1: Why did I choose to participate in the portfolio challenge?

I am a manual software tester with more than one year of commercial experience. 

I love challenges and **learning by doing**. I enjoy learning in a group and gaining knowledge from others by **finding solutions together**. 

I would like to expand my knowledge of automated testing and Python.




 ## TASK 2: SELECTORS

https://scouts-test.futbolkolektyw.pl/en/login

Login
1. //*[@id="login"]
2. /html/body/div/form/div/div[1]/div[1]/div/input
3. //input[@name="login"]

Passowrd
1. //*[@id="password"]//div
2. //input[@name="password"]
3. /html/body/div/form/div/div[1]/div[2]/div/input//div

Sign in
1. //*[text()="Sign in"]
2. //*[@id="__next"]/form/div/div[2]/button/span[1]
3. /html/body/div/form/div/div[2]/button/span[1]

English
1. //*[@id="__next"]/form/div/div[2]/div/div
2. //*[contains(@class, "MuiTypography-root MuiLink")]
3. /html/body/div/form/div/div[2]/div/div

Remind password
1. //*[text()="Remind password"]
2. //*[@id="__next"]/form/div/div[1]/a
3. /html/body/div/form/div/div[1]/a


PL https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true

Polski
1. //*[@id="__next"]/form/div/div[2]/div/div
2. //*[text()="Polski"]
3. /html/body/div/form/div/div[2]/div/div

Zaloguj
1. //*[@id="__next"]/form/div/div[2]/button/span[1]
2. //*[text()="Zaloguj"]
3. /html/body/div/form/div/div[2]/button/span[1]

