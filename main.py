import json

def create_nft_metadata(token_id, name, description, image_url, attributes):
    metadata = {
        "token_id": token_id,
        "name": f"{name} #{token_id}",
        "description": description,
        "image": image_url,
        "attributes": attributes
    }
    return metadata

if __name__ == "__main__":
    # Örnek özellikler listesi
    ornek_ozellikler = [
        {"trait_type": "Background", "value": "Blue"},
        {"trait_type": "Eyes", "value": "Laser"},
        {"trait_type": "Mouth", "value": "Grin"}
    ]

    nft_101 = create_nft_metadata(101, "Kripto Robot", "Bu koleksiyonun ilk robotu.", "ipfs://Qm.../101.png", ornek_ozellikler)

    # JSON'ı daha okunaklı bir formatta yazdır
    print(json.dumps(nft_101, indent=4))