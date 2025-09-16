import json
from PIL import Image
import os


def create_json_files(num_files, collection_name, collection_symbol, collection_description, royalties_percentage, image_file, traits, creators, external_url=None):

    if not os.path.isdir("images"):
        os.mkdir("images")

    if not os.path.isdir("json_files"):
        os.mkdir("json_files")

    failed_files = []

    for i in range(num_files):

        file_name = f"{i}.png"

        try:
            img = Image.open(image_file)
            img.save(f"images/{file_name}")
        except Exception as e:
            print(f"Error creating image {file_name}: {e}")
            failed_files.append(i)
            continue

        data = {
            "name": f"{collection_name} #{i}",
            "symbol": collection_symbol,
            "description": collection_description,
            "seller_fee_basis_points": int(royalties_percentage * 100),
            "image": f"{file_name}",
            "external_url": external_url,
            "attributes": traits,
            "properties": {
                "files": [
                    {
                        "uri": f"{file_name}",
                        "type": "image/png"
                    }
                ],
                "category": "image",
                "creators": creators
            }
        }

        try:
            with open(f"json_files/{i}.json", "w") as outfile:
                json.dump(data, outfile, indent=4)
            print(f"{i}.json created successfully")
        except Exception as e:
            print(f"Error creating JSON file {i}.json: {e}")
            failed_files.append(i)

    if failed_files:
        print(f"Retrying {len(failed_files)} failed files...")
        for i in failed_files:
            file_name = f"{i}.png"
            data = {
                "name": f"{collection_name} #{i}",
                "symbol": collection_symbol,
                "description": collection_description,
                "seller_fee_basis_points": int(royalties_percentage * 100),
                "image": f"{file_name}",
                "external_url": external_url,
                "attributes": traits,
                "properties": {
                    "files": [
                        {
                            "uri": f"{file_name}",
                            "type": "image/png"
                        }
                    ],
                    "category": "image",
                    "creators": creators
                }
            }
            try:
                with open(f"json_files/{i}.json", "w") as outfile:
                    json.dump(data, outfile, indent=4)
                print(f"{i}.json created successfully")
            except Exception as e:
                print(f"Error creating JSON file {i}.json: {e}")

    exit()


try:
    num_files = int(input("Enter the collection size: "))
    collection_name = input("Enter collection_name: ")
    collection_symbol = input("Enter collection symbol: ")
    collection_description = input("Enter collection description: ")
    royalties_percentage = float(
        input("Enter the percentage of royalties (1-10): ")) / 1
    image_file = input("Enter the location of the image file: ")
    external_url = input("Enter an external URL (optional): ")

    num_traits = int(input("Enter the number of traits: "))
    traits = []
    for i in range(num_traits):
        trait_type = input(f"Trait {i+1} type: ")
        value = input(f"Trait {i+1} value: ")
        traits.append({"trait_type": trait_type, "value": value})

    creators = []
    num_creators = int(input("Enter the number of creators: "))
    for i in range(num_creators):
        creator_address = input(f"Enter the address of creator {i+1}: ")
        creator_share = int(
            input(f"Enter the percentage of royalties for creator {i+1}: "))
        creators.append({"address": creator_address, "share": creator_share})

    create_json_files(num_files, collection_name, collection_symbol, collection_description,
                      royalties_percentage, image_file, traits, creators, external_url)

except ValueError as e:
    print(f"Error: {e}. Please enter a valid number or percentage.")
except Exception as e:
    print(f"Error: {e}. Please try again later.")
