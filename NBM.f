      PROGRAM  MeanVariance
      IMPLICIT   NONE
      INTEGER :: Number, IOstatus, rdopst, rdst, i, line2
      REAL    :: Data, Sum, Sum2, n, y!line, varb, b
      REAL    :: Mean, Var, Std, sum34, avg, SumSQR, var2 
      REAL    :: stdev
      character(30) :: rdfile, line5
      character(72) :: line
      TYPE :: wx
      Character(4):: letter
      Integer :: num
      Integer :: num2
      Integer :: num3
      Integer :: num4
      Integer :: num5
      Integer :: num6
      END Type wx
      type(wx),dimension(1)::wxrep

      !TYPE :: cities
      !Character(64):: names
      !END TYPE cities
      !type(cities),dimension(1)::citiesrep

      do
      write(*,'(a)', advance="no") "Input File Name: "
      read (*,*) rdfile
      open(12, file=rdfile, status="old", 
     +action="read", position="rewind")
      if (rdopst==0) exit
      end do
      i =1
      do i=1,2
      read(12,10)line
   10 FORMAT(A)
      write(*,*)line
      end do
      
      i = 1
      do i =1,2
      read(12,*)wxrep
      write(*,*)wxrep
      end do
      END PROGRAM
