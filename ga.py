import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Read the input file
input_file = 'world_country_and_usa_states_latitude_and_longitude_values.csv'  # Replace with your actual file name
data = pd.read_csv(input_file)

# Initialize geolocator
geolocator = Nominatim(user_agent="GetLoc")

# Add rate limiting to avoid overwhelming the geolocation service
geocode = RateLimiter(lambda lat_lon: geolocator.reverse(lat_lon, language='en'), min_delay_seconds=1)

# Define a function to get address from latitude and longitude
def get_address(lat, lon):
    try:
        location = geocode(f"{lat}, {lon}")
        return location.address
    except:
        return None

# Apply the function to each row
data['Address'] = data.apply(lambda row: get_address(row['latitude'], row['longitude']), axis=1)

# Save the result to a new file
output_file = 'output_with_addresses.csv'  # Replace with your desired output file name
data.to_csv(output_file, index=False)

print(f"Addresses added and saved to {output_file}")
