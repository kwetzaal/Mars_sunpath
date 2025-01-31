import numpy as np
import matplotlib.pyplot as plt

def solar_altitude_calculations(Ls, time, lat):
    solar_alt = []
    i = 0
    while i < len(time):
        hour_angle = np.deg2rad(15*time[i]-180) #time in martian hour (1/24 sol)

        declination = np.arcsin(0.42565*np.sin(Ls))+0.25*(np.sin(Ls)) # From JPL

        #declination = np.deg2rad(25.2 * np.sin(np.deg2rad((360*(day-1))/687))) # for day not Ls

        # From Earth models
        solar_altitude = np.rad2deg(np.arcsin(np.sin(lat)*np.sin(declination)+np.cos(lat)*np.cos(declination)*np.cos(hour_angle)))

        # from NASA JPL
        #solar_zenith = np.arccos(np.sin(declination)*np.sin(lat)+np.cos(declination)*np.cos(lat)*np.cos(hour_angle))
        #solar_altitude = 90 - np.rad2deg(solar_zenith)

        solar_alt.append(solar_altitude)
        i += 1
    return solar_alt

def solar_azimuth_calculations(Ls, time, lat, solar_altitude):
    solar_azi = []
    i = 0
    while i < len(time):
        hour_angle = np.deg2rad(15*time[i]-180) #time in martian hour (1/24 sol)

        declination = np.arcsin(0.42565*np.sin(Ls))+0.25*(np.sin(Ls)) # from JPL

        #declination = np.deg2rad(25.2 * np.sin(np.deg2rad((360*(day-1))/687))) # for day not Ls

        # From Earth models
        solar_azimuth = np.rad2deg(np.arcsin(np.cos(declination)*np.sin(hour_angle)/np.cos(np.deg2rad(solar_altitude[i]))))

        # from NASA JPL
        #solar_azimuth = np.arctan((np.sin(hour_angle))/(np.cos(lat)*np.tan(declination)-np.sin(lat)*np.cos(hour_angle)))
        #solar_azi.append(np.rad2deg(solar_azimuth))

        solar_azi.append(solar_azimuth)
        i += 1
    return solar_azi

def main():
    #intitialize values
    sol_long = input("Input solar longitude (deg): ")
    Ls = np.deg2rad(sol_long)

    # choice of time values
    full_time = np.arange(0, 24, 0.5)
    day_time = np.arange(6, 18, 0.1)
    select = False
    while select == False:
        time_choice = input("Please select Full day (F) or Half day(H):")
        if time_choice == "F":
            time = full_time
            select = True
        elif time_choice == "H":
            time = day_time
            select = True
        else:
            print("Please select a valid option (F/H)")

    # calculations for different latitudes
    solar_altitude_0 = solar_altitude_calculations(Ls, time, np.deg2rad(1e-3))
    solar_azimuth_0 = solar_azimuth_calculations(Ls, time, np.deg2rad(1e-3), solar_altitude_0)

    solar_altitude_15 = solar_altitude_calculations(Ls, time, np.deg2rad(15))
    solar_azimuth_15 = solar_azimuth_calculations(Ls, time, np.deg2rad(15), solar_altitude_15)

    solar_altitude_30 = solar_altitude_calculations(Ls, time, np.deg2rad(30))
    solar_azimuth_30 = solar_azimuth_calculations(Ls, time, np.deg2rad(30), solar_altitude_30)

    solar_altitude_60 = solar_altitude_calculations(Ls, time, np.deg2rad(60))
    solar_azimuth_60 = solar_azimuth_calculations(Ls, time, np.deg2rad(60), solar_altitude_60)

    solar_altitude_90 = solar_altitude_calculations(Ls, time, np.deg2rad(90))
    solar_azimuth_90 = solar_azimuth_calculations(Ls, time, np.deg2rad(90), solar_altitude_90)

    # plots all altitudes and azimuths
        # plot for solar altitude vs. time
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(time, solar_altitude_0, label = "lat = 0")
    axs[0, 0].plot(time, solar_altitude_15, label = "lat = 15")
    axs[0, 0].plot(time, solar_altitude_30, label = "lat = 30")
    axs[0, 0].plot(time, solar_altitude_60, label = "lat = 60")
    axs[0, 0].plot(time, solar_altitude_90, label = "lat = 90")
    axs[0, 0].set_title("Solar Altitude vs. Time")
    axs[0, 0].grid()
    axs[0, 0].legend()

        # plot for solar azimuth vs. time
    axs[0, 1].plot(time, solar_azimuth_0, label = "lat = 0")
    axs[0, 1].plot(time, solar_azimuth_15, label = "lat = 15")
    axs[0, 1].plot(time, solar_azimuth_30, label = "lat = 30")
    axs[0, 1].plot(time, solar_azimuth_60, label = "lat = 60")
    axs[0, 1].plot(time, solar_azimuth_90, label = "lat = 90")
    axs[0, 1].set_title("Solar Azimuth vs. Time")
    axs[0, 1].grid()
    axs[0, 1].legend()

        # plot for solar altitude vs. solar azimuth
    axs[1, 0].plot(solar_azimuth_0, solar_altitude_0, label = "lat = 0")
    axs[1, 0].plot(solar_azimuth_15, solar_altitude_15, label = "lat = 15")
    axs[1, 0].plot(solar_azimuth_30, solar_altitude_30, label = "lat = 30")
    axs[1, 0].plot(solar_azimuth_60, solar_altitude_60, label = "lat = 60")
    axs[1, 0].plot(solar_azimuth_90, solar_altitude_90, label = "lat = 90")
    axs[1, 0].set_title("Solar Azimuth vs. Solar Altitude")
    axs[1, 0].grid()
    axs[1, 0].legend()

    plt.show()

if __name__ == "__main__":
    main()