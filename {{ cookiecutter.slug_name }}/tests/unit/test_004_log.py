import logging
import os
import pathlib
import sys


def setup_module(module):
    """Make sure {{ cookiecutter.slug_name }} has not been imported

    Because tests are changing dotenv variables in runtime, the project
    could have already been imported.

    The library `pydantic` does not reload settings after inittalization
    (and it shouldn't!)
    """

    import shutil

    for module_dot in [*sys.modules.keys()]:
        if module_dot.startswith("{{ cookiecutter.slug_name }}"):
            del sys.modules[module_dot]

    log_folder = pathlib.Path(".").joinpath("test_log")

    shutil.rmtree(log_folder.as_posix(), ignore_errors=True)

    log_folder.mkdir(exist_ok=False)


def teardown_module(module):
    """"""

    import shutil

    for module_dot in [*sys.modules.keys()]:
        if module_dot.startswith("{{ cookiecutter.slug_name }}"):
            del sys.modules[module_dot]

    log_folder = pathlib.Path(".").joinpath("test_log")

    shutil.rmtree(log_folder.as_posix(), ignore_errors=True)


def test_log(monkeypatch, caplog):

    info_ = "__TEST__: This is information"
    error_ = "__TEST__: This is an error"

    with monkeypatch.context() as patcher:
        patcher.setitem(os.environ, "ENV", "production")
        patcher.setitem(os.environ, "LOG_STORAGE", "test_log")
        import {{ cookiecutter.slug_name }}  # noqa: F401

        {{ cookiecutter.slug_name }}.logger.info(info_)
        {{ cookiecutter.slug_name }}.logger.error(error_)

        logfiles = [
            handler.stream.buffer.name
            for handler in {{ cookiecutter.slug_name }}.logger.handlers
            if isinstance(handler, logging.handlers.RotatingFileHandler)
        ]

        found_err, found_info = False, False
        should_find_err, should_find_info = True, False
        for logfile in logfiles:
            if os.path.isfile(logfile):
                if "trace" in logfile:
                    should_find_err = True
                    should_find_info = True
                else:
                    should_find_err = True
                    should_find_info = False

                with open(logfile, "r") as log_file:
                    for line in log_file.readlines():
                        if error_ in line:
                            found_err = True
                        if info_ in line:
                            found_info = True
                if should_find_err:
                    assert found_err
                if should_find_info:
                    assert found_info
