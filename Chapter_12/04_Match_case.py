# Match-case enables structured and clear pattern matching for specific values.
def http_status(status): 
    match status: 
        case 200: 
            return "OK"  # Handles successful responses
        case 404: 
            return "Not Found"  # Handles resource not found errors
        case 500: 
            return "Internal Server Error"  # Handles server errors
        case _:  # Default case for unmatched status codes
            return "Unknown status"

# Testing various HTTP status codes
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(500))  # Output: Internal Server Error
print(http_status(403))  # Output: Unknown status
