class Phone:

    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")


class Android(Phone):
    def __init__(self, phone_number, color, size):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50
        self.size = size

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")


newphone = Android('888-777-3333', 'black', 8.5)

newphone.view_battery_life()
newphone.charge_phone(200)
newphone.view_battery_life()
newphone.view_phone_number()

newphone.call('859-699-0000')
newphone.open_app('Zoom')

# class IPhone(Phone):

# class GalaxyPhone(Android):
#   def __init__(self, )
