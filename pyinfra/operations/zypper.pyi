def repo(
    src,
    baseurl=None,
    present=True,
    description=None,
    enabled=True,
    gpgcheck=True,
    gpgkey=None,
    type="rpm-md",
    _sudo = None,
    _sudo_user = None,
    _use_sudo_login = None,
    _use_sudo_password = None,
    _preserve_sudo_env = None,
    _su_user = None,
    _use_su_login = None,
    _preserve_su_env = None,
    _su_shell = None,
    _doas = None,
    _doas_user = None,
    _shell_executable = None,
    _chdir = None,
    _env = None,
    _success_exit_codes = None,
    _timeout = None,
    _get_pty = None,
    _stdin = None,
    name = None,
    _ignore_errors = None,
    _precondition = None,
    _postcondition = None,
    _on_success = None,
    _on_error = None,
    _parallel = None,
    _run_once = None,
    _serial = None,
):...

def rpm(src, present=True, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def update(_sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def packages(
    packages=None,
    present=True,
    latest=False,
    update=False,
    clean=False,
    extra_global_install_args=None,
    extra_install_args=None,
    extra_global_uninstall_args=None,
    extra_uninstall_args=None,
    _sudo = None,
    _sudo_user = None,
    _use_sudo_login = None,
    _use_sudo_password = None,
    _preserve_sudo_env = None,
    _su_user = None,
    _use_su_login = None,
    _preserve_su_env = None,
    _su_shell = None,
    _doas = None,
    _doas_user = None,
    _shell_executable = None,
    _chdir = None,
    _env = None,
    _success_exit_codes = None,
    _timeout = None,
    _get_pty = None,
    _stdin = None,
    name = None,
    _ignore_errors = None,
    _precondition = None,
    _postcondition = None,
    _on_success = None,
    _on_error = None,
    _parallel = None,
    _run_once = None,
    _serial = None,
):...