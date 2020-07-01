      PROGRAM MathPractice
!REAL*8 sum,avg,n,input !Define variables with double-precision
      real, dimension(4) :: costs=(/10.0, 15.0, 20.0, 25.0/)
      print*, costs
      a = costs(1) + costs(2)
      do i =2,3
         b = costs(i-1)+costs(i)+costs(i+1)
         av = b/3
         print*,av
      enddo
      !Integer n, numbers
!PRINT *, 'ok'
      !DO n =1, 10
          !print*, n
      !END DO
      !real, dimension(4) :: costs=(/10.0, 15.0, 20.0, 25.0/)
      END PROGRAM MathPractice
      

     
