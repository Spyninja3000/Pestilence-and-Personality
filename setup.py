from distutils.core import setup
import sys

queue = setup(
    name="Pestilence and Personality"
)

queue() if not sys.modules.__contains__('socket') and __name__ == '__main__' else print("Intruder Alert")

class test():
    pass

