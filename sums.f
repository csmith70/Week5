      SUBROUTINE  Sums(x, Sum, SumSQR)
      IMPLICIT  NONE
      REAL :: x
      REAL :: Sum, SumSQR
      !character(32): Sum, line, SumSQR

      Sum    = Sum + x
      SumSQR = SumSQR + x*x
      END SUBROUTINE  Sums
