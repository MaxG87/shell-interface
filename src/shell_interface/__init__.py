from importlib import metadata

from .shell_interface import (
    ShellInterfaceError,
    StrPathList,
    pipe_pass_cmd_to_real_cmd,
    run_cmd,
)

__version__ = metadata.version(__name__)
__all__ = ["run_cmd", "ShellInterfaceError", "pipe_pass_cmd_to_real_cmd", "StrPathList"]
