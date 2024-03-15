class InvoiceData:

    def __init__(self):
        self.filename = "invoice_data.txt"

    def write_file(self):
        data = "Alves\t50\t160\n"
        data += "Alves\t60\t150\n"
        data += "Alves\t70\t180\n"
        f = open(self.filename, "w")
        f.write(data)

    def read_file(self):
        for line in open(self.filename, "r"):
            print(line.strip()) 

i = InvoiceData()
i.write_file()
i.read_file()

    
