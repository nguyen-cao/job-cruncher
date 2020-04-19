import os
import pandas as pd
from skills_ml.storage import FSStore
from skills_ml.datasets.onet_cache import OnetSiteCache
from skills_ml.ontologies.onet import Onet

class ONET():
    selected_occupations = [
        'Computer and Information Research Scientists', 
        'Social Science Research Assistants', 
        'Remote Sensing Scientists and Technologists',
        'Bioinformatics Scientists',
        'Geospatial Information Scientists and Technologists',
        'Survey Researchers',
        'Statisticians',
        'Computer Systems Analysts',
        'Mathematicians',
        'Software Developers, Systems Software',
        'Database Administrators',
        'Database Architects',
        'Database Administrators',
        'Data Warehousing Specialists',
        'Computer Systems Engineers/Architects',
        'Business Intelligence Analysts',
        'Financial Quantitative Analysts',
        'Clinical Data Managers',
        'Information Security Analysts',
        'Clinical Data Managers'
    ]

    def __init__(self):
        file_store = FSStore(path=os.path.realpath('../datasets/onet'))
        onet_cache = OnetSiteCache(storage=file_store)
        self.myonet = Onet(onet_cache=onet_cache)

    def print_stats(self):
        self.myonet.print_summary_stats()

    def find_occupations(self, name):
        if name is None:
            return []
        match_occupations = [occupation for occupation in self.myonet.occupations if name.title() in occupation.name]
        return match_occupations

    def occupations(self, names=None):
        data = []
        matched_ = set()
        columns = ['identifier', 'name', 'description', 'titles']
        selected_occupations = names
        if selected_occupations is None:
            selected_occupations = self.selected_occupations
        for occupation_name in selected_occupations:
            match_occupations = [occupation for occupation in self.myonet.occupations if occupation_name.title() in occupation.name]
            for occupation in match_occupations:
                if not occupation.name in matched_:
                    row = [occupation.identifier, occupation.name, occupation.other_attributes['description'], ','.join(occupation.other_attributes['alternate_titles'])]
                    data.append(row)
                    matched_.add(occupation.identifier)

        df = pd.DataFrame(data, columns=columns)
        return df

    def competencies(self, occupations=None):
        data = []
        columns = ['occupation', 'competency', 'category', 'description']
        selected_occupations = occupations
        if selected_occupations is None:
            selected_occupations = self.selected_occupations
        for occupation in selected_occupations:
            oc = self.myonet.filter_by(lambda edge: occupation.title() in edge.occupation.name)
            for competency in oc.competencies:
                row = [occupation, competency.name, competency.categories[0], competency.other_attributes['competencyText']]
                data.append(row)
        df = pd.DataFrame(data, columns=columns)
        return df

ONet_Manager = ONET()