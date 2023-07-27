from fileformats.core.mixin import WithMagicNumber
from fileformats.generic import File


class Data(File):
    iana_mime = None


class TextMatrix(Data):
    ext = ".mat"
    binary = False


class RData(WithMagicNumber, Data):
    """Data-file created by the R statistical package"""
    ext = ".rData"
    binary = True
    magic_number = b"RDA1"


class MatFile(WithMagicNumber, Data):
    """MATLAB Mat-File (https://au.mathworks.com/help/matlab/import_export/mat-file-versions.html)"""
    ext = ".mat"
    magic_number = "4D41544C"
    binary = True


class DatFile(Data):
    """Generic binary data file"""
    binary = True
    ext = ".dat"


class Hdf5(WithMagicNumber, Data):
    """Hierarchical Data Format (HDF) Version 5

    An open source file format that supports large, complex, heterogeneous data.
    HDF5 uses a "file directory" like structure that allows you to organize data within
    the file in many different structured ways, as you might do with files on your computer."""

    binary = True
    ext = ".h5"
    magic_number = "894844460d0a1a0a01"
