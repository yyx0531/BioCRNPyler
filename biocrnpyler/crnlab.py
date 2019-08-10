<<<<<<< HEAD
from .extracts import BasicExtract
=======
#  Copyright (c) 2019, Build-A-Cell. All rights reserved.
#  See LICENSE file in the project root directory for details.

from .txtl import BasicExtract
>>>>>>> ef22af172a089b24caf7c15fe63afb1133e0a3e2
from .mixture import Mixture
from .dna_assembly import DNAassembly
import csv
import libsbml
import warnings

<<<<<<< HEAD
class CRNLab(object):
    '''
    Implements high level modeling akin to experimental TX-TL experiments
    """
    def __init__(self, name):
        self.Mixture = Mixture
        self.name = name
        self.volume = 0
        self.crn = None

    def mixture(self, name, **kwargs):
        """
        Create a Mixture of a given name into the CRNLab object
        Specify the extract and buffer optionally
        Specify extra parameters to be loaded as dictionaries optionally
        """
        extract = kwargs.get('extract')
        buffer = kwargs.get('buffer')
        extract_parameters = kwargs.get('extract_parameters')
        extract_volume = kwargs.get('extract_volume')
        if kwargs.get('mixture_volume'):
            self.volume += kwargs.get('mixture_volume')
        if kwargs.get('final_volume'):
            self.volume = kwargs.get('final_volume')

        if kwargs.get('final_volume') and kwargs.get('mix_volume'):
            raise ValueError('Either set initial volume or the final volume')

<<<<<<< HEAD
        try:
            filename = name + str('.csv')
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                # Read off the parameters
                params = {}
                for row in reader:
                    temp = row[1].replace('.','',1).replace('e','',1).replace('-','',1)
                    if temp.isdigit():
                        params[str(row[0])] = float(row[1])
        except:
            if kwargs.get('parameter_warnings'):
                warnings.warn('{0}.csv does not exist. Mixture will use default parameter files available.'.format(name))
            
        # if extract:
        self.extract(extract, parameters = extract_parameters, volume = extract_volume, **kwargs)
        # if buffer:
        #     self.buffer(extract, parameters = buffer_parameters, volume = buffer_volume, **kwargs)
        return self.Mixture

    def extract(self, name, parameters = {}, volume = 0):
        """
        Create BasicExtract with the given name
        (Searches for the name.csv in the current folder to load parameters)
        Optionally load other parameters as dictionary.
        """
        if volume:
            self.volume += volume
        # Look for extract config file of the given name
        filename = name + str('.csv')
        import csv
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            # Read off the parameters
            params = {}
            for row in reader:
                temp = row[1].replace('.','',1).replace('e','',1).replace('-',
                                                                          '',1)
                if temp.isdigit():
                    params[str(row[0])] = float(row[1])
        if parameters:
            # If manually given
            filename = name + str('.csv')
            import csv
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                # Read off the parameters
                params = {}
                for row in reader:
                    temp = row[1].replace('.','',1).replace('e','',1).replace('-','',1)
                    if temp.isdigit():
                        params[str(row[0])] = float(row[1])
            params = parameters
            extract_mix = BasicExtract(self.name, parameters = params, 
                                        init = initial_concentration_dict, **kwargs)
        else:
            extract_mix = BasicExtract(self.name, init = initial_concentration_dict, **kwargs)
        self.Mixture = extract_mix
        return self.Mixture

<<<<<<< HEAD
   
    def add_dna(self, dna = None, name = "", promoter = "", rbs = "", protein = "", initial_conc ="", final_conc = "", volume = 0):
=======
    def txtl_buffer(self, name ="", components = [], parameters = {}, volume = 0):
        """
        TODO : To be implemented using energy models
        """
        self.name = name
        if volume:
            self.volume += volume
        return

    def add_dna(self, dna = None, name = "", promoter = "", rbs = "",
                protein = "", initial_conc ="", final_conc = "", volume = 0):
>>>>>>> ef22af172a089b24caf7c15fe63afb1133e0a3e2
        if volume:
            self.volume += volume
        if dna:
            self.Mixture.add_components(dna)
        elif name and promoter and rbs and protein and initial_conc:
            if final_conc:
                dna = DNAassembly(name, promoter = promoter, rbs = rbs,
                                  protein = protein, initial_conc = final_conc)
            elif initial_conc:
                dna = DNAassembly(name, promoter = promoter, rbs = rbs,
                                  protein = protein,
                                  initial_conc = initial_conc*volume)
            self.add_dna(dna)
        else:
            raise ValueError('add_dna either needs a DNAassembly object '
                             'OR a name, promoter, rbs, and protein etc.')
        return self.Mixture

    def add_component(self, component):
        self.Mixture.add_components(component)
        return self.Mixture

    def set_volumes(self):
        final_volume = self.volume
        # Not implemented yet
        if final_volume and False:
            print(self.Mixture.crn_species)
            for species in self.Mixture.crn_species:
                # Set the final concentration for all species
                # TODO
                species.initial_concentration = \
                                    species.initial_concentration/final_volume
            self.crn = self.Mixture.compile_crn()
            return self.volume
        else:
            return

<<<<<<< HEAD

    def get_model(self):
=======
    def combine_tubes(self):
>>>>>>> ef22af172a089b24caf7c15fe63afb1133e0a3e2
        self.crn = self.Mixture.compile_crn()
        return self.crn

    def write_sbml_file(self, filename, **kwargs):
        self.set_volumes()
        if self.volume:
            kwargs['volume'] = self.volume
            document, _ = self.crn.generate_sbml_model(**kwargs)
        else:
            document, _ = self.crn.generate_sbml_model(**kwargs)
        if document.getNumErrors():
            warnings.warn('SBML document has errors. It is recommended that you fix them before generating this model.')
        status = libsbml.writeSBML(document, filename)
        if status == libsbml.LIBSBML_OPERATION_SUCCESS:
            print('SBML file written successfully to {0}'.format(filename))
        return document 

    def validate_sbml_generated(self, **kwargs):
        document, _ = self.crn.generate_sbml_model(**kwargs)
        if document.getNumErrors():
            warnings.warn('SBML document has errors. It is recommended that you fix them before generating this model.')
            print('Here are the errors')
            print(document.getErrorLog())
        else:
            print('The SBML model generated is a valid document according to the SBML Level 3 Version 1 specifications. Use sbml.org/validator for further troubleshooting.')


# TODO : 
# Need to test extensively with Parameter class and if its working.
# Need to create more CRNLab examples to create models for other stuff. 
# Try to copy stuff over from MATLAB txtl to implement examples there and recreate the results.  
