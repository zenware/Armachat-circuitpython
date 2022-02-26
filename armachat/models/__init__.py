from abc import abstractmethod
from armachat.models.armachat_compact import ARMACHATCompact

class DeviceModel:
    """

    """
    def __init__(self):
        self.model_name = 'Unknown Model'
        self.radio = None
        self.display = None
        self.speaker = None

    @abstractmethod
    def init_radio(self):
        raise NotImplementedError()

    @abstractmethod
    def init_display(self):
        raise NotImplementedError()

    @abstractmethod
    def init_speaker(self):
        raise NotImplementedError()

    @staticmethod
    def select_device(detector):
        """Attempts to detect board and chip to supply an appropriate model.

        Makes use of adafruit_platformdetect import Detector
        """
        print("Chip id: ", detector.chip.id)
        print("Board id: ", detector.board.id)

        # NOTE: We are doing no detection currently, and furthermore I think
        # platform_detect may specificallyn not have support for the chip/board
        # we care abotu at the moment.
        return ARMACHATCompact

