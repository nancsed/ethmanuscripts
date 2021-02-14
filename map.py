from flask import Flask, render_template, url_for
import pandas as pd
import folium 

app = Flask(__name__)


googleSheetId = '15LtAukjlmXovxdvoAcPDQgalJmv6ZT7aYjmq8E5ilD0'

workSheetName = 'cent_df'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)

cols =['Century', 'Latitude','Longitude']

df = pd.read_csv(url, usecols=cols)

clr = 'Red'

@app.route('/')

def index():
    start_coords = (9.1450, 40.4897)
    c_map = folium.Map(location=start_coords, max_zoom=7,zoom_start=6)
    for (index,row) in df.iterrows():
        folium.CircleMarker(location=[row.loc['Latitude'], row.loc['Longitude']],
                 radius=10,popup=row.loc['Century'],color='#000000', fill=True, fill_color=clr,
                 tooltip=row.loc['Century']).add_to(c_map)
    return c_map._repr_html_()


  
   



# def index():
#     return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)