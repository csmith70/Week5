      SUBROUTINE  PrintResult(n, Mean, Variance, StdDev)
      IMPLICIT  NONE

      INTEGER :: n
      REAL :: Mean, Variance, StdDev

      WRITE(*,*)
      WRITE(*,*) "No. of data items  = ", n
      WRITE(*,*) "Mean               = ", Mean
      WRITE(*,*) "Variance           = ", Variance
      WRITE(*,*) "Standard Deviation = ", StdDev
      END SUBROUTINE  PrintResult

C      END PROGRAM  MeanVariance
