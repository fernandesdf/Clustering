# 2022-2023 Programacao 2 LTI
# Grupo 031
# 53481 Diogo Alexandre Fernandes Valente
# 54967 Diogo Miguel dos Santos Fernandes

class CommandInputError(Exception):
    """
    Raised when when there is inconsistency in the command line arguments
    and the inputFile, between the number of initial centroids from the
    inputFile and argument k.
    """
    pass