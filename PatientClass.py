class Patient:


    def __init__(self, id, name, address, phone, veteran_status):
        self.__pat_id = id
        self.__pat_name = name
        self.__pat_address = address
        self.__pat_phone = phone
        self.__pat_vet_stat = veteran_status

    def get_pat_id(self):
        return self.__pat_id
    def get_pat_name(self):
        return self.__pat_name
    def get_pat_address(self):
        return self.__pat_address
    def get_pat_phone(self):
        return self.__pat_phone
    def get_pat_vet_stat(self):
        return self.__pat_vet_stat
    


        