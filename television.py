class Television:
    """
    Class represents basic tv power, volume, channel, and mute functions.

    Class Variables:
    - MIN_VOLUME: Minimum volume level (0).
    - MAX_VOLUME: Maximum volume level (2).
    - MIN_CHANNEL: Minimum channel number (0).
    - MAX_CHANNEL: Maximum channel number (3).
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Starts a Television object with default values.

        :param self: Refers to current state of class
        :return: None
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggles power status of tv

        :param self: Refers to current state of class
        :return: None
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggles mute status of tv if powered on

        :param self: Refers to current state of class
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increases channel by one, going to MIN_CHANNEL if at MAX_CHANNEL
        Only works if tv is on

        :param self: Refers to current status of class
        :return: None
        """
        if self.__status:
            self.__channel = (
                Television.MIN_CHANNEL if self.__channel == Television.MAX_CHANNEL
                else self.__channel + 1
            )

    def channel_down(self):
        """
        Decreases the channel by one, going to MAX_CHANNEL if at MIN_CHANNEL
        Only works if tv is on

        :param self: Refers to current status of class
        :return: None
        """
        if self.__status:
            self.__channel = (
                Television.MAX_CHANNEL if self.__channel == Television.MIN_CHANNEL
                else self.__channel - 1
            )

    def volume_up(self):
        """
        Increases volume by one up to MAX_VOLUME. Stop muting tv if it was muted.
        Only works if tv is on

        :param self: Refers to current status of class
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases volume by one down to MIN_VOLUME. Stop muting tv if it was muted.
        Only works when tv is on.

        :param self: Refers to current status of class
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string of current state of tv

        :param self: Refers to current status of class
        :return: str - formated string shows power status, channel, and volume
        """
        volume_display = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"

