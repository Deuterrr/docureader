from src.core.response_builder import APIResponse


ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

async def validate_image_file(file):
    """Validate uploaded file type and content type for image inputs."""
    if isinstance(file, list):
        return APIResponse.invalid_input("Only one file is allowed")
    
    if not file or not hasattr(file, "filename"):
        return APIResponse.invalid_input("No file uploaded")

    ext = file.filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return APIResponse.invalid_input("Invalid file type. Must be JPG or PNG")

    if file.content_type not in ["image/jpeg", "image/png"]:
        return APIResponse.invalid_input("Invalid content type. Must be JPEG or PNG")

    return None
