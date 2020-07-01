! Christopher Smith
! Part of HW14: FORTRAN Data Sorting
! 11/04/19

	! Declare variables
        parameter (narray_max=1000000)
        real iarray_in(narray_max),iarray_out(narray_max), i2
        real av(narray_max), j
        integer window
        real :: sum = 0.0
        character(30) :: rdfile, wrfile
        character*80 namein
        character*1 cdum

	! Have the user enter the filename
        write(6,700)
700     format('Enter input filename : ',$)
        read(5,702)namein
702     format(A)
        call charlen(namein,80,len_namein)

       open(1, file=rdfile, status="old", 
     +action="read", position="rewind")
C        read(1,710)icol,ihead
C710     format(I,I)
C        read(1,702)cdum
C        read(1,702)cdum

	!Read the file and input points into array iarray_in 
        icount=1
100     continue
        read(1,*,end=102,err=802)i1,i2
        iarray_in(icount)=i2
        icount=icount+1
        goto 100
        write(*,*)i2

102     continue        
        npts=icount-1
        write(*,*)npts

C        write(99,790)namein(1:len_namein)
C790     format('2,3',/,'Sequence,Integer Value',/,
C     +  'Sorted data read from file ',A)

	!Read the number of points in the file to the screen
        write(6,708)npts,namein(1:len_namein)
708     format('Read ',I7,' points from file ',A)

!        call piksrt(iarray_in,iarray_out,npts)

        !call heapsort(iarray_in,iarray_out,npts)
          
                 ! compute the moving average:Practice
         !DO i=1, npts-5+1              !for each xi
         !DO j=i, i+5-1                 ! of xi, x(i+1), ...,
           ! Sum = Sum + iarray_in(j)  ! x(i+Window-1).
         ! END DO
         ! av(i) = Sum/5
         !END DO
        
        ! Write to fort.99 original data   
        do i=1,npts
           write(99,799)i,iarray_in(i)
           write(*,*)iarray_in(i)
        enddo
799     format(I6,3X,f7.2)  
        write(*,*)'Output written to unit 99'
        !Write running mean to fort.98
        do i = 3, npts-5+2
           sum = iarray_in(i-2)+iarray_in(i-1)+
     +     iarray_in(i) + iarray_in(i+1)+
     +     iarray_in(i+2)
           av=sum/5
           write(98,799)i+1879,av(i)
        enddo
      
       

        goto 999

800     write(6,801)namein(1:len_namein)
801     format('Can not open input file ',A,' : Program Stop')
        goto 999
802     write(6,803)namein(1:len_namein)
803     format('File read error file ',A,'  : Program Stop')
        write(*,*)i2

999     continue

        stop
        end


        subroutine charlen(char,nchar,ilen)
C      
C       Input: char, nchar
C       Output: ilen
C
C          ilen records place of first blank character
C          i.e., length of character string
C
        character*(*) char
        character*1 cc,blnK
        data blnk/' '/
        do ilen=nchar,1,-1
           cc=char(ilen:ilen)
           if(cc.ne.blnk) goto 100
        enddo
100     continue
        return
        end

