# HashKeyTwitterBot
This twitter bot uses selenium web driver to scrape twitter timelines and obtain account, tweet, date, and engagement data. This is facilitated by ChromeDriver, a web interaction tool that enables automated interaction of the chrome browser.

1. Clone this GitHub repo.

2. Install Dependencies:

    1. Install python at https://www.python.org/downloads/ if not installed already.

    2. Run "pip install selenium". You may need to install using "pip2" or "pip3" depending on your python version.

    3. Run "pip install python-dotenv". 

    4. Install ChromeDriver at https://sites.google.com/chromium.org/driver. Install the webdriver that is compatible with your version of chrome. You can check your chrome version by going to the three dots at the top right corner of your browser Help --> About Google Chrome. 

3. Access the ChromeDriver file and move chromedriver to your IDE. 

4. Make a new Twitter account to serve as your bot. It is preferable to make a new email for this, otherwise using a spare email/phone number is fine.

5. Follow relevant accounts through twitter. An inital list was provided that are considered "high signal". 
    High Signal Accounts: @ljxie, @tongnk, @kankanivishal, @zaki, @gavofyork, @cburniske, @delitzer, @wyatt_benmo, @divine_economy, @dynamo_patri

6. Insert your username and password credentials into the env file in your IDE. 

7. Run the program. You should see a new chrome window open. If this fails, you might have been signed into twitter already. In this case, sign out, kill the program, and rerun. If you were already signed out and it still fails, you might have used the wrong chromedriver version. 

WARNING: This bot has not been thoroughly tested for avoiding twitter's newly improved bot detection algorithms. Only primitive avoidance measures are used. Excessive use of the bot may result in IP blocking by Twitter, which may prevent your ability to use the bot or even access Twitter on your device. Use at your own discretion. 