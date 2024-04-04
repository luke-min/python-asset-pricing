import logging
import sys
import traceback
import optparse

# PROJECT LIB
from pps_settings import YF_TICK_LIST, DEFAULT_START_DT


def init_parser():
    parser = optparse.OptionParser()
    parser.add_option("-t",
                      "--tickers",
                      dset="tickers",
                      action="store",
                      default=YF_TICK_LIST,
                      help="Ticker Symbols to Pull")

    parser.add_option("--sd",
                      "--start_date",
                      dest="start_date",
                      action="store",
                      default=DEFAULT_START_DT,
                      help="Start Date when pulling data")

    parser.add_option("--ed",
                      "--end_date",
                      dest="end_date",
                      action="store",
                      is_optional=True,
                      help="End Date when pulling data")

    parser.add_option("-l",
                      "--log_root",
                      dest="log_root",
                      action="store",
                      is_optional=True,
                      default=None,
                      help="Log root")

    return parser

if __name__ == "__main__":
    parser = init_parser()
    (options, args) = parser.parse_args()

    if options.log_root is None:
        options.log_root = "c:/temp/logs"

    logger = logging.getLogger("pps_log")
    logger.setLevel(logging.DEBUG)

    try:
        with pps_svc.PPSService(logger, options) as svc:
            svc.execute()
        logger.info("COMPLETED calcualtion for PPS Service")

    except RuntimeError:
        logger.error("FAILED calculation: {tb}" "".format(tb=traceback.format_exc()))
        sys.exit(1)