import oomp

github_footprint_base = "https://github.com/oomlout/oomlout_oomp_footprint_bot/tree/main/foootprntss"
directory_footprint_base = "oomlout_oomp_footprint_bot/footprints"
directory_footprint_end = "/working/working.kicad_mod"

def get_footprints(**kwargs):

    matches = []

    #make a pattern match dict for the part, take each element on oomp.names_of_main_elements if the part matches all the items then add the footprint to kwargs

    ###### breakout_boards
    match = {}
    match["description_main"] = "atmega328"
    match["description_extra"] = "shennie"
    match["footprint_name"] = "kicad_module_arduino_nano_withmountingholes"
    matches.append(match)
    
    ###### button
    match = {}
    match["type"] = "button"
    match["size"] = "3_5_mm_x_6_mm_x_2_5_mm"
    match["footprint_name"] = "kicad_button_switch_smd_sw_tactile_spst_no_straight_ck_pts636sx25smtrlfs"
    matches.append(match)

    ###### capacitor
    match = {}
    match["type"] = "capacitor"
    match["size"] = "3216_avx_a"
    match["footprint_name"] = "kicad_capacitor_tantalum_smd_cp_eia_3216_18_kemet_a"
    matches.append(match)

    match = {}
    match["type"] = "capacitor"
    match["size"] = "0603"
    match["footprint_name"] = "kicad_capacitor_smd_c_0603_1608metric"
    matches.append(match)
    
    match = {}
    match["type"] = "capacitor"
    match["size"] = "0402"
    match["footprint_name"] = "kicad_capacitor_smd_c_0402_1005metric"
    matches.append(match)

    #crystal
    match = {}
    match["type"] = "ceramic_resonator"
    match["size"] = "3213"
    match["color"] = "3_pin_ground_pin_2"
    match["footprint_name"] = "kicad_crystal_resonator_smd_murata_cstxexxv_3pin_3_0x1_1mm"
    matches.append(match)


    ###### header
    #for pins 1-40
    for pin_count in range(1, 41):
        #regular pin through hole
        pin_s = str(pin_count).zfill(2)
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm"
        match["description_main"] = f"{pin_count}_pin"
        match["footprint"] = []
        match["footprint_name"] = f"kicad_connector_pinheader_2_54mm_pinheader_1x{pin_s}_p2_54mm_vertical"
        matches.append(match)   
        #surface mount regular
        if pin_count > 1: ##skip the 10 plus varriants
            match = {}
            match["type"] = "header"
            match["size"] = "2d54_mm"
            match["description_main"] = f"{pin_count}_pin"
            match["description_extra"] = "surface_mount"
            match["footprint_name"] = f"kicad_connector_pinheader_2_54mm_pinheader_1x{pin_s}_p2_54mm_vertical_smd_pin1left"
            matches.append(match)  
        #surface mount right angle
        if pin_count < 21 and pin_count > 2 : ##skip the 10 plus varriants
            match = {}
            match["type"] = "header"
            match["size"] = "2d54_mm"
            match["description_main"] = f"{pin_count}_pin"
            match["description_extra"] = "surface_mount_right_angle"
            match["footprint_name"] = f"kicad_connector_harwin_harwin_m20_890{pin_s}xx_1x{pin_s}_p2_54mm_horizontal"
            matches.append(match) 
        if pin_count > 1: ##skip the 1 pin varriant
            #jst sh
            match = {}
            match["type"] = "header"
            match["size"] = "1_mm_jst_sh"
            match["description_main"] = f"{pin_count}_pin"
            match["description_extra"] = "surface_mount_right_angle"
            match["footprint_name"] = f"kicad_connector_jst_jst_sh_sm{pin_s}b_srss_tb_1x{pin_s}_1mp_p1_00mm_horizontal"
            matches.append(match) 

    #dual row
    for pin_count in range(4, 40, 2):
        pin_s = str(pin_count).zfill(2)
        pin_s2x = str(int(pin_count/2)).zfill(2)
        match = {}
        match["type"] = "header"
        match["size"] = "2d54_mm_dual_row"
        match["description_main"] = f"2x{int(pin_count/2)}_dual_row_{pin_count}_pin"
        match["description_extra"] = ""
        match["footprint_name"] = f"kicad_connector_pinheader_2_54mm_pinheader_2x{pin_s2x}_p2_54mm_vertical"
        matches.append(match) 

    ###### ic

    match = {}
    match["size"] = "soic_28_wide"
    match["footprint"] = []
    match["footprint_name"] = f"kicad_package_so_soic_28w_7_5x17_9mm_p1_27mm"
    matches.append(match)  

    

    #for pins 1-40
    ###### is dip
    for pin_count in range(2, 40, 2):
        #regular pin through hole
        pin_s = str(pin_count).zfill(2)

        match = {}
        match["size"] = f"dip_{pin_s}"
        match["footprint_name"] = f"kicad_package_dip_dip_{pin_s}_w7_62mm"
        matches.append(match)  

    ###### ic mlf (also called vqfn by microchip)
    match = {}
    match["size"] = "mlf_32"
    match["footprint_name"] = f"kicad_package_dfn_qfn_vqfn_32_1ep_5x5mm_p0_5mm_ep3_1x3_1mm"
    matches.append(match) 
    
    ###### ic tqfp #microchip calls the pitch 1mm kicad 0.8mm 
    match = {}
    match["size"] = "tqfp_32"
    match["footprint_name"] = f"kicad_package_qfp_tqfp_32_7x7mm_p0_8mm"
    matches.append(match) 
    ###### ic qfn
    match = {}
    match["size"] = "qfn_32"
    match["footprint_name"] = f"kicad_package_dfn_qfn_qfn_32_1ep_5x5mm_p0_5mm_ep3_1x3_1mm"
    matches.append(match) 
    
    ###### ic vqfn
    match = {}
    match["size"] = "vqfn_28"
    match["footprint_name"] = f"kicad_package_dfn_qfn_vqfn_28_1ep_4x4mm_p0_45mm_ep2_4x2_4mm"
    matches.append(match)  

    ###### led
    match = {}
    match["type"] = "led"
    match["size"] = "5_mm"
    match["footprint_name"] = f"kicad_led_tht_led_d5_0mm"
    matches.append(match)  
    match = {}
    match["type"] = "led"
    match["size"] = "10_mm"
    match["footprint_name"] = f"kicad_led_tht_led_d10_0mm"
    matches.append(match)  
    match = {}
    match["type"] = "led"
    match["size"] = "0603"
    match["footprint_name"] = f"kicad_led_smd_led_0603_1608metric"
    matches.append(match)  


    ###### nettie
    nets = ["2","3","4"]
    for net in nets:
        match = {}
        match["type"] = "nettie"
        match["size"] = f"{net}_nets"
        match["description_main"] = "smd"
        match["footprint_name"] = f"kicad_nettie_nettie_{net}_smd_pad0_5mm"
        matches.append(match)  
        match = {}
        match["type"] = "nettie"
        match["size"] = f"{net}_nets"
        match["description_main"] = "through_hole"
        match["footprint_name"] = f"kicad_nettie_nettie_{net}_tht_pad0_3mm"
        matches.append(match)  



    ###### sod
    match = {}
    match["size"] = "sod_123"
    match["footprint_name"] = f"kicad_diode_smd_d_sod_123"
    matches.append(match)  
    

    ###### sop
    match = {}
    match["size"] = "sop_16"
    match["footprint_name"] = f"kicad_package_so_sop_16_3_9x9_9mm_p1_27mm"
    matches.append(match)  
    


    ###### led

    match = {}
    match["classification"] = "electronic"
    match["type"] = "led"
    match["size"] = "5_mm"
    match["footprint_name"] = f"kicad_led_tht_led_d5_00mm"
    matches.append(match)  

    ###### mounting_holes

    match["type"] = "mounting_hole"
    match["size"] = "m3"
    match["footprint_name"] = f"kicad_mountinghole_mountinghole_3_2mm_m3"
    matches.append(match)  

    match["type"] = "mounting_hole"
    match["size"] = "m6"
    match["footprint_name"] = f"kicad_mountinghole_mountinghole_6_4mm_m6"
    matches.append(match)  


    ###### resistor
    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["size"] = "0603"
    match["footprint_name"] = f"kicad_resistor_smd_r_0603_1608metric"
    matches.append(match)  
    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["size"] = "0805"
    match["footprint_name"] = f"kicad_resistor_smd_r_0805_2012metric"
    matches.append(match)
    
    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["size"] = "1206"
    match["footprint_name"] = f"kicad_resistor_smd_r_1206_3216metric"
    matches.append(match)

    match = {}
    match["classification"] = "electronic"
    match["type"] = "resistor"
    match["size"] = "quarter_watt_through_hole"
    match["footprint_name"] = f"kicad_resistor_tht_r_axial_din0207_l6_3mm_d2_5mm_p7_62mm_horizontal"
    matches.append(match)
       

    ###### socket    
    match = {}
    match["type"] = "socket"
    match["size"] = "usb_mini"
    match["description_main"] = "surface_mount_only"
    match["footprint_name"] = f"kicad_connector_usb_usb_mini_b_wuerth_65100516121_horizontal"
    matches.append(match)   


    ###### transistor and pmic sizes
    match = {}
    match["size"] = "sot_223"
    match["footprint_name"] = f"kicad_package_to_sot_smd_sot_223_3_tabpin2"
    matches.append(match)  
    




    footprints = []
    #go through the keys in oomp.names_of_main_elements if all the values in match match (ignore non mentioned keys) then add it to footprints
    for match in matches:
        if "footprint_name" in match:
            footprint_name = match["footprint_name"]
            match["footprint"] = []
            match["footprint"].append({"link": f"{github_footprint_base}/{footprint_name}", 
                            "oomp_key": f"oomp_{footprint_name}",                                 
                            "directory": f"{directory_footprint_base}/{footprint_name}/{directory_footprint_end}"})
            #remove footprint_name
            del match["footprint_name"]
        
        match_count = 0
        # get a list with oomp.names_of_main_elements and "id"
        elements_to_check = oomp.names_of_main_elements.copy()
        elements_to_check.append("id")
        for name in elements_to_check:
            try:
                if match[name] == kwargs[name]:
                    match_count += 1
            except:
                pass
                #value not in match check
        if match_count == len(match)-1:
            footprints.extend(match["footprint"])

    if len(footprints) > 0:
        kwargs["footprint"] = footprints
    return kwargs