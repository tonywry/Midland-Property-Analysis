
# Input Dataset
import pandas as pd
dataset = pd.read_csv("midland_data_cleansed.csv")
dataset = dataset.iloc[:,1:]


# Find outliers by ploting distribution density
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
dataset['sell_price'].hist(bins=20,ax=ax, edgecolor='k',normed=1)
dataset['sell_price'].plot(kind='kde',ax=ax)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
dataset['net_area'].hist(bins=20,ax=ax, edgecolor='k',normed=1)
dataset['net_area'].plot(kind='kde',ax=ax)


# Remove the outliers
dataset = dataset[dataset["sell_price"]<25]
dataset = dataset[dataset["net_area"]<1500]


##### Explore Selling Price distribution vs Renting Price Distribution

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
dataset['sell_price'].hist(bins=20,ax=ax, edgecolor='k',normed=1)
plt.xlabel("selling price")
dataset['sell_price'].plot(kind='kde',ax=ax)


dataset_rent = dataset[dataset["rent_price"]>0]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
dataset_rent['rent_price'].hist(bins=30,ax=ax, edgecolor='k',normed=1)
plt.xlabel("renting price")
dataset_rent['rent_price'].plot(kind='kde',ax=ax)



# Box Plot for layout against area
import seaborn as sns
dataset_layout = dataset[dataset["layout"]>0]
dataset_layout = dataset_layout.iloc[:,[0,2,5]]
sns.boxplot(x="layout", y="net_area", data=dataset_layout, palette="Set1");
plt.title("Box-Plot for layout against area")


# Box-Plot for layout against selling price
sns.set_style("darkgrid")
sns.boxplot(x="layout", y="sell_price", data=dataset_layout, palette="Set1");
plt.title("Box-Plot for layout against selling price")



# Box-Plot for orientation against selling price
dataset_orit = dataset[dataset["orit"] != ""]
sns.boxplot(x="orit", y="sell_price", data=dataset_orit, palette="Set1");
plt.title("Box-Plot for orientation against selling price")


#########################################
# Scatter plot the properties on HK map #
#########################################

# Keep the data where both Latitude and Longitude can be found
dataset_basemap = dataset[dataset["latitude"] > 0]
dataset_basemap = dataset_basemap[dataset_basemap["longitude"] > 0]

# define size of the scatter, larger size the property, larger size the scatter
def pltsize(l):
    if l < 300:
        size = 0.1
    elif l < 400:
        size = 0.2
    elif l < 500:
        size = 0.5
    elif l < 600:
        size = 0.8
    elif l < 700:
        size = 1
    elif l < 800:
        size = 3
    elif l < 900:
        size = 5
    elif l < 1000:
        size = 7
    elif l < 1500:
        size = 9
    elif l < 2000:
        size = 10
    else:
        size = 11
    return size



from mpl_toolkits.basemap import Basemap

my_dpi=300
plt.figure(figsize=(1500/my_dpi, 1200/my_dpi), dpi=my_dpi)

m = Basemap(llcrnrlon=113.8,llcrnrlat=22.15,urcrnrlon=114.5,urcrnrlat=22.52, resolution="h", epsg=2326)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")

lons = list(dataset_basemap['longitude'])
lats = list(dataset_basemap['latitude'])
sizes = [pltsize(z) for z in dataset_basemap['net_area']]
cols = [w for w in round(dataset_basemap["sell_price"])]

x, y = m(lons, lats)

m.scatter(x, y, s=sizes, cmap="Set1")








### Another Map, color by selling price
# define color of the marker, more expensive the property, more red
def pltcolor(l):
    if l < 3:
        col = 'lightcyan'
    elif l < 4:
        col = 'lightskyblue'
    elif l < 5:
        col = 'paleturquoise'
    elif l < 6:
        col = 'lightsteelblue'
    elif l < 7:
        col = 'powderblue'
    elif l < 8:
        col = 'lightblue'
    elif l < 9:
        col = 'skyblue'
    elif l < 10:
        col = 'salmon'
    elif l < 15:
        col = 'violet'
    elif l < 20:
        col = 'magenta'
    else:
        col = 'crimson'
    return col



from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches

my_dpi=100
plt.figure(figsize=(1500/my_dpi, 1200/my_dpi), dpi=my_dpi)

#codes to produce the map
m = Basemap(llcrnrlon=113.8,llcrnrlat=22.15,urcrnrlon=114.5,urcrnrlat=22.53)

#read the shapefile for Hong Kong
m.readshapefile('gadm36_HKG_1', 'hong kong', drawbounds=True, color='grey')

lons = list(dataset_basemap['longitude'])
lats = list(dataset_basemap['latitude'])
sell_price = list(dataset_basemap['sell_price'])
cols = [pltcolor(w) for w in round(dataset_basemap["sell_price"])]

# Define the legend
levels = [mpatches.Patch(color='lightcyan', label='<3M'),
          mpatches.Patch(color='lightskyblue', label='<4M'),
          mpatches.Patch(color='paleturquoise', label='<5M'),
          mpatches.Patch(color='lightsteelblue', label='<6M'),
          mpatches.Patch(color='powderblue', label='<7M'),
          mpatches.Patch(color='lightblue', label='<8M'),
          mpatches.Patch(color='skyblue', label='<9M'),
          mpatches.Patch(color='salmon', label='<10M'),
          mpatches.Patch(color='violet', label='<15M'),
          mpatches.Patch(color='magenta', label='<20M'),
          mpatches.Patch(color='crimson', label='>20M')]

plt.legend(handles=levels, title='selling price',bbox_to_anchor=(1.0, 1.0))

for i in range(len(cols)):
    x, y = m(lons[i],lats[i])
    m.plot(x, y, marker='o', markerfacecolor=cols[i], markersize=5)

