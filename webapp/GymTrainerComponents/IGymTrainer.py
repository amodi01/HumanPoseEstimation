import abc
import hpeModule
from abc import ABC, abstractmethod

class IGymTrainer(ABC):

    @abc.property
    def sampleVideo(self):
        pass
    def getPoseDetector(self):
        return PoseDetector()
