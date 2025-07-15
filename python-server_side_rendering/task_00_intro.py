import os

def generate_invitations(template, attendees):
    # Check the template type
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check the type of attendee list
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check that the template is not empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check that the list is not empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # For everyone present, we generate a file
    for idx, person in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            value = value if value else "N/A"
            content = content.replace(f'{{{key}}}', str(value))

        filename = f"output_{idx}.txt"
        with open(filename, 'w') as f:
            f.write(content)
