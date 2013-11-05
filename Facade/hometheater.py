# -*- coding: utf-8 -*-

from amplifier import Amplifier
from dvdplayer import DvdPlayer
from projector import Projector

class HomeTheaterFacade(object):
    def __init__(self, amplifier, dvdplayer, projector):
        self.__amplifier = amplifier
        self.__dvdplayer = dvdplayer
        self.__projector = projector

        print "Initalizing HomeTheaterFacade..."

    def play_movie(self, disk):
        self.__amplifier.power_on()
        self.__dvdplayer.power_on()
        self.__projector.power_on()

        self.__dvdplayer.insert_disk(disk)
        self.__projector.set_mode('DVD')

    def stop_movie(self):
        self.__dvdplayer.stop()
        self.__amplifier.power_off()
        self.__dvdplayer.power_off()
        self.__projector.power_off()

if __name__ == '__main__':
    amplifier = Amplifier()
    projector = Projector()
    dvdplayer = DvdPlayer(amplifier, projector)

    theater = HomeTheaterFacade(amplifier, dvdplayer, projector)
    theater.play_movie('Top Gun')
    theater.stop_movie()
