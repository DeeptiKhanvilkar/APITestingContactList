login_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "user": {
      "type": "object",
      "properties": {
        "_id": {
          "type": "string"
        },
        "firstName": {
          "type": "string"
        },
        "lastName": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "__v": {
          "type": "number"
        }
      },
      "required": [
        "_id",
        "firstName",
        "lastName",
        "email",
        "__v"
      ]
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "user",
    "token"
  ]
}