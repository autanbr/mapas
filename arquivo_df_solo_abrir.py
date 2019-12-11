from qgis.utils import iface

lista = list()
dicionario = {
'E:/MAPAS/uf_unidades_da_federacao/BRASILIA.shp':'brasilia', 
'E:/MAPAS/SOLOS/shape/arquivo_solo.shp':'solo'
}

for i in dicionario:
        iface.addVectorLayer(i, dicionario[i], "ogr")



