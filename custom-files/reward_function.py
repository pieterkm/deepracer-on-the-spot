import math

def reward_function(params) :

    #Modify peak speed reward setting
    peak_speed_reward = 2.4
    power_factor = 3

    # Read input variables
    x = params['x']
    y = params['y']
    #steps = params['steps']
    speed = params['speed']
    heading = params['heading']
    #progress = params['progress']
    waypoints = params['waypoints']
    is_offtrack = params['is_offtrack']
    #track_width = params['track_width']
    closest_waypoints = params['closest_waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    #distance_from_center = params['distance_from_center']
    #steering = abs(params['steering_angle']) # Only need the absolute steering angle

    reward = 1e-3

    # Choose the next waypoint ahead
    next_waypoint_index = closest_waypoints[1]
    look_ahead_distance = 5  # for example, look ahead 5 waypoints
    look_ahead_index = (next_waypoint_index + look_ahead_distance) % len(waypoints)
    look_ahead_waypoint = waypoints[look_ahead_index]

    # Calculate the desired heading towards the look-ahead waypoint
    waypoint_x, waypoint_y = look_ahead_waypoint
    desired_heading = math.degrees(math.atan2(waypoint_y - y, waypoint_x - x))
    
    # Calculate the difference between the current heading and the desired heading
    heading_diff = abs(desired_heading - heading)
    if heading_diff > 180:
        heading_diff = abs(360 - heading_diff)
        
    heading_factor = (1-(heading_diff/30))
        
    if is_offtrack or heading_diff > 30 or speed > 3:
        reward += 1e-3
    else:
        if all_wheels_on_track:
            reward +=(abs(5*(3-(abs(abs(((heading_diff/30)-1)*peak_speed_reward)-speed))))**power_factor)/10
    
    
    return float(reward)

