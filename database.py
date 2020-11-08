import boto3
from boto3.dynamodb.conditions import Attr, Key
           
class Temp:
    def __init__(self):
        self.__Tablename__ = "TTDatabase"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "Username"
        self.Primary_key = "Username"
        self.columns = ["TempRequest"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, Username,TempRequest):

    
        response = self.table.put_item(
            Item={
                self.Primary_Column_Name: Username,
                
                self.columns[0]: TempRequest
               
                
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "Description": "Request was created succesfully",
                "UserName": Username

            }
        else:
            return  {
                "Result": False,
                "Error": "Database error",
                "Description": "Database error",
                "UserName": None
            }

    def view(self):
        res = self.table.scan()

        return {
            "Result": True,
            "Error": None,
            "Description": "All request from database",
            "UserDB": res['Items']
        }
        


if __name__ == "__main__":
    temp = Temp()
   
   
#    # New Request
#     res = temp.put(Username="Dolma Gurung", TempRequest= "+1")
    

#     #for view
#     res = temp.view()


# print (res)
