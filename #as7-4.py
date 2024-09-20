#as7-4
class TV:
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200
    def __init__(self, volume = 5, channel = MIN_CHANNEL, is_on = False):
        self.__volume = volume
        self.__channel = channel
        self.__is_on = is_on

    def __str__(self):
        if not self.__is_on:
            return f"TV가 꺼짐 상태입니다."
        return f"볼륨 = {self.__volume}, 채널 = {self.__channel}"
        
    def toggle_power(self):
        self.__is_on = not self.__is_on

    def get_channel(self):
        return self.__channel
    
    def set_channel(self, channel):
        if TV.MIN_CHANNEL <= channel <= TV.MAX_CHANNEL:
            self.__channel = channel

    def get_volume(self):
        return self.__volume
    
    def set_volume(self, volume):
        if  TV.MIN_VOLUME <= volume <= TV.MAX_VOLUME:
            self.__volume = volume
        else:
            print('볼륨오류')
    def volume_up(self):
        if self.__volume < TV.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        if self.__volume > TV.MIN_VOLUME:
            self.__volume -= 1

    def channel_up(self):
        if self.__channel < TV.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = TV.MIN_VOLUME

    def channel_down(self):
        if self.__channel > TV.MIN_CHANNEL:
            self.__channel -= 1
        else:
            self.__channel = TV.MAX_CHANNEL

def main():
    my_tv = TV()
    print(my_tv)
    my_tv.toggle_power()
    print(my_tv)
    my_tv.set_channel(45)
    print(my_tv)
    my_tv.volume_up()
    my_tv.channel_up()
    print(my_tv)

main()

