import veryfi
import pprint
client_id="vrf5tlxtzGrgS9kjI4uMUwkFmhJUZLWkUtl6RM8"
client_secret="lnm95Xox7NT4nijyx0i3h36mXF9phOIMBfgA7rdjssWpf6keINc1lLVYWMP4nWASnsx7ge6YThuu9J4yPHAJKd9hMCztNVjfa7MofdcBa2Xx5ZWNeJA53xGHSw3KlAGN"
username="gnani4412"
api_key="edb0eb820124f7600358be4d322476c6"


client=veryfi.Client(client_id,client_secret,username,api_key)


categories=["Travel","Airfare","Lodging","Job Supplies and Materials","Grocery"]


result= client.process_document(r"C:\Users\Gnaneswar Yalla\Desktop\Final Year Project Code\Testing components\exp_date_extraction\images\fog.jpg")


pprint.pprint(result['date'])