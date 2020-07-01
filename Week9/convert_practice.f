      PROGRAM CONVERT PRACTICE
      IMPLICIT NONE
      REAL*8 lat, lon, latrad, lonrad
      REAL:: pi = 3.141592
      write(*,*)"Enter the latitude of location #1"
      read*, lat
      write(*,*)"Enter the longitude of location #1"
      read*, lon
C     Convert lat,lon to radians
      latrad = lat*(pi/180)
      lonrad = lon*(pi/180)
706   format(f7.5)
      write(*,706)latrad
      write(*,706)lonrad
      END
     
