import qwiic_pir
from time import sleep
import sys
from tqdm import tqdm


def pir_init():
    pir = qwiic_pir.QwiicPIR()

    if not pir.begin():
        print("[ERROR] Qwiic PIR isn't connected to the system.",
              file=sys.stderr)
        return

    print("[INFO] Waiting 30 secs for PIR to stabilize")
    for _ in tqdm(range(30), "Stabilizing PIR", bar_format="{l_bar}{bar}"):
        sleep(1)
    print("[INFO] Device Stable")

    return pir


if __name__ == '__main__':
    try:
        pir = pir_init()
    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)
