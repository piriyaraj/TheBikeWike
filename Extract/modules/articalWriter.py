"""
scrapping table from link
creat :29/12/2020
update:03/01/2021
"""


def artical(soup):
    artiKey=[
    'Model::Now we see about the modle_n. ',
    'Year::modle_n is the introduction to the motorcycle market in year_n. ',
    'Category::It\'s Category as Category_n. ',
    'Price as new::A brand modle_n price more than US price_n depending on the taxes that the country applies when being imported and the extra accessories.</div><div><br /></div><div>',
    'Displacement::Talking about the engine of the motorbike the displacement of the engine is displacement_n. ',
    'Engine type::Which is an enginetype_n. ',
    'Power::The power of the modle_n engine is power_n. ',
    'Torque::The torque of the engine is torque_n. ',
    'Top speed::Top speed of the modle_n is topspeed_n. ',
    'Compression::The Compression ratio of the modle_n is compression_n. ',
    'Bore x stroke::The size of the Bore x Stroke is bore_n. ',
    'Valves per cylinder::There are valves_n valves per cylinder. ',
    'Fuel system::The fuel system is fuelsystem_n. </div><div><br /></div><div>',
    'Fuel control::The fuel control is fuelcontrol_n. ',
    'Fuel consumption::The Millage of the modle_n is fuelconsumption_n',
    'Cooling system::And modle_n has  coolingsystem_n cooling system. ',
    'Gearbox:: modle_n have gearbox_n gearbox. ',
    'Transmission type,final drive::The transmission type of the bike is transmissiontype_n. ',
    'Clutch::It has clutch_n clutch. </div><div><br /></div><div>',
    'Driveline::And modle_n Driveline is driveline_n. ',
    'Exhaust system::Exhaust system of the bike is exhaustsystem_n. ',
    'Frame type::modle_n is made with a frametype_n frame type. ',
    'Rake (fork angle)::And has a fork angle of fork_n degrees. ',
    'Trail::The horizontal distance from to where the steering axis intersects the ground is trail_n. ',
    'Front suspension::Front suspension is frontsusension_n. ',
    'Rear suspension::And modle_n Rear suspension is rearsusension_n. ',
    'Front tyre::Front tyre is fronttyre_n. ',
    'Rear tyre::And Rear tyre is reartyre_n. ',
    'Front brakes::About front brakes is frontbrakes_n. ',
    'Diameter::Diameter of the front tyre is diameterrear_n. ',
    'Rear brakes::About Rear break is rearbrakes_n. ',
    'Diameter::Diameter of modle_n rear tyre is diameterrear_n. ',
    'Dry weight::modle_n motorbike weighs dryweight_n.\n\n',
    'Power/weight ratio::And the power to weight ratio is Powerweight_n. ',
    'Seat height::height of the sear is seatheight_n. ',
    'Overall width::And the overall width of the modle_n is overallwidth_n. ',
    'Wheelbase::The wheel has a measurement is Wheelbase_n. ',
    'Reserve fuel capacity::it has reserve_n Reserve fuel capacity.',  #37
    'Fuel capacity::And this bike has a fuel capacity of fuelcapacity_n.</div><div><br /></div><div>',
    'Color options::This bike is available in coloroptions_n. ', #39 line
    'Starter::this bike can be started with an starter_n starter. ',
    'Instruments::modle_n bike is available with instruments_n. ',
    'Electrical::The Electrical Details is electrical_n. ',
    'Light:: modle_n head light is light_n. ',
    ]
    keys   = []
    values = []
    #url="https://bikez.com/motorcycles/bmw_k_1600_b_2021.php"
    # reqs = requests.get(url)
    # soup = BeautifulSoup(reqs.text, 'html.parser')
    for i in soup.find_all('table'):
        if(i.text.find("General information")!=-1 or i.text.find("General moped information")!=-1 or i.text.find("Other specifications")!=-1):
            table=i
            break
    tr=table.findAll('tr')
    artical="<div>"
    for i in tr:
        td=i.findAll("td")
        if(len(td)==0 or len(td)==1):
            continue
        keys.append(td[0].text.replace(":",""))
        for i in artiKey:
            if(i.split("::")[0]==td[0].text.replace(":","")):
                artical+=i.split("::")[1]
        values.append(td[1].text)
    #print(keys)
    artical=artical+"</div>"
    try:artical=artical.replace("modle_n",values[keys.index('Model')])
    except:pass
    try:artical=artical.replace("year_n",values[keys.index('Year')])
    except:pass
    try:artical=artical.replace("Category_n",values[keys.index('Category')])
    except:pass
    try:artical=artical.replace("price_n",values[keys.index('Price as new')].split()[1])
    except:pass

    try:artical=artical.replace("displacement_n",values[keys.index('Displacement')])
    except:pass
    try:artical=artical.replace("enginetype_n",values[keys.index('Engine type')])
    except:pass
    try:artical=artical.replace("power_n",values[keys.index('Power')].replace("HP","horse power").replace("@","at").replace("RPM","rotations per minute"))
    except:pass
    try:artical=artical.replace("torque_n",values[keys.index('Torque')])
    except:pass
    try:artical=artical.replace("compression_n",values[keys.index('Compression')])
    except:pass
    try:artical=artical.replace("bore_n",values[keys.index('Bore x stroke')])
    except:pass
    try:artical=artical.replace("valves_n",values[keys.index('Valves per cylinder')])
    except:pass
    try:artical=artical.replace("fuelsystem_n",values[keys.index('Fuel system')])
    except:pass
    try:artical=artical.replace("fuelcontrol_n",values[keys.index('Fuel control')])
    except:pass
    try:artical=artical.replace("topspeed_n",values[keys.index('Top speed')])
    except:pass
    try:artical=artical.replace("coolingsystem_n",values[keys.index('Cooling system')])
    except:pass
    try:artical=artical.replace("gearbox_n",values[keys.index('Gearbox')])
    except:pass
    try:artical=artical.replace("transmissiontype_n",values[keys.index('Transmission type,final drive')])
    except:pass
    try:artical=artical.replace("clutch_n",values[keys.index('Clutch')])
    except:pass
    try:artical=artical.replace("driveline_n",values[keys.index('Driveline')])
    except:pass
    try:artical=artical.replace("exhaustsystem_n",values[keys.index('Exhaust system')])
    except:pass

    try:artical=artical.replace("frametype_n",values[keys.index('Frame type')])
    except:pass
    try:artical=artical.replace("fork_n",values[keys.index('Rake (fork angle)')])
    except:pass
    try:artical=artical.replace("trail_n",values[keys.index('Trail')])
    except:pass
    try:artical=artical.replace("frontsusension_n",values[keys.index('Front suspension')])
    except:pass
    try:artical=artical.replace("rearsusension_n",values[keys.index('Rear suspension')])
    except:pass
    try:artical=artical.replace("fronttyre_n",values[keys.index('Front tyre')])
    except:pass
    try:artical=artical.replace("reartyre_n",values[keys.index('Rear tyre')])
    except:pass
    try:artical=artical.replace("frontbrakes_n",values[keys.index('Front brakes')])
    except:pass
    try:artical=artical.replace("diameterrear_n",values[keys.index('Diameter')])
    except:pass
    try:artical=artical.replace("rearbrakes_n",values[keys.index('Rear brakes')])
    except:pass
    try:artical=artical.replace("diameterrear_n",values[keys.index('Diameter')])
    except:pass

    try:artical=artical.replace("dryweight_n",values[keys.index('Dry weight')])
    except:pass
    try:artical=artical.replace("Powerweight_n",values[keys.index('Power/weight ratio')])
    except:pass
    try:artical=artical.replace("seatheight_n",values[keys.index('Seat height')])
    except:pass
    try:artical=artical.replace("overallwidth_n",values[keys.index('Overall width')])
    except:pass
    try:artical=artical.replace("Wheelbase_n",values[keys.index('Wheelbase')])
    except:pass
    try:artical=artical.replace("reserve_n",values[keys.index('Reserve fuel capacity')])
    except:pass
    try:artical=artical.replace("fuelcapacity_n",values[keys.index('Fuel capacity')])
    except:pass
    try:artical=artical.replace("fuelconsumption_n",values[keys.index('Fuel consumption')])
    except:pass

    try:artical=artical.replace("coloroptions_n",values[keys.index('Color options')])
    except:pass
    try:artical=artical.replace("starter_n",values[keys.index('Starter')])
    except:pass
    try:artical=artical.replace("instruments_n",values[keys.index('Instruments')])
    except:pass
    try:artical=artical.replace("electrical_n",values[keys.index('Electrical')])
    except:pass
    try:artical=artical.replace("light_n",values[keys.index('Light')])
    except:pass


    qus1="<br/><h2 style=\"text-align: center;\">Frequently asked questions</h2>"
    try:
        no=keys.index('Price as new')
        qus1+="<h3>How much is a modle_n?</h3>   "+artiKey[3].split("::")[1].split(".")[0]+"."+"<br/>"
        value=(values[no].split()[1])
        qus1=qus1.replace("price_n",value)


    except:pass
    try:
        no=keys.index('Fuel consumption')
        qus1+="<h3>What is the real mileage of modle_n?(per liter)</h3>"+artiKey[14].split("::")[1]+"<br/><br/>"
        qus1=qus1.replace("fuelconsumption_n",values[no])
    except:pass
    try:
        no=keys.index('Top speed')
        qus1+="<h3>What is the speed of the modle_n?</h3>"+artiKey[8].split("::")[1]+"<br/><br/>"
        qus1=qus1.replace("topspeed_n",values[no])
    except:pass
    try:
        no=keys.index('Color options')
        qus1+="<h3>What are the colours available in modle_n?</h3>"+artiKey[39].split("::")[1]+"<br/></br>"
        qus1=qus1.replace("coloroptions_n",values[no])
    except:pass

    try:
        no=keys.index('Reserve fuel capacity')
        qus1+="<h3>What is the Reserve fuel capacity of modle_n?</h3>"+artiKey[37].split("::")[1]+"<br/><br/>"
        qus1=qus1.replace("reserve_n",values[no])
    except:pass
    try:
        no=keys.index('Fuel capacity')
        qus1+="<h3>What is the fuel capacity of modle_n?</h3>"+artiKey[38].split("::")[1].split(".")[0]+"."+"<br/><br/>"
        qus1=qus1.replace("fuelcapacity_n",values[no])
    except:pass
    try:
        no=keys.index('Cooling system')
        qus1+="<h3>What type of cooling system used in  modle_n?</h3>"+artiKey[15].split("::")[1]+"<br/><br/>"
        qus1=qus1.replace("coolingsystem_n",values[no])
    except:pass

    qus1=qus1.replace("modle_n",values[keys.index('Model')])

    # # try:qus1=qus1.replace("price_n",values[keys.index('Price as new')].split()[1])
    # # except:pass
    # try:qus1=qus1.replace("topspeed_n",values[keys.index('Top speed')])
    # except:pass
    # try:qus1=qus1.replace("fuelconsumption_n",values[keys.index('Fuel consumption')])
    # except:pass
    # try:qus1=qus1.replace("coloroptions_n",values[keys.index('Color options')])
    # except:pass

    # pyperclip.copy(artical+qus1)
    artical="<p><br /><br /></p><h2 style=\"text-align: center;\"><strong><span style=\"text-decoration: underline;\">"+values[keys.index('Model')]+"</span></strong></h2>"+artical

    return artical+qus1,keys,values

# url="https://bikez.com/motorcycles/aprilia_sr_50_mt_2021.php"
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')
# a,b,c=artical(soup)
# pyperclip.copy(a)
# print(a)
