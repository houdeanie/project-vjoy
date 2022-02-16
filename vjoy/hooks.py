from ctypes import *
import os

from .constants import *
from .enums import *
from .structs import *

DLL_FILENAME = "vJoyInterface.dll"

DLL_FILEPATH = os.path.join(os.path.dirname(__file__), DLL_FILENAME)

vj = cdll.LoadLibrary(DLL_FILEPATH)
# SHORT GetvJoyVersion(void)
GetvJoyVersion = vj.GetvJoyVersion
GetvJoyVersion.restype = c_short
GetvJoyVersion.argtypes = []

# BOOL vJoyEnabled(void)
vJoyEnabled = vj.vJoyEnabled
vJoyEnabled.restype = c_bool
vJoyEnabled.argtypes = []

# PVOID GetvJoyProductString(void)
GetvJoyProductString = vj.GetvJoyProductString
GetvJoyProductString.restype = c_wchar_p
GetvJoyProductString.argtypes = []

# PVOID GetvJoyManufacturerString(void)
GetvJoyManufacturerString = vj.GetvJoyManufacturerString
GetvJoyManufacturerString.restype = c_wchar_p
GetvJoyManufacturerString.argtypes = []

# PVOID GetvJoySerialNumberString(void)
GetvJoySerialNumberString = vj.GetvJoySerialNumberString
GetvJoySerialNumberString.restype = c_wchar_p
GetvJoySerialNumberString.argtypes = []

# VJOYINTERFACE_API enum VjdStat	__cdecl	GetVJDStatus(UINT rID);			// Get the status of the specified vJoy Device.
GetVJDStatus = vj.GetVJDStatus
GetVJDStatus.restype = VjdStat
GetVJDStatus.argtypes = [c_uint]

# BOOL DriverMatch(WORD * DllVer, WORD * DrvVer)
DriverMatch = vj.DriverMatch
DriverMatch.restype = c_bool
DriverMatch.argtypes = [POINTER(c_uint16),POINTER(c_uint16)]

# VOID RegisterRemovalCB(RemovalCB cb, PVOID data)
# RegisterRemovalCB = vj.RegisterRemovalCB
# RegisterRemovalCB.restype = None
# RegisterRemovalCB.argtypes = [RemovalCB,c_void_p]

# BOOL vJoyFfbCap(BOOL * Supported)
vJoyFfbCap = vj.vJoyFfbCap
vJoyFfbCap.restype = c_bool
vJoyFfbCap.argtypes = [POINTER(c_bool)]

# BOOL GetvJoyMaxDevices(int * n)
GetvJoyMaxDevices = vj.GetvJoyMaxDevices
GetvJoyMaxDevices.restype = c_bool
GetvJoyMaxDevices.argtypes = [POINTER(c_int)]

# BOOL GetNumberExistingVJD(int * n)
GetNumberExistingVJD = vj.GetNumberExistingVJD
GetNumberExistingVJD.restype = c_bool
GetNumberExistingVJD.argtypes = [POINTER(c_int)]

# int GetVJDButtonNumber(UINT rID)
GetVJDButtonNumber = vj.GetVJDButtonNumber
GetVJDButtonNumber.restype = c_int
GetVJDButtonNumber.argtypes = [c_uint]

# int GetVJDDiscPovNumber(UINT rID)
GetVJDDiscPovNumber = vj.GetVJDDiscPovNumber
GetVJDDiscPovNumber.restype = c_int
GetVJDDiscPovNumber.argtypes = [c_uint]

# int GetVJDContPovNumber(UINT rID)
GetVJDContPovNumber = vj.GetVJDContPovNumber
GetVJDContPovNumber.restype = c_int
GetVJDContPovNumber.argtypes = [c_uint]

# BOOL GetVJDAxisExist(UINT rID, UINT Axis)
GetVJDAxisExist = vj.GetVJDAxisExist
GetVJDAxisExist.restype = c_bool
GetVJDAxisExist.argtypes = [c_uint,c_uint]

# BOOL GetVJDAxisMax(UINT rID, UINT Axis, LONG * Max)
GetVJDAxisMax = vj.GetVJDAxisMax
GetVJDAxisMax.restype = c_bool
GetVJDAxisMax.argtypes = [c_uint,c_uint,POINTER(c_long)]

# BOOL GetVJDAxisMin(UINT rID, UINT Axis, LONG * Min)
GetVJDAxisMin = vj.GetVJDAxisMin
GetVJDAxisMin.restype = c_bool
GetVJDAxisMin.argtypes = [c_uint,c_uint,POINTER(c_long)]

# BOOL isVJDExists(UINT rID)
isVJDExists = vj.isVJDExists
isVJDExists.restype = c_bool
isVJDExists.argtypes = [c_uint]

# int GetOwnerPid(UINT rID)
GetOwnerPid = vj.GetOwnerPid
GetOwnerPid.restype = c_int
GetOwnerPid.argtypes = [c_uint]

# BOOL AcquireVJD(UINT rID)
AcquireVJD = vj.AcquireVJD
AcquireVJD.restype = c_bool
AcquireVJD.argtypes = [c_uint]

# VOID RelinquishVJD(UINT rID)
RelinquishVJD = vj.RelinquishVJD
RelinquishVJD.restype = None
RelinquishVJD.argtypes = [c_uint]

# BOOL UpdateVJD(UINT rID, PVOID pData)
UpdateVJD = vj.UpdateVJD
UpdateVJD.restype = c_bool
UpdateVJD.argtypes = [c_uint, POINTER(JOYSTICK_POSITION)]

# BOOL ResetVJD(UINT rID)
ResetVJD = vj.ResetVJD
ResetVJD.restype = c_bool
ResetVJD.argtypes = [c_uint]

# VOID ResetAll(void)
ResetAll = vj.ResetAll
ResetAll.restype = None
ResetAll.argtypes = []

# BOOL ResetButtons(UINT rID);		// Reset all buttons (To 0)
ResetButtons = vj.ResetButtons
ResetButtons.restype = c_bool
ResetButtons.argtypes = [c_uint]

# BOOL ResetPovs(UINT rID);		// Reset all POV Switches (To -1)
ResetPovs = vj.ResetPovs
ResetPovs.restype = c_bool
ResetPovs.argtypes = [c_uint]

# BOOL SetAxis(LONG Value, UINT rID, UINT Axis)
SetAxis = vj.SetAxis
SetAxis.restype = c_bool
SetAxis.argtypes = [c_long,c_uint,c_uint]

# BOOL SetBtn(BOOL Value, UINT rID, UCHAR nBtn)
SetBtn = vj.SetBtn
SetBtn.restype = c_bool
SetBtn.argtypes = [c_bool,c_uint,c_uint8]

# BOOL SetDiscPov(int Value, UINT rID, UCHAR nPov)
SetDiscPov = vj.SetDiscPov
SetDiscPov.restype = c_bool
SetDiscPov.argtypes = [c_int,c_uint,c_uint8]

# BOOL SetContPov(DWORD Value, UINT rID, UCHAR nPov)
SetContPov = vj.SetContPov
SetContPov.restype = c_bool
SetContPov.argtypes = [c_uint32,c_uint,c_uint8]

# FFBEType FfbGetEffect()
FfbGetEffect = vj.FfbGetEffect
FfbGetEffect.restype = FFBEType
FfbGetEffect.argtypes = []

# VOID FfbRegisterGenCB(FfbGenCB cb, PVOID data)
# FfbRegisterGenCB = vj.FfbRegisterGenCB
# FfbRegisterGenCB.restype = None
# FfbRegisterGenCB.argtypes = [FfbGenCB,c_void_p]

# BOOL FfbStart(UINT rID)
FfbStart = vj.FfbStart
FfbStart.restype = c_bool
FfbStart.argtypes = [c_uint]

# VOID FfbStop(UINT rID)
FfbStop = vj.FfbStop
FfbStop.restype = None
FfbStop.argtypes = [c_uint]

# BOOL IsDeviceFfb(UINT rID)
IsDeviceFfb = vj.IsDeviceFfb
IsDeviceFfb.restype = c_bool
IsDeviceFfb.argtypes = [c_uint]

# BOOL IsDeviceFfbEffect(UINT rID, UINT Effect)
IsDeviceFfbEffect = vj.IsDeviceFfbEffect
IsDeviceFfbEffect.restype = c_bool
IsDeviceFfbEffect.argtypes = [c_uint,c_uint]

# DWORD Ffb_h_DeviceID(const FFB_DATA * Packet, int *DeviceID)
Ffb_h_DeviceID = vj.Ffb_h_DeviceID
Ffb_h_DeviceID.restype = c_uint32
Ffb_h_DeviceID.argtypes = [POINTER(FFB_DATA),POINTER(c_int)]

# DWORD Ffb_h_Type(const FFB_DATA * Packet, FFBPType *Type)
Ffb_h_Type = vj.Ffb_h_Type
Ffb_h_Type.restype = c_uint32
Ffb_h_Type.argtypes = [POINTER(FFB_DATA),POINTER(FFBPType)]

# DWORD Ffb_h_Packet(const FFB_DATA * Packet, WORD *Type, int *DataSize, BYTE *Data[])
Ffb_h_Packet = vj.Ffb_h_Packet
Ffb_h_Packet.restype = c_uint32
Ffb_h_Packet.argtypes = [POINTER(FFB_DATA),POINTER(c_uint16),POINTER(c_int),POINTER(c_uint8)]

# DWORD Ffb_h_EBI(const FFB_DATA * Packet, int *Index)
Ffb_h_EBI = vj.Ffb_h_EBI
Ffb_h_EBI.restype = c_uint32
Ffb_h_EBI.argtypes = [POINTER(FFB_DATA),POINTER(c_int)]

# DWORD Ffb_h_Eff_Report(const FFB_DATA * Packet, FFB_EFF_REPORT*  Effect)
Ffb_h_Eff_Report = vj.Ffb_h_Eff_Report
Ffb_h_Eff_Report.restype = c_uint32
Ffb_h_Eff_Report.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_REPORT)]

# DWORD Ffb_h_Eff_Const(const FFB_DATA * Packet, FFB_EFF_CONST*  Effect)
# Ffb_h_Eff_Const = vj.Ffb_h_Eff_Const
# Ffb_h_Eff_Const.restype = c_uint32
# Ffb_h_Eff_Const.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_CONST)]

# DWORD Ffb_h_Eff_Ramp(const FFB_DATA * Packet, FFB_EFF_RAMP*  RampEffect)
Ffb_h_Eff_Ramp = vj.Ffb_h_Eff_Ramp
Ffb_h_Eff_Ramp.restype = c_uint32
Ffb_h_Eff_Ramp.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_RAMP)]

# DWORD Ffb_h_EffOp(const FFB_DATA * Packet, FFB_EFF_OP*  Operation)
Ffb_h_EffOp = vj.Ffb_h_EffOp
Ffb_h_EffOp.restype = c_uint32
Ffb_h_EffOp.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_OP)]

# DWORD Ffb_h_DevCtrl(const FFB_DATA * Packet, FFB_CTRL *  Control)
Ffb_h_DevCtrl = vj.Ffb_h_DevCtrl
Ffb_h_DevCtrl.restype = c_uint32
Ffb_h_DevCtrl.argtypes = [POINTER(FFB_DATA),POINTER(FFB_CTRL)]

# DWORD Ffb_h_Eff_Period(const FFB_DATA * Packet, FFB_EFF_PERIOD*  Effect)
Ffb_h_Eff_Period = vj.Ffb_h_Eff_Period
Ffb_h_Eff_Period.restype = c_uint32
Ffb_h_Eff_Period.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_PERIOD)]

# DWORD Ffb_h_Eff_Cond(const FFB_DATA * Packet, FFB_EFF_COND*  Condition)
Ffb_h_Eff_Cond = vj.Ffb_h_Eff_Cond
Ffb_h_Eff_Cond.restype = c_uint32
Ffb_h_Eff_Cond.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_COND)]

# DWORD Ffb_h_DevGain(const FFB_DATA * Packet, BYTE * Gain)
Ffb_h_DevGain = vj.Ffb_h_DevGain
Ffb_h_DevGain.restype = c_uint32
Ffb_h_DevGain.argtypes = [POINTER(FFB_DATA),POINTER(c_uint8)]

# DWORD Ffb_h_Eff_Envlp(const FFB_DATA * Packet, FFB_EFF_ENVLP*  Envelope)
Ffb_h_Eff_Envlp = vj.Ffb_h_Eff_Envlp
Ffb_h_Eff_Envlp.restype = c_uint32
Ffb_h_Eff_Envlp.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_ENVLP)]

# DWORD Ffb_h_EffNew(const FFB_DATA * Packet, FFBEType * Effect)
Ffb_h_EffNew = vj.Ffb_h_EffNew
Ffb_h_EffNew.restype = c_uint32
Ffb_h_EffNew.argtypes = [POINTER(FFB_DATA),POINTER(FFBEType)]

# DWORD Ffb_h_Eff_Constant(const FFB_DATA * Packet, FFB_EFF_CONSTANT *  ConstantEffect)
Ffb_h_Eff_Constant = vj.Ffb_h_Eff_Constant
Ffb_h_Eff_Constant.restype = c_uint32
Ffb_h_Eff_Constant.argtypes = [POINTER(FFB_DATA),POINTER(FFB_EFF_CONSTANT)]



