import pytesseract
import cv2
from PIL import Image
import pandas as pd

# Set path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_table_from_image(image_path):
    # Read image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use OCR to detect text with detailed data
    custom_config = r'--oem 3 --psm 6 -c tessedit_create_tsv=1'
    data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)
    
    # Extract text with bounding boxes
    text_data = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 30:  # Confidence threshold
            text_data.append({
                'text': data['text'][i],
                'left': data['left'][i],
                'top': data['top'][i],
                'width': data['width'][i],
                'height': data['height'][i],
                'conf': data['conf'][i]
            })
    
    return text_data

def organize_text_into_table(text_data):
    # Group text by rows based on y-coordinates
    rows = {}
    for item in text_data:
        row_key = item['top'] // 20  # Adjust this threshold based on your font size
        if row_key not in rows:
            rows[row_key] = []
        rows[row_key].append(item)
    
    # Sort rows and columns
    table_data = []
    for row_key in sorted(rows.keys()):
        row_items = sorted(rows[row_key], key=lambda x: x['left'])
        table_data.append([item['text'] for item in row_items])
    
    return table_data

# Usage
image_path = 'images/table_images.jpg'
text_data = extract_table_from_image(image_path)
table_data = organize_text_into_table(text_data)

# Convert to pandas DataFrame
df = pd.DataFrame(table_data)
print("Extracted Table:")
print(df)

# Save to CSV
df.to_csv('output_table.csv', index=False, encoding='utf-8')