import json


def save_config(data: dict, filename: str) -> None:
    """
    Save a dictionary to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    """
    Load and return configuration data from a JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value) -> None:
    """
    Load a JSON config, update one key, and save it back.
    """
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)


# --------------------------------------------------
# json.dump() vs json.dumps()
#
# json.dump() writes JSON data directly to a file.
# json.dumps() converts Python data into a JSON string.
# --------------------------------------------------


# Test Configuration
config = {
    "model": "RandomForest",
    "learning_rate": 0.01,
    "epochs": 10
}

# Save initial config
save_config(config, "config.json")

print("Original Config:")
print(load_config("config.json"))

# Update epochs
update_config("config.json", "epochs", 20)

print("\nUpdated Config:")
print(load_config("config.json"))