def table(obj,key,value):
    for index,i in enumerate(key):
        i=i.replace(" ","_").replace("/","_").capitalize()
        if(i == 'Model'):
            obj.Model =value[index]
        elif(i == 'Year'):
            obj.Year =value[index]
        elif(i == 'Category'):
            obj.Category =value[index]
        elif(i == 'Rating'):
            obj.Rating =value[index]
        elif(i == 'Displacement'):
            obj.Displacement =value[index]
        elif(i == 'Engine_type'):
            obj.Engine_type =value[index]
        elif(i == 'Power'):
            obj.Power =value[index]
        elif(i == 'Top_speed'):
            obj.Top_speed =value[index]
        elif(i == 'Fuel_system'):
            obj.Fuel_system =value[index]
        elif(i == 'Cooling_system'):
            obj.Cooling_system =value[index]
        elif(i == 'Gearbox'):
            obj.Gearbox =value[index]
        elif(i == 'Transmission_type'):
            obj.Transmission_type =value[index]
        elif(i == 'Clutch'):
            obj.Clutch =value[index]
        elif(i == 'Fuel_consumption'):
            obj.Fuel_consumption =value[index]
        elif(i == 'Greenhouse_gases'):
            obj.Greenhouse_gases =value[index]
        elif(i == 'Frame_type'):
            obj.Frame_type =value[index]
        elif(i == 'Front_suspension'):
            obj.Front_suspension =value[index]
        elif(i == 'Rear_suspension'):
            obj.Rear_suspension =value[index]
        elif(i == 'Front_tire'):
            obj.Front_tire =value[index]
        elif(i == 'Rear_tire'):
            obj.Rear_tire =value[index]
        elif(i == 'Front_brakes'):
            obj.Front_brakes =value[index]
        elif(i == 'Rear_brakes'):
            obj.Rear_brakes =value[index]
        elif(i == 'Dry_weight'):
            obj.Dry_weight =value[index]
        elif(i == 'Power_weight_ratio'):
            obj.Power_weight_ratio =value[index]
        elif(i == 'Seat_height'):
            obj.Seat_height =value[index]
        elif(i == 'Overall_height'):
            obj.Overall_height =value[index]
        elif(i == 'Overall_length'):
            obj.Overall_length =value[index]
        elif(i == 'Overall_width'):
            obj.Overall_width =value[index]
        elif(i == 'Wheelbase'):
            obj.Wheelbase =value[index]
        elif(i == 'Fuel_capacity'):
            obj.Fuel_capacity =value[index]
        elif(i == 'Color_options'):
            obj.Color_options =value[index]
        elif(i == 'Starter'):
            obj.Starter =value[index]
        elif(i == 'Factory_warranty'):
            obj.Factory_warranty =value[index]
        elif(i == 'Comments'):
            obj.Comments =value[index]
        elif(i == 'Update_specs'):
            obj.Update_specs =value[index]
        elif(i == 'Insurance_costs'):
            obj.Insurance_costs =value[index]
        elif(i == 'Finance_options'):
            obj.Finance_options =value[index]
        elif(i == 'Parts_finder'):
            obj.Parts_finder =value[index]
        elif(i == 'Maintenance'):
            obj.Maintenance =value[index]
        elif(i == 'Ask_questions'):
            obj.Ask_questions =value[index]
        elif(i == 'Related_bikes'):
            obj.Related_bikes =value[index]
    return obj