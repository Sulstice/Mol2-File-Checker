_WHITESPACE_REGEX = re.compile(r'\s+')

class ParseError(Exception):
    """Generic 'error occured while parsing' error."""

class MissingColumnError(ParseError):
    """Error raised when one or more required columns are missing.

    Args:
        columns(List[Column|str]): The missing column name(s).
    """
    def __init__(self, columns, msgfmt=u'Missing required column{}: {}'):
        msg = msgfmt.format(
            "s" if len(columns) > 1 else "", ", ".join(
                str(x) for x in columns))
        super(MissingColumnError, self).__init__(msg)

class MissingDataError(ParseError):
    """Error raised when fields in a row are missing required column data.

    Args:
        columnnames(List[str]): The missing column name(s)
        row(int): The row missing data, where 1 is the first row in the file.
    """

    def __init__(self, columnnames, row):
        msg = u"Row {} missing required value{}: {}".format(
            row, "s" if len(columnnames) > 1 else "",
            ", ".join(columnnames))
        super(MissingDataError, self).__init__(msg)


def whitespace_transform(header, index):
    """Default header transform.

    Strips all leading and trailing whitespace. Replaces all adjacent internal
    whitespace characters with single spaces.

    Args:
        header (str): The header to transform
        index (int): The header index (0-based)

    Returns:
        str: The transformed header

    Examples:
        >>> strip_whitespace(' a b\n\t c   \n  \t d  ', 1)
        'a b c d'
    """
    return _WHITESPACE_REGEX.sub(' ', header.strip())
