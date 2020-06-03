class USBReader:

    def read_usb(self, usb):
        print('read USB data:', usb.get_raw_usb_data())


class USBStick:

    def __init__(self):
        self.usb_data = ''

    def save_usb_format_data(self, data):
        if self.usb_data:
            self.usb_data += ',{}'.format(data)
        else:
            self.usb_data += data

    def get_raw_usb_data(self):
        return self.usb_data


class SDCard:

    def __init__(self):
        self.sd_data = []

    def save_sd_format_data(self, data):
        self.sd_data.append(data)

    def get_raw_sd_data(self):
        return self.sd_data


class SDCardAdapter(USBStick):

    def __init__(self, sd_card):
        super().__init__()
        self.sd_card = sd_card

    def save_usb_format_data(self, data):
        self.sd_card.sd_data.append(data)

    def get_raw_usb_data(self):
        raw_data = self.sd_card.get_raw_sd_data()
        return ','.join(raw_data)


if __name__ == '__main__':
    usb_stick = USBStick()
    usb_stick.save_usb_format_data('data1')
    usb_stick.save_usb_format_data('data2')
    usb_stick.save_usb_format_data('data3')
    sd_card = SDCard()
    sd_card_adapter = SDCardAdapter(sd_card)
    sd_card.save_sd_format_data('data4')
    sd_card_adapter.save_usb_format_data('data5')
    sd_card_adapter.save_usb_format_data('data6')

    usb_reader = USBReader()
    usb_reader.read_usb(usb_stick)
    usb_reader.read_usb(sd_card_adapter)
    # usb_reader.read_usb(sd_card)  ERROR! USB reader is not compatible with SD card.
