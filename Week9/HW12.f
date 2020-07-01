! Christopher Smith
! HW12: FORTRAN AVERAGE
! October 25, 2019
      PROGRAM first
      REAL*8 sum,avg,input !Define variables with double-precision
      Integer n
      PRINT *, 'Enter number of values to be averaged' !Asks user to input #of grades
      READ(*,*)n !Reads the value using defaul unit and unformatted read, stores in variable n
      sum = 0
!While the number of grades is < n, have user enter value of each grade and compute sum
      DO NUMBER = 1, n 
	   PRINT *, 'Enter value'
           READ (*,*) input
           sum = sum + input
      END DO
!Calculate average and write to screen 
      avg = real(sum) / real(n)
      WRITE(12,*) "Average =",avg
      END PROGRAM first !End program
    

