import TrainingTypeAttributes as ttp
import JumpingSquatsTrainer


class GymTrainerFatcory:
    def __init__(self, trainType=ttp.trainingTypeAttributes.JumpingSquats):
        self._trainingType = trainType

    def getGymTrainer(self):
        gymTrainer = JumpingSquatsTrainer()
