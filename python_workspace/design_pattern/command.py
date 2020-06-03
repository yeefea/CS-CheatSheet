class Command:

    def execute(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass


class Light:

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        print('Light is on')

    def off(self):
        self.is_on = False
        print('Light is off')


class SwitchLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        if self.light.is_on:
            self.light.off()
        else:
            self.light.on()


class Radio:

    def __init__(self):
        self.is_on = False
        self.is_am = True
        self.volume = 0

    def on(self):
        self.is_on = True
        print('Radio is on')

    def off(self):
        self.is_on = False
        print('Radio is off')

    def set_am(self):
        self.is_am = True
        print('Radio set to AM')

    def set_fm(self):
        self.is_am = False
        print('Radio set to FM')

    def set_volume(self, volume):
        self.volume = volume
        print('Radio volume set to', volume)


class RadioCommand(Command):

    def __init__(self, radio):
        self.radio = radio


class RadioOnCommand(RadioCommand):

    def execute(self):
        self.radio.on()


class RadioOffCommand(RadioCommand):
    def execute(self):
        self.radio.off()


class RadioAMCommand(RadioCommand):
    def execute(self):
        self.radio.set_am()


class RadioFMCommand(RadioCommand):

    def execute(self):
        self.radio.set_fm()


class RadioTurnUpCommand(RadioCommand):

    def __init__(self, radio):
        super().__init__(radio)
        self.origin_volume = radio.volume

    def execute(self):
        self.radio.set_volume(self.origin_volume + 10)

    def redo(self):
        self.execute()

    def undo(self):
        self.radio.set_volume(self.origin_volume - 10)


class RadioTurnDownCommand(RadioCommand):

    def __init__(self, radio):
        super().__init__(radio)
        self.origin_volume = radio.volume

    def execute(self):
        self.radio.set_volume(max(self.origin_volume - 10, 0))

    def redo(self):
        self.execute()

    def undo(self):
        self.radio.set_volume(self.origin_volume)


class CommandStack:

    def __init__(self):
        # command stack for undo and redo
        pass


if __name__ == '__main__':
    light = Light()
    radio = Radio()

    SwitchLightCommand(light).execute()
    RadioOnCommand(radio).execute()
    RadioTurnUpCommand(radio).execute()
    RadioTurnUpCommand(radio).execute()
    RadioTurnDownCommand(radio).execute()
    RadioAMCommand(radio).execute()
    RadioFMCommand(radio).execute()
    RadioOffCommand(radio).execute()
    SwitchLightCommand(light).execute()
