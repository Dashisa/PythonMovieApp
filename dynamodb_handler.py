import boto3

import key_config as keys


dynamodb_resource = boto3.resource(
    'dynamodb',
    #aws_access_key_id     = keys.ACCESS_KEY_ID,
    #aws_secret_access_key = keys.ACCESS_SECRET_KEY,
    region_name           = keys.REGION_NAME,
)


def create_table_movie():
   table = dynamodb_resource.create_table(
       TableName = 'Movie', # Name of the table
       KeySchema = [
           {
               'AttributeName': 'id',
               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key
           }
       ],
AttributeDefinitions = [
           {
               'AttributeName': 'id', # Name of the attribute
               'AttributeType': 'N'   # N = Number (B= Binary, S = String)
           }
       ],
       ProvisionedThroughput={
           'ReadCapacityUnits'  : 10,
           'WriteCapacityUnits': 10
       }
   )
   return table
   
MovieTable = dynamodb_resource.Table('Movie')

def add_item_to_movie_table(id, title, director):
    
    response = MovieTable.put_item(
        Item = {
            'id'     : id,
            'title'  : title,
            'director' : director,
            'likes'  : 0
        }
    )
    return response
    
def get_item_from_movie_table(id):

    response = MovieTable.get_item(
        Key = {
            'id': id
        },
        AttributesToGet = [
            'title','director'
        ]
    )
    return response
    
       
def update_item_in_movie_table(id, data:dict):

    response = MovieTable.update_item(
        #
        Key = {
           'id': id
        },
        AttributeUpdates={
            
            'title': {
               'Value'  : data['title'],
               'Action' : 'PUT' 
            },
            'director': {
               'Value'  : data['director'],
               'Action' : 'PUT'
            }
        },
        
        ReturnValues = "UPDATED_NEW"  # returns the new updated valu
)
    
    return response
