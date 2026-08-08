import os
import pandas as pd
from datetime import datetime

def main():
    ts = datetime.now().strftime("%Y-%M-%D %h:%m:%s")
    print(f"Hello. My name is Inigo Montoya! {ts}")


main()

