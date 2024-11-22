import requests

extension_mime_types = {}
final_data = [['Media Type', 'Type', 'Subtype', 'Template', 'Extensions']]
list_of_types = ['application', 'audio', 'font', 'haptics', 'image', 'message', 'model', 'multipart', 'text', 'video']

def get_data(type):
    response = requests.get(f'https://www.iana.org/assignments/media-types/{type}')
    return response.text

def extension_append():
    link = 'https://raw.githubusercontent.com/apache/httpd/refs/heads/trunk/docs/conf/mime.types'
    response = requests.get(link)
    if response.status_code == 200:
        mime_types_content = response.text

        # Process each line
        for line in mime_types_content.splitlines():
            # Skip comments and empty lines
            if line.strip().startswith("#") or not line.strip():
                continue
            
            # Extract MIME type and extensions
            parts = line.split()
            if len(parts) > 1:
                mime_type = parts[0]
                extensions = parts[1:]
                # Add to dictionary
                for ext in extensions:
                    if ext not in extension_mime_types:
                        extension_mime_types[mime_type] = ext
                    else:
                        # Handle multiple MIME types for a single extension
                        if isinstance(extension_mime_types[ext], list):
                            extension_mime_types[mime_type].append(ext)
                        else:
                            extension_mime_types[mime_type] = [extension_mime_types[mime_type], ext]
    else:
        print("Failed to fetch MIME types file.")

def process_data(data, type):
    global extension_mime_types
    lnk = 'http://www.iana.org/assignments/media-types/'
    print(f"Processing data for {type}.")
    for line in data.splitlines()[1:]:
        Media_type = line.split(',')[1]
        Type = line.split(',')[1].split('/')[0]
        Subtype = line.split(',')[0]
        Template = lnk + Type + '/' + Subtype
        Extension = extension_mime_types.get(Media_type, '')
        final_data.append([Media_type, Type, Subtype, Template, Extension])

def write_data(data):
    with open('data/media-types.csv', 'w') as file:
        for line in data:
            file.write(','.join(line) + '\n')

if __name__ == '__main__':
    print("Creating extensions dictionary.")
    extension_append()
    print("Processing IANA data.")
    for type in list_of_types:
        process_data(get_data(f"{type}.csv"), type)
    print(f"Data processed.")
    print("Writing data to CSV.")
    write_data(final_data)

