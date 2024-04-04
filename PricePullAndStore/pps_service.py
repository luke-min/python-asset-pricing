# STANDARD LIB
from collections import OrderedDict
import pandas as pd
import numpy as np

# PROJECT LIB
from base_service_layer import BaseServiceLayer



class PPSService(BaseServiceLayer):
    def __init__(self, logger, options):
        super(PPSService, self).__init__(logger)
        self.options = options
        self.reporter = data_collection.DataCollector()

    def get_version(self):
        return "0.0.0"

    def get_supported_args(self, **kwargs):
        """
        Get all arguments supported by service.

        Set default values and clean up data types here.
        """
        args = OrderedDict()

        args["start_date"] = kwargs.get("start_date", None)
        args["end_date"] = kwargs.get("end_date", None)
        tickers = kwargs.get("tickers", None)
        tickers = tickers.split(";")
        args["tickers"] = tickers

        unspported_args = []
        for k in kwargs:
            if k not in args:
                unspported_args.append(k)
        if unspported_args:
            self.logger.warn("Service does not support {}." "".format(unspported_args))

        return args

    def get_input_prep(self):
        return NotImplementedError

    def execute(self, **kwargs):
        """
        Generic execute, override base method.

        :return: void
        """

        start_date = kwargs["start_date"]
        end_date = kwargs.get("end_date", pd.Timestamp.today())
        tickers = kwargs["tickers"]

        pulled_data = self.execute_calculators(**kwargs)

        return pulled_data

    def execute_calculators(self, **kwargs):
        """
        Delegator for PPS calculator only
        """


