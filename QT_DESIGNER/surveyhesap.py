from PySide import QtCore, QtGui

from math import *
import os,os.path,shutil
from surveyui import Ui_Form

import osgeo.ogr

def derece(degrees):
    return degrees*((2*pi)/400)

class hesap(QtGui.QWidget):
    def __init__(self):
      QtGui.QWidget.__init__(self)

      self.ui = Ui_Form()
      self.ui.setupUi(self)

      # Validations
      tempValidator = QtGui.QDoubleValidator()
      tempValidator.setNotation(QtGui.QDoubleValidator.StandardNotation)
      self.ui.a.setValidator(tempValidator)
      self.ui.b.setValidator(tempValidator)
      self.ui.x1.setValidator(tempValidator)
      self.ui.y1.setValidator(tempValidator)
      self.ui.x2.setValidator(tempValidator)
      self.ui.y2.setValidator(tempValidator)
      self.ui.x3.setValidator(tempValidator)
      self.ui.y3.setValidator(tempValidator)
      self.ui.at.setValidator(tempValidator)
      self.ui.Rt.setValidator(tempValidator)
      self.ui.a_2.setValidator(tempValidator)
      self.ui.b_2.setValidator(tempValidator)
      self.ui.x1_2.setValidator(tempValidator)
      self.ui.y1_2.setValidator(tempValidator)
      self.ui.x2_2.setValidator(tempValidator)
      self.ui.y2_2.setValidator(tempValidator)
      '''self.ui.xp.setValidator(tempValidator)
      self.ui.yp.setValidator(tempValidator)'''

      
      self.ui.Ya_to1.setValidator(tempValidator)
      self.ui.Xa_to1.setValidator(tempValidator)
      self.ui.AB_to1.setValidator(tempValidator)
      self.ui.ABg_to1.setValidator(tempValidator)
      
      self.ui.Ya_to2.setValidator(tempValidator)
      self.ui.Xa_to2.setValidator(tempValidator)
      self.ui.Yb_to2.setValidator(tempValidator)
      self.ui.Xb_to2.setValidator(tempValidator)
      
      self.ui.ABg_to3.setValidator(tempValidator)
      self.ui.beta_to3.setValidator(tempValidator)
      
      self.ui.Ya_to4.setValidator(tempValidator)
      self.ui.Xa_to4.setValidator(tempValidator)
      self.ui.Yb_to4.setValidator(tempValidator)
      self.ui.Xb_to4.setValidator(tempValidator)
      self.ui.Xc_to4.setValidator(tempValidator)
      self.ui.Yc_to4.setValidator(tempValidator)
     
      # Signal/slot connections.
      self.setupConnections()

    def rapor(self):
        
        if os.path.exists("SINIR_KOORDINAT_RAPORU"):
            shutil.rmtree("SINIR_KOORDINAT_RAPORU")
        os.mkdir("SINIR_KOORDINAT_RAPORU")

        shapefile = osgeo.ogr.Open("SINIR.shp")
        layer = shapefile.GetLayer(0)

        for i in range(layer.GetFeatureCount()):
            feature = layer.GetFeature(i)
            name = feature.GetField("NAME")
            geometry = feature.GetGeometryRef()

            f = file(os.path.join("SINIR_KOORDINAT_RAPORU",
                          name + ".txt"), "w")
            f.write(geometry.ExportToWkt())
            f.close()

          
    '''def rendernow(self):
        symbolizer = mapnik2.PolygonSymbolizer(mapnik2.Color("red"))
        rule = mapnik2.Rule()
        rule.symbols.append(symbolizer)
        style = mapnik2.Style()
        style.rules.append(rule)
        layer = mapnik2.Layer("mapLayer")
        layer.datasource = mapnik2.Shapefile(file="render.shp")
        layer.styles.append("mapStyle")
        map = mapnik2.Map(8000, 5000)
        map.background = mapnik2.Color("green")
        map.append_style("mapStyle", style)
        map.layers.append(layer)
        map.zoom_all()
        mapnik2.render_to_file(map, "maprender.png", "png")//'''


    
    def calc(self):
      a = float(self.ui.at.text())
      R = float(self.ui.Rt.text())
      
      T=R*tan(derece(a/2))
      L=(2*pi*R*a)/400
      BS=(R/cos(derece(a/2)))-R

      self.ui.Tt.setText(str(T))
      self.ui.Lt.setText(str(L))
      self.ui.BSt.setText(str(BS))

    def temelodev1(self):

      ya1 = float(self.ui.Ya_to1.text())
      xa1 = float(self.ui.Xa_to1.text())
      ab1 = float(self.ui.AB_to1.text())
      abg1 = float(self.ui.ABg_to1.text())

      xb1=xa1+ab1*cos(derece(abg1))
      yb1=ya1+ab1*sin(derece(abg1))
      xb11=str(round(xb1,2))+" m"
      yb11=str(round(yb1,2))+" m"


      self.ui.Yb_to1.setText(str(yb11))
      self.ui.Xb_to1.setText(str(xb11))


    def temelodev2(self):
      ya2 = float(self.ui.Ya_to2.text())
      xa2 = float(self.ui.Xa_to2.text())
      yb2 = float(self.ui.Yb_to2.text())
      xb2 = float(self.ui.Xb_to2.text())

      dy=yb2-ya2
      dx=xb2-xa2
      

          
      ab2=sqrt((yb2-ya2)*(yb2-ya2)+(xb2-xa2)*(xb2-xa2))
      
      abg2=(200/pi)*atan(dy/dx)
      
      if dx>0 and dy>0:
          abg2=abg2
      if dx<0 and dy>0:
          abg2=abg2+200

      if dx<0 and dy<0:
          abg2=abg2+200
          
      if dx>0 and dy<0:
          abg2=abg2+400

      self.ui.AB_to2.setText(str(ab2))
      self.ui.ABg_to2.setText(str(abg2))
      #self.ui.AB_to2.setText(str(BS))
      #self.ui.ABg_to2.setText(str(BS))

    def temelodev3(self):
      abg3 = float(self.ui.ABg_to3.text())
      beta3 = float(self.ui.beta_to3.text())
       
      bc=abg3+beta3
      if bc<200:
          bc2=bc+200
          if bc2<0:
              bc2=bc2+200
       
      else:
          bc2=bc-200
          if bc2>400:
              bc2=bc2-400

      bc2=str(round(bc2,5))+" g"
      
      self.ui.BCg_to3.setText(str(bc2))
     
    def temelodev4(self):
      xa4 = float(self.ui.Xa_to4.text())
      ya4 = float(self.ui.Ya_to4.text())
      xb4 = float(self.ui.Xb_to4.text())
      yb4 = float(self.ui.Yb_to4.text())
      xc4 = float(self.ui.Xc_to4.text())
      yc4 = float(self.ui.Yc_to4.text())

      dy1=yc4-yb4
      dx1=xc4-xb4
      dy2=ya4-yb4
      dx2=xa4-xb4

      semtbc=(200/pi)*atan(dy1/dx1)
      semtba=(200/pi)*atan(dy2/dx2)

      if dx1>0 and dy1>0:
          semtbc=semtbc
      if dx1<0 and dy1>0:
          semtbc=semtbc+200

      if dx1<0 and dy1<0:
          semtbc=semtbc+200
          
      if dx1>0 and dy1<0:
          semtbc=semtbc+400



      if dx2>0 and dy2>0:
          semtba=semtba
      if dx2<0 and dy2>0:
          semtba=semtba+200

      if dx2<0 and dy2<0:
          semtba=semtba+200
          
      if dx2>0 and dy2<0:
          semtba=semtba+400


      if semtbc<semtba:
          abc=(semtbc+400)-semtba
      else:
          abc=semtbc-semtba

      abc=str(round(abc,5))+" g"

        
      self.ui.ABC_to4.setText(str(abc))
      
    def ilerdenkestir(self):
      bt = float(self.ui.b_2.text())
      at = float(self.ui.a_2.text())
     
      x1t = float(self.ui.x1_2.text())
      y1t = float(self.ui.y1_2.text())
      x2t = float(self.ui.x2_2.text())
      y2t = float(self.ui.y2_2.text())

      '''ypt = float(self.ui.yp.text())
      xpt = float(self.ui.xp.text())'''
      dx1=x2t-x1t
      dy1=y2t-y1t
      dx2=x1t-x2t
      dy2=y1t-y2t


      s=sqrt(dx1*dx1+dy1*dy1)

      t12=(200/pi)*atan(dy1/dx1)
      t21=(200/pi)*atan(dy2/dx2)
      
      # Aciklik Acisi Hesabi
      if dx1<0 and dy1>0:
          t12=t12+200

      if dx1<0 and dy1<0:
          t12=t12+200
          
      if dx1>0 and dy1<0:
          t12=t12+400
          
          
      if dx2<0 and dy2>0:
          t21=t21+200

      if dx2<0 and dy2<0:
          t21=t21+200
          
      if dx2>0 and dy2<0:
          t21=t21+400

      t1p=t12-at
      t2p=t21+bt

      s1=(s*sin(derece(bt)))/(sin(derece(at+bt)))
      s2=(s*sin(derece(at)))/(sin(derece(at+bt)))

      x1c=x1t+s1*cos(derece(t1p))
      y1c=y1t+s1*sin(derece(t1p))
      x2c=x2t+s2*cos(derece(t2p))
      y2c=y2t+s2*sin(derece(t2p))

      xpt=str(round((x1c+x2c)/2,3))+" m"
      ypt=str(round((y1c+y2c)/2,3))+" m"

      
      self.ui.yp_2.setText(str(ypt))
      self.ui.xp_2.setText(str(xpt))
    
    def kestir(self):
      bt = float(self.ui.b.text())
      at = float(self.ui.a.text())
     
      x1t = float(self.ui.x1.text())
      y1t = float(self.ui.y1.text())
      x2t = float(self.ui.x2.text())
      y2t = float(self.ui.y2.text())
      x3t = float(self.ui.x3.text())
      y3t = float(self.ui.y3.text())
      '''ypt = float(self.ui.yp.text())
      xpt = float(self.ui.xp.text())'''
      dx1=x2t-x1t
      dy1=y2t-y1t
      dx1t=x1t-x2t
      dy1t=y1t-y2t

      dx2=x2t-x3t
      dy2=y2t-y3t
      dx2t=x3t-x2t
      dy2t=y3t-y2t

      s1=sqrt(dx1*dx1+dy1*dy1)
      s2=sqrt(dx2*dx2+dy2*dy2)

      t12=(200/pi)*atan(dy1/dx1)
      t21=(200/pi)*atan(dy1t/dx1t)
      t32=(200/pi)*atan(dy2/dx2)
      t23=(200/pi)*atan(dy2t/dx2t)
      t3p=0
      
      # Aciklik Acisi Hesabi
      if dx1<0 and dy1>0:
          t12=t12+200

      if dx1<0 and dy1<0:
          t12=t12+200
          
      if dx1>0 and dy1<0:
          t12=t12+400
          
          
      if dx1t<0 and dy1t>0:
          t21=t21+200

      if dx1t<0 and dy1t<0:
          t21=t21+200
          
      if dx1t>0 and dy1t<0:
          t21=t21+400
          

      if dx2t<0 and dy2t>0:
          t23=t23+200

      if dx2t<0 and dy2t<0:
          t23=t23+200
          
      if dx2t>0 and dy2t<0:
          t23=t23+400


      if dx2<0 and dy2>0:
          t32=t32+200

      if dx2<0 and dy2<0:
          t32=t32+200
          
      if dx2>0 and dy2<0:
          t32=t32+400

      g=t21-t23
      k=400-(g+at+bt)
      mu=(200/pi)*atan((sin(derece(bt))*s1)/(sin(derece(at))*s2))
      k2=tan(derece((400-(at+bt+g))*.5))/tan(derece(50+mu))
      f=.5*(k+2*((200/pi)*atan(k2)))
      p=400-(g+at+bt)-f
      t1p=t12+f
      g2=200-(p+bt)
      t2p=t23+g2

      g1=200-(f+at)
      
      s11=s1*sin(derece(g1))/sin(derece(at))
      s33=s2*sin(derece(g2))/sin(derece(bt))
      x1c=x1t+s11*cos(derece(t1p))
      y1c=y1t+s11*sin(derece(t1p))
      #x2c=x2t+s*cos(derece(t2p))
      #y2c=y2t+s*sin(derece(t2p))
      x3c=x3t+s33*cos(derece(t3p))
      y3c=y3t+s33*cos(derece(t3p))

      xpt=str(round(x1c,3))+" m"
      ypt=str(round(y1c,3))+" m"


      
      '''xpt = (x1c+x3c)/2
      ypt= (y1c+y3c)/2'''
      
      self.ui.yp.setText(str(ypt))
      self.ui.xp.setText(str(xpt))

  
    def silk(self):
      self.ui.at.clear()
      self.ui.Rt.clear()
      self.ui.Tt.clear()
      self.ui.Lt.clear()
      self.ui.BSt.clear()
    def sil(self):
      self.ui.y3.clear()
      self.ui.y2.clear()
      self.ui.y1.clear()
      self.ui.x3.clear()
      self.ui.x2.clear()
      self.ui.x1.clear()
      self.ui.a.clear()
      self.ui.b.clear()
      self.ui.xp.clear()
      self.ui.yp.clear()
    def sili(self):
      self.ui.y2_2.clear()
      self.ui.y1_2.clear()
      self.ui.x2_2.clear()
      self.ui.x1_2.clear()
      self.ui.a_2.clear()
      self.ui.b_2.clear()
      self.ui.xp_2.clear()
      self.ui.yp_2.clear()
    def silp1(self):
        self.ui.Ya_to1.clear()
        self.ui.Xa_to1.clear()
        self.ui.Yb_to1.clear()
        self.ui.Xb_to1.clear()
        self.ui.AB_to1.clear()
        self.ui.ABg_to1.clear()
    def silp2(self):
        self.ui.Ya_to2.clear()
        self.ui.Xa_to2.clear()
        self.ui.Yb_to2.clear()
        self.ui.Xb_to2.clear()
        self.ui.AB_to2.clear()
        self.ui.ABg_to2.clear()
    def silp3(self):
        self.ui.BCg_to3.clear()
        self.ui.beta_to3.clear()
        self.ui.ABg_to3.clear()
    def silp4(self):
        self.ui.Ya_to4.clear()
        self.ui.Xa_to4.clear()
        self.ui.Yb_to4.clear()
        self.ui.Xb_to4.clear()
        self.ui.Yc_to4.clear()
        self.ui.Xc_to4.clear()
        self.ui.ABC_to4.clear()


    def setupConnections(self):
      self.connect(self.ui.hesapla_2, QtCore.SIGNAL('clicked()'),
          self.ilerdenkestir)
      self.connect(self.ui.hesapla, QtCore.SIGNAL('clicked()'),
          self.kestir)
     #self.connect(self.ui.render, QtCore.SIGNAL('clicked()'),self.rendernow)
      self.connect(self.ui.raporla, QtCore.SIGNAL('clicked()'),
          self.rapor)
      self.connect(self.ui.hesapla_to1, QtCore.SIGNAL('clicked()'),
          self.temelodev1)
      self.connect(self.ui.hesapla_to2, QtCore.SIGNAL('clicked()'),
          self.temelodev2)
      self.connect(self.ui.hesapla_to3, QtCore.SIGNAL('clicked()'),
          self.temelodev3)
      self.connect(self.ui.hesapla_to4, QtCore.SIGNAL('clicked()'),
          self.temelodev4)
      self.connect(self.ui.c, QtCore.SIGNAL('clicked()'),
          self.sil)
      self.connect(self.ui.temizle_2, QtCore.SIGNAL('clicked()'),
          self.sili)
      self.connect(self.ui.hesaplak, QtCore.SIGNAL('clicked()'),
          self.calc)
      self.connect(self.ui.temizlek, QtCore.SIGNAL('clicked()'),
          self.silk)
      self.connect(self.ui.sil_to1, QtCore.SIGNAL('clicked()'),
          self.silp1)
      self.connect(self.ui.sil_to2, QtCore.SIGNAL('clicked()'),
          self.silp2)
      self.connect(self.ui.sil_to3, QtCore.SIGNAL('clicked()'),
          self.silp3)
      self.connect(self.ui.sil_to4, QtCore.SIGNAL('clicked()'),
          self.silp4)
