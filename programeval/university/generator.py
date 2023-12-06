# Helper Generator Functions
import uuid

def generate_unique_code():
    # Generate a unique identifier
    unique_id = str(uuid.uuid4().int)[:3]

    # Create code with format: LO###
    code = f"LO{unique_id}"

    return code