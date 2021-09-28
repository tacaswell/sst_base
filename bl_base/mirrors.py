from ophyd import Device, Signal, EpicsSignal, EpicsSignalRO, PVPositioner
from ophyd import FormattedComponent as FmtCpt, Component as Cpt
from ophyd.signal import SignalRO

class HexapodMirror(Device):
    X = Cpt(EpicsSignal, 'X}Mtr_MON',write_pv='X}Mtr_SP',kind='hinted')
    Y = Cpt(EpicsSignal, 'Y}Mtr_MON',write_pv='Y}Mtr_SP',kind='hinted')
    Z = Cpt(EpicsSignal, 'Z}Mtr_MON',write_pv='Z}Mtr_SP',kind='hinted')
    Roll = Cpt(EpicsSignal, 'R}Mtr_MON',write_pv='R}Mtr_SP',kind='hinted')
    Pitch = Cpt(EpicsSignal, 'P}Mtr_MON',write_pv='P}Mtr_SP',kind='hinted')
    Yaw = Cpt(EpicsSignal, 'Yaw}Mtr_MON',write_pv='Yaw}Mtr_SP',kind='hinted')


class FMBHexapodMirrorAxis(PVPositioner):
    readback = Cpt(EpicsSignalRO, 'Mtr_MON')
    setpoint = Cpt(EpicsSignal, 'Mtr_POS_SP')
    actuate = FmtCpt(EpicsSignal, '{self.parent.prefix}}}MOVE_CMD.PROC')
    actual_value = 1
    stop_signal = FmtCpt(EpicsSignal, '{self.parent.prefix}}}STOP_CMD.PROC')
    stop_value = 1
    done = FmtCpt(EpicsSignalRO, '{self.parent.prefix}}}BUSY_STS')
    done_value = 0


class FMBHexapodMirror(Device):
    z = Cpt(FMBHexapodMirrorAxis, '-Ax:Z}')
    Y = Cpt(FMBHexapodMirrorAxis, '-Ax:Y}')
    X = Cpt(FMBHexapodMirrorAxis, '-Ax:X}')
    Pitch = Cpt(FMBHexapodMirrorAxis, '-Ax:P}')
    Yaw = Cpt(FMBHexapodMirrorAxis, '-Ax:Yaw}')
    Roll = Cpt(FMBHexapodMirrorAxis, '-Ax:R}')