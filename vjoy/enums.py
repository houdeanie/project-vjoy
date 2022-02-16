from .constants import *

from .c_enum import CEnumeration

class VjdStat(CEnumeration):
	VJD_STAT_OWN = 0	# The  vJoy Device is owned by this application.
	VJD_STAT_FREE = 1	# The  vJoy Device is NOT owned by any application (including this one).
	VJD_STAT_BUSY = 2	# The  vJoy Device is owned by another application. It cannot be acquired by this application.
	VJD_STAT_MISS = 3	# The  vJoy Device is missing. It either does not exist or the driver is down.
	VJD_STAT_UNKN = 4   # Unknown

class FFBEType(CEnumeration): # FFB Effect Type
	# Effect Type
	ET_NONE		=	0	  #    No Force
	ET_CONST	=	1    #    Constant Force
	ET_RAMP		=	2    #    Ramp
	ET_SQR		=	3    #    Square
	ET_SINE		=	4    #    Sine
	ET_TRNGL	=	5    #    Triangle
	ET_STUP		=	6    #    Sawtooth Up
	ET_STDN		=	7    #    Sawtooth Down
	ET_SPRNG	=	8    #    Spring
	ET_DMPR		=	9    #    Damper
	ET_INRT		=	10   #    Inertia
	ET_FRCTN	=	11   #    Friction
	ET_CSTM		=	12   #    Custom Force Data


class FFBPType(CEnumeration): # FFB Packet Type
	# Write
	PT_EFFREP	=  HID_ID_EFFREP	# Usage Set Effect Report
	PT_ENVREP	=  HID_ID_ENVREP	# Usage Set Envelope Report
	PT_CONDREP	=  HID_ID_CONDREP	# Usage Set Condition Report
	PT_PRIDREP	=  HID_ID_PRIDREP	# Usage Set Periodic Report
	PT_CONSTREP	=  HID_ID_CONSTREP	# Usage Set Constant Force Report
	PT_RAMPREP	=  HID_ID_RAMPREP	# Usage Set Ramp Force Report
	PT_CSTMREP	=  HID_ID_CSTMREP	# Usage Custom Force Data Report
	PT_SMPLREP	=  HID_ID_SMPLREP	# Usage Download Force Sample
	PT_EFOPREP	=  HID_ID_EFOPREP	# Usage Effect Operation Report
	PT_BLKFRREP	=  HID_ID_BLKFRREP	# Usage PID Block Free Report
	PT_CTRLREP	=  HID_ID_CTRLREP	# Usage PID Device Control
	PT_GAINREP	=  HID_ID_GAINREP	# Usage Device Gain Report
	PT_SETCREP	=  HID_ID_SETCREP	# Usage Set Custom Force Report

	# Feature
	PT_NEWEFREP	=  HID_ID_NEWEFREP+0x10	# Usage Create New Effect Report
	PT_BLKLDREP	=  HID_ID_BLKLDREP+0x10	# Usage Block Load Report
	PT_POOLREP	=  HID_ID_POOLREP+0x10		# Usage PID Pool Report


class FFBOP(CEnumeration):
	EFF_START	= 1 # EFFECT START
	EFF_SOLO	= 2 # EFFECT SOLO START
	EFF_STOP	= 3 # EFFECT STOP


class FFB_CTRL(CEnumeration):
	CTRL_ENACT		= 1	# Enable all device actuators.
	CTRL_DISACT		= 2	# Disable all the device actuators.
	CTRL_STOPALL	= 3	# Stop All Effects� Issues a stop on every running effect.
	CTRL_DEVRST		= 4	# Device Reset� Clears any device paused condition, enables all actuators and clears all effects from memory.
	CTRL_DEVPAUSE	= 5	# Device Pause� The all effects on the device are paused at the current time step.
	CTRL_DEVCONT	= 6	# Device Continue� The all effects that running when the device was paused are restarted from their last time step.


class FFB_EFFECTS(CEnumeration):
	Constant	= 0x0001
	Ramp		= 0x0002
	Square		= 0x0004
	Sine		= 0x0008
	Triangle	= 0x0010
	Sawtooth_Up = 0x0020
	Sawtooth_Dn = 0x0040
	Spring		= 0x0080
	Damper		= 0x0100
	Inertia		= 0x0200
	Friction	= 0x0400
	Custom		= 0x0800
