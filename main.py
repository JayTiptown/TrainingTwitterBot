import logIn
import scrape_tl
import time

def main():
    logIn.logInPath()

    time.sleep(3)

    scrape_tl.scrape()

    while (True):
        pass

if __name__ == "__main__":
    main()