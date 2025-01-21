import csv
import os

# Define the structure of the .field-meta.xml file
def generate_field_meta_xml(label, api_name, field_type, length, required):
    required_value = "true" if required.lower() == "true" else "false"
    if field_type.lower() == 'text':
        xml_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<CustomField xmlns=\"http://soap.sforce.com/2006/04/metadata\">
    <fullName>{api_name}</fullName>
    <externalId>false</externalId>
    <label>{label}</label>
    <length>{length}</length>
    <required>{required_value}</required>
    <trackTrending>false</trackTrending>
    <type>Text</type>
    <unique>false</unique>
</CustomField>
"""
    elif field_type.lower() == 'boolean':
        xml_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<CustomField xmlns=\"http://soap.sforce.com/2006/04/metadata\">
    <fullName>{api_name}</fullName>
    <defaultValue>false</defaultValue>
    <label>{label}</label>
    <trackTrending>false</trackTrending>
    <type>Checkbox</type>
</CustomField>
"""
    return xml_content

# Read the CSV file and generate .field-meta.xml files
def process_csv_and_generate_files(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        
        # Create output directory if it doesn't exist
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        for row in csv_reader:
            label = row['Label']
            api_name = row['API-name']
            field_type = row['Type']
            length = row['Length'] if 'Length' in row else ''
            required = row['Required']

            # Generate XML content
            xml_content = generate_field_meta_xml(label, api_name, field_type, length, required)

            # Write to file
            file_name = os.path.join(output_dir, f"{api_name}.field-meta.xml")
            with open(file_name, mode='w', encoding='utf-8') as xml_file:
                xml_file.write(xml_content)

            print(f"Generated: {file_name}")

# Specify the input CSV file
csv_file = "object-fields.csv"
process_csv_and_generate_files(csv_file)
