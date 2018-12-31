

# Import pandas to work with excel data
import pandas as pd

# Import pluggable modules
import configs
import tplins
import tplouts

class E2T: 
    """The main excel2txt class.
    """
    # folder containing input file
    inputfolder: str              
    # input file name     
    inputfile: str
    # class that defines input template
    inputtpl: tplins.DefaultIn
    # folder containing output file
    outputfolder: str
    # output file name
    outputfile: str
    # class that defines output template
    outputpl: tplouts.DefaultOut

    def __init__(self, config):
        """Initialize a new instance using the given configuration."""
        self.inputfolder = config['inputfolder']
        self.inputfile = config['inputfile']
        self.inputtpl = config['inputtpl']
        self.outputfolder = config['outputfolder']
        self.outputfile = config['outputfile']
        self.outputtpl = config['outputtpl']
        


    ##########################################################
    def run_convert(self):
        """ run the converstion excel -> txt"""
        myinclass = getattr(tplins, self.inputtpl)(self.inputfolder, self.inputfile)
        myindata = myinclass.df
        print(myindata.shape)

        myoutclass = getattr(tplouts, self.outputtpl)(self.outputfolder, self.outputfile, myindata)
        myoutclass.write_output_file()

###################################
def SelectConfig():
    """ Select the Configuration for this run"""
    config = configs.DefaultConfig
    return config

###################################
def run():
    """Run the E2T app"""

    config = SelectConfig()
    myE2T = E2T(config)
    myE2T.run_convert()

#########################################
if __name__ == '__main__':
    """ main """
    run()

