import yandexcloud
# you can store and read it from JSON file 
sa_key={
    "id":"ajeccis8j8hlvf1vksug",
    "service_account_id":"ajebjgekvn0efc847uq8",
    "private_key":"-----BEGIN PRIVATE KEY----- MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuUaci26P4qQ6veicN15uJjYnFD+EKIXR7P7xGBIg87KXeQJTjrtA6lko1VeGudT+7a2Tn7WNuXqTgQfb3rvrlUeWfDuGSi19/5pvUE5F0pddZBJy8xpuOaONSIQ08E6ZJwdfnOC5ANgWl3at0+/H8dZboHkavRiEBkD/JalokZSYEoFKQ0zyanfKQvOUkuBfFfiblN3MUAOf/l7yI5mZ4P7ubPtpahGeEYX5dDjAXhiICsp45GW/6OquilMfIty2ab+JfyopxA5kBIC+yxOytWzn6vmUOsf1wyP/Msqwsj9o775rny1pOXVUHe1sfTdDXZlUCqXoV6HTc8miWbddBAgMBAAECggEAFxkiuG+6LnzYQVBCVIc5SOTEWKReAWWldZ9gZza6hrgk0mpkUDcdyGWZt6+FlARdSYxVdpXyEvHfjweunetFu5U6g/UI1s44/U2lYFincXl4K4d87Vazzg7/8CYJBujjo+pXnX/IQSHnZa8VxQ6NZhJ+yIsaeqckQHzItvusrh2xCsr4dL4EFIRI3AlidNC5Dcx2CFIvXvEmUo7EdB03UoMJvy6u51bEemfO7R5y7dzlkz1mfOmMVy2iHUtA2C1AEAf0OfxAmJzXAy62oHOMGfDXzBIVVwTtao+B7XNwrBl5fTVKH5HKXiuRPS+j/HbDv0OhszuKbNpE1ILNJEb8QQKBgQDWIKbnAXiiwxlleyQQTx9M1BNAYglkdjJRiQB3ub6EsEbkuempz2ygJ/8JuyvsdSxaf4zLFrVlBzzh9nFY6Ykirxys+k9DuWYFPxJG2+wuhBtKOSyfXvLU7iweCDEauu4rEwFL+xK335KDHy2/NudOjbDhizAqZEVmbm8emXqfjQKBgQDQaCj2mAHI0QWDSaaN5pnqtOGH60uLsbhDk1SsnCp+JgBCtbDAG5xxINPafHaah9MEAA2Zwgz7ewKzxXNRhupZxMPuPBQFmduc9Hjs/bIMppGaPReRTGSVmXYwvpHlakHjUYfbdSen+eDjVktzsddZqhDtTzotId/aOuAo4Vp/hQKBgQDT+XMAkLZJ+nXzvlnPQ2Sq++8q92Jw74mUqdmqrFhsps0ntNwaXNseGToi+gXbiYuk80v/6LUeFHIzB3LiIB7AFTaADzPUyX6zhuKi/yfqTKFvcvY3txkRrc5C1L03xwHr5l6MRzsah9tUrtLszn9hhmcqgE3oSWdipcSfODTqKQKBgAp6YizbwaM2Fx/dsRkLUgvB4mDyDI9OdSQ4oRY4l85V3Md92RAfk0MA0oX2ogPs9kgKNKTZY8u1CJK/R6f+r4Op5+vva1ZIwQjoJbhMnQoTydhGYAv3GkuHNrEGs9EkAYILVFhNUJwabRsg+JQtidVBPq6fwB4KyPVw5lpH0kP9AoGAVBxRDXO/0BilnbyRVbfVfm+87L15Em3iOv0HmY60XgeUDcBgXWYfndgKOfLHuCN/JVB6+CebjKB3nvD+yrxBVmqUoHwqdF0h4lwMMDTbtRsI1BjgcjhaEMMcRKnpCf6cMVN9lAUwgbVSYgG3VVPuodzhz/ag/aZL0bQPGQJih0w= -----END PRIVATE KEY-----"
}

sdk=yandexcloud.SDK(service_account_key=sa_key)
bucket_name="fouda"
bucket=sdk.create_bucket(bucket_name)