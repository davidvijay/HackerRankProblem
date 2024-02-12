s = '01:00:00PM'
hour_value = s.split(":")[0]
if "AM" in s and hour_value=="12":
    result = "00"+s[2:-2]
    print(result)
elif "PM" in s and hour_value!="12":
    result=str(int(hour_value)+12)+s[2:-2]
    print(result)   
else:
    result = s[:-2]
    print(result)