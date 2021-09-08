import requests



response = requests.get('https://61261a39e40e190017072808.mockapi.io/test')

list_obj = response.json()[0]


def get_res(search):

     if type(search) == list:

          for obj in search:
               get_res(obj)

     elif type(search) == dict:

          for key in search:

               value = search[key]

               if type(value) == list:
                    get_res(value)

               elif type(value) == dict :
                    result = value.get('res')
                    print(result)

                    if result == 'res':
                         break

get_res(list_obj)

