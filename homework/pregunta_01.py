"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones_bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    with open('files/input/clusters_report.txt', "r") as file:
      renglones = file.readlines()
  

    cols_l1 = re.split(r"\s{2,}", renglones[0].strip())
    cols_l2 = re.split(r"\s{2,}", renglones[1].strip())

    columnas = [cols_l1[0], cols_l1[1] + " " + cols_l2[0], cols_l1[2] + " " + cols_l2[1], cols_l1[3]]

    patron = r"^\s*(?:(\d+)\s+(\d+)\s+([\d.,]+)(?:\s*%)?\s+)?[ \t·]*(.*?[^\s\.])\s*(?:\.?)?$"

    texto = "".join(linea for linea in renglones[4:])

    fila_procesado = re.findall(patron, texto, re.DOTALL | re.MULTILINE)

    filas = [[cluster, cantidad, porcentaje, ""] for cluster, cantidad, porcentaje, _ in fila_procesado if cluster != ""]

    actual = -1
    for cluster, _, _, frag in fila_procesado:
        frag = re.sub(r"\s+", " ", frag).strip()
        if cluster:
            actual += 1
            filas[actual][3] = frag
        else:
            filas[actual][3] += " " + frag

    dataframe = pd.DataFrame({
        columnas[0].lower().replace(" ", "_"):[int(elemento[0]) for elemento in filas],
        columnas[1].lower().replace(" ", "_"):[int(elemento[1]) for elemento in filas],
        columnas[2].lower().replace(" ", "_"):[float(elemento[2].replace(",", ".")) for elemento in filas],
        columnas[3].lower().replace(" ", "_"):[elemento[3] for elemento in filas]
    })
    

    return dataframe
   

