
###############################################################################
# Output Templates
###############################################################################

# Import pandas to work with excel data
import pandas as pd

class TplOutsBase:
    """
    Base class for output template
    """

    def __init__(self) -> None:
        """Initialize an output template
        """
        self.format_comment = 'general super class'
        
    def write_output_file(self) -> None:
        """
        Writes the output file
        """
        raise NotImplementedError


class DefaultOut(TplOutsBase):
    """
    Deveopment ouput class
    """
    def __init__(self, outputfolder, outputfile, dataframe):
        """Initialize a a input template
        """
        self.df = dataframe
        self.outputfile = outputfolder + '\\' + outputfile

    
    def write_output_file(self):
        """
        Reads input file into pandas dataset
        """
        # Load spreadsheet
        self.df.to_csv(self.outputfile)