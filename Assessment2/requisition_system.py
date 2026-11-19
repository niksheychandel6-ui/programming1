class Requisition:

    requisition_counter = 10000

    def __init__(self, date, staff_id, staff_name):

        Requisition.requisition_counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.requisition_counter

        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"


print("Requisition System Created")