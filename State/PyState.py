# -*- coding: utf-8 -*-

class State(object):
    def __init__(self, context):
        self.context = context
    def insert_coin(self):
        raise NotImplementedError()
    def eject_coin(self):
        raise NotImplementedError()
    def turn_crank(self):
        raise NotImplementedError()
    def dispense(self):
        raise NotImplementedError()

class GumBallMachine(object):
    def __init__(self,count):
        self.count = count
        if self.count > 0:
            self.state = NoCoinState(self)
        else:
            self.state = SoldOutState(self)
    def insert_coin(self):
        print 'inserting a coin...'
        self.state.insert_coin()
    def eject_coin(self):
        print 'ejecting a coin...'
        self.state.eject_coin()
    def turn_crank(self):
        print 'turning crank...'
        self.state.turn_crank()
        self.state.dispense()
    def release_ball(self):
        if self.count != 0:
            self.count -= 1
            print '--> Relased a gum ball.'
            print '    There are %d gum balls left.' % self.count
        else:
            print '--> Sorry. Gum balls are sold out.'

class NoCoinState(State):
    def __init__(self, context):
        super(self.__class__, self).__init__(context)
    def insert_coin(self):
        print '>> a coin has been inserted.'
        self.context.state = HasCoinState(self.context)
    def eject_coin(self):
        print '>> There are no coin'
    def turn_crank(self):
        print '>> Put a coin before you turn a crank'
    def dispense(self):
        pass

class HasCoinState(State):
    def __init__(self, context):
        super(self.__class__, self).__init__(context)
    def insert_coin(self):
        print '>> There is already a coin.'
    def eject_coin(self):
        print '>> a coin has been ejected.'
        self.context.state = NoCoinState(self.context)
    def turn_crank(self):
        self.context.state = SoldState(self.context)
    def dispense(self):
        pass
    
class SoldState(State):
    def __init__(self, context):
        super(self.__class__, self).__init__(context)
    def insert_coin(self):
        print '>> wait a moment. a gum ball is being released.'
    def eject_coin(self):
        print '>> you already turned a crank. a coin cannot be ejected.'
    def turn_crank(self):
        print '>> you cannot get another gum ball if you turn a crank again.'
    def dispense(self):
        self.context.release_ball()
        if self.context.count > 0:
            self.context.state = NoCoinState(self.context)
        else:
            self.context.state = SoldOutState(self.context)

class SoldOutState(State):
    def __init__(self, context):
        super(self.__class__, self).__init__(context)
    def insert_coin(self):
        print '>> sold out...'
    def eject_coin(self):
        print '>> sold out...'
    def turn_crank(self):
        print '>> sold out...'
    def dispense(self):
        pass

if __name__ == '__main__':
    machine = GumBallMachine(3)

    print ''
    machine.insert_coin()
    machine.turn_crank()

    print ''
    machine.insert_coin()
    machine.eject_coin()
    machine.turn_crank()
    
    print ''
    machine.insert_coin()
    machine.turn_crank()

    print ''
    machine.insert_coin()
    machine.turn_crank()

    print ''
    machine.insert_coin()
    machine.turn_crank()
