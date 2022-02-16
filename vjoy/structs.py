from ctypes import * 
from .enums import *

class JOYSTICK_POSITION(Structure):
    _fields_ = [
        ("bDevice", c_uint8),	# Index of device. 1-based.
        ("wThrottle", c_long),
        ("wRudder", c_long),
        ("wAileron", c_long),
        ("wAxisX", c_long),
        ("wAxisY", c_long),
        ("wAxisZ", c_long),
        ("wAxisXRot", c_long),
        ("wAxisYRot", c_long),
        ("wAxisZRot", c_long),
        ("wSL0", c_long),
        ("wSL1", c_long),
        ("wWheel", c_long),
        ("wAxisVX", c_long),
        ("wAxisVY", c_long),
        ("wAxisVZ", c_long),
        ("wAxisVBRX", c_long),
        ("wAxisVBRY", c_long),
        ("wAxisVBRZ", c_long),
        ("lButtons", c_long),	# 32 buttons: 0x00000001 means button1 is pressed, 0x80000000 -> button32 is pressed
        ("bHats", c_uint32),		# Lower 4 bits: HAT switch or 16-bit of continuous HAT switch
        ("bHatsEx1", c_uint32),	# 16-bit of continuous HAT switch
        ("bHatsEx2", c_uint32),	# 16-bit of continuous HAT switch
        ("bHatsEx3", c_uint32),	# 16-bit of continuous HAT switch
    ]

class JOYSTICK_POSITION_V2(Structure):
    _fields_ = [
        #/ JOYSTICK_POSITION
        ("bDevice", c_uint8),	# Index of device. 1-based.
        ("wThrottle", c_long),
        ("wRudder", c_long),
        ("wAileron", c_long),
        ("wAxisX", c_long),
        ("wAxisY", c_long),
        ("wAxisZ", c_long),
        ("wAxisXRot", c_long),
        ("wAxisYRot", c_long),
        ("wAxisZRot", c_long),
        ("wSlider", c_long),
        ("wDial", c_long),
        ("wWheel", c_long),
        ("wAxisVX", c_long),
        ("wAxisVY", c_long),
        ("wAxisVZ", c_long),
        ("wAxisVBRX", c_long),
        ("wAxisVBRY", c_long),
        ("wAxisVBRZ", c_long),
        ("lButtons", c_long),	# 32 buttons: 0x00000001 means button1 is pressed, 0x80000000 -> button32 is pressed
        ("bHats", c_uint32),		# Lower 4 bits: HAT switch or 16-bit of continuous HAT switch
        ("bHatsEx1", c_uint32),	# Lower 4 bits: HAT switch or 16-bit of continuous HAT switch
        ("bHatsEx2", c_uint32),	# Lower 4 bits: HAT switch or 16-bit of continuous HAT switch
        ("bHatsEx3", c_uint32),	# Lower 4 bits: HAT switch or 16-bit of continuous HAT switch ("lButtonsEx1", c_long), # Buttons 33-64
        
        #/ JOYSTICK_POSITION_V2 Extenssion
        ("lButtonsEx1", c_long), # Buttons 33-64
        ("lButtonsEx2", c_long), # Buttons 65-96
        ("lButtonsEx3", c_long), # Buttons 97-12
    ]
 
class DEVCTRLS(Structure): 
    _fields_ = [ 
        ("Init", c_bool), 
        ("Rudder", c_bool), 
        ("Aileron", c_bool), 
        ("AxisX", c_bool), 
        ("AxisY", c_bool), 
        ("AxisZ", c_bool), 
        ("AxisXRot", c_bool), 
        ("AxisYRot", c_bool), 
        ("AxisZRot", c_bool), 
        ("Slider", c_bool), 
        ("Dial", c_bool), 
        ("Wheel", c_bool), 
        ("AxisVX", c_bool), 
        ("AxisVY", c_bool), 
        ("AxisVZ", c_bool), 
        ("AxisVBRX", c_bool), 
        ("AxisVBRY", c_bool), 
        ("AxisVBRZ", c_bool), 
        ("nButtons", c_int),	 
        ("nDescHats", c_int), 
        ("nContHats", c_int), 
    ] 
 
class DeviceStat(Structure): 
    _fields_ = [ 
        ("h", c_void_p),								# Handle to the PDO interface that represents the virtual device 
        ("stat", VjdStat),							# Status of the device 
        ("position", JOYSTICK_POSITION_V2),			# Current Position of the device
        ("hDeviceNotifyHandle", c_void_p),			# Device Notification Handle 
        ("DeviceControls", DEVCTRLS),				# Structure Holding the data about the device's controls 
        ("pPreParsedData", c_void_p),	# structure contains a top-level collection's preparsed data. 
    ] 

class DEV_INFO(Structure):
    _fields_ = [
        ("DeviceID", c_uint8),		# Device ID: Valid values are 1-16
        ("nImplemented", c_uint8),	# Number of implemented device: Valid values are 1-16
        ("isImplemented", c_uint8),	# Is this device implemented?
        ("MaxDevices", c_uint8),		# Maximum number of devices that may be implemented (16)
        ("DriverFFB", c_uint8),		# Does this driver support FFB (False)
        ("DeviceFFB", c_uint8),		# Does this device support FFB (False)
    ] 
 
class FFB_DATA(Structure):
    _fields_ = [ 
        ("size", c_ulong),
        ("cmd", c_ulong),
        ("data", POINTER(c_uint8)),
    ] 
 
class FFB_EFF_CONSTANT(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("Magnitude", c_long), 			  # Constant force magnitude: 	-10000 - 10000 
    ] 
 
class FFB_EFF_RAMP(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("Start", c_long),             # The Normalized magnitude at the start of the effect (-10000 - 10000) 
        ("End", c_long),               # The Normalized magnitude at the end of the effect	(-10000 - 10000) 
    ] 
 
class FFB_EFF_REPORT(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("EffectType", FFBEType), 
        ("Duration", c_uint16),# Value in milliseconds. 0xFFFF means infinite 
        ("TrigerRpt", c_uint16), 
        ("SamplePrd", c_uint16), 
        ("Gain", c_uint8), 
        ("TrigerBtn", c_uint8), 
        ("Polar", c_bool), # How to interpret force direction Polar (0-360�) or Cartesian (X,Y) 
        ("DirX", c_uint8), # X direction: Positive values are To the right of the center (X); Negative are Two's complement 
        ("DirY", c_uint8), # Y direction: Positive values are below the center (Y); Negative are Two's complement 
    ] 

FFB_EFF_CONST = FFB_EFF_REPORT

class FFB_EFF_OP(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("EffectOp", FFBOP), 
        ("LoopCount", c_uint8), 
    ] 
 
class FFB_EFF_PERIOD(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("Magnitude", c_uint32),			# Range: 0 - 10000 
        ("Offset", c_long),				# Range: �10000 - 10000 
        ("Phase", c_uint32),				# Range: 0 - 35999 
        ("Period", c_uint32),				# Range: 0 - 32767 
    ] 
 
class FFB_EFF_COND(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("isY", c_bool), 
        ("CenterPointOffset", c_long), # CP Offset:  Range -�10000 �- 10000 
        ("PosCoeff", c_long), # Positive Coefficient: Range -�10000 �- 10000 
        ("NegCoeff", c_long), # Negative Coefficient: Range -�10000 �- 10000 
        ("PosSatur", c_uint32), # Positive Saturation: Range 0 � 10000 
        ("NegSatur", c_uint32), # Negative Saturation: Range 0 � 10000 
        ("DeadBand", c_long), # Dead Band: : Range 0 � 1000 
    ] 
 
class FFB_EFF_ENVLP(Structure): 
    _fields_ = [ 
        ("EffectBlockIndex", c_uint8), 
        ("AttackLevel", c_uint32),   # The Normalized magnitude of the stating point: 0 - 10000 
        ("FadeLevel", c_uint32),	   # The Normalized magnitude of the stopping point: 0 - 10000 
        ("AttackTime", c_uint32),	   # Time of the attack: 0 - 4294967295 
        ("FadeTime", c_uint32),	   # Time of the fading: 0 - 4294967295 
    ] 