DEVICENAME_STRING			= "vJoy"
NTDEVICE_NAME_STRING		= "/Device/"+DEVICENAME_STRING
SYMBOLIC_NAME_STRING		= "/DosDevices/"+DEVICENAME_STRING
DOS_FILE_NAME				= "//./"+DEVICENAME_STRING
VJOY_INTERFACE				= "Device_"

# Version parts
VER_X_= 0
VER_H_= 2
VER_M_= 1
VER_L_= 8

# Device Attributes
VENDOR_N_ID		= 0x1234
RODUCT_N_ID	= 0xBEAD
ERSION_N	= (VER_L_ + 0x10*VER_M_ + 0x100*VER_H_ + 0x1000*VER_X_)

# Device Strings
VENDOR_STR_ID		= "Shaul Eizikovich"
PRODUCT_STR_ID		= "vJoy - Virtual Joystick"

# Function codes;

F_LOAD_POSITIONS	= 0x910
F_GETATTRIB			= 0x911
F_GET_FFB_DATA		= 0x912
F_SET_FFB_STAT		= 0x913
F_GET_FFB_STAT		= 0x916
F_GET_DEV_INFO      = 0x917
F_IS_DRV_FFB_CAP	= 0x918
F_IS_DRV_FFB_EN		= 0x919
F_GET_DRV_DEV_MAX	= 0x91A
F_GET_DRV_DEV_EN	= 0x91B
F_IS_DEV_FFB_START	= 0x91C
F_GET_DEV_STAT		= 0x91D
F_GET_DRV_INFO		= 0x91E
F_RESET_DEV			= 0x91F
F_GET_POSITIONS		= 0x920


# HID Descriptor definitions - Axes
HID_USAGE_X		= 0x30
HID_USAGE_Y		= 0x31
HID_USAGE_Z		= 0x32
HID_USAGE_RX	= 0x33
HID_USAGE_RY	= 0x34
HID_USAGE_RZ	= 0x35
HID_USAGE_SL0	= 0x36
HID_USAGE_SL1	= 0x37
HID_USAGE_WHL	= 0x38
HID_USAGE_POV	= 0x39

# HID Descriptor definitions - FFB Effects
HID_USAGE_CONST = 0x26    #    Usage ET Constant Force
HID_USAGE_RAMP  = 0x27    #    Usage ET Ramp
HID_USAGE_SQUR  = 0x30    #    Usage ET Square
HID_USAGE_SINE  = 0x31    #    Usage ET Sine
HID_USAGE_TRNG  = 0x32    #    Usage ET Triangle
HID_USAGE_STUP  = 0x33    #    Usage ET Sawtooth Up
HID_USAGE_STDN  = 0x34    #    Usage ET Sawtooth Down
HID_USAGE_SPRNG = 0x40    #    Usage ET Spring
HID_USAGE_DMPR  = 0x41    #    Usage ET Damper
HID_USAGE_INRT  = 0x42    #    Usage ET Inertia
HID_USAGE_FRIC  = 0x43    #    Usage ET Friction


# HID Descriptor definitions - FFB Report IDs
HID_ID_STATE	= 0x02	# Usage PID State report
HID_ID_EFFREP	= 0x01	# Usage Set Effect Report
HID_ID_ENVREP	= 0x02	# Usage Set Envelope Report
HID_ID_CONDREP	= 0x03	# Usage Set Condition Report
HID_ID_PRIDREP	= 0x04	# Usage Set Periodic Report
HID_ID_CONSTREP	= 0x05	# Usage Set Constant Force Report
HID_ID_RAMPREP	= 0x06	# Usage Set Ramp Force Report
HID_ID_CSTMREP	= 0x07	# Usage Custom Force Data Report
HID_ID_SMPLREP	= 0x08	# Usage Download Force Sample
HID_ID_EFOPREP	= 0x0A	# Usage Effect Operation Report
HID_ID_BLKFRREP	= 0x0B	# Usage PID Block Free Report
HID_ID_CTRLREP	= 0x0C	# Usage PID Device Control
HID_ID_GAINREP	= 0x0D	# Usage Device Gain Report
HID_ID_SETCREP	= 0x0E	# Usage Set Custom Force Report
HID_ID_NEWEFREP	= 0x01	# Usage Create New Effect Report
HID_ID_BLKLDREP	= 0x02	# Usage Block Load Report
HID_ID_POOLREP	= 0x03	# Usage PID Pool Report