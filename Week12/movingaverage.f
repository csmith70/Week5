       PROGRAM  MovingAverage
       IMPLICIT  NONE
  
       INTEGER, PARAMETER :: MAX_SIZE = 150000       ! array size
       REAL, DIMENSION(1:MAX_SIZE) :: x, Avg     ! arrays
       REAL               :: Sum                 ! for computation use
       INTEGER            :: Window              ! window size
       INTEGER            :: Size                ! actual array size
       INTEGER            :: i, j                ! indices

       READ(*,*)  size, (x(i), i = 1, size)      ! read in input data
       READ(*,*)                      ! read in window value
   
       WRITE(*,*) "**********************************"     ! display input
       WRITE(*,*) "*   Moving Average Computation   *"
       WRITE(*,*) "**********************************"
       WRITE(*,*)
       WRITE(*,*) "Input Array:"
       WRITE(*,*) (x(i), i = 1, 139)
       WRITE(*,*)
       WRITE(*,*) "Window Size = ", Window

       DO i = 1, 139-5+1                   ! for each xi
         Sum = 0.0                              ! compute the moving average
         DO j = i, i+5-1                   ! of xi, x(i+1), ..., 
            Sum = Sum + x(j)                    ! x(i+Window-1).
         END DO
      Avg(i) = Sum / 5                  ! save the result
      END DO
      i = i+1  
      j = j+1

      WRITE(*,*)                                ! display the result
      WRITE(*,*)  "Moving Average of the Given Array:"
      WRITE(*,*)  (Avg(i), i = 1, Size-Window+1)
      END PROGRAM  MovingAverage
