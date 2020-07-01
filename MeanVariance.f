      PROGRAM  MeanVariance
      IMPLICIT   NONE
      INTEGER :: Number, IOstatus, rdopst, rdst, i
      REAL    :: Data, Sum, Sum2, n, y, line, varb, b
      REAL    :: Mean, Var, Std, sum34, avg, SumSQR, var2 
      REAL    :: stdev
      character(30) :: rdfile
      !character(32) :: line
      
  
      !Number = 0                           ! initialize the counter
      Sum    = 0.0                         ! initialize accumulators
      Sum2   = 0.0 
      do
      write(*,'(a)', advance="no") "Input File Name: "
      read (*,*) rdfile
      open(12, file=rdfile, status="old", 
     +action="read", position="rewind")
      if (rdopst==0) exit
      end do
      i = 1
      DO
      READ(12,*)line
      write(*,*) line
      !read(*, '(f10.0)') y
      !Read(line,'(f10.0)')y ! read in a value
      IF (rdst < 0)  EXIT
      !i = i+1          ! if end-of-file reached, exit
      !Number = Number + 1               ! no, have one more value
      WRITE(*,*)  "Data item ", i, ": ", line
      sum= sum+line
      b = sum
      mean = sum/i
      !varb = (line-mean)**2  
      varb = varb + line**2
      var2 = (varb - (b**2/i))/(i-1)
      stdev = sqrt(var2)
      !SumSQR = SumSQR + line*line
      !avg = sum34/5
      !Write(*,*)sum
      !write(*,*)line
      !Read(*,'(f10.0)')y
      !close(12)
      CALL  Sums(Data, Sum, Sum2)       ! accumulate the values
      write(*,*) sum
      write(*,*) mean
      write(*,*) var2
      write(*,*) stdev
      i = i+1
      END DO

      CALL  Results(Sum, Sum2, i, Mean, Var, Std)  ! compute results
      !CALL  PrintResult(Number, Mean, Var, Std)         ! display them
      write(*,*)Sum
      END PROGRAM MeanVariance

