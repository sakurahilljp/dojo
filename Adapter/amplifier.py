# -*- coding: utf-8 -*-

class Amplifier(object):
    def __init__(self):
        self.__volume = 10
        
        print 'Initializing %s' % self
        print '   default volume is %d' % self.__volume

    def __repr__(self):
        return 'Amplifier()'
        
    def power_on(self):
        print '%s : power on' % (self,)
    def power_off(self):
        print '%s : power off' % (self,)
    def volume_up(self, step=1):
        self.__volume += step
        print '%s : volume is up to %d' % (self, self.__volume)
    def volume_down(self, step=1):
        self.__volume -= step
        print '%s : volume is down to %d' % (self, self.__volume)
        

if __name__ == '__main__':
    
    # amplifier control example
    
    amp = Amplifier()
    amp.power_on()
    amp.power_off()
    amp.volume_up(10)
    amp.volume_down(5)
