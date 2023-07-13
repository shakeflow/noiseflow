import os
import re
import json


env = os.environ.get('CONDA_DEFAULT_ENV')

if env is None:
    env = ''
else:
    env = re.sub('[^a-zA-Z0-9_]', '', env)[0:50]
    
config_path = os.path.abspath(os.path.expanduser(f'~/.noiseflow/config_{env}.json'))    

try:
    from noiseflow.lib import cc_share
    from noiseflow.lib import signal_share
    NOISEFLOW_USE_CPP = True
except:
    NOISEFLOW_USE_CPP = False

os.makedirs(os.path.expanduser('~/.noiseflow'), exist_ok=True)
compile_time_env = {"NOISEFLOW_USE_CPP": NOISEFLOW_USE_CPP}
with open(config_path, 'w') as f:
    json.dump(compile_time_env, f)


from noiseflow.config.rawdata import RawData_Class
from noiseflow.config.rfftdata import RFFTData_Class
from noiseflow.config.corrdata import CorrData_Class
from noiseflow.config.stackdata import StackData_Class

from noiseflow.cc.wrapper import rfft, corr, stack
from noiseflow.client.client import downloader
from noiseflow.signal.wrapper import bandpass, bandstop, lowpass, highpass, detrend, decimate, taper

from noiseflow.utils.load import load_raw, load_rfft, load_corr, load_stack
from noiseflow.utils.timestamp import time_linspace, get_timestamp, get_stack_timestamp


# __all__ = ["cc",
#            "client",
#            "config",
#            "signal",
#            "utils",
#            "tests"]

__version__ = "0.0.9"
