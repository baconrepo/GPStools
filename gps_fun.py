## gps plotting functions ##




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import operator
from PIL import Image, ImageDraw
import plotly.express as px
import plotly.graph_objects as go



class GPSf(object):
    """
    Class for fucking my shit up
    """



    def __init__(self,data_path, map_path, points):
        """
        param: data_path, path to gps data
        param: map_path, path to map
        param: points, corners of map    
        """
        self.data_path = data_path
        self.map_path = map_path
        self.points = points

        self.result_image = Image
        self.x_ticks = []
        self.y_ticks = []


    def plot_map(self, output='save', save_as='resultMap.png'):
        """
        function for plotting the map, choose to save or show
        
        param: output, plot OR save
        param: save_as, if save choose filename
        """

        self.get_ticks()
        fig,axis1 = plt.subplots(figsize(10,10))
        axis1.imshow(self.result_image)
        axis1.set_xlabel('Longitude')
        axis1.set_ylabel('Latitude')
        axis1.set_xticklabels(self.x_ticks)
        axis1.set_yticklabels(self.y_ticks)
        axis1.grid()

        if output == 'save':
            plt.savefig(save_as)
        elif output == 'show':
            plt.show()
        else:
            print("Something broke while plotting the map...")



    def get_corners(self, data_path):
        """
        method to get the extreme corners of gps data to set map coordinates

        param: lat_long, tuple containing lat long data
        """

        data = pd.read_csv(self.data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')
        gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))
    
        lat = sorted(gps_data, key=operator.itemgetter(0))    ##sorted list smallest to biggest
        long = sorted(gps_data, key=operator.itemgetter(1)) 
    
        sx = lat[0][0]
        bx = lat[-1][0]
        sy = long[0][-1]
        by = long[-1][-1]

       
        df = pd.read_csv(data_path)

        slat=df.sort_values(by=['autodrive_nav.latitude'])
        slon=df.sort_values(by=['autodrive_nav.longitude'])


        print("slat1", slat['autodrive_nav.latitude'][0])
        print("slong1", slon['autodrive_nav.longitude'][0])
        print("slatmax", slat['autodrive_nav.latitude'].iloc[-1])
        print("slonmax", slon['autodrive_nav.longitude'].iloc[-1])


     

        ##works for different data set not datadog
        """
        print("sx", sx)
        print("bx", bx)
        print("sy", sy)
        print("by", by)

        topr = bx,by 
        topl = sx, by 
        botl = sx, sy 
        botr = bx, sy 

        print("Top Right:", topr)
        print("Top Left:", topl)
        print("Bottom Right:", botr)
        print("Bottom Left:", botl)

        corners = [topr,topl,botr,botl]
        zip(*corners)
        plt.scatter(* zip(*corners))
        plt.title("GPS Corners Sanity Check...")
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")      
        plt.show()
        """

    def plot_datadog_navpoints(self,data_path):
        df = pd.read_csv(data_path)
        fig2=go.Figure()
        fig2.add_trace(go.Scattermapbox(lat=df['autodrive_nav.latitude'],lon=df['autodrive_nav.longitude'], mode='markers',marker=go.scattermapbox.Marker(size=14),text=df['Host'], name=str(df['Host'][0])))
        fig2.update_layout(showlegend=True)
        fig2.update_layout(legend={"title":"Hosts"})
        fig2.update_layout(mapbox_style="open-street-map")
        fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig2.show()

"""
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])

"""

    



def get_corners(self, data_path):
    """
    method to get the extreme corners of gps data to set map coordinates

    param: lat_long, tuple containing lat long data
    """

    data = pd.read_csv(self.data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')
    gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))

    lat = sorted(gps_data, key=operator.itemgetter(0))    ##sorted list smallest to biggest
    long = sorted(gps_data, key=operator.itemgetter(1)) 

    sx = lat[0][0]
    bx = lat[-1][0]
    sy = long[0][-1]
    by = long[-1][-1]

    print("sx", sx)
    print("bx", bx)
    print("sy", sy)
    print("by", by)

    topr = bx,by 
    topl = sx, by 
    botl = sx, sy 
    botr = bx, sy 

    print("Top Right:", topr)
    print("Top Left:", topl)
    print("Bottom Right:", botr)
    print("Bottom Left:", botl)

    corners = [topr,topl,botr,botl]
    zip(*corners)
    plt.scatter(* zip(*corners))
    plt.title("GPS Corners Sanity Check...")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")      
    plt.show()










































































































































































































































































