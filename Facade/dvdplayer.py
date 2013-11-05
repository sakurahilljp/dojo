# -*- coding: utf-8 -*-

class DvdPlayer(object):
    def __init__(self, ampifier, projector):
        self.__ampifier = ampifier
        self.__projector = projector
        self.__disk = None

        print 'Initalizing DVD Player'
        print '   connected to %s' % (self.__ampifier,)
        print '   connected to %s' % (self.__projector,)

        
    def __repr__(self):
        return 'DvdPlayer(ampifier="%s", projector="%s")' % (self.__ampifier, self.__projector)

    def power_on(self):
        print '%s : power on' % (self,)

    def power_off(self):
        print '%s : power off' % (self,)

    def insert_disk(self, disk):
        if self.__disk is None:
            self.__disk = disk
            print '%s : Disk "%s" is inserted.' % (self, self.__disk)
        else:
            print '%s : Disk has been already inserted.' % (self,)

    def eject_disk(self):
        if self.__disk is not None:
            self.stop()
            print '%s : Disk "%s" is ejected.' % (self, self.__disk)
            self.__disk = None

    def play(self):
        if self.__disk is not None:
            print '%s : Playing disk "%s"' % (self, self.__disk)
    def stop(self):
        print '%s : Stopping disk "%s"' % (self, self.__disk)

if __name__ == '__main__':
    player = DvdPlayer('Amplifier', 'Projector')
    player.power_on()
    player.insert_disk('Reality Bites')  
    player.play()
    player.stop()
    player.eject_disk()
    player.power_off()
