
class Procedure:

    def __init__(self, proced_name, proced_date, pract_name, proced_charge, pat_id):
        self.__proced_name = proced_name
        self.__proced_date = proced_date
        self.__pract_name = pract_name
        self.__proced_charge = proced_charge
        self.__pat_id = pat_id

    def get_proced_name(self):
        return self.__proced_name
    
    def get_proced_date(self):
        return self.__proced_date
    
    def get_pract_name(self):
        return self.__pract_name
    
    def get_proced_charge(self):
        return self.__proced_charge
    
    def get_pat_id(self):
        return self.__pat_id
    


