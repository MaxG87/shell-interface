from pathlib import Path
from unittest import mock

from hypothesis import given
from hypothesis import strategies as st

from butter_backup import __main__ as bb

path_to_config_files = st.text(min_size=1)


def test_no_args_parsing() -> None:
    default_config = bb.DEFAULT_CONFIG
    with mock.patch("sys.argv", ["butter-backup"]):
        config = bb.parse_args()
    assert config == default_config


@given(config=path_to_config_files)
def test_parse_args_returns_passed_file(config: str) -> None:
    with mock.patch("sys.argv", ["butter-backup", "--config", config]):
        parsed_config = bb.parse_args()
    assert Path(config) == parsed_config