import qwiic_pir
from time import sleep
import sys
from tqdm import tqdm

pir = qwiic_pir.QwiicPIR()

if not pir.begin():
    print("[ERROR] Qwiic PIR isn't connected to the system.",
          file=sys.stderr)
    sys.exit(1)

print("[INFO] Waiting 30 secs for PIR to stabilize")
for _ in tqdm(range(30),
              "[INFO] Stabilizing PIR", bar_format="{l_bar}{bar}"):
    sleep(1)
print("[INFO] Device Stable")
