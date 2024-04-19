from __future__ import print_function
import qwiic_pir
import time
import sys

def run_example():

	print("\nSparkFun Qwiic PIR  Example 2\n")
	my_PIR = qwiic_pir.QwiicPIR()

	if my_PIR.begin() == False:
		print("The Qwiic PIR isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print ("Waiting 30 seconds for PIR to stabilize")
	for i in range(0, 30):
		print(i)
		time.sleep(1)

	print("Device Stable")

	while True:
		if my_PIR.available() is True:
			if my_PIR.object_detected():
				print("Object Detected")
				print("Doing something...")
				sleep(10)
			if my_PIR.object_removed():
				print("Object Removed")
			my_PIR.clear_event_bits()
		time.sleep(0.2)

if __name__ == '__main__':
	try:
		run_example()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 2")
		sys.exit(0)
