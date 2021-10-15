"""Exceptions used by the TrollFactory cli and library."""


class UnmetDependenciesException(Exception):
    """An exception raised when there is an unresolved prop dependency."""


class UnsupportedDatasetException(Exception):
    """An exception raised when a requested dataset is not supported."""


class InvalidGenderException(Exception):
    """An exception raised when a requested gender is not supported."""
