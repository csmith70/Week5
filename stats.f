      SUBROUTINE  Results(Sum, SumSQR, n, Mean, Variance, StdDev)
      IMPLICIT  NONE

      INTEGER n
      REAL Sum, SumSQR
      REAL Mean, Variance, StdDev

      Mean = Sum / n
      Variance = (SumSQR - Sum*Sum/n)/(n-1)
      StdDev   = SQRT(Variance)
      END SUBROUTINE Results

