# Hooks
import pytest

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print('Step failed: {step}')