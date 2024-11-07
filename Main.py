#TODO: check if __init__, __main__ is OK
from WasRun import WasRun

class Main:
    def main():
        print("hello world")

        test = WasRun("testMethod")
        print(test.wasRun)
        test.run()
        print(test.wasRun)

Main.main()