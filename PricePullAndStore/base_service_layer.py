# STANDARD LIB
import abc

class BaseServiceLayer(object):
    def __init__(self, logger):
        self.logger = logger

    @abc.abstractmethod
    def get_version(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def get_run_id(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def get_input_prep(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def execute_calculators(self, **kwargs):
        raise NotImplementedError