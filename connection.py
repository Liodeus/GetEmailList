import getpass


def connect(browser):
    # Authentification
    username = raw_input("Username : ")
    password = getpass.getpass("Password : ")

    # Fill the authentification form
    browser.form = list(browser.forms())[0]
    browser["username"] = username
    browser["password"] = password

    # Send the form you just fill and get the cookie(s)
    response = browser.submit()
    cookies = browser._ua_handlers['_cookies'].cookiejar
    browser.back()

    # If there is 1 cookie then you aren't connected
    if len(cookies) == 1:
        print("")
        return connection(browser)
