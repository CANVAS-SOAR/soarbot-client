import json
class CarController:
    def __init__(self, steer=0, acceleration=0, brake=0, clutch=0, gear=0):
        self.setControls(steer, acceleration, brake, clutch, gear)

    def setControls(self, steer, acceleration, brake, clutch, gear):
        self.steer = steer
        self.acceleration = acceleration
        self.brake = brake
        self.clutch = clutch
        self.gear = gear

    def setSteer(self, steer):
        self.steer = steer

    def setAcceleration(self, acceleration):
        self.acceleration = acceleration

    def setBrake(self, brake):
        self.brake = brake

    def setClutch(self, clutch):
        self.clutch = clutch

    def setGear(self, gear):
        self.gear = gear

    def serialize(self):
        controls = dict();
        controls["steerCmd"] = self.steer;
        controls["accelCmd"] = self.acceleration;
        controls["brakeCmd"] = self.brake;
        controls["clutchCmd"] = self.clutch;
        controls["gearCmd"] = self.gear;
        
        json.dumps(controls)
        data = bytearray(json.dumps(controls), 'utf8') + b'\x00'
        return data
