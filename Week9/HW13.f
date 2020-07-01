! Christopher Smith
! October 30, 2019
! HW12: FORTRAN Lat and Lon Conversion
      
      PROGRAM third
      IMPLICIT NONE 
      REAL*8 pi, radians, n, input, Lat, Lon, radianLat, radianLon
      parameter (pi = 3.14159)
      integer :: i
      PRINT *, 'The number of locations to find' 
      READ(*,*)n
      DO i = 1, n
	PRINT *, 'Enter latitude'
        READ (*,*) Lat
        PRINT *, 'Enter longitude'
        READ(*,*) Lon
        radianLat = Lat * pi/180 
        radianLon = Lon * pi/180
        PRINT *, radianLat, radianLon
        CONTINUE
      END DO
      ! Number of S.F. needed
      ! 800 km satellite height
      ! Radius of Earth is 6371 km
      !parameter (acc = 0.2)
      !radius = 6371
      !height = 800
      !ans = acc/(radius+height)
      
      
    
      END
