from enum import Enum


class Type(Enum):
    """ button type """
    PRIMARY = "primary"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"
    INFO = "info"
    DEFAULT = "default"

class Size(Enum):
    """ button size """
    DEFAULT = "default"
    LARGE = "large"
    SMALL = "small"
