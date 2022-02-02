# Python
#### Comments
> тестовое задание на работу       


### FizzBizz
> Python v. 3.9.7

Папулярные алгоритмы    
1. sorting_by_bubble - сортировка пурырьком   
2. factorial - факториал числа
3. Fibonacci -  числа Фибоначчи
4. Lowenstein -  растояние левенштейна, нахождение кратчайшего пути между двух точек
  
  [Microsoft Access](https://www.microsoft.com/ru-ru/microsoft-365/access)
  [MySQL](https://www.mysql.com/downloads)



### Карта Марса 
[ссылка на источник](https://habr.com/ru/company/skillfactory/blog/649097/)
~~~
      import rasterio
      import numpy as np
      
      mars = rasterio.open('../../Planets/mars/data/Mars_MGS_MOLA_DEM_mosaic_global_463m.tif')
      mars = mars.read()
      
      print(mars.shape)
      print(np.amin(mars[0]))
      print(np.amax(mars[0]))
      print(np.amax(mars[0]) + abs(np.amin(mars[0])))
      
            
      import matplotlib.pyplot as plt
      fig, ax = plt.subplots()
      fig.set_size_inches(14, 7)

      ax.imshow(mars[0], cmap="viridis")
      ax.axis('off')

      plt.show()
      
      
      from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap
import numpy as np

custom_cmap = LinearSegmentedColormap.from_list('mars', ['#162252',
                                                         '#104E8B',
                                                         '#00B2EE',
                                                         '#00FF00',
                                                         '#FFFF00',
                                                         '#FFA500',
                                                         '#FF0000',
                                                         '#8b0000',
                                                         '#964B00',
                                                         '#808080',
                                                         '#FFFFFF'], N=2221)

bounds = np.arange(-8210, 14000, 10)
norm = BoundaryNorm(bounds, custom_cmap.N)
      
      
      
fig, ax = plt.subplots()
fig.set_size_inches(14, 7)

ax.imshow(mars[0], cmap=custom_cmap, norm=norm)
ax.axis('off')
logo = plt.imread('../../Branding/globe_black.png')
newax = fig.add_axes([0.82, 0.13, 0.08, 0.08], anchor='NE')
newax.imshow(logo)
newax.axis('off')
txt = ax.text(0.0, 0.02, "Martian Topography \n@PythonMaps",
              size=4,
              color='white',
              transform = ax.transAxes)
plt.show()


def label_features(ax):

     ax.text(5000, 8400, "Olympus\n Mons")
     ax.text(7000, 10000, "Ascreaus\n Mons")
     ax.text(6200, 11500, "Pavonis\n Mons")
     ax.text(5000, 13000, "Arsia\n Mons")
     ax.text(8500, 13000, "Tharsis", rotation=45)
     ax.text(12000, 14000, "Vallies\n Marineris")
     ax.text(17000, 18000, "Argyre")
     ax.text(20000, 2000, "Vastitas Borealis")
     ax.text(17000, 8500, "Chryse\n Planitia")
     ax.text(20000, 5000, "Acidalia Planitia")
     ax.text(30000, 16500, "Hellas", color='white')
     ax.text(37000, 5000, "Utopia\n Planitia")
     ax.text(41000, 8000, "Elysium")
     ax.text(34000, 9800, "Isidis")
     ax.text(7000, 5000, "Alba Patera")
     ax.text(2000, 6500, "Amazonis\n Planitia")

     return ax

fig, ax = plt.subplots()
fig.set_size_inches(14, 7)

ax.imshow(mars[0], cmap=custom_cmap, norm=norm)
ax = label_features(ax)
ax.axis('off')
newax = fig.add_axes([0.82, 0.13, 0.08, 0.08], anchor='NE')
newax.imshow(logo)
newax.axis('off')
txt = ax.text(0.0, 0.02, "Martian Topography \n@PythonMaps",
              size=4,
              color='white',
              transform = ax.transAxes)
plt.show()



colors_undersea = plt.cm.ocean(np.linspace(0.2, 0.8, 821))
undersea_map = LinearSegmentedColormap.from_list('undersea_map', colors_undersea, N=821)

colors_land = plt.cm.terrain(np.linspace(0.25, 1, 1400))
land_map = LinearSegmentedColormap.from_list('land_map', colors_land, N=1400)

colors = np.vstack((colors_undersea, colors_land))
terrain_map = LinearSegmentedColormap.from_list('cut_terrain', colors, N=2221)

bounds = np.arange(-8210, 14000, 10)
norm = BoundaryNorm(bounds, terrain_map.N)



def label_features_terrain(ax):
    ax.text(5000, 8400, "Olympus\n Mons")
    ax.text(7000, 10000, "Ascreaus\n Mons")
    ax.text(6200, 11500, "Pavonis\n Mons")
    ax.text(5000, 13000, "Arsia\n Mons")
    ax.text(8500, 13000, "Tharsis", rotation=45)
    ax.text(12000, 14000, "Vallies\n Marineris")
    ax.text(17000, 18000, "Argyre", color='white')
    ax.text(20000, 2000, "Vastitas Borealis", color='white')
    ax.text(17000, 8500, "Chryse\n Planitia", color='white')
    ax.text(20000, 5000, "Acidalia Planitia", color='white')
    ax.text(30000, 16500, "Hellas", color='white')
    ax.text(37000, 5000, "Utopia\n Planitia", color='white')
    ax.text(41000, 8000, "Elysium")
    ax.text(34000, 9800, "Isidis", color='white')
    ax.text(7000, 5000, "Alba Patera")
    ax.text(2000, 6500, "Amazonis\n Planitia", color='white')
    return ax

fig, ax = plt.subplots()
fig.set_size_inches(14, 7)

ax.imshow(mars[0], cmap=terrain_map, norm=norm)
ax = label_features_terrain(ax)
ax.axis('off')
newax = fig.add_axes([0.82, 0.13, 0.08, 0.08], anchor='NE')
newax.imshow(logo)
newax.axis('off')
txt = ax.text(0.0, 0.02, "Martian Topography \n@PythonMaps",
              size=4,
              color='white',
              transform = ax.transAxes)
plt.show()



def change_sea_level(new_sea_level):
    new_sea_level = new_sea_level / 10
    undersea = int(800 + new_sea_level)
    land = int(1400 - new_sea_level)
    colors_undersea = plt.cm.ocean(np.linspace(0.2, 0.8, undersea))
    undersea_map = LinearSegmentedColormap.from_list('undersea_map', colors_undersea, N=undersea)

    colors_land = plt.cm.terrain(np.linspace(0.25, 1, land))
    land_map = LinearSegmentedColormap.from_list('land_map', colors_land, N=land)

    colors = np.vstack((colors_undersea, colors_land))
    terrain_map = LinearSegmentedColormap.from_list('cut_terrain', colors, N=2221)

    bounds = np.arange(-8210, 14000, 10)
    norm = BoundaryNorm(bounds, terrain_map.N)
    return terrain_map, norm


terrain_map0, norm0 = change_sea_level(new_sea_level = 0)
terrain_map3000, norm3000 = change_sea_level(new_sea_level = 3000)
terrain_map_3000, norm_3000 = change_sea_level(new_sea_level = -3000)


terrain_map1500, norm1500 = change_sea_level(new_sea_level = 1500)

fig, ax = plt.subplots()
fig.set_size_inches(14, 7)

ax.imshow(mars[0], cmap=terrain_map1500, norm=norm1500)
ax = label_features_terrain(ax)
ax.axis('off')
newax = fig.add_axes([0.82, 0.13, 0.08, 0.08], anchor='NE')
newax.imshow(logo)
newax.axis('off')
txt = ax.text(0.0, 0.02, "Martian Topography \n@PythonMaps",
              size=4,
              color='white',
              transform = ax.transAxes)
plt.show()



import earthpy as et
import earthpy.spatial as es

hillshade = es.hillshade(mars[0], azimuth=250, altitude=1)
fig, ax = plt.subplots(facecolor='#FCF6F5FF')
fig.set_size_inches(14, 7)
ax.imshow(mars[0], cmap=terrain_map, norm=norm)
ax.imshow(hillshade, cmap="Greys", alpha=0.2)
ax = label_features_terrain(ax)
ax.axis('off')
newax = fig.add_axes([0.8, 0.78, 0.08, 0.08], anchor='NE')
newax.imshow(logo)
newax.axis('off')
txt = ax.text(0.02, 0.03, "Martian Topography \n@PythonMaps",
              size=8,
              color='black',
              transform = ax.transAxes)
plt.show()
