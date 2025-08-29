import csv
import requests
import os
import json

# --- KONFIGURASI ---
BASE_URL = "https://minecraft-server-tiebymin-be-production.dgrttk.easypanel.host/v1" 
CSV_DIR = "/Users/rafaelrnzo/Proj/Proj/Lantech/tiebymin-be/tiebymin-be-v2/tests/api/seed/" # Sesuaikan dengan path Anda

# --- FUNGSI-FUNGSI SEEDING ---

def seed_data(endpoint: str, file_name: str, transform_func: callable, entity_name: str):
    file_path = os.path.join(CSV_DIR, file_name)
    print(f"\n--- Seeding {entity_name} ---")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    payload = transform_func(row)
                    response = requests.post(f"{BASE_URL}{endpoint}", json=payload)
                    
                    if response.status_code == 201:
                        print(f"  SUCCESS: Created {entity_name} '{payload.get('name') or payload.get('kategori') or 'record'}'")
                    else:
                        print(f"  FAILED: Could not create {entity_name}. Status: {response.status_code}, Response: {response.text}")
                except (ValueError, KeyError) as e:
                    print(f"  ERROR: Skipping row due to invalid data: {row}. Details: {e}")
    
    except FileNotFoundError:
        print(f"ERROR: File not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred during {entity_name} seeding: {e}")

# --- FUNGSI TRANSFORMASI DATA PER ENTITAS ---

def transform_bmi(row):
    return {
        "kategori": row["kategori"],
        "min_bmi": float(row["min_bmi"]),
        "max_bmi": float(row["max_bmi"]) if row.get("max_bmi") else None,
        "tips_fashion": row["tips_fashion"],
        "is_active": row["is_active"].lower() == 'true',
        "bmi_tips_summary": row.get("bmi_tips_summary") or None
    }

def transform_body_shape(row):
    return {
        "name": row["name"],
        "penjelasan_body_shape": row["penjelasan_body_shape"],
        "karakteristik": row["karakteristik"],
        "tips_body_shape": row["tips_body_shape"],
        "link_picture": row["link_picture"],
        "is_active": row["is_active"].lower() == 'true'
    }
    
def transform_face_shape(row):
    return {
        "name": row["name"],
        "penjelasan_face_shape": row["penjelasan_face_shape"],
        "karakteristik": row["karakteristik"],
        "tips_bentuk_wajah": row["tips_bentuk_wajah"],
        "illustration_url": row.get("illustration_url") or None,
        "is_active": row["is_active"].lower() == 'true'
    }

def transform_color_analysis(row):
    return {
        "name": row["name"],
        "penjelasan_color_analysis": row["penjelasan_color_analysis"],
        "make_up_tips": row["make_up_tips"],
        "tips_warna_kulit_pakaian": row["tips_warna_kulit_pakaian"],
        "best_colour": json.loads(row["best_colour"]),
        "worst_colour": json.loads(row["worst_colour"]),
        "neutral_colour": json.loads(row["neutral_colour"]),
        "best_colour_combination": json.loads(row["best_colour_combination"]),
        "personality": row["personality"],
        "karakteristik": row["karakteristik"],
        "is_active": row["is_active"].lower() == 'true',
        "color_tips_summary": row.get("color_tips_summary") or None
    }

def transform_product(row):
    return {
        "name": row["name"],
        "description": row["description"],
        "original_price": float(row["original_price"]),
        "current_price": float(row["current_price"]),
        "discount_percentage": float(row["discount_percentage"]) if row.get("discount_percentage") else None,
        "average_rating": float(row["average_rating"]),
        "total_reviews": int(row["total_reviews"]),
        "size_range": row["size_range"],
        "brand": row.get("brand") or None,
        "category": row["category"],
        "product_link": row["product_link"],
        "images": json.loads(row["images"]),
        "is_active": row["is_active"].lower() == 'true',
        "stock_quantity": int(row["stock_quantity"])
    }
    
def transform_celebrity(row):
    return {
        "name": row["name"],
        "picture_url": row["picture_url"],
        "description": row["description"],
        "similarity_text": row["similarity_text"],
        "faceshape_id": row.get("faceshape_id") or None,
        "color_analysis_id": row.get("color_analysis_id") or None
    }

def transform_product_color(row):
    return {
        "product_id": row["product_id"],
        "color_name": row["color_name"],
        "hex_color": row["hex_color"],
        "color_image_url": row.get("color_image_url") or None,
        "is_available": row["is_available"].lower() == 'true',
        "stock_quantity": int(row["stock_quantity"])
    }

def transform_compatibility(row):
    # Fungsi generik untuk semua tabel kompatibilitas
    payload = {}
    for key, value in row.items():
        if key.endswith("_id"):
            payload[key] = value
        elif key.endswith("_score"):
            payload[key] = int(value)
        else:
            payload[key] = value
    return payload

if __name__ == "__main__":
    print("Starting database seeding process...")

    # --- Seed Master Data ---
    seed_data("/bmi-categories/", "bmi_categories_rows.csv", transform_bmi, "BMI Categories")
    # seed_data("/body-shapes", "body_shapes_rows.csv", transform_body_shape, "Body Shapes")
    seed_data("/face-shapes/", "face_shapes_rows.csv", transform_face_shape, "Face Shapes")
    seed_data("/color-analysis/", "color_analysis_rows.csv", transform_color_analysis, "Color Analysis")

    # --- Seed Dependent Data ---
    seed_data("/products/", "products_rows.csv", transform_product, "Products")
    seed_data("/celebrities/", "celebrities_rows.csv", transform_celebrity, "Celebrities")
    
    # --- Seed Data yang Bergantung pada Produk ---
    seed_data("/product-colors/", "product_colors_rows.csv", transform_product_color, "Product Colors")

    # --- Seed Compatibility Tables ---
    seed_data("/product-bmi-compatibility/", "product_bmi_compatibility_rows.csv", transform_compatibility, "Product BMI Compatibility")
    seed_data("/product-body-shape-compatibility/", "product_body_shape_compatibility_rows.csv", transform_compatibility, "Product Body Shape Compatibility")
    seed_data("/product-face-shape-compatibility/", "product_face_shape_compatibility_rows.csv", transform_compatibility, "Product Face Shape Compatibility")
    seed_data("/product-color-analysis-compatibility/", "product_color_analysis_compatibility_rows.csv", transform_compatibility, "Product Color Analysis Compatibility")
    
    print("\nSeeding process finished.")