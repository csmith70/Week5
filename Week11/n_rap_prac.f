      PROGRAM Newton
      INTEGER JMAX
      REAL rtnewt, x1, x2, xacc
      EXTERNAL func01_aosc652
      call rtnewt(func01_aosc652, x1, x2, xacc)
      PARAMETER(JMAX=20)
      INTEGER j
      REAL df, dx, f
      rtnewt=.5*(x1+x2)
      DO j=1,JMAX
      	call funcd(rtnewt,f,df)
      END DO
      END

