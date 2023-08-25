# -*- coding: utf-8 -*-
"""
Plota mapa do Brasil e área de estudo CPRM do projeto Carajás
REPÚBLICA FEDERATIVA DO BRASIL
MINISTÉRIO DE MINAS E ENERGIA – MME
SECRETARIA DE GEOLOGIA, MINERAÇÃO E TRANSFORMAÇÃO MINERAL – SGM
CPRM - SERVIÇO GEOLÓGICO DO BRASIL
PROGRAMA GEOLOGIA DO BRASIL (PGB)
LEVANTAMENTO AEROGRAVIMÉTRICO
CARAJÁS
RELATÓRIO FINAL DO LEVANTAMENTO E PROCESSAMENTO DOS DADOS 
MAGNETOMÉTRICOS E GRAVIMÉTRICOS
VOLUME I
TEXTO TÉCNICO

Tabela 1  Coordenadas da Área.
Foram utilizadas as seguintes aeronaves para a execução destes projetos: Cessna 
Caravan C208-B, prefixos PR-FAS e PP-AGP.
Figura 3 – Aeronave Cessna C-208B Caravan – PR-FAS.
Figura 4 – Aeronave Cessna C-208B Caravan – PP-AGP.
Vértice
Este Norte Longitude Latitude (UTM Zona 22 Sul)
1 278246,65 9446998,28 -53º00’00” -5º00’00”
2 666300,36 9447145,94 -49º30’00” -5º00’00”
3 665317,06 9115400,93 -49º30’00” -8º00’00”
4 279558,30 9115166,53 -53º00’00” -8º00’00”



"""
import pandas as pd
import geopandas 
from shapely.geometry import Point
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

df = geopandas.read_file('shapefiles/lim_unidade_federacao_a.shp')

# Area do projeto Carajas em latitude e longitude
p1 = Polygon([(-53, -5), (-49.5, -5), (-49.5,-8),(-53, -8)])
print(p1)

f, ax = plt.subplots(1, figsize=(5, 5))
ax = df.plot(axes=ax)

poly_union =  geopandas.GeoSeries(p1)

ax = df.plot(axes=ax)
poly_union.plot(axes=ax, color='red')

#lims = plt.axis('equal')

ax.set_ylim([-35, 6])
ax.set_xlim([-75, -33])

plt.xlabel('latitude  ($\circ$)' )
plt.ylabel('longitude  ($\circ$)' )
ax.grid()

plt.savefig('../manuscript/Fig/Brazil_map.png', dpi= 300)
plt.show()




