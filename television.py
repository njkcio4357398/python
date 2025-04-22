class Television:
    """
    A class to simulate a basic Television with power, channel, volume, and mute controls.
    """
    MIN_CHANNEL = 1
    MAX_CHANNEL = 50
    MIN_VOLUME = 0
    MAX_VOLUME = 10

    def __init__(self) -> None:
        """Initialize the Television to default state."""
        self._power = False
        self._channel = self.MIN_CHANNEL
        self._volume = self.MIN_VOLUME
        self._muted = False
        self._last_volume = self._volume

    def power(self) -> None:
        """Toggle the power state of the TV."""
        self._power = not self._power

    def mute(self) -> None:
        """Toggle mute state. Muting sets volume to 0 but remembers previous volume."""
        if self._power:
            if not self._muted:
                self._last_volume = self._volume
                self._volume = 0
            else:
                self._volume = self._last_volume
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the channel number, wrap to MIN_CHANNEL if MAX_CHANNEL is exceeded."""
        if self._power:
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

    def channel_down(self) -> None:
        """Decrease the channel number, wrap to MAX_CHANNEL if MIN_CHANNEL is underflowed."""
        if self._power:
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self) -> None:
        """Increase volume by 1, respecting the MAX_VOLUME limit and unmuting if muted."""
        if self._power:
            if self._muted:
                self._muted = False
                self._volume = self._last_volume
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
                self._last_volume = self._volume

    def volume_down(self) -> None:
        """Decrease volume by 1, respecting the MIN_VOLUME limit and unmuting if muted."""
        if self._power:
            if self._muted:
                self._muted = False
                self._volume = self._last_volume
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
                self._last_volume = self._volume

    def __str__(self) -> str:
        """Return the string representation of the TV state."""
        return f"Power = {self._power}, Channel = {self._channel}, Volume = {self._volume}"
