from skyfield.api import load, EarthSatellite, wgs84, utc
from datetime import datetime, timedelta
import plotly.graph_objects as go

def main():
    # TLE data
    tle_line1 = "1 52739U 22057H   22159.11954099  .00002612  00000+0  15663-3 0  9993"
    tle_line2 = "2 52739  97.5193 273.9452 0009301 198.3423 161.7473 15.11805174  2023"
    satellite = EarthSatellite(tle_line1, tle_line2, "OBJECT H")

    ts = load.timescale()
    now = datetime.now(utc)

    # Collect satellite positions
    lats, lons = [], []
    for minutes in range(0, 180, 5):
        t = ts.utc(now.year, now.month, now.day, now.hour, now.minute + minutes)
        geocentric = satellite.at(t)
        subpoint = wgs84.subpoint(geocentric)
        lats.append(subpoint.latitude.degrees)
        lons.append(subpoint.longitude.degrees)

    # Ground station location [NASA Kennedy Space Center Ground Station (KSC)]
    ground_lat = 28.572
    ground_lon = -80.648

    fig = go.Figure()

    # Satellite track
    fig.add_trace(go.Scattergeo(
        lat=lats,
        lon=lons,
        mode='lines+markers',
        line=dict(width=2, color='red'),
        marker=dict(size=4, color='blue'),
        name='Uydu Yolu'
    ))

    # Ground Station marker
    fig.add_trace(go.Scattergeo(
        lat=[ground_lat],
        lon=[ground_lon],
        mode='markers+text',
        marker=dict(size=10, color='green'),
        text=["Base Station"],
        textposition="top center",
        name="Base Station"
    ))

    # Earth map config
    fig.update_geos(
        projection_type="orthographic",
        showland=True, landcolor="rgb(243, 243, 243)",
        showocean=True, oceancolor="LightBlue",
        showcountries=True,
    )

    fig.update_layout(
        title="3D Satellite Tracking on Earth",
        margin=dict(l=0, r=0, t=30, b=0)
    )

    fig.write_html("satellite_track_3d.html")
    print("✅ created 3D map with ground station: satellite_track_3d.html")

if __name__ == "__main__":
    main()
