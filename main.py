import os
import json
import random
import cv2
import numpy as np
from PIL import Image

def save_labelme_json(filename, shapes, image_size):
    json_data = {
        "version": "4.5.7",
        "flags": {},
        "shapes": shapes,
        "imagePath": os.path.basename(filename),
        "imageData": None,  # Optional: Can be base64 encoded string of image data
        "imageHeight": image_size[1],
        "imageWidth": image_size[0]
    }
    with open(filename.replace('.jpg', '.json'), 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


def load_annotations(folder_path):
    annotations = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_path = os.path.join(folder_path, filename)
            with open(json_path, 'r') as file:
                data = json.load(file)
                image_path = os.path.join(folder_path, filename.replace(".json", ".jpg"))
                annotations.append((image_path, data['shapes']))
    return annotations

def extract_region(image_path, shape):
    image = cv2.imread(image_path)
    points = shape['points']
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    points = np.array(points, dtype=np.int32)
    cv2.fillPoly(mask, [points], 255)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    x, y, w, h = cv2.boundingRect(points)
    cropped_region = masked_image[y:y+h, x:x+w]
    return cropped_region, mask[y:y+h, x:x+w], (x, y, w, h)

def place_regions(background_image, annotations, num_regions_per_image, output_path, img_index):
    bg_w, bg_h = background_image.size
    placements = []
    shapes = []  # List to hold data for JSON
    for _ in range(num_regions_per_image):
        while True:
            image_path, shapes_data = random.choice(annotations)
            shape = random.choice(shapes_data)
            region, mask, bbox = extract_region(image_path, shape)
            x, y, w, h = bbox
            pos_x = random.randint(0, bg_w - w)
            pos_y = random.randint(0, bg_h - h)
            placement = (pos_x, pos_y, pos_x + w, pos_y + h)
            if all(not overlaps(placement, p) for p in placements):
                placements.append(placement)
                pil_region = Image.fromarray(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
                pil_mask = Image.fromarray(mask)
                background_image.paste(pil_region, (pos_x, pos_y), pil_mask)

                # Ensure points are transformed within the bounds of the image
                transformed_points = []
                for point in shape['points']:
                    new_x = min(max(point[0] + pos_x - x, 0), bg_w - 1)
                    new_y = min(max(point[1] + pos_y - y, 0), bg_h - 1)
                    transformed_points.append([new_x, new_y])

                shapes.append({
                    "label": shape['label'],
                    "points": transformed_points,
                    "shape_type": "polygon",
                    "flags": {}
                })
                break

    # Save the image and JSON
    output_filename = os.path.join(output_path, f'output_{img_index + 1}.jpg')
    background_image.save(output_filename)
    save_labelme_json(output_filename, shapes, (bg_w, bg_h))





def overlaps(a, b):
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])

def main():
    background_image_path = './images/bg.jpg'
    folder_path = './soybean_processed'
    output_path = './simulated_images'
    num_images = 5
    min_regions_per_image = 30  # Set minimum number of regions
    max_regions_per_image = 50  # Set maximum number of regions

    annotations = load_annotations(folder_path)
    background_image = Image.open(background_image_path)

    for i in range(num_images):
        bg_copy = background_image.copy()
        # Randomly choose the number of regions for this image within the specified range
        num_regions = random.randint(min_regions_per_image, max_regions_per_image)
        place_regions(bg_copy, annotations, num_regions, output_path, i)
        # Output file saving is now handled inside place_regions

if __name__ == '__main__':
    main()
