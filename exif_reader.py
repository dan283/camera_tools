import os
import exifread

def get_focal_length(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        focal_length = tags.get('EXIF FocalLength')
        if focal_length:
            return float(focal_length.values[0].num) / float(focal_length.values[0].den)
        else:
            return None

def main():
    directory = '/Users/danielulrich/Desktop'
    with open('lens_data.txt', 'w') as f:
        for filename in os.listdir(directory):
            if filename.endswith('.jpg'):
                file_path = os.path.join(directory, filename)
                focal_length = get_focal_length(file_path)
                print(focal_length)
                if focal_length:
                    f.write(f'{filename}: {focal_length}\n')

if __name__ == '__main__':
    main()


