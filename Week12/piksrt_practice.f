      PROGRAM xpiksrt
C      driver for routine piksrt
      INTEGER i,j
      REAL a(100)
      open(11, file='random_integers_1_100.dat',status='OLD')
      read(11,*) (a(i),i=1,100)
      close(11)
C     print original array
      write(*,*)'Original array:'
      DO 11 i=1,10
     	write(*,'(1x,10f7.2)')(a(10*(i-1)+j),j=1,10)
11    continue
C     sort array
      call piksrt(100, a)
C     print sorted array
      write(*,*)'Sorted araray:'
      DO 12 i=1,10
      	write(*,'(1x,10f7.2)')(a(10*(i-1)+j),j=1,10)
12    continue
      END

