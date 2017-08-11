from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
import httplib2



#To be continued

#this is the gid when the request body asks for sheet id
spreadsheetId = '1JVXPrjB479OuxqpV7EG1gzlQ8i729fkuTmKaUU1deW8'

json_key = 'demoproject-a76c319a8d32.json'
scope = ['https://www.googleapis.com/auth/spreadsheets']


credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)

# http = httplib2.Http()
# http = credentials.authorize(http)


service = build('sheets','v4',credentials=credentials)


#Changing the border
# change_border = {
#   "requests": [
#     {
#       "updateBorders": {
#         "range": {
#           "sheetId": 278861843,
#           "startRowIndex": 0,
#           "endRowIndex": 10,
#           "startColumnIndex": 0,
#           "endColumnIndex": 7
#         },
#         "top": {
#           "style": "DASHED",
#           "width": 1,
#           "color": {
#             "blue": 1.0
#           },
#         },
#         "bottom": {
#           "style": "DASHED",
#           "width": 1,
#           "color": {
#             "blue": 1.0
#           },
#         },
#         "innerHorizontal": {
#           "style": "DASHED",
#           "width": 1,
#           "color": {
#             "blue": 1.0
#           },
#         },
#       }
#     }
#   ]
# }


#Changing the colors of the cells
requests_body =  {
  "requests": [
    {
      "repeatCell": {
        "range": {
          "sheetId": 257757471, 
          "startColumnIndex": 0,
          "endColumnIndex": 7,
          "startRowIndex": 0,
          "endRowIndex": 1
        },
        "cell": {
          "userEnteredFormat": {
            "backgroundColor": {
              "red": 50,
              "green": 50,
              "blue": 102
            },
            "horizontalAlignment" : "CENTER",
            "textFormat": {
              "fontSize": 12,
              "bold": True
            }
          }
        },
        "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
      }
    },
    {
      "updateSheetProperties": {
        "properties": {
          "sheetId": 257757471,
          "gridProperties": {
            "frozenRowCount": 1 
          }
        },
        "fields": "gridProperties.frozenRowCount"
      }
    }
  ]
}


requests_body_cells =  {
  "requests": [
    {
      "repeatCell": {
        "range": {
          "sheetId": 257757471, 
          "startColumnIndex": 2,
          "endColumnIndex": 3,
          "startRowIndex": 1,
          "endRowIndex": 2
        },
        "cell": {
          "userEnteredFormat": {
            "backgroundColor": {
              "red": 0,
              "green": 100,
              "blue": 100
            },
            "horizontalAlignment" : "CENTER",
            "textFormat": {
              "fontSize": 10,
              "bold": False
            }
          }
        },
        "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
      }
    },
  ]
}



# req2 = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,body=change_border)
# response = req2.execute()
request_one = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,body=requests_body)
response = request_one.execute()
request_two = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,body=requests_body_cells)
response = request_two.execute()

print(response)










# result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,range=rangeName)

# response = result.execute()

# print(response)






