#!/usr/bin/env python

import time

class SpamGame(object):
    duration = 2

    def __init__(self, phrase):
        self.phrase = phrase
        self.count = 0

    def quit(self):
        print "ByeBye"

    def run(self):
        try:
            while True:
                self.count += 1
                print "%s (times seen: %d)" % (self.phrase, self.count)
                time.sleep(self.duration)
        except KeyboardInterrupt:
            self.quit()

if __name__ == "__main__":
    spammer = SpamGame("You can't catch me, I'm the gingerbread man")
    spammer.run()


