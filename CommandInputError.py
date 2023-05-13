class CommandInputError(Exception):
    """
    Raised when when there is inconsistency in the command line arguments
    and the inputFile, between the number of initial centroids from the
    inputFile and argument k.
    """
    pass