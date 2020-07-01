      REAL, DIMENSION(:), ALLOCATABLE:: VAL
      REAL*8 bb
      INTEGER N, I,J, COUNT, CURRENTCOUNT, C
      character (LEN=75) ::Format, dd
      !WRITE(*,*)' WHAT IS THE VALUE FOR N? '
      !READ(*,*) N
      !ALLOCATE(VAL(N))
      !WRITE(*,*) 'ENTER THE NUMBERS'
      OPEN(2,FILE='ozone_fit_regression_input.dat')
      !Read(2,*)bb
      format = "(A, E5.15)"
      do n = 3, 100
      read(2,'(E5.2)')bb
      write(*,*)bb
      end do
      END
