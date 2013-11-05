# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

class Projector(object):
    def __init__(self):
        self.__mode = 'TV'

        print 'Initalizing Projector'
        print '   default mode is "%s"' % (self.__mode,)
        
    def __repr__(self):
        return 'Projector()'

    def power_on(self):
        print '%s : power on' % (self,)

    def power_off(self):
        print '%s : power off' % (self,)
        
    def set_mode(self, mode):
        self.__mode = mode
        print '%s : mode is set to "%s"' % (self, self.__mode)

if __name__ == '__main__':
    projector = Projector()
    projector.power_on()
    projector.set_mode('Cinema')
    projector.power_off()
    
