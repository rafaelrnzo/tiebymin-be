from .storage_service import upload_file

if __name__ == "__main__":
    url = upload_file("/Users/rafaelrnzo/Proj/Proj/Lantech/tiebymin-be/tiebymin-be-v2/anne-hathaway-4_43.jpeg")
    print("URL file:", url)
