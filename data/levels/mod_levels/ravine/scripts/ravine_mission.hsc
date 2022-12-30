(global vehicle vh_start_phantom NONE)

(script command_script cs_start_phantom
    ;(if debug (print "Spawn Start Phantom"))
    (set vh_start_phantom (ai_vehicle_get_from_starting_location start_phantom/phantom))
        (ai_place start_phantom_01)
            (sleep 30)
    (ai_vehicle_enter_immediate start_phantom_01 vh_start_phantom "phantom_p_l")

	(cs_vehicle_speed .5)
    (cs_fly_by Phantom_Start/p0)
    (cs_fly_by Phantom_Start/p1)
    (cs_fly_by Phantom_Start/p2)
    (cs_fly_to Phantom_Start/p3)
    ;(vehicle_hover vh_start_phantom TRUE)
 
    (unit_open vh_start_phantom)
    (begin 
        (vehicle_unload vh_start_phantom "phantom_p_l")
        (sleep (random_range 5 15))
    )

    (sleep 50)
    (unit_close vh_start_phantom)

    ;(vehicle_hover vh_start_phantom FALSE)
    (cs_fly_by Phantom_Start/p2)
    (cs_vehicle_boost TRUE)
    (cs_fly_to Phantom_Start/p4)
    (ai_erase ai_current_squad)
)