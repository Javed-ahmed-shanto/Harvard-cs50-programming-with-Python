import cowsay
import sys
from sayings import hello

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
    hello(sys.argv[1])