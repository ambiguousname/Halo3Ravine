(global vehicle vh_start_phantom NONE)

(script command_script deploy
    (sleep 100)
    (cs_enable_pathfinding_failsafe TRUE)
	(ai_activity_abort ai_current_actor)
)

(script startup initial_wave
    (sleep_until 
        (or 
            (<= (ai_living_count start_squad) 2)
            (volume_test_objects start_phantom_vol (players))
        )
    )
    (ai_place start_phantom)
)

(script command_script cs_start_phantom
    (cs_enable_pathfinding_failsafe TRUE)
    ;(if debug (print "Spawn Start Phantom"))
    (set vh_start_phantom (ai_vehicle_get_from_starting_location start_phantom/phantom))
        (ai_place start_phantom_01)
            (sleep 30)
    (vehicle_load_magic vh_start_phantom "phantom_p_r" (ai_actors start_phantom_01))

	(cs_vehicle_speed 1)
    (cs_fly_by Phantom_Start/p0)
    (cs_fly_by Phantom_Start/p1)
    (cs_fly_by Phantom_Start/p2)
    (cs_fly_to Phantom_Start/p3)
    ;(vehicle_hover vh_start_phantom TRUE)
 
    (unit_open vh_start_phantom)
    (begin 
        (vehicle_unload vh_start_phantom "phantom_p_r")
        (sleep (random_range 5 15))
        (cs_run_command_script start_phantom_01 deploy)
    )

    (sleep 50)
    (unit_close vh_start_phantom)

    ;(vehicle_hover vh_start_phantom FALSE)
    (cs_fly_by Phantom_Start/p2)
    (cs_vehicle_boost TRUE)
    (cs_fly_to Phantom_Start/p4)
    (ai_erase ai_current_squad)
)