import numpy as np
import matplotlib.pyplot as plt

def solar_altitude_calculations(Ls, time, lat):
    solar_alt = []
    i = 0
    while i < len(time):
        #axial_tilt = np.deg2rad(24.936) #24.936 is axial tilt

        declination = np.arcsin(0.42565*np.sin(Ls))*0.25*np.sin(Ls)
        hour_angle = np.deg2rad(15*(time[i]-12)) #time in martian hour (1/24 sol)

        #solar_altitude = np.arcsin(np.sin(np.deg2rad(lat))*np.sin(declination)+np.cos(np.deg2rad(lat))*np.cos(declination)*np.cos(np.deg2rad(hour_angle)))
        solar_zenith = np.arccos(np.sin(declination)*np.cos(lat)+np.cos(declination)**np.sin(lat)*np.cos(hour_angle))
        solar_altitude = 90-np.rad2deg(solar_zenith)
        solar_alt.append(solar_altitude)
        i += 1
    return solar_alt

def solar_azimuth_calculations(Ls, time, lat, solar_altitude):
    solar_azi = []
    i = 0
    while i < len(time):

        declination = np.arcsin(0.42565*np.sin(Ls))*0.25*np.sin(Ls)
        hour_angle = np.deg2rad(15*(time[i]-12)) #time in martian hour (1/24 sol)
        
        #solar_azimuth = np.arccos(np.cos(declination)*np.sin(np.deg2rad(hour_angle))/np.cos(np.deg2rad(solar_altitude[i])))

        # equation 6
        #solar_azimuth = np.arccos(np.sin(np.deg2rad(lat))*np.cos(np.deg2rad(90-solar_altitude[i]))-np.sin(declination))/(np.cos(np.deg2rad(lat))*np.sin(np.deg2rad(90-solar_altitude[1])))

        solar_azimuth = np.arctan(np.sin(hour_angle)/(np.cos(lat)*np.tan(declination)-np.sin(lat)*np.cos(hour_angle)))
        solar_azi.append(np.rad2deg(solar_azimuth)+180)

        i += 1
    return solar_azi

def main():
    #Ls = int(input("Solar Longitude: "))
    #n = int(input("nth orbit of Mars since Aug 26, 1996 (Vernal Equinox): "))
    #Ls = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]

    Ls = np.deg2rad(0)
    full_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    day_time = np.arange(6, 18, 0.1)
    time = day_time
    lat = np.deg2rad(40) #0 Ls and 0 lat breaks the code and IDK how to fix it :(
    if lat == 0:
        lat = 0.1e-3


    solar_altitude = solar_altitude_calculations(Ls, time, lat)
    solar_azimuth = solar_azimuth_calculations(Ls, time, lat, solar_altitude)

    print(solar_altitude)
    print(solar_azimuth)

    x_scale = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
    y_scale = [0, 30, 60, 90, 180, 210, 240, 270, 300, 330, 360]
    plt.plot(solar_azimuth, solar_altitude)
    # plt.plot(solar_azimuth, solar_altitude)
    plt.xlabel("Solar Azimuth(deg)")
    #plt.xticks(x_scale)
    plt.ylabel("Solar Altitude(deg)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()