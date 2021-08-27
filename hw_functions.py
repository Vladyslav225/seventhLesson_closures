import requests
import json



response = requests.get('https://61261a39e40e190017072808.mockapi.io/test')



list_obj = response.json()[0]
# print(type(list_obj))
# print(list_obj)


def get_res(data):
     
     for obj in data:

          for key in obj.keys():

               value = obj[key]
               
               if type(value) == list:
                    get_res(value)

               if type(value) == dict:
                    get_value = value.get('res')
                    print(get_value)
                    

for key in list_obj.keys():
     value = list_obj[key]

     if type(value) == list:
          get_res(list_obj[key])















