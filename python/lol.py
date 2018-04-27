from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAALw1EZz4:APA91bFqW7lsYB8TPNVHjW0EZZFz205x548hq6qjJfVTIcq_4NC0Zd5RuWQ_PJb2IiuqjLUri_Yl0SgIrTsfUoQuAfWWGIK3KSbd2Q8QVWDUTT9frXJOAKcjCchaInzY0xKK2M72kCId")

registration_id =  "eQ16-VXA7HE:APA91bGveQZmrOlSiMR-jl7WCjkZs-igGIuAu0THfI58o2hhoSiEnoZ24ud-KhIcDNBsc5AquwoGAqn-0_r8AegelOZpPHBQajiMWFOcdXfuTjWL2bkT29Fr_3zcA-pEeSCMqZlDuX_z"
#registration_id = "fFhiOEFnr6M:APA91bHr2-2O-InTAwThl-AJqyAxMRjc75FEFSVOIWWO-uNPXVx6XaVm5es9qkc8xWHNnZ_MS3drz3c15zjcbW_pIDzALV9167Axy_ekPhUQdvKFdtDGxIl1vwA8baNgnDVqlPW96Bxq"

message_title = "Animal Spotted"
message_body = "An Animal has been spotted near you. Please open to check."

data_message = {
    "lat" : "19.198496",
    "longi" : "73.176674",
    "animal" : "Dragon"
}

result = push_service.notify_single_device(registration_id=registration_id, message_body=message_body, data_message=data_message)

print(result)
