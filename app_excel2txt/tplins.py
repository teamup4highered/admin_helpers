###############################################################################
# Input Templates
###############################################################################

# Import pandas to work with excel data
import pandas as pd

##################################
class TplInsBase:
    """
    Base Class for input templates
    """

    def __init__(self):
        """Initialize an input template
        """
        self.read_input_file()
        
        
    def read_input_file(self):
        """
        Reads input file into pandas dataset
        """
        raise NotImplementedError

################################
class DefaultIn(TplInsBase):
    """
    Default Input Class
    """
    
    def __init__(self, inputfolder, inputfile):
        """Initialize a a input template
        """

        self.read_input_file(inputfolder, inputfile)

    
    def read_input_file(self, inputfolder, inputfile):
        """
        Reads input file into pandas dataset
        """
        # Load spreadsheet
        xl = pd.ExcelFile(inputfolder + '\\' + inputfile)
        self.df = xl.parse(sheet_name=0, header=0)