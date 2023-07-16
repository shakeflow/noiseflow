import json
import os
import re

env = os.environ.get("CONDA_DEFAULT_ENV")

if env is None:
    env = ""
else:
    env = re.sub("[^a-zA-Z0-9_]", "", env)[0:50]

config_path = os.path.abspath(os.path.expanduser(f"~/.noiseflow/config_{env}.json"))

try:
    from noiseflow.lib import cc_share, signal_share  # noqa: E402

    NOISEFLOW_USE_CPP = True
except Exception:
    NOISEFLOW_USE_CPP = False

os.makedirs(os.path.expanduser("~/.noiseflow"), exist_ok=True)
compile_time_env = {"NOISEFLOW_USE_CPP": NOISEFLOW_USE_CPP}
with open(config_path, "w") as f:
    json.dump(compile_time_env, f)


from noiseflow.cc.wrapper import corr, rfft, stack  # noqa: E402
from noiseflow.client.client import downloader  # noqa: E402
from noiseflow.config.corrdata import CorrData_Class  # noqa: E402
from noiseflow.config.rawdata import RawData_Class  # noqa: E402
from noiseflow.config.rfftdata import RFFTData_Class  # noqa: E402
from noiseflow.config.stackdata import StackData_Class  # noqa: E402
from noiseflow.signal.wrapper import (
    bandpass,
    bandstop,
    decimate,
    detrend,
    highpass,
    lowpass,
    taper,
)
from noiseflow.utils.load import (  # noqa: E402
    load_corr,
    load_raw,
    load_rfft,
    load_stack,
)
from noiseflow.utils.timestamp import (  # noqa: E402
    get_stack_timestamp,
    get_timestamp,
    time_linspace,
)

__all__ = ["cc", "client", "config", "signal", "utils", "tests"]

__version__ = "0.1.0"
