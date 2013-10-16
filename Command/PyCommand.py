# -*- coding: utf-8 -*-

class NopCommand(object):
    def execute(self):
        print "NOP"
    def __str__(self):
        return "NOP"

class RemoteController(object):
    def __init__(self):
        self._switches = 
        {
            0:{'on':NopCommand(), 'off':NopCommand()},
            1:{'on':NopCommand(), 'off':NopCommand()},
            2:{'on':NopCommand(), 'off':NopCommand()},
            3:{'on':NopCommand(), 'off':NopCommand()},
            4:{'on':NopCommand(), 'off':NopCommand()},
        }

    def add(self,key, on_command, off_command):
        if key in self._switches.keys():
            self._switches[key] = {'on':on_command, 'off':off_command}

    def show(self):
        print 'Intelligent Remote Controller:'
        for key in self._switches.iterkeys():
            print "[%d] %s,%s" % ( key, self._switches[key]['on'], 
                                   self._switches[key]['off']);
        else:
            print ''
            
    def on(self, key):
        self._switches[key]['on'].execute()

    def off(self, key):
        self._switches[key]['off'].execute()
        
# Light
class Light(object):
    def __init__(self, name):
        self.name = name
    def on(self):
        print "Turning on '%s' light." % (self.name)
    def off(self):
        print "Turning off '%s' light." % (self.name)

# Fan
class Fan(object):
    def __init__(self, name):
        self.name = name
    def on(self):
        print "Turning on '%s' fan." % (self.name)
    def off(self):
        print "Turning off '%s' fan." % (self.name)

# Command for any light
class LightCommand(object):
    def __init__(self, light):
        self._light = light
class LightOnCommand(LightCommand):
    def execute(self):
        self._light.on()
    def __str__(self):
        return '"%s" Light On Command' % self._light.name
class LightOffCommand(LightCommand):
    def execute(self):
        self._light.off()
    def __str__(self):
        return '"%s" Light Off Command' % self._light.name

# Command for any fan
class FanCommand(object):
    def __init__(self, fan):
        self._fan = fan
class FanOnCommand(FanCommand):
    def execute(self):
        self._fan.on()
    def __str__(self):
        return '"%s" Fan On Command' % self._fan.name
class FanOffCommand(FanCommand):
    def execute(self):
        self._fan.off()
    def __str__(self):
        return '"%s" Fan Off Command' % self._fan.name

if __name__ == '__main__':
    
    # Create equipments
    gate_light = Light("Gate")
    entrance_light = Light("Entrance")
    living_fan = Fan('Living')
    kitchen_fan = Fan('Kitchen')

    # Create a controller and congigure it.
    controller = RemoteController()
    controller.add(0, LightOnCommand(gate_light), LightOffCommand(gate_light));
    controller.add(1, LightOnCommand(entrance_light), LightOffCommand(entrance_light));
    controller.add(2, FanOnCommand(living_fan), FanOffCommand(living_fan));
    controller.add(3, FanOnCommand(kitchen_fan), FanOffCommand(kitchen_fan));
    controller.show()

    # Control equipment
    controller.on(0)
    controller.off(0)

    controller.on(1)
    controller.off(1)
    
    controller.on(2)    
    controller.off(2)

    controller.on(3)
    controller.off(3)
