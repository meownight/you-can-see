ent_hr = input("進場時間").split(":")
ent_min = int(ent_hr[0]) * 60 + int(ent_hr[1])
out_hr = input("離場時間").split(":")
if int(out_hr[0]) >= int(ent_hr[0]):
    out_min = int(out_hr[0]) * 60 + int(out_hr[1])
    lic = input("是否有申請月租車位:")
    time = out_min - ent_min
    if lic == "Y": 
        fee = 0
        print(fee)
        print("請記得下個月繳費")
    if lic == "N":
        if time // 30 == 0:
            fee = (time // 30) * 20
        else:
            fee = ((time // 30) + 1) * 20
        print(int(fee))