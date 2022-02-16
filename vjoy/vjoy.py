from .hooks import *

class VJoy:
    # SHORT GetvJoyVersion(void)
    @staticmethod
    def GetvJoyVersion():
        return GetvJoyVersion()

    # BOOL vJoyEnabled(void)
    @staticmethod
    def vJoyEnabled():
        return vJoyEnabled()

    # PVOID GetvJoyProductString(void)
    @staticmethod
    def GetvJoyProductString():
        return GetvJoyProductString()

    # PVOID GetvJoyManufacturerString(void)
    @staticmethod
    def GetvJoyManufacturerString():
        return GetvJoyManufacturerString()

    # PVOID GetvJoySerialNumberString(void)
    @staticmethod
    def GetvJoySerialNumberString():
        return GetvJoySerialNumberString()

    
	# VjdStat GetVJDStatus(UINT rID)
    @staticmethod
    def GetVJDStatus(rid):
        return GetVJDStatus(rid)

    # BOOL DriverMatch(WORD * DllVer, WORD * DrvVer)
    @staticmethod
    def DriverMatch(dllver, drvver):
        return DriverMatch(dllver, drvver)

    # VOID RegisterRemovalCB(RemovalCB cb, PVOID data)
    # @staticmethod
    # def RegisterRemovalCB(cb, data):
    #     return RegisterRemovalCB(cb, data)

    # BOOL vJoyFfbCap(BOOL * Supported)
    @staticmethod
    def vJoyFfbCap():
        supported = c_bool()
        rv = vJoyFfbCap(supported)
        return supported.value if rv else None

    # BOOL GetvJoyMaxDevices(int * n)
    @staticmethod
    def GetvJoyMaxDevices():
        n = c_int()
        rv = GetvJoyMaxDevices(n)
        return n.value if rv else None

    # BOOL GetNumberExistingVJD(int * n)
    @staticmethod
    def GetNumberExistingVJD():
        n = c_int()
        rv = GetNumberExistingVJD(n)
        return n.value if rv else None

    # int GetVJDButtonNumber(UINT rID)
    @staticmethod
    def GetVJDButtonNumber(rid):
        return GetVJDButtonNumber(rid)

    # int GetVJDDiscPovNumber(UINT rID)
    @staticmethod
    def GetVJDDiscPovNumber(rid):
        return GetVJDDiscPovNumber(rid)

    # int GetVJDContPovNumber(UINT rID)
    @staticmethod
    def GetVJDContPovNumber(rid):
        return GetVJDContPovNumber(rid)

    # BOOL GetVJDAxisExist(UINT rID, UINT Axis)
    @staticmethod
    def GetVJDAxisExist(rid, axis):
        return GetVJDAxisExist(rid, axis)

    # BOOL GetVJDAxisMax(UINT rID, UINT Axis, LONG * Max)
    @staticmethod
    def GetVJDAxisMax(rid, axis):
        _max = c_long()
        rv = GetVJDAxisMax(rid, axis, _max)
        return _max.value if rv else None

    # BOOL GetVJDAxisMin(UINT rID, UINT Axis, LONG * Min)
    @staticmethod
    def GetVJDAxisMin(rid, axis):
        _min = c_long()
        rv = GetVJDAxisMin(rid, axis, _min)
        return _min.value if rv else None

    # BOOL isVJDExists(UINT rID)
    @staticmethod
    def isVJDExists(rid):
        return isVJDExists(rid)

    # int GetOwnerPid(UINT rID)
    @staticmethod
    def GetOwnerPid(rid):
        return GetOwnerPid(rid)

    # BOOL AcquireVJD(UINT rID)
    @staticmethod
    def AcquireVJD(rid):
        return AcquireVJD(rid)

    # VOID RelinquishVJD(UINT rID)
    @staticmethod
    def RelinquishVJD(rid):
        return RelinquishVJD(rid)

    # BOOL UpdateVJD(UINT rID, PVOID pData)
    @staticmethod
    def UpdateVJD(rid, pdata):
        return UpdateVJD(rid, pdata)

    # BOOL ResetVJD(UINT rID)
    @staticmethod
    def ResetVJD(rid):
        return ResetVJD(rid)

    # VOID ResetAll(void)
    @staticmethod
    def ResetAll():
        return ResetAll()

    # BOOL ResetButtons(UINT rID);		// Reset all buttons (To 0)
    @staticmethod
    def ResetButtons(rid):
        return ResetButtons(rid)

    # BOOL ResetPovs(UINT rID);		// Reset all POV Switches (To -1)
    @staticmethod
    def ResetPovs(rid):
        return ResetPovs(rid)

    # BOOL SetAxis(LONG Value, UINT rID, UINT Axis)
    @staticmethod
    def SetAxis(value, rid, axis):
        return SetAxis(value, rid, axis)

    # BOOL SetBtn(BOOL Value, UINT rID, UCHAR nBtn)
    @staticmethod
    def SetBtn(value, rid, nbtn):
        return SetBtn(value, rid, nbtn)

    # BOOL SetDiscPov(int Value, UINT rID, UCHAR nPov)
    @staticmethod
    def SetDiscPov(value, rid, npov):
        return SetDiscPov(value, rid, npov)

    # BOOL SetContPov(DWORD Value, UINT rID, UCHAR nPov)
    @staticmethod
    def SetContPov(value, rid, npov):
        return SetContPov(value, rid, npov)

    # FFBEType FfbGetEffect()
    @staticmethod
    def FfbGetEffect():
        return FfbGetEffect()

    # VOID FfbRegisterGenCB(FfbGenCB cb, PVOID data)
    @staticmethod
    def FfbRegisterGenCB(cb, data):
        return FfbRegisterGenCB(cb, data)

    # BOOL FfbStart(UINT rID)
    @staticmethod
    def FfbStart(rid):
        return FfbStart(rid)

    # VOID FfbStop(UINT rID)
    @staticmethod
    def FfbStop(rid):
        return FfbStop(rid)

    # BOOL IsDeviceFfb(UINT rID)
    @staticmethod
    def IsDeviceFfb(rid):
        return IsDeviceFfb(rid)

    # BOOL IsDeviceFfbEffect(UINT rID, UINT Effect)
    @staticmethod
    def IsDeviceFfbEffect(rid, effect):
        return IsDeviceFfbEffect(rid, effect)

    # DWORD Ffb_h_DeviceID(const FFB_DATA * Packet, int *DeviceID)
    @staticmethod
    def Ffb_h_DeviceID(packet, deviceid):
        return Ffb_h_DeviceID(packet, deviceid)

    # DWORD Ffb_h_Type(const FFB_DATA * Packet, FFBPType *Type)
    @staticmethod
    def Ffb_h_Type(packet, type):
        return Ffb_h_Type(packet, type)

    # DWORD Ffb_h_Packet(const FFB_DATA * Packet, WORD *Type, int *DataSize, BYTE *Data[])
    @staticmethod
    def Ffb_h_Packet(packet, type, datasize, data):
        return Ffb_h_Packet(packet, type, datasize, data)

    # DWORD Ffb_h_EBI(const FFB_DATA * Packet, int *Index)
    @staticmethod
    def Ffb_h_EBI(packet, index):
        return Ffb_h_EBI(packet, index)

    # DWORD Ffb_h_Eff_Report(const FFB_DATA * Packet, FFB_EFF_REPORT*  Effect)
    @staticmethod
    def Ffb_h_Eff_Report(packet, effect):
        return Ffb_h_Eff_Report(packet, effect)

    # DWORD Ffb_h_Eff_Const(const FFB_DATA * Packet, FFB_EFF_CONST*  Effect)
    @staticmethod
    def Ffb_h_Eff_Const(packet, effect):
        return Ffb_h_Eff_Const(packet, effect)

    # DWORD Ffb_h_Eff_Ramp(const FFB_DATA * Packet, FFB_EFF_RAMP*  RampEffect)
    @staticmethod
    def Ffb_h_Eff_Ramp(packet, rampeffect):
        return Ffb_h_Eff_Ramp(packet, rampeffect)

    # DWORD Ffb_h_EffOp(const FFB_DATA * Packet, FFB_EFF_OP*  Operation)
    @staticmethod
    def Ffb_h_EffOp(packet, operation):
        return Ffb_h_EffOp(packet, operation)

    # DWORD Ffb_h_DevCtrl(const FFB_DATA * Packet, FFB_CTRL *  Control)
    @staticmethod
    def Ffb_h_DevCtrl(packet, control):
        return Ffb_h_DevCtrl(packet, control)

    # DWORD Ffb_h_Eff_Period(const FFB_DATA * Packet, FFB_EFF_PERIOD*  Effect)
    @staticmethod
    def Ffb_h_Eff_Period(packet, effect):
        return Ffb_h_Eff_Period(packet, effect)

    # DWORD Ffb_h_Eff_Cond(const FFB_DATA * Packet, FFB_EFF_COND*  Condition)
    @staticmethod
    def Ffb_h_Eff_Cond(packet, condition):
        return Ffb_h_Eff_Cond(packet, condition)

    # DWORD Ffb_h_DevGain(const FFB_DATA * Packet, BYTE * Gain)
    @staticmethod
    def Ffb_h_DevGain(packet, gain):
        return Ffb_h_DevGain(packet, gain)

    # DWORD Ffb_h_Eff_Envlp(const FFB_DATA * Packet, FFB_EFF_ENVLP*  Envelope)
    @staticmethod
    def Ffb_h_Eff_Envlp(packet, envelope):
        return Ffb_h_Eff_Envlp(packet, envelope)

    # DWORD Ffb_h_EffNew(const FFB_DATA * Packet, FFBEType * Effect)
    @staticmethod
    def Ffb_h_EffNew(packet, effect):
        return Ffb_h_EffNew(packet, effect)

    # DWORD Ffb_h_Eff_Constant(const FFB_DATA * Packet, FFB_EFF_CONSTANT *  ConstantEffect)
    @staticmethod
    def Ffb_h_Eff_Constant(packet, constanteffect):
        return Ffb_h_Eff_Constant(packet, constanteffect)

    @staticmethod
    def ResetState(rid):
        pos = JOYSTICK_POSITION()
        pos.wAxisX = VJoy.GetVJDAxisMax(rid, HID_USAGE_X) >> 1
        pos.wAxisY = VJoy.GetVJDAxisMax(rid, HID_USAGE_Y) >> 1
        pos.wAxisZ = VJoy.GetVJDAxisMax(rid, HID_USAGE_Z) >> 1
        pos.wAxisXRot = VJoy.GetVJDAxisMax(rid, HID_USAGE_RX) >> 1
        pos.wAxisYRot = VJoy.GetVJDAxisMax(rid, HID_USAGE_RY) >> 1
        pos.wAxisZRot = VJoy.GetVJDAxisMax(rid, HID_USAGE_RZ) >> 1

        pos.wSL0 = VJoy.GetVJDAxisMax(rid, HID_USAGE_SL0) >> 1
        pos.wSL1 = VJoy.GetVJDAxisMax(rid, HID_USAGE_SL1) >> 1
        pos.lButtons = 0x00000000
        pos.bHats = 0x8C40

        return VJoy.UpdateVJD(rid, pos) 
