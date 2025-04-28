# Function to create vCard
def create_vcard(name, phone, email, address):
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""
    return vcard

# Accepting contact details from the user
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")
address = input("Enter Address: ")

# Generate the vCard content
vcard_content = create_vcard(name, phone, email, address)

# Saving to a vCard file
file_name = "contact.vcf"
with open(file_name, "w") as file:
    file.write(vcard_content)

print(f"vCard has been created successfully and saved as {file_name}")
