from eol_matrix.runtimes.python import PythonVersion

from .base import BaseRuntimeVersion

RUNTIME_VERSION = {"python": PythonVersion}


def get_runtime(runtime: str) -> type[BaseRuntimeVersion]:
    try:
        return RUNTIME_VERSION[runtime]
    except KeyError:
        raise NotImplementedError(f"`{runtime}` not implemented!")
