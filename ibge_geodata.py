import geopandas as gpd
import psycopg2
import os    

password = os.environ.get('PG_PASSWORD')
print(password)
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    database='ibge',
    user='postgres',
    password=password
)

# Create a cursor
cursor = conn.cursor()

# Execute a test query
cursor.execute('SELECT version();')
result = cursor.fetchone()

# Print the result
print('Connection successful!')
print('PostgreSQL version:', result[0])

# Close the cursor and connection
cursor.close()


# Specify the path to the zip file and the relative path to the shapefile within the zip folder
zip_path = 'original_data/qg_2021_800_facelogradouro_coleta.zip'
shapefile_path = 'qg_2021_800_facelogradouro_coleta.shp'

# Read the shapefile from the zip file
gdf = gpd.read_file(f"zip://{zip_path}/{shapefile_path}")

# Access the loaded shapefile data
print(gdf.head())



"""


for file_name in list_of_shapefiles:  # Replace with the list of shapefile names
    shapefile_path = f"{shapefile_folder}/{file_name}"

    # Read shapefile into a GeoDataFrame
    gdf = gpd.read_file(shapefile_path)

    # Get column names and types from the GeoDataFrame
    column_names = gdf.columns.tolist()
    column_types = gdf.dtypes.tolist()

    # Construct the CREATE TABLE query dynamically
    create_table_query = f"CREATE TABLE {file_name.replace('.shp', '')} ("

    for name, data_type in zip(column_names, column_types):
        # Map GeoPandas data types to equivalent PostgreSQL types
        pg_data_type = {
            'int64': 'INTEGER',
            'float64': 'FLOAT',
            'object': 'TEXT',
            'geometry': 'GEOMETRY'
        }.get(str(data_type), 'TEXT')

        # Append column definition to the CREATE TABLE query
        create_table_query += f"{name} {pg_data_type}, "

    # Append the geometry column definition
    create_table_query += "geometry GEOMETRY(Point, 4326)"

    # Complete the CREATE TABLE query
    create_table_query += ");"

    # Execute the CREATE TABLE query
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()

# Close the connection to the PostgreSQL database
conn.close()
"""