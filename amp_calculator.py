"""
Power = Watt
Current = Ampare (I)

R = Resistence (ohm)
W = Watt
I = Current (Ampare)

R = V / I
W = V * I
I = W / V
"""


V = int(input("Enter the voltage: "))
W = int(input("Enter the watt: "))

def electricity(v,w):
    A = w/v
    ohm = v/A
    pf = 0.8
    ohm =  f"{ohm:.2f}"
    I = f"{A:.2f}"
    I = float(I)
    watt = w*pf
    print()

    print(f"PF: {pf}")
    print(f"Voltage: {v} V")
    print(f"Watt before PF: {w} W")
    print(f"Watt after PF: {watt} VA")
    print(f"Current: {I} A")
    print(f"Resistence: {ohm} Ohm")
    
    if I < 6:
    	print(f"Bracker size: 6A")
    elif I > 6 and I < 10:
    	print(f"Bracker size: 10A")
    elif I > 10 and I < 16:
    	print(f"Bracker size: 16A")
    elif I > 16 and I < 20:
    	print(f"Bracker size: 20A")
    elif I > 20 and I < 25:
    	print(f"Bracker size: 25A")
    elif I > 25 and I < 32:
    	print(f"Bracker size: 32A")
    elif I > 32 and I < 40:
    	print(f"Bracker size: 40A")
    elif I > 40 and I < 50:
    	print(f"Bracker size: 50A")
    elif I > 50 and I < 63:
    	print(f"Bracker size: 63A")
    
electricity(V,W)