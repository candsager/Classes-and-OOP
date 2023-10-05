import PatientClass as pac
import ProcedureClass as prc

def main():

    patient = pac.Patient(1, "Matt Jones","123 Main St. Waco TX 76706", "254-555-7415","TRUE")
    physical = prc.Procedure("Physical Exam","2/15/2022","Dr. Irvine",250,1)
    mri = prc.Procedure("MRI","2/15/2022","Dr. Hamilton",1500,1)
    ct_scan = prc.Procedure("CT Scan","2/17/2022","Dr. Drey",1200,2)
    charge_total = 0

    print("*** Patient Bill ***")
    print(f"Name: {patient.get_pat_name()}\nAddress: {patient.get_pat_address()}\nPhone: {patient.get_pat_phone()}\n")


    if patient.get_pat_id() == physical.get_pat_id():
        print(f"Procedure: {physical.get_proced_name()}")
        print(f"Date: {physical.get_proced_date()}")
        print(f"Practitioner: {physical.get_pract_name()}")
        print(f"Charge: {physical.get_proced_charge()}\n")

        charge_total += int(physical.get_proced_charge())

        if patient.get_pat_id() == mri.get_pat_id():
            print(f"Procedure: {mri.get_proced_name()}")
            print(f"Date: {mri.get_proced_date()}")
            print(f"Practitioner: {mri.get_pract_name()}")
            print(f"Charge: {mri.get_proced_charge()}\n")

            charge_total += int(mri.get_proced_charge())

            if patient.get_pat_id() == ct_scan.get_pat_id():
                print(f"Procedure: {ct_scan.get_proced_name()}")
                print(f"Date: {ct_scan.get_proced_date()}")
                print(f"Practitioner: {ct_scan.get_pract_name()}")
                print(f"Charge: {ct_scan.get_proced_charge()}\n")

                charge_total += int(ct_scan.get_proced_charge())

    if patient.get_pat_vet_stat() == "TRUE":
        new_charge_total = float(charge_total * .6)
        print(f"Total Charges: ", '$', new_charge_total)
    else:
        print(f"Total Charges: ",'$', charge_total)    


main()