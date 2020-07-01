      PROGRAM STATISTICS
        !Created by : Rethnaraj Rambabu
      IMPLICIT NONE

      REAL, DIMENSION(:), ALLOCATABLE:: VAL
      REAL TEMP, MEDIAN, QUARTILE, ev, evensteven
      REAL EVEN, MEAN, SUM, FMODE, third

      INTEGER N, I,J, COUNT, CURRENTCOUNT, C

      WRITE(*,*)' WHAT IS THE VALUE FOR N? '
      READ(*,*) N
      ALLOCATE(VAL(N))

      WRITE(*,*) 'ENTER THE NUMBERS'
      !READ(*,*) C
      OPEN(1,FILE='FILE.txt')
      READ(1,*)(VAL(I),I=1,N)
      CLOSE(1)
      WRITE(*,*) VAL

  !/---FOR SORTING----/!

      DO I=1,N-1
      DO J=1,N-1
      IF(VAL(J) > VAL(J+1)) THEN
      TEMP=VAL(J)
      VAL(J)=VAL(J+1)
      VAL(J+1)=TEMP
      END IF
      END DO
      END DO
  !/---MAE----/!
      
  !/-----MEDIAN----/!

      IF ((N/2*2) /= N) THEN
      MEDIAN=VAL((N+1)/2)
      ELSE IF ((N/2*2) == N) THEN
      EVEN= (VAL(N/2)+VAL((N+2)/2))
      MEDIAN=EVEN/2
      END IF

      WRITE(*,*)'MEDIAN=', MEDIAN

  !/-----25 Percentile----/!
      IF ((N/4*4) /= N) THEN
      QUARTILE = (VAL((N+3)/4)+VAL(N/4))
      QUARTILE = QUARTILE/2
      ELSE IF ((N/4*4) == N) THEN
      ev= (VAL(N/4)+VAL((N+2)/2))
      QUARTILE=ev/2
      END IF
      !quartile=VAL(
      WRITE(*,*)'25th Percentile=',QUARTILE

  !/-----75 Percentile----/!
      IF (((3*N)/4) /= N) THEN
      third =(VAL(((3*N)+2)/4))+VAL((3*N)/4)
      Write(*,*)'hi im',third
      third = third/2
      !ELSE IF ((N/(4/3)*(4/3)) == N) THEN
      !evensteven= (VAL(N/(4/3))+VAL((N+2)/2))
      !third=ev/2
      END IF
      !quartile=VAL(
      WRITE(*,*)'75th Percentile=',third

      
      WRITE(*,*) VAL
      FMODE = VAL(1)
      COUNT = 1
      CURRENTCOUNT = 1
      DO I = 2, N
      ! We are going through the loop looking for values == VAL(I-1)...
      IF (VAL(I) == VAL(I-1)) THEN
        ! We spotted another VAL(I-1), so increment the count.
      CURRENTCOUNT = CURRENTCOUNT + 1
      ELSE
        ! There are no more VAL(I-1)
      IF (CURRENTCOUNT > COUNT) THEN
            ! There were more elements of value VAL(I-1) than of value FMODE
      COUNT = CURRENTCOUNT
      FMODE = VAL(I-1)
      END IF
      ! Next we are looking for values == VAL(I), so far we have spotted one...
      CURRENTCOUNT = 1
      END IF
      END DO
      IF (CURRENTCOUNT > COUNT) THEN
      ! This means there are more elements of value VAL(N) than of value FMODE.
      FMODE = VAL(N)
      END IF
      write(*,*)FMODE
      END 
